# ARC-13 — rastreio do bucket Admin renderMaterialGroups — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket exato `function renderMaterialGroups` tem 12 ocorrências. O caminho foi seguido até os helpers chamados pela função, incluindo a geração das opções por alvo e seus dados dinâmicos. Trata-se de leitura do código em `main`; nenhuma chave foi proposta e não houve alteração do produto, do índice, do catálogo ou de `decisions.json`.

## Os 12 textos e seus consumers

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 999 | `${title} · opções válidas | Heading do cartão; `title` vem de `materialTargetOptions()`: “Frentes”, “Pedra e rodapé” ou “Puxador · ${item.label}”. | O sufixo é interface Admin; título e label do puxador vêm da lista/catálogo e permanecem dados dinâmicos. Não embutir nomes de grupos ou puxadores numa chave. |
| 1005 | Disponível para clientes | Texto do toggle de disponibilidade, apenas para alvos `handle:<id>`. | Copy fixa da interface do Admin. O estado do checkbox e o id do puxador são dados. |
| 1006 | Definir depois não é um puxador e não recebe materiais. | Nota sob a disponibilidade de materiais de puxador. | Explica uma regra de domínio: o sentinel `none` não representa um produto. Confirmar wording com owner de catálogo/editorial antes de propor uma chave. |
| 1007 | Cores e materiais deste puxador | Label passado ao helper de disponibilidade; o heading final acrescenta a quantidade selecionada e a palavra variável `disponível(is)`. | Texto fixo do Admin com cardinalidade dinâmica gerada pelo helper; contrato de pluralização permanece adiado à etapa de localização. |
| 1008 | Definir depois; Puxador selecionado inicialmente | Opção sentinel `none` e label do seletor inicial, respectivamente. Outras opções são `priceEntryId` e `label` do item, com id como fallback. | A label do campo é interface Admin; “Definir depois” nomeia um estado de configuração exposto ao cliente/editor e sua ownership deve ser revisada no catálogo/editorial já aprovado pelo usuário. Não tratar opções dinâmicas como copy. |
| 1011 | Nome da opção | Label do campo que edita `group.label`. | Label da interface; o valor editável do grupo é dado de catálogo, não uma chave. |
| 1012 | Pedras e texturas disponíveis para bancada e rodapé | Label para `appendMaterialAvailabilityList`, somente no grupo `stone-all`. | Termo editorial/técnico que descreve dois alvos do domínio; revisar com owner antes de propor chave ou alterar texto. A lista de materiais e a quantidade são dinâmicas. |
| 1013 | Materiais válidos para frentes | Label do dropdown de checkbox no ramo não pedra/puxador. | Copy de interface que condiciona a lista de materiais ao grupo ativo; opções usam id, nome, cor e textura do modelo. |
| 1016 | Cor selecionada inicialmente | Label do select somente em `fronts-all`; opções resultam de acabamentos ativos, globais e disponíveis no grupo. | Label Admin; cor/label e lista de opções vêm dos dados de acabamento/material. |
| 1018 | Pedra selecionada inicialmente | Label do select no outro grupo; opções vêm dos ids do grupo e dos labels dos materiais. | Label Admin; opções e valor selecionado são dados. |
| 1019 | A disponibilidade do serviço de rodapé é controlada separadamente na etapa; pedra e rodapé compartilham o material escolhido. | Nota somente no ramo de pedra/rodapé. | Regra de produto/comercial, não mero texto genérico de interface. A semântica depende do fluxo de etapa e do compartilhamento de material; exigir owner do domínio antes de qualquer proposta de chave ou edição. |

## Fronteiras observadas

- `materialTargetOptions()` combina dois alvos de catálogo fixos com alvos de puxadores e labels vindos de `model.handleProducts`. O heading não deve absorver esses nomes numa chave.
- A disponibilidade de puxadores chama `appendMaterialAvailabilityList`; a seleção de frentes usa `makeMaterialCheckboxDropdown`. Os dois helpers exibem materiais do modelo, nomes dinâmicos e estado selecionado. O helper de lista também gera contagem com `disponível(is)`; a pluralização foi adiada pelo usuário para localização.
- `Definir depois` aparece como option sentinel no seletor inicial e como texto da nota de regra. Essa relação não torna os dois sinks intercambiáveis: uma é escolha/estado visível e a outra explica o que esse estado significa.
- Labels de campo, texto de catálogo e regras comerciais têm owners distintos. A heurística lexical não determina ownership; os cinco itens de catálogo/editorial seguem a decisão de manter no catálogo e pedir revisão do owner.

## Resultado e próximo passo

As 12 ocorrências têm sinks de interface Admin, domínio de catálogo/editorial e explicação comercial. Valores de grupo, puxador, material, id, cor, textura, contagem e seleção são dados; não devem ser congelados em copy. Nenhuma chave foi proposta ou migrada.

Próximo bucket: rastrear a renderização de materiais (`renderMaterials`, 12 candidatas no mapa) até seus inputs, opções e estados de remoção. Separar labels de interface dos nomes e atributos do catálogo, e preservar a regra de pluralização para a etapa de localização.
