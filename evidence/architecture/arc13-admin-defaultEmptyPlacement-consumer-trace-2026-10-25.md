# ARC-13 — rastreio de `defaultEmptyPlacement`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

Quando um item é movido para uma etapa sem grupo/seção de destino, o handler cria uma colocação inicial para um novo grupo e seção. `defaultEmptyPlacement` calcula o comportamento e o componente a partir do item e dos defaults da hierarquia, gera ids técnicos e escolhe `stage.label || "Grupo"` como título do grupo; o título da seção vem do label do item.

A ocorrência indexada é somente o fallback estático “Grupo”, não um nome de etapa, grupo persistido ou valor de catálogo. Ele só aparece quando `stage.label` é falso/vazio. Os ids gerados e o comportamento de apresentação não são texto localizável.

## Limites

Rastreio estático do handler e do helper; não houve runtime com etapa sem rótulo nem confirmação do contrato de labels vazios no schema. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
