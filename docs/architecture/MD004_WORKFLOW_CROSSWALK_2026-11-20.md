## Readback operacional vigente — pós-#302 — 22/11/2026 (BRT)

- Product `main@2b1c70c049cdcb5e2a75fb2a970d1fd3d112cc98`; `development@f640f9018e6bc36cbf4ca79313a6576080e9ded4`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.
- #299–#302 foram integradas em `development`; nove workflows passaram no head exato da #302 `6d96342250ac34dc2a945b6794e5a09c67e0cdc7`, com árvore idêntica no squash integrado. Sem Deploy Preview; `main` não mudou.
- A matriz de 21 workflows abaixo é uma baseline histórica. Ela não representa a lista integral atual e não prova quais checks são obrigatórios; essa relação permanece `UNKNOWN`.
- #290 segue como PR Draft `main`→`development`; comparar deltas seletivos. O compare atual tem 450 commits exclusivos em `development`, 14 em `main`, base `221b54b2`.
- Product tem 6 refs: `main`, `development`, arquivo #274, buffer NAV-005 e branches integradas #301 `codex/cmp017-admin-control-contract-20261122` e #302 `codex/cmp017-finish-availability-20261122`. As onze refs anteriormente autorizadas foram removidas; #301/#302 permanecem.
- A PR DS #124 permanece documental e aberta; o head corrente não tem check-runs nem reviews registrados. A atualização documental não equivale à integração em Design System `main`.
- As entradas seguintes são snapshots históricos; seus pins e estados não devem ser usados como estado live.

---

## Readback após a publicação da #291 — 22/11/2026

- Product `main@2b1c70c049cdcb5e2a75fb2a970d1fd3d112cc98`; `development@188f5074f60dc35df7aa8c673dbac4a2249813be`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.
- A PR #291 foi integrada à main e a Production está pronta no deploy Netlify `6b033828fda9e5b6e8ced61b`; os quatro gates pós-merge passaram.
- A integração promoveu a ferramenta e o inventário ARC-13 como candidato não revisado; não aprova textos como catálogo nem conclui LOC-002…008.
- #274 segue Draft e preserva material exclusivo para triagem. #290 permanece inadequada para sincronização integral.
- A divergência segue ampla: 14 commits main-only, 446 development-only, base `221b54b2`. Product tem 13 refs; o soft cap é 5.
- A PR #124 permanece documental e sem integração. A tabela de workflows abaixo continua histórica; required checks atuais são UNKNOWN.

---

## Revalidação operacional live — 22/11/2026

- Product pins: `main@5b29934150a8f939057fbd3ae14fd1c1511afd03`, `development@188f5074f60dc35df7aa8c673dbac4a2249813be`.
- #271/#281 estão integradas em main e o deploy Production associado está ready.
- #297 e #298 estão integradas em development; os gates seletivos passaram. Isso não estabelece que seus workflows sejam required checks.
- PR #291: 12 checks sem falha e Deploy Preview READY, aguardando autorização explícita para main.
- #274 continua Draft com artefatos históricos preservados. #290 segue inadequada para sincronização integral.
- Compare entre branches: 13 commits main-only e 446 development-only a partir de `221b54b2`; não promover toda a árvore.
- A tabela abaixo descreve uma baseline histórica, não cobertura atual completa. Required checks permanecem UNKNOWN.

---

## Revalidação live — 22/11/2026 (BRT)

- Pins: Product main@5b29934150a8f939057fbd3ae14fd1c1511afd03; development@9e352dbd2644e4e91c8fe533f92bf0a8827a840d. A matriz de 21 workflows abaixo continua sendo uma baseline histórica, não um inventário completo.
- #293 está integrada em development após 14 checks verdes no head exato da PR. Nenhum Deploy Preview foi produzido para o alvo development; a integração não é prova de revisão visual hospedada nem de Production.
- #295 mantém o foco em dois gates: pin de main e assentamento do layout do fallback antes da comparação geométrica. O head 7d6f759337c67d0ffbb5733dfeaa294528708644 tinha Current asset gates verde; o workflow VIS-002C continuava em andamento no último readback. Não há evidência de required checks.
- #291 aguarda autorização para main; #274 segue Draft, com 35 caminhos exclusivos preservados para triagem. Não promover a árvore inteira de development à main.

