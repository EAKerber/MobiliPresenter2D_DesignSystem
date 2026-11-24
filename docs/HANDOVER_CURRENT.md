# Current operational handover — v0.9 plan execution

**Verified:** 24 November 2026 (BRT)  
**Purpose:** current working snapshot, not a declaration that the v0.9 plan is complete.

## Canonical repository state

| Repository | Ref | Verified SHA |
|---|---|---|
| Product | main | `01ded2c100fbfd8b16897e26113dc5068a83e429` |
| Product | development | `81207f32d0bd2100421172fb7b6585099c3fa78a` |
| Design System | main | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |

Product `main..development` shares base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: 543 commits are development-only and 17 are main-only. These are commit counts, not a measure of runtime divergence. Promotion remains selective; do not merge the entire tree without classifying consumers.

## Open work and branch hygiene

- Product has one open PR, #400, which prepares exact retirement of the integrated TST-004 crosswalk branch. Design System has open PR #137 for this handover update.
- The live remote inventory is **13 branches**: 11 in Product and 2 in Design System, including this PR’s temporary handover branch. There are not 60 live branches; “60 refs” is a legacy executor/test-fixture value.
- Product branch `codex/tst001-pr-inventory-readback-20261124` was retired after verifying PR #403 merged, the branch was unprotected, no open PR used it as a head, and its tree exactly matched current development. Its PR and commits remain recorded.
- The TST-004 crosswalk branch `codex/tst004-mask-assertion-crosswalk-20261124` is integrated through PR #399 at `531c2814235c9524289ccb9efd909f43e01d908b`; its tree matches current development. PR #400 pins this exact target for the bounded retirement workflow, so preserve it until that apply/readback route is deliberately integrated and verified.
- Other extra refs are active buffers, unmerged experiments, or retained evidence. In particular, preserve NAV-005, the closed-but-unmerged TST-004 browser setup experiments, and the closed ARC-13 PR #274 evidence branch. Do not delete a branch solely because its PR is closed.

### Remaining refs

| Repository | Branch | SHA | Role/status |
|---|---|---|---|
| Product | `main` | `01ded2c1` | stable |
| Product | `development` | `81207f32` | active integration buffer |
| Product | `codex/hygiene-retire-tst004-crosswalk-20261124` | `d2f1f3ae` | open PR #400; apply still awaits integration and readback |
| Product | `codex/arc13-localization-menu-theme-20261122` | `fc12bb62` | localization/theme candidate; latest PR closed unmerged |
| Product | `codex/nav005-development-buffer-20261121` | `9c18dd97` | NAV-005 buffer; preserve |
| Product | `codex/tst001-current-snapshot-20261124` | `a8b31e3e` | current inventory candidate; compare with integrated snapshot before reuse |
| Product | `codex/tst001-refreshable-inventory-20261124` | `6f7a0d3f` | closed-unmerged generation experiment; preserve evidence |
| Product | `codex/tst004-browser-image-setup-20261124` | `c8c7f71f` | closed-unmerged browser setup experiment; preserve evidence |
| Product | `codex/tst004-mask-assertion-crosswalk-20261124` | `531c2814` | integrated by #399; exact target in PR #400 retirement manifest |
| Product | `codex/tst004-playwright-image-current-20261124` | `e1e92abd` | closed-unmerged image experiment; measured net slowdown, preserve result |
| Product | `docs/arc13-post-273-reconciliation-20261114` | `82cca3b5` | closed Draft PR #274; preserve documentation and evidence pending triage |
| Design System | `main` | `c6ff6545` | stable |
| Design System | `codex/handover-live-reconciliation-20261124` | `61e718f6` | open PR #137; documentary reconciliation |

The total is above the preferred steady-state target. Continue retiring only refs with a verified terminal disposition, while keeping active integration buffers and unresolved evidence.



### Hygiene mechanism and stale batch

Product development has exact-SHA bounded hygiene tooling. The retirement workflow on Product main is triggered by changes to `ops/branch-hygiene-development-retirement.json` and applies that manifest after it reaches main. Its current manifest still lists 7 branch refs that are absent from the live branch list (codex/cmp017-admin-control-contract-20261122, codex/cmp017-finish-availability-20261122, codex/cmp017-price-publication-reason-20261122, codex/cmp017-material-disabled-reasons-20261122, codex/cmp017-object-asset-disabled-reason-20261122, codex/arc13-deterministic-scan-20261122, codex/loc004-youtube-links-20261123). Do not replay that manifest unchanged. PR #400 replaces both stale batches with the single current #399 head and exact terminal disposition. On the PR head, the bounded retirement audit passed with one proof and `deleted: 0`; the development audit passed with `count: 0` and `readback: NOT_APPLIED`. The ref has not been deleted. Integration to Product main may run its connected site build/deploy pipeline, so keep that publication effect separate from the audit result. The hard-coded “60 refs” in the legacy executor/test fixture is not a live inventory.

