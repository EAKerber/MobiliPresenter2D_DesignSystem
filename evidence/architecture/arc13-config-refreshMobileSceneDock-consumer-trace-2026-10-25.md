# ARC-13 — rastreio de `refreshMobileSceneDock`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; rota `/config/`.

## Consumer e transição

A função só atua quando o modo PiP está disponível e configurado como `auto-after-anchor`. Ela mede se o fim da âncora do Viewer passou do topo, combina esse estado com `mobileScenePinEnabled` e atualiza `mobileSceneIsMini`. Sem mudança de estado, retorna sem sincronizar UI nem anunciar. Na transição para mini-cena, sincroniza o dock e escreve “Mini-cena disponível abaixo das etapas. Selecione um módulo diretamente na cena.” no live region `#configurationAnnouncement[aria-live="polite"]`.

A função é chamada em eventos de scroll e no resize em modo automático; também é chamada pelo launcher no caminho automático. O `IntersectionObserver` da sentinela repete a mesma mensagem e atualiza o mesmo estado. Como cada caminho compara e altera `mobileSceneIsMini` antes do anúncio, uma transição idêntica não deveria anunciar duas vezes; oscilações entre as duas medições durante movimento real não foram testadas.

## Relação com o bucket pai

A mensagem já aparece no rastreio de anúncios de `startConfigurator` e também no callback do `IntersectionObserver`. O texto é idêntico, mas os sinks pertencem a caminhos diferentes de detecção. O contrato aparente é a entrada do dock automático; compartilhar uma futura chave exige confirmar que a regra comum de transição e a eventual oscilação não alteram o contrato de anúncio.

## Limites

Rastreio estático de eventos, estado e região viva; sem ensaio runtime/AT. A mensagem é anunciada apenas na entrada em mini-cena, não no retorno ao estado normal. Nenhuma chave foi proposta; produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
