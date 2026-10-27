# ARC-13 — rastreio do bucket Admin renderEvents — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket exato `function renderEvents` tem 13 ocorrências candidatas. O rastreio segue cada ramo de renderização até os elementos adicionados a `eventsList`. A análise é estática do consumer no head registrado; não testa persistência nem altera código, índice, catálogo ou `decisions.json`. Nenhuma chave foi proposta.

## Consumers e contratos

| Linha(s) | Texto(s) | Sink / condição | Limite semântico |
|---|---|---|---|
| 1099 | Ajuste de dimensão; Ativar ou desativar item; Ajuste legado de profundidade | Heading do cartão, escolhido pelo valor persistido de `rule.action`: dimensões como padrão, mudança de estado ou ação histórica `set-depth`. | Três rótulos de heading do editor. O ramo legado não deve ser confundido com a ação atual de dimensão. Confirmar com owner técnico se o termo “legado” é copy adequada ao usuário Admin. |
| 1101 | Alterar dimensão de módulo; Ativar ou desativar módulo ou serviço; Profundidade fixa do Módulo 07 | Opções visíveis do seletor “Ação”, associadas aos valores técnicos estáveis `set-dimension`, `set-enabled` e `set-depth`. | Labels de opções do contrato de regras. A opção do Módulo 07 descreve compatibilidade histórica e nomeia o alvo; não converter esse identificador em parâmetro sem rever o formato armazenado. |
| 1102 | Quando este item | Label do seletor `eventTrigger`; as opções vêm dinamicamente de `eventTriggerOptions()`. | Label fixa de campo; entidades e nomes de opções são dados dinâmicos fora deste bucket. |
| 1105 | Aplicar ao Módulo 07 · Profundidade em mm | Texto de label somente no ramo legado `set-depth`; o input numérico recebe `rule.valueMm` e guarda o valor em mm. | Label técnica condicionada ao schema antigo. Preservar a unidade e o vínculo histórico com o Módulo 07; o valor numérico é dado, não copy. |
| 1108 | Aplicar a | Label do alvo no ramo `set-enabled`; opções são entidades fornecidas ao seletor. | Consumer de estado. Embora use o campo `targetId`, não tem a mesma lista de opções do ramo de dimensão. |
| 1109 | Definir estado | Label do seletor do estado aplicado no ramo `set-enabled`; o valor salvo é booleano convertido para string. | Label de campo. Os valores do seletor são enum de estado, separados de texto livre; não inferir uma chave a partir dos valores técnicos. |
| 1112 | Aplicar ao módulo | Label do alvo no ramo atual de dimensão; opções são compostas de módulos do catálogo com referência e título. | Consumer de dimensão; a lista e os títulos vêm de dados do catálogo e não são constantes localizáveis deste bucket. Não compartilhar automaticamente com “Aplicar a”. |
| 1114 | Valor em mm | Texto de label do input numérico de dimensão; `rule.valueMm` fornece o dado. | Preservar unidade métrica; o número é dinâmico e não deve ser embutido em uma string. |
| 1117 | Remover evento | Texto visível do botão de remoção; o mesmo botão recebe `data-remove-event=rule.id`. | Ação do editor. O identificador do evento é dado dinâmico; manter a ação vinculada à regra correta. |

## Síntese

Os 13 candidatos são labels e headings de editor distribuídos entre três tipos de regra com estados e schemas diferentes. A condição vem de `rule.action`; opções, catálogo, ids e valores numéricos são fornecidos como dados. Os labels “Aplicar a” e “Aplicar ao módulo” têm campos parecidos, mas listas distintas e consumidores diferentes. O ramo `set-depth` mantém linguagem e unidade de compatibilidade que pedem revisão técnica antes de qualquer proposta de chave.

A classificação de owner como interface Admin é uma pista de consumer, não substitui a revisão do responsável pelo contrato de regras. Pluralização não se aplica a este lote. Não propor chaves nem migrar o índice nesta etapa.

## Próximo passo

Rastrear `renderMaterialGroups` (12 ocorrências) até seus sinks e dados dinâmicos. Preservar a distinção entre labels da interface e nomes/valores fornecidos pelo catálogo.
