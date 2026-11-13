# HANDOVER CANÔNICO — MobiliPresenter2D Design System

**Snapshot histórico:** 26/10/2026, fuso `America/Sao_Paulo`.  
**Destino:** recuperação histórica do trabalho daquele checkpoint.  
**Prioridade registrada em 26/10:** estabilizar/reconciliar branches do Design System e não editar o produto até nova orientação. Essa restrição foi superada pela instrução explícita deste chat para continuar o plano de arquitetura nos dois repositórios.  
**Retomada atual (12/11/2026):** o escopo solicitado abrange a implementação integral do plano arquitetural ARC-01…ARC-16 e V0–V6, mantendo os gates G0–G8 e DS-05A como trilhas de validação relacionadas. Consulte o [checkpoint G0–G8](../evidence/architecture/architecture-g0-g8-current-checkpoint-2026-11-09.md), a [recaptura CSSOM local do Admin](../evidence/architecture/g2-admin-initial-state-labels-cssom-2026-11-12.md) e a reconciliação do plano geral ao final deste handover. A execução segue o método Git do produto, mantém os documentos correntes e observa os soft caps de refs. O Design System tem meta/soft cap de 2 refs; o produto tem soft cap de 5 durante trabalho ativo e meta de 2 quando estável (`main` + `development`). Ao chegar a 5, revisar se um hard cap é útil; 2 e 5 não são regras rígidas nem autorização para exclusão por contagem. Há autorização para trabalho de arquitetura e preview hospedado moderado; não há autorização para deploy de produção ou operação de banco. O usuário também dispensou o runtime bootstrap neste chat. Revalidar HEADs e PRs na API antes de cada ação.

## Verificação posterior à PR #82 — snapshot de retomada (26/10/2026, São Paulo)

