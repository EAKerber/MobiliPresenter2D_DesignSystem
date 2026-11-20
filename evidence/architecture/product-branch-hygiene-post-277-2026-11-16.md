# Product branch hygiene readback after PR #277 — 16/11/2026 (BRT)

## Approved target and precondition

The user explicitly authorized removal of exactly `fix/how-video-fullscreen-control-20261116` at SHA `1d1f68a19836830f071a153e1a3ee11ca1446410`.

Before deletion, GitHub readback showed:
- Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`, tree `439fb0fc9a3295f9e45486198e9de83fca8376ee`.
- Target branch unprotected at `1d1f68a19836830f071a153e1a3ee11ca1446410`; its commit tree was also `439fb0fc9a3295f9e45486198e9de83fca8376ee`.
- PR [#277](https://github.com/EAKerber/MobiliPresenter2D/pull/277) was closed and merged; no open PR used this branch.
- Product had 6 refs. This was the only target in the authorization.

## Operation and readback

The remote ref was deleted with an explicit force-with-lease for the exact expected SHA. Git returned `[deleted]`. A subsequent GitHub readback confirmed:
- The branch no longer appears in the Product branch list.
- Product now has 5 refs: `main@efc40584`, `development@1a69ff76`, `codex/ds04-208-preview-batch-20261111@a6c64305`, `codex/nav005-public-compact-main-20261110@43c9f566` and `docs/arc13-post-273-reconciliation-20261114@68441080`.
- Product `main` remains `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` with tree `439fb0fc9a3295f9e45486198e9de83fca8376ee`; no PR was merged and no deployment changed.
- The open PR set remains #269, #271 and #274; none points to the removed branch.

The PR #277 and deployed Product contents remain integrated. The deleted branch name no longer directly references its original head. This hygiene action reduces refs from 6 to 5; five is the review threshold/soft cap, not a hard cap. The stable target remains `main` plus `development` (2 refs).

## Scope

No application files were changed; the action affected only this exact remote branch ref. No application content or production deployment was changed.
