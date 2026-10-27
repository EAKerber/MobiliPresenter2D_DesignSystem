# ARC-13 — rastreio do bucket Admin renderMaterials — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

A consulta ao mapa encontrou **10** ocorrências para `function renderMaterials` (não 12 como a fila anterior estimava). O rastreio segue os labels e estados até os inputs, opções de arquivo, alvos, preview e botão de remoção. Helpers e handlers compartilhados foram verificados para distinguir texto de interface dos dados. Nenhuma chave foi proposta; produto, índice, catálogo e `decisions.json` não foram alterados.

## As 10 ocorrências

| Linha(s) | Texto | Sink / estado | Owner e contrato |
|---|---|---|---|
| 956 | Nome | Label de `makeField`; o mesmo `material.label` aparece no heading do cartão e segue editável como dado de catálogo. | “Nome” é label do Admin; título e valor editável não são copy fixa. |
| 957 | Cor base | Label do input HTML `color`; o valor vem de `material.color`, com fallback visual `#b7b0a7`; fica desabilitado quando o valor é `null`. | Label fixa; código de cor é dado/estado, não texto localizável. |
| 961 | Sem cor/tinta base | Texto junto ao checkbox que representa cor nula; checkbox só é editável quando `material.kind === "texture"`. | Copy de controle do Admin; a condição é regra de modelo e precisa permanecer sincronizada com o comportamento do input. |
| 962 | Tipo de material | Label do select do tipo. | Label fixa do Admin. |
| 964 | Cor sólida; Textura | Opções de tipo vinculadas aos enums `color` e `texture`. | Labels de opções localizáveis, valores do enum permanecem estáveis. “Textura” também aparece em outros contextos; não inferir compartilhamento sem comparar owner e sink. |
| 966 | Textura (arquivo existente) | Label do select de assets; as opções vêm de `materialAssetChoices()`, que combina arquivos referenciados pelo catálogo de acabamentos, pacotes de pedra e materiais existentes. | Label de interface. Caminhos são valores/dados; manter o escopo explícito de arquivos já existentes. |
| 968 | Somente cor | Option sentinel com valor vazio no select de textura. | Rótulo do estado sem textureAsset; valor vazio é contrato técnico. |
| 971 | `Textura ${material.label}` | `alt` do preview de imagem, presente apenas quando há `textureAsset`. | Template acessível com `material.label` como parâmetro/dado; não congelar o nome do material na chave. |
| 973 | Válido para… | Summary que abre o disclosure dos alvos; opções e seleção vêm de `materialTargetOptions()` e do estado dos grupos/puxadores. | Label concisa de controle. Nomes de alvo e ids vêm do catálogo/modelo. |
| 983 | Remover material | Texto visível do botão; recebe `data-remove-material=material.id`. O botão fica desabilitado para três materiais locked ou quando a remoção deixaria vazio algum grupo associado. | Ação de interface; id é dado. Preservar as guardas de integridade ao avaliar futuras mudanças no sink. |

## Limites de sink

O título do cartão usa o label do material como dado, também usado na thumbnail, no seletor de alvos e no editor de opções. A ocorrência localizável é apenas o template do `alt`; cada label do material continua sob ownership de catálogo.

Os estados de cor nula, textura, alvos associados e remoção não são copy isolada: governam controles, preview e integridade de grupos. A lista de arquivos tem origem no catálogo/modelo e não permite caminhos externos neste consumer. Não converter ids, paths ou valores de cor em mensagens.

## Resultado e próximo passo

Foram rastreados 10 candidatos, não 12. O lote mistura labels de edição, opções enum, um sentinel, um template acessível com dado e uma ação protegida por regras de integridade. Nenhuma chave foi proposta ou migrada.

Próximo passo: revisar o próximo bucket lexical do mapa por ocorrência e owner; não estimar sua contagem a partir do nome de função. Manter pluralização para a etapa de localização e pedir revisão do owner para texto de catálogo/editorial.
