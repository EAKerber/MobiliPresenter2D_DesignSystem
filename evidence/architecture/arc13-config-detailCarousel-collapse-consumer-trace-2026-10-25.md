# ARC-13 — rastreio do click em `collapse` no carrossel

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Escopo: `createDetailCarousel`, rota `/config/`.

## Estados e consumers

- Expandido: nome acessível `Recolher visualizações`, texto visível `Recolher`, `aria-expanded=true`.
- Recolhido: nome acessível `Expandir visualizações`, texto visível `Mostrar`, `aria-expanded=false`.

O click alterna estado por entidade, classe de recolhimento e semântica acessível; também encerra a rotação automática. `Mostrar` aparece em outro componente (revelação de senha no Admin), mas o significado e owner são diferentes: não compartilhar só pela igualdade lexical.

## Limites

Rastreio manual do listener e do estado inicial, sem runtime/AT. Nenhuma chave foi proposta; código, índice e `decisions.json` permanecem inalterados.
