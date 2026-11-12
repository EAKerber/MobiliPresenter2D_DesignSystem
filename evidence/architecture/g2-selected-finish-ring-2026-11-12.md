# G2 — A/B do anel de acabamento selecionado (2026-11-12, BRT)

**Resultado do subgate local:** a regra candidata torna o acabamento selecionado mais fácil de identificar nas combinações claras/escuras observadas. Os 40 estados (16 sem hover, 16 com hover e 8 com foco visível por teclado) terminaram com a seleção real ativa, `aria-pressed="true"`, tema solicitado/resolvido coincidente e configuração Buyer V5 validada. Isto registra a evidência do anel; não fecha G2 nem os critérios amplos de #208/#216.

## Identidade e método

- Produto: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, checkout detached limpo.
- CSS base: `app/styles.css` Git blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`.
- CSS candidata, idêntica ao blob em Product #271: `app/styles.css` Git blob `eb346a41ad91f6dc53875cb954e9018fdc1dd713`; SHA-256 `8dbe02cb5c03880ef86eff2e7d21b561bd377e184a7c8dc0fa6d8783683fb608`.
- Fluxo real do Configurador: avançou para Acabamentos e clicou nos botões reais `.swatch[data-finish-id]` para `base-light` e `shadow`. Defaults do Buyer V5 foram projetados localmente.
- Matriz pareada: base/candidata × light/dark × 390×900 e 1366×900 CSS px × Base clara/Carvão. São 16 capturas sem hover, 16 com hover e 8 com `:focus-visible` por teclado (40 PNGs no total). Chrome 156.0.8078.82, DPR 1; 390 px usa layout compact e 1366 px side-rail.
- As requisições foram roteadas para arquivos locais. Sem Netlify, autenticação, banco ou serviço externo.
- Captura sem hover: depois de cada seleção, o ponteiro foi movido para `(0,0)` e o CSSOM aguardado até `transform === "none"`.
- Captura hover: o ponteiro permaneceu sobre o swatch selecionado; a captura aguardou `:hover` e a transformação final `matrix(1.06, 0, 0, 1.06, 0, 0)`, mais 200 ms de estabilização. O estado ativo e `aria-pressed` foram rechecados para cada captura.
- Captura de foco: o ponteiro foi movido para `(0,0)`; o foco foi navegado por Tab/Shift+Tab até o swatch selecionado. A fixture confirmou `:focus-visible`, `transform:none`, seleção ativa e `aria-pressed=true` em todos os oito casos mobile.

## CSSOM e observação visual

| Braço | Borda selecionada | `box-shadow` |
|---|---|---|
| Base | `rgb(255, 255, 255)` | `rgba(255, 255, 255, 0.12) 0 0 0 2px` |
| Candidata | `rgb(41, 39, 35)` (`#292723`) | `rgb(255, 255, 255) 0 0 0 2px, rgb(41, 39, 35) 0 0 0 4px` |

Na captura mobile, o swatch Carvão ficou mais nítido sobre a superfície clara e Base clara ganhou contorno identificável no tema escuro. A dupla borda branca/escura também preserva o contraste interno do Carvão no tema escuro; o anel exterior escuro se mistura à superfície escura, sem remover o anel branco. O estado ativo foi confirmado pelo DOM em todos os casos, e não inferido apenas pelo CSS.

### Capturas sem hover por viewport, tema e acabamento

| Viewport | Tema | Acabamento | Base | Candidata |
|---:|---|---|---|---|
| 390×900 | light | Base clara | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-light-390-base-light.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-light-390-base-light.png) |
| 390×900 | light | Carvão | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-light-390-shadow.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-light-390-shadow.png) |
| 390×900 | dark | Base clara | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-dark-390-base-light.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-dark-390-base-light.png) |
| 390×900 | dark | Carvão | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-dark-390-shadow.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-dark-390-shadow.png) |
| 1366×900 | light | Base clara | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-light-1366-base-light.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-light-1366-base-light.png) |
| 1366×900 | light | Carvão | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-light-1366-shadow.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-light-1366-shadow.png) |
| 1366×900 | dark | Base clara | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-dark-1366-base-light.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-dark-1366-base-light.png) |
| 1366×900 | dark | Carvão | [PNG](g2-selected-finish-ring-2026-11-12%2Fbaseline-dark-1366-shadow.png) | [PNG](g2-selected-finish-ring-2026-11-12%2Fcandidate-dark-1366-shadow.png) |