---

# MD-004 — crosswalk de workflows do Produto (baseline de 21)

**Pin da baseline histórica (21 workflows):** Product `main@dc066f55619824626ea4752ecc0bafc67f9d9110` (20/11/2026 BRT).  
**Método:** leitura estática de eventos e filtros, jobs, comandos, imports/fixtures e assertions chamadas. O crosswalk descreve o contrato pretendido do gate; não transforma um run verde em confirmação de check obrigatório, deploy no mesmo SHA ou comportamento hospedado.  
**Execuções:** esta leitura não dispara workflows. Os resultados listados abaixo são execuções separadas nos heads candidatos de #286 e #287; não definem required checks nem provam deployment.

## Revalidação live — 21/11/2026, atualização após #292

- Product pins: main@5b29934150a8f939057fbd3ae14fd1c1511afd03, development@44c7cb6495540e4038717b26fb2b1e96b02571f4. A tabela abaixo continua descrevendo a baseline histórica main@dc066f55; não é um inventário completo dos workflows atuais.
- #269, #271 e #281 estão integradas na main; Production está pronta no deploy 6b01d6e95f50b12695984d74, SHA 5b29934150a8f939057fbd3ae14fd1c1511afd03.
- #291 (head 1f34543974ae64abd7d133baffab64f3a238953b) está pronta para revisão, ainda fora da main. Passaram ARC-13 (44934586742), Buyer (44934586734), assets (44934586750), NAV-005 (44934586866) e skip-link (44934586728); Deploy Preview READY. Nenhum run dessa PR atualiza a contagem da baseline da main.
- #292 foi integrada em development@44c7cb6 após os gates ARC-13 e assets passarem no head exato da PR. A atualização do scanner e inventário não altera runtime público nem conta como gate pós-merge no SHA de integração.
- #274 segue Draft na base antiga. #290 tenta apontar a main inteira para development, está mergeable=false, e não é seguro como veículo: compare exato indica 13 commits main-only contra 441 development-only. Required checks permanecem UNKNOWN.
- UX-04 run 44838594398 é sucesso no SHA histórico development@be743fd; o development corrente está em 44c7cb6. Não inferir validação do head atual.

**O delta UX-04 de 20/11 abaixo é um snapshot histórico.**

### Delta UX-04 — snapshot de 20/11/2026

- Pins atuais: Product `main@29e824e2f6c44af9c8f04fd9966ec3190f3637b8`; `development@be743fd98063b19be5ee0614add21b8c85fb4a85`. A branch principal contém 22 workflows; a tabela dos 21 itens abaixo é a baseline histórica pinada em `main@dc066f55`.
- A #279 foi integrada em `main` como o 22º workflow: `.github/workflows/development-ux04-geometry.yml`, blob `96703ca3ae3c195153f10742134dca7aa69b0faf`. O workflow também está em `development@be743fd` com o mesmo blob e os arquivos necessários ao gate.
- **Evento e proteção:** `workflow_dispatch` e `push` apenas em `development` nos caminhos declarados; `permissions: contents: read`; sem secrets, serviços externos ou runtime do Produto.
- **Jobs:** arquivo/autoridade/testes estáticos (`unittest`, flow layout/model, hierarchy e `pages:check`); depois browser V5 local com geometria UX-04 e regressão completa de teclado Chromium. Os artefatos são dois JSONs, retidos por 14 dias.
- **Estado atual:** o [run 44838594398](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44838594398), disparado por `workflow_dispatch`, passou os dois jobs no SHA exato `development@be743fd98063b19be5ee0614add21b8c85fb4a85`. O artefato `development-ux04-geometry-focus-44838594398` (ID `14679149233`, 1.644 bytes, SHA-256 `ecb908825ae970d436b9bc995d9840a5416428edf82129f753345ac4421bf8f7`) está disponível até `2026-12-04T23:42:21Z`. O run usa V5 local; não prova preview hospedado nem configuração de checks obrigatórios.
- Nenhum teste foi removido. O delta não altera a baseline histórica dos 21 workflows nem define required checks.

