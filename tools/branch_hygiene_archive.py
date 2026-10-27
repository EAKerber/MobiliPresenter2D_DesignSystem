#!/usr/bin/env python3
"""Fail-closed proof of exact SHA Git DAG retention behind a protected lightweight tag.

This verifier never creates, updates, or deletes Git refs; caller alone controls
batch selection, open-PR checks, leases, and deletion/readback.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from branch_hygiene_observe import api_get
from ds_dag_tag_retain import (
    PREFIX, REPO, RULESET_ID, MANIFEST, OWNER_VERIFIED_RULE_UPDATED_AT,
    same_verified_ruleset_revision,
)

SHA = re.compile(r"[0-9a-f]{40}\Z")
RULESET_PATTERN = PREFIX + "*"


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], capture_output=True,
                            text=True, check=True)
    return result.stdout.strip()


def verify_protected_archive(repository: str, token: str, entry: dict) -> dict | None:
    tag = entry.get("protectedArchiveTag")
    if tag is None:
        return None
    branch, sha = entry.get("branch"), entry.get("sha")
    if repository != REPO or not isinstance(branch, str) or not isinstance(sha, str) or not SHA.fullmatch(sha):
        raise RuntimeError("ARCHIVE_IDENTITY_INVALID")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    candidates = manifest.get("candidates")
    if (manifest.get("schemaVersion") != "DSHistoricalDAGRetentionProposal/0.1"
            or manifest.get("status") != "PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE"
            or manifest.get("repository") != REPO
            or manifest.get("tagNamespace") != PREFIX
            or not isinstance(candidates, list) or len(candidates) != 8):
        raise RuntimeError("ARCHIVE_MANIFEST_INVALID")
    matches = [x for x in candidates if x.get("branch") == branch and
               x.get("sha") == sha and x.get("tag") == tag]
    if len(matches) != 1 or tag != PREFIX + branch.replace("/", "--") + "-" + sha[:12]:
        raise RuntimeError("ARCHIVE_NOT_EXACT_MANIFEST_PIN")
    rule = api_get(repository, f"rulesets/{RULESET_ID}", token)
    if (rule.get("id") != RULESET_ID or rule.get("target") != "tag"
            or rule.get("source") != REPO or rule.get("enforcement") != "active"
            or rule.get("conditions", {}).get("ref_name") !=
                {"exclude": [], "include": [RULESET_PATTERN]}
            or not {"update", "deletion"}.issubset({r.get("type") for r in rule.get("rules", [])})
            or rule.get("bypass_actors") not in ([], None)
            or rule.get("current_user_can_bypass") != "never"
            or not same_verified_ruleset_revision(rule.get("updated_at"))):
        raise RuntimeError("ARCHIVE_RULESET_NOT_VERIFIED")
    # The Actions token masks the bypass list. A separate admin readback of
    # [] at the pinned ruleset revision is recorded in the canonical handover.
    tags = git("ls-remote", "--refs", "--tags", "origin", PREFIX + "*")
    actual = {}
    for line in tags.splitlines():
        object_sha, ref = line.split("\t", 1)
        if ref in actual:
            raise RuntimeError("ARCHIVE_DUPLICATE_TAG")
        actual[ref] = object_sha
    expected = {x["tag"]: x["sha"] for x in candidates}
    if actual != expected:
        raise RuntimeError("ARCHIVE_TAG_INVENTORY_OR_SHA_DRIFT")
    obj = api_get(repository, "git/ref/tags/" + tag.removeprefix("refs/tags/"), token).get("object", {})
    if obj.get("sha") != sha or obj.get("type") != "commit":
        raise RuntimeError("ARCHIVE_TAG_NOT_LIGHTWEIGHT_COMMIT")
    if git("cat-file", "-t", tag) != "commit" or git("rev-parse", tag) != sha:
        raise RuntimeError("ARCHIVE_COMMIT_OBJECT_MISMATCH")
    # Prove DAG and all referenced trees/blobs are locally traversable, not
    # just the HEAD's working tree. An incomplete/shallow clone fails closed.
    reachable = git("rev-list", "--objects", "--missing=print", tag).splitlines()
    if not reachable or any(line.startswith("?") for line in reachable) or not any(
            line.split(" ", 1)[0] == sha for line in reachable):
        raise RuntimeError("ARCHIVE_HISTORY_MISSING_OBJECTS")
    workflow_dir = Path(".github/workflows")
    if workflow_dir.exists() and any(
        branch in p.read_text(encoding="utf-8") for pattern in ("*.yml", "*.yaml")
        for p in workflow_dir.glob(pattern)
    ):
        raise RuntimeError("ARCHIVE_ACTIVE_WORKFLOW_BRANCH_DEPENDENCY")
    return {
        "branch": branch, "sha": sha, "tag": tag,
        "rulesetId": RULESET_ID, "rulesetUpdatedAt": OWNER_VERIFIED_RULE_UPDATED_AT,
        "reachableObjectCount": len(reachable),
        "proof": "PROTECTED_ARCHIVE_TAG_EXACT_COMMIT",
        "authorizesDeletionAlone": False,
    }
