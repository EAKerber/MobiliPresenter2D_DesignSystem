# ARC-13 — rastreio do bucket Admin appendHierarchyChoiceOptions — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8); mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function appendHierarchyChoiceOptions` contém quatro ocorrências. O rastreio seguiu a geração de escolhas por tipo de catálogo e a condição de renderização; esta seção só expõe estado e não altera opções. Pluralização permanece adiada para a etapa de localização. Nenhuma chave foi proposta; produto, índice e `decisions.json` inalterados.

## As quatro ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 380 | Opções do item · ${availableCount} disponível(is) | Summary do disclosure, só criado quando há opções; contagem soma opções cujo `available` é verdadeiro. | Label de interface com contagem dinâmica; o contrato plural foi adiado. “Opção” neste painel não significa item hierárquico independente. |
| 384 | Estas são opções do item, não itens hierárquicos independentes. Disponibilidade e dados comerciais continuam nas abas próprias. | Nota dentro do disclosure. | Regra de domínio/editor: opções pertencem ao item e disponibilidade/dados comerciais são editados em outras abas. Preservar essa separação de ownership e consumer. |
| 398 | Disponível; Indisponível | Status visível por escolha, derivado de `choice.available`. | Estados de interface; label/id da opção vem do catálogo. Disponibilidade é computada conforme o tipo: puxadores pela lista do grupo com exceções de ausência, acabamentos pela lista + enabled + scope global, e pedras pela lista de grupo quando houver. |

## Fronteiras observadas

`hierarchyChoiceOptions(itemId)` obtém a origem de opções a partir das capacidades do item. Cada escolha é um registro com id, label e boolean `available`; os nomes variam por catálogo e são dados. O helper não cria seletor nem persiste alterações, apenas apresenta o estado atual no cartão hierárquico.

O disclosure nem aparece quando não há choices. O número do summary é dinâmico e a palavra em `disponível(is)` exige pluralização futura. A nota é a fronteira contra tratar as escolhas como filhos da hierarquia ou mover os dados comerciais para este consumer.

## Resultado e próximo passo

Quatro ocorrências foram rastreadas. Há um template com contagem, uma explicação de ownership e dois estados binários, com labels de opção provenientes do catálogo. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin por volume: `renderFinishes` (4 ocorrências), distinguir os labels de disponibilidade/aplicação dos valores e nomes de material/variante.
