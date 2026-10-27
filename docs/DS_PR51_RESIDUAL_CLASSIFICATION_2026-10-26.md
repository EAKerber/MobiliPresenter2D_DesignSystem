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
