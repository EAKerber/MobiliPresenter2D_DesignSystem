# PR #51 — triagem verificável do conteúdo residual (26/10/2026)

**Origem imutável:** [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), branch `docs/current-handover-20261024` @ `28062602a4ddcd1bee090742fe2587fe3837175d`. **Baseline da main:** `9386d0fc847369bfd5080cb22859b25c90cda021`.

**Inventário SHA-pinned:** [DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json](DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json) lista individualmente todos os blobs divergentes, tamanho, SHA de origem e SHA existente na main (quando houver). A classificação é estática; não certifica runtime, merge nem descarte.

## Resultado do confronto por árvores Git

| Grupo | Diferenças vs. main | Avaliação |
| --- | ---: | --- |
| `evidence/architecture/` exclusivos | 161 | 153 artefatos ARC-13 (rastros de consumidores e lotes de classificação) e 8 outros; documentação técnica datada. **Indexar primeiro, selecionar depois**, sem tratar propostas como decisões. |
| `evidence/runtime/` exclusivos | 60 | 49 textos e 11 WebP. São observações e capturas de 24–26/10, não provas do runtime atual. |
| Caminhos já existentes, mas divergentes | 11 | 2 workflows e 9 registros/documentos/inventários. Preservar autoridade atual da main; reconciliar por seções/campos e não substituir arquivos inteiros. |
| **Total** | **232** | **221 caminhos exclusivos** e **11 modificados**. Contagem diferente dos 236 arquivos da PR porque este inventário compara os heads atuais, não o diff histórico da PR. |

## Disposições e ordem

1. **D04-MEDIA-01 — extração exata proposta neste lote:** 3 WebP `image-failure-fallback-{baseline,option-a,option-b}-2026-10-25.webp`, somando 80.804 bytes. O documento de comparação [já está na main](../evidence/runtime/image-failure-fallback-options-2026-10-25.md) e aponta para esses três arquivos; importar os blobs corrige a preservação e os links. **Nenhuma opção A/B foi homologada**, pois são protótipos DOM simulados.
2. **ISSUE-226 — HOLD prioritário:** 8 capturas WebP na pasta `evidence/runtime/issue226-captures/` (~353 KB), acompanhadas por `issue226-current-production-matrix-2026-10-25.md`, `issue226-accordion-grid-current-production-recheck-2026-10-24.md` e `issue226-real-zoom-user-confirmation-2026-10-25.md`. Revisar versão de produto, estado da issue e valor da prova antes de importar; não concluir sucesso visual por capturas discrepantes.
3. **ARC-13 — HOLD/indexado:** 153 blobs únicos de consumidores/lotização (MD/JSON) devem ser agrupados por conjunto lógico e conferidos contra mapa atual de arquitetura/localização. Não duplicar quase 4,5 MB de evidências por inércia nem apagar os rastros antes de verificar cobertura.
4. **Runtime residual — HOLD:** demais evidências de acessibilidade, navegação, Viewer, CI, autenticação e propostas são datadas; selecionar as decisivas e anotar versões de produto, CI e limites. Não extrapolar uma amostra para conformidade geral.
5. **11 arquivos divergentes — HOLD/field-level:** `README.md`, `RUNTIME_AUDIT.md`, `DECISION_APPLICATION_MAP.md`, `FINDINGS_REGISTER.md`, `runtime-evidence.json`, `visual-inventory.json`, três docs de arquitetura/roadmap e dois workflows. **Não** reverter decisões canônicas nem ativar workflows legados. Comparar por campo e proveniência.

**Cálculo após integração do lote de 3 imagens (condicional ao merge):** exclusividades desta fonte caem de 221 para 218, e diferenças de 232 para 229, desde que nenhum dos heads tenha mudado. Os outros **218** caminhos permanecem HOLD. Nenhuma branch foi declarada elegível à exclusão por este recorte.