## TST-001 workflow inventory

The manual dispatch route was removed because a workflow present only on `development` cannot be manually dispatched from the default branch. The shared inventory job now runs on both `push` and `pull_request`, pins the exact PR head (not GitHub's merge ref), verifies the push SHA, emits the full JSON to readable logs, and names artifacts uniquely.

- PR-head readback passed at exact SHA `5da6d931fdf77b839a9ef6c1c4e70fa52e4c3154` (run #45420119869). The run exposed and fixed an initial merge-ref checkout defect before it passed.
- The integrated push readback passed at exact `development@81207f32d0bd2100421172fb7b6585099c3fa78a` (run #45420518073; conclusion: success). Its source tree is `d5f57b82c68d66169eed52ca663f85eafbba23f8`, verified against the development pin.
- The live snapshot reports 27 main workflows, 68 development workflows, 25 shared, 2 main-only, and 43 development-only; 70 definitions, event counts PR 27 / push 62 / workflow_dispatch 54 / schedule 1, seven paths marked write-signal, and zero parse warnings.
- The checked-in JSON still pins historical `fa4e482`; the current successful readback is in the workflow log/artifact, not yet a refreshed committed snapshot. TST-001 remains incomplete: finish the workflow → trigger → job → command → assertion → result mapping and clearly distinguish existing, candidate, and historical routes.



## TST-004 mask assertion slice

PR #398 integrated a partial crosswalk in Product development. It maps three existing assertion groups to source anchors, the `candidate-assets.yml` job/step, branch/path filters, and trigger conditions. The pull-request event is path-filtered with no base-branch filter; push is path-filtered to `main`; manual dispatch is unfiltered.

The exact candidate gate run #45402572720 passed 24/24 impact-plan tests. A prior successful asset-gate run #45307538355 is retained as runtime evidence; the current mask-validation step text is identical, and the test scripts, metadata, inline mask data, and referenced mask blobs match the measured source. This is only one TST-004 slice; the full workflow/path/condition/command/assertion/cost matrix remains incomplete.

The PR #398 diff changed only the impact test, advisory bundle description, and crosswalk receipt. It did not change mask images/data, Viewer behavior, Netlify, or Production.

## TST-004 public-navigation assertion slice

PR #399 integrated a partial crosswalk into Product development at exact head `531c2814235c9524289ccb9efd909f43e01d908b`. It maps five assertion groups from the shared 124-case public-navigation browser suite to the current development and main workflow routes, path filters, and job conditions. The Viewer’s separate 20-case depth-2 gate remains distinct. The impact-plan workflow passed on the exact PR head (run #45406708875). This is workflow/assertion reachability evidence, not a new runtime browser pass or a claim that TST-004 is complete.

## Other test and domain status

- **TST-002:** the Buyer boundary crosswalk from PR #395 is integrated in development. It remains partial (six assertion groups); reconcile its older source pin and extend one risk family at a time.
- **TST-022:** the selector remains advisory and does not suppress or replace existing gates.
- **TST-005:** re-read required checks and branch rules before making any protection decision.
- **Main-only work:** classify all 17 main-only commits by consumer and promotion risk; use selective packages rather than a whole-tree merge.
- **DOM/CMP/ARC:** continue by each work item's definition of done, preserving explicit unknowns and consumer boundaries.

Product main, Netlify settings, deploy previews, and Production were not changed by the inventory/crosswalk work.

## Immediate sequence

1. Finish TST-001 by reconciling the checked-in snapshot with the exact current readback and completing the workflow → trigger → job → command → assertion → result matrix; keep candidate and historical routes explicit.
2. Continue TST-004 through the remaining gate families, including path/filter/condition edge cases; preserve existing gates until assertion reachability and equivalence are proven.
3. Complete GIT-021 through PR #400’s bounded exact-SHA retirement path. Its target is already integrated in development; the remaining step reaches Product main and can trigger the connected site build/deploy pipeline, so verify that publication effect separately from audit and deletion/readback.
4. Reconcile Product issues against current implementation, contracts, consumers, and evidence before resolving them.
5. Classify the 17 main-only commits by consumer and promotion risk; prepare selective packages rather than a whole-tree merge.
6. Continue DOM/CMP/ARC work by each item’s definition of done, preserving explicit unknowns and exact readback before any later promotion.
