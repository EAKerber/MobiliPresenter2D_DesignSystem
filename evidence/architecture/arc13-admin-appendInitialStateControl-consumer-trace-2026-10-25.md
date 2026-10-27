# ARC-13 — rastreio do bucket Admin appendInitialStateControl — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function appendInitialStateControl` tem sete ocorrências candidatas. O rastreio segue branches de módulos, objetos e serviços, preservando nomes de item como valores dinâmicos de labels acessíveis e distinguindo estados de configurador e Viewer. O helper de medidas nominais é uma fronteira relacionada, fora deste bucket. Sem alterações no produto, índice ou `decisions.json); nenhuma chave foi proposta.

## As sete ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 241, 263 | `${item.label}: ativo inicialmente | `aria-label` do checkbox de estado inicial, nos ramos `module/object` e `service`. O módulo/objeto grava em `initialState.entities`; serviço em `initialState.services`. | Template acessível com nome do item como parâmetro. Os dois sinks compartilham frase e função auxiliar; revisar se owner, significado e contrato da variável podem ser compartilhados antes de propor uma chave única. |
| 244 | Iniciar visível no configurador | Texto visível do controle inicial no ramo `module`. | Label de interface para visibilidade inicial na superfície do Configurador. |
| 244, 266 | Iniciar ativo | Texto visível no ramo `object` ou `service`. | Label fixa para ativação inicial; embora compartilhe estado booleano com “visível”, o significado de domínio não é igual ao de renderização de módulo no Configurador. |
| 251 | `${item.label}: visível inicialmente no viewer | `aria-label` do checkbox `initialViewerEntity`, só para `module`; grava em `initialState.viewerEntities`. | Template acessível distinto do estado inicial no Configurador; nome do módulo é parâmetro/dado. |
| 254 | Iniciar visível no viewer | Texto visível do checkbox acima, somente para módulos. | Label de interface específica da visibilidade inicial no Viewer; não combinar automaticamente com o controle do Configurador. |

## Fronteiras observadas

A função seleciona o branch pelo kind retornado de `configurationCore.itemRegistry(catalog)`. Módulos e objetos têm controle inicial do Configurador; somente módulos recebem controle adicional de visibilidade inicial no Viewer e chamada a `appendNominalDimensionControls`. Serviços usam outro armazenamento inicial e só têm o controle “Iniciar ativo”. Outras categorias não geram controles neste helper.

Os dois usos de “ativo inicialmente” têm o mesmo texto e interpolação, mas estão associados a estruturas de estado diferentes (entities e services). A semelhança permite investigação de compartilhamento; não é aprovação automática, pois o contrato do estado e o owner precisam coincidir. O label de “visível” não é sinônimo de ativo.

## Resultado e próximo passo

Foram rastreadas sete ocorrências em três famílias de item e dois contexts de exibição. Nomes são parâmetros; estados booleanos e ids ficam nos dados/contratos. Medidas nominais seguem outro helper e precisam de seu próprio rastreio. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin por volume: `loadSettings` (7 ocorrências); seguir os estados de carregamento, falha e recuperação sem colapsar erros distintos.