### Capturas com hover no swatch selecionado

Em 16/16 casos, base e candidata computaram o mesmo transform de hover e mantiveram o item selecionado. A diferença de ring continua no `box-shadow` registrado acima; a transformação amplia a caixa visível para cerca de 46,64×46,64 px nos swatches mobile (CSS layout base 44×44 px).

| Viewport | Tema | Acabamento | Base em hover | Candidata em hover |
|---:|---|---|---|---|
| 390×900 | light | Base clara | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-light-390-base-light.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-light-390-base-light.png) |
| 390×900 | light | Carvão | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-light-390-shadow.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-light-390-shadow.png) |
| 390×900 | dark | Base clara | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-dark-390-base-light.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-dark-390-base-light.png) |
| 390×900 | dark | Carvão | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-dark-390-shadow.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-dark-390-shadow.png) |
| 1366×900 | light | Base clara | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-light-1366-base-light.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-light-1366-base-light.png) |
| 1366×900 | light | Carvão | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-light-1366-shadow.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-light-1366-shadow.png) |
| 1366×900 | dark | Base clara | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-dark-1366-base-light.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-dark-1366-base-light.png) |
| 1366×900 | dark | Carvão | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fbaseline-dark-1366-shadow.png) | [PNG](g2-selected-finish-ring-hover-2026-11-12%2Fcandidate-dark-1366-shadow.png) |


### Capturas com `:focus-visible` por teclado

O recorte de foco cobre 390×900 CSS px em light/dark, acabamento Base clara/Carvão e CSS base/candidata (8 PNGs). Os oito elementos mantiveram `:focus-visible`, a seleção e `aria-pressed=true`; `:hover` ficou inativo e o ring selecionado permaneceu no CSSOM. O outline teve 2 px e a mesma cor entre base/candidata em cada tema:

| Tema | Outline computado |
|---|---|
| light | `rgb(110, 81, 46) solid 2px` |
| dark | `rgb(216, 188, 124) solid 2px` |

A inspeção visual mobile não mostrou clipping do outline na área do swatch.

| Viewport | Tema | Acabamento | Base com foco | Candidata com foco |
|---:|---|---|---|---|
| 390×900 | light | Base clara | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fbaseline-light-390-base-light.png) | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fcandidate-light-390-base-light.png) |
| 390×900 | light | Carvão | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fbaseline-light-390-shadow.png) | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fcandidate-light-390-shadow.png) |
| 390×900 | dark | Base clara | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fbaseline-dark-390-base-light.png) | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fcandidate-dark-390-base-light.png) |
| 390×900 | dark | Carvão | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fbaseline-dark-390-shadow.png) | [PNG](g2-selected-finish-ring-focus-visible-2026-11-12%2Fcandidate-dark-390-shadow.png) |

O [recibo JSON](g2-selected-finish-ring-2026-11-12/result.json) contém os 40 estados, CSSOM, tema, interação, seleção acessível, SHA-256 de cada PNG e erros HTTP por caso.

## Limites e próximo passo

Houve um HTTP 404 da bundle privada `/core/private-navigation.bundle.js` em cada contexto, ausente no checkout local; não houve erro de página e o estado Buyer V5 foi validado. As capturas cobrem hover somente no swatch selecionado e foco visível somente nesse swatch em mobile; não cobrem a navegação completa por teclado, foco em outros controles, zoom ou Safari/iPad. Também não cobrem configuração hospedada nem o restante de #208/#216. A rota hospedada `/config/` continua sem configuração publicada válida, então a revisão hospedada do anel ainda não foi possível. O subgate de labels do Admin de #271 passou na revisão autenticada do Preview, conforme [recibo CSSOM do Admin](g2-admin-initial-state-labels-cssom-2026-11-12.md). G2 permanece em andamento; nenhuma mudança de código foi integrada à Product `main`.
