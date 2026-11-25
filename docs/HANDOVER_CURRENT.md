# Current operational handover — v0.9 plan execution

**Readback:** 2026-11-25 13:28 UTC. Point-in-time snapshot; refresh exact refs, PRs, deployments, and access controls before dependent operations. This document is proposed in open Design System PR #137 and is not yet on Design System `main`.

## Authority hierarchy

1. **Method and intended DoD:** [Plano Diretor v0.9](architecture/MOBILIPRESENTER2D_PLANO_DIRETOR_CONSOLIDADO_v0.9.md), blob `59bb530b14172eb9772b9f89bb62272173f4381c`.
2. **Execution state:** Product's single [125-ID operational register](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/architecture/plan-v0.9-execution-register.json); re-read its current blob before relying on status.
3. **Design decisions:** [decisions.json](../decisions.json), blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`.
4. **Implementation:** exact Product source and consumers at the named remote ref.
5. **Validation:** source-pinned crosswalks and exact test/Actions receipts. Local, hosted, Preview, production, and approval evidence remain distinct.

Historical records are preserved as provenance. Their dated state and operational instructions are not current authorization.

## Live repository readback

| Repository | Ref | SHA |
|---|---|---|
| Product | `main` | `01ded2c100fbfd8b16897e26113dc5068a83e429` |
| Product | `development` | `c1cc51bd557b5dd564d1f5888791b3e96da29b68` |
| Design System | `main` | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |
| Design System | `development` | not found (GitHub returned 404) |

Product main and development diverge from merge base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. GitHub's compare response capped its file list, so it is not a complete file-level promotion audit. Promotion remains selective.

Netlify production deploy `6b045acbbb56d5e17bde8f8a` was READY on Product main at `01ded2c100fbfd8b16897e26113dc5068a83e429` at last readback.

## Open work and disposition

| PR | Base | Intent / current disposition |
|---|---|---|
| Product #400 | `main` | Branch-retirement maintenance candidate. Recorded audit did not apply deletions; no retirement is inferred. |
| Product #407 | `main` | Make the Viewer pricing gate reachable on main-targeting PRs; separate from runtime promotion. |
| Product #432 | `main` | Test-only CAS race and missing-readback assertions. Seven triggered gates passed and Preview was READY. Merge requires its specific approval; no runtime changes. |
| Design System #137 | `main` | This handover refresh only; documentation candidate, not integrated. |

Product PR #433 has since been squash-merged into development at `c1cc51bd557b5dd564d1f5888791b3e96da29b68`. It refreshed Product entry points and marked dated handovers historical, preserving their contents.

## Selective promotion findings

The shared V5 read/inspection/save core matches between Product main and development. The test-only candidate in Product #432 adds deterministic concurrent-CAS and missing-readback assertions.

The Admin endpoint still differs: main may substitute defaults for missing or invalid V3 state, while development returns explicit missing/invalid results. This may affect first-run and recovery behavior. Keep the handler, its tests, and a main-reachable endpoint gate on hold until the policy is decided. V5 test evidence does not settle this V3 behavior.

## Validation and access limits

- Five V5 read/save tests passed locally against source blobs matching Product development. Test doubles do not prove hosted Identity behavior or provider-level atomicity under independent-instance contention.
- GitHub's branch-protection API returned 403. Required checks and rulesets remain unknown; observed workflow runs do not prove required-check policy.
- The Design System development branch lookup returned 404.
- Documentation and test-only changes do not establish a production deployment or completion of the v0.9 plan.

No runtime, stored configuration, production content, or access-control setting changed as part of this handover update.
