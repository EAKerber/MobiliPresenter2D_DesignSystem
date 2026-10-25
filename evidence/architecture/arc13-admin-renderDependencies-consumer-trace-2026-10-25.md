# ARC-13 — rastreio do bucket Admin renderDependencies — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderDependencies` tem quatro ocorrências. O rastreio segue o cartão e os selects até o helper de opções dinâmicas; as regras de validação/persistência da dependência não são alteradas nem inferidas só pelo texto da UI. Sem alteração do produto, índice, modelo ou `decisions.json); nenhuma chave foi proposta.

## As quatro ocorrências

| Linha(s) | Texto | Sink / estado | Owner e contrato |
|---|---|---|---|
| 1085 | Item dependente | Heading do cartão de cada `model.dependencies` rule. | Nome da relação no editor Admin; o cartão representa uma regra, não o item/entidade em si. |
| 1086 | Este item | Label do select `dependencyDependent`, valor selecionado `rule.dependentId). | Papel do item dependente na relação; opção/id vem de `entityOptions()`. |
| 1086 | Requer todos estes itens | Label do select múltiplo `dependencyRequires`, valores `rule.requires). | Papel da lista obrigatória na regra. “Todos” sinaliza semântica de AND; não simplificar para seleção sem confirmar o contrato. |
| 1087 | Remover dependência | Botão vinculado a `rule.id` via `data-remove-dependency). | Ação de remover uma regra inteira; o id identifica a regra e permanece dado dinâmico. |

## Opções e limites

Os dois selects compartilham `entityOptions()`, que deriva ids e labels de módulos, acessórios, itens de cena editáveis e entidades explicitamente incluídas. As opções são dados de catálogo/cena, não parte destas quatro strings. O primeiro select escolhe um valor; o segundo aceita múltiplos e `makeRuleSelect` define seu tamanho conforme o número de opções.

A análise do bucket identifica as labels e os campos que controlam. Não valida se todas as combinações de dependência são válidas, se ciclos são rejeitados ou como a regra afeta publicação; esses contratos precisam ser lidos no validador/consumer próprio antes de uma proposta de chave ou mudança de produto.

## Resultado e próximo passo

Foram rastreadas quatro strings de editor com uma regra relacional e dois papéis de entidade. A distinção entre item dependente e itens exigidos é parte do contrato do consumer; ids e nomes continuam dados. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin de quatro ocorrências a rastrear: `showPasswordAction`; distinguir convite e recuperação de senha sem unificar as ações.