**SHA de `main` confirmado antes desta atualização documental:** `ae9ac472ed4092effd12a3c41d5e3e560dc40f18`, [PR #82](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/82) **MERGED**. A leitura independente de GitHub encontrou **10 branches** (1 `main`, 1 operacional e 8 HOLDS), apenas **duas PRs abertas** ([#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39), [#51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51)) e observação sem escrita da [Actions #40428162828](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40428162828) **PASS** no mesmo SHA.

**Branch operacional ativa:** `maintenance/ds-pr41-runtime-evidence-extract-20261026@9107ec1fce1feb90429c28729bc6c2e4014f1626` (sem PR aberta em seu head; **não presumir seguro apagar** sem gate completo). Os oito HOLDS estão enumerados na seção 4 e registrados em `ops/branch-dispositions.json`; **não excluir por ser branch antiga ou PR encerrada**. `ops/branch-hygiene-batch.json` conserva o lote P12 já consumido, **não deve ser reaplicado**. O executor ativo é o portado do produto (PR #64); o legado foi desativado.

**Verificações materiais recentes:** PR [#80](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/80) aplicou P12 com readback; PR [#81](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/81) atualizou o procedimento; PR [#82](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/82) publicou este handover e seu ponteiro no README. A extração exata de sete blobs de #41 está na PR #78, o FIND-015 datado na #79, e a #41 ficou **CLOSED sem merge** e **branch HOLD**. A PR #51 ainda contém numerosos arquivos exclusivos (especialmente arquitetura/runtime) e a #39 experimentos/propostas não homologados. A próxima ação é **classificação e extração seletiva com proveniência**, não apagar em massa.

Este bloco registra somente **documentação e leitura Git/Actions**. Não comprova conformidade funcional de login, contraste, produto ou publicação. O commit produzido por esta própria atualização virá depois do SHA de snapshot acima; obter o SHA efetivo na API ao retomar.

## 0. Instruções de recuperação do snapshot de 26/10

1. Consultar o SHA de `main`, inventário completo de branches, PRs abertas/fechadas relevantes e Actions no repositório [Design System](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem).
2. Ler este arquivo, [guia operacional de higiene](BRANCH_HYGIENE_OPERATIONS.md), [D01–D04 homologadas](APPROVALS_D01_D04_2026-10-26.md), [ledger de extração D04](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md), `decisions.json`, os manifests `dist/` e `FINDINGS_REGISTER.md`.
3. Naquele snapshot, o repositório do produto era tratado apenas como referência e a edição estava fora do escopo. A autorização posterior de 09/11 permite trabalho de arquitetura no produto. A autorização posterior de 10/11 inclui um preview hospedado moderado; deploy de produção e banco continuam sem autorização.
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

## Checkpoint validado 27/10 — #39/#51 encerradas, 187 exclusivos ARC-13/runtime pendentes

- [PR #93](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/93) preservou os **21 blobs exclusivos** de #39 sem ativar os dois workflows; [#94](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/94) reconciliou **nove** arquivos canônicos mais antigos. O comentário de encerramento da [#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) explica D03; **CLOSED / merged=false**, branch `architecture/dom-css-consolidation-20261020@8e7d857528c9ea14fa45c3f58b57c07c7036bca0` continua HOLD, sem delete.
- [PR #95](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/95) importou por SHA exata seis fontes ARC-13 (176.171 bytes) com sua distinção `classified` vs `proposal`: arquivo técnico de teclado 35/35 **não localizáveis** como controle negativo; 39 propostas transacionais de Admin, 26 propostas de carrossel, 27 pricing, 29 private-nav, 72 validation. [Relatório](DS_ARC13_CONTRACT_REVIEW_2026-10-27.md) · [manifesto](DS_ARC13_CONTRACT_REVIEW_2026-10-27.json).
- Readback de `main@2d869a9c494313008930bd2e6ee8594262bd985d`: [Actions #40444401507](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40444401507) **PASS**. **0 PRs abertas; 10 branches no total = main + 1 operacional + 8 HOLDs**. #51 CLOSED/not merged desde 03:14:18Z; a ref `docs/current-handover-20261024@28062602a4ddcd1bee090742fe2587fe3837175d` continua HOLD.
- Inventário residual #51 por comparação atual de árvores: **187 caminhos exclusivos**, sendo **34** lotes ARC-13 `classified`, **36** outros ARC-13/índices/propostas, **69** rastreios de consumer, **3** propostas VIS-002 datadas e **45** notas runtime. Não declarar "zero legado" nem compactar toda a fonte sem gate.

**Próximo gate recomendado**: começar pela relação dos índices ARC-13 de 24/10 com os 34 batches e 69 rastreios restantes; a leitura textual integral do mestre `arc13-runtime-js-candidates-main-2026-10-24.json` (Git Blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`, 1.335.718 B) não veio completa via conector e permanece **não validada**, logo não se deve declarar que o mestre substitui os batches. Como passo paralelo de risco menor, selecionar notas runtime que documentem achados de acessibilidade/segurança com source head e gatilhos verificáveis. A prova da política de branch hygiene continua separada: **nenhum HOLD divergente fica elegível apenas por PR fechada ou por ausência de caminhos exclusivos**, e o caso da última branch operacional não foi resolvido pelo executor SHA-pinned. Nenhuma operação no repositório do produto, preview ou deploy nesta rodada.

## ARC-13 — índices gigantes lidos integralmente, 36 lotes cruzados (27/10/2026; PR pendente de gate)

Foi superado o bloqueio de leitura do mestre `arc13-runtime-js-candidates-main-2026-10-24.json` (SHA `1954dfd9a4fe6194812b4fd336281eed39f64ecf`, 2.181 ocorrências) por leitura direta do Git Blob. O mestre HTML separado (SHA `0d748a7cfbbdc28d3476ef200bae5e05fa7dac9c`) contém 480 ocorrências. **27/29** batches JS e **7/7** HTML coincidiram exatamente por multiconjunto de `file,line,currentText,classification`. Exceções: técnico Viewer/Configurator (30 ocorrências lexicais versus 33 entradas semânticas e 41 localizações) e JS de Access/Tema (23 lexicais versus 27 entradas semânticas); transformações de templates e linhas divergentes impedem substituição mecânica. [Auditoria com grupos/SHA](DS_ARC13_MASTER_BATCH_AUDIT_2026-10-27.json) · [relatório](DS_ARC13_MASTER_BATCH_RECONCILIATION_2026-10-27.md). Proposta preservar índices e ambas exceções por blob exato, sem alterar catálogo nem indexar como aprovado. Após merge #51 residuais 187→183. **A correspondência de quatro campos não equivale à conservação de owner/consumer/params dos batches não importados**. PRs #39/#51 continuam encerradas sem merge, heads divergidos HOLD, zero exclusões.

## ARC-13 D04 — preservação integral do contexto dos 32 lotes restantes (27/10/2026; pré-merge)

Após [auditoria de 36 batches](DS_ARC13_MASTER_BATCH_AUDIT_2026-10-27.json), os **30 batches classificados ligados ao índice** ainda exclusivos foram lidos e comparados além da tupla básica, encontrando hashes de fonte, notas, consumidores/owners e parâmetros que o índice não reproduz integralmente. Dois auxiliares independentes (revisão de 3 scripts inline e 2 arquivos grandes de dados) são controles negativos fora dos índices. Seleção para transportar 32 blobs exatos com [proveniência](DS_ARC13_CLASSIFIED_CONTEXT_BLOBS_2026-10-27.json) e [interpretação](DS_ARC13_CLASSIFIED_CONTEXT_RECONCILIATION_2026-10-27.md), sem promover chaves, alterar fonte do produto ou ativar workflows. Após merge/readback esperado: #51 183→151 exclusivos; 0 lotes `arc13-classified-*` exclusivos. Histórico das branches ainda HOLD; nenhum delete.

## D04 — 69 rastreios ARC-13 por consumer e dois mapas auxiliares (27/10/2026; pré-merge)

Foco em preservar escopo/owner/parametrização não recuperável pela lista de ocorrências: **69 consumer-trace MDs** (Admin e Configurador) com Git Blob SHA exato e **2 mapas históricos** (`arc13-unkeyed-consumer-scope-map` e `arc13-unkeyed-consumer-context-map`). [Manifesto de 71 objetos](DS_ARC13_CONSUMER_TRACE_BLOBS_2026-10-27.json) · [interpretação e amostras](DS_ARC13_CONSUMER_TRACE_PRESERVATION_2026-10-27.md). Classificar como leitura estática do produto `5ccb2a8`; nenhuma chave final, runtime ou tradução homologados. Após merge/readback esperado, #51 151→80 exclusivos (32 outras fontes ARC13, 3 VIS-002, 45 runtime). Nenhuma branch excluída. O gate de higiene continua separado.

## D04 — últimos 35 registros de arquitetura da #51 (27/10/2026, pré-merge)

Seleção de **32 objetos ARC-13** (propostas, auditoria cruzada, residuais e reclassificações) e **3 VIS-002** contextualizados, por Git Blob SHA exato e sem ativar alteração visual. [Manifesto](DS_D04_ARCHITECTURE_CANDIDATES_BLOBS_2026-10-27.json) · [política e limites](DS_D04_ARCHITECTURE_CANDIDATES_2026-10-27.md). Atenção: a evidência VIS-002 de keylines do hotspot só registra autorização para **preview da PR #242**, não Production. Propostas ARC13 seguem candidatas; convenção aprovada não é aprovação de string, catálogo ou owner. Após merge/readback: #51 80→45 exclusivos (apenas notas runtime). Não autoriza exclusão das refs HOLD.

## D04 — últimos 45 relatórios runtime da #51 (27/10/2026; pré-merge)

Seleção de **45 arquivos Markdown runtime** datados (24–26/10) com Git Blobs idênticos da PR #51. [Inventário/SHAs](DS_D04_RUNTIME_EVIDENCE_BLOBS_2026-10-27.json) e [nota sobre limites e status datado](DS_D04_RUNTIME_EVIDENCE_PRESERVATION_2026-10-27.md). Amostras incluem DS-05A auth fixture, Issue #224, NAV-005, PRs #242 e contraste VIS-002; nenhum status histórico vira verdade atual automaticamente. Se merge/readback passar, #51 tem **0 paths exclusivos** em relação à main, mas ainda contém **11 blobs canônicos modificados** e histórico divergido; fica HOLD, não `SAFE_TO_DELETE`. As outras sete branches HOLD e a branch operacional permanecem, sem exclusão.

## D04 — 11 blobs canônicos históricos da #51 arquivados inertemente (27/10/2026; pré-merge)

A [PR #101](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/101) resultou em **0 paths exclusivos** frente a `docs/current-handover-20261024@28062602a4ddcd1bee090742fe2587fe3837175d`, mas restam 11 versões alteradas no mesmo path. O lote atual propõe preservar **os 11 Git Blobs antigos exatos** (2 workflows, 7 docs/handover, 2 índices) em `docs/historical-branch-blobs/pr51/**.txt` sem sobrescrever as versões da main, com [manifesto](DS_D04_PR51_OLD_CANONICAL_BLOBS_2026-10-27.json) e [explicação](DS_D04_PR51_CANONICAL_ARCHIVE_2026-10-27.md). Após merge a **cobertura de conteúdo do head** estará completa; NÃO a retenção do histórico Git, cujo gate de exclusão continua bloqueado. Fonte #51 CLOSED/not-merged e demais refs HOLD continuam sob proteção.

## D04 — pool de blobs dos sete heads HOLD restantes (27/10/2026; pré-merge)

Auditoria comparou sete HEADs divergentes com a árvore atual: **54 instâncias de blobs ausentes do tree da main**, **45 SHAs distintos** após deduplicar por identidade. Proposta de preservação de cada SHA em `docs/historical-branch-blobs/hold-pool/<sha>.txt` com [manifesto de origem por branch](DS_HOLD_HEAD_BLOB_POOL_2026-10-27.json) e [limites](DS_HOLD_HEAD_BLOB_COVERAGE_2026-10-27.md). Junto à PR #102 para a #51, a cobertura de **conteúdo dos oito HEADs HOLD** deverá ficar completa após readback; NÃO preserva cadeia histórica de commits nem torna as refs elegíveis ao executor de exclusão. Proibido afirmar SAFE_TO_DELETE sem gate. Branch count esperado ainda 10.

## Readback final D04 — conteúdo dos 8 HEADs HOLD 100% alcançável; história Git ainda divergente (27/10/2026)

Conferência em `main@18e50981c322e153819d7cb1ce80139d8f71c4d9`, [Actions #40448667631](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40448667631) PASS. Após [PR #102](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/102) (11 blobs antigos da #51 inertemente) e [PR #103](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/103) (45 blobs distintos de outras 7 refs, 54 usos), **0 arquivos-blobs do HEAD dos oito HOLDs ficaram sem cópia por SHA na tree da main**. [Tabela de 8 heads/SHAs e limites](DS_HOLD_FINAL_HEAD_CONTENT_READBACK_2026-10-27.json) · [relatório de riscos remanescentes](DS_HOLD_FINAL_RETIREMENT_GATES_2026-10-27.md). A comparação de Git commits ainda marca os oito heads como divergidos, alguns com longo histórico exclusivo (ex.: 814 commits no head da #51); preservação do HEAD **não** preserva versões intermediárias. A branch operacional é ancestral, mas manifesta a armadilha de se solicitar a própria exclusão em PR SHA-pinned. **0 PRs abertas; 10 refs; nenhuma exclusão**. Próximo objetivo: retenção verificável do DAG histórico e terminalidade do executor, então lotes curtos; não simular merge `ours` nem relaxar gates silenciosamente. A higiene do produto pode ser retomada separadamente após confirmação explícita do alvo nesse chat.

## DAG histórico — pré-gate de retenção não destrutiva (27/10/2026)

Após #99–#104, os **8 HEADs HOLD têm 100% dos blobs atuais alcançáveis na main**; contudo, os DAGs intermediários ainda não o são. Um estudo de tags leves com SHAs originais está documentado em [DS_DAG_TAG_RETENTION_PROTOCOL_2026-10-27.md](DS_DAG_TAG_RETENTION_PROTOCOL_2026-10-27.md) e [manifesto de 8 heads](DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json); auditor puro de readback em `tools/branch_hygiene_retention_audit.py` com testes negativos. GitHub apresentou **0 tags e 0 rulesets**, então **nenhuma ref foi arquivada nem removida**. Não promover `terminalBranches`, não modificar `ops/branch-hygiene-batch.json` e não fazer merge artificial `ours`. A tag proposta só seria suficiente para deleção sob proteção comprovada e executor revisado em PR separada. Problema terminal da branch operacional igualmente pendente de gate. `main` no início do estudo: `8d50d9167f1e85616f7e2f00389a534e1d879888`; 10 branches, 0 PRs abertas. 

## Readback pós-PR #105 — auditor de retenção DAG ainda sem tags (27/10/2026)

A [PR #105](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/105) foi integrada em `main@166e1bff22d3624a4d6dcc20c21541bee30fd635`; [Actions #40452100882](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40452100882) e [#40452100814](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40452100814) passaram no HEAD da PR, incluindo os testes negativos do novo auditor, e [push/main #40452178002](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40452178002) terminou **PASS**. O repositório segue com **10 branches, 0 PRs abertas, 0 tags, 0 rulesets retornados** pela API. Portanto **nenhum DAG divergente está arquivado por tags ainda**. [Protocolo](DS_DAG_TAG_RETENTION_PROTOCOL_2026-10-27.md), [manifesto de SHA fixo e status PROPOSAL_ONLY](DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json), `tools/branch_hygiene_retention_audit.py` (read-only). **Próximo gate dependente do dono do repositório:** configurar e confirmar proteção de atualização/exclusão do padrão de tag `ds-history/2026-10-27/*`; só depois rever autorização e executar criação de tags e check de preservação DAG, em PR e lote distintos. Nada em `ops/branch-dispositions.json` ou batch de exclusão foi alterado. A última branch operacional também continua sem mecanismo terminal de exclusão validado; não forçar self-delete. Nenhuma ref eliminada.

## Handover de recuperação autônomo — 27/10/2026, após PR #106 (antes do merge da presente PR)

Documento de retomada autocontido: [HANDOVER_DAG_HYGIENE_2026-10-27.md](HANDOVER_DAG_HYGIENE_2026-10-27.md). Readback feito em `main@14596cbd489c16cb23406d9a5f407b406185916f`, [Actions #40452414779](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40452414779) **PASS**, 10 branches, 0 PRs abertas, 0 rulesets. O readback anterior #106 registrou também 0 tags. #99–#104 preservaram todos os Git Blobs dos oito HEADs HOLD por SHA, mas não o DAG intermediário; #105–#106 apenas preparam/registram gate de tags sem executá-lo. Decisão operacional: **não excluir branch**, não alterar manifests de exclusão, não criar tags antes de proteção ativa validada. Próximo ato depende de configuração pelo dono do repo da proteção de `ds-history/2026-10-27/*`; depois criar tags em fase separada, validar readback e só então estudar gate destrutivo.


## Checkpoint 27/10/2026 — DAG preservado por oito tags protegidas (pós-#111)

Verificado no GitHub em `main@a2621721a5fad8e453748374d6fc2fc50d9c5fd1`: ruleset **#25953910** ativa para `refs/tags/ds-history/2026-10-27/*` bloqueia updates/deletes, sem bypass; **8/8 tags leves apontam por SHA exato a commits dos oito HEADs históricos**, sem tags adicionais; 10 branches inalteradas, 0 PRs abertas, **0 branch deletes**. [GitHub Actions #40500797873](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40500797873) **PASS** (recibo `ds-dag-tag-retention-40500797873`, artifact `12732920974`); hygiene [#40500797879](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40500797879) **PASS**. Implementação não destrutiva #109–#111. Agora o DAG histórico tem refs protegidas além das branches; a autoridade de `decisions.json@main` não mudou. **A retenção não autoriza exclusão automática:** o executor de branch-hygiene ainda não tem modo homologado `PROTECTED_ARCHIVE_TAG_EXACT_COMMIT`, `ops/branch-dispositions.json` mantém oito HOLDs e batch P12 está consumido. Implementar/revisar o gate separadamente antes de qualquer lote de remoção. Ver [handover de DAG](HANDOVER_DAG_HYGIENE_2026-10-27.md).


## Higiene DAG P13–P16 — 8 HOLDs retirados (27/10/2026; pré-PR terminal)

As PRs [#114](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/114) / P13 [40511965874](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40511965874), [#115](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/115) / P14 [40512535633](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40512535633), [#116](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/116) / P15 [40513316115](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40513316115) e [#117](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/117) / P16 [40514015814](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40514015814) tiveram **apply PASS e readback**, removendo os oito HEADs divergentes sem perder os oito DAGs arquivados por tags protegidas. Snapshot pré-terminal `main@14549a411c278b476ea1590d1a5c9e48ced8474d`: **duas branches** (main + única operacional), **8 tags**, ruleset #25953910 ativa, `preserveBranches=[]`, `terminalBranches` contém oito registros históricos. Batch P16 está consumido, não reaplicar. A [PR #118](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/118) implementa gate distinto de exclusão da branch operacional pelo **segundo pai verdadeiro do merge** + identidade da PR/head/ref remotos/lease; **não declarar a retirada efetivada sem Actions PASS e readback**. Ver [handover detalhado](HANDOVER_DAG_HYGIENE_2026-10-27.md).


## Design System: higiene de branches concluída (27/10/2026, pós-PR #118)

**Estado confirmado:** repositório possui **somente a branch `main`**, **0 PRs abertas**, **8/8 tags históricas leves protegidas** em `ds-history/2026-10-27/*` (ruleset #25953910 Active/sem bypass). Os 8 HOLDs antigos foram retirados pelos lotes auditados P13–P16 (#114–#117), com [applies #40511965874](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40511965874), [#40512535633](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40512535633), [#40513316115](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40513316115) e [#40514015814](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40514015814) PASS. A branch operacional foi eliminada pela [PR #118](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/118), gate de segundo pai `e08ef913bf673702bacdf96a06e0b7e97e609c6e` do merge commit real `d22f87b803b07c1995f11d61b6c41e3fefe5cdb5`, [Actions #40515276768](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40515276768) **PASS/readback**, recibo artifact `12738896985`; [Actions observacional #40515276681](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40515276681) PASS. Scripts P16 e terminal são **consumidos, não reexecutar**; `terminalBranches` é ledger histórico, não lista de refs vivas. Nenhuma alteração/deploy no repo de produto. [Handover detalhado](HANDOVER_DAG_HYGIENE_2026-10-27.md) contém os gates e links. Este checkpoint foi escrito diretamente na `main` para não recriar branches; reler o HEAD ao retomar.


## Retomada desta conversa — atualização 2026-11-10

A fotografia detalhada das fases G0–G8 está em [checkpoint atual](../evidence/architecture/architecture-g0-g8-current-checkpoint-2026-11-09.md). Os registros datados anteriores permanecem como histórico; este adendo é o estado operacional mais recente verificado.

- **Design System:** `main@79db735d6f05177b0c406e383d35832f3d72fdef`; PR #119 segue draft na branch `docs/architecture-status-20261109`, head `f100a815606646460898f58da426730c68a2631d` no início desta atualização. Há 2 branches remotas e 1 PR; o limite brando DS≤2 é respeitado. Nenhuma branch foi excluída.
- **Produto:** `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`; 3 branches e PR draft #269, head `6195e90c012a45a7abf1b8db6de220be03dc9fb4`. Limite brando produto≤5 respeitado. Issues #208/#216/#218/#232 permanecem abertas; #217/#224/#226 fechadas.
- No head atual de #269, **13/15 checks passaram; dois foram skipped**. NAV-005 local-only passou 124 cenários. O job de layout responsivo, que falhou uma vez no WebKit ao voltar de 701 px para 1366 px, passou na única repetição isolada com 24/24; não se identificou causa raiz para a primeira falha. Public routing passou na parte estática, mas não executou browser remoto enquanto o PR está draft. Nenhum Deploy Preview da branch foi encontrado no Netlify; nenhum deploy manual foi realizado.
- O usuário autorizou um preview em moderação. Ele permanece pendente por não haver preview automático do PR draft. O PR continua draft; não foi alterado para pronto para revisão, não houve merge nem publicação.
- #216 continua aberta, mas o subgate da regra vencedora avançou: Chrome DevTools capturou os vencedores nos três seletores originais × light/dark em `main@221b54b`, e a razão CSSOM recalculada no viewport 766×608 coincidiu com o recibo anterior. O procedimento local `file://`, as folhas injetadas e limites estão em [evidence/architecture/vis002c-cascade-winner-trace-2026-11-10.md](../evidence/architecture/vis002c-cascade-winner-trace-2026-11-10.md). Não é preview nem prova do CDN; `.study-band .eyebrow`, os cinco consumidores adicionais, `/config/` e #208 permanecem fora/abertos. A tentativa do coletor Playwright ainda falha antes de navegar pelo perfil temporário do Edge (`-5`).
- UX-04 continua sem Actions no SHA exato de `development`; o workflow de dispatch segue ausente da branch padrão `main`. Assim G1 permanece parcial, G2 em andamento, G3 parcial, G4/G6 em HOLD, G5 parcial/HOLD e G7/G8 pendentes. Nenhuma fase do plano geral pode ser considerada concluída por estes resultados.
- Próximos passos: obter um único preview hospedado para revisar a candidata #269; terminar o crosswalk G2 para #208/#216, `/config/` e DS-05A; destravar o gate UX-04 no runner Linux/Node 22; continuar G3–G7 com ownership e evidência por domínio antes de qualquer migração compartilhada. Não promover para release sem revisão e validação integrada.

## Retomada desta conversa — atualização de evidência 2026-11-10 (BRT)

Esta atualização substitui os HEADs e limites da seção de retomada anterior; consulte o checkpoint G0–G8 acima para o estado por fase.

- **Design System:** branch `docs/architecture-status-20261109`, PR #119 draft. O snapshot inicial desta atualização foi `fc5770fe7f917cc4375ca5cfe524fac996d78ab3`; após o commit documental, confirmar o head pelo readback da API. O inventário remoto observado permanece 2 branches/1 PR, dentro do soft cap DS≤2.
- **Produto:** `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`; 3 branches e PR #269 draft, head `6195e90c012a45a7abf1b8db6de220be03dc9fb4`. Soft cap produto≤5 respeitado; não há branch remota a excluir apenas para cumprir o limite.
- **G1:** a candidata #269 tem 13/15 checks em success, 2 skipped; NAV-005 local-only passou 124 cenários, e a repetição focada do job de layout passou 24/24. A validação hospedada segue pendente: a tentativa de transição temporária para ready não gerou Deploy Preview e foi revertida para draft. Nenhum deploy manual, merge ou publicação ocorreu.
- **G2/G3:** o trace local foi ampliado aos dez seletores v0.3 (14 elementos) e à exceção `.study-band .eyebrow`, nas três rotas públicas, em light/dark. A inspeção por Chrome DevTools confirmou os winners e o DOM calculado. A fonte local `file://` e a carga direta das folhas limitam a inferência; não provaram HTTP/CDN, aceitação visual, comportamento global, nem ownership além desses contextos.
- **Pendências de arquitetura:** #216 permanece aberta; #208, 98 pares UNCERTAIN de `/config/` e DS-05A permanecem separados e em aberto/HOLD. G3 não fecha ownership amplo; G4/G6 continuam HOLD, G5 parcial/HOLD, G7 pendente e G8 não iniciado como release.
- **Próxima ação de maior retorno:** atualizar este trace/checkpoint/handover como um lote documental, mantendo uma só branch DS; depois continuar a evidência de G2 para #208, `/config/` e DS-05A. Gerar um preview hospedado para a candidata #269 assim que a via de Preview estiver acessível; agrupar correções relacionadas antes de outra rodada, sem tratar validação local como substituta.



## Retomada desta conversa — atualização de evidência 2026-11-11 (BRT)

Esta atualização substitui os estados operacionais anteriores de G1/G2 e confirma o acesso aos Previews pelo navegador do ChatGPT. A evidência não fecha critérios de release nem autoriza merge ou publicação.

- **Design System:** PR #119 permanece draft em `docs/architecture-status-20261109`, head `bc6b4764612e5c4ea6317eaf035d371b89089b3e` antes desta atualização; 2 branches e 1 PR aberta, dentro do limite DS≤2.
- **Produto:** `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`; 5 branches, dentro do limite produto≤5. #269 permanece draft no head `19bbf9d25e71c5fa94abc3ee12baff52747ec54c`; #271 está aberta e não draft no head `6030eec03e8dad0c91672744b59b9c63080ce835`. #270 foi encerrada sem merge como supersedida e sua branch permanece. Nenhuma branch foi removida.
- **G1 / #269:** 12 verificações de Actions no SHA atual terminaram em success, incluindo NAV-005 local e o gate de fluxo responsivo. O Deploy Preview `6af3e1508734d4fdfd61a482` está ready em [deploy-preview-269](https://deploy-preview-269--mobilipresenter2d.netlify.app/how-it-works/). Pelo navegador do ChatGPT, a página pública foi revisada em desktop e a 390 px; o cabeçalho e o menu aberto mostraram os links e CTA sem sobreposição visível. Isso é uma inspeção visual pontual, não fecha os critérios de #218 para toque, zoom, foco, larguras/dispositivos ou Safari/iPad.
- **G2 / #271:** 8 verificações de Actions no SHA atual terminaram em success. O Deploy Preview `6af3e14b24bd296921873555` está ready; a entrada `/config/` redirecionou para `/access/` e informou que não havia token válido. Não foi fornecido acesso válido e a barreira não foi contornada. Assim, o Configurador/Viewer internos e o fluxo autenticado ainda não tiveram revisão visual hospedada. #208 permanece aberta; o Preview não substitui a validação local nem fecha os demais critérios.
- **UX-04:** o último run verde segue no SHA antigo `c7c2822d5b651ae0bcfcf0ac28c66cb61b645e98`; `development` continua em `1a69ff76a5f36e3245a288773bb409aa662e4e62`. O workflow tem `workflow_dispatch` em development, mas o arquivo não existe em `main`, por isso o Actions UI não oferece disparo para o SHA atual. G1 continua parcial até haver evidência Linux/Node 22 no SHA atual e conclusão de #218.
- **G2 e fases seguintes:** #216 e #208 continuam abertas; 98 pares de `/config/` seguem UNCERTAIN e DS-05A continua incompleto/HOLD. G3 permanece parcial, G4/G6 em HOLD, G5 parcial/HOLD, G7 pendente e G8 não iniciado como release. Sem merge, deploy de produção ou operação de banco.

Próximo passo: manter os dois PRs abertos para revisão apropriada; avançar o gate UX-04 no SHA atual e a evidência acessível de #208/#216 sem remover a barreira do Configurador. Agrupar correções relacionadas antes de outro ciclo de Preview.


## Retomada desta conversa — avanço G3 e sessão de Preview (2026-11-11, BRT)

- **G3:** foi adicionada uma auditoria inicial no [inventário de riscos/ownership CSS](architecture/CSS-OWNERSHIP-RISKS-2026-10-20.md), pinada em `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. Ela classifica `.visually-hidden` como candidato de contrato igual com ganho ainda não demonstrado; `.eyebrow` e `.button` como variantes/homônimos contextuais; `.scene-hotspot` como indeterminado/alto risco; e `.site-header` como shell público com variante de página, ainda dependente de G1/#218. Não autoriza extração G4.
- **G4:** permanece HOLD. O candidato `.visually-hidden` aparece em bundles diferentes e não co-carregados; mover a regra para `ui-theme.css` pode aumentar bytes em rotas sem consumidor. Falta medir bytes/cache, CSSOM, árvore acessível e impressão.
- **Admin/preview:** o usuário informou login administrativo. No Preview #269, a rota `/admin` abriu o editor autenticado. A rota `/config/` abriu o shell, mas depois exibiu “Não foi possível validar a configuração publicada. O configurador está temporariamente indisponível.” Portanto não houve revisão visual válida de módulos/estados nesse Preview. No host #271, `/admin` ainda mostrou formulário de login e `/config/` redirecionou para `/access/` sem token válido; a sessão do host #269 não deu acesso ao #271. Nenhuma credencial foi copiada e nenhum dado/configuração foi alterado.
- **Estado:** PR #269 continua draft; PR #271 continua aberta sem draft; PR #119 continua draft. As branches permanecem no limite 5/5 produto e 2/2 Design System. G0 segue contínuo, G1/G2 parciais/em andamento e G3 parcial; G4–G8 sem mudança de status.
- **Próximo avanço independente:** continuar a matriz G3 no PR #119 e a reconciliação local DS-05A; para revisar o head G2 #271 visualmente, a sessão deve estar autenticada nesse mesmo host e o configurador precisa ter uma configuração publicada validável. Não criar branches extras nem considerar erros de carregamento como validação de contraste.


## Retomada desta conversa — revisão G2 autenticada do Preview #271 (2026-11-11, BRT)

O usuário informou login administrativo e orientou entrar pelo Admin. Com essa sessão no host exato do Preview #271 (`deploy-preview-271--mobilipresenter2d.netlify.app`), foi possível abrir o Viewer e a página de gerenciamento:

- **Viewer / pontos mobile:** revisão visual no viewport 390×844 CSS px em tema escuro e claro. Os quatro pontos estavam presentes; o ativo permaneceu acentuado e os três inativos ficaram visualmente distintos. CSSOM: dark inativo `rgb(196, 188, 178)`, light inativo `rgb(112, 108, 102)`; os pontos são 7×7 px. Isto valida somente a apresentação dos pontos nestes dois temas/um viewport, não a navegação completa nem contraste não textual em todos os fundos.
- **Access/manage CTA:** a página autenticada renderizou “Enviar link de acesso”. No tema escuro, CSSOM computou foreground `rgb(41, 39, 35)` sobre `rgb(226, 201, 145)`, razão `9.23:1`. Revisão visual confirmada. O painel de acessos recentes reportou falha de configuração do serviço. Não foi preenchido destinatário nem enviado convite.
- **Configurador:** o acesso Admin no host #271 permitiu abrir `/config/`, mas o shell depois reportou “Não foi possível validar a configuração publicada. O configurador está temporariamente indisponível.” O estado inicial anterior ao erro não foi usado como evidência. Títulos de seção e anel de acabamento selecionado seguem **sem revisão visual hospedada**. Nenhuma configuração foi publicada ou salva.
- **Efeito em G2:** dois dos quatro pontos visuais alterados em #271 têm evidência hospedada pontual (pontos do Viewer e CTA de acesso); Configurador (títulos/anel) permanece pendente. #208 segue aberta. A lista de acessos falha no Preview e não foi tratada como regressão da mudança CSS sem diagnóstico do serviço.
- **Sessão/preview:** login foi concluído no host do #271 por ação do usuário; não houve cópia de credenciais ou token. O viewport temporário será restaurado após a revisão.


## Continuação — matriz G3 de navegação (2026-11-11, BRT)

A PR #119 foi ampliada no mesmo branch, sem abrir branch adicional. No pin `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, a matriz agora documenta separadamente: menu público estático das páginas Landing/How/About; menu privado gerado por `core/private-navigation.js` para Admin/Access e dependente de sessão/papel; folhas e ordem declaradas; estados `aria-expanded`, `aria-current`, `hidden`, foco, Escape, pointer fora, hover e loading/autorização. A conclusão atual é que não há contrato comum entre as famílias para extrair: o público mantém shell/controlador próprios; Admin e Access compartilham o contrato privado, mas com conteúdo condicionado por sessão. **G3 segue parcial** porque faltam runtime/CSSOM/screenshot por estado e os focos restantes (marca/ícone/slots, estados adicionais).

O checkpoint também foi corrigido: o login no Admin ocorreu no host #271; a hierarquia administrativa carregou, enquanto `/config/` autenticado falhou na validação da configuração publicada. A revisão limitada do Viewer e CTA de Access/manage permanece registrada. O viewport temporário foi restaurado e a aba do Admin ficou aberta para continuidade. Nenhum dado foi publicado, convite enviado ou alteração de CSS feita.

**Branches:** Design System continua em 2/2 e produto em 5/5. Não removi a branch encerrada de #270: o procedimento do produto exige autorização por SHA e manifesto aprovado, e ela não bloqueia a execução no limite atual. A próxima proposta de limpeza deve apontar para a branch e SHA exatos, depois de revalidar proteção, conteúdo e relação com #271.


## Continuação — G3 marca e tema (2026-11-11, BRT)

Foi documentado no inventário de ownership que `core/ui-theme.js` centraliza a escolha auto/light/dark, a persistência, a troca de logo e a criação do toggle, enquanto públicos, Viewer e páginas privadas fornecem slots/geometrias próprios. A conclusão distingue contrato comportamental compartilhado de layout contextual; não sugere globalizar o CSS nem aprova token novo. G3 segue parcial, e G4 continua condicionado à evidência de runtime/custos do consumidor.


## Continuação — UX-04 dispatch e higiene exata (2026-11-11, BRT)

A PR de navegação #269 recebeu o workflow `.github/workflows/development-ux04-geometry.yml`, copiado byte a byte do pin `development@1a69ff76a5f36e3245a288773bb409aa662e4e62` (blob `96703ca3ae3c195153f10742134dca7aa69b0faf`). A mudança desde o head visualmente revisado só adiciona esse workflow; a árvore de aplicação permanece idêntica. No head #269 `2533a66376a016bcb8442e401de8933cb5a1edb4`, 12/12 checks Actions concluíram com sucesso. A PR permanece draft e sem merge; o workflow ainda não está em `main`, logo não foi possível despachar UX-04 no SHA corrente de development. Após a integração pelo fluxo de revisão, reobservar `development` e despachar seu SHA exato.

**Candidato de higiene produto #270:** PR fechada sem merge, branch `codex/ds04-208-css-contrast-20261111@219d9e672bf390a7af4b5815d50f9ea15f723913`, sem proteção. A branch `codex/ds04-208-preview-batch-20261111@6030eec03e8dad0c91672744b59b9c63080ce835` (PR #271 aberta) está dois commits adiante, sem diferenças de árvore; a mudança de #270 está retida na linha de commits de #271. O ref #270 pode ser candidato depois de aprovação exata, mas a política vigente exige `ops/branch-dispositions.json` e `ops/branch-hygiene-batch.json` integrados na main, revisão do plano com hash, aplicação via workflow e readback. Não apaguei diretamente. Produto segue com 5 refs (5/5); DS com 2 (2/2). Um PR de higiene dedicado exigiria branch temporária acima do soft cap, então aguarda-se decisão do usuário sobre autorizar a remoção deste SHA exato e permitir esse lote temporário.


## Rechecagem do executor de higiene do produto — 2026-11-11

A auditoria do código em `main` confirmou um bloqueio adicional para o candidato #270. `tools/branch_hygiene_plan.py` inclui evidência `explicit-terminal-disposition` e marca o ref como `delete-candidate` quando `terminalBranches` fixa SHA e `allowDelete=true`. Porém `select_bounded_batch()` aceita somente `ancestor-of-control` ou uma prova `squashMerge` ligada a PR mesclada; a evidência de disposição terminal não satisfaz o seletor. A PR #270 está closed/unmerged e sua branch não é ancestral de main, então o workflow atual rejeitaria o lote mesmo com SHA autorizado. A branch aberta #271 tem árvore idêntica, mas não serve como prova de squash da #270. **Não contornar** com exclusão direta; corrigir o seletor e adicionar cobertura negativa/positiva no processo canônico antes de qualquer aplicação. A autorização exata por `codex/ds04-208-css-contrast-20261111@219d9e672bf390a7af4b5815d50f9ea15f723913` e qualquer branch temporária acima do soft cap ainda precisam de concordância do usuário.


## Atualização operacional — preview G2 e lote de higiene #270 (2026-11-11, BRT)

Esta seção prevalece sobre os snapshots anteriores para os estados explicitamente atualizados abaixo. As fotografias históricas permanecem preservadas.

- **Refs/PRs:** Produto main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95, development@1a69ff76a5f36e3245a288773bb409aa662e4e62, seis branches remotas: main, development, #269, #270, #271 e #272. O limite brando produto≤5 está excedido em uma branch temporária, conforme lote aprovado; não remover refs antes do gate. Design System segue com 2 branches e PR #119 draft.
- **Higiene #270:** usuário autorizou preparar o lote exato. PR [#272](https://github.com/EAKerber/MobiliPresenter2D/pull/272) está aberta e pronta para revisão, head 5a49057b769096e04eda5b208f3d0944db1369fc. Ela corrige a seleção da disposição terminal e fixa somente codex/ds04-208-css-contrast-20261111@219d9e672bf390a7af4b5815d50f9ea15f723913 (PR #270 encerrada, sucedida pela #271). A auditoria do lote passou sem deletar refs; checks de branch hygiene e preview terminaram em sucesso. O merge da #272 acionará o apply e a limpeza condicional da branch head da PR; nada foi integrado e #270 continua presente. Readback pós-apply ainda é obrigatório; resultado esperado: 5 branches, sujeito a novas verificações de identidade/proteção/inventário no runner.
- **G2/#216 no Preview #271:** revisão CSSOM no Preview público https://deploy-preview-271--mobilipresenter2d.netlify.app, commit 6030eec03e8dad0c91672744b59b9c63080ce835, viewport 503×667 CSS px, temas light/dark. Em /, .hero-description, e /how-it-works/, .how-hero-note, o tema claro computou #292723 sobre #F0EDE8 (12,77:1) e o escuro #C4BCB2 sobre #20211F (8,61:1). Em /about/, .about-scale p:not(.eyebrow) correspondeu a 3 parágrafos com os mesmos valores. A exceção .study-band .eyebrow computou #70522F sobre #E8E3DC (5,60:1) em light e #D8BC7C sobre #20211F (8,78:1) em dark. Elementos visíveis e regras vencedoras confirmadas no CSSOM. A cor clara #292723 vem do token explícito desta candidata e não é o par histórico #675F55; excede o mínimo, mas a equivalência visual não foi homologada por isso. Esta checagem não é screenshot/revisão visual da página completa, nem cobre os cinco consumidores adicionais, Configurador, #208 ou DS-05A. #216 permanece aberta; G2 segue em andamento.
- **G1–G8:** sem mudança global: G0 contínuo; G1 parcial (UX-04 no runner Linux/Node 22 e critérios restantes de #218 pendentes); G2 em andamento; G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente; G8 não iniciado como release. Nenhum merge, deploy de produção ou operação de banco ocorreu.


## Atualização de evidência — G3 runtime, DS-05A e #viewerHint (2026-11-11, BRT)

- **G3 tema:** no Deploy Preview #271 head `86c4945cb56c04df31954e2a02f66ca3e703dc67`, Chrome 156, viewport 503×667 CSS px/DPR 1,5, modo `auto` acompanhou a preferência light/dark. Landing/How/About usaram a mesma classe de controle e botão 44×44 px; Enter percorreu auto/light/dark/auto, rótulos acessíveis mudaram, logo light/dark alternou e `casa-ui-theme-mode-v1` persistiu ao navegar entre rotas. CSSOM mostra regra em `ui-theme.css:61/73`; folhas/shell de página seguem contextuais. Slice público e uma largura, sem touch ou Safari/iPad.
- **G2 #viewerHint:** PR #271 head `86c4945` agora inclui a regra de development `.viewer-card__footer { color: var(--muted) }`. O subgate local reporta 1,00/4,05:1 em main e 5,22/4,88:1 em development (light/dark), mas o receipt não identifica a folha CSS por hash. Checks estão em execução e o Deploy Preview foi marcado pronto. No contexto isolado da auditoria, `/config/` redirecionou a `/access/`; não houve confirmação CSSOM hospedada da nova regra.
- **Errata DS-05A:** o JSON de runtime foi capturado com a regra experimental `.module-number` já presente. 13,02:1/8,10:1 são medições pós-patch sem braço anterior; não provam melhora nem defeito original. O recibo não fixa o CSS blob, a regra não é probe nomeado em #208 e falta revisão visual. A redação local foi corrigida e a regra não foi levada ao produto. Próxima decisão exigiria A/B isolado, pin/hash de cada folha, cobertura de estados e revisão visual.
- **Repos/limites:** #271 segue aberta; #272 segue sem merge/apply; produto 6 refs, Design System 2. Sem remoção de branch, publicação de produção ou alteração de dados.

## Retomada — avanço G1 NAV-005 e percurso arquitetural (2026-11-11, BRT)

Esta seção prevalece sobre os snapshots operacionais anteriores. O checkpoint completo e a matriz de medidas estão em [architecture G0–G8 current checkpoint](../evidence/architecture/architecture-g0-g8-current-checkpoint-2026-11-09.md).

- PR produto #269 está aberta/draft no head 2e202e4d7d36f29bfb62508bc15f40cdc18f130b, com Deploy Preview pronto e 12/12 Actions success. A regra .site-header--public .brand foi ajustada de 36vw para 30vw dentro do limite de marca definido em #218.
- No Preview, a revisão cobriu 486; 321/320; 291/290; 900/901; três rotas públicas a 1366; Viewer a 390; menu/CTA e teclado Enter/Space, Tab, Escape, foco claro/escuro. G1 avançou, mas #218 segue aberta para touch/dispositivo real, zoom de navegador e Safari/iPad. UX-04 é separado e ainda depende de seu workflow chegar à branch padrão antes do dispatch em development.
- Produto mantém 6 refs (cap 5 excedido em uma): #270 fechada sem merge, #269/#271/#272 abertas. O lote exato da #270 está preparado na #272, sem apply/deleção. Design System mantém 2 refs (cap atingido), PR #119 aberta/draft. Não criar refs novas; seguir Git Data + expected-SHA lease pelo método do produto.
- G0 contínuo; G1 parcial; G2 em andamento (#208/#216 e DS-05A sem fechamento); G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente; G8 sem release.
- Próxima sequência: completar os gates G1 que exigem dispositivo/zoom; resolver G2 com configuração válida, comparação A/B e CSS blobs exatos; terminar ownership por rota/estado em G3. Só então avaliar extrações reversíveis G4/G5; preservar zero extração onde não houver equivalência/ganho. G6 continua experimental até haver segundo consumidor editorial. G7/G8 requerem jornadas protegidas, validação integrada, revisão e autorização apropriadas.
- A regra experimental .module-number continua sem adoção: o recibo DS-05A é pós-patch, sem braço prepatch. Não extrapolar os valores observados.
- Sem merge de PR, remoção de refs, publicação ou alteração de dados nesta retomada.

## Retomada live — plano G0–G8 e higiene de refs (2026-11-11, BRT)

Esta seção prevalece sobre os snapshots operacionais anteriores; eles permanecem como histórico.

- **Design System:** remoto `EAKerber/MobiliPresenter2D_DesignSystem`, `main@79db735d6f05177b0c406e383d35832f3d72fdef`, 2 refs (`main` + branch da #119), na meta de estabilidade; o gatilho para avaliar um limite rígido é 5. PR #119 segue Draft.
- **Produto:** `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, 7 refs. O gatilho 5 foi excedido por 2 e exige revisão do crescimento, mas não é autorização de exclusão. #273 está aberta em Draft, com base exatamente no SHA atual de `main` e cinco commits à frente; suas mudanças estão isoladas na PR. #272 prepara remoção exata de #270 e limpeza condicional de sua branch após integração, reduzindo 7→5; não houve merge nem exclusão.
- **Proteção de `main`:** comparação GitHub confirmou `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` e #273 Draft aberta nesse mesmo base SHA, com 5 commits à frente, 0 atrás e 10 arquivos no diff. #269/#271/#272 também estão abertas e sem merge. O conteúdo transitório da #273 não está em `main`.
- **G0–G8:** G0 contínuo; G1 parcial (UX-04 runner Linux/Node 22 e critérios touch/zoom/Safari/iPad de #218 pendentes); G2 em andamento (#208/#216, 98 pares UNCERTAIN, configuração de Preview inválida e DS-05A incompleto/HOLD); G3 parcial, com recaptura local de 28 casos em 7 rotas, 2 viewports e 2 temas; tema e seleção de assets concordaram, mas bundles/APIs privadas sem fixture retornaram 404; G4 HOLD; G5 parcial/HOLD; G6 HOLD; G7 pendente (#232 e fixture autorizada); G8 release não iniciado, sem autorização de produção.
- **CI da #273:** head `0d666c6db586ba5f4a2622d2684bbef122c208e7`, Preview pronto. Os gates `scoped-raster` e `browser` falham: raster Chromium 390 px acusa 18 pixels fora dos limites autorizados de texto ([#43123581900](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43123581900)); Chromium passa em 390, 700, 701, 1050, 1051 e 1366 px em light/dark, mas WebKit falha em 390 px/light (`expected compact`, `actual side-rail`), sem observação dos demais casos WebKit ([#43123581593](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43123581593)). CI não está verde.
- **Progresso desta retomada:** recapturar G2 localmente e ampliar G3 para 28 casos; ambos seguem parciais por configuração publicada inválida, 98 pares UNCERTAIN e cobertura privada/plataforma ainda ausentes. Meta estável: 2 refs. Ao atingir 5, revisar crescimento e considerar um hard cap; 7 refs do produto exige revisão, sem excluir por contagem. Usar branches existentes #119/#272, sem nova ref. Sem merge, exclusão, deploy de produção ou operação de banco.
## Continuação G2 — recaptura local do Configurador (2026-11-11, BRT)

A captura antiga tinha uma linha candidata escura cujo CSSOM não correspondia à aparência do screenshot; ela não foi usada como evidência. A reprodução mais recente fixa o tema antes da navegação e registra o tema solicitado, `data-theme`, `CASA_UI_THEME.getResolved()` e SHA-256 por screenshot. O conflito antigo não se repetiu, sem atribuir causa raiz.

O pacote [G2 recapture](../evidence/architecture/g2-configurator-recapture-2026-11-11.md), com oito imagens e recibo JSON, fixa produto `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, CSS base `d43e6fb5e66133d2389b5c39b165b76b13cfa868`, candidata #271 `eb346a41ad91f6dc53875cb954e9018fdc1dd713`, Edge `157.0.4341.46`, DPR 1 e 390×900/1366×900 nos dois temas. Todos os oito estados validaram o Buyer V5 local e tiveram os três indicadores de tema coincidentes. Um único 404 da bundle de navegação privada ocorreu em cada carregamento; não houve exceção de página. Esta evidência é local e não cobre autenticação/navegação privada nem substitui a validação hospedada.

G2 continua em andamento: configuração publicada inválida no Preview; anel de acabamento selecionado ainda sem captura deste lote; #208/#216, 98 pares UNCERTAIN e DS-05A permanecem pendentes. A documentação e o pacote foram adicionados à branch já existente da PR #119; nenhuma nova branch, mudança no produto, merge, deploy de produção ou operação de banco foi feita nesta continuação.


## Continuação G3 — recaptura local de tema e marca (2026-11-11, BRT)

A captura em produto main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95 percorreu /, /how-it-works/, /about/, /viewer/, /config/, /admin.html e /access/manage.html em 390×900/1366×900 CSS px e light/dark: 28 casos. A preferência, tema raiz e API concordaram; os src de todos os assets de marca corresponderam ao tema e os logos de cabeçalho carregaram. Os controles completaram duas transições e não houve exceções JavaScript de página.

As requisições às bundles e APIs privadas não foram preenchidas: 28 respostas 404, incluindo /api/buyer-configuration. O shell estático e o controlador foram observados; menu/sessão autenticados, configuração publicada, foco/hover, tela tátil, Safari/iPad e revisão visual não foram validados. Duas imagens de marca nos cards de comparação mobile de /how-it-works/ ainda informavam complete=false, com naturalWidth=380; esse detalhe está registrado no recibo.

Veja [relatório G3](../evidence/architecture/g3-theme-controller-slots-recapture-2026-11-11.md) e seu recibo JSON. G3 permanece parcial; os slots de marca/controle continuam contextuais. Nenhum código do produto foi alterado.


## Retomada live — main estável e política de refs (2026-11-12, BRT)

Esta seção prevalece sobre o snapshot anterior e preserva as entradas anteriores como histórico.

- **Política:** Design System — meta/soft cap de 2 refs, sem hard rule; produto — soft cap de 5 durante trabalho ativo, com alvo de 2 refs (`main` + `development`) quando estável. Ao chegar a 5, reavaliar crescimento e considerar hard cap; a contagem não autoriza apagar refs.
- **Main e hotfix:** produto `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; #273 está Draft no head `016b33f9315620ee09b28c4e2c9ba5752b858471`, baseada exatamente nesse SHA, 8 commits à frente e 0 atrás, com 11 workflows aprovados e Preview pronto. O conteúdo da #273 permanece fora da `main`; a revisão visual final da PR ainda está pendente. #269, #271 e #272 também permanecem sem merge.
- **Refs:** Produto tem 7 refs, acima do soft cap de 5. A #272 prepara a remoção exata da branch obsoleta #270 e a limpeza condicional da própria branch de higiene após integração, com queda prevista de 7 para 5; a PR não foi integrada e nenhuma ref foi removida. Design System tem 2 refs: `main` e a branch documental da #119, que continua Draft.
- **G0–G8:** G0 contínuo; G1 parcial; G2 em andamento; G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente (#232/fixture autorizada); G8 não iniciado. Os gates de arquitetura continuam independentes da revisão do hotfix.
- **Proteção:** GitHub informa que as regras de proteção das branches `main` estão desativadas nos dois repositórios. Nenhuma regra foi alterada neste trabalho; a estabilidade observada é processual.

## Atualização de 12/11 — G2 Admin e refs live

O recálculo local do Admin confirmou uma única lacuna de contraste clara para `.initial-state-option`: 4,229:1 no Product `main@221b54b`, com o dark em 8,384:1. O ajuste scoped em #271 mediu 9,092:1 usando o token já existente; consulte o [recibo completo](../evidence/architecture/g2-admin-initial-state-labels-cssom-2026-11-12.md). #271 está aberta no head `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`; os 9 workflows da PR e o status Netlify Deploy Preview passaram. **Na data desta entrada**, a revisão visual/CSSOM do Admin ainda dependia de autenticação; essa pendência foi superada pela revisão descrita na atualização posterior abaixo. `/config/` segue sem configuração publicada válida. Nada foi integrado à `main`.

Inventário conferido pela API: Produto tem **7 refs** (soft cap 5 excedido por 2; revisar, sem exclusão automática); Design System tem **2 refs**, dentro da meta. A #272 não foi integrada e nenhuma ref foi excluída. A regra vigente continua: Product target 2 quando estável; DS soft target 2; ao chegar a 5, avaliar se um hard cap é útil.


## Revalidação do Preview da Product #271 (2026-11-12, BRT)

Para o head exato `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`, a API confirmou nove workflows de PR com `success` e status do Netlify Deploy Preview com `success`. A publicação está pronta, mas não foi feita revisão visual/CSSOM hospedada da nova regra do Admin nesta revalidação; `/config/` ainda falha ao validar a configuração publicada. Product `main` permanece em `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. Nenhum merge, remoção de refs, deploy de produção ou operação de banco ocorreu.


## Continuação G2 — anel de acabamento selecionado (2026-11-12, BRT)

No checkout detached limpo do Product `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, a comparação base/candidata usou os blobs CSS `d43e6fb5e66133d2389b5c39b165b76b13cfa868` e `eb346a41ad91f6dc53875cb954e9018fdc1dd713`. O fluxo real avançou para Acabamentos e selecionou Base clara e Carvão. Chrome 156.0.8078.82 / DPR 1, 390×900 e 1366×900, temas light/dark: 16 capturas no total. Os 16 casos tiveram configuração Buyer V5 validada, estado selecionado real, `aria-pressed=true` e tema solicitado/documento/API coincidentes.

O CSSOM candidato computou borda `#292723` e anéis `0 0 0 2px #fff, 0 0 0 4px #292723`; a base usa borda branca e anel branco translúcido. As capturas mobile mostram contorno mais visível para Base clara no escuro e Carvão no claro. Relatório, recibo e capturas: [G2 selected ring](../evidence/architecture/g2-selected-finish-ring-2026-11-12.md). Um 404 esperado da bundle privada ausente ocorreu por contexto, sem exceção de página.

O subgate de seleção local avançou; G2 permanece em andamento. A configuração publicada de `/config/` continua inválida, e, **na data desta entrada**, a nova regra do Admin de #271 ainda aguardava revisão autenticada; veja a atualização posterior abaixo. #208/#216, 98 pares UNCERTAIN, DS-05A, teclado/foco, zoom e validação Safari/iPad permanecem fora desta evidência. Nenhuma mudança foi integrada à Product `main`.


## Atualização após revisão autenticada do Admin e correção das capturas G2 — 12/11/2026 BRT

O usuário autenticou no Preview exato da Product #271. A leitura do Admin em 634×652 CSS px / DPR 1,5 encontrou 18 labels `.initial-state-option` com caixas visíveis; as checkboxes estavam habilitadas e marcadas, e não foram alteradas. No CSSOM, light ficou em `#403A34` sobre `#EAE7E2` (9,092:1), dark permaneceu `#C4BCB2` sobre `#232321` (8,384:1). Nenhuma configuração foi salva. Os hashes das capturas de sessão e fonte da regra estão no [recibo Admin](../evidence/architecture/g2-admin-initial-state-labels-cssom-2026-11-12.md). Isso passa só o subgate de labels.

O primeiro lote do anel exibia transform de hover em 15/16 linhas. Ele foi substituído por 16 PNGs recapturados com o ponteiro em `(0,0)` e `transform:none` confirmado antes de cada captura; os hashes dos bytes conferem com o recibo compacto. A seleção real, `aria-pressed=true`, configuração Buyer V5 e tema são válidos em 16/16. **Este parágrafo registra o snapshot anterior ao recapture hover/foco:** naquela etapa, o relatório e o JSON cobriam somente o A/B sem hover; a cobertura foi ampliada nos adendos subsequentes. `/config/` continua sem configuração válida, então a revisão hospedada do ring segue pendente e G2 em andamento. 

Product `main` continua em `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; DS `main` continua em `79db735d6f05177b0c406e383d35832f3d72fdef`. O ramo DS existente da #119 está em `1f832fc1b2cc8fd2f3ccbf892ab8f9cea43fea15` antes desta atualização; o Branch hygiene run #81 passou nesse SHA. Inventário live: 7 refs no Produto (acima do soft cap 5) e 2 no DS. Nenhuma branch foi criada ou apagada, nenhum PR foi integrado, e não houve alteração de runtime/deploy/DB.


## Adendo G2 — estado hover do anel e coerência do handover (12/11/2026 BRT)

A mesma matriz local foi rodada com o ponteiro sobre o swatch selecionado. Em 16/16 casos, `:hover` permaneceu ativo após estabilização de 200 ms, o transform computado foi `matrix(1.06, 0, 0, 1.06, 0, 0)`, a seleção real persistiu com `aria-pressed=true`, e o Buyer V5/tema permaneceram válidos. O box-shadow base continuou branco translúcido; o candidato conservou o par branco/`#292723`. Não houve exceção de página; o 404 por contexto da bundle privada ausente foi o único erro HTTP. **Snapshot anterior à matriz de foco visível:** naquele ponto, o relatório e o recibo reuniam 16 capturas sem hover + 16 com hover; a seção posterior amplia o pacote para 40 estados. Isto não equivale a cobertura geral de hover/foco nem a revisão hospedada do anel; `/config/` continua inválido.

O subgate do Admin segue aprovado com autenticação, sem interação nas checkboxes. Para eliminar a contradição entre as notas datadas de 12/11, as entradas anteriores que dizem que a revisão do Admin aguardava autenticação são agora explicitamente históricas e apontam para a atualização que registra a conclusão.


## Adendo G2 — foco visível por teclado no swatch selecionado (12/11/2026 BRT)

Com a mesma fixture Buyer V5 local, foram comparados baseline/candidata, light/dark e Base clara/Carvão em 390×900 CSS px: oito capturas. O ponteiro ficou fora dos swatches; Tab/Shift+Tab levou foco ao botão selecionado. Em 8/8, `:focus-visible` foi verdadeiro, `:hover` falso, `transform:none`, a seleção persistiu e `aria-pressed=true`. O outline computado foi `rgb(110,81,46) solid 2px` em light e `rgb(216,188,124) solid 2px` em dark; o `box-shadow` do anel permaneceu específico de base/candidata. A revisão visual das capturas mobile não mostrou clipping. Sem exceções de página; apenas o 404 esperado por contexto da bundle privada ausente. O [relatório e recibo combinados](../evidence/architecture/g2-selected-finish-ring-2026-11-12.md) agora reúnem 40 estados: 16 no-hover, 16 hover e 8 focus-visible. Este recorte não cobre a navegação completa por teclado, outros controles, zoom, Safari/iPad ou o ring hospedado; `/config/` segue inválido.


## Snapshot G3 — ownership de `.swatch` no Configurador (12/11/2026 BRT, pré-captura local; superado pelo adendo final)

A varredura do pin Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` encontrou dois geradores dentro de `/config/`: `renderFinishControlsFromData()` cria os acabamentos globais em `#finishSwatches`, e `createLocalFinishControl()` cria acabamentos locais dentro de `moduleDetail`. Ambos usam `.swatch`, `.is-selected` e `aria-pressed`; os handlers e os domínios de seleção são separados. A rota carrega `styles.css` (`app/config/index.html:30`) antes de `ui-theme.css` (`:41`); a família inclui base/hover/selected/responsivo em `app/styles.css:349–367,692` e foco geral de botão em `:96–98`.

**Snapshot pré-captura, superado pelo adendo final desta página:** a matriz de 40 estados do anel cobria então somente o consumidor global (`data-finish-id`). O consumidor local (`data-local-finish-id`) estava mapeado estaticamente e ainda não tinha prova runtime naquele ponto. A captura posterior de 8 casos abaixo completa a linha `.swatch`; G3 como gate geral permanece parcial. Não extrair CSS nem alterar produto.


## Snapshot G3 — ownership de `.swatch` no Configurador (12/11/2026 BRT, pré-captura local; superado pelo adendo final)

A varredura do pin Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` encontrou dois geradores dentro de `/config/`: `renderFinishControlsFromData()` cria os acabamentos globais em `#finishSwatches`, e `createLocalFinishControl()` cria acabamentos locais dentro de `moduleDetail`. Ambos usam `.swatch`, `.is-selected` e `aria-pressed`; os handlers e os domínios de seleção são separados. A rota carrega `styles.css` (`app/config/index.html:30`) antes de `ui-theme.css` (`:41`); a família inclui base/hover/selected/responsivo em `app/styles.css:349–367,692` e foco geral de botão em `:96–98`.

**Snapshot pré-captura, superado pelo adendo final desta página:** a matriz de 40 estados do anel cobria então somente o consumidor global (`data-finish-id`). O consumidor local (`data-local-finish-id`) estava mapeado estaticamente e ainda não tinha prova runtime naquele ponto. A captura posterior de 8 casos abaixo completa a linha `.swatch`; G3 como gate geral permanece parcial. Não extrair CSS nem alterar produto.


## Atualização G3 — runtime do acabamento local ao módulo (12/11/2026, BRT)

A cópia limpa destacada do Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` gerou um fixture Buyer V5 em memória: `base-light` permaneceu global; `cocoa` e `shadow` ficaram locais e habilitados para `module-01`. O validador e a projeção Buyer V5 aceitaram o fixture. O Playwright abriu `/config/`, selecionou o módulo e clicou os botões locais reais. Nenhuma configuração foi salva ou publicada; não houve API remota ou banco.

- 8 capturas: baseline/candidata × light/dark × `cocoa`/`shadow`, em 390×900 CSS px, Chrome 156.0.8078.82 / DPR 1.
- Em 8/8, o `aria-pressed` local acompanhou a seleção; o acabamento global permaneceu `base-light`. Borda, box-shadow e transform computados coincidiram entre swatch local e global na mesma página. Sem erro de página nem erro HTTP inesperado.
- Relatório, recibo e PNGs: [evidência G3 do consumidor local](../evidence/architecture/g3-module-local-swatch-runtime-2026-11-12.md). Os 40 casos G2 anteriores continuam sendo estritamente a matriz global; as 8 capturas locais são separadas.
- Classificação `.swatch`: aparência do anel compartilhada dentro de `/config/`; escopos de seleção distintos por design; nenhum consumidor cross-route identificado. A linha runtime de G3 agora está coberta e não sugere extração. G3 como gate geral segue parcial; G2 hospedado continua pendente porque `/config/` rejeita a configuração publicada.

Sem alteração do produto, banco, publicação, refs remotas ou `main` do Product.

## Reconciliação live do plano arquitetural geral — 12/11/2026

O objetivo corrente abrange ARC-01…ARC-16 e V0–V6; G0–G8 é outro plano de consolidação e verificação que continua sendo acompanhado. Este adendo compara as afirmações históricas com o Product main confirmado, sem reescrever evidência antiga.

### Entregas arquiteturais já integradas

- O Product main observado é 221b54b2a41ecc8c338d1bf2cf67280cf165ce95. A PR [#237](https://github.com/EAKerber/MobiliPresenter2D/pull/237) está merged; seu merge commit 5ccb2a8dde6dd16e136f03387dc833aab828c5cf e o commit de origem ARC-03C ff5c55c24ef42eb106e6dda6aa7698b00355270a são ancestrais desse main.
- ARC-03C está implementado no build: scripts/compile-primary-pages.mjs gera as páginas a partir de architecture/pages e architecture/fragments; package.json inclui o gate/build; architecture/fragments/primary-header.routes.json declara BUILD_AUTHORITATIVE_ARC03C e exclui Viewer, Config, Admin e Access do escopo. A PR #237 integrou o controlador de navegação pública e preservou a variante Viewer NAV-005. O resultado é integração em main, não apenas uma prova isolada.
- O arquivo de integração ARC-03C e o handover do produto de 22/10 ainda descrevem a etapa como isolada ou como próximo passo. Esses trechos agora são snapshots pré-integração; uma revisão documental focada no Product permanece pendente.

### Entregas e gates ainda abertos

- V0/ARC-13 ainda não tem inventário integral nem catálogo pt-BR consumido pelo runtime. O índice legado de 826 ocorrências em 26 fontes continua como histórico de candidatas. Um scanner local sobre Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` está pronto no branch local `work/arc13-ui-inventory-20261112` (HEAD `c7262cf`, commits locais; sem publicação/PR e com `app/` inalterado). Ele gera um candidato limitado e não classificado com 988 ocorrências (600 HTML, 388 sinks JS; 154 estáticas e 234 dinâmicas/mistas), 17 exclusões explícitas, zero erros de análise e zero lacunas de rota. Símbolos e pontuação dinâmica permanecem para revisão contextual. Isso ainda não prova cobertura integral nem rastreia todas as origens de dados; classificação, origem/owner e reconciliação das lacunas precedem qualquer catálogo de runtime.
- V2/P-TOKEN: há pin e exportações versionadas, mas isso não prova ativação geral de tokens no CSS do produto. A origem e os consumidores precisam ser reconciliados com os pares visuais homologados; nenhuma paleta global deve ser ativada por inferência.
- Os gates G0–G8 permanecem conforme o checkpoint de 12/11: G0 contínuo; G1 parcial; G2 em andamento; G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente; G8 sem release. A conclusão de ARC-03C não fecha esses gates nem o plano geral.
- G4/G5 de CSS compartilhado continuam condicionados à prova de ownership e equivalência por consumidor. A linha .swatch está coberta em G3, mas o inventário de ownership geral está parcial.
- V6/G7/G8 ainda exigem cobertura funcional integrada por risco, evidência de dispositivo e autenticação quando cabível, revisão dos riscos residuais, aceitação e autorização de release. CI, preview e merge não se substituem entre si.

### Próxima sequência de execução

1. Reconciliar a documentação do Product com o main@221b54b, começando por ARC-03C já integrado e preservando a proveniência do snapshot de outubro.
2. Revisar o candidato local V0/ARC-13 já gerado: classificar as 988 ocorrências e 17 exclusões por origem/rota/consumidor/owner, completar a auditoria de sinks e lacunas e reconciliar o resultado com o contrato ARC-13. Só depois planejar substituições pt-BR em lotes reversíveis. Publicar a branch do produto após a higiene autorizada reduzir as refs; não criar catálogo ou alterar runtime antes da revisão.
3. Prosseguir G1–G3 nos gates ainda reproduzíveis; manter hospedado/PENDING o que depender da configuração publicada inválida, e classificar sem adivinhação os 98 pares com backdrop-filter.
4. Só então avançar extrações V2/G4/G5 aprovadas por família, mantendo domínio V5, autorização e publicação independentes; avaliar V5/G6 apenas por consumidores reais e benefício medido.
5. Fechar V6/G7/G8 com validação representativa e readback antes de propor release.

### Refs e operações

A consulta live de 12/11 mostra 2 refs no Design System (main e a branch da PR #119) e 7 no produto. A PR #272 prepara um lote exato para reduzir o produto de 7 para 5 após integração e readback; o lote ainda não foi aplicado. Nenhuma ref deve sair por contagem ou antiguidade. A documentação deste adendo é acrescentada à branch já existente da PR #119, sem criar ref; main, produto e dados publicados permanecem sem alteração nesta atualização.

## Retomada ARC-13 — revisão de fontes e inventário por ocorrência — 12/11/2026, BRT

Este adendo substitui a contagem anterior de 988 ocorrências como estado atual. O Product segue em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; a ferramenta e o relatório permanecem locais no branch `work/arc13-ui-inventory-20261112`, agora em `04945d6`. Não há PR de inventário nem ref remota do Product; `app/` continua inalterado.

- O scanner passou de 388 para 396 sinks JavaScript ao incluir atribuições compostas a texto e propriedades textuais em `Object.assign`; são 600 ocorrências HTML + 396 sinks JS = 996 registros, 159 valores JS estáticos e 237 dinâmicos/mistos.
- Agrupamento exato: 759 ocorrências com valor estático correspondem a 584 valores distintos; 65 grupos repetidos somam 175 ocorrências além da primeira. Há também 48 referências HTML. Esses valores incluem símbolos, marca e referências; continuam impróprios como estimativa de chaves ou esforço de tradução.
- A revisão manual cobriu 546 registros públicos, 280 de Admin/Acesso e 230 do Configurador; os recortes compartilham módulos de runtime e não são aditivos. O relatório permanece `candidate-unreviewed`; zero erros de parser, owners ou rotas não demonstram cobertura lexical.
- As fontes ainda ausentes incluem a tabela de explicações de Como funciona, labels da navegação compartilhada, mapas/opções/mensagens de erro do Admin e textos em módulos de dados de Landing/Viewer. O próximo trabalho é inventariá-las como fontes com provenance separada dos sinks, e só depois fechar a classificação e planejar o primeiro lote pt-BR.
- O usuário apontou dois checks diferentes no Admin. O check por item (“Iniciar ativo”) e o controle de disponibilidade da etapa (“Ativa/Inativa”) têm responsabilidades distintas. Em `admin.css`, o primeiro não declara `accent-color` e herda o azul padrão do navegador; o segundo usa `var(--accent)`. Manter variantes semânticas faz sentido, mas a hierarquia visual ainda precisa de decisão baseada no contexto.

O recibo local detalhado está em `docs/architecture/arc13-source-review-2026-11-12.md` na branch local indicada. Nenhuma alteração de runtime, catálogo de mensagens, preview, deploy, banco, merge ou ref remota foi feita nesta retomada. A higiene continua em 7 refs no Product (duas acima do soft cap de 5) e 2 no Design System; a PR #272 continua preparada, não integrada.


## Retomada ARC-13 — fontes de texto, testes e controles do Admin (12/11/2026 BRT)

O Product continua ancorado em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. O trabalho ARC-13 permanece isolado na branch local `work/arc13-ui-inventory-20261112`, agora em `fb92edbc84fda44d19a68eed4fedb8326090c8d3` (commit `fb92edb`); não foi criado um ref remoto nem PR do Product.

- A ferramenta local passou a schema 3 e preserva duas listas diferentes: **1.011 ocorrências candidatas de sink** (600 HTML + 411 JavaScript) e **143 literais de origem JavaScript** em `sourceEntries`. As fontes não são somadas aos sinks. Há 167 sinks JS estáticos e 244 dinâmicos/mistos; 22 exclusões; 66 arquivos com hash; zero erros de análise, owners não atribuídos ou rotas JS não atribuídas. Tudo segue `unreviewed`.
- Entre as 143 fontes, 89 têm consumidor ativo documentado, 7 labels de vista são passados ao renderizador mas não usados, 2 campos da Landing não têm consumidor ativo e 45 mensagens de `Error` ainda precisam de rastreio antes de classificar como texto de usuário ou diagnóstico. A cobertura inclui tabelas de Como funciona/navegação/tema, textos da Landing e do Viewer e opções fixas do Admin. Dados editáveis do V5 e conteúdo comercial continuam fora de uma classificação automática.
- O número anterior “988 candidatos” era 600 sinks HTML + 388 sinks JavaScript; não representa 988 testes nem 988 mensagens únicas. A cobertura adicionada aumentou o número de sítios reconhecidos sem alterar o código do produto. Os recortes manuais 546/280/230 pertencem ao snapshot de 996 sinks; compartilham módulos e precisam ser reconciliados antes de virar porcentagem de cobertura.
- A validação padrão do Configurador encadeia 19 scripts Node e 2 validadores de assets. Nenhuma suíte foi executada nesta etapa e não houve auditoria de sobreposição entre asserções; quantidade e nomes de arquivos, sozinhos, não demonstram redundância.
- Os dois checks mostrados no Admin têm funções diferentes: checkbox por item para estado inicial, e toggle de disponibilidade da etapa. O primeiro não declara `accent-color` em `initial-state-option`; o segundo usa `var(--accent)` em `.switch`. A diferença de cor é explicada pelo CSS, mas a intenção de hierarquia visual continua sem decisão. Nenhum checkbox foi alterado.

A revisão detalhada está no checkout local do Product em `docs/architecture/arc13-source-review-2026-11-12.md`. A geração do relatório foi concluída e `git diff --check` passou; a suíte de testes não foi executada. `app/`, runtime, configuração publicada, refs remotas, merges e deploys permaneceram sem alteração. Ref count verificada nesta retomada: Product 7 (2 acima do soft cap 5), Design System 2.
