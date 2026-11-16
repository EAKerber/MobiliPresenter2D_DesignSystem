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

O próximo subgate DS-05A é preparar cópias limpas e detached dos dois pins, carregar a mesma fixture sintética local em cada uma, e registrar CSSOM e capturas pareadas no Chromium real. Incluir os estados e seletores do Configurador necessários ao escopo, hashes dos quatro blobs, dimensões/tema e resultado por par. A falha hospedada de `/config/` no Preview #271 continua HOLD; a fixture local não substitui sua validação nem prova dados publicados. Até concluir esse gate, não extrair tokens, não promover `.module-number` e não declarar G2 aprovado.
