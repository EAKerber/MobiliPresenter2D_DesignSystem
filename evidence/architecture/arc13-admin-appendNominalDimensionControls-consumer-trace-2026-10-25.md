# ARC-13 — rastreio do bucket Admin appendNominalDimensionControls — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O mapa classifica cinco ocorrências sem chave em `appendNominalDimensionControls`. O código declara três eixos; “Profundidade” não aparece como ocorrência candidata no mapa atual, e isso não foi tratado como falha nem duplicado na contagem. O rastreio conferiu o controle, o nome acessível e o handler de validação. Sem alteração do produto, do índice ou de `decisions.json); nenhuma chave foi proposta.

## As cinco ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 277 | Medidas nominais (mm) | Legend do fieldset, criado apenas quando `model.moduleDimensions[itemId]` existe. | Título do controle e unidade visível; a categoria “nominal” deve permanecer explícita. |
| 281 | Atualiza as cotas e vistas técnicas; não altera a geometria da cena. | Nota do fieldset. | Explica limite funcional do input: altera cotas/vistas técnicas e não geometria da cena. Confirmar wording técnico antes de reutilizar fora deste controle. |
| 283 | Largura; Altura | Labels dos inputs numéricos; o terceiro eixo, “Profundidade”, existe no mesmo array, mas não consta como candidato sem chave deste mapa. | Labels de eixo; manter as dimensões associadas às chaves de dados `width`, `height`, `depth`. |
| 296 | `${label}: ${axisLabel} nominal em milímetros | `aria-label` de cada input, com nome do módulo/objeto e eixo interpolados. | Template acessível; `label` e `axisLabel` continuam parâmetros. Unidade e qualificador nominal pertencem ao contrato. |

## Validação e fronteira de dados

O controle recebe `itemId` e `label` do catálogo de módulos, mas só é renderizado quando há dimensões nominais para esse item. Cada input é número com intervalo 1–5.000 mm e passo de 0,1. O handler `stagesList` valida número finito, limite e no máximo uma casa decimal; em valor inválido, restaura o valor anterior e emite mensagem de erro que pertence a outro bucket.

Os valores armazenados em `model.moduleDimensions[itemId][axis]` atualizam a informação nominal e vistas técnicas. Os ids dos eixos e os valores dimensionais são dados/contratos, não textos. Esta passagem não inspecionou todos os consumers downstream das vistas.

## Resultado e próximo passo

Cinco ocorrências foram rastreadas; “Profundidade” permanece fora da fila sem chave registrada, sem inferir o motivo. Preservar a unidade, o caráter nominal e o limite de que a geometria da cena não muda. Nenhuma chave foi proposta ou migrada.

Próximo bucket de hierarquia Admin por volume: `appendHierarchyChoiceOptions` (4 ocorrências), seguindo destinos compatíveis até labels, ids e regras de escolha.
