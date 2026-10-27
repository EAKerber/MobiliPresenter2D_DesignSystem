# ARC-13 — rastreio do bucket Admin renderObjects — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderObjects` tem sete ocorrências. Foram seguidas as labels dos campos até `makeField`, e a seção condicional de materiais até seu estado vazio. Os textos editáveis em `model.objects[id]` e os nomes de catálogo não foram tratados como copy fixa. Sem alteração do produto, catálogo, índice ou `decisions.json); nenhuma chave foi proposta.

## As sete ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 793 | Nome público | Label do campo `data.title`, texto usado como título público do item. | Label Admin; valor é conteúdo de produto sob owner editorial/catálogo. Preservar a decisão vigente: conteúdo fica no catálogo e deve ser revisado pelo owner. |
| 794 | Descrição | Label de `data.description`. | Label Admin; o texto descritivo permanece conteúdo do catálogo, não chave de interface. |
| 795 | Destaques (um por linha) | Label do textarea `data.benefits`; cada linha é um elemento do array de benefícios. | Label Admin com instrução de formato. Os itens são copy autoral/comercial e permanecem no catálogo para revisão do owner. |
| 796 | Componentes (um por linha) | Label do textarea `data.components`; cada linha é conteúdo configurável do item. | Label Admin; não extrair os nomes/valores de componentes como copy de interface. |
| 797 | Requisitos (um por linha) | Label do textarea `data.requirements`. | Label Admin; os requisitos continuam conteúdo de catálogo e precisam de revisão de owner antes de qualquer mudança. |
| 801 | Materiais deste puxador | Heading de uma seção exibida somente se o objeto selecionado também existir em `model.handleProducts`. | Copy da interface Admin para relação de catálogo; lista de materiais é dado dinâmico. |
| 803 | Nenhum material associado. Configure a lista na aba Cores e acabamentos. | Fallback quando a lista de ids não resolve para nomes de materiais. | Estado vazio mais orientação de navegação; só aparece em objetos puxadores e depende da aba de configuração. Confirmar owner de produto antes de agrupar com outras mensagens vazias. |

## Fronteiras de dados

`catalogObjects()` define os objetos selecionáveis e seus labels a partir de módulos, acessórios, serviços, puxadores e pacotes de pedra. Esse label forma o heading do cartão, mas não é uma destas sete ocorrências candidatas. `model.objects[id]` fornece título, descrição, benefícios, componentes e requisitos; esses valores podem ser específicos do catálogo e são editáveis pelo Admin.

A seção de materiais é condicional a uma correspondência de `priceEntryId`. A mensagem vazia é fallback para id sem label resolvido, não para “nenhum objeto” ou carregamento. Sua ação leva à aba Cores e acabamentos.

## Resultado e próximo passo

O bucket contém cinco labels de edição e dois textos condicionais sobre a relação de materiais do puxador. É necessário manter a fronteira entre copy da ferramenta e conteúdo de catálogo; o ownership dos cinco campos editoriais não foi transferido para o índice de interface. Nenhuma chave foi proposta ou migrada.

Próximo bucket empatado por volume: `appendInitialStateControl` (7 ocorrências); seguir opções de estado inicial e preservar nomes/labels de catálogo como dados.
