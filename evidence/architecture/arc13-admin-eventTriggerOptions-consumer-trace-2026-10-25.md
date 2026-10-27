# ARC-13 — rastreio de `eventTriggerOptions`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

As opções são passadas ao seletor de gatilho de `renderEvents`. O helper combina entidades editáveis, serviços do catálogo com seus títulos e uma opção estática `stone-skirting` com label “Rodapé de pedra”. O id é usado pelo motor de eventos e não é texto.

A ocorrência indexada é a label do gatilho para rodapé de pedra. O código acrescenta essa opção depois de mapear serviços; não confirmei se existe serviço de catálogo com o mesmo id, então duplicidade/ownership da label permanecem ponto de domínio a validar. As demais labels vêm dos dados de cena/catálogo.

## Limites

Rastreio estático de construção e consumer do seletor; sem leitura do catálogo publicado nem verificação do motor para o id `stone-skirting`. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
