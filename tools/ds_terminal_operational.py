#!/usr/bin/env python3
"""One-shot removal of the final integrated operational branch.

The SHA cannot be recorded in its own PR. Verify that the second parent of
the actual, fully merged main commit is exactly the source HEAD of a pinned
merged PR and exactly the current remote branch ref; never guess an SHA.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

from branch_hygiene_observe import api_get
from ds_dag_tag_retain import (
    PREFIX, REPO, OPS, RULESET_ID, MANIFEST, same_verified_ruleset_revision
)

SHA = re.compile(r"[0-9a-f]{40}\Z")
CONFIG = Path("ops/ds-last-branch-retirement.json")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout.strip()


def refs(kind, pattern=None):
    args = ["ls-remote", "--refs", "--" + kind, "origin"]
    if pattern:
        args.append(pattern)
    out = {}
    for line in git(*args).splitlines():
        sha, ref = line.split("\t", 1)
        if ref in out:
            raise RuntimeError("DUPLICATE_REMOTE_REF")
        out[ref] = sha
    return out


def terminal_gate(cfg, main_sha, parents, live_branches, pr, open_prs, protected,
                  remote_tags, tag_manifest, rule, has_workflow_dependency):
    if (cfg.get("schemaVersion") != "DSOperationalBranchFinalRetirement/0.1"
            or cfg.get("repository") != REPO
            or cfg.get("branch") != OPS
            or cfg.get("mode") != "MERGE_SECOND_PARENT_EXACT_MAIN"
            or type(cfg.get("pullRequest")) is not int
            or cfg["pullRequest"] < 1):
        raise RuntimeError("UNTRUSTED_TERMINAL_MANIFEST")
    if not SHA.fullmatch(main_sha) or len(parents) != 3 or parents[0] != main_sha:
        raise RuntimeError("REQUIRE_TRUE_TWO_PARENT_MERGE")
    source_sha = parents[2]
    if not SHA.fullmatch(source_sha) or not SHA.fullmatch(parents[1]):
        raise RuntimeError("BAD_PARENT_SHA")
    if live_branches != {"refs/heads/main": main_sha, "refs/heads/" + OPS: source_sha}:
        raise RuntimeError("EXACT_FINAL_TWO_REFS_REQUIRED")
    head, base = pr.get("head") or {}, pr.get("base") or {}
    if (pr.get("number") != cfg["pullRequest"]
            or pr.get("state") != "closed" or not pr.get("merged_at")
            or pr.get("merge_commit_sha") != main_sha
            or head.get("ref") != OPS or head.get("sha") != source_sha
            or (head.get("repo") or {}).get("full_name") != REPO
            or base.get("ref") != "main"
            or (base.get("repo") or {}).get("full_name") != REPO):
        raise RuntimeError("MERGED_PR_SECOND_PARENT_NOT_ATTESTED")
    if open_prs:
        raise RuntimeError("OPEN_PULL_REQUEST_EXISTS")
    if protected is not False or has_workflow_dependency:
        raise RuntimeError("PROTECTED_OR_WORKFLOW_DEPENDENCY")
    if (rule.get("id") != RULESET_ID or rule.get("target") != "tag"
            or rule.get("enforcement") != "active"
            or rule.get("source") != REPO
            or rule.get("conditions", {}).get("ref_name") !=
                {"exclude": [], "include": [PREFIX + "*"]}
            or rule.get("bypass_actors") not in ([], None)
            or rule.get("current_user_can_bypass") != "never"
            or not same_verified_ruleset_revision(rule.get("updated_at"))
            or not {"update", "deletion"}.issubset({x.get("type") for x in rule.get("rules", [])})):
        raise RuntimeError("HISTORICAL_TAG_PROTECTION_CHANGED")
    candidates = tag_manifest.get("candidates")
    if (tag_manifest.get("schemaVersion") != "DSHistoricalDAGRetentionProposal/0.1"
            or tag_manifest.get("status") != "PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE"
            or not isinstance(candidates, list) or len(candidates) != 8
            or remote_tags != {c["tag"]: c["sha"] for c in candidates}):
        raise RuntimeError("HISTORICAL_TAG_REFERENCES_INCOMPLETE")
    return source_sha


def main():
    if (os.environ.get("GITHUB_REPOSITORY") != REPO
            or os.environ.get("GITHUB_EVENT_NAME") != "push"
            or os.environ.get("GITHUB_REF") != "refs/heads/main"):
        raise RuntimeError("REQUIRES_MAIN_MERGE_PUSH")
    main_sha = os.environ.get("GITHUB_SHA", "")
    if git("rev-parse", "HEAD") != main_sha:
        raise RuntimeError("CHECKOUT_MAIN_SHA_MISMATCH")
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    tag_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    batch = json.loads(Path("ops/branch-hygiene-batch.json").read_text(encoding="utf-8"))
    dispositions = json.loads(Path("ops/branch-dispositions.json").read_text(encoding="utf-8"))
    if (batch.get("wave") != "DS-HYG-P16-2026-10-27"
            or len(dispositions.get("terminalBranches", [])) != 8
            or dispositions.get("preserveBranches") != []):
        raise RuntimeError("FINAL_HOLD_BATCH_NOT_CONFIRMED")
    token = os.environ["GITHUB_TOKEN"]
    parent_words = git("rev-list", "--parents", "-n", "1", main_sha).split()
    pr = api_get(REPO, f"pulls/{cfg['pullRequest']}", token)
    open_prs = api_get(REPO, "pulls?state=open&per_page=100", token)
    live_branches = refs("heads")
    tags = refs("tags", PREFIX + "*")
    rule = api_get(REPO, f"rulesets/{RULESET_ID}", token)
    info = api_get(REPO, "branches/" + OPS, token)
    workflow_dir = Path(".github/workflows")
    has_dependency = any(
        OPS in p.read_text(encoding="utf-8") for pat in ("*.yml", "*.yaml")
        for p in workflow_dir.glob(pat)
    )
    source_sha = terminal_gate(cfg, main_sha, parent_words, live_branches,
                               pr, open_prs, info.get("protected"), tags,
                               tag_manifest, rule, has_dependency)
    if git("cat-file", "-t", source_sha) != "commit":
        raise RuntimeError("SOURCE_HEAD_NOT_COMMIT")
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", source_sha, main_sha],
                              check=False).returncode == 0
    if not ancestor or git("rev-parse", main_sha + "^2") != source_sha:
        raise RuntimeError("SECOND_PARENT_NOT_MAIN_ANCESTOR")
    # No external state changes until all immutable/read-only gates passed.
    if refs("heads") != live_branches or refs("tags", PREFIX + "*") != tags:
        raise RuntimeError("REF_DRIFT_PRE_DELETE")
    if api_get(REPO, "pulls?state=open&per_page=100", token):
        raise RuntimeError("NEW_OPEN_PR")
    if api_get(REPO, f"rulesets/{RULESET_ID}", token) != rule:
        raise RuntimeError("TAG_PROTECTION_DRIFT")
    print("TERMINAL_GATE_PASS", source_sha, flush=True)
    subprocess.run([
        "git", "push", "origin",
        "--force-with-lease=refs/heads/" + OPS + ":" + source_sha,
        ":refs/heads/" + OPS,
    ], check=True)
    if refs("heads") != {"refs/heads/main": main_sha}:
        raise RuntimeError("FINAL_BRANCH_READBACK_FAILED")
    if refs("tags", PREFIX + "*") != tags:
        raise RuntimeError("HISTORICAL_TAG_READBACK_FAILED")
    receipt = {
        "schemaVersion": "DSFinalOperationalRetirement/0.1", "mode": "APPLY",
        "repository": REPO, "mainSha": main_sha, "pullRequest": cfg["pullRequest"],
        "mergeFirstParent": parent_words[1], "mergeSecondParent": source_sha,
        "deletedBranch": OPS, "deletedSha": source_sha, "remainingBranches": ["main"],
        "protectedTagCount": len(tags), "branchDeletionCount": 1,
        "readback": "PASS", "status": "PASS"}
    Path("ds-last-branch-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
