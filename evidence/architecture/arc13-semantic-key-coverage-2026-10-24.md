# Cobertura e qualidade inicial de chaves semânticas ARC-13 — 24/10/2026

## Fonte e método

Índice atual do produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`: `arc13-runtime-js-candidates-main-2026-10-24.json`, blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`. As contagens abaixo foram calculadas sobre as ocorrências com `classification=interface-localizable`; não contam strings técnicas ou itens deferidos.

## Resultado

- **728 ocorrências** localizáveis no inventário JS.
- **359** têm campo `semanticKey`; **369** ainda não têm chave proposta.
- Entre as 359 com campo preenchido, **212 chaves terminam no número da linha de origem** (por exemplo, `admin.validation.164`, `admin.configuration.validation.23`, `admin.flowValidation.76`, `admin.hierarchyValidation.68` e `admin.pricing.validation.56`). São localizadores de código, não chaves semânticas estáveis para extração; deslocar código pode mudar o identificador.
- As 369 ocorrências sem chave se distribuem em 209 referências do lote Admin runtime, 155 do Configurador runtime e cinco rótulos de uma palavra descobertos na revisão de sinks DOM.
- Existem 346 valores distintos de `semanticKey` entre as ocorrências preenchidas. Algumas chaves aparecem em fragmentos de templates ou variantes de contagem; isso requer revisão dos parâmetros e da composição, não deduplicação automática.

## Limite e próximo passo

A presença de um valor no campo `semanticKey` não prova estabilidade semântica, unicidade de mensagem ou prontidão para extração. Este registro não escolhe a estratégia de chaves, não aprova conteúdo/ownership e não altera produto. O próximo lote de ARC-13 deve definir uma convenção semântica estável e revisar primeiro as 212 chaves ancoradas em linha, mantendo rastreabilidade para arquivo/hash/linha; em seguida, propor chaves para as 369 ocorrências ausentes. Fragments com parâmetros e mensagens de validação precisam de revisão de owner/consumer antes de formar catálogo.


## Proposta inicial separada

Um lote de cinco rótulos administrativos de uma palavra recebeu sugestões contextuais em [arc13-semantic-key-proposal-admin-sinks-2026-10-24.json](arc13-semantic-key-proposal-admin-sinks-2026-10-24.json). São propostas não canônicas; os campos `semanticKey` do índice continuam sem alteração. A convenção global e as 364 referências restantes sem chave estável ou com chave baseada em linha seguem pendentes.
