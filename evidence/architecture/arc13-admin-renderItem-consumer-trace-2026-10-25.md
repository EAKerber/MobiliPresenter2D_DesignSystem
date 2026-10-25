# ARC-13 — rastreio do bucket Admin renderItem — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8); mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderItem` tem três ocorrências. O rastreio acompanhou destinos compatíveis, condição de criação de seção e handler de retirada até a camada de hierarquia. Os labels dinâmicos de item/destino e as funções dos controles aninhados pertencem a outros buckets. Nenhuma chave foi proposta; sem alteração de produto, índice ou `decisions.json).

## As três ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 432 | Mover para | Label que envolve o seletor de destino compatível do item. O valor atual é `stage.id|group.id|section.id`; os nomes de destino são montados dinamicamente. | Label do editor hierárquico. O destino não é texto fixo. O controle não inclui o nome do item no próprio label; isso fica como ponto para avaliação de nome acessível no runtime, sem afirmar falha apenas com leitura estática. |
| 452 | Nova seção | Botão exibido somente quando a seção atual tem mais de um item; dispara o fluxo de dividir o item para uma nova seção, com prompt em outro bucket. | Ação estrutural condicionada. Não renomeia o item nem cria nova entrada de catálogo. |
| 462 | Retirar | Botão de cada item ligado a `data-remove-hierarchy-item=itemId). | Remove o item da hierarquia corrente. O handler chama `hierarchyEditor.removeItem`, que retira o id da seção e apaga grupo/seção vazios; não remove o registro do catálogo. Manter essa distinção no texto e no consumer. |

## Destinos e fronteiras

`compatibleDestinationOptions(itemId)` oferece somente etapas compatíveis, preservando o comportamento padrão do item. Se uma etapa compatível não tem grupos, a opção apresenta criação da estrutura inicial; caso contrário, oferece seções cujo behavior corresponde. Ids/caminhos e labels de destino são dados da hierarquia.

O cartão também chama `appendInitialStateControl` e `appendHierarchyChoiceOptions`; os textos desses controls são rastreados nos buckets próprios e não foram contados nestas três ocorrências. A ação “Nova seção” abre um prompt fora desta função.

## Resultado e próximo passo

As três strings têm sinks diferentes: movimentação, divisão estrutural e retirada apenas da hierarquia. O nome genérico “Mover para” pode merecer uma checagem de anúncio por leitor de tela, pois vários itens usam o mesmo label; fica como observação para evidência runtime, não como falha confirmada. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin: `renderSection` (3 ocorrências); rastrear título de seção, movimento entre grupos e chamada de divisão estrutural.
