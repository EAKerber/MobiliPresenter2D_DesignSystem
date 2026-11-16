# DS-05A — comparação de proveniência CSS do Produto

**Data:** 15/11/2026 (BRT)  
**Tipo de evidência:** comparação estática de fontes Git; não é captura CSSOM nem aprovação visual.

## Pins consultados

- Product `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`, árvore `e40a01d7e5abdd6ecf3c1c313568c8dc50f37061`.
- Product `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, árvore `6dff4a40f1f10db8e783e3da7604c6e0144d3e10`.
- Merge-base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; a comparação está divergente: 434 commits à frente e 2 atrás.

## Resultado da comparação

O compare completo contém 300 caminhos. Treze arquivos `.css` diferem; quatro são folhas runtime em `app/**`, com total de **41 adições e 12 remoções**. Os nove restantes são uma referência de paleta, fixtures e snapshots arquivados de reconciliação. Não os trate como CSS ativo do produto.

| Folha runtime | Blob em main | Blob em development | Diff | Observação de origem |
|---|---|---|---:|---|
| `app/how-it-works/how-it-works.css` | `e70439be98b0fc7a705fd541f62e4844f6323472` | `0dff501eb14df78081f35d81ae1eca17abca85ba` | +6 / −0 | Regra estreita até 290 px para padding e tamanho do título. |
| `app/landing/landing.css` | `8df2c39d1993a6e6b4da8bb4dcd2289c7f50eb79` | `3e307c155a406f91337b2e54534e0362d2c21636` | +24 / −7 | Escopos de header público, CTA do menu e larguras estreitas. |
| `app/styles.css` | `d43e6fb5e66133d2389b5c39b165b76b13cfa868` | `d1ac2b5701f215de56ff8f7c12b1d5e7dcbe47a8` | +1 / −1 | Cor do rodapé do viewer troca literal RGBA por `var(--muted)`. |
| `app/ui-theme.css` | `3114bbfe0a67cbdc53757f5f50a0d035559767a6` | `36137b4264aa5b12999b286284cda227923a606a` | +10 / −4 | Toggle distingue header público/privado; foco usa `--ui-theme-focus`. |

Os nove caminhos não runtime são:

- `design-system/pins/vis-002/v0.1.0/approved-palette-reference.css`
- `docs/design-system/review-lab/tools/_fixture/app/admin/admin.css`
- `docs/design-system/review-lab/tools/_fixture/app/styles.css`
- `docs/design-system/review-lab/tools/_fixture/app/ui-theme.css`
- `docs/reconciliation/ci-v5-nav-clean/source/app/styles.css`
- `docs/reconciliation/main-authority/public-legacy/viewer-editorial/app/viewer/viewer.css`
- `docs/reconciliation/ux04-main-authority/legacy/app/admin/admin.css`
- `docs/reconciliation/ux04-main-authority/legacy/app/styles.css`
- `docs/reconciliation/vis002/legacy/audit/evidence/visual/public-text-contrast-candidate-v1.css`

## Limites e próximo gate

Esta leitura compara blobs e patches dos dois commits. Não mede estilos computados, contraste, comportamento nem equivalência visual. Não houve alteração de CSS no Produto nem execução de suíte nesta atualização.

O checkout local de desenvolvimento mantém alterações não commitadas e não é baseline; a regra candidata `.module-number` não pertence aos quatro blobs de runtime acima. Preserve esse trabalho local sem promovê-lo. A divergência de 434/2 também não autoriza mesclar `development` integralmente em `main`.

## Captura local do candidato `.module-number` em development

Em 15/11/2026, o runner local `work/_ds05a-cssom-paired-local/scripts/ds05a-runtime-cssom-v2.cjs` mediu o DOM real de `/config/` em uma projeção sintética local, sem banco ou origem externa.

- O Product canônico foi `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`; a árvore `app/` `6b5f66dab510221ebef216a3b0613fec904d10d7` e a folha `app/ui-theme.css` `36137b4264aa5b12999b286284cda227923a606a` correspondem ao pin. O checkout auxiliar é sintético (`ab9aafd5a55fe6483eccd50431292ef7ef040d51`), não tem a mesma identidade de commit.
- A regra candidata, injetada somente em memória e apenas no tema claro, foi `html[data-theme="light"] .module-number { background: rgb(34 33 31 / 8%); color: var(--text); }` (SHA-256 `88a531048d52807c5a0dca73f1887463d22daa4d6d70d4e926bbf118c4ad8407`).
- Seis pares foram capturados em 390, 1050 e 1366 px, claro/escuro. Os sete números dos módulos mudaram em cada largura clara; a ferramenta calculou 1,43:1 no baseline e 13,02:1 com a candidata. Nos três controles escuros, nenhum badge mudou. Foram salvas seis capturas.
- Runner SHA-256 `ab2a1e2dc68ffe19b4689a264214454c0a3dc135715bba2820cfcc5ed86ce359`; Node `v24.20.0`; Chrome `156.0.8078.82`. O recibo local `work/_ds05a-cssom-capture-20261115-4/runtime_cssom.json` tem SHA-256 `ced933e3eb696459ded4f668bed3d73a493fb7998b6870a62660632d012f8208`.

É uma medição restrita ao pin development e a essa candidata. Não compara a árvore app de main, não altera CSS, não confirma comportamento publicado ou conformidade universal, e não fecha DS-05A/G2. A configuração hospedada de `/config/` continua HOLD.

## Próximo gate

Repetir a medição contra o pin canônico atual `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`, mantendo fixture, candidato, dimensões e captura iguais; então comparar os pares main/development. Preparar a cópia main a partir do commit exato, registrar a identidade e os blobs completos, e manter o resultado isolado de qualquer mudança de runtime. O erro hospedado de `/config/` segue sem solução e requer validação autorizada própria.
