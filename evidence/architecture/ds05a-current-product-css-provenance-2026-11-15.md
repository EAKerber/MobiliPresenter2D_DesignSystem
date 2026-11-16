# DS-05A — comparação de proveniência CSS do Produto

**Data:** 15/11/2026 (BRT)  
**Tipo de evidência:** comparação estática de fontes Git e capturas CSSOM locais pareadas; não é validação hospedada nem aprovação visual.

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
| `app/styles.css` | `d43e6fb5e66133d2389b5c39b165b76b13cfa868` | `d1ac2b5701f215de56ff8f7c12b1d5e7dcbe47a8` | +1 / −1 | `.viewer-card__footer` fixa `rgba(255, 255, 255, 0.42)` em main e usa `var(--muted)` em development; essa diferença coincide com as leituras CSSOM de `#viewerHint`. |
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

## Capturas locais pareadas do candidato .module-number — main e development

Em 15/11/2026 (BRT), o mesmo runner comparou a regra candidata, injetada em memória, contra seis estados de cada árvore Product. O DOM real de /config/ foi inicializado com uma projeção local sintética baseada em defaults versionados; não foi usado banco nem origem externa. O app foi servido localmente pelo runner via interceptação CDP, com requisições externas bloqueadas.

A regra candidata foi idêntica nos dois pins e não foi gravada nos arquivos:

    html[data-theme="light"] .module-number { background: rgb(34 33 31 / 8%); color: var(--text); }

SHA-256 da regra: 88a531048d52807c5a0dca73f1887463d22daa4d6d70d4e926bbf118c4ad8407.

| Product pin | Identidade do checkout auxiliar | Árvore app/ verificada | Blob app/ui-theme.css | Recibo local (SHA-256) |
|---|---|---|---|---|
| development@1a69ff76a5f36e3245a288773bb409aa662e4e62 | Commit sintético ab9aafd5a55fe6483eccd50431292ef7ef040d51 | 6b5f66dab510221ebef216a3b0613fec904d10d7, igual ao pin | 36137b4264aa5b12999b286284cda227923a606a | work/_ds05a-cssom-capture-20261115-4/runtime_cssom.json — ced933e3eb696459ded4f668bed3d73a493fb7998b6870a62660632d012f8208 |
| main@46a52e76a0eeae4bed4b567b12da5311ed90b475 | Commit sintético 04b2331f4059f6d61b81122b3e4f40f96cb06d0f | 2e388a350f610e30cb24aab15bb61debd81a8941, igual ao pin | 3114bbfe0a67cbdc53757f5f50a0d035559767a6 | work/_ds05a-main-capture-46a52e76-20261115/runtime_cssom.json — 79e6ebb51ec5a8365f208ee16d4a8c6fdc0d0c942b67dded6cc2a88e136966db |

O snapshot local de main foi montado a partir da árvore de development, substituindo os 15 blobs diferentes em app/; cada blob foi conferido com o SHA retornado pela API do GitHub, e a árvore final conferiu exatamente com main. Portanto, os commits auxiliares são sintéticos, mas o conteúdo medido de app/ corresponde aos pins canônicos.

O mesmo runner (ds05a-runtime-cssom-v2.cjs, SHA-256 ab2a1e2dc68ffe19b4689a264214454c0a3dc135715bba2820cfcc5ed86ce359), Node v24.20.0 e Chrome 156.0.8078.82 capturou 390, 1050 e 1366 px nos temas claro e escuro em cada pin: seis estados pareados por árvore. Em cada estado havia sete badges de módulo.

| Árvore | Badge claro: baseline → candidata | Controle escuro | Resultado |
|---|---:|---:|---|
| development | 1,43:1 → 13,02:1 | 8,10:1, sem alteração | Os sete badges mudaram nas três larguras claras; nenhum badge mudou no tema escuro. |
| main | 1,43:1 → 13,02:1 | 8,10:1, sem alteração | Mesmo efeito nos badges; o candidato não altera o controle escuro. |

