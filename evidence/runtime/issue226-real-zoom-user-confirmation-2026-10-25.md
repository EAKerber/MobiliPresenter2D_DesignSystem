# Issue #226 — zoom real em produção, confirmação manual — 2026-10-25

**Rota:** https://casaemmodulos.casa/how-it-works/  
**Escopo:** último gate de zoom real da apresentação dos acordeões.  
**Fonte de fix:** PR [#230](https://github.com/EAKerber/MobiliPresenter2D/pull/230), mergeada em 2026-10-21; a CSS atual em `main@5ccb2a8` mantém `align-items:start` nas grades `.foundation-list` e `.study-topics` a partir de 901 px.

## Evidência automatizada já registrada

A issue contém a revalidação [Actions #40222887693](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40222887693): 8/8 combinações funcionais Chromium/WebKit em 390/1366 px e temas claro/escuro; o artefato comparativo foi inspecionado e mostrou somente o cartão expandido crescendo, irmãos fechados sem alongamento e espaço vazio fora dos cartões. Resize com item aberto, fechamento, teclado e abertura independente também estavam cobertos.

## Confirmação manual de zoom real

Após solicitação para conferir a janela Chrome em 400% real, o usuário informou que realizou o teste e confirmou o comportamento independente: um `<details>` que está aberto permanece aberto até ser fechado; abrir outro não substitui automaticamente o anterior. O usuário declarou preferir esse comportamento, que corresponde ao HTML atual sem atributo `name` e sem handler que feche irmãos.

## Limite do readback

A automação não conseguiu inspecionar a janela Chrome com segurança. O alvo separado de DevTools continuou reportando viewport 501 × 69 px, DPR 1,5 e escala visual 1; esse valor **não** representa uma medição do zoom manual do usuário e não foi usado como resultado. Não há screenshot nem leitura automatizada de geometria/scrollWidth em 400%. O gate de zoom foi aceito com base na confirmação manual do usuário, somada aos gates automatizados existentes.

**Conclusão:** a issue #226 foi encerrada após o usuário confirmar o teste manual em zoom real. Não houve alteração de produto ou Production nesta confirmação.
