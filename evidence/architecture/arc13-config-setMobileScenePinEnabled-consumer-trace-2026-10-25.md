# ARC-13 — rastreio de `setMobileScenePinEnabled`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer em `/config/`.

## Ação e feedback

O clique no controle `mobileScenePin` inverte `mobileScenePinEnabled` e chama este helper. Fixar mantém a mini-cena associada ao fluxo; liberar também limpa `mobileSceneIsMini`. Em ambos os ramos, a UI é sincronizada antes de anunciar no live region polite:

- ação de fixar: `Cena fixada para contexto durante a configuração.`;
- ação de liberar: `Cena liberada para o fluxo normal.`.

O launcher de re-fixação usa outro fluxo de ativação e mensagens do PiP, portanto não é automaticamente o mesmo consumer da alternância deste controle.

## Limites

Rastreio manual do caller e helper, sem runtime/AT. Nenhuma chave foi proposta; código, índice e `decisions.json` permanecem inalterados.
