# HANDOVER ATUAL — MobiliPresenter2D + Design System

## Revalidação live — 24/10/2026

Esta seção é o estado atual verificado; os snapshots antigos abaixo permanecem apenas como histórico.

- Produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` inclui ARC-03C/P-COMP-01 via #237.
- PR #238 está DRAFT em `a2835c6`. Gate autenticado passou em `a9129e1`; depois dele mudaram somente dois commits de documentação. Gates anônimo/assets passaram no head atual. #232 permanece aberta até revisão e integração dos workflows legados.
- PR #239 está DRAFT; seis checks passaram e o foco do skip link About foi conferido no preview, sem homologação global.
- Issue #224 continua aberta. Uma passagem em 390×844 no Production `main@5ccb2a8` manteve Lavanderia visível após selecionar grupo 2; não reproduziu a falha uma vez e não fecha a reprodução anterior 4/4.
- PR #51 do Design System permanece aberta e DRAFT; consulte a head live na própria PR. A branch de handover contém inventário ARC-13 atualizado.
- ARC-13: 480 ocorrências/392 valores distintos nas oito entradas HTML, com 464 localizáveis, quatro identificadores excluídos e 12 itens comerciais deferidos. Em JS, o heurístico inicial ligou 2.176 candidatas em 52 fontes; uma busca direcionada por sinks DOM acrescentou cinco rótulos de uma palavra. O índice atual liga e classifica **2.181 referências**: 728 localizáveis, 1.263 técnicas/não localizáveis e 190 itens deferidos (17 de apresentação, 173 autorais/configuráveis/comerciais). Não restam referências indexadas sem classificação, mas a busca direcionada não prova cobertura completa da geração DOM. Os três scripts inline de `app/config/index.html` foram revisados sem literais localizáveis e os dois arquivos de dados grandes sem texto humano. As decisões dos 190 itens, a convenção de chaves, 369 chaves ausentes no índice e 212 sufixos baseados em linha continuam em revisão: cinco chaves ausentes e 13 substituições numéricas têm propostas não canônicas; 364 ausentes e 199 numéricas seguem sem proposta. Não houve extração, migração ou alteração do produto. [Lotes DOM](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json) · [cobertura](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) · [convenção proposta](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json).
- Os projetos Netlify principal e isolado reportam deploy Production READY em `main@5ccb2a8`, com nove Functions e uma Edge Function `access-check` presentes. A leitura não exercitou a chamada da função nem validou valores de ambiente.
- O percentual ~22% é histórico/provisório, sem recálculo por pesos.

### Snapshot histórico — 24/10/2026, 09:35 UTC

O checkpoint a seguir descreve o estado observado naquela hora. Seus SHAs e estados de PR são históricos e foram substituídos pela revalidação acima.

**Estimativa global:** permanece em aproximadamente **22%** conforme o plano canônico. A matriz V5 e o OIDC ganharam evidência técnica, mas as mudanças relacionadas continuam em PRs Draft/stacked; produto `main` ainda é `15e1cfb4866886649adbcd00fef9bef5e5843fda`. Não contar branches ou previews como integração publicada.

### Estado revalidado

- Design System `main`: `ae1be563d298ae4a6d384936cbb2d9d05ee449ae`. Os resultados VIS-002C × P-TOKEN-02B v0.2 abaixo continuam sendo o checkpoint técnico; a reconciliação não autoriza uso global de tokens.
- Produto PR [#231](https://github.com/EAKerber/MobiliPresenter2D/pull/231): P-TOKEN-01B/02B, aberta **DRAFT/HOLD**, head `afb80965336083209eac93e2729de77170524ee5`; está divergente da `main` atual (`15e1cfb`, 24 commits à frente e 4 atrás) e seus cinco checks browser seguem falhando nesse head antigo. A recuperação desses fluxos está em #234/#236, sem alterar #231.
- Produto PR [#234](https://github.com/EAKerber/MobiliPresenter2D/pull/234): ARC-03C, aberta **DRAFT/HOLD**, base `main@15e1cfb`, head `fbd00a9628c81b4902a8c679abb7ac72e93ca549`; fonte autoral/build e `pages:check` presentes, 11 checks documentados PASS.
- Produto PR [#236](https://github.com/EAKerber/MobiliPresenter2D/pull/236): cinco ajustes de testes browser, **DRAFT/HOLD**, empilhada sobre #234 em `b5e06ff030e268fd934835fde1a6b99244908efc`. Diff de cinco arquivos; os cinco fluxos de browser V5 local e o gate de assets passaram (6/6 checks). `pages:check` permanece executável pela base #234.
- Produto PR [#235](https://github.com/EAKerber/MobiliPresenter2D/pull/235): fixture experimental do Deploy Store, fechada **sem merge** após readback/hash V5 e negação anônima.
- A issue [#232](https://github.com/EAKerber/MobiliPresenter2D/issues/232) permanece **aberta**. OIDC autenticado separado passou duas execuções integrais ([#40039686284](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40039686284) e [#40039882104](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40039882104)): Mobile/PiP, Keyboard, Flow, Summary/Preços e Stone 5/5; Admin negado, logout e replay negado. Os workflows antigos ainda precisam chegar à `main` com a separação entre fixture local positiva e teste anônimo negativo.

### Próximo passo e limites

Revisar a dependência #234 → #236 e a CI do head atual. Manter #231, #234 e #236 em DRAFT/HOLD; não integrar ou publicar sem decisão explícita. Não abrir outro preview para reproduzir os gates já aprovados, não reusar convites antigos e não declarar #232 resolvida enquanto a cobertura migrada não estiver integrada e lida de volta na `main`.

---


> **VIS-002C × P-TOKEN-02B v0.2 — RECONCILIAÇÃO TÉCNICA PASS (23/10):**
> [Actions #39894163198 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39894163198)
> na branch isolada produto [`integration/vis002c-p-token-02b-v2-20261023@34a305c`](https://github.com/EAKerber/MobiliPresenter2D/tree/integration/vis002c-p-token-02b-v2-20261023).
> **48/48** equivalências exatas entre v0.1/v0.2 para os três consumidores antigos;
> **36/36** cenários de contraste e **72** verificações de pares; 424 medições
> conformes, **0 abaixo**, 32 `UNVERIFIED`; **12/12** pares full-page,
> **90.315 pixels alterados e nenhum fora dos cinco textos aprovados**.
> O [mapeamento DS v0.2](VIS002C_CONTEXTUAL_MAPPING_V0_2_0.json) define oito
> contextos sem duplicar a cor homologada em `VIS-002`; pin Git SHA, CSS
> gerado v0.2 e versão v0.1 histórica preservados. **Sem uso global de token**.
> PR #231 original continua DRAFT e não foi reescrita; a integração v0.2
> é derivada dela. PR #234 DRAFT e issue #232 de CI autenticado continuam HOLD.
> **Sem PR nova, Netlify Preview, merge ou publicação.**
> [Gate, proveniência e próximos bloqueios](VIS002_PUBLIC_TEXT_CONTRAST_APPLICATION_RULE_2026-10-22.md).

> **VIS-002C — gate visual full-page PASS, integração ainda HOLD (23/10/2026):**
> [Actions #39891404267](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39891404267)
> concluiu **12/12 pares full-page** (Landing/About/Como funciona × 390/1366
> × Chromium/WebKit, light), com **90.315 pixels alterados, zero fora dos textos
> homologados**, sem mudança de geometria. Repassou **36/36 cenários** de
> contraste, 72 checagens de pares e 0 violações entre 424 medições confirmadas;
> 32 casos continuaram `UNVERIFIED`. Produto branch `fix/vis002c-public-text-contrast-20261022@007fc8e`.
> A [PR #231](https://github.com/EAKerber/MobiliPresenter2D/pull/231) também
> edita as três CSS e já possui token contextual DS gerado; conciliar as fontes
> quando ela for integrada, sem duplicar autoridade. PR #234 e CI privado #232
> seguem independentes em HOLD. [Evidências e roadmap](VIS002_PUBLIC_TEXT_CONTRAST_APPLICATION_RULE_2026-10-22.md).
> **Sem PR nova, preview, merge ou release da VIS002C.**

> **VIS-002C — DECISÃO CONTEXTUAL E IMPLEMENTAÇÃO ISOLADA (23/10):**
> O usuário autorizou aplicar a cor secundária homologada `#705C4B` aos
> cinco contextos de leitura que falhavam por reutilizar `--public-muted`.
> [Contrato fail-closed e escopo homologado](VIS002_PUBLIC_TEXT_CONTRAST_APPLICATION_RULE_2026-10-22.md),
> sem mudança de `decisions.json` ou quebra do hash de exportação P-TOKEN-01.
> Produto [branch `fix/vis002c-public-text-contrast-20261022@b0eb52f`](https://github.com/EAKerber/MobiliPresenter2D/tree/fix/vis002c-public-text-contrast-20261022):
> três arquivos CSS de páginas alterados, sem globals/auth/Viewer/V5, com
> [CI #39890589800 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39890589800)
> nos jobs CSS contract e navegador: **36/36 cenários**, **72 pares verificados**,
> **456 medições (424 PASS, 0 abaixo do limiar, 32 não verificadas)**.
> Workflow preparado para ser gate de PR/main após integração, sem congelar
> alterações CSS independentes. **Ainda sem PR, preview, merge nem produção**;
> não confundir o PASS técnico em branch com homologação global da interface.

> **AUDIT-PUBLIC-TEXT-02 — gate diferencial PASS; homologação visual ainda HOLD (23/10/2026):**
> [GitHub Actions #39888294326 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326),
> branch isolada `audit/public-text-contrast-coverage-20261022@ace8510`.
> Testes de CSS candidato injetado: **36/36 cenários**, 36 elementos light corrigidos,
> 36 elementos dark sem alteração, **84 controles negativos inalterados**, 10 pares
> de capturas antes/depois. Contrastes previstos/computados: 4,9534:1
> em `#E8E3DC` e 5,4146:1 em `#F0EDE8`; `--public-muted` intacto.
> Os primeiros fails eram instrumentação/animação e a inclusão incorreta
> de `.finish-signature`, cujo tom próprio deve ser preservado.
> O CSS experimental permanece fora de `app/`, sem PR, preview, merge ou release.
> **VIS-002 não foi ampliado: cinco novos contextos continuam SEM HOMOLOGAÇÃO VISUAL**.
> [Checkpoint, rollback e caveats de screenshot](PUBLIC_TEXT_CONTRAST_CANDIDATE_2026-10-22.md).

> **Auditoria de contraste público concluída (22/10):**
> [Actions #39883740485 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39883740485),
> branch isolada `audit/public-text-contrast-coverage-20261022@35d9c22`,
> **36/36 cenários; 456 medições**, 388 acima do limiar, 36 abaixo em **cinco contextos**
> (`/ .story-section`, `/ .feature-copy`, `/about/ .about-closing`,
> `/about/ .about-scale__stat`, `/how-it-works/ .finish-copy`) e 32
> não verificadas. **36/36 checagens de pares já homologados PASS**.
> Nenhum CSS/HTML alterado; nenhuma PR/preview/merge.
> [Relatório com seletores, contraste e limites](PUBLIC_TEXT_CONTRAST_AUDIT_2026-10-22.md).
> Não expandir VIS-002 automaticamente: próximo gate exige aprovação contextual dos novos pares.

> **RETOMADA MAIS RECENTE — ARC-03C (22/10/2026):** no produto, a branch
> [architecture/arc03c-static-page-build-20261022](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/arc03c-static-page-build-20261022)
> implementou fonte autoral única das três páginas primárias, outputs estáticos rastreados em app/,
> manifesto de hashes e checagem fail-closed antes do build Netlify real. O gate isolado
> [Actions #39871907031 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39871907031)
> passou **60/60 Chromium/WebKit com zero diferenças de raster** contra o HTML imutável main@303468b,
> além de testes de tampering, build e controle de escopo. O primeiro run #39871724976
> falhou antes do browser por safe.directory no container; correção no commit 4318e81 e rerun verde.
> [Checkpoint detalhado no produto (branch)](https://github.com/EAKerber/MobiliPresenter2D/blob/architecture/arc03c-static-page-build-20261022/docs/architecture/arc03c-source-authority-and-netlify-build-2026-10-22.md).
> **Integração atual (22/10): [PR #234 DRAFT/HOLD](https://github.com/EAKerber/MobiliPresenter2D/pull/234)** em `8ab231761e8e0e3d9fe4b6e6eabec2e565cc27e7`; preview Netlify [#234](https://deploy-preview-234--mobilipresenter2d.netlify.app/) **READY**, deploy `6adab05d4044efc65ed6660b`, único preview criado. Não houve merge nem release. Gates de build purity, assets, variantes e contrato público estático PASS, mas os gates de navegador protegido Mobile/Stone/Keyboard e smoke público com pressuposto de `/config/` público falharam reproduzindo as assinaturas da issue #232, já classificadas como falta de sessão; Flow e Summary também finalizaram em FAILURE por timeout de readiness em `/config/` anônimo. **9/9 workflows encerrados**: build purity, assets e variantes PASS; Mobile, Stone, Keyboard, Flow, Summary e Public routing browser FAIL; job público estático PASS. **NÃO mascarar estas falhas; manter HOLD até fixture autenticada independente**.
> A PR #231 continua HOLD e
> a issue #232 ainda exige fixture autorizada para testes privados. Próximo gate: revisão de integração
> do ARC-03C e CI aplicável, sem liberar /config/ nem presumir homologação de produção.


**Data da fotografia:** 22/10/2026 (America/Sao_Paulo). **Autoria:** checkpoint de consolidação baseado em leitura real de branches, PRs, issues e runs GitHub, e não só na memória do chat.

**Este é o primeiro documento para retomar a consolidação arquitetural.** O ponto de entrada recíproco do produto está em [`MobiliPresenter2D/docs/handoffs/ARCHITECTURE-CURRENT-2026-10-22.md`](https://github.com/EAKerber/MobiliPresenter2D/blob/main/docs/handoffs/ARCHITECTURE-CURRENT-2026-10-22.md). É mais recente que as instruções operacionais de 08–12/10 existentes em `CURRENT_STATE.md` e antigos handovers; conservar esses textos como histórico, mas não restaurar planos superados.

## Repositórios e baseline atual

| Autoridade | HEAD observado em 22/10, antes de registrar estes arquivos | Responsabilidade |
|---|---|---|
| **Produto** `EAKerber/MobiliPresenter2D` | `main@303468b4ddbb07a761316abca28901ccaea219df` **antes da documentação deste handover**; o único conteúdo runtime desde o baseline `840a0cd` permanece igual. Um novo commit de documentação será adicionado e deve ser lido por HEAD live | Código HTML/CSS/JS Vanilla, `app/`, build/Netlify, Core V5/Viewer e testes |
| **Design System** `EAKerber/MobiliPresenter2D_DesignSystem` | `main@5ba1137721ad056bee82da9615f3e24eda192699` **antes deste handover**; será atualizado por commits de documentação | `decisions.json` visual, contratos ARC, geração de tokens aprovados, inventários e checkpoints |

**Autoridade arquitetural:** [ARC-01…16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md) — componentes vanilla com especialização por papel, DSL/data-driven só onde o domínio exige, headers via fragmentos **estáticos de build**, paleta DS aprovada com export determinístico e pinado, testes por risco e equivalência visual.
**Autoridade visual:** `decisions.json`, especialmente NAV-004, NAV-005, VIS-002, VIS-003 e EST; contratos arquiteturais não são automaticamente uma homologação estética.

## Resultado mais recente: ARC-03B passou, produção ainda não foi migrada

A branch de produto [`architecture/arc03-primary-header-fragment-prototype-20261022`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/arc03-primary-header-fragment-prototype-20261022) no commit **`e459b9bd85c4e9c8bb96813ae6758789de75dc13`** contém:
- um fragmento HTML único para **headers públicos primários**;
- mapa explícito das variantes/links/ARIA de Landing, About, Como funciona;
- três arquivos de **autoria** separados em `architecture/pages`, com slot de header;
- compilador determinístico `scripts/compile-primary-pages.mjs`, emitindo **somente** `artifacts/arc03b/pages` e manifesto de hashes;
- gates Node + **60/60** comparações de DOM/CSS/posicionamento/screenshots em **Chromium/WebKit × 5 larguras (320/390/486/768/1366) × 2 temas × 3 páginas**;
- comparação independente de Git provando ausência de alteração em `app/`, `netlify.toml`, `package.json`, `netlify/`; Viewer NAV-005 excluído.

**Gate final [Actions #39867859774 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39867859774)**, com **0 divergências de pixels**. O run anterior [#39867401114](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39867401114) teve 60/60 nos browsers mas falhou porque invocou `git diff` em container sem checkout Git disponível; corrigido com um job runner separado, **sem tocar no runtime**.

[Documento analítico e instruções ARC-03B](ARC03B_AUTHORED_PAGES_STATIC_COMPILER_BROWSER_GATE_2026-10-22.md).

**Não houve cutover de produção nem execução do compilador no `npm run build` efetivo.** A duplicação temporária de HTML de autoria entre `architecture/pages` e `app/` é **aceitável apenas durante POC**, não pode tornar-se permanente. O próximo incremento é **ARC-03C**: integração source→generated com autoridade unívoca no build Netlify `publish=app`, preservação de Admin/Viewer/Config/Acesso e gates browser idênticos. **Não confundir o build experimental `app/dist` com a pasta realmente publicada.**

## Outras frentes: status e gates

| Frente | Realizado | Limite / próxima ação |
|---|---|---|
| **Decisões ARC** | **16/16** homologadas quanto à arquitetura, com compromisso ARC-13 amplo e ARC-16 gates reais | Não converter em aprovação visual genérica |
| **V0-A/V0-B** | Matriz de componentes, proprietários, 54 JS contabilizados, 84 classes CSS lexicais repetidas e lacunas de localização | Não alegar i18n completo, CSSOM/DOM universal ou 84 bugs |
| **P-COMP-01** | Branch produto `architecture/p-comp-01-public-menu-20261021@4ba9384`, [Actions #39697470826 PASS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39697470826): 40 visuais, 16 funcionais, 20 Viewer NAV-005 | Sem merge; branch **1 commit atrás** da `main` após #233; integrar separadamente de ARC-03C |
| **P-TOKEN-01A** | [DS PR #49 MERGED](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/49), fonte VIS-002 executável, manifestos gerados e pino de proveniência | Padrão de paleta é **referência**, não alias global automático |
| **P-TOKEN-02B DS** | [DS PR #50 MERGED](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/50), apenas três textos `#705C4B` em contexto VIS-002 light | Não generalizar para backgrounds, estados ou Viewer |
| **P-TOKEN-01B/02B produto** | [PR #231 DRAFT](https://github.com/EAKerber/MobiliPresenter2D/pull/231), branch `architecture/p-token-02b-contextual-copy-20261022@afb8096`; [48/48 PASS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39780241560), zero diffs | Não integrado; branch **1 commit atrás** da main; CI geral/auth ainda bloqueiam revisão para merge; preview #231 foi gerado uma única vez |
| **CI-BASELINE-01 / #233** | [Issue #233 CLOSED](https://github.com/EAKerber/MobiliPresenter2D/issues/233), assertions públicas corrigidas em produto `main@303468b`, com testes de domínio em [#39848703737 PASS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39848703737) | Não reaplicar da branch antiga; código V5 de runtime não modificado |
| **CI-BASELINE-01 / #232** | [Issue #232 OPEN](https://github.com/EAKerber/MobiliPresenter2D/issues/232); [#39849284220](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39849284220) confirmou que usuários anônimos em `/config/` são enviados a `/access/` (produção e preview) | **PENDÊNCIA EXPLÍCITA**: fixture autorizada de sessão limitada/segura para testes de /config. Não abrir rota ou desabilitar checks |
| **ARC-13 i18n** | Inventário de candidatos e blind spots no DS | Scanner AST e migração gradual; UI versus dados comerciais/domínio separados |

A PR #231 ficou em **DRAFT/HOLD**, pois seus testes restritos de tokens passaram, mas workflows gerais de mobile/keyboard/flow/summary/stone tentam exercer `/config/` sem sessão e falham. A correção de contrato público #233 já entrou na main, mas isso **não torna os testes autenticados verdes**. A política é **não mascarar falhas nem mergear sem gates adequados**.

As issues #212/#213/#222 e pendências de publicação/Viewer da #228/#229 seguem abertas no tracker; não inferir que sua implementação necessariamente está ausente — conferir código atual e validação antes de resolver. PRs DS #39/#41 continuam draft e não devem ser fundidas em bloco. No produto há PRs CP-PUBLIC antigas em HOLD: só considerar mediante reconciliação explícita.

## Próxima execução técnica (quando o usuário pedir prosseguimento)

**Prioridade: ARC-03C independente da fixture de auth.**

1. Checar novo HEAD do produto e do DS. Ler este handover, [ARC-03B](ARC03B_AUTHORED_PAGES_STATIC_COMPILER_BROWSER_GATE_2026-10-22.md), `architecture/pages` e `scripts/compile-primary-pages.mjs` na branch `architecture/arc03-primary-header-fragment-prototype-20261022`, e `package.json`/`netlify.toml` da main.
2. Definir **uma fonte autoral**: build determinístico leva fontes `architecture/pages` ao output publicado em `app/` (sem sobrescrever código/manual silenciosamente); manifesto de entradas/saídas, verificação `--check` para drift e rollback. Não introduzir framework, SSR ou engine de página universal.
3. Preservar os três headers exatamente e manter Viewer com seu header NAV-005 diferente. Não unir com P-COMP-01, P-TOKEN, mudanças de preço ou alterações auth.
4. Revalidar no build real: 3 páginas × 5 larguras × 2 temas × Chromium/WebKit, menus fechado/aberto, foco teclado, navegação, CSSOM e screenshot. Inspecionar rotas não afetadas como controles negativos.
5. Só abrir PR de produto se a mudança/validação exigir revisão de integração; evitar várias prévias Netlify. Não declarar produção concluída sem merge, CI requerido e readback do deploy.
6. Continuar a registrar checkpoints aqui e no ponto de entrada do produto; issue #232 permanece bloco de testes privados separado.

**Parada:** prova de compilador não substitui integração nem homologação de publicação. A solicitação "prossiga" habilita execução incremental governada por gates, não autoriza remover controles de acesso, modificar preços comerciais ou tomar decisões estéticas adicionais.

## Estimativa de programa (com ressalvas)

**~22% de trabalho ponderado concluído**, ante ~15% no relato anterior (**+7 pontos percentuais**), plausível **18–25%**. Ações executadas em branches e gates reduzem incerteza e esforço futuro, mas não representam a mesma porcentagem publicada em `main`. A infraestrutura e decisões estão à frente da adoção visual no produto.

**Resumo de segurança:** nenhuma nova publicação de V5, schema, identidade, dados comerciais ou config privada foi feita por estes incrementos de arquitetura. A homologação visual continua dependente de `decisions.json`; `viewerPricePublication` somente sob controle explícito e inicialmente desligado.


## Evidência runtime adicional — Preview #234, 24/10

A auditoria somente de leitura no Deploy Preview #234, commit `fbd00a9`, confirmou as rotas públicas em contexto isolado, tema claro/escuro e preferência por movimento reduzido. Não houve overflow horizontal no recorte; 28/28 imagens de “Como funciona” carregaram após scroll. `/config/` redirecionou para `/access/` sem token. O foco de teclado medido diverge do registro do Design System em espessura e cor clara; os limites completos estão em [RUNTIME_AUDIT.md](../RUNTIME_AUDIT.md) e [runtime-evidence.json](../runtime-evidence.json). Isso não é auditoria de produção, homologação nem integração.


A inspeção adicional do menu público em 390 × 844 escuro mostrou que Escape não o fechou em duas tentativas enquanto o foco permanecia no controle. O resultado foi registrado como observado somente no Preview #234; clique externo e produção continuam sem conclusão.


### Diagnóstico do menu público — preview #234

O evento Escape chega à página, mas a implementação ativa `landing.js` não o trata: o preview não carrega `header-menu.js`. O ramo experimental P-COMP-01 em `4ba9384` tem o handler e gate PASS; permanece fora de PR/merge. Como ele difere da base atual em 13 arquivos e altera saídas HTML, a adoção exige reconciliação com ARC-03C e novo `pages:check`; não reapliquei o ramo antigo.


### Evidência de atualização do inventário de localização — 24/10/2026

Os índices heurísticos V0-A existentes foram gerados contra produto `840a0cda`: somam 826 ocorrências candidatas em 26 fontes, com ressalvas explícitas de falsos positivos e cobertura incompleta. Comparei os hashes das 26 fontes com produto `main@5ccb2a8`: 19 ainda coincidem e 7 divergem (quatro HTML e três JS). A árvore atual tem 744 arquivos rastreados, incluindo 8 entradas HTML e 77 arquivos JS sob `app/` (entre eles testes e módulos de dados). Esses números definem o universo a classificar; **não** são contagem de strings localizáveis nem prova de cobertura. O próximo gate ARC-13 é revarrer fontes atuais, separar código de UI, testes, conteúdo comercial/autoria V5 e identificadores, e registrar linha/consumidor/chave/status antes de qualquer extração para bundles.


### Primeiro lote de extração estática ARC-13 — 24/10/2026

Foi produzido [arc13-static-html-candidates-main-2026-10-24.json](../evidence/architecture/arc13-static-html-candidates-main-2026-10-24.json) sobre as oito entradas HTML do produto `main@5ccb2a8`: **480 ocorrências / 392 valores distintos**, todas marcadas `candidate-unreviewed`, com arquivo, linha e rota. Isto é um índice lexical de candidatos, não cobertura final nem autorização para trocar textos. Os três blocos JavaScript embutidos em `app/config/index.html` (2.343 bytes no total), módulos JavaScript externos, mensagens geradas no DOM, dados comerciais/autoria V5 e textos CSS continuam fora deste lote. A classificação de dono e chave semântica permanece pendente. Próximo recorte: rastrear strings nos módulos de UI/runtime e nos scripts inline, mantendo catálogo/modelos V5 e identificadores fora do bundle localizável.


### Varredura lexical das fontes JavaScript — 24/10/2026

O segundo recorte ARC-13 está em [arc13-runtime-js-candidates-main-2026-10-24.json](../evidence/architecture/arc13-runtime-js-candidates-main-2026-10-24.json), pinado em `MobiliPresenter2D@5ccb2a8`. Foram lidas **52 fontes JS de runtime**, excluindo 23 testes/ferramentas e deixando para exame separado `app/data/mask-data.js` e `app/data/stone-data.js`. A heurística encontrou 4.752 literais e marcou 2.176 ocorrências (1.466 valores distintos) para triagem. O arquivo contém hashes por fonte, linha, texto candidato, consumidor/owner ainda não atribuídos e status não revisado; um literal longo está truncado e marcado. Não é contagem final de strings localizáveis: comentários são ignorados, mas regex literals, templates interpolados, escapes JS, dados carregados e conteúdo DOM exigem revisão adicional. Os três scripts inline de `app/config/index.html` também seguem fora do lote.

**Estado ARC-13:** cobertura bruta já começou em HTML e JS, mas a condição de saída permanece distante: classificar cada texto por owner/consumer e semântica, excluir identificadores/mensagens técnicas e dados comerciais/autoria V5, atribuir chaves, cobrir fontes inline/runtime que faltam e fechar exceções explícitas antes de qualquer migração de bundle.


### Primeira classificação manual ARC-13 — 24/10/2026

[arc13-classified-ui-js-batch-2026-10-24.json](../evidence/architecture/arc13-classified-ui-js-batch-2026-10-24.json) registra **27 entradas localizáveis** em três fontes atuais: controlador compartilhado de tema, confirmação de acesso e gerenciador de convites/acessos. Cada entrada tem chave semântica proposta, texto pt-BR atual, linha/blob de origem, consumer/owner e, quando aplicável, parâmetros dinâmicos. IDs de papel, email inserido pelo usuário, endpoints, códigos de erro internos e datas como dado ficaram fora. A classificação vale só para esses três arquivos, ainda é inventário documental e não introduziu bundle nem alterou o produto. Próximo: revisar as famílias de strings do Configurador/Admin e Viewer, mantendo conteúdo comercial V5 e textos autorados separados.


### Classificação de strings do Viewer e detalhes técnicos — 24/10/2026

[arc13-classified-viewer-configurator-batch-2026-10-24.json](../evidence/architecture/arc13-classified-viewer-configurator-batch-2026-10-24.json) classifica **33 entradas** com **41 referências de origem** em `app/viewer/technical-views.js`, `app/core/technical-drawings.js`, `app/core/scene-component.js` e no carrossel de detalhes de `app/app.js`. Inclui captions e notas de desenhos, dimensões, descrições acessíveis e navegação do carrossel. Campos de título/referência/segmentos e medidas continuam como parâmetros de domínio; o texto e a acessibilidade recebem as chaves candidatas. Os símbolos L/A/P e `mm` ficam marcados como rótulos/formato de domínio para revisão, em vez de serem traduzidos por inferência. A classificação é documental e focada neste subconjunto; nenhum código do produto foi alterado.


### Readback da fixture auth CI e previews — 24/10/2026

- PR produto #238 tem Deploy Previews READY, head `a2835c6`: [mobilipresenter2d](https://deploy-preview-238--mobilipresenter2d.netlify.app/) e [m2d-auth-ci-isolated](https://deploy-preview-238--m2d-auth-ci-isolated.netlify.app/). O segundo é o host dedicado previsto no workflow; o deploy Production em `main@5ccb2a8` é separado e não substitui esses previews.
- Leitura de nomes/escopos, sem registrar valores: no projeto Netlify `m2d-auth-ci-isolated`, `DATABASE_URL` e `ACCESS_GATE_SECRET` estão presentes em Deploy Preview e Production (também nos demais contextos listados). As funções de acesso atuais leem essas duas chaves; `ACCESS_PUBLIC_ORIGIN` não aparece como requisito nesse caminho. A leitura não valida conectividade DB nem se os segredos dos diferentes contextos são iguais/diferentes.
- No head atual de #238 há somente o workflow anônimo e os gates de assets concluídos; não há execução do workflow autenticado. Esse workflow é manual e lê a environment do **GitHub Actions** `ci-auth-isolated`: variable `CI_STAGING_SUPABASE_REF` e secret `CI_STAGING_DATABASE_URL`. Esses nomes não são substituídos pelas variáveis do Netlify. A leitura dessas environments não é exposta pelo conector atual; portanto, a existência dos dois valores no GitHub permanece **UNKNOWN** até readback ou execução do gate.
- Próxima etapa da fixture: confirmar/adicionar esses dois valores no caminho `Repository → Settings → Environments → ci-auth-isolated`, depois executar o workflow `CI-BASELINE-01 isolated authenticated Config` manualmente na branch da PR #238. Não inserir os valores no repositório, workflow log ou conversa.


### Classificação estática de “Quem somos” — 24/10/2026

[arc13-classified-static-about-batch-2026-10-24.json](../evidence/architecture/arc13-classified-static-about-batch-2026-10-24.json) classifica manualmente as **44 ocorrências** do inventário lexical de `/about/` (**42 valores distintos**), com chave semântica, arquivo/hash/linha, consumidor e owner. Inclui título e descrição da página, navegação, nomes acessíveis, texto editorial e rodapé. O nome de marca foi preservado como conteúdo de marca. Segmentos de texto separados por nós HTML continuam separados no inventário; a extração futura precisa permitir recomposição e ordem de frase por idioma. É evidência documental, sem alteração no produto nem bundle de tradução. As outras sete páginas e as demais fontes ARC-13 continuam em aberto.

### Atualização de CI de autenticação — 24/10/2026

O run autenticado [#40075575871](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40075575871) terminou **SUCCESS** na revisão `a9129e11afeae6e92fa8a9dda88f44e01c385c8a`. A head atual de #238 é `a2835c6fe92abdd3649e169231d05090172518ee`; a comparação entre as duas revisões mostra somente dois commits e um arquivo de documentação de handoff alterado, sem mudanças de código/workflow depois do gate. Portanto o resultado cobre o código funcional atual da PR. Os gates anônimo e assets também passaram em `a2835c6` (#40081895237 e #40081898326). A issue #232 ainda depende de revisão/integracão do PR; #238 segue DRAFT. O sucesso comprova que o GitHub Environment tinha os valores necessários durante aquela execução, sem expor nem validar o valor de segredo em si.


### Classificação estática do Viewer — 24/10/2026

[arc13-classified-static-viewer-batch-2026-10-24.json](../evidence/architecture/arc13-classified-static-viewer-batch-2026-10-24.json) classifica **17 ocorrências / 16 valores distintos** da entrada HTML de `/viewer/`, cobrindo metadados, navegação, rótulos da cena, instrução e acessibilidade. O conteúdo dinâmico de módulos, modelos e dados técnicos permanece separado como dado/domínio. É inventário documental; nenhum texto ou runtime do produto mudou.

### Readback dos deploys Netlify após a ação do usuário — 24/10/2026

O deploy atualmente publicado no projeto principal `mobilipresenter2d` está **READY**, contexto Production, branch `main`, commit `5ccb2a8`; o deploy isolado `m2d-auth-ci-isolated` também está **READY** em Production e no mesmo commit. O readback dos dois informa 9 Functions e 1 Edge Function implantadas, incluindo `access-check`. Isso confirma o estado do deploy e a presença do handler no pacote publicado; não foi feito teste de chamada da função nem validação dos valores de ambiente. As páginas principais seguem na main já integrada; a inspeção não publicou mudanças de código.


### Classificação estática das páginas de acesso — 24/10/2026

[arc13-classified-static-access-batch-2026-10-24.json](../evidence/architecture/arc13-classified-static-access-batch-2026-10-24.json) classifica **33 ocorrências / 27 valores** em `/access/` e `/access/manage.html`: títulos, navegação, acessibilidade, política de acesso, login e controles estáticos. Estados de grant, datas de expiração, papéis e mensagens do servidor ficam fora deste recorte. Somando os três lotes HTML documentados, são **94 ocorrências / 75 valores distintos entre lotes** nas páginas About, Viewer e Access. Ainda é inventário documental; sem alteração no produto ou criação de bundles.


### Classificação estática da página Admin — 24/10/2026

[arc13-classified-static-admin-batch-2026-10-24.json](../evidence/architecture/arc13-classified-static-admin-batch-2026-10-24.json) revisa as **68 ocorrências** de `/admin.html`: 64 textos de interface foram classificados como localizáveis; quatro valores internos (`admin`, `custom`, `finishes`, `services`) foram excluídos como identificadores estáveis. A classificação não altera a interface nem traduz conteúdo comercial do catálogo. O lote permanece documental.

**Cobertura ARC-13 estática registrada até aqui:** cinco rotas e **162 ocorrências / 129 valores distintos entre lotes**, com 158 textos de interface classificados e quatro identificadores excluídos. Restam quatro entradas HTML no índice, scripts inline, conteúdo de runtime e revisão de dados/autoria comercial antes da extração.


### Classificação estática do Configurador — 24/10/2026

[arc13-classified-static-config-batch-2026-10-24.json](../evidence/architecture/arc13-classified-static-config-batch-2026-10-24.json) revisa as **45 ocorrências** estáticas de `/config/`: 37 controles/instruções foram classificados como localizáveis; oito trechos sobre políticas e serviços comerciais foram mantidos em revisão de ownership até confirmação da fonte canônica V5/catálogo. Scripts inline e textos gerados pelo runtime continuam fora deste lote. Sem alteração no produto.

**Cobertura estática classificada/documentada até aqui:** seis das oito entradas HTML; **207 ocorrências / 165 valores distintos entre lotes**, sendo 195 localizáveis, quatro identificadores não localizáveis e oito itens comerciais deferidos. Permanecem sem classificação estática a landing `/` e `/how-it-works/`; a extração integral ainda depende de completar essas rotas, inventário JavaScript/inline e exceções de dados.


### Classificação estática da landing — 24/10/2026

[arc13-classified-static-landing-batch-2026-10-24.json](../evidence/architecture/arc13-classified-static-landing-batch-2026-10-24.json) classifica **44 ocorrências / 38 valores** da página inicial, incluindo metadados, navegação, chamadas de ação, acessibilidade, benefícios e fallback do carrossel. A ordem das chaves foi conferida com os consumidores do HTML; conteúdo gerado pelo runtime segue pendente.

**Cobertura de inventário HTML:** sete das oito entradas, **251 ocorrências / 191 valores distintos entre lotes**; 239 textos de interface classificados, quatro identificadores excluídos e oito itens comerciais aguardando ownership. A entrada `/how-it-works/` permanece pendente. Também faltam scripts inline, mensagens de runtime e revisão dos lotes JS restantes.


### Índice HTML reconciliado — 24/10/2026

O índice [arc13-static-html-candidates-main-2026-10-24.json](../evidence/architecture/arc13-static-html-candidates-main-2026-10-24.json) agora liga as 480 ocorrências às classificações documentadas por rota: **464 localizáveis, quatro identificadores excluídos e 12 itens comerciais deferidos**; os **392 valores distintos** do inventário foram preservados. O HTML estático das oito rotas foi coberto. A condição ARC-13 não está concluída: fontes JS e scripts inline ainda exigem classificação, e os 12 itens deferidos precisam de owner canônico antes de eventual extração.


### Classificação JS de baixo volume — 24/10/2026

[arc13-classified-js-low-volume-batch-2026-10-24.json](../evidence/architecture/arc13-classified-js-low-volume-batch-2026-10-24.json) revisa **65 ocorrências candidatas em 22 fontes**: nove mensagens/rótulos da interface receberam chaves; 54 literais de código, schema, CSS/geométricos ou diagnóstico interno foram excluídos; dois valores de preço/aviso comercial permanecem deferidos. O lote cobre arquivos com até oito candidatos, fixados por blob e linha; não representa a revisão dos 52 arquivos nem a completude do scanner.


### Revisão dos scripts inline do Configurador — 24/10/2026

O arquivo [`arc13-classified-inline-config-scripts-2026-10-24.json`](../evidence/architecture/arc13-classified-inline-config-scripts-2026-10-24.json) registra os três blocos inline de `app/config/index.html` no produto `main@5ccb2a8`, hash `97c284c9831de05607ede0d024e4d919a898b7fa`, totalizando 2.343 bytes. Os blocos tratam de redirecionamento de hash de autenticação, escolha inicial do perfil de layout e controle de ponteiro para redimensionar a cena mobile; não há literais de interface a extrair. Este recorte está fechado para esse hash. Conteúdo gerado no DOM e strings de dados seguem fora dessa revisão.


### Revisão de dados grandes ARC-13 — 24/10/2026

O arquivo [`arc13-classified-large-data-files-2026-10-24.json`](../evidence/architecture/arc13-classified-large-data-files-2026-10-24.json) registra a inspeção integral dos blobs de `app/data/stone-data.js` e `app/data/mask-data.js` no produto `main@5ccb2a8`. As 52 strings de `stone-data.js` são chaves de estrutura/visibilidade ou payloads de imagem; as 47 de `mask-data.js` são `use strict`, caminhos de máscara e payloads de imagem. Nenhuma é texto humano a extrair. A conclusão vale somente para os hashes registrados.


## Consolidação revalidada — 24/10/2026

Base do produto: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; Production Netlify `6adc221479c773577ed45e23` READY. Este resumo complementa a linha do tempo acima; não substitui os registros históricos de cada gate.

- **ARC-13:** 480 ocorrências HTML/392 valores distintos: 464 localizáveis, 4 identificadores excluídos e 12 itens comerciais deferidos. O índice JS começou com 2.176 candidatos heurísticos em 52 fontes; a varredura direcionada de sinks textuais nos mesmos 52 blobs (todos com hash correspondente) encontrou cinco rótulos de uma palavra fora da heurística. O índice passou a ligar e classificar 2.181 referências: 728 textos de interface, 1.263 itens técnicos e 190 itens de conteúdo/domínio deferidos. O lote suplementar [`arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json`](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json) descreve os cinco rótulos e os limites da busca direcionada; ela não certifica cobertura completa de toda construção DOM. Os três scripts inline de `app/config/index.html` foram revistos (2.343 bytes; zero texto localizável). `stone-data.js` e `mask-data.js` foram revisados nos hashes registrados (zero texto humano). A checagem de chave semântica encontrou 369/728 ocorrências localizáveis sem chave e outras 212 com identificadores terminados no número da linha, ainda não considerados estáveis. Cinco rótulos administrativos receberam propostas contextuais separadas, não canônicas, e o índice permanece sem alteração. Permanecem a descoberta de outros caminhos de texto gerado no DOM, ownership dos itens deferidos, convenção de chaves estáveis, extração e migração. Registros: [cobertura](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) e [propostas](../evidence/architecture/arc13-semantic-key-proposal-admin-sinks-2026-10-24.json).
- **DS-05:** DS-05A continua incompleto. O workflow autenticado da PR produto #238 passou e a fixture abre `/config/`, confirma o workspace e revoga a sessão, mas não verifica DOM do contador nem da barra de preço/próxima etapa. A mesma fixture exige 401/403 de `/api/admin-bootstrap`, portanto não valida opções do Admin. Registro: [limite da fixture autenticada](../evidence/runtime/ds05a-ci-auth-fixture-limit-2026-10-24.md). Os dois alvos do Config podem ser acrescentados à observação da fixture existente; as opções do Admin ainda exigem sessão administrativa de teste ou fixture separado explicitamente autorizado. DS-05B/DS-05C também seguem pendentes. Não ampliar permissões do papel `access_ci_fixture` por inferência.
- **NAV-004/menu público:** em Production `main@5ccb2a8`, um percurso móvel 390×844 validou Tab/Enter para abrir, foco no primeiro link, navegação por Tab, fechamento por Escape com retorno de foco e fechamento por clique externo. O menu e o botão não tinham animação em execução com movimento reduzido. Esta amostra não cobre todos os estados/temas. [Evidência](../evidence/runtime/public-menu-production-escape-2026-10-24.md).
- **NAV-005 / issue produto #218:** a composição compacta foi simulada sem alteração de código e documentada em [evidência temporária](../evidence/runtime/nav005-public-compact-header-proposal-2026-10-24.md). A decision canônica continua com `implementationAuthorized: false`; implementação, homologação visual completa e fechamento da issue não foram feitos.
- O arquivo original HTML v0.2 e o inventário original de 43 famílias ainda não estão importados neste repositório. A lacuna de recuperação permanece aberta; nenhuma fonte ausente foi reconstruída por inferência.
- Nenhuma execução desta revalidação alterou código/runtime do produto, variáveis/secrets, sessão de conta ou produção. A estimativa geral aproximada de 22% continua histórica/provisória; sem pesos definidos, não foi recalculada.



- **About / link de salto:** na Production `main@5ccb2a8`, Enter no link atualiza a âncora para `#main`, mas o foco termina no body. PR produto #239 corrige apenas o estilo visual (ver preview), não o foco do destino; [evidência da Production](../evidence/runtime/about-skip-link-production-focus-2026-10-24.md). Sem mudança de produto ou homologação de comportamento.

- **CI-BASELINE-01 / Netlify:** o deploy isolado atual está READY e inclui `access-check`, mas o `DATABASE_URL` do Netlify só foi confirmado para o projeto de teste em `dev`; `production`/ `deploy-preview` ainda coincidem com o site principal. A fixture CI lê outra conexão, do GitHub Environment `ci-auth-isolated`. Alinhar os contextos Netlify usados pelo host e então refazer o gate autenticado; [evidência](../evidence/runtime/netlify-ci-auth-environments-2026-10-24.md). Nenhum valor secreto foi registrado.

- **ARC-13 / convenção de chaves:** há uma proposta não canônica de convenção semântica com 13 mapeamentos de exemplo para sufixos numéricos. Mantém namespaces e parâmetros como contratos de revisão, sem alterar índice ou produto. Faltam revisão/aprovação, outros 199 casos numéricos sem exemplo e 364 ocorrências sem proposta de chave (cinco sinks já têm lote separado); [proposta](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json).

- **Landing / Como funciona:** Production não tem link de salto ao conteúdo nas duas rotas; primeiro Tab foca a marca e `main` não tem id. O anel de foco dessa marca também difere de VIS-002. [Evidência](../evidence/runtime/public-skip-navigation-focus-2026-10-24.md). Achado observado; sem implementação ou decisão inferida.

- **VIS-002 / foco público:** a amostra da Landing mediu dez paradas de Tab em claro/escuro. As regras fonte declaram 3 px/offset 3 px globalmente e 3 px/offset 2 px no controle de tema, abaixo dos 4 px/offset 3 px aprovados. A CSSOM retornou 2.67 px para regra e teste inline de 3 px; a causa não foi identificada. [Evidência](../evidence/runtime/public-focus-ring-production-component-sample-2026-10-24.md). Não autoriza aplicação global.

- **VIS-002 / origem do foco:** a folha pública declara 3 px/offset 3 px; `ui-theme.css` força a cor clara `#6E512E` e o botão de tema declara offset 2 px. O About da PR #239 propõe 4/3 px localmente. [Mapa de escopo proposto](../evidence/architecture/vis002-focus-ring-source-map-proposal-2026-10-24.md); sem mudança de CSS ou canonização.


- **VIS-002 / mapa estático de foco ampliado:** oito entradas do produto mapeadas para as folhas consumidas. Há exceções de 2 px/2 px e 2 px/3 px em Configurador, Admin e Como funciona, além de hotspots sem outline explícito no Viewer/Configurador com pistas alternativas que ainda precisam de avaliação runtime. Escopo proposto, sem declarar falha nem alterar tokens/CSS: [mapa das folhas e componentes](../evidence/architecture/vis002-focus-ring-source-map-proposal-2026-10-24.md).
- **VIS-002 / Viewer runtime:** em Production, o módulo 02 exibiu borda dourada e marcador ao receber foco por Tab em claro e escuro; o foco não ativou o módulo. Contraste e demais superfícies seguem sem medição. [Registro](../evidence/runtime/viewer-scene-hotspot-keyboard-focus-production-2026-10-24.md).
- **VIS-002 / Como funciona runtime:** o botão “Compra em escala” recebeu foco por Tab; no tema claro, CSSOM confirmou `#6E512E` sobre a superfície opaca `#25231F`, razão calculada 2,15:1. Leituras de offset foram 2.66667 px e, na confirmação, 3 px como na fonte; diferença sem causa isolada. O risco está observado nesta combinação. Tema escuro foi visto sem readback CSSOM; outras superfícies permanecem sem cobertura. [Registro](../evidence/runtime/how-it-works-economy-action-focus-production-2026-10-24.md).
- **VIS-002 / contraste em Como funciona:** CSSOM confirmou `#6E512E` no outline sobre o fundo opaco `#25231F` em tema claro; o contraste calculado é 2,15:1. Risco observado só para este botão/rota/viewport; não generalizar. O pai imediato do botão é transparente e o offset positivo mantém o traço fora do preenchimento translúcido do próprio cartão. [Registro](../evidence/runtime/how-it-works-economy-action-focus-production-2026-10-24.md).


- **Login administrativo / responsivo em Production:** `/access/manage.html` redirecionou para o formulário de login em `/admin.html`; 1280×720, 390×844 e 320×700 CSS px sem overflow horizontal nos estados observados. Os campos estavam preenchidos pelo navegador; nenhum valor foi lido, alterado ou enviado, e não se concluiu que o perfil estivesse limpo. O fluxo autenticado não foi aberto. [Evidência](../evidence/runtime/admin-login-no-session-focus-production-2026-10-24.md).
- **Como funciona / imagens e movimento:** em 1280×720, após percorrer a rota Production, 28/28 imagens carregaram; 0 falhas e 0 imagens sem `alt`. Movimento reduzido retornou `false` e a API de animações não estava disponível; estado de animação e resposta a movimento reduzido nesta rota continuam não verificados. [Auditoria](../evidence/runtime/how-it-works-images-motion-production-2026-10-24.md).


- ****Landing / NAV-005 / overflow atual em Production**:** em 310 e 290 px, `html/body` computaram `min-width:320px`; em 290 px o menu e o conteúdo ficaram cortados nos dois temas. A issue #218 / NAV-005 segue aberta; a proposta compacta é uma simulação documental, não uma correção aplicada. [Evidência Production](../evidence/runtime/landing-public-compact-header-production-2026-10-24.md).
