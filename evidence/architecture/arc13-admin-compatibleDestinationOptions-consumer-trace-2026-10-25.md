# ARC-13 — rastreio de `compatibleDestinationOptions`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O helper calcula destinos onde um item pode ser colocado: só inclui etapas que oferecem o item; em etapas não vazias, filtra seções pelo comportamento compatível. Para uma etapa vazia, cria uma opção cujo label é “{stage.label} · criar grupo/seção inicial”. O valor técnico dessa opção contém somente o id da etapa; a ação seguinte cria os ids de grupo/seção e mantém o comportamento padrão do item.

O trecho candidato é uma instrução contextual de destino, com label configurado da etapa como parâmetro. Não é nome de catálogo nem conteúdo persistido. Os destinos já estruturados usam labels de etapa, grupo e seção como dados do Admin.

## Limites

Rastreio estático de filtro e composição do label; sem runtime com destinos vazios nem leitura assistiva das opções do seletor. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
