# Current operational handover — v0.9 plan execution

**Readback:** 2026-11-25 13:21 UTC. This is a point-in-time snapshot. Re-read live refs, PRs, deploys, and access controls before any Git or publication operation. This file is the head of open Design System PR #137; until that PR is integrated, Design System `main` remains at its separately verified SHA.

## Authority hierarchy

1. **Method and intended DoD:** this repository's [Plano Diretor v0.9](architecture/MOBILIPRESENTER2D_PLANO_DIRETOR_CONSOLIDADO_v0.9.md), blob `59bb530b14172eb9772b9f89bb62272173f4381c`.
2. **Execution state:** Product's single [125-ID operational register](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/architecture/plan-v0.9-execution-register.json). Read its live blob and state dimensions; a partial implementation is not a completed item.
3. **Design decisions:** this repository's [`decisions.json`](../decisions.json), blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`.
4. **Implementation and consumers:** exact Product source at the confirmed ref; code and its consumers decide what is implemented.
5. **Validation:** source-pinned test crosswalks and exact test/Actions receipts. Keep local, hosted, Preview, production, and approval evidence distinct.

Historical handovers and archives remain preserved. Their dated state and instructions are not live authorization.

## Live repository readback

| Repository | Ref | SHA |
|---|---|---|
| Product | `main` | `01ded2c100fbfd8b16897e26113dc5068a83e429` |
| Product | `development` | `cc495684f8ace2c4d84443022d79ecd48a6ad47b` |
| Design System | `main` | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` |
| Design System | `development` | not found (GitHub returned 404) |

Product main and development are divergent from merge base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. GitHub's compare response returned a capped file list, so it is not a complete file-by-file promotion audit. Promotion remains selective.

The confirmed Netlify production deploy is `6b045acbbb56d5e17bde8f8a`, READY on Product main at `01ded2c100fbfd8b16897e26113dc5068a83e429`.

## Open work requiring live disposition

| PR | Base | Head SHA | Intent / current disposition |
|---|---|---|---|
| Product #400 | `main` | `d1fe79faafa1ed7345aff8afeb33bbf5e4a21e22` | Branch-retirement maintenance candidate. Its recorded audits did not apply deletions; do not infer that a ref was removed. |
| Product #407 | `main` | `b986159d0c9d87d57aa5133eca9d26b2f8b31137` | Make the Viewer pricing gate reachable on main-targeting PRs; separate from runtime promotion. |
| Product #432 | `main` | `8ebfdad9ef335bf0a9701718ebd947162adea2c3` | Test-only CAS concurrency and missing-readback assertions. Seven triggered gates passed and its Preview is READY. Merge awaits the user's specific authorization; no runtime code changes. |
| Product #433 | `development` | `2db41c0739c1126fa69db71822dda6c368095345` | Refresh Product entry points and mark old dated handovers historical; documentation only. |
| Design System #137 | `main` | this PR head | Refresh this live handover; documentation only. |

None of these rows alone establishes approval, required-check policy, production deployment, or branch retirement. Re-read each PR before acting.

## Selective promotion findings

The V5 shared read/inspection/save core is byte-identical between the current Product main and development snapshots. A bounded test-only candidate is prepared in Product #432.

The Admin endpoint has a behavioral difference: main may substitute defaults for missing/invalid V3 state, while development returns an explicit missing/invalid result. That can affect first-run and recovery behavior; the handler, its tests, and a main-reachable endpoint gate require a bounded policy decision before promotion. The V5 test evidence does not settle that V3 behavior.

## Validation and access limits

- Product's V5 read/save tests pass locally against blobs that match the development source; the Blob/Identity doubles do not prove hosted Identity or provider-level atomicity under independent-instance contention.
- The branch-protection endpoints returned 403 through the connected GitHub app. Required checks and rulesets are **UNKNOWN**; observed workflow runs are not proof that a status is required.
- The Design System development branch lookup returned 404.

No runtime, stored configuration, production content, or access-control setting was changed as part of this handover update.