## Snapshot histórico dos ports de trigger — 20/11/2026, antes das integrações #278–#280

- Product `main@dc066f55619824626ea4752ecc0bafc67f9d9110`; `development@acf12c4170401ceb822526a613d89657e26c6310`.
- #286 foi integrada por squash em development depois de 9/9 gates únicos verdes no head `4680ddca`. O readback confirma o merge como ponta de development; a consulta de Actions não encontrou runs no SHA do merge. O pacote altera somente filtros YAML.
- #287 permanece Draft no head `26a2da331445ca2901d2851c0d37976a871ea875`, base exata `main@dc066f55`. Os quatro gates relevantes passaram no head exato e o Preview #287 está READY. O diff final contém quatro workflows e nenhum runtime.
- ARC-03C foi diagnosticado no head pai `30db98d728fc2cd4c578c1081053d0bf7b8b3e47`: build/fonte passaram; a comparação de browser divergiu da baseline histórica `303468b4` em `/about/320/light` (`rgb(34, 33, 31)` atual vs. `rgb(0, 0, 0)`). O trigger temporário foi removido ao restaurar o workflow ao conteúdo de `main`; não houve rerun no head atual. Páginas/CSS não mudaram e nenhuma asserção ou baseline foi alterada.
- #274 continua Draft sobre base anterior; tem 15/15 classificações técnicas LOC-002 e quatro gates verdes, mas owners/destinos continuam pendentes. Nenhuma classificação implica aprovação editorial.
- Nenhum teste foi removido. Required checks e associação de resultado a deployment permanecem `UNKNOWN`.

