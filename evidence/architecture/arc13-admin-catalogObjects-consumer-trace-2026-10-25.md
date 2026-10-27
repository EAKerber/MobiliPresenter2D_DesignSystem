# ARC-13 — rastreio de `catalogObjects`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O helper monta a lista usada pelo seletor de objetos do Admin, combinando ids estáveis com rótulos. Módulos usam referência e título do catálogo; acessórios e serviços usam seus títulos; opções de puxador e pedra recebem prefixos de tipo (“Puxador · {label}” e “Pedra · {label}”). O seletor usa esses valores como `option.textContent`; o item atual também reaproveita o label em headings e no rótulo enviado a `renderObjectAssets`.

As duas strings encontradas pelo mapa são prefixos de interface para distinguir categorias; `item.label` é conteúdo dinâmico do catálogo e permanece parâmetro. Não fundir os prefixos: um seleciona puxador, o outro pacote de pedra. Rótulos de módulos/acessórios/serviços são valores de catálogo e não candidatos deste bucket.

## Limites

Rastreio estático de helper e consumers diretos; não houve leitura de configuração publicada nem teste de teclado/AT no Admin. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
