# Issue #224 — reprodução transitória e validação da PR #243

Data: 2026-10-24  
Repositório do produto: `EAKerber/MobiliPresenter2D`  
Base observada: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
Correção em preview: PR [#243](https://github.com/EAKerber/MobiliPresenter2D/pull/243), head `8f2c3e5f5c0e2c3d17e01c1abc899675cd058ceb`  
Preview principal: [deploy-preview-243](https://deploy-preview-243--mobilipresenter2d.netlify.app/)

## Reprodução da falha na main

Em viewport mobile 390 × 844, iniciar o scroll suave para o grupo 2 e selecionar Lavanderia quando o cartão está pelo menos 75% visível reproduziu a falha nos temas claro e escuro. Lavanderia permanecia selecionada, mas a paginação mudava ao grupo 1 e `scrollLeft` retornava a zero.

A falha ocorria durante o scroll, antes da posição final. As verificações anteriores aguardavam o scroll estabilizar e, por isso, não exercitavam esta janela transitória.

## Correção em preview

A função `revealCard()` agora decide a direção pelo limite que ultrapassa a janela: borda direita leva ao grupo 2; borda esquerda leva ao grupo 1. A alteração está limitada a uma condição em `app/landing/landing.js`.

## Repetição do cenário no preview

O mesmo cenário foi repetido com acionamento de clique via DOM durante o scroll:

| Viewport | Tema | Momento do clique | Visibilidade de Lavanderia | `scrollLeft` no clique | Resultado imediato |
|---|---|---:|---:|---:|---|
| 320 × 844 | claro | 231 ms | 83% | 287/307 | selecionada; grupo 2 |
| 320 × 844 | escuro | 189 ms | 83% | 287/307 | selecionada; grupo 2 |
| 390 × 844 | claro | 216 ms | 76% | 344/380 | selecionada; grupo 2 |
| 390 × 844 | escuro | 199 ms | 82% | 353/380 | selecionada; grupo 2 |

Nos quatro cenários, depois de estabilizar, a paginação continuou no grupo 2, Lavanderia permaneceu selecionada e o carrossel chegou ao máximo (`307/307` px em 320; `380/380` px em 390). O documento não teve overflow horizontal.

## Gates e limites da evidência

O deploy preview principal está READY. Todos os workflows de Actions associados ao head da PR passaram após a repetição do job de roteamento. A primeira tentativa recebeu 404 de `/api/public-modules` durante a convergência do deploy; a repetição confirmou HTTP 200, projeção pública, respostas negativas esperadas e smoke desktop/mobile.

A evidência cobre dois viewports e dois temas no preview atual. Não valida outros tamanhos, Production, integração ou uma sequência física de teclado. A PR #243 permanece DRAFT aguardando revisão; não houve merge nem deploy de produção.
