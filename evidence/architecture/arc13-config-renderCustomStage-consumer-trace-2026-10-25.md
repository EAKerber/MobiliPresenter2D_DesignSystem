# ARC-13 — rastreio de `renderCustomStage`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumers e condições

- **Descrição da etapa customizada:** `Escolha os itens desta etapa.` aparece sob `stage.label`, que é dado dinâmico da configuração do fluxo.
- **Itens da etapa:** cada checkbox tem nome acessível e título visível obtidos por `customStageItemLabel(id)`, que resolve para título de módulo, acessório, serviço ou, se não houver correspondência, o próprio id. O nome do item é dado de catálogo/configuração.
- **Categoria visível:** `Módulo` é usado quando o id existe em `catalog.modules`; nos demais casos o texto é `Item opcional`. A classe resulta da resolução do catálogo, não de texto fornecido pelo item.
- **Estado controlado por evento:** quando um evento ativo define o estado, o checkbox desabilita e recebe o tooltip `Controlado por um evento da configuração.`; sem override, o título é limpo. O mesmo sentido já aparece em outros controles; só será compartilhável como chave se contrato de owner e consumer for confirmado.
- **Etapa vazia:** `Inclua itens na administração para preencher esta etapa.` só é renderizado quando `stage.items` está vazio.

A mudança no checkbox escolhe o caminho pela forma do item no estado: ids presentes em `visibilityByEntity` passam por `setEntityVisibility`; os demais atualizam seleção global de serviço e sincronizam a cena. A etapa pode conter itens de classes diferentes, portanto o nome dinâmico e o consumer não devem assumir que tudo é serviço ou módulo.

## Limites e ponto de revisão

Rastreio de fonte e listener, sem runtime/AST. A categoria `Item opcional` é determinada apenas por “não é módulo”; isso não comprova que o item seja opcional em todos os fluxos. Confirmar o sentido de domínio com o owner do fluxo antes de canonizar essa label. Nenhuma chave foi proposta; código, índice, catálogo e `decisions.json` seguem inalterados.
