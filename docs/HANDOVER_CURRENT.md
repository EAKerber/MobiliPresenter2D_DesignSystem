# Current operational handover — v0.9 plan execution

**Readback:** 2026-11-25 15:30 UTC. Point-in-time snapshot; refresh exact refs, PRs, deployments, and access controls before dependent operations. This document is proposed in open Design System PR #137 and is not on Design System `main`.

## Authority hierarchy

1. **Method and intended DoD:** [Plano Diretor v0.9](architecture/MOBILIPRESENTER2D_PLANO_DIRETOR_CONSOLIDADO_v0.9.md), blob `59bb530b14172eb9772b9f89bb62272173f4381c`.
2. **Execution state:** Product's [125-ID operational register](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/architecture/plan-v0.9-execution-register.json); re-read its current blob before relying on any task status.
3. **Design decisions:** [decisions.json](../decisions.json), blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`.
4. **Implementation:** exact Product source and consumers at the named remote ref.
5. **Validation:** source-pinned crosswalks and exact test/Actions receipts. Local, hosted, Preview, production, and approval evidence remain distinct.

Historical records are preserved as provenance. Their dated state and operational instructions are not current authorization.

## Live repository readback

| Repository | Ref | SHA |
|---|---|---|
| Product | `main` | `e462f5df33e2354c81bbbc18170106c1a9d79ead` |
| Product | `development` | `02c6ace2c59b96a11e3a2c87ab444eae00a27f3b` |
| Design System | `main` | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |
| Design System | `development` | not found (GitHub returned 404) |

Product `main` and `development` diverge from merge base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. GitHub's compare file list is capped; it is not a complete file-level promotion audit. Promotion remains selective.

Netlify production deploy `6b06ed3909631cffb66b2d7b` is READY on Product `main` at `e462f5df33e2354c81bbbc18170106c1a9d79ead`. The site is `https://casaemmodulos.casa`.

## Open work and disposition

| PR | Base | Intent / current disposition |
|---|---|---|
| Product #400 | `main` | Branch-hygiene maintenance candidate; its description is not evidence that any ref has been deleted. |
| Product #407 | `main` | Make the Viewer pricing gate reachable on main-targeting PRs; CI-only change. |
| Product #432 | `main` | Test-only CAS race and missing-readback assertions. Open; integration remains separately authorized. |
| Product #442 | `main` | Prevent Admin PUT from writing fallback defaults when V3 state is absent or invalid; preserve the documented GET fallback. All nine triggered workflows passed; Deploy Preview #442 is READY at `https://deploy-preview-442--mobilipresenter2d.netlify.app`. Open; merge would publish to production. |
| Product #445 | `main` | Use `NormalizedConfiguratorFlow` for stage navigation, ownership, and item availability; refresh the ARC-13 report. All nine triggered workflows passed; Deploy Preview #445 is READY at `https://deploy-preview-445--mobilipresenter2d.netlify.app`. Open; merge would publish to production. |
| Design System #137 | `main` | This handover refresh only; documentation candidate, not integrated. |

Product PR #443 integrated the normalized-flow consumer correction into `development` at `5c89e08e3a700e640f31927fd01d6c8373b6d64f`; all ten exact-head workflows passed. Product PR #444 integrated the adversarial Buyer DTO projection test and execution-register reconciliation into `development` at `02c6ace2c59b96a11e3a2c87ab444eae00a27f3b`; all nine exact-head workflows passed.

## Selective promotion findings

- The V5 read/inspection/save core matches between Product `main` and `development`. PR #432 adds deterministic concurrent-CAS and missing-readback assertions to `main`; it changes tests only.
- Admin behavior differs for missing or invalid V3. PR #442 closes the unsafe PUT-from-defaults path while preserving the historical GET fallback, and adds the shared Admin policy/Identity error handling. Hosted Identity and provider-level atomicity remain unproven.
- DOM-006 is implemented and validated in Product `development`. PR #445 prepares the equivalent consumer-authority correction for `main`; it is not integrated.
- DOM-001 remains partial. PR #444 added and integrated nested DTO allowlist assertions, but the wider schema/default/pricing/compatibility inventory and its CMP-001 dependency remain open.

## Validation and access limits

- Local flow suites passed 4/4 for the candidate changes. PR #442 local full tests and Buyer boundary checks passed; PR #444's projection test passed 1/1.
- All exact-head Actions workflows passed for PRs #442, #443, #444, and #445. The PR #442 and #445 Deploy Previews are READY; these states are separate from production.
- Netlify production remains on Product `main` at `e462f5df33e2354c81bbbc18170106c1a9d79ead`; neither main-targeting PR has changed production.
- The protected `/config/` route was not reviewed in an authenticated session for these candidates. No hosted Identity/cookie behavior or provider-level atomicity is claimed.
- GitHub's branch-protection API returned 403 in the previous live check. Required checks and rulesets remain unknown; observed workflow runs do not prove required-check policy.

This handover refresh changes documentation only. It does not change runtime, stored configuration, production content, or access-control settings.
