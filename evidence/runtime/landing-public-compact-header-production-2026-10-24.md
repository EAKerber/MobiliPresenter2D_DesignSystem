# Landing — cabeçalho compacto em Production (24/10/2026)

**Alvo:** Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`, rota `/`. Viewports temporários; temas foram restaurados e a aba fechada ao final.

| Viewport | Tema | Largura de conteúdo | Resultado |
|---|---|---:|---|
| 390 × 844 | Escuro e claro | 375 px úteis | Sem overflow horizontal; header ocupou a largura útil. |
| 320 × 700 | Claro | 320 px | Conteúdo permaneceu dentro do viewport. A diferença de 15 px entre `innerWidth` e `clientWidth` corresponde à área da barra vertical no browser desta sessão. |
| 310 × 700 | Claro | 320 px | `html` e `body` computaram `min-width: 320px`; o documento ultrapassou o viewport em 10 px. |
| 290 × 700 | Claro e escuro | 320 px | O documento ultrapassou o viewport em 30 px. O botão do menu ocupa x=264–306; na largura útil de 275 px, somente 11 px dos 42 px ficam dentro da área visível. |

A captura em 290 px no tema claro mostrou barra horizontal e conteúdo cortado: parte do botão de menu, texto do hero e CTA não cabiam no viewport. A medição do DOM confirmou `min-width: 320px` em `html` e `body`, além de header com 320 px. O problema ocorre nos dois temas observados em 290 px. Esta reprodução se relaciona à família já registrada em [issue #218 / NAV-005](https://github.com/EAKerber/MobiliPresenter2D/issues/218); amplia a evidência ao estado da Landing atual e também identifica overflow horizontal em 310 px. Não altera nem substitui a issue.

Não abri o menu nem naveguei pelo conteúdo. Captura não persistida; a leitura foi feita sem login e sem enviar dados. Um viewport por largura; 320 px foi medido somente no tema claro. Nenhum CSS/token ou deploy do produto foi alterado. A simulação experimental NAV-005 permanece separada da implementação atual e não foi aplicada.
