# G2 — A/B do anel de acabamento selecionado (2026-11-12, BRT)

**Resultado do subgate local:** a regra candidata torna o acabamento selecionado mais fácil de identificar nas combinações claras/escuras observadas. Os 16 estados terminaram com a seleção real ativa, `aria-pressed="true"`, tema solicitado/resolvido coincidente e configuração Buyer V5 validada. Isto registra a evidência do anel; não fecha G2 nem os critérios amplos de #208/#216.

## Identidade e método

- Produto: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, checkout detached limpo.
- CSS base: `app/styles.css` Git blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`.
- CSS candidata, idêntica ao blob em Product #271: `app/styles.css` Git blob `eb346a41ad91f6dc53875cb954e9018fdc1dd713`; SHA-256 `8dbe02cb5c03880ef86eff2e7d21b561bd377e184a7c8dc0fa6d8783683fb608`.
- Fluxo real do Configurador: avançou para Acabamentos e clicou nos botões reais `.swatch[data-finish-id]` para `base-light` e `shadow`. Defaults do Buyer V5 foram projetados localmente.
- Matriz pareada: base/candidata × light/dark × 390×900 e 1366×900 CSS px × Base clara/Carvão (16 capturas). Chrome 156.0.8078.82, DPR 1; 390 px usa layout compact e 1366 px side-rail.
- As requisições foram roteadas para arquivos locais. Sem Netlify, autenticação, banco ou serviço externo.

## CSSOM e observação visual

| Braço | Borda selecionada | `box-shadow` |
|---|---|---|
| Base | `rgb(255, 255, 255)` | `rgba(255, 255, 255, 0.12) 0 0 0 2px` |
| Candidata | `rgb(41, 39, 35)` (`#292723`) | `rgb(255, 255, 255) 0 0 0 2px, rgb(41, 39, 35) 0 0 0 4px` |

Na captura mobile, o swatch Carvão ficou mais nítido sobre a superfície clara e Base clara ganhou contorno identificável no tema escuro. A dupla borda branca/escura também preserva o contraste interno do Carvão no tema escuro; o anel exterior escuro se mistura à superfície escura, sem remover o anel branco. O estado ativo foi confirmado pelo DOM em todos os casos, e não inferido apenas pelo CSS.

### Capturas por viewport, tema e acabamento

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

O [recibo JSON compacto](g2-selected-finish-ring-2026-11-12/result.json) registra CSSOM, tema, estado acessível, SHA-256 de cada screenshot e erros HTTP por caso.

## Limites e próximo passo

Houve um HTTP 404 da bundle privada `/core/private-navigation.bundle.js` em cada contexto, ausente no checkout local; não houve erro de página e o estado Buyer V5 foi validado. As capturas não cobrem foco/teclado, hover, zoom, Safari/iPad, configuração hospedada nem o restante de #208/#216. A rota hospedada `/config/` continua sem configuração publicada válida. O Admin de #271 ainda precisa de revisão autenticada no Preview. G2 permanece em andamento; nenhuma mudança de código foi integrada à Product `main`.
