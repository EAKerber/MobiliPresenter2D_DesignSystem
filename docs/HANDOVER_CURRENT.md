# HANDOVER CANÔNICO — MobiliPresenter2D Design System

**Checkpoint verificado:** 26/10/2026, fuso `America/Sao_Paulo`.  
**Destino:** próximo chat/agente sem acesso ao contexto corrente.  
**Prioridade atual:** estabilizar, reconciliar e reduzir as branches do **Design System primeiro**. Não retomar trabalhos no repositório do produto até nova orientação do usuário.  
**Este é o ponto de retomada permanente**; o README aponta para cá. Ler o GitHub em tempo real antes de assumir que números ou SHAs continuam atuais.

## Verificação posterior à PR #82 — snapshot de retomada (26/10/2026, São Paulo)

**SHA de `main` confirmado antes desta atualização documental:** `ae9ac472ed4092effd12a3c41d5e3e560dc40f18`, [PR #82](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/82) **MERGED**. A leitura independente de GitHub encontrou **10 branches** (1 `main`, 1 operacional e 8 HOLDS), apenas **duas PRs abertas** ([#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39), [#51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51)) e observação sem escrita da [Actions #40428162828](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40428162828) **PASS** no mesmo SHA.

**Branch operacional ativa:** `maintenance/ds-pr41-runtime-evidence-extract-20261026@9107ec1fce1feb90429c28729bc6c2e4014f1626` (sem PR aberta em seu head; **não presumir seguro apagar** sem gate completo). Os oito HOLDS estão enumerados na seção 4 e registrados em `ops/branch-dispositions.json`; **não excluir por ser branch antiga ou PR encerrada**. `ops/branch-hygiene-batch.json` conserva o lote P12 já consumido, **não deve ser reaplicado**. O executor ativo é o portado do produto (PR #64); o legado foi desativado.

**Verificações materiais recentes:** PR [#80](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/80) aplicou P12 com readback; PR [#81](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/81) atualizou o procedimento; PR [#82](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/82) publicou este handover e seu ponteiro no README. A extração exata de sete blobs de #41 está na PR #78, o FIND-015 datado na #79, e a #41 ficou **CLOSED sem merge** e **branch HOLD**. A PR #51 ainda contém numerosos arquivos exclusivos (especialmente arquitetura/runtime) e a #39 experimentos/propostas não homologados. A próxima ação é **classificação e extração seletiva com proveniência**, não apagar em massa.

Este bloco registra somente **documentação e leitura Git/Actions**. Não comprova conformidade funcional de login, contraste, produto ou publicação. O commit produzido por esta própria atualização virá depois do SHA de snapshot acima; obter o SHA efetivo na API ao retomar.

## 0. Bootstrap indispensável

1. Consultar o SHA de `main`, inventário completo de branches, PRs abertas/fechadas relevantes e Actions no repositório [Design System](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem).
2. Ler este arquivo, [guia operacional de higiene](BRANCH_HYGIENE_OPERATIONS.md), [D01–D04 homologadas](APPROVALS_D01_D04_2026-10-26.md), [ledger de extração D04](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md), `decisions.json`, os manifests `dist/` e `FINDINGS_REGISTER.md`.
3. O repositório do produto é [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D); o [handover canônico do produto](https://github.com/EAKerber/MobiliPresenter2D/blob/main/docs/handoffs/HANDOVER-CURRENT-2026-10-26.md) descreve a área de produto. **Não editar, criar previews ou iniciar refatorações de produto** durante a etapa atual.
4. Usar o conector GitHub, sem depender de `gh`. Antes de qualquer escrita: revisar conteúdo exclusivo, HEAD exato, proteções, relações com PR, dependências de workflows, gate e rollback. Atualizar este handover a cada checkpoint material.

## 1. Objetivo e decisões de governança

**Objetivo do usuário:** reduzir a divergência histórica/documental do Design System, preferencialmente a **uma única branch permanente (`main`)**. A meta não é licença para descartar arquivos únicos, fechar PRs indiscriminadamente, apagar árvores de Git exclusivas, ou transformar documentos antigos em norma atual.

**Decisões expressas e vigentes (26/10/2026):**

- **D01=A:** integração incremental, somente após os gates técnicos aplicáveis.
- **D02=B:** aceitar inicialmente testes isolados **quando cobrem de fato o contrato**, deixando explícito o que falta validar em autenticação/runtime real. Não equivale a conformidade global.
- **D03=A:** extrair o que ainda é útil das PRs CP-PUBLIC substituídas e somente então encerrá-las, com prova de cobertura.
- **D04=A:** consolidação seletiva de documentação/evidências com **proveniência e SHA de origem**; não mesclar integralmente a PR DS #51.

Todas as homologações visuais já encerradas permanecem **CLOSED**; não reabrir debates resolvidos (cores, VIS-002, NAV-005, etc.) por encontrar uma implementação divergente. Separar `DECISION_APPROVED`, `TECHNICAL_GATE_PASS`, `DEPLOYED`, `RUNTIME_VERIFIED`, `HISTORICAL_EVIDENCE` e `SAFE_TO_DELETE`: nenhum implica automaticamente os demais. `decisions.json` é fonte para as decisões; as páginas manuais, propostas e capturas são apresentações/observações, não autoridade substituta.

## 2. Estado Git/CI comprovado antes desta publicação

| Item | Verificado |
| --- | --- |
| Design System `main` antes do commit deste handover | `38363dfb8a5b788544931d43ed3f6c72fe6bd719` — [PR #81](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/81) |
| Branches DS | **10**, sendo `main` + 1 operacional + 8 HOLDs |
| PRs DS abertas | [#39 DOM/CSS e UI declarativa](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39), [#51 handover/evidências acumuladas](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51) |
| PR #41 | **CLOSED sem merge integral**; extrações aprovadas já na `main`, branch preservada |
| Hygiene observacional da main | [Actions #40425292755](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40425292755), **PASS** |
| Último lote de exclusão | [PR #80](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/80), audit [#40424786709](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40424786709) PASS, apply [#40424863430](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40424863430) **PASS/readback PASS/count=1** |
| Repositório do produto (somente leitura) | `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, **61 branches**, **12 PRs abertas** |
| Product production | Última verificação histórica no handover do produto: Netlify READY alinhado ao seu main. Não foi emitido novo preview/deploy neste trabalho. |

Este documento, quando integrado, criará um SHA de `main` posterior ao registrado na tabela. **É necessário reconsultar a main para obter o commit efetivo.** Não presumir que os valores sejam atuais em um novo chat.

## 3. Higiene: ferramenta canônica e resultados

O Design System **já possui o mecanismo do repositório de produto portado e testado**, integrado em [PR DS #64](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/64):

- `tools/branch_hygiene_observe.py` — inventário Git/API paginado, proteção, árvore, ancestry e heads/bases de PRs abertas.
- `tools/branch_hygiene_plan.py` — plano determinístico com hash e preservação explícita (`ops/branch-dispositions.json`).
- `tools/branch_hygiene_apply.py` — batches **de 1 a 3 refs com SHA exato**, reobservação, prova de squash-tree quando aplicável, bloqueio de workflows referenciando branches, `--force-with-lease`, readback independente e recibos.
- `.github/workflows/branch-hygiene.yml` — **somente leitura** e artefatos de observação; trigger semanal/manual/PR/main.
- `.github/workflows/branch-hygiene-bounded.yml` — **audit-only no PR**; `apply` apenas no push `main` se `ops/branch-hygiene-batch.json` tiver mudado; sem comando genérico `delete all`.
- `tests/test_branch_hygiene_*.py` — regressões de segurança. Executor/manifest/workflow antigos `retire_merged_branches` foram aposentados e preservados somente no histórico Git.

**Ledger principal:** [BRANCH_HYGIENE_OPERATIONS.md](BRANCH_HYGIENE_OPERATIONS.md) — modo de usar, dez primeiros lotes, recibos Actions e HOLDs. Depois, [#77](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/77) / [apply #40423479233](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40423479233) removeram ref preparatória vazia (`count=1`); [#80](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/80) / [apply #40424863430](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40424863430) removeram ref operacional anterior (`count=1`).

**Resultado:** partiu de **38 branches**; os primeiros 10 batches removeram **30 refs**, P11/P12 outras **2 refs**, e após criação/aposentadoria de branches operacionais o saldo conferido é **10 refs** (redução líquida de 28). Os arquivos e árvores que permanecem divergentes **não são elegíveis só por nome, idade ou PR encerrada**.

**Regra operacional:** abrir PR de manifesto SHA-pinned; aguardar testes e audit PASS; verificar HEAD `main`/PR, escopo e nenhuma PR aberta envolvendo as refs; merge por commit com head esperado; exigir `apply PASS/readback PASS`, consultar refs de novo e registrar recibos. O manifesto já consumido é histórico — **nunca executá-lo outra vez manualmente**. É aceitável reutilizar a única branch operacional após encerrar sua PR anterior, desde que o diff contra a `main` seja limitado ao lote novo.

## 4. Inventário das 10 branches — snapshot histórico, revalidado no bloco mais recente

| Branch | SHA em 26/10 | Situação e gate |
| --- | --- | --- |
| `main` | `ae9ac472ed4092effd12a3c41d5e3e560dc40f18` **antes da presente atualização** | Única branch permanente pretendida; reconsultar após este commit documental |
| `maintenance/ds-pr41-runtime-evidence-extract-20261026` | `9107ec1fce1feb90429c28729bc6c2e4014f1626` | Operacional, PR #82 mesclada; revalidar ancestralidade e elegibilidade antes de retirar em batch separado |
| `architecture/dom-css-consolidation-20261020` | `8e7d857528c9ea14fa45c3f58b57c07c7036bca0` | [#39 OPEN](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39); ~24 caminhos exclusivos: propostas, experimentos, workflows. Selecionar com proveniência e gates isolados, **não** merge geral |
| `docs/current-handover-20261024` | `28062602a4ddcd1bee090742fe2587fe3837175d` | [#51 OPEN](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51); ~221 caminhos só nesta branch, ~5,1 MB, majoritariamente 161 rastros de arquitetura e 60 de runtime; precisa classificação/proveniência, sem merge indiscriminado |
| `audit/access-confirmation-runtime-20261020` | `ae58f2199e9b3be5ba4ea313c86e7d26dd60ff37` | [#41 CLOSED sem merge](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/41); 7 blobs exclusivos importados por #78 e FIND-015 por #79; histórico restante divergente não comprovado como descartável |
| `audit/approved-contrast-runtime-20261021` | `e848e079071f4b2ce788e18a10a2284e6a24ff7a` | [#42 CLOSED sem merge](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/42); árvore datada, alterações em registro de decisões e evidências, conferir cobertura por conteúdo |
| `audit/auth-session-flow-2026-10-19` | `360d2e6d93d93ab74036149b518f22c01d57ecb0` | [#37 CLOSED sem merge](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/37); `evidence/runtime/auth-session-flow-2026-10-19.md` já tem **mesmo blob SHA na main**; outros registros divergem temporalmente |
| `docs/reconcile-approved-focus-record` | `430f4e1c7b376ae08e1788bd3aa365a32f2b76e2` | [#46 CLOSED sem merge](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/46); `PALETTE_CONFORMANCE.md` blob já igual à main; `decisions.json` antigo não deve substituir o atual |
| `docs/handover-reconcile-20261023` | `96093786ed8fb182c604182c37a42681cba8d6c9` | Sem PR associada no inventário; checkpoint 23/10 e detalhes OIDC/CI/ARC-03C precisam confronto com handovers mais recentes |
| `proposal/vis002-semantic-state-colors-2026-10-19` | `a924c2be0e8b75d90e4faa570a8a9f55f0b6f812` | [#23 MERGED](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/23), mas HEAD da branch **diferente** do head integrado; SVGs de candidatos/seleção verificados com blobs idênticos na main, `decisions.json` da branch é mais antigo |

**Nota importante sobre HOLD:** não há método autorizado de delete dos oito diverged heads pelo executor atual sem equivalência de árvore completa/ancestralidade e demais proteções. Uma tentativa anterior de criar arquivo/fluxo especial de arquivamento histórico foi **bloqueada por segurança**; não contornar bloqueio por chamada alterna. Retomar pelo caminho documental/integração explicitamente permitido, com verificação real do histórico relevante.

## 5. Reconciliações já materializadas — D04

### Fonte PR #51

A [extração DS #56](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/56) importou **sete documentos originais** de runtime, com SHAs listados no [ledger D04](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md), relacionados a produto #238, #241–#244, VIS-002C e fallback. O resto da PR #51 não foi reconciliado. Três WebP de alternativas de fallback permanecem na branch; não descrever como perdidos ou como integrados sem prova.

### Fonte PR #41

A [PR #78](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/78) importou **exatamente 7 blobs** da branch original com identidade SHA confirmada: 3 Markdown de runtime e 4 JPEG relativos a `/access/` e `/admin.html`. A [PR #79](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/79) adicionou FIND-015 em `FINDINGS_REGISTER.md` como **desvio de superfície contextual observado em 20/10/2026**, não problema atual nem homologação. A PR #41 foi encerrada **SEM MERGE integral** e manteve sua referência por cautela. O [guia atualizado por #81](BRANCH_HYGIENE_OPERATIONS.md) documenta todas essas ações.

**Limites:** snapshot do produto `1878ae1`, deploy `6ad6c3b51b6be05647167f94`. Havia diferença visual de estado de login entre abas, porém **não houve sequência controlada login/logout** nem diagnóstico causal da sessão. Nenhuma medição antiga comprova runtime atual. Não copiar `runtime-evidence.json` antigo sobre a main.

## 6. Riscos, inconsistências e critérios de parada

- `index.html` apresenta decisões parcialmente **duplicadas manualmente** em relação a `decisions.json`. Enquanto não existir projeção gerada e verificada, a página visual é demonstração, não fonte canônica; não fazer replace em massa sem testes.
- Muitos documentos do README são checkpoints **datados** (18–24/10), e relatórios antigos descrevem versões do produto anteriores. Sempre conferir commit/deploy explícitos, artefatos e conteúdo atual antes de atualizar status.
- #51 representa acúmulo documental de alta entropia. Extrair prioritariamente o que agrega ao roadmap atual; agrupar inventário por `evidence/architecture`, `evidence/runtime`, binários e arquivos modificados; nunca integrar dois documentos contraditórios como autoridade simultânea.
- #39 tem protótipos úteis e dois workflows exclusivos; não habilitar workflows experimentais automaticamente nem confundir **testes isolados** com integração real de componentes.
- Aumentar número de branches para fazer limpeza pode neutralizar a redução. Reutilizar branch operacional, fazer PR pequena e aposentar refs de manutenção **somente quando segura e não mais utilizada por PR aberta**.
- Preservar privacidade: não copiar tokens, emails ou contas de navegação autenticada; as capturas incorporadas de #41 são de telas anônimas.
- Não gerar Netlify Deploy Previews sem necessidade. Não inventar estados PASS nem resultados de dispositivos/CI. Nenhuma decisão visual nova foi autorizada neste ciclo.

## 7. Plano recomendado para o próximo chat (sem pedir novo questionário)

1. **Revalidar o inventário** de 10 refs/2 PRs abertas e SHA de `main`, checar que este handover foi integrado.
2. **Classificar PR #51 por grupo**, verificar blobs únicos e relevância atual; extrair seletivamente material importante em PRs pequenas com ledger D04. Priorizar binários que documentam opções realmente aprovadas; preservar o resto até classificação explícita.
3. **Classificar PR #39**, separar arquitetura ainda útil de documentação superada e experimentos sem gate; trazer apenas o que foi demonstrado e não converter proposal em homologação.
4. **Fechar 5 HOLDs documentais antigos** (#37, #42, #46, orphan de 23/10 e proposta #23 alterada) só quando toda informação útil estiver representada, ou histórica e seguramente preservada, em `main`. Revisar individualmente os campos `decisions.json` e os blobs, não fazer merge completo do arquivo antigo.
5. **Revisitar #41**: conteúdo exclusivo já incorporado; provar conservação segura do restante antes de qualquer delete físico.
6. **Rodar higiene somente para refs elegíveis** através do mecanismo `ops/branch-hygiene-batch.json` (máx. 3, SHA-pinned, PR audit PASS → push main apply PASS → readback). Não existe modo delete indiscriminado; parar quando o próximo gate não estiver demonstrado.
7. Atualizar o presente arquivo, o ledger e o README, com HEAD/PR/Actions verificados. A `main` deve continuar a única referência **permanente**, mesmo que branches temporárias e HOLDs sobrevivam durante a transição.

## 8. Referências de recuperação

- [Repositório DS / main](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/tree/main)
- [Guia de higiene + evidências de 12 lotes](BRANCH_HYGIENE_OPERATIONS.md)
- [D01–D04 aprovadas](APPROVALS_D01_D04_2026-10-26.md)
- [Ledger D04 de extrações por Git blob](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md)
- [PRs #64–#81](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pulls?q=is%3Apr+is%3Amerged+DS-HYG)
- [Handover do produto](https://github.com/EAKerber/MobiliPresenter2D/blob/main/docs/handoffs/HANDOVER-CURRENT-2026-10-26.md)
- [Registro de decisões](../decisions.json), [achados](../FINDINGS_REGISTER.md), [paleta](../PALETTE_CONFORMANCE.md), [mapa de aplicação](../DECISION_APPLICATION_MAP.md)

**GATE DE PUBLICAÇÃO DESTE HANDOVER:** verificar apenas que o documento e o ponteiro do README estão na `main`, preservam as fontes e não alteram decisões/tokens/workflows. Este artefato não constitui gate de runtime/produção do produto.

## Continuação D04 — triagem da PR #51 e preservação visual (26/10/2026)

Retomada auditada contra `main@9386d0fc847369bfd5080cb22859b25c90cda021`: 10 branches (1 main, 1 operacional, 8 HOLD), 2 PRs abertas (#39 e #51), [Actions #40435400023](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40435400023) **PASS** nessa main. A comparação do head `#51@28062602a4ddcd1bee090742fe2587fe3837175d` encontrou 221 caminhos exclusivos e 11 divergentes; 161 em arquitetura (153 ARC-13) e 60 em runtime (11 WebP). O diff histórico da PR conta 236 caminhos por usar uma base diferente.

Foi preparado um lote incremental D04-MEDIA-01 para preservar **3 WebP originais de comparação do fallback** já referenciados por `evidence/runtime/image-failure-fallback-options-2026-10-25.md`, junto com [classificação por grupos](DS_PR51_RESIDUAL_CLASSIFICATION_2026-10-26.md), [inventário SHA-pinned](DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json) e atualização do [ledger D04](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md). **Não considerar merge, CI ou readback concluídos sem verificação posterior da PR.** Após integração os 218 blobs exclusivos restantes da #51 devem continuar HOLD; próximas prioridades: 8 capturas da issue #226 com seus textos e triagem dos 153 ARC-13, sem substituir documentação vigente.

Nenhum gate de runtime do produto, homologação visual, exclusão de branch ou deploy foi executado nesta classificação. O repositório do produto permanece fora do escopo de escrita.

## Continuidade de higiene após a PR #83 — triagem dos HOLDs (26/10/2026)

A [PR #83](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/83) foi **MERGED** em `main@390bef5ded2fd3bc904de49e8130ebeb514671d4`. O readback independente confirmou os três WebP originais e seus blobs SHAs, o inventário e este handover; [Actions #40438390030](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40438390030) **PASS** de branch hygiene observacional no push. Nenhum batch de exclusão foi aplicado e continuam 10 refs/2 PRs abertas (#39 e #51). O arquivo `ops/branch-hygiene-batch.json` segue como P12 consumido.

O novo [diagnóstico de 7 HOLDs](DS_HOLD_BRANCH_DIFFERENCES_2026-10-26.md) e o [índice SHA](DS_HOLD_BRANCH_BLOBS_2026-10-26.json) mostram que a #39 mantém 24 caminhos exclusivos e 9 blobs modificados. **Os seis outros HOLDs antigos (#41, #42, #37, #46, orphan de 23/10 e #23) têm ZERO caminhos exclusivos**, porém somam 48 divergências de conteúdo em caminhos existentes, e seus HEADs continuam divergidos de `main`; portanto, **nenhum é SAFE_TO_DELETE**. A próxima etapa é comparação por campo com a autoridade atual, com provas de substituição/proveniência, não exclusão por coincidência de path. Os 218 arquivos exclusivos da #51 também permanecem HOLD.

## Continuidade D04 — ISSUE-226 e divergência temporal (26/10/2026)

Ao continuar a triagem da #51 após [PR #84](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/84), houve diferença de estado **dentro dos próprios documentos históricos**: matriz de 25/10 registra gate de zoom pendente, porém `issue226-real-zoom-user-confirmation-2026-10-25.md` declara o encerramento posterior da issue #226 por confirmação manual do usuário. Lote incremental preserva os **3 documentos e 8 capturas WebP originais** de `#51@28062602a4ddcd1bee090742fe2587fe3837175d`, com proveniência Git Blob em [DS_ISSUE226_BLOBS_2026-10-26.json](DS_ISSUE226_BLOBS_2026-10-26.json) e ledger D04. Não há rechecagem live do produto, nem inferência de estado atual da issue. Após o lote, os 207 outros caminhos exclusivos de #51 permanecem HOLD. **Nenhuma branch antiga pode ser excluída por este lote.**

## Continuação — auditoria por campo de decisões antigas (26/10/2026)

Após [PR #85](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/85), `main@f0417cb3eb243080207efc26b521ccee25e5a91f` passou no [Actions #40440191356](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40440191356); as evidências #226 importadas mantêm blobs exatos. [Auditoria do `decisions.json` dos cinco HOLDS que o modificaram](DS_HOLD_DECISIONS_FIELD_AUDIT_2026-10-26.md): todos têm os mesmos 22 IDs da main, sem decisões novas; divergências limitadas aos campos das decisões NAV-005, VIS-002, VIS-003 e EST-02 (na #46, só NAV-005). Campo completo e SHA em [JSON](DS_HOLD_DECISION_FIELDS_2026-10-26.json). Os textos/status antigos são preservados como snapshot, não restaurados na autoridade. **Este gate cobre somente decisões.json, não 48 diferenças documentais históricas nem ancestralidade das refs.** Nenhuma exclusão de branch foi autorizada por este diagnóstico.

## D04 — ponteiro de runtime histórico conciliado (26/10/2026)

[Reconciliação do índice runtime #41](DS_HOLD_RUNTIME_INDEX_RECONCILIATION_2026-10-26.md): `runtime-evidence.json` histórico contém `authFlowReview.menu.currentCrossPageObservation`, referência ausente no índice main, mas o alvo `evidence/runtime/private-menu-cross-tab-state-2026-10-20.md` está preservado na main, com blob SHA `d486214a482d7a0e6b78114746f1d476449a177f` desde PR #78. Não reintroduzir campo `current*` de observação antiga como estado atual. A comparação de outros índices antigos não mostrou outra chave nova, **mas valores/arrays e demais arquivos divergentes não passaram gate de equivalência integral**. #41 e demais HOLDS seguem preservados. PR #86 integrou a auditoria por campo de `decisions.json` em `main@c200aa83bd2fbf7f97696fe7f6693dd381162122`, [Actions #40440478801](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40440478801) PASS.

## Decisão de encerramento dos HOLDs e restrição de lote autorreferente (26/10/2026)

O usuário delegou a política de remoção; a [disposição técnica e de governança](DS_BRANCH_RETIREMENT_DECISIONS_2026-10-26.md) escolhe `main` única como alvo, conservação do histórico relevante, autoridade atual de `decisions.json` e uso exclusivo dos gates homologados. O preflight da branch operacional `@544ca507` confirmava ancestralidade, ausência de PR aberta e workflow referenciando a ref; **mas** um batch dentro da própria branch não consegue manter seu SHA pin depois do commit, então P13 não pode autopodar a branch. O candidato foi **retirado do diff antes de PR ou merge**; `ops/branch-hygiene-batch.json` na main continua sendo P12 consumido. Não houve exclusão, mutação da main ou mudança de política operacional. As 8 branches HOLD também permanecem bloqueadas por conteúdo ou ancestry; não usar rotas de arquivamento alternativas já rejeitadas.

## Lote D04 — ownership e ARC-13 crítico (27/10/2026; pré-merge)

Proposta seletiva de **9 blobs históricos originais**, sem adaptar conteúdo: três fontes de ownership DOM/CSS da #39 e seis rastreios ARC-13 de fronteira Admin/auth/persistência da #51. [Manifesto de blobs](DS_D04_OWNERSHIP_AND_ADMIN_BLOBS_2026-10-27.json), [critérios e limites](DS_D04_OWNERSHIP_AND_ADMIN_2026-10-27.md). Se gates, PR e readback aprovarem: exclusivos #39 24→21 e #51 207→201. O restante, incluindo dois workflows e código experimental da #39, permanece HOLD. **Não considerar integração ou validação de runtime confirmadas até recibo final.**

## D04 — aprovação de chave semântica e contrato Viewer recuperados (27/10/2026; pré-merge)

Quatro blobs exclusivos da PR #51 recuperam: (a) a **convenção** ARC-13 aprovada em 25/10 (camelCase, namespace e condição owner/consumer/parâmetros; exemplos e migração **não** aprovados); (b) histórico quantitativo de cobertura; (c) escolha do placeholder com descrição para falha da cena Viewer, sem homologação de release; (d) gate autenticado DS-05A, cujo último estado histórico ainda falhava Keyboard/Flow. Os dois suportes do Viewer (`pr242-viewer-scene-image-failure-implementation` e `pr241-public-image-failure-coverage`) já estão na main com mesmos blobs e não serão duplicados. [Nota](DS_D04_CONTRACT_PROVENANCE_2026-10-27.md) · [manifesto exato](DS_D04_CONTRACT_PROVENANCE_2026-10-27.json). PR #51 201→197 somente após merge/readback; demais HOLDs intactos.

## D04 — preservação da cobertura G0–G8 e DS-04 (27/10/2026; pré-merge)

Quatro documentos de #51 selecionados para manter a matriz de 8 rotas, famílias de regras CSS, reauditoria de 16 achados DS-04 da issue #208 e reconciliação do plano G0–G8 de 25–26/10. Arquivos copiados por SHA com [inventário](DS_D04_COVERAGE_BLOBS_2026-10-27.json) e [nota de limites](DS_D04_COVERAGE_RECONCILIATION_2026-10-27.md). Os dados de produto `5ccb2a8`/PRs são históricos, não status live. A importação de 4 originais prevê #51 197→193 exclusivos; só após readback. Revisar links de relatórios runtime ainda HOLD se essas matrizes forem usadas como documentos de navegação; não certificar cobertura só porque a matriz foi preservada.

## Readback após D04-91 — fechamento concorrente da PR #51 (27/10/2026)

PRs [#89](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/89), [#90](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/90) e [#91](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/91) foram integradas seletivamente, sem merge integral das fontes #39/#51. Confirmação em `main@6a4783b2f6217c689117b1183daceea00ef18f17` e [Actions #40443041873](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40443041873): **PASS** de branch hygiene observacional. Contagem por comparação SHA-pinned dos trees em 27/10: #39 tem **21** caminhos exclusivos restantes; #51, **193**.

**Evento concorrente importante:** `#51@28062602a4ddcd1bee090742fe2587fe3837175d` apareceu **CLOSED / merged=false** no GitHub em `2026-10-27T03:14:18Z`, evento de fechamento atribuído à conta `EAKerber`; o fechamento ocorreu fora do fluxo de merge de #91 e não deve ser tratado como integração, equivalência de conteúdo ou autorização para apagar o branch `docs/current-handover-20261024`. O head/source permanece preservado como HOLD em `ops/branch-dispositions.json`. A PR #39 permanece OPEN/DRAFT. Total de branches segue **10** (main, 1 operacional, 8 HOLDs), sem exclusões realizadas nesta rodada.

**Próximo risco prático:** 193 caminhos da #51 incluem 38 batches classificados ARC-13 (~1,78 MB), 38 outros ARC-13 (~2,42 MB), 69 consumer traces (~143 KB), 3 outros arquivos de arquitetura (15.817 B) e 45 notas runtime (~162 KB), somando **38 + 69 + 38 + 3 + 45 = 193**. Preservação seletiva orientada por contrato continua; não importar lotes volumosos apenas para atingir uma contagem cosmética de branches. O produto não foi inspecionado nesta rodada.

## D03/D04 — PR #39, 21 caminhos exclusivos triados (27/10/2026; pré-merge)

Extração planejada dos 12 documentos/ADRs datados de 20/10 e 7 experimentos isolados da #39, sem alterar conteúdo, mais **2 workflows históricos preservados como texto inerte** fora de `.github/workflows/`; todos referenciados por Git Blob SHA em [manifesto](DS_PR39_ALL_EXCLUSIVE_BLOBS_2026-10-27.json) e [classificação](DS_PR39_EXCLUSIVE_CLOSURE_2026-10-27.md). Nenhum source build, CSS, decisão, runtime, workflow ativo ou produto foi alterado. Depois de merge/readback, a #39 não terá mais documentação/experimento exclusivo por caminho, restando dois paths `.github/workflows` representados inertemente; **os 9 caminhos canônicos de versão divergente e a ancestralidade continuam HOLD**. Antes de fechar #39, comparar o conteúdo divergente; não declarar branch apta a delete só por paths preservados.

## D03 — PR #39 antiga reconciliada por arquivo (27/10/2026, antes de fechamento)

A [PR #93](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/93) integrou 21 blobs exclusivos da #39 (19 nos paths originais e 2 workflows em texto inerte) e teve [Actions #40443734932](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40443734932) PASS. Auditoria dos **9 caminhos canônicos divergentes**: [relatório](DS_PR39_CANONICAL_RECONCILIATION_2026-10-27.md) + [manifesto de source/main SHAs](DS_PR39_CANONICAL_FIELD_RECONCILIATION_2026-10-27.json). Todas as decisões (22 IDs) já existem na main, que carrega revisões posteriores; `runtime-evidence.json` da main inclui interações/followups do head original e informações adicionais; `visual-inventory.json` da main mapeia produto mais recente (1878ae1 vs 483ef2e). As seis fontes Markdown são snapshots de status anterior / link antigo, não atualizações a sobrescrever. **A conclusão autoriza fechar #39 como PR substituída após gates desta reconciliação, mas NÃO excluir a branch histórica**, cuja head diverge da main. Não atualizar `ops/branch-dispositions.json` para SAFE_TO_DELETE.

## D03 fechamento #39 e D04 recorte ARC-13 (27/10/2026; pré-merge do lote)

A PR [#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) foi efetivamente **CLOSED / merged=false** por esta rodada após [#93](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/93) (21 fontes únicas preservadas com workflows inertes) e [#94](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/94) (9 versões canônicas reconciliadas, [Actions #40444036554](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40444036554) PASS). Comentário de disposição registrado na #39; sua branch ainda é HOLD, não elegível a delete. PR #51 também está CLOSED/not-merged, ainda HOLD.

Lote ARC-13 proposto: seis blobs SHA-exact de #51, cobrindo publicação Admin, validação de preços, navegação privada, técnica de teclado **não localizável**, validação Admin e carrossel Configurador. Dois arquivos são sugestões de chave **não canônicas**, quatro são inventários classificados; nenhuma mudança ao índice ARC-13, app, decisões ou workflows. [Relatório](DS_ARC13_CONTRACT_REVIEW_2026-10-27.md), [manifesto](DS_ARC13_CONTRACT_REVIEW_2026-10-27.json). Após merge e readback, #51 exclusivos 193→187; gate depende do commit, sem exclusão de ref.
