# Current operational handover — v0.9 plan execution

**Readback:** 2026-11-25 15:08 UTC. Point-in-time snapshot. Refresh exact refs, PRs, deployments, and access controls before dependent operations. This document is proposed in open Design System PR #137 and is not on Design System `main`.

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
| Product | `development` | `6e043ee7fb399d1599840c8d07fc57ec2dcf31e3` |
| Design System | `main` | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |
| Design System | `development` | not found (GitHub returned 404) |

Product `main` and `development` diverge from merge base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. The GitHub compare file list is capped; it is not a complete file-level promotion audit. Promotion remains selective.

Netlify production deploy `6b06ed3909631cffb66b2d7b` is READY on Product `main` at `e462f5df33e2354c81bbbc18170106c1a9d79ead`. The site is `https://casaemmodulos.casa`.

## Open work and disposition

| PR | Base | Intent / current disposition |
|---|---|---|
| Product #400 | `main` | Branch-hygiene maintenance candidate; its description is not evidence that any ref has been deleted. |
| Product #407 | `main` | Make the Viewer pricing gate reachable on main-targeting PRs; CI-only change. |
| Product #432 | `main` | Test-only CAS race and missing-readback assertions. Open; integration remains separately authorized. |
| Product #442 | `main` | Prevent Admin PUT from writing fallback defaults when V3 state is absent or invalid; preserve the documented GET fallback. Open at head `f6f75cbdb1d1cb07b39ba69d2a4801c3cd2bbcfd`; all nine triggered workflows passed, and its Deploy Preview is READY. Integration is pending because it targets production `main`. |
| Design System #137 | `main` | This handover refresh only; documentation candidate, not integrated. |

Product PR #441 has been squash-merged into `development` at `6e043ee7fb399d1599840c8d07fc57ec2dcf31e3`; it added four approved private-navigation labels from the copy catalog.

## Selective promotion findings

The shared V5 read/inspection/save core matches between Product `main` and `development`. PR #432 adds deterministic concurrent-CAS and missing-readback assertions to `main`; it changes tests only.

The Admin endpoint differs on absent or invalid V3 data. Product `main` preserves the historical GET fallback but previously allowed PUT to use fallback defaults as the basis of a write. PR #442 closes that write path, returns conflict without storage mutation, handles Identity failure explicitly, and applies the shared Admin authorization policy. Its test and deployment gates pass on the exact PR head. It remains unintegrated pending the required main publication decision. This does not establish hosted Identity behavior or provider-level atomicity.

## Validation and access limits

- The local full test suite and the Buyer projection/authorization boundary checks passed for PR #442's exact candidate.
- All nine PR-triggered GitHub Actions workflows passed for `f6f75cbdb1d1cb07b39ba69d2a4801c3cd2bbcfd`; Netlify Deploy Preview #442 is READY at `https://deploy-preview-442--mobilipresenter2d.netlify.app`.
- Netlify production remains on Product `main` at `e462f5df33e2354c81bbbc18170106c1a9d79ead`; PR #442 has not changed production.
- GitHub's branch-protection API returned 403 in the prior live check. Required checks and rulesets remain unknown; observed workflow runs do not prove required-check policy.
- The Design System development branch lookup returned 404.
- Documentation and test-only changes do not establish production deployment or completion of the v0.9 plan.

This handover refresh changes documentation only. It does not change runtime, stored configuration, production content, or access-control settings.
