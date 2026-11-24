# Current operational handover — v0.9 plan execution

**Verified:** 24 November 2026 (BRT)  
**Purpose:** current working snapshot, not a declaration that the v0.9 plan is complete.

## Canonical repository state

| Repository | Ref | Verified SHA |
|---|---|---|
| Product | main | `01ded2c100fbfd8b16897e26113dc5068a83e429` |
| Product | development | `fbe6b9b409dd67884dd9447b02f87752a7d0f8ff` |
| Design System | main | `efe754d25466ba3b77dedde04bf1e2d7c0abc0e7` |

Product `main..development` shares base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: 541 commits are development-only and 17 are main-only. These are commit counts, not a measure of runtime divergence. Promotion remains selective; do not merge the entire tree without classifying consumers.

## Open work and branch hygiene

- Product has no open PRs. Design System has open PR #136, which updates this handover.
- Product has 16 open issues; reconcile them against current code, contracts, consumers, and evidence before marking any resolved.
- There are **11 live branches**, not 60: 9 in Product and 2 in Design System. The number 60 belongs to a legacy executor/test fixture, not the live branch list.
- Five integrated refs were retired after exact SHA, merged-PR, protection, and open-PR checks. Their PRs and commits remain recorded.
- One integrated Product ref is technically eligible for retirement: `codex/tst004-mask-assertion-crosswalk-20261124` @ `531c2814235c9524289ccb9efd909f43e01d908b`. PRs #398 and #399 are merged; PR #399 integrated this head into development at `fbe6b9b409dd67884dd9447b02f87752a7d0f8ff`. Its tree exactly matches current development (`80d486ab8044a398286de26f26aa70853489df08`), it is unprotected, no open PR uses it, and the current 68 development workflows do not reference its branch name. Retirement still needs to pass the current exact-SHA hygiene batch and readback.

### Remaining refs

| Repository | Branch | SHA | Role/status |
|---|---|---|---|
| Product | `main` | `01ded2c1` | stable |
| Product | `development` | `fbe6b9b4` | active integration buffer |
| Product | `codex/arc13-localization-menu-theme-20261122` | `fc12bb62` | localization/theme candidate; disposition still to verify |
| Product | `codex/nav005-development-buffer-20261121` | `9c18dd97` | NAV-005 buffer; preserve |
| Product | `codex/tst001-current-snapshot-20261124` | `a8b31e3e` | evidence candidate; pin/disposition still to verify |
| Product | `codex/tst001-refreshable-inventory-20261124` | `6f7a0d3f` | stale/diverged candidate; inspect before reuse |
| Product | `codex/tst004-browser-image-setup-20261124` | `c8c7f71f` | divergent browser setup candidate; preserve until disposition |
| Product | `codex/tst004-mask-assertion-crosswalk-20261124` | `531c2814` | PR #399 merged; tree equals development; controlled retirement candidate |
| Product | `docs/arc13-post-273-reconciliation-20261114` | `82cca3b5` | ARC-13 evidence; preserve pending reconciliation |
| Design System | `main` | `efe754d2` | stable |
| Design System | `codex/md001-current-handover-20261124` | current PR #136 head | open handover update |

The count remains above the preferred steady-state target. Continue retiring only refs with a verified terminal disposition; keep the active buffer and unresolved evidence.

### Hygiene mechanism and stale batch

Product development has exact-SHA bounded hygiene tooling. The retirement workflow on Product main is triggered by changes to `ops/branch-hygiene-development-retirement.json` and applies that manifest after it reaches main. Its current manifest still lists 7 branch refs that are absent from the live branch list (codex/cmp017-admin-control-contract-20261122, codex/cmp017-finish-availability-20261122, codex/cmp017-price-publication-reason-20261122, codex/cmp017-material-disabled-reasons-20261122, codex/cmp017-object-asset-disabled-reason-20261122, codex/arc13-deterministic-scan-20261122, codex/loc004-youtube-links-20261123). Do not replay that manifest unchanged. Reconcile consumed batches and pins (GIT-021), update the candidate disposition, and run the audit-only path before any apply. The hard-coded “60 refs” in the legacy executor/test fixture is not a live inventory.

## TST-001 workflow inventory

The manual dispatch route was removed because a workflow present only on `development` cannot be manually dispatched from the default branch. The reachable push-triggered inventory job passed on exact `development@fa4e482209933e20bab7a3f512fc29337a95b449` (run #45395199309; artifact #14920182560; SHA-256 `d55a65310889b24f4c0a8831663d375d286b470118a160516fa621e84559291d`). PR #397 persisted that generated snapshot to Product development at `3b339fbedd16679e42e204b461d9b77301491141`; PRs #398 and #399 changed only tests/evidence mapping; neither changed workflow definitions.

At the measured snapshot, the inventory reports 27 workflows in main, 68 in development, 25 shared, 2 main-only, 41 development-only, and 0 parse warnings. The JSON correctly leaves command/assertion validation separate. The file pins `fa4e482`, the exact measured workflow snapshot, rather than claiming the JSON commit itself was measured.

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

1. Reconcile consumed hygiene batches and pins (GIT-021); the current main manifest references only absent refs. Then audit the #399 integrated head through the exact-SHA bounded path before any apply.
2. Continue TST-004 across remaining workflow families, starting with path/condition edge cases; preserve existing gates until assertion equivalence is proved.
3. Reconcile the 16 Product issues to current implementation and architecture work items.
4. Classify the 17 main-only commits and prepare only compatible promotion packages.
5. Continue open DOM/CMP/ARC work in development, with exact readback before any later promotion.
