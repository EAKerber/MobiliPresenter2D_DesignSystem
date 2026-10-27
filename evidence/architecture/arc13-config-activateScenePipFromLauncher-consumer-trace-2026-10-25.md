# ARC-13 — rastreio de `activateScenePipFromLauncher`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; rota `/config/`.

## Consumer e modos

O launcher retorna se o PiP não estiver disponível; caso contrário, ativa `mobileScenePinEnabled`. No modo manual, abre o PiP, sincroniza a UI, agenda foco de retorno ao botão e anuncia “Mini-cena fixada para contexto durante a configuração.” No modo automático, delega a `refreshMobileSceneDock(profile)` e sincroniza a UI; a mensagem específica de mini-cena só é anunciada se a âncora já tiver sido ultrapassada e a transição para o estado mini ocorrer.

O literal indexado pertence, portanto, ao caminho manual do launcher. A formulação é uma confirmação de ação/estado acessível, distinta da orientação anunciada ao entrar no dock automático. Não deve ser agrupada com a mensagem de `refreshMobileSceneDock` apenas porque ambas mencionam a mini-cena.

## Limites

Rastreio estático do branch manual/automático, atualização de estado, foco e anúncio. Não houve runtime/AT nem confirmação de que o elemento que aciona a função é o único launcher em todos os perfis. Nenhuma chave foi proposta; produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
