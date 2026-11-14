# G3 runtime — acabamento local do módulo

**Data:** 12/11/2026 (BRT)  
**Produto fixado:** `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`  
**CSS base:** blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`  
**CSS candidato:** blob `eb346a41ad91f6dc53875cb954e9018fdc1dd713`; SHA-256 `8dbe02cb5c03880ef86eff2e7d21b561bd377e184a7c8dc0fa6d8783683fb608`  
**Navegador:** Chrome `156.0.8078.82`; DPR 1; viewport `390×900` CSS px.

## Fixture e método

A configuração Buyer V5 foi criada em memória a partir dos defaults versionados. `base-light` permaneceu global e habilitado. `cocoa` e `shadow` foram habilitados como acabamentos locais de `module-01`. A validação normal da configuração e a projeção Buyer V5 foram executadas antes de abrir `/config/`; a página então abriu a ficha real do módulo e clicou nos controles reais gerados por `createLocalFinishControl()`.

O runner serviu HTML, JavaScript, CSS e assets da cópia limpa e destacada no SHA acima por rotas locais do Playwright. O endpoint local da fixture não persiste estado. Nenhuma sessão autenticada, API remota, banco, opção administrativa, publicação ou deploy foi usado.

Matriz pareada: baseline/candidato × light/dark × `cocoa`/`shadow` = **8 capturas**. Após cada clique, o ponteiro foi movido para fora e `transform:none` foi confirmado antes da captura. O relatório registra CSSOM, regras correspondentes, `aria-pressed`, seleção global e hashes SHA-256.

## Resultado

- Em 8/8 casos, o acabamento local selecionado teve `.is-selected` e `aria-pressed=true`; o outro acabamento local ficou desmarcado.
- Em 8/8, a seleção global permaneceu `base-light` (`aria-pressed=true`). A interação local alterou somente `state.localSelections` pelo handler `core.setLocalFinish`; não mudou `globalSelections`.
- Baseline: `border-color: rgb(255, 255, 255)` e `box-shadow: rgba(255, 255, 255, 0.12) 0px 0px 0px 2px`.
- Candidata: `border-color: rgb(41, 39, 35)` e `box-shadow: rgb(255, 255, 255) 0px 0px 0px 2px, rgb(41, 39, 35) 0px 0px 0px 4px`.
- As propriedades computadas do anel (cor/espessura/estilo da borda, box-shadow e transform) coincidiram entre o controle local selecionado e o global selecionado na mesma página em 8/8 casos. `outline-style` foi `none`; sua cor computada sem uso herda do texto ao redor de cada controle. O layout do wrapper continua específico de `module-detail__local-finish`.
- Não houve exceção de página nem erro HTTP inesperado.

## Capturas

| Braço | Tema | Acabamento | SHA-256 |
|---|---|---|---|
| baseline | light | cocoa | `be482afa727b7062eae45c4819d60749b0de4a33d8b21d5ef46aa4ff81d0750c` |
| baseline | light | shadow | `86de393a9a961519cdd6bdde43c206c7a675f6f10b12b24b49d3732d1fdcb7a4` |
| candidate | light | cocoa | `bbbbd6c84d425e19c352baf73f564b5a35d0a6d7baf008c6f1b433476e247dd1` |
| candidate | light | shadow | `dba8d2a5796b3c6459a8d4aacc734334bb38205f5e5ff1888ea90926ef3fc879` |
| baseline | dark | cocoa | `be482afa727b7062eae45c4819d60749b0de4a33d8b21d5ef46aa4ff81d0750c` |
| baseline | dark | shadow | `86de393a9a961519cdd6bdde43c206c7a675f6f10b12b24b49d3732d1fdcb7a4` |
| candidate | dark | cocoa | `bbbbd6c84d425e19c352baf73f564b5a35d0a6d7baf008c6f1b433476e247dd1` |
| candidate | dark | shadow | `dba8d2a5796b3c6459a8d4aacc734334bb38205f5e5ff1888ea90926ef3fc879` |

The images are in [`g3-module-local-swatch-runtime-2026-11-12/`](g3-module-local-swatch-runtime-2026-11-12/); [`result.json`](g3-module-local-swatch-runtime-2026-11-12/result.json) contains the compact machine-readable receipt. Light and dark images are byte-identical for each arm/finish because the measured local swatch and wrapper rules are theme-independent in these states; the receipt still records that both theme modes were applied.

## G3 classification and limits

`.swatch` has two real consumers on `/config/`: global finish controls and module-local finish controls. The selected-ring appearance is shared within this route; selection ownership is intentionally different (whole configuration versus one module). No `.swatch` consumer in another route was confirmed, so this evidence does not propose cross-route extraction.

This closes the runtime gap for this G3 ownership row. It does **not** close G2's hosted review: the hosted `/config/` preview still rejects its published configuration. This capture also does not cover keyboard focus, hover, zoom, Safari/iPad, other control families, or persisted administrative settings.