| Workflow | Evento e alcance do filtro | Job / comandos principais | Fixture e contrato/assertion principal | Leitura do gatilho |
|---|---|---|---|---|
| `app-build-purity.yml` | PR, push em `main`, dispatch; amplo `app/**`. | `current-build`: `npm run build`, verifica pureza do build, `npm test`; R5A só em replay explícito. | Checkout do app. Build deve ser reproduzível e não reescrever fontes rastreadas; suíte principal segue disponível. | `app/**` é coerente com dependências. O replay histórico continua manual. |
| `candidate-assets.yml` | PR, push em `main`, dispatch; app, ferramentas, referências e oito módulos Python nomeados. | `current-asset-gates`: módulos Python focais, `app/npm test`, manifesto/render de variantes, validadores de pedra, torneira, faixa, intake e proveniência. | `reference/variant-cases.json` e evidência local temporária; publica artifacts/relatório. | #284/#285 já estreitaram `tests/**` para os oito arquivos executados. Sobrepõe operações de variante, mantendo checagens extras. |
| `variant-fidelity.yml` | PR, push em `main`, dispatch; app, referências de variantes e ferramentas. | `variants`: `app/npm test`, manifesto, renderizador e resumo de fidelidade. | Casos do manifesto de variantes; prova dedicada de fidelidade e artefato. | Não observa `tools/requirements.txt`; `candidate-assets` cobre `tools/**` e repete manifesto/render. Repetição de comando não equivale a assertion redundante. |
| `module02-fidelity.yml` | `workflow_dispatch` com `target_ref`; sem PR/push. | Checkout da ref escolhida, validação R4, `app/npm test`; replay R4 somente na baseline aplicável. | Imagens históricas pinadas no workflow. Replay de checkpoint visual histórico. | Evento manual faz sentido para replay direcionado. SHA imutável efetivamente usado permanece desconhecido. |
| `about-skip-link-focus.yml` | PR para `main` e push em branch histórica; filtros de página, script e workflow. | Build, `pages:check`, servidor local e Playwright. | Páginas compiladas; Tab/ativação do skip link deve levar foco a `main#main[tabindex="-1"]`. | #287 inclui `package.json` e `scripts/compile-primary-pages.mjs`; o run `44808609053` passou no head exato `26a2da33`. |
| `admin-hierarchy-browser.yml` | PR, push em `main`, dispatch; filtros por admin/core/endpoint/testes. | `browser`: três testes Playwright para hierarquia, persistência isolada de puxadores e Save V5/readback. | Servidores locais temporários e stubs. Confere hierarquia, V3/V5, preço, escrita segura e ausência de erro browser. | Cinco inputs estavam ausentes; todos são adicionados nos dois eventos por #286. |
| `arc03c-static-page-build-gate.yml` | Push em duas branches históricas no pin da `main`; sem PR. | `build-and-source`: autoridade, build e contenção privada; `browser-baseline`: build e diferencial Chromium/WebKit em 60 estados. | Baseline HTML histórica; compara DOM/CSS/layout e pixels dentro da tolerância. | A PR #287 restaura este workflow exatamente ao conteúdo de `main`; ele não integra a diff final. O diagnóstico `44799226223` no head `30db98d7` passou build/source e divergiu visualmente da baseline histórica em `/about/320/light`; não houve rerun no head atual. |
| `p-comp-01-public-menu-gate.yml` | Push somente em `architecture/p-comp-01-arc03c-reconcile`; sem PR/main. | Contrato de cutover, servidores locais baseline/candidate, Chromium/WebKit e browser de menu/header secundário. | Nenhum backend Netlify; testa quatro menus, teclado/pointer, foco, tema, viewport e preservação DOM/CSS/pixels. | Faltam no filtro dois testes executados. Como o evento é preso a branch de integração, confirmar se a branch/gate ainda é ativo antes de ampliar eventos. |
| `public-routing-before-clerk.yml` | PR e push em `main`; rotas públicas, função e testes selecionados. | Contratos estáticos/endpoint; browser do Deploy Preview apenas na PR para `main`. | Fixture local e preview; testa rotas, DTO allowlist e respostas negativas. | #286 adiciona catálogo/cena em PR/push e demais dependências de push. O glob de testes vira uma lista por evento: PR roda `public-cutover-contract.cjs`, `public-module-projection.test.cjs` e `public-pages-smoke.cjs`; push lista apenas os dois testes estáticos, pois o browser não roda. O crosswalk preserva que o browser hospedado foi pulado em #286, cuja base é `development`. |
| `public-production-readonly.yml` | PR para scripts do gate; push em `main` também páginas públicas e função. | `production-readonly`: Node 22, `node tests/public-production-readonly.cjs`. | Sem fixture local; GET real anônimo em Production. Rotas públicas retornam status/assinaturas esperadas; `/config/` redireciona a `/access/`; DTO JSON respeita schema/allowlist; inspeção é 400 e PUT é 405. | #287 acrescenta `app/core/public-module-projection.js` ao filtro de push; o run read-only `44808609186` passou no head exato `26a2da33`. Ainda não associa a resposta a deployment id/SHA, que segue UNKNOWN. |
| `r0-contract.yml` | Somente `workflow_dispatch` com `target_ref`. | Checkout completo, instalação Python, compila validadores e executa `python tools/check-r0-contract.py`. | Manifesto e bytes reais da ref. Valida schema/canvas, caminhos, tamanhos/SHA, dimensões, alphaBounds e reconstrução pixel-idêntica. | Manual é coerente para replay histórico. No pin `dc066`, manifesto está READY; anotação antiga UNKNOWN está superada. Mutabilidade da ref escolhida não foi auditada. |
| `ux-auth-viewer-integration-gate.yml` | Push apenas em `integration/ux-auth-viewer-preview-20261021`; sem PR/main. | Auth recovery, cutover estático, `node --check`, accordion, Viewer header e editorial em Playwright. | Provedores de auth simulados, arquivos locais e API de módulos interceptada. Sessão velha não pode sobrescrever identidade atual; cutover mantém separação de páginas; browsers cobrem accordion, Viewer e editorial sem overflow/erros. | Repete dois testes de P-COMP e adiciona auth/accordion/editorial. O contrato de cutover lê Landing/root, `netlify.toml` e função que não estão nos paths. Branch-only; não ampliar sem confirmar vigência do fluxo. |
| `viewer-base-price-contract-gate.yml` | PR para `main`, push em `main` e branch de integração, mais dispatch; Admin, Viewer, função e testes. | Testes de save/publicação, quatro verificadores, `node --check`, build/pages-check e browser em Chromium/WebKit; runner Ubuntu 24.04. | V5 e catálogo fake; store em memória com ETag; DTO ON/OFF roteado no browser. Confere allowlist, cents positivos, fail-closed, save condicional/readback/revogação e 16 estados de apresentação sem overflow/erros. | #287 acrescentou paths de catálogo/cenas e eliminou filtro de branch temporária. O run `44808609090` passou no head exato `26a2da33`. |
| `vis002c-v03-product-pin.yml` | PR para `main`; paths de CSS/tokens/páginas/fallback/testes/pin. | Verifica pin, fallbacks, build/pages-check e dois testes Playwright de raster. | Blobs pinados, DOM real local, raster legado sintético, mídia YouTube mockada; valida 12 cenários/40 seletores e 16 contextos/152 imagens, área de pixels autorizada e fallback/alt/foco. | #287 inclui `package.json` e `scripts/compile-primary-pages.mjs`; run `44808609027` passou no head exato `26a2da33`. |
| `branch-hygiene.yml` | PR, push em `main`, cron semanal e dispatch. | Planejador Py3.12: unit tests, `py_compile`, observação e plano; upload read-only. | API GitHub + refs locais, dispositions e fixtures sintéticas do planner. Confere inventário/SHA, determinismo e preservação de refs protegidas/PR. Sem comando apply. | O filtro de PR agora enumera `branch_hygiene_apply.py`, `branch_hygiene_observe.py` e `branch_hygiene_plan.py`, que o job compila; evita acordar pelo `branch_hygiene_merged_pr_cleanup.py`, não executado por este job. O push da main permanece sem filtro. Overlap com bounded é deliberado. |
| `branch-hygiene-bounded.yml` | PR lifecycle; push em `main` quando batch muda. | Em PR: discovery tests, `py_compile`, observe/plan e apply audit-only; em main: reobserva, aplica somente batch autorizado, readback; PR merged: cleanup delimitado. | Batch limita 1–3 refs+SHAs; testes de planos, eventos e árvores sintéticas. Mutação exige autorização flag, main SHA e releitura. | Faltava `ops/branch-dispositions.json` em `pull_request.paths`; #286 adiciona. O gate de PR continua audit-only. |
| `flow-layout-browser.yml` | PR, push em `main`, dispatch; filtros dirigidos. | Fixture local V5; `flow-layout-browser.cjs`, `buyer-v5-browser.cjs`, `nav-flow-responsive-crossbrowser.cjs`; Chromium/WebKit. | Defaults projetados como V5; fluxo, panes/dock, ordem grupos/seções, paridade V3/V5 e limites responsivos 700/701 e 1050/1051. | Faltavam nove imports do helper e entradas do build/pages-check. #286 adiciona. |
| `keyboard-browser.yml` | PR, push em `main`, dispatch; filtros dirigidos. | Fixture local V5; `keyboard-browser.cjs`; Chromium. | Setas, Espaço/Enter/Escape/dígitos/Ctrl+setas, foco/scroll e ordem do fluxo normalizado. | Faltavam nove imports, `flow-layout.js` e entradas do build/pages-check. #286 adiciona. |
| `mobile-browser.yml` | PR, push em `main`, dispatch; `app/**`, testes e helpers. | Fixture V5 para PiP; `mobile-pip-main-browser.cjs` e `home-hero-phone-geometry-browser.cjs`. | Perfis empilhado/compacto, PiP, resize, toque, conflitos hit-test, detalhes/swipe; hashes e limites geométricos do hero. | Helper usa build/pages-check, mas filtros omitiam `package.json` e compilador. #286 adiciona. |
| `stone-browser.yml` | PR, push em `main`, dispatch; `app/**`, teste e helpers. | `test-runtime-contracts.js`, fixture V5, `stone-browser.cjs`; Chromium. | Estado legado reparado, toggle pedra/MDF/rodapé, canvas/pixels e ocultação dos hosts. | Helper usa build/pages-check; #286 adiciona `package.json` e compilador ao filtro. |
| `summary-pricing-browser.yml` | PR, push em `main`, dispatch; `app/**`, teste e helpers. | Guards de ownership, `test-core.js`, fixture V5 e `summary-pricing-browser.cjs`; Chromium. | Totais persistidos, subtotal, cobrança global única, remoção/ativação do rodapé e preço da pedra sincronizados. | Helper usa build/pages-check; #286 adiciona `package.json` e compilador ao filtro. |

