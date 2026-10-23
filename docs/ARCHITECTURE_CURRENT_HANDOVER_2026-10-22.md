# HANDOVER ATUAL — MobiliPresenter2D + Design System

> **Preparação transversal validada — 23/10/2026:** [Migration Inspector V0](https://github.com/EAKerber/MobiliPresenter2D/tree/tooling/migration-inspector-v0-20261023) introduz inventário estático somente leitura (8 rotas; 56 dependências diretas distintas; 28 compartilhadas; 5 pares de sobreposição CSS lexical **não homologada como defeito**). O scanner passou de 39 falsos diagnósticos de origem ausente (33 causados por base href=/ no Configurador, seis referências a três bundles gerados) para **0 referências estáticas ausentes sem explicação conhecida** após modelar base HTML e package.json --outfile. [Gate do código e testes #40031745534 PASS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40031745534). O relatório não vê imports, DOM dinâmico, autorização, runtime CSSOM ou artefatos após build: nunca usá-lo para dispensar gates por impacto negativo. Branch isolada, nenhum PR/preview/merge. Três branches da correção nav/Flow/CI atualizaram asserções desatualizadas em app/tools/test-core.js; [App build purity #40031062438 PASS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40031062438), mas CI browser protegido requer fixture de sessão. **Não solicitar senha no chat**; preservar convite temporário de menor privilégio em GitHub Environment secret para #235; autenticação real pós-correção ainda HOLD. Nenhum dado, segredo ou main foi modificado.


> **Estado técnico mais recente — 23/10/2026 (substitui os diagnósticos 3/5 abaixo, que são históricos):** a branch limpa [`fix/ci-baseline-v5-nav-flow-clean-20261023`](https://github.com/EAKerber/MobiliPresenter2D/tree/fix/ci-baseline-v5-nav-flow-clean-20261023), derivada de `main@15e1cfb`, corrigiu a geometria intermitente da barra responsiva movendo `flow-steps` de `.flow-nav` para `.controls`, preservando o breakpoint visual antigo de 500px com a compensação de 14px. Os nove cenários Flow V3 legados agora são validados/projetados a V5 e interceptam `/api/buyer-configuration`, sem reduzir asserções. [Gate limpo #40011470495](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40011470495): **5/5 suítes funcionais PASS, 28/28 cenários Chromium/WebKit PASS e 56/56 equivalências visuais PASS**. [Gate de limiar #40012591081](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40012591081): **20/20 equivalências PASS** na faixa anteriormente não coberta. [Repetição integral no commit com o limiar corrigido #40012591135](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40012591135): **PASS confirmado**, 5/5 funcionais + 28/28 cross-browser + 56/56 visuais, após correção do limiar; a autenticação real permanece HOLD. [Checkpoint canônico atualizado da correção](https://github.com/EAKerber/MobiliPresenter2D/blob/fix/ci-baseline-v5-nav-flow-clean-20261023/docs/handoffs/CI_BASELINE_01_NAV_FLOW_CLEAN_2026-10-23.md). **HOLD remanescente:** GET autenticado 200 pós-correção no preview #235 e matriz autenticada; dois convites anteriores consumidos/revogados. Não solicitar/consumir novo convite antes de preparar o runner e o preview com a correção homologada. PRs #231/#234/#235 seguem DRAFT/HOLD; nenhum merge na `main`, nenhum novo Deploy Preview ou alteração de dados.


> **Reconciliação cruzada — 23/10/2026 (prioridade sobre o estado anterior deste arquivo).** Produto `main@15e1cfb`, DS `main@ae1be56` na leitura desta reconciliação. Registro mantido na branch **`docs/handover-reconcile-20261023`**, sem deploy ou merge.
>
> **Produto ARC-03C:** [PR #234](https://github.com/EAKerber/MobiliPresenter2D/pull/234) em DRAFT/HOLD, branch `architecture/arc03c-static-page-build-20261022@8ab2317`. O compilador já alimenta o build real para três páginas com fonte única e detecção de drift; [60/60 Chromium/WebKit PASS, zero diferenças](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39871907031), mas não foi integrado à main. NAV-004 e NAV-005 permanecem autoridades distintas.
>
> **CI-BASELINE-01 #232:** preview experimental [PR #235](https://github.com/EAKerber/MobiliPresenter2D/pull/235) é somente prova de `getDeployStore` V5 no deploy, **não candidato a merge**. [Deploy READY](https://app.netlify.com/projects/mobilipresenter2d/deploys/6adb87a7fc8cd994e4a86c10) e [preflight sem credencial #39985006606](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39985006606) PASS com marcadores públicos; ainda **UNVERIFIED** resposta autenticada `/api/buyer-configuration=200` após fix. Dois convites temporários consumidos/revogados. [Run local #39987226959](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39987226959): **3/5 PASS** (Mobile, Summary, Stone), **2/5 HOLD** (Keyboard/Flow, foco e navegação), sob V5 sintético local, não equivalente ao Netlify. [Handover detalhado CI](https://github.com/EAKerber/MobiliPresenter2D/blob/ci/ci-baseline-01-auth235-only-20261023/docs/handoffs/CI_BASELINE_01_AUTH235_READY_2026-10-23.md). Investigação dedicada em `ci/ci-baseline-01-nav-sequence-probe-20261023`. Sem convite novo até diagnóstico das duas suítes.
>
> **VIS-002C:** [reconciliação v0.2 #39894163198 PASS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39894163198), em `integration/vis002c-p-token-02b-v2-20261023`: 48/48 equivalências v0.1, 36/36 cenários de contraste, cinco textos contextuais autorizados, 90.315 pixels alterados apenas no escopo homologado; 32 casos continuam UNVERIFIED. Sem integração da PR #231 e sem distribuição global de paleta.
>
> **Responsabilidade de autoridade:** DS mantém `decisions.json`, contratos ARC, exportação e homologação visual; produto mantém HTML Vanilla, V5, build e testes. Os ganhos em branches e previews **não são implementação publicada**. Não converter histórico de CI vermelho em waiver, não expor `/config/` nem migrar controles comerciais por conveniência.
>
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
