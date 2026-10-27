#!/usr/bin/env python3
"""Read-only verifier for candidate history-retention tag refs.

Does NOT create tags, adjust branch-dispositions, authorize or delete branches.
Uses exact SHA identity and a previously captured fresh branch observation.
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
from pathlib import Path

SHA = re.compile(r"^[0-9a-f]{40}$")
NAMESPACE = "refs/tags/ds-history/2026-10-27/"


def evaluate(manifest: dict, observation: dict, remote_tags: dict[str, str]) -> dict:
    """Return a fail-closed read-only report. Never qualifies a branch for deletion."""
    if (manifest.get("schemaVersion") != "DSHistoricalDAGRetentionProposal/0.1"
            or manifest.get("status") != "PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE"
            or observation.get("schemaVersion") != "BranchObservation 0.1"
            or observation.get("complete") is not True
            or observation.get("repository") != manifest.get("repository")
            or observation.get("controlBranch") != "main"
            or manifest.get("tagNamespace") != NAMESPACE
            or manifest.get("tagStyle") != "lightweight-commit-ref-exact-SHA"):
        raise ValueError("UNTRUSTED_MANIFEST_OR_OBSERVATION")
    candidates = manifest.get("candidates")
    if not isinstance(candidates, list) or len(candidates) != 8:
        raise ValueError("EXPECTED_EIGHT_CANDIDATES")
    live = {item["name"]: item["sha"] for item in observation["branches"]}
    if len(live) != len(observation["branches"]):
        raise ValueError("DUPLICATE_LIVE_BRANCHES")
    if live.get("main") != observation.get("controlSha"):
        raise ValueError("CONTROL_SHA_MISMATCH")
    heads = set(observation.get("openPrHeads", []))
    bases = set(observation.get("openPrBases", []))
    seen_names: set[str] = set()
    seen_tags: set[str] = set()
    rows = []
    for item in candidates:
        name, sha, tag = item.get("branch"), item.get("sha"), item.get("tag")
        if (not isinstance(name, str) or name == "main"
                or not isinstance(sha, str) or not SHA.fullmatch(sha)
                or not isinstance(tag, str) or not tag.startswith(NAMESPACE)
                or not re.fullmatch(r"refs/tags/ds-history/2026-10-27/[a-zA-Z0-9._-]+-[0-9a-f]{12}", tag)
                or name in seen_names or tag in seen_tags):
            raise ValueError("INVALID_OR_DUPLICATE_PIN")
        expected_tag = NAMESPACE + name.replace("/", "--") + "-" + sha[:12]
        if tag != expected_tag:
            raise ValueError("TAG_IDENTITY_NOT_CANONICAL")
        seen_names.add(name); seen_tags.add(tag)
        live_sha = live.get(name)
        tag_sha = remote_tags.get(tag)
        if live_sha != sha:
            state = "BRANCH_HEAD_DRIFT"
        elif name in heads or name in bases:
            state = "OPEN_PR_DEPENDENCY"
        elif tag_sha is None:
            state = "NO_TAG_YET"
        elif tag_sha != sha:
            state = "TAG_SHA_MISMATCH_OR_ANNOTATED_TAG"
        else:
            state = "EXACT_TAG_POINTER_PRESENT"
        rows.append({"branch": name, "sha": sha, "tag": tag,
                     "remoteTagSha": tag_sha, "status": state})
    extras = sorted(tag for tag in remote_tags if tag.startswith(NAMESPACE) and tag not in seen_tags)
    if extras:
        raise ValueError("UNEXPECTED_TAGS_IN_ARCHIVE_NAMESPACE")
    return {
        "schemaVersion": "DSDAGRetentionAudit/0.1",
        "mode": "audit-only",
        "repository": manifest["repository"],
        "controlSha": observation["controlSha"],
        "readbackCount": sum(x["status"] == "EXACT_TAG_POINTER_PRESENT" for x in rows),
        "pendingCount": sum(x["status"] == "NO_TAG_YET" for x in rows),
        "blockedCount": sum(x["status"] not in ("EXACT_TAG_POINTER_PRESENT", "NO_TAG_YET") for x in rows),
        "status": ("TAGS_PRESENT_NOT_DELETE_AUTHORIZATION"
                   if all(x["status"] == "EXACT_TAG_POINTER_PRESENT" for x in rows)
                   else "INCOMPLETE_OR_BLOCKED"),
        "branchDeletionAuthorized": False,
        "tagRuleSetProtectionVerified": False,
        "entries": rows
    }


def read_remote_tags() -> dict[str, str]:
    proc = subprocess.run(
        ["git", "ls-remote", "--refs", "--tags", "origin", "refs/tags/ds-history/2026-10-27/*"],
        text=True, capture_output=True, check=True
    )
    refs = {}
    for line in proc.stdout.splitlines():
        sha, ref = line.split("\t", 1)
        if ref in refs:
            raise ValueError("DUPLICATE_REMOTE_TAG")
        refs[ref] = sha
    return refs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--observation", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    with args.manifest.open(encoding="utf-8") as f:
        manifest = json.load(f)
    with args.observation.open(encoding="utf-8") as f:
        observation = json.load(f)
    report = evaluate(manifest, observation, read_remote_tags())
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0 if report["blockedCount"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
