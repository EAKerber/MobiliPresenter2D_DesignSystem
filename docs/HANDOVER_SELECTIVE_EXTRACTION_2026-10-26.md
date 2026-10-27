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

## Segundo recorte independente — PR #41 (20/10/2026)

**Origem:** [PR DS #41](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/41), head `ae58f2199e9b3be5ba4ea313c86e7d26dd60ff37`, [extração seletiva PR #78](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/78). Sete blobs originais foram incorporados nesta PR de extração, sem edição de bytes ou mudança de nomes, preservando os links entre documentos e capturas.

| Caminho original | Git Blob SHA |
| --- | --- |
| `evidence/runtime/access-confirmation-menu-2026-10-20.md` | `69763e80890473195e31b2a32cb48042adc20d2e` |
| `evidence/runtime/admin-login-menu-2026-10-20.md` | `f02e9e218ca812fef66228bd2f3db4e1d3c71940` |
| `evidence/runtime/private-menu-cross-tab-state-2026-10-20.md` | `d486214a482d7a0e6b78114746f1d476449a177f` |
| `visualEvidence/private/access-confirmation/access-menu-dark-2026-10-20.jpg` | `f3fee96753339663c7bac9a698ab23a65a6fe929` |
| `visualEvidence/private/access-confirmation/access-menu-light-2026-10-20.jpg` | `33773d9a5d9684daa1fcbd9db35a64afbccd6e3a` |
| `visualEvidence/private/admin-login/admin-login-menu-dark-2026-10-20.jpg` | `2041b7d977a5673b4ed2eff350b3cbb1a2c4d1fe` |
| `visualEvidence/private/admin-login/admin-login-menu-light-2026-10-20.jpg` | `bd311b2a8a2e968276b6a1799bced4942152eb3e` |

**Contexto fixo e limites:** observações anônimas de 20/10/2026 no produto `1878ae1057ce7c6190e0c8cb08a1f3baadd49463`, Netlify `6ad6c3b51b6be05647167f94`. Uma aba existente exibia menu de sessão autenticada enquanto outras exibiam sessão anônima, **sem prova causal nem login/logout controlados**. O estado atual, a validade de sessão, o fluxo de convites e os pares de contraste em todos os contextos **não foram validados por esta extração**.

Não houve promoção de `decisions.json`, alterações em `runtime-evidence.json` ou atualização de autoridade no README. A PR #41 foi **encerrada sem merge integral** após [#78](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/78) preservar os sete blobs exclusivos e [#79](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/79) classificar FIND-015 como achado histórico. Sua branch permanece **HOLD** para conservação do histórico divergente, sem elegibilidade automática à exclusão. O recorte é evidência histórica com proveniência de blob, não homologação de novo padrão.


## Terceiro recorte — D04-MEDIA-01 / inventário residual da PR #51 (26/10/2026)

O confronto de árvores `main@9386d0fc847369bfd5080cb22859b25c90cda021` vs. `#51@28062602a4ddcd1bee090742fe2587fe3837175d` encontrou **232 diferenças: 221 caminhos exclusivos + 11 arquivos existentes divergentes**. A classificação por grupos e SHA está em [DS_PR51_RESIDUAL_CLASSIFICATION_2026-10-26.md](DS_PR51_RESIDUAL_CLASSIFICATION_2026-10-26.md) e o inventário de cada blob em [DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json](DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json).

D04-MEDIA-01 seleciona as três capturas WebP citadas pelo documento `evidence/runtime/image-failure-fallback-options-2026-10-25.md`, preservando seus Git Blobs originais:

| Arquivo relativo a `evidence/runtime/` | Git Blob SHA | Bytes |
| --- | --- | ---: |
| `image-failure-fallback-baseline-2026-10-25.webp` | `86a4bd1a721ac54250f423953248f5580cfa8f57` | 33588 |
| `image-failure-fallback-option-a-2026-10-25.webp` | `a3cbaa497d4e95065c7e51ed4d9fb3aa17930052` | 22388 |
| `image-failure-fallback-option-b-2026-10-25.webp` | `9b31f191d704a3e9d43bf91d79b3aa747114539b` | 24828 |

Os estados representados são baseline, opção A e opção B em DOM isolado: **nenhuma opção foi homologada**. Esta integração é exclusivamente documental/binária, sem alteração de design tokens, decisões, workflows ou código de produto. O destino e a identidade dos blobs exigem readback após merge; até lá, os 218 arquivos ainda não escolhidos continuam sob HOLD, assim como a branch #51.

## Quarto recorte D04 — ISSUE-226 (26/10/2026, preservação histórica)

A origem continua [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), head `28062602a4ddcd1bee090742fe2587fe3837175d`. Selecionados **11 blobs originais** (3 Markdown de rastreamento + 8 WebP do antes/depois em claro/escuro). Contagem de bytes de imagens: **352424**, preservados sem transcodificação. Consulte o [manifest exato de proveniência](DS_ISSUE226_BLOBS_2026-10-26.json).

A sequência documental importa: `issue226-current-production-matrix-2026-10-25.md` inicialmente anotava a issue como aberta por zoom real pendente, mas `issue226-real-zoom-user-confirmation-2026-10-25.md` registra confirmação manual posterior do usuário em 400% e **declara issue encerrada em 25/10**. A leitura presente só confirma a **ordem e o texto dos snapshots históricos**, não reconsulta nem certifica a issue no repositório do produto. O teste manual não possui screenshot/medição própria; o gate WebKit isolado anterior passou conforme o documento. Não converter afirmações dos snapshots em verificação moderna independente.

Após esta extração, **207** caminhos exclusivos da #51 continuam HOLD (218 antes, 11 retirados), condicionados à manutenção dos mesmos heads. `decisions.json`, workflows, produto e deploys permanecem inalterados.

## Lote D04 — ownership e fluxo crítico Admin (27/10/2026)

Seleção de 9 blobs SHA-exact de [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) e [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51). Proposta de documentação estática/ownership (3) e contratos de erros, auth e publicação no Admin (6). Proveniência [JSON](DS_D04_OWNERSHIP_AND_ADMIN_BLOBS_2026-10-27.json) e [nota](DS_D04_OWNERSHIP_AND_ADMIN_2026-10-27.md). Não aplicar workflows históricos nem confundir PR com homologação. Contagens condicionadas ao merge: #39 21 exclusivos, #51 201. Gates de exclusão permanecem independentes.

## D04 — contrato ARC-13 e Viewer / DS-05A (27/10/2026)

Quatro fontes exclusivas da #51 em [manifesto](DS_D04_CONTRACT_PROVENANCE_2026-10-27.json) e [síntese com limites](DS_D04_CONTRACT_PROVENANCE_2026-10-27.md). Convenção de chaves aprovada apenas para nomeação (não exemplos), erro global do Viewer com placeholder aprovado para comportamento (não deploy), gate auth com pendências Keyboard/Flow. Dois documentos de suporte já existem na main com SHAs originais e não serão duplicados. Após merge, 197 caminhos exclusivos restantes na #51.

## D04 — matrizes CSS, G0–G8 e 16 achados DS-04 (27/10/2026)

Quatro documentos por Git Blob exato de #51, classificação e SHAs em [DS_D04_COVERAGE_RECONCILIATION_2026-10-27.md](DS_D04_COVERAGE_RECONCILIATION_2026-10-27.md) e [manifesto](DS_D04_COVERAGE_BLOBS_2026-10-27.json). As leituras de Production/PR são datadas e parciais; evidência estática não cobre navegador autenticado nem estado atual. Após merge, 193 exclusivos na #51.

## D03/D04 — PR #39 documentos, experimentos e workflows inertes (27/10/2026)

21 Git Blobs exclusivos da #39 selecionados: 12 docs/ADRs, 7 experimentos isolados e 2 arquivos de workflow mantidos como texto inerte `docs/architecture/legacy-workflow-sources/*.yml.txt` com **mesmo blob SHA**. [Relatório de risco](DS_PR39_EXCLUSIVE_CLOSURE_2026-10-27.md) · [manifesto 21 blobs](DS_PR39_ALL_EXCLUSIVE_BLOBS_2026-10-27.json). Não promova experimentos como contrato do produto; workflows antigos não ativados; 9 caminhos canônicos divergentes ainda exigem reconciliação por campo. Nenhum branch delete neste lote.

## D04 — seis contratos ARC-13 de baixo volume e controle negativo (27/10/2026)

Preservar em main por SHA exata de #51 (não mergeada) 6 arquivos de 24–25/10: proposta do fluxo de salvamento Admin (39 itens), validações de pricing (27) e Admin (72), navegação privada (29), controle negativo de teclado (35 itens, 0 localizáveis) e proposta do carrossel (26). [Relatório](DS_ARC13_CONTRACT_REVIEW_2026-10-27.md) · [manifesto](DS_ARC13_CONTRACT_REVIEW_2026-10-27.json). Inventário não valida segurança nem aprova chaves; #51 193→187 exclusiva após merge.

## ARC-13 — índices JS/HTML e exceções semânticas (27/10/2026)

Após ler o master via Git Blob SHA, auditoria original-vs-batches em 36 vínculos: 27/29 JS PASS no multiconjunto de quatro campos; sete de sete HTML PASS; dois batches JS têm normalização/composição semântica e referências de linha não-bijetivas. [Relatório](DS_ARC13_MASTER_BATCH_RECONCILIATION_2026-10-27.md) · [manifesto com 36 SHAs](DS_ARC13_MASTER_BATCH_AUDIT_2026-10-27.json). Extrair sem transformação dois índices e dois batches excepcionais, mantendo 183 exclusivos na #51 apenas após readback. Os demais batches ainda preservam owners e parâmetros contextuais únicos; não descartar pela contagem lexical.

## ARC-13 — contexto de classificação de 32 batches (27/10/2026)

Trinta lotes possuem mesmo multiconjunto lexical do master mas notas/owner/consumer/source-hash/params que não são inteiramente deriváveis do índice. Dois controles negativos independentes cobrem scripts embutidos e grandes arquivos de dados. [Manifesto exato](DS_ARC13_CLASSIFIED_CONTEXT_BLOBS_2026-10-27.json) · [justificativa](DS_ARC13_CLASSIFIED_CONTEXT_RECONCILIATION_2026-10-27.md). Não importar esse material como catálogo; saldo da #51 183→151 após merge.
