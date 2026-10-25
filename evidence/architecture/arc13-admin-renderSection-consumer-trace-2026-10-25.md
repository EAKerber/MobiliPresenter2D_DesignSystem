# ARC-13 — rastreio do bucket Admin renderSection — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8); mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderSection` tem três ocorrências. O rastreio incluiu as condições de apresentação e os handlers correspondentes para distinguir mover, dividir e unir. Labels de seção/grupo e ids continuam dados de hierarquia; prompts de criação pertencem a outros buckets. Nenhuma chave foi proposta ou migrada.

## As três ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 513 | Mover seção para grupo | Label do select de destino; só aparece quando a etapa possui mais de um grupo. As opções usam id/label dos grupos da mesma etapa. | Ação de movimentação estrutural. A seleção atual é válida e não remove a seção; o id do grupo é dado. |
| 538 | Mover para novo grupo | Botão apenas quando o grupo atual tem mais de uma seção. O handler pede nome do grupo em prompt, remove a seção do grupo atual e a coloca como única seção de um novo grupo. | Ação de divisão/transposição estrutural; não recria nem apaga o conteúdo da seção. O prompt “Nome do novo grupo” está fora deste bucket. |
| 545 | Remover seção e unir | Botão também condicionado a haver mais de uma seção. Se a seção é a primeira, seus itens são unidos no início da seção seguinte; caso contrário, vão para o final da seção anterior. A seção de origem é removida. | Rótulo descreve remoção do contêiner e preservação/movimentação dos itens. Não significa excluir os itens ou suas entradas de catálogo. O sentido de ordem é parte do comportamento do handler. |

## Fronteiras observadas

O select de grupo usa as opções da etapa atual; o handler move a seção identificada por `stageId|sourceGroupId|sectionId`. A divisão usa ids/labels de seção e um id único calculado a partir do nome fornecido. A fusão escolhe a seção adjacente via direção `next`/ `previous`, preserva os ids de item e então remove somente a seção fonte.

“Seção” e “grupo” são entidades da hierarquia editável; labels, nomes e ids estão nos dados do modelo. Esta função também delega renderização de itens e labels de ordenação a helpers separados, fora das três ocorrências.

## Resultado e próximo passo

As três labels nomeiam mudanças estruturais distintas. “Remover seção e unir” preserva os itens ao remover o contêiner; “Mover para novo grupo” conserva a seção. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin por ocorrência: `renderGroup` (3 candidatas); distinguir spans, seção e regra de última-seção nas ações do grupo.
