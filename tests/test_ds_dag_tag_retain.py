import copy
import unittest
from tools.ds_dag_tag_retain import PREFIX, RULESET_ID, REPO, OPS, PATTERN, OWNER_VERIFIED_RULE_UPDATED_AT, validate


class RetentionCreationSafetyTests(unittest.TestCase):
    def setUp(self):
        self.main_sha = "a" * 40
        self.rows = []
        for i, name in enumerate(["architecture/x", "audit/a", "audit/b", "audit/c",
                                  "docs/a", "docs/b", "docs/c", "proposal/a"], 1):
            sha = str(i) * 40
            self.rows.append({"branch": name, "sha": sha,
                              "tag": PREFIX + name.replace("/", "--") + "-" + sha[:12]})
        self.m = {"schemaVersion": "DSHistoricalDAGRetentionProposal/0.1",
                  "repository": REPO, "controlBranch": "main",
                  "status": "PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE",
                  "tagNamespace": PREFIX, "tagStyle": "lightweight-commit-ref-exact-SHA",
                  "candidates": self.rows}
        self.heads = {"refs/heads/main": self.main_sha, "refs/heads/" + OPS: "f" * 40}
        self.heads.update({"refs/heads/" + c["branch"]: c["sha"] for c in self.rows})
        self.rule = {"id": RULESET_ID, "target": "tag", "source": REPO, "enforcement": "active",
                     "updated_at": OWNER_VERIFIED_RULE_UPDATED_AT,
                     "bypass_actors": [], "current_user_can_bypass": "never",
                     "conditions": {"ref_name": {"exclude": [], "include": [PATTERN]}},
                     "rules": [{"type": "deletion"}, {"type": "update"},
                               {"type": "non_fast_forward"}]}

    def check(self, tags=None, prs=None):
        return validate(self.m, self.heads, tags or {}, self.rule, prs or [], self.main_sha)

    def test_all_missing_is_safe_to_create_not_delete(self):
        self.assertEqual(len(self.check()), 8)

    def test_all_present_is_idempotent(self):
        self.assertEqual(self.check({x["tag"]: x["sha"] for x in self.rows}), [])

    def test_bad_tag_existing_rejected(self):
        with self.assertRaisesRegex(ValueError, "ARCHIVE_TAG_DRIFT"):
            self.check({self.rows[0]["tag"]: "0" * 40})

    def test_unexpected_tag_rejected(self):
        with self.assertRaisesRegex(ValueError, "UNEXPECTED_ARCHIVE_TAG"):
            self.check({PREFIX + "surprise": "0" * 40})

    def test_drifted_head_rejected(self):
        self.heads["refs/heads/" + self.rows[0]["branch"]] = "0" * 40
        with self.assertRaisesRegex(ValueError, "HOLD_HEAD_DRIFT"):
            self.check()

    def test_main_drift_rejected(self):
        self.heads["refs/heads/main"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "MAIN_HEAD_DRIFT"):
            self.check()

    def test_open_pr_rejected(self):
        with self.assertRaisesRegex(ValueError, "OPEN_PULL_REQUEST"):
            self.check(prs=[{"number": 123}])

    def test_rule_disabled_rejected(self):
        self.rule["enforcement"] = "disabled"
        with self.assertRaisesRegex(ValueError, "TAG_PROTECTION_NOT_VERIFIED"):
            self.check()

    def test_actions_masked_bypass_requires_same_owner_verified_revision(self):
        self.rule["bypass_actors"] = None
        self.assertEqual(len(self.check()), 8)
        self.rule["updated_at"] = "2026-10-28T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "TAG_PROTECTION_NOT_VERIFIED"):
            self.check()

    def test_rule_bypass_rejected(self):
        self.rule["bypass_actors"] = [{"actor_id": 1}]
        with self.assertRaisesRegex(ValueError, "TAG_PROTECTION_NOT_VERIFIED"):
            self.check()

    def test_rule_wrong_namespace_rejected(self):
        self.rule["conditions"]["ref_name"]["include"] = ["refs/tags/*"]
        with self.assertRaisesRegex(ValueError, "TAG_PROTECTION_NOT_VERIFIED"):
            self.check()

    def test_rule_update_missing_rejected(self):
        self.rule["rules"] = [{"type": "deletion"}]
        with self.assertRaisesRegex(ValueError, "TAG_PROTECTION_NOT_VERIFIED"):
            self.check()

    def test_manifest_cannot_approve_delete(self):
        self.m["status"] = "APPROVED"
        with self.assertRaisesRegex(ValueError, "BAD_MANIFEST"):
            self.check()


if __name__ == "__main__":
    unittest.main()
