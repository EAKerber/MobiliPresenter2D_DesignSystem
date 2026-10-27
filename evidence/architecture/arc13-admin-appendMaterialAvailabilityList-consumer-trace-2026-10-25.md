# ARC-13 — rastreio de `appendMaterialAvailabilityList`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O helper renderiza uma lista paginada de materiais para um destino. O heading combina o label dinâmico recebido do grupo/destino, a quantidade em `selectedIds.length` e o texto “disponível(is)”. Os itens usam labels e amostras do catálogo; ids, textura, página e seleção permanecem dados.

O candidato é texto de interface, mas a concordância atual está embutida em “disponível(is)”. A decisão do projeto adia pluralização para a etapa de localização: qualquer proposta posterior deve manter a contagem como parâmetro e escolher um contrato de pluralização, não congelar o sufixo “(is)” como solução final.

## Limites

Rastreio estático do helper e do fluxo paginado; sem readback publicado nem avaliação editorial/AT no Admin. Ownership da label do grupo vem do chamador e não foi consolidado aqui. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
