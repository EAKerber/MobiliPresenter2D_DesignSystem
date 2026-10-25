# ARC-13 — rastreio do bucket Admin renderPager — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O helper compartilhado `renderPager` tem três ocorrências sem chave. Os callbacks nos consumidores foram verificados apenas para confirmar navegação/re-render; conteúdo das listas e ordenação ficam fora deste bucket. Nenhuma chave foi proposta ou migrada.

## As três ocorrências

| Linha(s) | Texto | Sink / estado | Owner e contrato |
|---|---|---|---|
| 898 | ← Anterior | Texto do botão anterior, desabilitado quando `index <= 0). Clique chama `onPage(index - 1)`. | Ação de paginação curta; a seta aponta para a página anterior. |
| 900 | `${index + 1} / ${pages} | Status ao vivo com número de página 1-based e total. O estado interno `index` é 0-based; `pages` é calculado pelo consumer. | Template de status com dois parâmetros numéricos; anunciando em `aria-live="polite"`. Preservar a relação índice visível +1 e total. |
| 901 | Próxima → | Texto do botão seguinte, desabilitado quando `index >= pages - 1). Clique chama `onPage(index + 1)`. | Ação de paginação curta; a seta aponta para a página seguinte. |

## Consumidores e limites

O helper é usado por abas de disponibilidade de materiais/acabamentos e pelas listas de materiais/targets. O callback fornece a atualização específica; o pager não conhece o conteúdo do catálogo. O botão anterior/final desabilitado mantém a posição dentro dos limites do consumer.

A string do status é um padrão acessível e dinâmico; não deve virar um literal com números congelados. O contador também é o feedback de mudança de página para leitor de tela, devido ao live region.

## Resultado e próximo passo

Foram rastreadas três ocorrências: dois rótulos de navegação e um template numérico anunciado. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin de três ocorrências: `showUser`; seguir autenticação, autorização, dados do Admin e tratamento de falha até o estado visual apresentado.
