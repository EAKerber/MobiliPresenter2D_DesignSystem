#!/usr/bin/env python3
"""Retire a small, explicitly pinned batch of GitHub branches, fail-closed.

Only run in GitHub Actions on main pushes of the batch manifest. No gh dependency.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen


def run(*args):
    return subprocess.run(args, text=True, capture_output=True, check=True).stdout.strip()


def api(repo, endpoint):
    req = Request(f"https://api.github.com/repos/{repo}/{endpoint}", headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "m2d-bounded-branch-retirement",
    })
    with urlopen(req, timeout=20) as response:
        return json.load(response)


def remote_refs():
    result = {}
    for line in run("git", "ls-remote", "--heads", "origin").splitlines():
        sha, ref = line.split("\t", 1)
        result[ref.removeprefix("refs/heads/")] = sha
    return result


def observe(repo):
    refs = remote_refs()
    branches = api(repo, "branches?per_page=100")
    prs = api(repo, "pulls?state=open&per_page=100")
    if not isinstance(branches, list) or not isinstance(prs, list) or len(branches) >= 100 or len(prs) >= 100:
        raise RuntimeError("PAGINATION_UNVERIFIED")
    by_name = {b["name"]: b for b in branches}
    if len(by_name) != len(branches) or set(refs) != set(by_name):
        raise RuntimeError("BRANCH_INVENTORY_MISMATCH")
    for name, sha in refs.items():
        if by_name[name]["commit"]["sha"] != sha:
            raise RuntimeError("BRANCH_SHA_MISMATCH:" + name)
    protected = {name for name, b in by_name.items() if b.get("protected")}
    in_pr = set()
    for pr in prs:
        head, base = pr.get("head") or {}, pr.get("base") or {}
        if (head.get("repo") or {}).get("full_name") == repo:
            in_pr.add(head.get("ref"))
        in_pr.add(base.get("ref"))
    return refs, protected, in_pr



def verify_squash(repo, entry, control):
    """Verify one explicitly pinned, fully identical squash merge (fail-closed).

    This is NOT an inferred equivalence or a request to delete other refs.
    All PR metadata is obtained live and all commit/tree facts are read from Git.
    """
    proof = entry.get("squashMerge")
    if proof is None:
        return None
    if (not isinstance(proof, dict)
            or set(proof) != {"pullRequest", "mergeCommit"}
            or type(proof["pullRequest"]) is not int
            or proof["pullRequest"] <= 0
            or not isinstance(proof["mergeCommit"], str)
            or not re.fullmatch(r"[0-9a-f]{40}", proof["mergeCommit"])):
        raise RuntimeError("INVALID_SQUASH_PROOF")

    name, expected = entry["branch"], entry["sha"]
    pr_number, merge = proof["pullRequest"], proof["mergeCommit"]
    pr = api(repo, f"pulls/{pr_number}")
    head, base = pr.get("head") or {}, pr.get("base") or {}
    if (pr.get("state") != "closed" or not pr.get("merged_at")
            or pr.get("merge_commit_sha") != merge
            or head.get("ref") != name or head.get("sha") != expected
            or (head.get("repo") or {}).get("full_name") != repo
            or base.get("ref") != "main"
            or (base.get("repo") or {}).get("full_name") != repo):
        raise RuntimeError("SQUASH_PR_IDENTITY_MISMATCH:" + name)

    parents = run("git", "rev-list", "--parents", "-n", "1", merge).split()
    if len(parents) != 2 or parents[0] != merge:
        raise RuntimeError("SQUASH_MERGE_NOT_SINGLE_PARENT:" + name)
    if (subprocess.run(["git", "merge-base", "--is-ancestor", merge, control],
                       check=False).returncode != 0
            or subprocess.run(["git", "merge-base", "--is-ancestor",
                               parents[1], expected], check=False).returncode != 0):
        raise RuntimeError("SQUASH_ANCESTRY_NOT_PROVEN:" + name)

    head_tree = run("git", "show", "-s", "--format=%T", expected)
    merge_tree = run("git", "show", "-s", "--format=%T", merge)
    if not re.fullmatch(r"[0-9a-f]{40}", head_tree) or head_tree != merge_tree:
        raise RuntimeError("SQUASH_FULL_TREE_MISMATCH:" + name)

    # Read named workflow references from origin/main (not the PR's working tree).
    # Block even when the branch has been fully integrated.
    grep = subprocess.run(
        ["git", "grep", "-l", "-F", "-e", name,
         "origin/main", "--", ".github/workflows"],
        text=True, capture_output=True, check=False,
    )
    if grep.returncode == 0:
        raise RuntimeError("SQUASH_ACTIVE_WORKFLOW_REF:" + name)
    if grep.returncode != 1:
        raise RuntimeError("SQUASH_WORKFLOW_LOOKUP_FAILED:" + name)
    return {
        "branch": name, "sha": expected, "pullRequest": pr_number,
        "mergeCommit": merge, "treeSha": head_tree, "mainSha": control,
        "proof": "MERGED_SQUASH_IDENTICAL_FULL_TREE",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(Path(args.batch).read_text())
    repo = os.environ["GITHUB_REPOSITORY"]
    sha = os.environ["GITHUB_SHA"]
    if manifest.get("schema") != "BoundedBranchRetirement 0.1" or manifest.get("repository") != repo:
        raise RuntimeError("BAD_BATCH_IDENTITY")
    entries = manifest.get("branches")
    if not isinstance(entries, list) or not (1 <= len(entries) <= 3):
        raise RuntimeError("BATCH_LIMIT_1_TO_3")
    names = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise RuntimeError("INVALID_ENTRY")
        name, expected = entry.get("branch"), entry.get("sha")
        if not isinstance(name, str) or not isinstance(expected, str):
            raise RuntimeError("INVALID_PINNED_REF")
        if (name == "main" or not re.fullmatch(r"[a-zA-Z0-9._/-]+", name)
                or name.startswith("-") or ".." in name or "//" in name
                or not re.fullmatch(r"[0-9a-f]{40}", expected) or name in names):
            raise RuntimeError("INVALID_PINNED_REF")
        names.add(name)
    if args.apply and (os.environ.get("GITHUB_EVENT_NAME") != "push" or os.environ.get("GITHUB_REF") != "refs/heads/main"):
        raise RuntimeError("APPLY_REQUIRES_MAIN_PUSH")
    if run("git", "rev-parse", "HEAD") != sha:
        raise RuntimeError("CHECKOUT_SHA_MISMATCH")
    run("git", "fetch", "--no-tags", "origin", "+refs/heads/*:refs/remotes/origin/*")
    original, protected, in_pr = observe(repo)
    if original.get("main") != sha:
        if args.apply:
            raise RuntimeError("MAIN_HEAD_DRIFT")
        # pull_request checks out a merge ref; compare against the remote main instead
        if os.environ.get("GITHUB_EVENT_NAME") != "pull_request":
            raise RuntimeError("UNEXPECTED_HEAD")
    control = original["main"]
    squash_proofs = []
    for entry in entries:
        name, expected = entry["branch"], entry["sha"]
        if original.get(name) != expected or name in protected or name in in_pr:
            raise RuntimeError("PRECHECK_REF_PROTECTED_OR_CHANGED:" + name)
        is_ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", expected, control], check=False)
        proof = verify_squash(repo, entry, control)
        if is_ancestor.returncode != 0 and proof is None:
            raise RuntimeError("UNMERGED_CONTENT:" + name)
        if proof is not None:
            squash_proofs.append(proof)
    receipt = {"repository": repo, "batch": Path(args.batch).name, "main": control,
               "approvedPins": entries, "squashProofs": squash_proofs,
               "deleted": [], "mode": "apply" if args.apply else "audit"}
    def save():
        Path("/tmp/branch-retirement-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    if args.apply:
        expected_inventory = original.copy()
        for entry in entries:
            name, expected = entry["branch"], entry["sha"]
            current, now_protected, now_pr = observe(repo)
            if current != expected_inventory or current.get("main") != control or name in now_protected or name in now_pr:
                raise RuntimeError("CONCURRENT_CHANGE_ABORT:" + name)
            # The same historical identity/tree check must still hold at mutation.
            # For ancestors, recheck ancestry as well instead of trusting the audit.
            proof = verify_squash(repo, entry, control)
            if proof is None and subprocess.run(
                ["git", "merge-base", "--is-ancestor", expected, control],
                check=False
            ).returncode != 0:
                raise RuntimeError("ANCESTRY_DRIFT:" + name)
            run("git", "push", f"--force-with-lease=refs/heads/{name}:{expected}", "origin", f":refs/heads/{name}")
            expected_inventory.pop(name)
            # GitHub REST may briefly lag the Git ref service after deletion.
            for attempt in range(4):
                try:
                    readback, _, _ = observe(repo)
                    if readback == expected_inventory:
                        break
                except RuntimeError:
                    pass
                if attempt < 3:
                    time.sleep(2)
            else:
                raise RuntimeError("READBACK_MISMATCH:" + name)
            receipt["deleted"].append({"branch": name, "sha": expected})
            save()
    receipt["status"] = "PASS"
    save()
    print(json.dumps({"status": "PASS", "mode": receipt["mode"], "count": len(receipt["deleted"]), "batch": receipt["batch"]}))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("RETIREMENT_ABORT:", error, file=sys.stderr)
        raise