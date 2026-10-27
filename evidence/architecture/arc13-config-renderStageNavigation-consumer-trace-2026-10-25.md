# ARC-13 — rastreio de `renderStageNavigation`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; `app/styles.css` blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`. Rota `/config/`.

## Consumer

`applyConfiguratorSettings` normaliza o fluxo configurado e chama `renderStageNavigation()`. Para cada etapa habilitada, o renderer cria um botão com o número ordinal, `data-step`, `aria-controls` e nome acessível igual ao `stage.label` vindo do fluxo. O conteúdo visual principal também preserva o label completo.

A única string do mapa neste bucket, `Resumo`, está no valor compacto associado a `stageKind(stage) === "summary"`. Os labels compactos de etapas de sistema são escolhidos no mapa local (`Módulos`, `Acab.`, `Serv.`, `Resumo`); para etapa customizada, o valor compacto vem do próprio `stage.label`. Em `app/styles.css`, o container da navegação usa a forma compacta até 500 px: o label completo é visualmente ocultado e o pseudo-elemento exibe `data-compact-label`. O nome acessível do botão continua o label completo.

## Limites

O literal `Resumo` funciona como abreviação visual específica da etapa summary, não como o nome acessível completo nem como conteúdo comercial. A relação foi rastreada estaticamente entre normalização do fluxo, criação do botão e regra compacta; não houve runtime/AT com múltiplas configurações publicadas. Nenhuma chave foi proposta, e produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
