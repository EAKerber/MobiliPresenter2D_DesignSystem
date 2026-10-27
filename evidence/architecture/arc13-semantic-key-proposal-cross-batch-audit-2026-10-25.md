# ARC-13 — auditoria cruzada das propostas de chaves semânticas

**Data:** 25/10/2026  
**Produto de referência:** `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
**Índice:** `arc13-runtime-js-candidates-main-2026-10-24.json`, blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`  
**Branch documental:** `docs/current-handover-20261024`

## Escopo e método

Li os 30 arquivos `arc13-semantic-key-proposal-*.json` da branch, validei seu JSON e comparei as chaves em `entries` com as 2.181 ocorrências do índice fixado. Também agrupei entradas repetidas por chave e comparei texto, owner, consumer, sink e contrato de parâmetros. A auditoria foi somente leitura sobre o índice e o runtime.

- 517 registros de proposta em 30 arquivos.
- 507 chaves de proposta distintas; quatro correspondem a reaproveitamentos intencionais que já existem no índice.
- Nove grupos de chaves aparecem em mais de uma ocorrência. O uso compartilhado no carrossel preserva o parâmetro semântico `pageLabel`, embora o valor venha de `previousPage.label` ou `nextPage.label`.
- Os quatro reaproveitamentos preexistentes (`configurator.carousel.collapse.expand`, `configurator.carousel.collapse.collapse`, `configurator.carousel.action.show` e `configurator.carousel.action.hide`) já constavam como intencionais no próprio lote do carrossel; não encontrei outra colisão com o índice.

## Reconciliação feita

A chave candidata `admin.configurationLoad.revisionLabel` aparecia nos lotes `admin-interactions-auth` e `admin-remaining-controls` com o mesmo texto, owner, sink `revisionLabel.textContent` e parâmetro `revision`, mas rótulos de consumer diferentes (`loadSettings` e `revisionLabel shared DOM sink`). A inspeção do código de referência confirmou que as ocorrências de carga e gravação atualizam o mesmo campo de revisão no editor hierárquico. Padronizei ambas as propostas como **Admin configuration editor revisionLabel textContent**.

O índice tem dois fragmentos localizáveis na linha 1289 (`Versão ` e ` · editor hierárquico`); as duas ocorrências da mesma linha na proposta preservam essa origem fragmentada. Não é uma colisão de chaves.

## Resultado e limite

Não encontrei colisão de chave proposta não documentada contra o índice. Os registros duplicados restantes têm o mesmo owner/consumer/contrato, ou foram explicitamente agrupados por um parâmetro de mensagem compartilhado. A revisão documenta a aplicação da convenção aprovada, mas não canoniza chaves individuais.

Os 30 lotes continuam com status de proposta. Nenhuma chave foi escrita no índice, no catálogo, no produto ou em `decisions.json`; nenhuma migração de runtime foi realizada.
