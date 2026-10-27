# ARC-13 — rastreio do bucket Admin renderStages — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderStages` tem 12 ocorrências. O rastreio cobre a área de itens disponíveis e o cartão/estado de cada etapa até a chamada de helpers para destinos compatíveis, ordenação e grupos. As strings internas de `renderGroup`, `compatibleDestinationOptions` e `makeOrderButtons` pertencem aos próprios buckets. Leitura estática em `main`; sem alteração do produto, índice, catálogo ou `decisions.json`, e sem proposta de chaves.

## Os 12 textos e seus consumers

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 624 | Itens do catálogo sem seção | `aria-label` da seção que reúne itens ainda não atribuídos. | Nome acessível do agrupamento; sua relação com itens e seções é estrutural, não nome de conteúdo do catálogo. |
| 626 | Itens disponíveis | Heading visível da mesma área. | Título de interface; confirmar se “disponíveis” significa todos os compatíveis ainda sem seção, conforme o filtro por etapa. |
| 629 | Itens pertencem a seções explícitas. Escolha uma seção compatível ou crie a estrutura inicial de uma etapa vazia. | Texto de orientação sob o heading. | Explica uma regra da hierarquia Admin: cada item deve estar numa seção explícita e destinos são filtrados por compatibilidade. Revisão do owner do fluxo antes de qualquer chave ou edição. |
| 649 | Adicionar | Botão por item não atribuído; recebe id dinâmico `data-place-hierarchy-item` e fica desabilitado sem destino compatível. | Ação de interface; o item e os destinos compatíveis são dados. Não remover a associação ao item do botão. |
| 658 | Todos os itens compatíveis já pertencem a uma seção. | Mensagem vazia quando `availableById` não contém itens. | Estado vazio condicional ao cálculo de compatibilidade/atribuição; não é mensagem de lista genericamente vazia. |
| 677 | Nome da etapa | Label do input de `stage.label`; o input aceita até 40 caracteres e altera dado editável. | Label fixa Admin; nome atual é conteúdo de etapa, não copy fixa. |
| 683 | Nome da etapa ${stage.label} | `aria-label` do mesmo input, com nome de etapa atual interpolado. | Template acessível; preservar nome de etapa como parâmetro/dado. |
| 699 | Remover etapa | Botão por cartão, vinculado ao id da etapa; remoção fica bloqueada para `modules` e `summary`. | Ação da interface sujeita a regra de domínio; manter guardas para etapas estruturais protegidas. |
| 711 | Ativar etapa ${stage.label} | `aria-label` do checkbox de ativação. | Template acessível com nome dinâmico como parâmetro. O checkbox é desabilitado para etapas protegidas e para etapas sem itens. |
| 712 | Ativa; Inativa | Estado visível ao lado do checkbox, derivado de `stage.enabled`. | Dois labels de estado da interface; não representam configuração de nome/tipo. Estado é dado booleano. |
| 723 | Etapa vazia. Adicione um item disponível para criar o primeiro grupo e seção. | Mensagem quando o cartão de uma etapa não tem grupos. | Orientação para o estado vazio de uma etapa; pressupõe que adicionar item crie a hierarquia inicial. Confirmar wording com owner do editor de etapas. |

## Fronteiras observadas

A área de itens disponíveis é calculada a partir do conjunto global de itens já associados e das opções permitidas para cada etapa. Os títulos dos itens, ids e rótulos dos destinos compatíveis vêm dos dados e de helpers externos ao bucket. “Adicionar” depende de destino selecionado; quando não existem destinos compatíveis, o botão não pode executar a ação.

Cada cartão recebe nome, estado e ordem de dados da etapa. O input modifica `stage.label`; os labels ARIA o reutilizam como parâmetro. Ativação e remoção respeitam os invariantes das etapas `modules` e `summary`; além disso, etapa sem itens não pode ser ativada. Grupos e seções são renderizados pelo helper `renderGroup`, fora destas 12 ocorrências.

## Resultado e próximo passo

As 12 ocorrências cobrem um heading/agrupamento, uma explicação de regra, ações por item e etapa, um estado vazio e labels de estado/nome acessíveis. Os textos de domínio relacionados à hierarquia devem ser revisados pelo owner antes de propor chaves; ids, títulos de item/destino, ordem e nomes de etapa permanecem dados/parâmetros. Nenhuma chave foi proposta ou migrada.

Próximo bucket por volume ainda não rastreado no Admin: `renderObjectAssets` (10 ocorrências). Seguir a origem dos caminhos de assets e o nome/identificador do objeto, separando rótulos de interface dos dados de cena.
