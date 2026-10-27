# ARC-13 — rastreio de `selectEntity`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer em `/config/`, ficha de módulo.

## Ação e feedback

A seleção só prossegue se houver produto no catálogo. Guarda a origem de foco, seleciona a entidade, retorna à etapa Módulos e sincroniza a cena. O live region anuncia `Ficha de {referenceLabel}, {title}, aberta.`; referência e título são parâmetros do catálogo.

Se a seleção veio da cena, a ficha rola para a área visível, salvo quando o PiP está fixado. No PiP fixado, preserva a cena em miniatura. Em qualquer origem, move foco para o botão de fechar. A mesma função é usada por seleção na cena/lista e navegação de ficha; o parâmetro de origem muda o tratamento de scroll/foco.

## Limites

Rastreio manual de caller e helper, sem runtime/AT. O anúncio com dados do catálogo é distinto do hint visual `Ficha selecionada: {title}` do renderer. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` permanecem inalterados.
