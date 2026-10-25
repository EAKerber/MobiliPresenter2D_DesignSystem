# ARC-13 — rastreio do bucket Admin syncPasswordReveal — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8); mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function syncPasswordReveal` tem quatro ocorrências. Foram inspecionados os dois inputs que chamam a função em `app/admin.html), como fronteira de estado inicial. Esta análise não muda auth, senha, acessibilidade nem markup; nenhuma chave foi proposta, e `decisions.json` permanece intacto.

## As quatro ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 102 | Mostrar senha; Ocultar senha | O valor escolhido por `revealed` é escrito no `aria-label` e no atributo `title` do mesmo botão. | Label completo acessível/tooltip. A cópia comunica claramente o estado/operação sobre senha, não contém o valor da senha. |
| 106 | Mostrar; Ocultar | Texto visual do botão, sincronizado com o mesmo booleano `revealed`. | Label curta de UI; seu comprimento/contrato visual difere do texto completo usado no leitor de tela. Não substituir pela forma curta em `aria-label`/tooltip. |

## Estados e markup inicial

`admin.html` inclui dois controles:
- `passwordInput`, autocomplete `current-password`, inicialmente type `password`;
- `newPasswordInput`, autocomplete `new-password), inicialmente type `password`.

Cada botão já contém no HTML inicial `aria-label="Mostrar senha"`, `title="Mostrar senha"), `aria-pressed="false") e texto visível “Mostrar”. A rotina JavaScript reconcilia label/tooltip e texto com `input.type === "text"`; clique alterna entre `password` e `text`, depois recalcula `aria-pressed`.

Essas duas cópias de estado inicial estão em HTML fora do bucket JS. Qualquer futura migração apenas dos quatro literais JS deixaria o primeiro render em HTML com strings fixas; a cobertura ARC-13 de markup precisa verificar esses pontos separadamente. O comportamento não revela valores por texto ou log; o input alterna sua apresentação após ação do usuário.

## Resultado e próximo passo

Os dois pares têm contratos diferentes (label completo versus botão compacto), e são compartilhados entre os campos de senha atual e senha nova. O estado inicial em HTML é uma fronteira necessária para eventual migração completa, mas não foi contado como ocorrência JS. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin por volume: `function renderItem` (3 ocorrências); rastrear heading, controles de estado inicial/opções e labels de catálogo até os sinks hierárquicos.
