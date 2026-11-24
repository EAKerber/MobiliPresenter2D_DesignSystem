# Current operational handover — v0.9 plan execution

**Verified:** 24 November 2026, 20:00 BRT  
**Purpose:** live working snapshot; this is not a declaration that the v0.9 plan is complete.

## Canonical repository state

| Repository | Ref | Verified SHA |
|---|---|---|
| Product | main | `01ded2c100fbfd8b16897e26113dc5068a83e429` |
| Product | development | `116800e11016fb9093ce4ab5e3c0ed1e8527fe15` |
| Design System | main | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |

Product `main..development` shares base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: 549 commits are development-only and 17 are main-only. These counts do not measure runtime divergence. Promotion remains selective; do not merge the entire tree without classifying consumers.

## Branch inventory and hygiene

There are **15 live remote Product branches** and **2 Design System branches**. The shared local Product repository has 44 local branch heads and 5 remote-tracking refs; these local pointers overlap the remote branches and many are attached to worktrees. Therefore “about 60” can describe a naïve sum of local and remote pointers, but not 60 distinct live hosted branches.

Product is 10 branches above the plan's soft review trigger of 5 and 13 above the stable target of 2. Design System is at its target of 2.

- Product open PRs: #400 and #407, both target `main`. Design System open PR: #137, this handover.
- Product refs `main@01ded2c1` and `development@116800e1` are the permanent control refs.
- NAV-005 remains an active integration buffer. Closed or merged PR status alone does not make an experimental or evidence branch disposable.
- Product #400 now prepares one exact retirement wave for #399, #409, and #411. Each head is pinned to its squash merge; the three current trees match their recorded integration trees. The current audit rechecks SHA, protection, open PRs, workflow references, and tree identity before any deletion.
- The #400 audit run [#45505817682](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/45505817682) and retirement workflow run [#45505817693](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/45505817693) completed successfully on its current head; the audit passed and no branch was deleted. The Deploy Preview check passed at [preview #400](https://deploy-preview-400--mobilipresenter2d.netlify.app).
- If the exact authorization reaches Product `main` and the apply gate passes, the wave reduces Product from 15 to 12 remote branches. No runtime files change, but merging to `main` can trigger the connected site build/deploy. The PR remains open; it has not been integrated.

The remaining Product remote refs are: `main`, `development`, `codex/arc13-localization-menu-theme-20261122`, `codex/cmp001-admin-stage-availability-20261124`, `codex/dom011-buyer-fixture-v5-validation-20261124`, `codex/hygiene-retire-tst004-crosswalk-20261124`, `codex/loc006-viewer-price-copy-20261124`, `codex/nav005-development-buffer-20261121`, `codex/tst001-current-snapshot-20261124`, `codex/tst001-refreshable-inventory-20261124`, `codex/tst004-browser-image-setup-20261124`, `codex/tst004-mask-assertion-crosswalk-20261124`, `codex/tst004-playwright-image-current-20261124`, `codex/tst004-viewer-price-main-pr-trigger-20261124`, and `docs/arc13-post-273-reconciliation-20261114`. This list is a point-in-time readback, not a deletion recommendation.

## TST-001 and gate friction

The checked-in workflow inventory still pins an older development snapshot at `81207f32`; it must be regenerated or reconciled against current `development@116800e1` before its counts are used as current. The global workflow → trigger → job → command → assertion → result crosswalk remains incomplete.

PR #411 is integrated in development at `116800e1`. It adds one current CMP-001/TST-001 slice for Admin stage availability to the existing gate-friction review. That record links the editable state, required/empty-stage rules, assertions, Admin workflow route, and exact evidence. It distinguishes stage availability from initial configurator/viewer/service visibility; both use checkboxes but have separate state and meaning. The exact Admin browser run on PR #410's tested candidate [#45501943629](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/45501943629) passed, and the Admin source, test, and workflow blobs match the integrated development tree. The harness is local-browser evidence, not proof of hosted Admin/API behavior. CMP-001 and TST-001 remain partial.

Previous evidence remains scoped: TST-001 workflow inventory and operational-friction runs are historical snapshots; the Admin slice does not complete the full crosswalk. TST-004 has partial mask and public-navigation assertion slices, but the remaining workflow/path/condition/command/assertion/cost matrix is still open. Do not remove existing gates until unique assertions are mapped and equivalent replacement evidence is demonstrated.

## Immediate sequence

1. Reconcile the checked-in TST-001 inventory with the exact current development tree and current open-PR readback; then continue the workflow → trigger → job → command → assertion → result matrix.
2. Continue CMP-001 in bounded batches, expanding the Admin inventory beyond the stage-availability pilot and preserving semantic distinctions rather than creating generic checkbox abstractions.
3. Extend TST-004 through remaining gate families and path/condition edges; retain existing gates during the audit.
4. Classify the 17 main-only commits by consumer and risk, then prepare selective promotions rather than a whole-tree merge.
5. Continue DOM/V5 and other P0 plan items by their own DoD, keeping implementation, development integration, main promotion, and publication as separate states.

Product `main`, Design System `main`, and production were not changed by the latest crosswalk or hygiene preparation.