#!/usr/bin/env python3
"""Create only eight immutable lightweight DAG-retention tag refs; never delete a ref.

Run only on a reviewed main push. All remote state is rechecked immediately before
the push. The manifest remains PROPOSAL_ONLY and never authorizes branch deletion.
"""
import argparse
import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

REPO = "EAKerber/MobiliPresenter2D_DesignSystem"
RULESET_ID = 25953910
# Owner-capable GitHub API confirmed bypass_actors=[] at this exact revision.
# GitHub Actions GITHUB_TOKEN has no ruleset-write permission and receives null
# for this protected field (documented API behavior). Timestamp pins the owner's
# independent attestation; any edit to the ruleset blocks publication.
OWNER_VERIFIED_RULE_UPDATED_AT = "2026-10-27T08:49:23.055-03:00"
PREFIX = "refs/tags/ds-history/2026-10-27/"
PATTERN = PREFIX + "*"
OPS = "maintenance/ds-pr41-runtime-evidence-extract-20261026"
MANIFEST = Path("docs/DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json")
SHA = re.compile(r"[0-9a-f]{40}\Z")


def git(*args):
    return subprocess.run(["git", *args], check=True, text=True, capture_output=True).stdout.strip()


def gh(path):
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/repos/" + REPO + path,
        headers={"Authorization": "Bearer " + token,
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def remote_refs(kind, pattern=None):
    args = ["ls-remote", "--refs", "--" + kind, "origin"]
    if pattern:
        args.append(pattern)
    refs = {}
    for line in git(*args).splitlines():
        sha, name = line.split("\t")
        if name in refs:
            raise ValueError("DUPLICATE_REMOTE_REF")
        refs[name] = sha
    return refs


def validate(manifest, branches, tags, rule, open_prs, main_sha):
    if (manifest.get("schemaVersion") != "DSHistoricalDAGRetentionProposal/0.1"
            or manifest.get("repository") != REPO
            or manifest.get("controlBranch") != "main"
            or manifest.get("status") != "PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE"
            or manifest.get("tagNamespace") != PREFIX
            or manifest.get("tagStyle") != "lightweight-commit-ref-exact-SHA"):
        raise ValueError("BAD_MANIFEST_OR_UNAUTHORIZED_MODE")
    if (rule.get("id") != RULESET_ID or rule.get("target") != "tag"
            or rule.get("enforcement") != "active"
            or rule.get("source") != REPO
            or rule.get("bypass_actors") not in ([], None)
            or rule.get("updated_at") != OWNER_VERIFIED_RULE_UPDATED_AT
            or rule.get("current_user_can_bypass") != "never"
            or rule.get("conditions", {}).get("ref_name") !=
            {"exclude": [], "include": [PATTERN]}
            or not {"deletion", "update"}.issubset(
                {r.get("type") for r in rule.get("rules", [])})):
        raise ValueError("TAG_PROTECTION_NOT_VERIFIED")
    if open_prs:
        raise ValueError("OPEN_PULL_REQUEST")
    if branches.get("refs/heads/main") != main_sha or not SHA.fullmatch(main_sha):
        raise ValueError("MAIN_HEAD_DRIFT")
    if OPS not in [b.removeprefix("refs/heads/") for b in branches]:
        raise ValueError("MISSING_OPERATIONAL_HEAD")
    rows = manifest.get("candidates", [])
    if not isinstance(rows, list) or len(rows) != 8:
        raise ValueError("EXPECTED_EXACTLY_EIGHT_HOLDS")
    if set(branches) != {"refs/heads/main", "refs/heads/" + OPS} | {
        "refs/heads/" + c["branch"] for c in rows}:
        raise ValueError("UNEXPECTED_BRANCH_INVENTORY")
    names = set()
    missing = []
    for c in rows:
        name, sha, tag = c["branch"], c["sha"], c["tag"]
        if (not SHA.fullmatch(sha)
                or name == "main" or name == OPS
                or tag != PREFIX + name.replace("/", "--") + "-" + sha[:12]
                or name in names
                or branches.get("refs/heads/" + name) != sha):
            raise ValueError("HOLD_HEAD_DRIFT_OR_BAD_TAG")
        names.add(name)
        existing = tags.get(tag)
        if existing is None:
            missing.append((sha, tag))
        elif existing != sha:
            raise ValueError("ARCHIVE_TAG_DRIFT")
    if set(tags) != {c["tag"] for c in rows if c["tag"] in tags}:
        raise ValueError("UNEXPECTED_ARCHIVE_TAG")
    return missing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", required=True)
    args = parser.parse_args()
    if not args.apply or os.environ.get("GITHUB_REPOSITORY") != REPO:
        raise ValueError("REQUIRES_AUTHORIZED_MAIN_WORKFLOW")
    expected_main = os.environ.get("GITHUB_SHA", "")
    if os.environ.get("GITHUB_REF") != "refs/heads/main":
        raise ValueError("NOT_MAIN")
    manifest = json.loads(MANIFEST.read_text())
    branches = remote_refs("heads")
    tags = remote_refs("tags", PREFIX + "*")
    rule = gh("/rulesets/" + str(RULESET_ID))
    prs = gh("/pulls?state=open&per_page=100")
    missing = validate(manifest, branches, tags, rule, prs, expected_main)
    for c in manifest["candidates"]:
        sha = c["sha"]
        if git("cat-file", "-t", sha) != "commit":
            raise ValueError("NOT_A_GIT_COMMIT")
        if not git("rev-list", "--count", sha).isdigit():
            raise ValueError("INCOMPLETE_COMMIT_GRAPH")
    print("PREFLIGHT_PASS missing=" + str(len(missing)), flush=True)
    if missing:
        # No force, no branch updates and no deletions. All refs are fixed SHA tags.
        specs = [sha + ":" + tag for sha, tag in missing]
        subprocess.run(["git", "push", "origin", *specs], check=True)
    readback = remote_refs("tags", PREFIX + "*")
    if len(readback) != 8 or any(readback.get(c["tag"]) != c["sha"] for c in manifest["candidates"]):
        raise ValueError("POST_PUSH_READBACK_FAILED")
    for c in manifest["candidates"]:
        tagref = gh("/git/ref/tags/" + c["tag"].removeprefix("refs/tags/"))
        if tagref.get("object", {}).get("sha") != c["sha"] or tagref.get("object", {}).get("type") != "commit":
            raise ValueError("GITHUB_API_TAG_READBACK_FAILED")
    if gh("/rulesets/" + str(RULESET_ID)) != rule:
        raise ValueError("PROTECTION_CHANGED_DURING_EXECUTION")
    report = {"schemaVersion": "DSDAGRetentionExecution/0.1",
              "repository": REPO, "mainSha": expected_main, "rulesetId": RULESET_ID,
              "tags": [{"ref": c["tag"], "sha": c["sha"]} for c in manifest["candidates"]],
              "createdCount": len(missing), "readbackCount": 8,
              "branchDeletionAuthorized": False, "branchDeletionCount": 0}
    Path("ds-dag-retention-receipt.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