A comparação das seis baselines encontrou a mesma contagem e os mesmos valores de contraste para os sete números nas duas árvores. Também revelou uma diferença fora da candidata: #viewerHint passou pelo cálculo local como 5,22:1 no claro e 4,88:1 no escuro em development; em main, como 1,00:1 e 4,05:1, respectivamente. Isso coincide com a declaração de origem: em app/styles.css, .viewer-card__footer usa rgba(255, 255, 255, 0.42) em main e var(--muted) em development. No tema claro, --muted resolve para #706c66; no escuro, para rgba(255, 255, 255, 0.48). Depois de aplicar a candidata, essa falha separada de #viewerHint continua nos seis estados de main; a regra .module-number não a toca. Essa observação requer triagem própria e não foi corrigida neste lote.

Cada recibo guarda seis capturas claras (baseline/candidata em três larguras), com tamanho e SHA-256 de cada PNG. Os recibos e as imagens permanecem nos diretórios locais citados acima; não foram adicionados ao PR. Ambos os recibos registram seis estados baseline e seis candidate, seis pares, efeito apenas claro e controle negativo escuro inalterado.

## Limites e próximo passo

Isto mede somente os seletores e estados alcançados pela projeção sintética local. Não valida a configuração publicada, o Preview ou todas as superfícies; não é uma revisão visual completa nem prova universal de conformidade WCAG. Nenhum CSS do Produto foi alterado e nenhum gate DS-05A/G2 foi fechado. A configuração hospedada de /config/ permanece HOLD. A candidata .module-number continua restrita a este componente e aguardando revisão separada; a nova observação de #viewerHint também não autoriza uma correção automática.

## Readback de CSS após publicação da #275 — 16/11/2026

A #275 foi incorporada ao Product main por squash em `64d934dabc7cfb8175dfe2f0a5d04fe1669a41ba`. A árvore atual da main é `f7e1d4b492dadff91d85b969616618ae42cf1daf`; development permanece em `1a69ff76a5f36e3245a288773bb409aa662e4e62`, árvore `6dff4a40f1f10db8e783e3da7604c6e0144d3e10`. As duas árvores foram comparadas por path/blob: 13 CSS ainda diferem, quatro são folhas runtime e nove são referências/fixtures/snapshots não-runtime.

| Folha runtime | Product main@64d934d | Product development@1a69ff76 | Observação |
|---|---|---|---|
| `app/how-it-works/how-it-works.css` | `e70439be98b0fc7a705fd541f62e4844f6323472` | `0dff501eb14df78081f35d81ae1eca17abca85ba` | Igual ao blob de main46 documentado acima. |
| `app/landing/landing.css` | `2fd79249fc7e21f798f48906614db73860eab41c` | `3e307c155a406f91337b2e54534e0362d2c21636` | Alterado pela integração #275; o diff de linhas divulgado acima pertence ao par main46/development e não é carregado para este novo pin. |
| `app/styles.css` | `d43e6fb5e66133d2389b5c39b165b76b13cfa868` | `d1ac2b5701f215de56ff8f7c12b1d5e7dcbe47a8` | Igual ao blob de main46; diferença de `#viewerHint` continua fora do patch da Home. |
| `app/ui-theme.css` | `3114bbfe0a67cbdc53757f5f50a0d035559767a6` | `36137b4264aa5b12999b286284cda227923a606a` | Igual ao blob de main46; candidata `.module-number` não mudou na integração #275. |

Os outros nove caminhos continuam presentes somente no lado development e foram listados acima. A publicação altera a proveniência de `app/landing/landing.css`, portanto as capturas CSSOM de 15/11 não são promovidas como capturas da árvore completa main64. O seletor `.module-number` e a declaração de origem de `#viewerHint` mantêm os mesmos blobs, mas o relatório não repetiu renderização, CSSOM ou contraste no novo SHA.

A main foi publicada no deploy Netlify `6afa62020df61721601fe111`, estado `ready`, commit `64d934dabc7cfb8175dfe2f0a5d04fe1669a41ba`. Isso confirma deployment e readback do commit, não validação hospedada de `/config/`. G2/DS-05A permanecem em HOLD; nenhum CSS Product foi alterado por este lote documental.
