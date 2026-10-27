# ARC-13 — rastreio do bucket Admin renderGroup — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8); mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderGroup` tem três ocorrências. O rastreio incluiu o seletor de largura e o handler de união do grupo vizinho; labels do nome, componente e ordenação são consumers próprios. Nenhuma chave foi proposta; sem alteração de produto, índice ou `decisions.json).

## As três ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 578 | 1 coluna; 2 colunas | Opções do seletor numérico `group.columnSpan`, limitado a `hierarchyCore.COLUMN_SPANS`. | Labels de enum de layout; valores 1 e 2 são dados/contrato, não parte de copy. |
| 603 | Remover grupo e unir conteúdo | Botão somente se a etapa tiver mais de um grupo. O destino é escolhido pelo índice: grupo inicial une no seguinte; demais unem no anterior. | Ação estrutural: suas seções são transferidas para o grupo vizinho e o contêiner grupo de origem é removido. Não exclui as seções ou itens. A ordem das seções preserva a ordem relativa no merge. |

## Fronteiras observadas

O handler usa `hierarchyEditor.mergeGroupIntoNext/Previous`: no primeiro caso, coloca as seções do grupo de origem no início do grupo seguinte; no segundo, ao final do grupo anterior. A seleção de `columnSpan` altera a extensão do grupo, com valores discretos; títulos e ids de grupos permanecem dados editáveis.

A remoção/união só está disponível quando existe grupo adjacente, evitando a tentativa de remover o único grupo da etapa. O nome “unir conteúdo” refere-se às seções do grupo, não a concatenar texto.

## Resultado e próximo passo

Três ocorrências cobrem as opções de largura e uma ação de união condicional. A união preserva seção/item; elimina somente o grupo fonte. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin por ocorrência: `renderPager` (3 candidatas); rastrear rótulos de navegação e a contagem dinâmica da página.
