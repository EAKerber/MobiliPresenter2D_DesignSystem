# Current operational handover — v0.9 plan execution

**Readback:** 2026-11-26 05:17 UTC, immediately before this refresh was pushed. Point-in-time snapshot; re-read exact refs, PRs, deployments, permissions, and the execution register before dependent actions. This handover is updated in the open Design System PR #137 and becomes part of Design System `main` only if that documentation PR is integrated.

## Authority hierarchy

1. **Method and intended DoD:** [Plano Diretor v0.9](architecture/MOBILIPRESENTER2D_PLANO_DIRETOR_CONSOLIDADO_v0.9.md), blob `59bb530b14172eb9772b9f89bb62272173f4381c`.
2. **Execution state:** Product's [125-ID operational register](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/architecture/plan-v0.9-execution-register.json); re-read its current blob before relying on task status.
3. **Design decisions:** [decisions.json](../decisions.json), blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`.
4. **Implementation:** exact Product source and consumers at the named remote ref.
5. **Validation:** source-pinned crosswalks and exact test/Actions receipts. Local, hosted, Preview, production, and approval evidence remain distinct.

Historical records are preserved as provenance. Their dated state and operational instructions are not current authorization.

## Live repository readback

| Repository | Ref | SHA |
|---|---|---|
| Product | `main` | `5c6e652693bd30218e6915bf8cb160bde03ac719` |
| Product | `development` | `c04efa2c98f4ddd7d0566fe19b3cf3c5fa6df510` |
| Design System | `main` | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |
| Design System | `development` | not found (GitHub returned 404) |

Product has exactly two live branches, `main` and `development`, and no open Product PRs at this readback. Design System has `main` only; its open PR #137 is the documentation refresh carrying this handover. GitHub's issues endpoint returned 16 open Product issues; their current relevance and mapping to the 125-ID register remain an MD-001 task, so issue titles alone are not treated as proof of active defects.

Product `main` and `development` diverge from merge base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: development has 599 unique commits, main has 35, and the compare response is capped at 300 paths. The smaller reverse comparison lists 92 main-side changed paths. These are not grounds for a whole-tree merge; promotion remains selective by family.

Netlify production deploy [`6b07bd0f17cb2fd1e0d65b34`](https://6b07bd0f17cb2fd1e0d65b34--mobilipresenter2d.netlify.app) is READY on Product `main` at `5c6e652693bd30218e6915bf8cb160bde03ac719`. The site is [casaemmodulos.casa](https://casaemmodulos.casa).

## Recent Product integrations

| PR | Destination | Result |
|---|---|---|
| #400 | `main` | Branch-hygiene maintenance integrated at `19f5ab1db5f545ab38e43eba9535d9a8e7a727ac`. |
| #407 | `main` | Viewer pricing gate trigger coverage integrated at `309939ad5f78acda29539a7be5b9e71d797688bd`; CI/test change. |
| #442 | `main` | Blocked saving fallback defaults when V3 state is missing/invalid, while retaining the documented GET fallback; integrated at `6bdc9d30f5f3ae5bbc5c62bd53418cc48c5ceb8d`. |
| #445 | `main` | Normalized configurator flow now governs stage lookup, ownership and item availability; integrated at `9112bacc3341718696c61b7cb0488beb713e4682`. |
| #432 | `main` | Test-only deterministic CAS race and missing-readback coverage; integrated at current `main` SHA `5c6e652693bd30218e6915bf8cb160bde03ac719`. |
| #475 | `development` | Admin scene-asset fixed copy moved to its catalog; integrated at `ef943910f5513c423ce22b84b4ced548f9c042f2`. |
| #476 | `development` | Execution register and historical handover context refreshed; integrated at `c04efa2c98f4ddd7d0566fe19b3cf3c5fa6df510`. |

## Selective promotion and architecture findings

- **Normalized flow:** DOM-006 is integrated and validated in both Product destinations. The main-targeting implementation in #445 passed its exact-head gates, and the current production deploy is on a descendant of that integration.
- **Admin V3:** the unsafe PUT-from-defaults path was closed by #442; its GET fallback remains a deliberate behavior to compare with development. Provider-level Identity and storage atomicity have not been proven. A local Admin login fixture is anonymous by design; use a deployed preview for real authentication.
- **Test overlap:** TST-003 reconciliation found one `npm test` call in main's `app-build-purity`. `candidate-assets` runs scoped asset/mask/provenance checks and `variant-fidelity` derives/renders variant outputs; neither repeats that app test. Keep those guarantees distinct and do not transplant a duplicate-removal change to main.
- **CSS-00:** the exact CSS baseline is still partial. The initial Config/Admin readback found distinct local bundles and other inline/dynamic CSS surfaces; the full stylesheet/selector inventory remains to be completed.
- **FND-01 candidate:** `.visually-hidden` is defined identically in Product `app/styles.css` and `app/admin/admin.css`, consumed by the Config hidden heading and Admin brand name. Preserve `.sr-only`, which serves a different Config heading/live-region role. Product `app/ui-theme.css` is not Design System-derived or pinned and differs between main/development. A Design System-owned versioned export, manifest, Product pin and direct semantic/CSSOM/focus tests are needed before extraction; no implementation is claimed.
- **v0.9 register:** all 125 IDs are retained. The current reconciliation count is 7 done, 20 partial and 98 unreviewed. This is a count of reconciled register entries, not a percentage of implementation completion.

## Token validation and limits

At exact Design System `main@c6ff6545e9ae2071e695109fd94ac91676e7fb0a`, local checks passed after reading the source and generated outputs as canonical Git blob bytes: P-TOKEN-01 tests 6/6, P-TOKEN-02B tests 3/3, and VIS-002C v0.3 verification passed. No new hosted workflow was run on this SHA. Windows `core.autocrlf=true` converts LF files to CRLF and causes false source-hash/generated-output failures in a standard checkout; the underlying repository blobs were unchanged.

GitHub's branch-protection/ruleset API returned 403; required-check policy remains unknown. Observed workflow results do not establish protection.

This handover refresh changes documentation only. It does not change runtime, stored configuration, production content, or access-control settings.
