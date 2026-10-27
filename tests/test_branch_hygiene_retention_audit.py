#!/usr/bin/env python3
"""Fail-closed synthetic tests for archival-tag readback (never mutates refs)."""
import unittest
from tools.branch_hygiene_retention_audit import evaluate


class RetentionAuditTests(unittest.TestCase):
    def setUp(self):
        repo = "EAKerber/MobiliPresenter2D_DesignSystem"
        self.heads = [
            ("audit/a", "1" * 40), ("audit/b", "2" * 40),
            ("docs/a", "3" * 40), ("docs/b", "4" * 40),
            ("proposal/a", "5" * 40), ("proposal/b", "6" * 40),
            ("architecture/a", "7" * 40), ("architecture/b", "8" * 40),
        ]
        self.manifest = {"schemaVersion":"DSHistoricalDAGRetentionProposal/0.1",
                         "status":"PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE",
                         "repository":repo,"tagStyle":"lightweight-commit-ref-exact-SHA",
                         "tagNamespace":"refs/tags/ds-history/2026-10-27/",
                         "candidates":[{
                             "branch":n,"sha":s,
                             "tag":"refs/tags/ds-history/2026-10-27/"+n.replace("/","--")+"-"+s[:12]
                         } for n,s in self.heads]}
        self.obs = {"schemaVersion":"BranchObservation 0.1","complete":True,
                    "repository":repo,"controlBranch":"main","controlSha":"a"*40,
                    "branches":[{"name":"main","sha":"a"*40}]+
                    [{"name":n,"sha":s} for n,s in self.heads],
                    "openPrHeads":[],"openPrBases":[]}
        self.tags = {x["tag"]:x["sha"] for x in self.manifest["candidates"]}

    def test_empty_remote_tags_is_pending_not_safe_to_delete(self):
        r=evaluate(self.manifest,self.obs,{})
        self.assertEqual(r["pendingCount"],8)
        self.assertFalse(r["branchDeletionAuthorized"])

    def test_exact_tags_are_only_evidence_not_authorization(self):
        r=evaluate(self.manifest,self.obs,self.tags)
        self.assertEqual(r["readbackCount"],8)
        self.assertEqual(r["status"],"TAGS_PRESENT_NOT_DELETE_AUTHORIZATION")
        self.assertFalse(r["tagRuleSetProtectionVerified"])
        self.assertFalse(r["branchDeletionAuthorized"])

    def test_branch_head_drift_fails(self):
        self.obs["branches"][1]["sha"]="f"*40
        self.assertEqual(evaluate(self.manifest,self.obs,self.tags)["blockedCount"],1)

    def test_wrong_tag_sha_fails(self):
        k=next(iter(self.tags)); self.tags[k]="f"*40
        self.assertEqual(evaluate(self.manifest,self.obs,self.tags)["blockedCount"],1)

    def test_open_pr_fails(self):
        self.obs["openPrHeads"]=["audit/a"]
        self.assertEqual(evaluate(self.manifest,self.obs,self.tags)["blockedCount"],1)

    def test_unexpected_archive_tag_fails(self):
        self.tags["refs/tags/ds-history/2026-10-27/extra-"+ "f"*12]="f"*40
        with self.assertRaises(ValueError):
            evaluate(self.manifest,self.obs,self.tags)

    def test_source_duplication_fails(self):
        self.manifest["candidates"][1]=dict(self.manifest["candidates"][0])
        with self.assertRaises(ValueError):
            evaluate(self.manifest,self.obs,self.tags)

    def test_self_protection_cannot_be_disabled(self):
        self.manifest["status"]="APPROVED"
        with self.assertRaises(ValueError):
            evaluate(self.manifest,self.obs,self.tags)


if __name__ == "__main__":
    unittest.main()
