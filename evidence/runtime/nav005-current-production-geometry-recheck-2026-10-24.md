# NAV-005 — rechecagem da geometria atual do header privado

Data local: 2026-10-24  
Produção observada: [`/admin.html`](https://casaemmodulos.casa/admin.html)  
Produto base correlacionado: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
CSS inspecionado: `app/ui-theme.css` no mesmo commit  
Contexto do navegador: isolado, sem sessão administrativa  
Método: viewport móvel emulado e leitura somente de DOM/CSSOM. Os temas claro/escuro foram emulados; nenhuma preferência ou dado foi salvo.

## Resultados

Em todos os pontos amostrados, o layout e a geometria foram iguais nos temas claro e escuro:

| Viewport | Header | Logo | Controle de tema | Menu | Layout |
|---:|---:|---:|---:|---:|---|
| 288 px | 104,6 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | duas linhas |
| 291 px | 104,6 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | duas linhas |
| 320 px | 104,6 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | duas linhas |
| 321 px | 104,6 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | duas linhas |
| 336 px | 104,6 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | duas linhas |
| 337 px | 62 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | uma linha |
| 340 px | 62 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | uma linha |
| 350 px | 62 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | uma linha |
| 360 px | 62 px | 105 px | 65,7 × 40 px, texto “Auto” | 40 × 40 px | uma linha |

O primeiro ponto amostrado de uma linha foi 337 px e o último ponto amostrado de duas linhas foi 336 px. Não houve overflow horizontal em nenhuma amostra. A passagem anterior de 18/10 registrou 340 px em duas linhas; a rechecagem atual encontrou uma linha em 340 px, logo o limite observado mudou entre essas medições. Não inferir o breakpoint exato apenas desses pontos.

## Comparação com a direção aprovada

A regra comportamental registrada em `decisions.json` pede uma composição em uma linha até o piso de 291 px, logo reduzida no máximo 30%, texto do tema mantido enquanto couber e controle somente ícone em 320 px ou abaixo; sob 291 px, duas linhas. A implementação atual não realiza esses ajustes: a logo fica em 105 px, o controle continua com 65,7 px e a composição quebra em duas linhas até 336 px. A maior parte dos alvos medidos também fica em 40 px, abaixo dos 44 × 44 px recomendados pela especificação.

Este achado confirma uma diferença entre a regra aprovada e o runtime, mas não autoriza mudança de produto. `decisions.json` mantém `NAV-005.implementationAuthorized=false`. Os valores recomendados continuam sujeitos a validação na implementação; esta passagem mediu apenas a geometria atual.

## Limites

A rota abriu a tela pública de login, sem sessão administrativa. O estado interno do Configurador, páginas autenticadas, identificadores excepcionais longos, alinhamento/ordem de todos os controles e validação visual pós-implementação não foram auditados. Os nove pontos de largura cobrem apenas a transição observada entre 336 e 337 px.
