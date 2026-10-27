# ARC-13 — rastreio do bucket Admin renderFinishes — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderFinishes` tem quatro ocorrências sem chave. O rastreio seguiu os toggles e seletor de escopo, incluindo as guardas para não remover a última opção global ativa. Labels de material e módulo são dados do catálogo. Sem alteração do produto, catálogo, índice ou `decisions.json); nenhuma chave proposta.

## As quatro ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 860 | Disponível para clientes | Label do checkbox de ativação; estado `finish.enabled). O checkbox é desabilitado quando o acabamento é o último global habilitado. | Copy fixa do Admin. A guarda preserva ao menos uma opção de acabamento global ativa. |
| 866 | Global · conjunto todo; Local · módulo individual | Opções do seletor `finish.scope`, com valores técnicos `global` e `local). | Labels de enum do Admin; valores permanecem contrato. “Local” significa por módulo, não por unidade física ou usuário. A opção local fica bloqueada ao tentar desativar o único global habilitado. |
| 877 | Módulos que aceitam ${source.label} | `aria-label` do conjunto de checkboxes, somente em escopo local; `source.label` vem do material associado ao acabamento. | Template acessível com nome do material como parâmetro de catálogo. A lista mostra `module.referenceLabel`; ids persistidos são `module.entityId`. |

## Consumer e integridade

Cada cartão só aparece se o acabamento corresponder a um material existente e esse material pertencer ao grupo de frentes. A swatch e eventual textura também vêm do material. Quando local, o editor apresenta módulos e bloqueia a remoção do último módulo selecionado. Esses bloqueios são regras de integridade, não copy, e devem permanecer juntos dos controles.

O evento externo salva `enabled`, `scope` ou `moduleIds` em `model.finishes`. A chamada seguinte a `reconcileInitialMaterials()` pode ajustar o acabamento inicial; a UI é então atualizada. Nomes de materiais/módulos e seus ids não são textos fixos do Admin.

## Resultado e próximo passo

Quatro candidatas são labels de disponibilidade/escopo e um template acessível com nome de material. As regras de ao menos um acabamento global e ao menos um módulo por acabamento local são guardrails. Nenhuma chave foi proposta ou migrada.

Próximo bucket empatado por volume: `renderDependencies` (4 ocorrências); distinguir explicação de regra dos nomes de item e ids selecionados.
