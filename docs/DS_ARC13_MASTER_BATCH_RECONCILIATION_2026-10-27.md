# ARC-13 — auditoria real de índices e lotes classificados (27/10/2026)

**Fonte histórica pinada:** [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), branch `docs/current-handover-20261024@28062602a4ddcd1bee090742fe2587fe3837175d`; produto de referência `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. Esta auditoria **leu integralmente os dois índices** e os 36 lotes referenciados, usando comparação multiconjunto da tupla `arquivo + linha + texto + classificação`. [Resultado JSON por lote e SHA](DS_ARC13_MASTER_BATCH_AUDIT_2026-10-27.json).

## Resultado quantitativo

| Matriz | Ocorrências fonte | Lotes | Lotes coincidentes no critério de quatro campos | Lotes com transformação semântica não equivalente |
| --- | ---: | ---: | ---: | ---: |
| [Índice JavaScript](../evidence/architecture/arc13-runtime-js-candidates-main-2026-10-24.json) | 2.181 | 29 | **27** | **2** |
| [Índice HTML](../evidence/architecture/arc13-static-html-candidates-main-2026-10-24.json) | 480 | 7 | **7** | **0** |

O índice JavaScript registra **728** ocorrências localizáveis, **1.263** técnicas excluídas e **190** diferidas; total = 2.181. O índice HTML registra **464** localizáveis, **4** excluídas e **12** diferidas; total = 480. Os 36 ponteiros `classificationBatch` dos índices têm blobs reais no commit de origem; nenhum vínculo de lote está ausente.

Nos **34 lotes coincidentes**, a multiplicidade das quatro propriedades é igual entre índice e batch, inclusive ocorrências repetidas. Esta prova não compara todos os campos (`owner`, `consumer`, `parameterContract` etc.), não torna uma proposta homologada nem demonstra atualização do produto atual.

## Duas exceções reais — não 'corrigir' automaticamente

1. [Viewer/Configurator técnico](../evidence/architecture/arc13-classified-viewer-configurator-batch-2026-10-24.json): **30 ocorrências brutas** no índice, mas **33 entradas semânticas** e **41 localizações de fonte** no batch. Contratos de caption/ARIA/descrição estão agrupados ou ampliados; não há bijeção arquivo/linha/texto. O índice bruto tem ocorrência em `app/core/technical-drawings.js:93` e fragmentos `app/viewer/technical-views.js:34`; o batch enumera outros call sites, como `technical-drawings.js:76`. **HOLD para conferência por consumer/call site**, não concluir erro de código sem novo readback.
2. [UI JS, acesso e tema](../evidence/architecture/arc13-classified-ui-js-batch-2026-10-24.json): **23 ocorrências brutas** versus **27 entradas semânticas**. Frases com template de expiração são normalizadas para `{expiry}`, e os fragmentos do seletor de tema são compostos em rótulos/templates completos. Exemplo de divergência de origem: o índice cita `app/access/manage.js:66` para `Expirado`, o batch usa `app/access/manage.js:152`. **HOLD de proveniência/owner**; não propagar linhas antigas como corretas.

Os dois batches divergentes foram preservados lado a lado com os índices para conservar nuances, em vez de sobrescrever um pelo outro. A aprovação da convenção de chaves ARC-13 em 25/10 autoriza apenas a convenção, não exemplos, owner, strings normalizadas ou migração.

## Escopo desta integração e sequência

- **4 Git Blobs exatos**, sem recodificação: dois índices mestres JS/HTML e os dois batches que precisam de conciliação contextual. A main recebe fonte inspecionável e exceções sem ativar código/testes de produto.
- **#51: 187 → 183 caminhos exclusivos** após merge/readback. Ainda restam batches, propostas, 69 rastreios de consumer, capturas/notas runtime e versões canônicas divergentes; não apagar a ref.
- Próximo passo de alto valor: verificar as duas exceções com o código-fonte da revisão pinada ou no trabalho futuro de produto; para os demais batches, decidir se notas de owner/params exigem preservação explícita além dos quatro campos. A prova de 'igualdade lexical' **não autoriza descartar material com informações de contexto**.
- Nenhuma mudança em `decisions.json`, tokens, tradução, código da aplicação, workflows, autenticação, preview, deploy ou política de exclusão.
