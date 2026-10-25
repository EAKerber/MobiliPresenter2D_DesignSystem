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

Um lote de cinco rótulos administrativos de uma palavra recebeu sugestões contextuais em [arc13-semantic-key-proposal-admin-sinks-2026-10-24.json](arc13-semantic-key-proposal-admin-sinks-2026-10-24.json). São propostas não canônicas; os campos `semanticKey` do índice continuam sem alteração. A convenção global e as 364 referências restantes sem proposta, além das 212 referências com chave baseada em linha, seguem pendentes.


## Proposta de convenção para chaves ancoradas em linha

Uma proposta não canônica define regras e 13 exemplos de substituição semântica para a amostra de chaves numéricas, preservando os namespaces existentes e mantendo separadas mensagens com contratos de parâmetros distintos: [proposta](arc13-semantic-key-convention-proposal-2026-10-24.json). A proposta não altera o índice. Restam 199 das 212 chaves numéricas sem exemplo de substituição; Entre as 369 ocorrências sem chave no índice, cinco sinks têm propostas de chave em lote separado e 364 seguem sem proposta.


## Auditoria de proveniência e colisões — 25/10/2026

O índice ARC-13 revisado é o blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`, gerado para `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. Revalidei as propostas contra as ocorrências atuais desse índice: 13/13 substituições de chaves numéricas coincidem unicamente por arquivo, linha, chave atual e texto; os cinco rótulos de Admin também coincidem unicamente e não têm chave preenchida. As 18 chaves propostas não duplicam entre si nem colidem com chaves existentes do inventário.

Isso confirma proveniência e ausência de colisões para a amostra; não aprova a convenção, não resolve ownership/consumer e não altera índice, código ou `decisions.json`. Permanecem 199 das 212 referências numéricas sem proposta, 364 das 369 ocorrências sem chave sem proposta e 190 itens de conteúdo deferidos. A decisão de promover a convenção e os exemplos segue pendente de revisão humana.
