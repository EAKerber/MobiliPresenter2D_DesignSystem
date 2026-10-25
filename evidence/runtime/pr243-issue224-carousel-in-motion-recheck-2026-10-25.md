# Issue #224 — rechecagem do carrossel durante scroll — 25/10/2026

## Escopo e identidade

Rechecagem somente no Deploy Preview da PR de produto [#243](https://github.com/EAKerber/MobiliPresenter2D/pull/243), branch/head fix/issue224-carousel-preserve-page-20261024@8f2c3e5f5c0e2c3d17e01c1abc899675cd058ceb. Sem alteração do produto durante a leitura e sem ação em Production.

Preview: https://deploy-preview-243--mobilipresenter2d.netlify.app/.

## Método reproduzível

Chromium em contexto isolado, 320×844 e 390×844 CSS px, temas claro/escuro. Para cada combinação: voltei à página 1, aguardei a estabilização, iniciei o scroll para página 2, esperei 100 ms e li o scrollLeft antes de selecionar Lavanderia. Essa leitura confirmou movimento real: start≈2–3 px; aos 100 ms, scrollLeft≈159–160 px; máximo 307 px (320) ou 380 px (390). Selecionei Lavanderia enquanto scrollLeft estava estritamente entre início e máximo; aguardei 700 ms para estabilizar.

## Resultado nas quatro combinações

| Largura | Tema | Scroll em movimento ao selecionar | Estado imediato | Estado final | Cartão visível | Overflow do documento |
|---:|---|---|---|---|---|---|
| 320 px | claro | 159,3 / 307 px | Lavanderia selecionada, página 2 | página 2, scrollLeft 307,3 px | sim, dentro da janela | não |
| 390 px | claro | 159,3 / 380 px | Lavanderia selecionada, página 2 | página 2, scrollLeft 380 px | sim, dentro da janela | não |
| 320 px | escuro | 160 / 307 px | Lavanderia selecionada, página 2 | página 2, scrollLeft 307,3 px | sim, dentro da janela | não |
| 390 px | escuro | 158,7 / 380 px | Lavanderia selecionada, página 2 | página 2, scrollLeft 380 px | sim, dentro da janela | não |

A leitura dos limites do cartão mostrou sua caixa totalmente dentro da janela de ambientes, tolerando menos de 1 CSS px para arredondamento fracionário. Em todos os casos, seleção e indicador de página permaneceram sincronizados imediatamente após o clique e após a estabilização.

## Limites e estado

Esta evidência confirma a correção no preview para as quatro combinações testadas; não substitui o readback em Production depois de integração. Issue #224 permanece aberta e PR #243 continua DRAFT, sem review humana, merge ou deploy de Production.