| `development-ux04-geometry.yml` | `push` apenas em `development` com filtros de arquivo; `workflow_dispatch`. | Unit tests de autoridade, flow/model/hierarchy, `pages:check`; depois build Buyer V5 local, Playwright geometry/focus e keyboard browser. | Fixture V5 local e browser Chromium; publica dois JSONs de resultado com retenção de 14 dias. | Delta live: 22º workflow em `main` após #279. Histórico: run `41344513485` passou em `c7c2822` (2026-11-01); artefatos não estão mais listados. Sem run no `development@be743fd` atual; repetir no SHA live. |

## Síntese

- **21/21 workflows da baseline** têm crosswalk compacto de evento/path → job/comando → fixture → garantia/contrato e disposição de trigger. O novo 22º workflow está documentado separadamente como delta live.
- **Sem conclusão de redundância por contagem.** Preparadores e comandos repetidos são infraestrutura compartilhada ou testes em camadas diferentes; nenhum teste foi removido.
- **#286:** integrado por squash em `development@acf12c41` após 9/9 gates verdes no head da PR; não houve run de Actions no SHA de merge. **#287:** quatro gates verdes no head atual `26a2da33`; ARC-03C tem diagnóstico de baseline no head pai `30db98d7` e não faz parte da diff final.
- #287 remove os triggers temporários e adiciona o Viewer PR gate para `main`; o fluxo ARC-03C permanece inalterado/dormente neste pacote. P-COMP e UX/auth seguem dormentes. Duração comparável e required checks seguem UNKNOWN.
- Amostra da execução nos heads candidatos: 12 gates únicos #286/#287 somaram ~15,7 job-min executados (skips fora); o Flow cancelado ficou 18,28 min instalando browser, sem rodar testes. Total de runner observado incluindo essa tentativa: ~34,0 job-min; Keyboard foi o maior gate concluído (7,53 min). A mistura de PRs/bases não é comparável à baseline histórica de 7,12 job-min e não prova redundância.
- Diagnóstico inicial de #287 no head `30db98d7`: Viewer price falhou antes dos testes por incompatibilidade Ubuntu 26.04/Playwright 1.56.0; o runner foi fixado em 24.04 e o gate passou nos heads posteriores, inclusive no atual. ARC-03C passou build/source e encontrou divergência com a baseline visual antiga; o workflow foi restaurado ao estado de `main` e não foi rerun no head atual.
- Nenhuma assertion foi removida ou enfraquecida. Required checks seguem UNKNOWN; execuções não provam deployment.
