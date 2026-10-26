# D04 — extração seletiva do handover (2026-10-26)

Origem: PR #51 — https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51 ; branch docs/current-handover-20261024, head 28062602a4ddcd1bee090742fe2587fe3837175d.

O inventário de comparação apresentou 236 caminhos diferentes da main, dos quais 161 sob evidence/architecture e 67 sob evidence/runtime. A PR não foi mesclada integralmente.

Critério: importar agora sete documentos completos que dão apoio imediato às PRs ativas #238, #241–#244 e ao VIS-002C, sem modificar conteúdo, mantendo o Git Blob SHA como prova de proveniência. São evidências datadas, não validação moderna independente.

| Caminho preservado | SHA blob de origem | Escopo |
| --- | --- | --- |
| [evidence/runtime/pr238-ci-fixture-allowlist-cleanup-2026-10-26.md](../evidence/runtime/pr238-ci-fixture-allowlist-cleanup-2026-10-26.md) | `d74053c82c45a12b99207e22ca178fd242e57ea2` | CI #238 |
| [evidence/runtime/pr241-public-image-failure-coverage-2026-10-26.md](../evidence/runtime/pr241-public-image-failure-coverage-2026-10-26.md) | `7a2017e89095f5c611261686a08840a6e3fe69f5` | VIS #241 |
| [evidence/runtime/pr242-viewer-scene-image-failure-implementation-2026-10-26.md](../evidence/runtime/pr242-viewer-scene-image-failure-implementation-2026-10-26.md) | `88baeb2433b44f35a5549d15084d44841d97db65` | Viewer #242 |
| [evidence/runtime/pr243-issue224-carousel-in-motion-recheck-2026-10-25.md](../evidence/runtime/pr243-issue224-carousel-in-motion-recheck-2026-10-25.md) | `166553dd5c0177310a754b44b3cb65a709a677c7` | Landing #243 |
| [evidence/runtime/nav005-pr244-preview-implementation-check-2026-10-24.md](../evidence/runtime/nav005-pr244-preview-implementation-check-2026-10-24.md) | `16fec367c24d9dad78406c0de89033c9a396cbe1` | NAV-005 #244 |
| [evidence/runtime/vis002c-v03-preview-10-contexts-manual-review-2026-10-25.md](../evidence/runtime/vis002c-v03-preview-10-contexts-manual-review-2026-10-25.md) | `959131d6f2c5e469996333a2b17d15dc4f310e28` | VIS-002C v0.3 |
| [evidence/runtime/image-failure-fallback-options-2026-10-25.md](../evidence/runtime/image-failure-fallback-options-2026-10-25.md) | `23f3bfd65ada57fbb6fa5ac01bc4e42609e1a7c1` | Fallback histórico |

## Ainda não consolidado

- A branch e a PR #51 ficam preservadas até classificação dos demais arquivos. D04=A não significa eliminação do histórico não extraído.
- Os três WebP de comparação baseline/opção A/opção B de fallback continuam apenas na branch original, neste primeiro recorte textual. Origem: https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/tree/docs/current-handover-20261024/evidence/runtime . Não declarar estes binários perdidos; eventual importação deverá preservar os bytes.
- Não sobrescrever RUNTIME_AUDIT.md, DECISION_APPLICATION_MAP.md nem o roadmap/main com versões mais antigas divergentes. Selecionar mudanças por seção e rastrear autoria/SHAs.
- Na etapa seguinte, classificar os 161 rastros de arquitetura, os demais arquivos runtime e os documentos modificados como importados, indexados sem cópia, redundantes com evidência ou pendentes.
- Antes de fechar PR #51, registrar evidência de cobertura do conteúdo residual. Até lá o estado é HOLD/PRESERVE.

Primeiro lote D04: sete documentos originais, sem mudança de decisões visuais, runtime, tokens globais ou deploy.
