#!/usr/bin/env python3
"""Independent negative tests of protected archived HEAD retirement."""
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from branch_hygiene_plan import build_plan, select_bounded_batch
from branch_hygiene_archive import verify_protected_archive
from ds_dag_tag_retain import PREFIX, REPO, RULESET_ID, OWNER_VERIFIED_RULE_UPDATED_AT

SHA = "2" * 40
BRANCH = "audit/proven"
TAG = PREFIX + "audit--proven-" + SHA[:12]
def make_observation():
    return {"schemaVersion": "BranchObservation 0.1", "repository": REPO,
            "controlBranch": "main", "controlSha": "1"*40, "complete": True,
            "observedAt": "", "observationHash": "a"*64, "openPrHeads": [], "openPrBases": [],
            "branches": [{"name": "main", "sha": "1"*40, "treeSha": "a"*40,
                          "protected": False, "ancestorOfControl": True},
                         {"name": BRANCH, "sha": SHA, "treeSha": "b"*40,
                          "protected": False, "ancestorOfControl": False}]}
def make_disposition():
    return {"schemaVersion": "BranchDispositionSet 0.1", "controlBranch": "main",
            "preserveBranches": [], "terminalBranches": [
                {"branch": BRANCH, "sha": SHA, "reason": "proof required", "allowDelete": True}]}
def make_batch():
    return {"schemaVersion": "BranchHygieneBatch 0.1", "repository": REPO,
            "branches": [{"branch": BRANCH, "sha": SHA, "protectedArchiveTag": TAG}]}

class ProtectedArchiveSelection(unittest.TestCase):
    def select(self, obs=None, disp=None, batch=None):
        return select_bounded_batch(build_plan(obs or make_observation(),
                                               disp or make_disposition()),
                                    batch or make_batch())
    def test_explicit_archive_is_only_request_for_runtime_proof(self):
        s = self.select()
        self.assertEqual(s[0]["protectedArchiveTag"], TAG)
    def test_missing_proof_blocks(self):
        b = make_batch()
        b["branches"][0].pop("protectedArchiveTag")
        with self.assertRaises(ValueError):
            self.select(batch=b)
    def test_missing_terminal_authorization_blocks(self):
        d = make_disposition(); d["terminalBranches"] = []
        with self.assertRaises(ValueError):
            self.select(disp=d)
    def test_preserve_conflict_blocks(self):
        d = make_disposition(); d["preserveBranches"] = [BRANCH]
        with self.assertRaises(ValueError):
            self.select(disp=d)
    def test_open_pr_and_protected_branch_block(self):
        for kind in ("openPrHeads", "openPrBases", "protected"):
            o = make_observation()
            if kind == "protected":
                o["branches"][1]["protected"] = True
            else:
                o[kind] = [BRANCH]
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                self.select(obs=o)
    def test_drifted_sha_and_wrong_tag_block(self):
        for mutate in ("sha", "protectedArchiveTag", "squashMerge"):
            b = make_batch()
            if mutate == "sha":
                b["branches"][0]["sha"] = "3"*40
            elif mutate == "protectedArchiveTag":
                b["branches"][0]["protectedArchiveTag"] = TAG.replace("proven", "fake")
            else:
                b["branches"][0]["squashMerge"] = {
                    "pullRequest": 3, "mergeCommit": "4"*40}
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                self.select(batch=b)

class ProtectedArchiveRuntime(unittest.TestCase):
    def setUp(self):
        self.entry = {"branch": BRANCH, "sha": SHA, "protectedArchiveTag": TAG}
        self.candidates = [{"branch": BRANCH, "sha": SHA, "tag": TAG}]
        for i in range(7):
            name = "audit/" + str(i)
            ss = str(i+3)*40
            self.candidates.append({"branch": name, "sha": ss,
                                    "tag": PREFIX + name.replace("/", "--") + "-" + ss[:12]})
        self.rule = {"id": RULESET_ID, "source": REPO, "target": "tag",
                     "enforcement": "active",
                     "conditions": {"ref_name": {"exclude": [], "include": [PREFIX+"*"]}},
                     "bypass_actors": None, "current_user_can_bypass": "never",
                     "updated_at": OWNER_VERIFIED_RULE_UPDATED_AT,
                     "rules": [{"type": "deletion"}, {"type": "update"}]}
        self.manifest = {"schemaVersion": "DSHistoricalDAGRetentionProposal/0.1",
                         "status": "PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE",
                         "repository": REPO, "tagNamespace": PREFIX, "candidates": self.candidates}
    def check(self, rule=None, tags=None, manifest=None, git_mod=None):
        records = {x["tag"]: x["sha"] for x in self.candidates}
        def fake_git(*args):
            if git_mod is not None:
                return git_mod(args, records)
            if args[0] == "ls-remote":
                return "\n".join(s + "\t" + t for t, s in (tags or records).items())
            if args[0] == "cat-file":
                return "commit"
            if args[0] == "rev-parse":
                return SHA
            if args[0] == "rev-list":
                return SHA + "\n" + "9"*40 + " README.md"
            raise AssertionError(args)
        def api(_repo, path, _token):
            if path.startswith("rulesets/"):
                return rule if rule is not None else self.rule
            if path.startswith("git/ref/tags/"):
                return {"object": {"sha": SHA, "type": "commit"}}
            raise AssertionError(path)
        with patch("branch_hygiene_archive.MANIFEST") as mf, \
             patch("branch_hygiene_archive.api_get", side_effect=api), \
             patch("branch_hygiene_archive.git", side_effect=fake_git), \
             patch("branch_hygiene_archive.Path", wraps=Path) as pf:
            mf.read_text.return_value = __import__("json").dumps(manifest or self.manifest)
            return verify_protected_archive(REPO, "test", self.entry)
    def test_complete_tag_and_protected_history(self):
        self.assertEqual(self.check()["proof"], "PROTECTED_ARCHIVE_TAG_EXACT_COMMIT")
    def test_wrong_tag_or_removed_tag(self):
        tags = {x["tag"]: x["sha"] for x in self.candidates}
        tags[TAG] = "f"*40
        with self.assertRaisesRegex(RuntimeError, "SHA_DRIFT"):
            self.check(tags=tags)
        tags.pop(TAG)
        with self.assertRaisesRegex(RuntimeError, "SHA_DRIFT"):
            self.check(tags=tags)
    def test_weak_ruleset_and_bypass_rejected(self):
        for key,value in (("enforcement","disabled"), ("updated_at","2026-10-28T00:00:00Z"),
                          ("bypass_actors",[{"actor_id":1}])):
            rule = copy.deepcopy(self.rule); rule[key] = value
            with self.subTest(key=key), self.assertRaisesRegex(RuntimeError, "RULESET_NOT_VERIFIED"):
                self.check(rule=rule)
    def test_missing_historical_object_blocks(self):
        def fail(args, records):
            if args[0] == "rev-list":
                return SHA + "\n?" + "f"*40
            if args[0] == "ls-remote":
                return "\n".join(s+"\t"+t for t,s in records.items())
            return "commit" if args[0] == "cat-file" else SHA
        with self.assertRaisesRegex(RuntimeError, "MISSING_OBJECTS"):
            self.check(git_mod=fail)
    def test_manifest_mismatch_rejected(self):
        m = copy.deepcopy(self.manifest)
        m["candidates"][0]["sha"] = "f"*40
        with self.assertRaisesRegex(RuntimeError, "NOT_EXACT_MANIFEST_PIN"):
            self.check(manifest=m)

if __name__ == "__main__":
    unittest.main()
