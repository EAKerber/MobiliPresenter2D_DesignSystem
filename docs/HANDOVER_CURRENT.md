# Current operational handover — v0.9 plan execution

**Readback:** 2026-11-26 10:13 UTC. Point-in-time snapshot; re-read exact refs, PRs, deployments, permissions, and the execution register before dependent actions. Product PR #488 was integrated into `development` at `ea66294bae4190ac09d8793b615cf00338d0795a`; Design System `main` is `4c075fc8f8653b5d87f1f07f7471959718b106b2`. Production deploy state and current branch protections were not revalidated in this readback.

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
| Product | `development` | `ea66294bae4190ac09d8793b615cf00338d0795a` |
| Design System | `main` | `4c075fc8f8653b5d87f1f07f7471959718b106b2` |
| Design System | `development` | not found (GitHub returned 404) |

Product has three live branches: `main`, `development`, and the retained `codex/v09-loc006-register-correction-20261126`; it has no open PR. PR #488 updated the 125-ID register and was squash-integrated into `development` at `ea66294bae4190ac09d8793b615cf00338d0795a`. Design System has four live branches: `main`, `codex/handover-live-reconciliation-20261124`, `codex/v09-current-readback-after-137-20261126`, and `codex/v09-current-readback-loc006-20261126`; it has no open PR and no `development` branch. Mapping live issues to the 125-ID register remains an MD-001 task; issue titles alone are not proof of active defects.

Product `main` and `development` diverge from merge base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: development has 611 unique commits and main has 35. The reverse compare lists 92 main-side changed paths. These are not grounds for a whole-tree merge; promotion remains selective by family.

Previous readback recorded Netlify production deploy [`6b07bd0f17cb2fd1e0d65b34`](https://6b07bd0f17cb2fd1e0d65b34--mobilipresenter2d.netlify.app) as READY on Product `main` at `5c6e652693bd30218e6915bf8cb160bde03ac719`; deploy state was not revalidated in this refresh. The site is [casaemmodulos.casa](https://casaemmodulos.casa).

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
| #481 | `development` | Centralized the equivalent `.visually-hidden` utility; integrated at `daede4b89525ffe4e2caafd89da9a1cda7684665` after 16/16 exact-head workflow runs succeeded. |
| #482 | `development` | Current v0.9 register readback; squash-integrated at `3a55c4486c3c93108bf276368a3a9c774ddcf3f9`. |
| #483 | `development` | Corrected LOC-006 integration evidence and removed the stale local-candidate state; integrated at `eff75d93655cb2796f1823ab3b9789c0aa9c591c`. |
| #486 | `development` | Centralized Admin materials heading and empty-state copy; integrated at `0d929f0d3898d976e3e8b510b1495ac987c3cd7f`. |
| #487 | `development` | Centralized the shared Admin pager labels; 11 exact-head gates passed; integrated at `212796fcab4b610ffa0bd721a26b823a05191a5c`. |
| #488 | `development` | Reconciled exact v0.9 evidence for completed slices and refreshed live refs; documentation only, integrated at `ea66294bae4190ac09d8793b615cf00338d0795a`. |

## Selective promotion and architecture findings

- **Normalized flow:** DOM-006 is integrated and validated in both Product destinations. The main-targeting implementation in #445 passed its exact-head gates; the last recorded production deploy was on a descendant of that integration, but production was not revalidated in this readback.
- **Admin V3:** the unsafe PUT-from-defaults path was closed by #442; its GET fallback remains a deliberate behavior to compare with development. Provider-level Identity and storage atomicity have not been proven. Netlify Identity login is not supported in `file://`, a static local server, or `netlify dev`; use a Deploy Preview for authenticated behavior.
- **Test overlap:** TST-003 reconciliation found one `npm test` call in main's `app-build-purity`. `candidate-assets` runs scoped asset/mask/provenance checks and `variant-fidelity` derives/renders variant outputs; neither repeats that app test. Keep those guarantees distinct and do not transplant a duplicate-removal change to main.
- **CSS-00:** the exact CSS baseline is still partial. The initial Config/Admin readback found distinct local bundles and other inline/dynamic CSS surfaces; the full stylesheet/selector inventory remains to be completed.
- **FND-01:** Product `development` now owns the identical `.visually-hidden` utility in `app/ui-theme.css`; PR #481 removed the duplicate Admin/Config rules and preserved Config's distinct `.sr-only`. Its exact head passed all 16 workflow runs. The Product register refresh in PR #482 keeps the family partial: CSS-00/ownership and the remaining focal focus/clip proof still need closure. Product `main` does not contain this change. Whether a Design-System-owned versioned export and Product pin are required remains a recorded architecture decision, not an assumption.
- **LOC-006:** the Admin scene-asset copy (#475), materials copy (#486), and pager labels (#487) are integrated into Product `development`. PR #486 moved the materials heading/empty-state copy into the catalog; #487 moved shared pager labels and passed 11 exact-head gates. These close bounded copy families only. LOC-006 remains partial because fixed copy across Admin/Config is not fully inventoried; Product `main` is unchanged.
- **v0.9 register:** all 125 IDs remain. At Product `development@ea66294`, the register blob is `0312567d072b6a204be0f2b6dad0c62be52e2fbb`: 3 done, 18 in progress, 104 not started; reconciliation is 12 done, 21 partial, 92 unreviewed, and 92 entries have no attached evidence. This is an inventory, not an implementation percentage. The register's baseline readback captures Product development immediately before PR #488, which changed only this document.

## Token validation and limits

At exact Design System `main@c6ff6545e9ae2071e695109fd94ac91676e7fb0a`, local checks passed after reading the source and generated outputs as canonical Git blob bytes: P-TOKEN-01 tests 6/6, P-TOKEN-02B tests 3/3, and VIS-002C v0.3 verification passed. No new hosted workflow was run on this SHA. Windows `core.autocrlf=true` converts LF files to CRLF and causes false source-hash/generated-output failures in a standard checkout; the underlying repository blobs were unchanged.

GitHub's branch-protection/ruleset API returned 403; required-check policy remains unknown. Observed workflow results do not establish protection.

This handover refresh changes documentation only. It does not change runtime, stored configuration, production content, or access-control settings.
