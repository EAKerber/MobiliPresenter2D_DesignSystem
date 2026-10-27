# ARC-13 — rastreio de `createModuleSelectionControl`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer em `/config/`, dentro do cabeçalho dos detalhes de um módulo.

## Consumers e estados

- **Nome acessível do checkbox:** combina a ação `Selecionar`/ `Desselecionar` com `entity.label`, vindo da entidade de cena. O estado inicial é `isVisible`; o nome muda para descrever a ação oposta ao estado atual.
- **Texto visível:** mostra `Selecionado` quando ativo e `Selecionar` quando inativo. É um sinal curto de estado/ação; não inclui o nome da entidade, que fica no nome acessível.
- **Atualização:** o listener de mudança registra pulso visual ao ativar, chama `setEntityVisibility(entityId, checked)` e atualiza a contagem visível. A seleção não é apenas decorativa.

O controle é uma checkbox dentro de um `label` e só é criado para o módulo selecionado no painel de detalhes. `entity.label` é dado dinâmico da cena, e não deve ser confundido com `product.title` do cartão de módulos.

## Limites

Rastreio manual de fonte e do listener correspondente, sem teste runtime/AST. As ações e estados curtos são strings de interface candidatas; o label da entidade é parâmetro de dado. Nenhuma chave foi proposta; código, índice, catálogo e `decisions.json` não foram alterados.
