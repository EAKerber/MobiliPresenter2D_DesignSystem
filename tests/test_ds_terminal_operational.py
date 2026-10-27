#!/usr/bin/env python3
"""Terminal SHA must be derived from the actual merge and exactly match remote."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from ds_terminal_operational import terminal_gate
from ds_dag_tag_retain import OPS, PREFIX, REPO, RULESET_ID, OWNER_VERIFIED_RULE_UPDATED_AT

MAIN="1"*40; BASE="2"*40; SOURCE="3"*40
def fixtures():
    cfg={"schemaVersion":"DSOperationalBranchFinalRetirement/0.1",
         "repository":REPO,"branch":OPS,"mode":"MERGE_SECOND_PARENT_EXACT_MAIN",
         "pullRequest":118}
    heads={"refs/heads/main":MAIN,"refs/heads/"+OPS:SOURCE}
    pr={"number":118,"state":"closed","merged_at":"date","merge_commit_sha":MAIN,
        "head":{"ref":OPS,"sha":SOURCE,"repo":{"full_name":REPO}},
        "base":{"ref":"main","repo":{"full_name":REPO}}}
    rule={"id":RULESET_ID,"target":"tag","enforcement":"active","source":REPO,
          "bypass_actors":None,"current_user_can_bypass":"never",
          "conditions":{"ref_name":{"include":[PREFIX+"*"],"exclude":[]}},
          "updated_at":OWNER_VERIFIED_RULE_UPDATED_AT,
          "rules":[{"type":"update"},{"type":"deletion"}]}
    tags={}
    for i in range(8):
        sha=str(i+1)*40
        tags[PREFIX+"audit--"+str(i)+"-"+sha[:12]]=sha
    manifest={"schemaVersion":"DSHistoricalDAGRetentionProposal/0.1",
              "status":"PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE",
              "candidates":[{"tag":k,"sha":v} for k,v in tags.items()]}
    return [cfg, MAIN, [MAIN,BASE,SOURCE], heads, pr, [], False, tags, manifest, rule, False]
class LastBranchTests(unittest.TestCase):
    def run_gate(self, a):
        return terminal_gate(*a)
    def test_strict_true_merge_second_parent(self):
        self.assertEqual(self.run_gate(fixtures()),SOURCE)
    def test_reject_sha_drift(self):
        a=fixtures();a[3]["refs/heads/"+OPS]="4"*40
        with self.assertRaisesRegex(RuntimeError,"TWO_REFS"):
            self.run_gate(a)
    def test_reject_squash_and_wrong_parent(self):
        for parents in ([MAIN,BASE], [MAIN,BASE,"f"*40]):
            a=fixtures();a[2]=parents
            with self.assertRaises(RuntimeError):
                self.run_gate(a)
    def test_reject_unmerged_pr_or_wrong_pr(self):
        for key,val in (("merged_at",None),("merge_commit_sha","8"*40),("number",117)):
            a=fixtures();a[4][key]=val
            with self.assertRaisesRegex(RuntimeError,"NOT_ATTESTED"):
                self.run_gate(a)
    def test_reject_pr_head_drift(self):
        a=fixtures();a[4]["head"]["sha"]="9"*40
        with self.assertRaisesRegex(RuntimeError,"NOT_ATTESTED"):
            self.run_gate(a)
    def test_reject_open_pr(self):
        a=fixtures();a[5]=[{"number":120}]
        with self.assertRaisesRegex(RuntimeError,"OPEN_PULL_REQUEST"):
            self.run_gate(a)
    def test_reject_protected_or_workflow(self):
        for idx in [6,10]:
            a=fixtures();a[idx]=True
            with self.assertRaisesRegex(RuntimeError,"PROTECTED_OR_WORKFLOW"):
                self.run_gate(a)
    def test_reject_missing_tag(self):
        a=fixtures();a[7].pop(next(iter(a[7])))
        with self.assertRaisesRegex(RuntimeError,"REFERENCES_INCOMPLETE"):
            self.run_gate(a)
    def test_reject_rule_drift_or_bypass(self):
        for field,value in [("enforcement","disabled"),("updated_at","2026-10-28T00:00:00Z"),
                            ("bypass_actors",[{"actor_id":1}])]:
            a=fixtures();a[9][field]=value
            with self.assertRaisesRegex(RuntimeError,"TAG_PROTECTION_CHANGED"):
                self.run_gate(a)
    def test_ref_count_must_be_exactly_two(self):
        a=fixtures();a[3]["refs/heads/extra"]="4"*40
        with self.assertRaisesRegex(RuntimeError,"TWO_REFS"):
            self.run_gate(a)
    def test_manifest_requires_exact_mode_and_pr(self):
        for key,value in [("mode","manual"),("pullRequest",0),("branch","main")]:
            a=fixtures();a[0][key]=value
            with self.assertRaisesRegex(RuntimeError,"UNTRUSTED_TERMINAL_MANIFEST"):
                self.run_gate(a)

if __name__=="__main__":
    unittest.main()
