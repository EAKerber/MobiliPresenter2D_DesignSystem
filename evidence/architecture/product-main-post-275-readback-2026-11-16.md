## Product — readback da main após a #275

**Data:** 16/11/2026 (BRT)  
**Fonte:** GitHub e Netlify, leitura dos refs/PRs/workflows/deploy. Este recibo não altera refs nem deploys. O detalhamento é um instantâneo, não uma regra de aprovação futura.

### Publicação

- PR #275: merged, squash, merge commit `64d934dabc7cfb8175dfe2f0a5d04fe1669a41ba`; head original `3481ade561deddf561de57225cf8a65491b34654`, base anterior `46a52e76a0eeae4bed4b567b12da5311ed90b475`. Merge lido em `2026-11-16T01:53:04Z`.
- `main` aponta para `64d934dabc7cfb8175dfe2f0a5d04fe1669a41ba`, árvore `f7e1d4b492dadff91d85b969616618ae42cf1daf`.
- Deploy de produção Netlify `6afa62020df61721601fe111`: `ready`, branch `main`, commit `64d934dabc7cfb8175dfe2f0a5d04fe1669a41ba`, publicado em `2026-11-16T01:53:43Z`.
- 11/11 workflows no SHA exato terminaram em `success`, incluindo `Public production read-only verification`, `App build purity`, `Current variant fidelity`, os gates Summary pricing/Stone/Mobile/Keyboard browser, `Branch hygiene`, `Public routing before Clerk` e `Current asset gates`. São os resultados já associados à publicação; nenhuma suíte foi executada pela atualização documental posterior.

### PRs abertas e bases

| PR | Estado | Head | Base observada | Readback |
|---|---|---|---|---|
| #269 | Draft, aberta | `43c9f5662aa666d655be72a0e39b4b12ae11461a` | `46a52e76a0eeae4bed4b567b12da5311ed90b475` | 18 caminhos; API reporta não mergeável. |
| #271 | Aberta, não Draft | `a6c64305e4e595f2d0ce8d3db37b8a126a2e23d2` | `46a52e76a0eeae4bed4b567b12da5311ed90b475` | 4 caminhos; API reporta mergeável, mas base está desatualizada. |
| #274 | Draft, aberta | `68441080f1ba29f546e6f97926e487a945f7fa2f` | `46a52e76a0eeae4bed4b567b12da5311ed90b475` | 39 caminhos sem `app/**`; API reporta não mergeável; ARC-13 continua pinado na main anterior à #275. |

Todos os resultados de mergeability são observações do instante do readback; reconsultar após qualquer atualização de branch.

### Refs do Product

Seis branches remotas foram observadas:

- `main@64d934dabc7cfb8175dfe2f0a5d04fe1669a41ba`
- `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`
- `codex/ds04-208-preview-batch-20261111@a6c64305e4e595f2d0ce8d3db37b8a126a2e23d2`
- `codex/nav005-public-compact-main-20261110@43c9f5662aa666d655be72a0e39b4b12ae11461a`
- `docs/arc13-post-273-reconciliation-20261114@68441080f1ba29f546e6f97926e487a945f7fa2f`
- `fix/home-hero-group-a11y-20261114@3481ade561deddf561de57225cf8a65491b34654`

A última branch não está protegida e sua árvore é igual à main após squash; o commit original não é ancestral de main. Nenhuma PR aberta aponta para ela. É um candidato concreto para revisar a contagem de 6 para 5, mas este recibo não autoriza exclusão. A autorização anterior para outro alvo não abrange esta branch; qualquer remoção exige nome, SHA e plano explícitos, seguidos de readback.