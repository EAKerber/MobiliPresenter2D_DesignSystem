# ARC-13 — preservação do contexto dos 32 lotes classificados restantes (27/10/2026)

**Fonte verificada:** [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), head `28062602a4ddcd1bee090742fe2587fe3837175d` (CLOSED, not merged); produto observado `5ccb2a8`. [Manifesto por Git Blob original](DS_ARC13_CLASSIFIED_CONTEXT_BLOBS_2026-10-27.json).

## Por que a equivalência do índice não permite descartar os batches

A [auditoria do índice-mestre](DS_ARC13_MASTER_BATCH_RECONCILIATION_2026-10-27.md) confirmou quatro campos iguais em 27/29 grupos JS e 7/7 HTML. Nesta rodada os **30 lotes classificados ainda exclusivos e vinculados ao índice** também tiveram sua correspondência lexical verificada diretamente. Porém, a tupla `file, line, text, classification` não transporta todos os campos de origem. Exemplos checados:

- **Admin (423 ocorrências) e Configurador (466):** os lotes guardam o SHA do JS de origem e as notas de classificação; os textos de `consumer` nos lotes são genéricos e diferem daqueles do índice-mestre. Não são objetos intercambiáveis.
- **Fluxos de validação:** o lote `configuration-validation-and-legacy-labels` mantém parâmetros em 36 registros; o `flow-model-validation` em 27. Lotes Viewer, drawing, scene e Landing também guardam parâmetros que podem mudar tradução e formatação.
- **HTML:** sete batches preservam `owner` e `consumer` mais específicos ou diferentes do índice lexical, com hashes dos documentos originais e notas. As chaves semânticas históricas diferem em 3 entradas de Admin estático, 2 do Configurador e 1 da Landing; **isso não aprova nenhuma delas**.
- **Controles negativos independentes:** `arc13-classified-inline-config-scripts` exclui três scripts embutidos (nenhum literal de UI localizável), e `arc13-classified-large-data-files` registra dois arquivos de dados com paths/imagens incorporadas, também sem recurso de texto para tradução. Não têm grupo correspondente nos índices JS/HTML.

Portanto, remover esses registros baseando-se apenas nos índices apagaria dados de decisão/contexto. O lote desta PR preserva **32 Git Blobs históricos sem alteração de bytes**, sendo **30 vinculados e 2 auditorias independentes**.

## Limites explícitos

- **Não** ativar tradução, migrar locale, criar strings do produto, substituir `decisions.json` ou promover `semanticKey` proposta.
- Reaproveitamento no produto requer nova inspeção de `owner`/`consumer`, parâmetros, interpolação, acessibilidade e versão do código.
- Os dois lotes de semântica não bijetiva `ui-js` e `viewer-configurator` já estão preservados com seus índices na [extração anterior](DS_ARC13_MASTER_BATCH_AUDIT_2026-10-27.json).
- Os lotes classificados são *evidência histórica técnica*, não regra visual nem aprovação de arquitetura. Manter snapshots datados, sem reescrever relatos antigos como estados atuais.

## Gate e saldo

Conferir os 32 arquivos somente sob `evidence/architecture/arc13-classified-*`, cada destino com SHA igual à origem. Não alterar `.github/workflows/`, `decisions.json`, índices master, produto, autenticação ou CSS. Preflight: **183 caminhos exclusivos** da #51; após integração/readback, **151** (0 batches `arc13-classified-*` exclusivos; demais 34 outros ARC13, 69 consumer traces, 3 propostas visuais, 45 runtime notes). Branch `docs/current-handover-20261024` continua HOLD: divergência histórica e ausência de prova de exclusão independente, mesmo que esses batches estejam copiados.
