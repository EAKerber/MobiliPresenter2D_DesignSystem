# Current operational handover — v0.9 plan execution

**Verified:** 24 November 2026 (BRT)  
**Purpose:** current working snapshot, not a declaration that the v0.9 plan is complete.

## Canonical repository state

| Repository | Ref | Verified SHA |
|---|---|---|
| Product | main | `01ded2c100fbfd8b16897e26113dc5068a83e429` |
| Product | development | `3b339fbedd16679e42e204b461d9b77301491141` |
| Design System | main | `efe754d25466ba3b77dedde04bf1e2d7c0abc0e7` |

Product `main..development` shares base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: 538 commits are development-only and 17 are main-only. These are commit counts, not a measure of runtime divergence. Promotion remains selective; do not merge the entire tree without classifying consumers.

## Open work and branch hygiene

- Product has no open PRs. Design System has open PR #136, which updates this handover.
- Product has 16 open issues; reconcile them against current code, contracts, consumers, and evidence before marking any resolved.
- There are **10 live branches**, not 60: 8 in Product and 2 in Design System. The earlier 60-ref roster was historical.
- Five verified integrated branch refs were retired after exact SHA, merged-PR, protection, and open-PR checks. The closed PRs and commits remain recorded. The remaining refs are:

| Repository | Branch | SHA | Role/status |
|---|---|---|---|
| Product | `main` | `01ded2c1` | stable |
| Product | `development` | `3b339fbe` | active integration buffer |
| Product | `codex/arc13-localization-menu-theme-20261122` | `fc12bb62` | localization/theme candidate; disposition still to verify |
| Product | `codex/nav005-development-buffer-20261121` | `9c18dd97` | NAV-005 buffer; preserve |
| Product | `codex/tst001-current-snapshot-20261124` | `a8b31e3e` | evidence candidate; pin/disposition still to verify |
| Product | `codex/tst001-refreshable-inventory-20261124` | `6f7a0d3f` | stale/diverged candidate; inspect before reuse |
| Product | `codex/tst004-browser-image-setup-20261124` | `c8c7f71f` | browser-gate setup candidate; disposition still to verify |
| Product | `docs/arc13-post-273-reconciliation-20261114` | `82cca3b5` | ARC-13 evidence; preserve pending reconciliation |
| Design System | `main` | `efe754d2` | stable |
| Design System | `codex/md001-current-handover-20261124` | `176d621c` | open PR #136 |

The live count is above the preferred steady-state target. Further retirement should follow the same exact-reference checks; keep the active buffer, evidence, and unresolved candidates until their disposition is recorded.

## TST-001 workflow inventory

The manual dispatch route was removed because a workflow present only on `development` cannot be manually dispatched from the default branch. The reachable push-triggered inventory job passed on exact `development@fa4e482209933e20bab7a3f512fc29337a95b449` (run #45395199309; artifact #14920182560; SHA-256 `d55a65310889b24f4c0a8831663d375d286b470118a160516fa621e84559291d`). PR #397 persisted that generated snapshot to Product development at `3b339fbedd16679e42e204b461d9b77301491141`; its only file change was the inventory JSON. The source pin remains `fa4e482` because that is the exact measured workflow snapshot; the later commit only records the snapshot.

At the measured snapshot, the inventory reports 27 workflows in main, 68 in development, 25 shared, 2 main-only, 41 development-only, and 0 parse warnings. The JSON status correctly leaves command/assertion validation separate. This is not yet the workflow-to-assertion crosswalk.

## Other test and domain status

- **TST-002:** the Buyer boundary crosswalk from PR #395 is integrated in development. It remains partial (six assertion groups); reconcile its source pin and extend one risk family at a time.
- **TST-004 / TST-022:** still partial. The selector remains advisory and no workflow coverage was removed. Repeated command text alone does not prove duplicate assertions.
- **TST-005:** re-read required checks and branch rules before making any protection decision.
- **Main-only work:** classify all 17 main-only commits by consumer and promotion risk; use selective packages rather than a whole-tree merge.
- **DOM/CMP/ARC:** continue by each work item's definition of done, preserving explicit unknowns and consumer boundaries.

The recent inventory and gate changes are CI/documentation only. They do not change Viewer runtime, mask content, or mask consumers. Product main, Netlify settings, deploy previews, and Production were not changed in this work.

## Immediate sequence

1. Continue TST-004 from workflow/path filters through conditions, jobs, commands, assertions, outcomes, and representative cost; preserve existing coverage until equivalence is proven.
2. Reconcile the 16 Product issues to current code and their architecture-plan work items.
3. Classify the 17 main-only commits and prepare only compatible promotion packages.
4. Continue the open DOM/CMP/ARC work in the development buffer, with exact readback before any later promotion.
