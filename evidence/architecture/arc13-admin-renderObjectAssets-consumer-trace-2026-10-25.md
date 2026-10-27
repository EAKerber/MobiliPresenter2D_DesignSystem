# ARC-13 — rastreio do bucket Admin renderObjectAssets — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderObjectAssets` tem 10 ocorrências candidatas. O rastreio cobre heading, três seletores de asset, texto alternativo, falha de imagem, estados vazios e nota de segurança/capacidade. A análise é estática em `main`; sem alterar código, índice, dados de assets ou `decisions.json), e sem propor chaves.

## Os 10 textos e seus consumers

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 815 | `${label} · arquivos da cena | Heading do cartão. `label` vem de `catalogObjects()`, chamada por `renderObjects()`, e pode ser nome de módulo, acessório, serviço, puxador ou pacote de pedra. | O sufixo é copy de interface; o nome é catálogo/dado e deve permanecer parâmetro. |
| 818 | Imagem da cena; Imagem dos detalhes; Máscara de acabamento | Três labels para selects separados pelos campos `imageAsset`, `detailImageAsset` e `maskAsset`. | Rótulos de interface com semânticas distintas; não os unificar. |
| 821 | Usar o padrão / sem máscara | Option vazia com valor `""), disponível nos três selects. | Sentinel de interface; o significado depende do campo e do comportamento do preview. |
| 827 | `${title} · ${label} | `alt` da imagem de preview, com o título do seletor e o nome de catálogo como parâmetros. | Template acessível. Preservar ambos os nomes dinâmicos e não armazenar o alt como dado do asset. |
| 828 | Prévia indisponível | Texto inserido no preview ao ocorrer erro de carregamento de uma imagem. | Estado de erro visual da prévia; o handler usa `{ once: true }`. Não informa que o arquivo foi removido do catálogo nem afeta o select. |
| 829 | Sem máscara · usar o recorte padrão | Estado sem preview path. O ramo aparece para `maskAsset` sem máscara e também quando não há caminho/default de cena para os campos de imagem. | Texto condicional cujo wording menciona máscara, mesmo em campos de imagem. Validar com owner se todos esses contextos são intencionais antes de criar chave/corrigir copy. |
| 832 | A lista contém apenas arquivos já presentes na cena. O painel não carrega arquivos novos nem permite caminhos externos. | Nota mostrada quando `id` corresponde a uma entidade da cena. | Limite de capacidade e segurança do painel; preservar a distinção entre seleção de arquivo existente e upload/caminho externo. Confirmar owner técnico antes de reescrever. |
| 832 | Este item não possui camada visual própria na cena. Configure cores e texturas na biblioteca de materiais. | Nota alternativa quando o objeto de catálogo não tem entidade visual na cena. | Estado de contexto sem camada; direciona para outro owner/tela (Biblioteca de Materiais), não é a nota de segurança do ramo anterior. |

## Fronteiras de dados verificadas

- `assetChoices("imageAsset")` coleta `entity.asset` da cena. A lista é usada tanto para imagem da cena quanto para imagem de detalhes.
- `assetChoices("maskAsset")` coleta máscaras da entidade e variantes de acabamento. Todos os caminhos são deduplicados e ordenados; são valores dinâmicos, não copy.
- O select fica desabilitado se o id de catálogo não existir em `scene.entities`. O preview de imagem/definição de detalhes pode usar o asset default da entidade; máscara sem override não tem imagem de preview.
- O heading e os alts usam labels de catálogo. Não são nomes próprios da interface Admin.

## Resultado e próximo passo

As 10 candidatas representam três campos distintos, um option sentinel, dois templates/estados de preview e duas notas de contexto. O texto “Sem máscara · usar o recorte padrão” precisa de leitura contextual porque o mesmo fallback também pode aparecer num campo de imagem. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin por volume: `renderPricing` (8 ocorrências); rastrear os textos até os modelos de preço, regras e mensagens dinâmicas, mantendo quantias e percentuais como dados.
