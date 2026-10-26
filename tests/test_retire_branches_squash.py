"""Guardrail tests for optional identical-full-tree squash retirement.

These tests never mutate refs or access the network.
"""
import copy
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from tools.retire_merged_branches import verify_squash

REPO = "EAKerber/MobiliPresenter2D_DesignSystem"
BRANCH = "audit/sample-merged-squash"
HEAD = "2" * 40
MERGE = "4" * 40
CONTROL = "5" * 40
PARENT = "1" * 40
TREE = "a" * 40


def entry():
    return {"branch": BRANCH, "sha": HEAD,
            "squashMerge": {"pullRequest": 49, "mergeCommit": MERGE}}


def pr():
    return {"state": "closed", "merged_at": "2026-10-26T20:00:00Z",
            "merge_commit_sha": MERGE,
            "head": {"ref": BRANCH, "sha": HEAD,
                     "repo": {"full_name": REPO}},
            "base": {"ref": "main", "repo": {"full_name": REPO}}}


def git_run(*args):
    if args[:3] == ("git", "rev-list", "--parents"):
        return MERGE + " " + PARENT
    if args[:3] == ("git", "show", "-s"):
        return TREE
    raise AssertionError(str(args))


def subprocess_run(args, **kwargs):
    if args[:3] == ["git", "merge-base", "--is-ancestor"]:
        return SimpleNamespace(returncode=0, stdout="")
    if args[:2] == ["git", "grep"]:
        return SimpleNamespace(returncode=1, stdout="")
    raise AssertionError(str(args))


class SquashRetirementTests(unittest.TestCase):
    def verify(self, item=None, response=None, run_fn=git_run, subprocess_fn=subprocess_run):
        with patch("tools.retire_merged_branches.api", return_value=response or pr()), \
             patch("tools.retire_merged_branches.run", side_effect=run_fn), \
             patch("tools.retire_merged_branches.subprocess.run", side_effect=subprocess_fn):
            return verify_squash(REPO, item if item is not None else entry(), CONTROL)

    def test_explicit_identical_squash_passes(self):
        result = self.verify()
        self.assertEqual(result["treeSha"], TREE)
        self.assertEqual(result["proof"], "MERGED_SQUASH_IDENTICAL_FULL_TREE")

    def test_no_proof_is_not_permission(self):
        self.assertIsNone(self.verify(item={"branch": BRANCH, "sha": HEAD}))

    def test_malformed_proof_fail_closed(self):
        bads = [{}, {"pullRequest": 49},
                {"pullRequest": True, "mergeCommit": MERGE},
                {"pullRequest": 49, "mergeCommit": "invalid"},
                {"pullRequest": 49, "mergeCommit": MERGE, "extra": True}]
        for proof in bads:
            with self.subTest(proof=proof):
                item = entry()
                item["squashMerge"] = proof
                with self.assertRaisesRegex(RuntimeError, "INVALID_SQUASH_PROOF"):
                    self.verify(item=item)

    def test_mismatched_pr_identity_fails(self):
        alterations = [
            {"state": "open"}, {"merged_at": None},
            {"merge_commit_sha": "8" * 40},
            {"head": {"ref": BRANCH, "sha": "f" * 40, "repo": {"full_name": REPO}}},
            {"base": {"ref": "development", "repo": {"full_name": REPO}}},
        ]
        for alteration in alterations:
            with self.subTest(value=alteration), self.assertRaisesRegex(RuntimeError, "PR_IDENTITY"):
                record = pr()
                record.update(alteration)
                self.verify(response=record)

    def test_changed_full_tree_fails(self):
        def mismatch(*args):
            if args[:3] == ("git", "show", "-s") and args[-1] == MERGE:
                return "b" * 40
            return git_run(*args)
        with self.assertRaisesRegex(RuntimeError, "FULL_TREE_MISMATCH"):
            self.verify(run_fn=mismatch)

    def test_not_a_squash_merge_fails(self):
        def two_parents(*args):
            if args[:3] == ("git", "rev-list", "--parents"):
                return MERGE + " " + PARENT + " " + ("9" * 40)
            return git_run(*args)
        with self.assertRaisesRegex(RuntimeError, "NOT_SINGLE_PARENT"):
            self.verify(run_fn=two_parents)

    def test_unmerged_commit_fails(self):
        def outside_main(args, **kwargs):
            if args[:3] == ["git", "merge-base", "--is-ancestor"] and args[3] == MERGE:
                return SimpleNamespace(returncode=1)
            return subprocess_run(args, **kwargs)
        with self.assertRaisesRegex(RuntimeError, "ANCESTRY_NOT_PROVEN"):
            self.verify(subprocess_fn=outside_main)

    def test_active_workflow_dependency_fails(self):
        def named_in_workflow(args, **kwargs):
            if args[:2] == ["git", "grep"]:
                return SimpleNamespace(returncode=0)
            return subprocess_run(args, **kwargs)
        with self.assertRaisesRegex(RuntimeError, "ACTIVE_WORKFLOW_REF"):
            self.verify(subprocess_fn=named_in_workflow)

    def test_workflow_lookup_error_fails(self):
        def api_unavailable(args, **kwargs):
            if args[:2] == ["git", "grep"]:
                return SimpleNamespace(returncode=128)
            return subprocess_run(args, **kwargs)
        with self.assertRaisesRegex(RuntimeError, "WORKFLOW_LOOKUP_FAILED"):
            self.verify(subprocess_fn=api_unavailable)


if __name__ == "__main__":
    unittest.main()
