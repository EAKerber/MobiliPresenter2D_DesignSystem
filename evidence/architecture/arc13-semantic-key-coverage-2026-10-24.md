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


## Tamanho da fila de revisão semântica — 25/10/2026

A `main` do produto ainda aponta para o `productHead` do índice ARC-13. Com os 13 exemplos de chaves numéricas e os cinco rótulos já verificados contra suas fontes, o restante pode ser preparado por módulo/consumer sem misturar ownership:

| Fila | Restantes | Agrupamento confirmado | Observação de revisão |
|---|---:|---|---|
| Chaves baseadas em linha | 199 de 212 | `configuration.js` 64; `hierarchy-administration.js` 32; `flow-model.js` 30; `presentation-contract.js` 29; `pricing-contract.js` 24; `administration-v5.js` 13; `legacy-stage-repair.js` 7 | 132 são templates com valores dinâmicos; documentar parâmetros e revisar owner/consumer antes de qualquer compartilhamento. |
| Ocorrências sem chave | 364 de 369 | `admin.js` 209; `app.js` 155 | 59 são templates; o índice ainda os classifica com consumer não resolvido, então precisa de leitura de contexto antes de nomear. |
| Conteúdo deferido | 190 | Inventário editorial separado | Não mesclar com strings de runtime nem gerar chaves sem atribuir owner e consumer. |

Esta é uma fila de revisão, não uma convenção aprovada nem um lote de migração. A convenção global e os owners continuam aguardando revisão humana.


## Decisão da convenção — 25/10/2026

O usuário aprovou a convenção operacional: preservar o namespace existente, usar sufixo semântico estável em camelCase, manter valores dinâmicos como parâmetros e compartilhar uma chave somente quando owner, consumer e contrato de parâmetros coincidirem. Números de linha, nomes de arquivo, texto traduzido e versões de schema não compõem a identidade da chave.

A aprovação canoniza as regras, não os exemplos nem seus owners. A auditoria dos 13 exemplos numéricos e cinco rótulos confirma correspondência única e ausência de colisões na amostra observada; cada chave ainda exige revisão contextual antes de migração. O índice, o runtime e decisions.json não foram alterados. A fila segue: 199 propostas numéricas restantes, 364 textos sem chave sem proposta e 190 itens de conteúdo deferidos.


## Primeiro lote após aprovação da convenção — configuration.js (25/10/2026)

O arquivo [arc13-semantic-key-proposal-configuration-batch-2026-10-25.json](arc13-semantic-key-proposal-configuration-batch-2026-10-25.json) registra candidatos para as 64 ocorrências remanescentes em app/core/configuration.js: 63 chaves sugeridas, 33 ocorrências com parâmetros e zero colisões com as chaves presentes no índice ARC-13. As ocorrências das linhas 455 e 459 compartilham a sugestão conflictingEventTarget: o texto, owner/consumer e parâmetro rule.id são idênticos, mas o registro mantém as duas proveniências para revisão contextual. Cada linha preserva texto atual, contexto de código, owner, consumer, parâmetros e hashes.

Este lote reduz de 199 para 135 as referências numéricas ainda sem sugestão. As chaves continuam candidatas, não foram inseridas no índice e nenhum código do produto foi alterado.


## Reconciliação da fila numérica — 25/10/2026

Os dois lotes subsequentes à aprovação da convenção agora cobrem as 199 ocorrências que não tinham proposta: 64 em configuration.js e 135 nos seis módulos centrais. O arquivo de configuration registra 63 chaves sugeridas (duas linhas idênticas agrupadas); o lote central registra 133 chaves sugeridas (três ocorrências idênticas agrupadas). Os 13 exemplos iniciais mais essas 199 propostas cobrem as 212 referências numéricas inventariadas. Isso é cobertura de proposta, não aprovação semântica final, ownership confirmado ou extração. Zero chaves propostas colidiram com o índice atual. A fila seguinte permanece 364 textos sem chave, com consumer não resolvido, e 190 itens de conteúdo deferidos em trilha separada.

[Lote de configuration.js](arc13-semantic-key-proposal-configuration-batch-2026-10-25.json) · [Lote dos seis módulos](arc13-semantic-key-proposal-core-modules-2026-10-25.json).


## Contexto da fila sem chave — 25/10/2026

As 364 ocorrências ainda sem chave foram mapeadas contra os arquivos-fonte no commit de produto registrado pelo índice. A análise lexical as agrupou em 72 funções candidatas; encontrou 22 grupos de texto repetido e seis valores com aparência de código/markup que exigem reclassificação. O agrupamento não confirma consumers nem autoriza compartilhamento. O próximo passo é revisar uso DOM/ARIA e ownership antes de propor as chaves.

[Mapa com proveniência e linhas](arc13-unkeyed-consumer-context-map-2026-10-25.json).


## Reclassificação sugerida de literais técnicos — 25/10/2026