**Provenance gate:** imagens copiadas por referência ao próprio Git Blob SHA do commit `28062602a4ddcd1bee090742fe2587fe3837175d`; a ação de integração deve verificar SHA exato na main. Não reconstruir PNG/WebP, recodificar, nem usar print raster como substituto. D04=A, D01=A e D02=B continuam vigentes.

## Atualização de destinação D04 — 27/10/2026 (após PRs #89–#91)

Baseline vivo do Design System `main@6a4783b2f6217c689117b1183daceea00ef18f17`. Desde a fotografia deste arquivo, foram integradas [#89](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/89) (ownership estático + 6 consumer traces), [#90](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/90) (convenção ARC-13 aprovada em escopo restrito, Viewer e gate DS-05A) e [#91](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/91) (matrizes G0–G8, 8 rotas, 1.390 blocos CSS e issue DS-04). Todas foram seletivas e documentadas com hashes.

O saldo de **193 caminhos exclusivos da #51** após #91 é:

| Grupo remanescente | Arquivos | Tamanho aproximado | Disposição atual |
|---|---:|---:|---|
| `arc13-classified-*` | 38 | 1.777.887 B | HOLD: batches de classificação; avaliar cobertura/deduplicação vs fonte e versão antes de importar |
| Outros `arc13-*` (fora consumer/classified) | 38 | 2.420.206 B | HOLD: propostas/índices de suporte, não migrar automaticamente para catálogo |
| `*consumer-trace-*` | 69 | 143.278 B | HOLD: rastreios estáticos pontuais, selecionar por risco/owner |
| Outros `evidence/architecture/` | 3 | 15.817 B | HOLD: propostas/casos restantes, não aprovações de produto |
| `evidence/runtime/*.md` | 45 | 162.306 B | HOLD: snapshots de rotas, CI e previews, não status atual |

**Observação sobre os tamanhos:** os tamanhos foram calculados no tree atual após PR #91, comparando o HEAD SHA imutável da #51 com a main. Os 3 restantes no grupo de outros arquivos de arquitetura são propostas de VIS-002 para superfícies/foco, não homologações.

A PR [#51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51) está **CLOSED, NOT MERGED**, desde `2026-10-27T03:14:18Z` pelo evento atribuído à conta `EAKerber`. A branch de origem ainda existe; D04 e `ops/branch-dispositions.json` seguem impondo **HOLD**. Encerrar PR não prova integridade de todos os dados remanescentes e não satisfaz a elegibilidade do executor de exclusão. A PR #39 permanece aberta; #39 tem 21 exclusivos (12 docs/ADRs, 7 arquivos de experimento, 2 workflows antigos). Nenhum workflow histórico novo foi ativado.

## Seleção D04 ARC-13 por risco (27/10/2026)

Novo lote de seis blobs SHA-exact, classificado em [DS_ARC13_CONTRACT_REVIEW_2026-10-27.md](DS_ARC13_CONTRACT_REVIEW_2026-10-27.md). Quatro entradas `arc13-classified-*` e duas propostas `arc13-semantic-key-proposal-*`; o lote de teclado é controle negativo com 35/35 elementos técnicos não localizáveis. **Se e somente se** o lote passar merge/readback, exclusivos da #51: 193→187; batches classificados: 38→34; outros ARC13: 38→36; traces: 69; outras arquiteturas: 3; runtime: 45. O restante HOLD.

## Readback D03/D04 — PRs históricas fechadas e saldo real (27/10/2026)

A #39 está **CLOSED/NOT MERGED**, pois os 21 paths exclusivos foram tratados na PR #93 e os 9 canônicos foram reconciliados na PR #94, sem merge integral; ref fonte continua HOLD. A #51 também está CLOSED/NOT MERGED, com ref fonte HOLD. A #95 integrou seis ARC-13 por SHA exata (classes técnicas vs propostas de chave), reduzindo **193→187** caminhos exclusivos: 34 classified + 36 other ARC13 + 69 consumer traces + 3 VIS-002 candidates + 45 runtime docs = 187. [Actions #40444401507](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40444401507) PASS em `main@2d869a9c494313008930bd2e6ee8594262bd985d`. Nenhuma PR aberta no readback; nenhuma ref excluída. A fonte mestre ARC13 de 1.335.718 B não foi materializada/lida integralmente nesta rodada: preservar HOLD até poder conferir cobertura de forma reproduzível.

## Auditoria de cobertura ARC-13 (27/10/2026)

Leitura integral do mestre JS com **2.181** ocorrências e mestre HTML com **480**. Conferência por multiconjunto `arquivo+linha+texto+classificação` encontrou **27 de 29 lotes JS** e **7 de 7 lotes HTML** iguais nesse critério; dois lotes de UI JS/Viewer técnico não são equivalentes por terem propostas agregadas e templates normalizados, exigindo revisão de owner/consumer. Preservar 4 blobs fonte (índices+exceções) na [extração](DS_ARC13_MASTER_BATCH_RECONCILIATION_2026-10-27.md) e [prova SHA](DS_ARC13_MASTER_BATCH_AUDIT_2026-10-27.json). Se PR passar, 187→183 exclusivos na #51, sem declarar os demais lotes redundantes.

## D04 — fechamento da faixa `arc13-classified-*` (27/10/2026; pendente de merge)

Trinta lotes vinculados ao master não são contextualmente redundantes apesar de coincidirem nos quatro campos de ocorrência: conservam SHA de origem, notas e, em alguns casos, owners/consumers e parâmetros diferentes. Dois arquivos auxiliares são exclusões independentes do índice. [Manifesto](DS_ARC13_CLASSIFIED_CONTEXT_BLOBS_2026-10-27.json) e [relatório](DS_ARC13_CLASSIFIED_CONTEXT_RECONCILIATION_2026-10-27.md). Após merge, os 32 batches ficam preservados sem modificar a aprovação de chaves, e a #51 passa a 151 exclusivos (34 outros ARC13 + 69 consumer traces + 3 outros arquitetura + 45 runtime). Manter head HOLD.

## D04 — 69 traces e dois mapas (27/10/2026; pendente de gate)

Mais 71 fontes históricas do head #51: 69 MDs `*consumer-trace-*` e dois índices de escopo/contexto `arc13-unkeyed-consumer-*-map`. Identificam regras de autorização, price breakdown, estados de erro e ARIA não capturados por inventário lexical. [Manifesto](DS_ARC13_CONSUMER_TRACE_BLOBS_2026-10-27.json) · [riscos](DS_ARC13_CONSUMER_TRACE_PRESERVATION_2026-10-27.md). Após merge: 151→80 exclusivos. Permanecem 32 outras fontes ARC13, 3 propostas VIS-002, 45 notas runtime. Não existe autorização de descarte de histórico divergente.

## D04 — encaminhamento das 35 fontes arquiteturais remanescentes (27/10/2026)

32 fontes ARC-13 (chaves **ainda candidatas**) e 3 VIS-002 (uma proposta de foco Viewer autorizada somente para preview, demais não canônicas) copiados por SHA exato. [Manifesto](DS_D04_ARCHITECTURE_CANDIDATES_BLOBS_2026-10-27.json), [relatório de limites](DS_D04_ARCHITECTURE_CANDIDATES_2026-10-27.md). Após merge e readback, #51 terá **45** caminhos exclusivos restantes: exclusivamente relatórios `evidence/runtime/*.md`. Histórico de PRs/ref não muda.

## D04 — zero caminhos exclusivos da #51 (27/10/2026; após último lote, sujeito a readback)

45 relatórios runtime históricos em [manifesto Git exato](DS_D04_RUNTIME_EVIDENCE_BLOBS_2026-10-27.json) e [interpretação](DS_D04_RUNTIME_EVIDENCE_PRESERVATION_2026-10-27.md). Saldo esperado da diferença de paths 45→**0**, mas **11 paths existentes em ambas as árvores possuem blobs de conteúdo diferente** e a ref da #51 diverge em Git. Nenhum desses fatos autoriza eliminar a ref; verificar runtime historical states separadamente e manter `ops/branch-dispositions.json` como HOLD.
