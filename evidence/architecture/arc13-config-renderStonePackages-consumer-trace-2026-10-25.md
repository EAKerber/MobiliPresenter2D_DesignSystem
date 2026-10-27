# ARC-13 — rastreio de `renderStonePackages`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumers

- **Nome acessível do pacote:** `Selecionar pedra ` + `stone.label`; o prefixo é copy da interface e o nome vem do catálogo. O mesmo nome aparece visualmente no cartão e `aria-pressed` comunica a seleção.
- **Descrição/preço:** `stone.description` permanece dado editorial. O renderer acrescenta preço positivo formatado ou a frase `sem adicional.` quando não há valor. A pontuação, moeda e valor são parte do estado do preço; não converter em texto estático.
- **Ajuda do rodapé:** o toggle de rodapé de pedra fica marcado conforme estado global efetivo. Se regra ativa controla `stone-skirting`, o toggle desabilita e recebe `Controlado por um evento da configuração.`; sem override, o `title` fica vazio. É o mesmo sentido do tooltip em outros controles regidos por evento, mas compartilhar uma chave exige confirmar o contrato comum de consumer.

## Limites

O renderer seleciona o pacote global, preserva labels/descrições dinâmicos do catálogo e não comprova a política editorial desses dados. Rastreio manual de fonte, sem runtime/AST; nenhuma chave foi proposta e nenhum produto, catálogo, índice ou `decisions.json` foi alterado.