A revisão de contexto confirmou seis ocorrências não textuais entre os 364 itens sem chave: classes CSS `has-module-detail` e `admin-note`, tags HTML `dl` e código interno `requirement-hidden`. As seis não devem receber chaves de localização. A mensagem visível na linha que contém `admin-note` permanece uma ocorrência localizável separada. Com esta revisão, 358 itens sem chave permanecem candidatos de texto; o índice original não foi alterado. [Auditoria](arc13-unkeyed-code-literal-reclassification-2026-10-25.md).


## Readback cruzado dos lotes e sinks — 25/10/2026

Revalidei todos os lotes de propostas no índice fixado. São 217 ocorrências propostas (13 exemplos numéricos, 199 sufixos numéricos restantes e cinco labels de Admin), com 214 chaves únicas. As três ocorrências excedentes estão agrupadas em duas chaves repetidas: duas instâncias de conflicting event target e três de unsupported layout profile. Todas têm contratos de owner/consumer/parâmetros registrados para revisão; não há colisões entre qualquer chave proposta e as chaves do índice atual.

Na fila originalmente não chaveada e unclassified, a inspeção de source/linha identificou 19 literais técnicos para exclusão; restam 345 candidatos de texto. Desses, 106 têm escrita textual direta, 33 são ARIA/alt, 14 são title/tooltip, três vêm de markup, 66 estão em mapas/arrays e 123 em outras expressões. Os últimos 189 ainda não foram ligados ao consumer real. [Auditoria de sinks](arc13-unkeyed-direct-sink-audit-2026-10-25.md) · [Reclassificação dos 19 literais](arc13-unkeyed-code-literal-reclassification-2026-10-25.md).


## Atualização da fila ARC-13 sem chave — 25/10/2026

A fotografia acima continua correta para a cobertura total de 728 ocorrências (369 sem chave, incluindo lotes com propostas separadas). Na subfila de 364 candidatos sem chave e sem consumer, a revisão separou 19 literais técnicos e quatro mensagens de diagnóstico interno, restando **341 itens**: 208 em `app/admin/admin.js` e 133 em `app/app.js`. Isso não altera o número do índice nem os 369 itens sem chave da cobertura total.

O [mapa corrigido](arc13-unkeyed-consumer-scope-map-2026-10-25.json) substitui o mapa anterior, que podia atribuir listeners do módulo à função anterior. São pistas lexicais/call sites; consumers, ownership e contratos seguem pendentes. Nenhum lote de chaves foi criado para esses itens.


## Reclassificação adicional de identificadores — 25/10/2026

A subfila cai de 341 para **338** após separar três formatos técnicos confirmados no código: slug interno de etapa, ID ligado por `aria-controls` e ID ligado por `aria-describedby`. Totais atuais da subfila: 22 valores técnicos e quatro diagnósticos internos fora da fila de revisão, 207 ocorrências no Admin e 131 no Configurador. A cobertura total do índice continua 728 localizáveis / 369 sem chave; nenhuma classificação canônica foi alterada.


## ARC-13 — primeiro lote com consumer confirmado (25/10/2026)

Rastreei `createDetailCarousel` no Configurador: o lote reúne **26 ocorrências** de títulos/rótulos curtos/descrições, nomes acessíveis, tooltips e ações de recolher. A proposta contém 16 chaves novas e quatro reutilizações intencionais de chaves já atribuídas ao mesmo carrossel; usa parâmetros `pageLabel`, `shortLabel`, `pageNumber` e `pageCount`. Anterior/próximo continuam mensagens distintas. A auditoria encontrou zero colisões com significado diferente e zero conflito de texto entre chaves. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-configurator-carousel-2026-10-25.json). O índice e o produto não mudaram; os itens continuam sem chave canônica até reconciliação.


## ARC-13 — ajuste após revisão do consumer do Viewer (25/10/2026)

O literal `Estrutural` em `updateSelection` é um valor comparado para escolher uma descrição, não um rótulo renderizado. A fila documental atual fica em **337 textos** (207 Admin, 130 Configurador), com 23 valores técnicos e quatro diagnósticos internos separados. [Reclassificação](../evidence/architecture/arc13-unkeyed-code-literal-reclassification-2026-10-25.md). O índice permanece em 369 textos sem chave no total; os lotes contextualizados continuam propostas até reconciliação canônica.


## ARC-13 — segundo lote com consumer confirmado (25/10/2026)

O consumer `updateSelection` foi revisado até os sinks DOM. Dos 13 registros do bucket, **12** têm proposta de chave em `configurator.moduleDetail`, sem colisão; `product.title` é parâmetro nomeado. O décimo terceiro item, ` · ${product.configurationNote}`, ficou deferido porque combina pontuação de composição com conteúdo vindo do catálogo; a ownership/mensagem final precisa ser confirmada antes de localizar. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-module-detail-2026-10-25.json). Nenhum índice ou runtime alterado.
