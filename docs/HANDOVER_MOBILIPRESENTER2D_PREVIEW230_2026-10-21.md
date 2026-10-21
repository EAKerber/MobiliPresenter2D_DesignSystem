# Handover operacional — MobiliPresenter2D / revisão do preview #230 (21/10/2026)

**Tipo:** checkpoint factual, plano de retomada e registro do feedback mais recente do usuário.  
**Autoridade de homologação:** [`decisions.json`](../decisions.json) (NAV-004, NAV-005 etc.), [`DECISION_APPLICATION_MAP.md`](../DECISION_APPLICATION_MAP.md), [índice de profundidade](NAVIGATION_DEPTH_AUTHORITY_GATE_2026-10-21.md).  
**Produto:** [`EAKerber/MobiliPresenter2D`](https://github.com/EAKerber/MobiliPresenter2D); fonte operacional [issue-mestra #229](https://github.com/EAKerber/MobiliPresenter2D/issues/229); revisão [PR #230](https://github.com/EAKerber/MobiliPresenter2D/pull/230).

> **LEIA PRIMEIRO:** não usar a memória deste ou de outros chats para reconstruir homologação. O usuário confirmou que o Viewer é **profundidade 2**, não uma Landing reduzida, e corrigiu o posicionamento do retorno. Esta correção JÁ está no `decisions.json` da main deste Design System e JÁ foi aplicada à branch do produto. A PR continua draft. Este documento não substitui esses registros nem autoriza merge/publicação.

## 1. Snapshot verificável (GitHub consultado em 21/10/2026)

| Referência | Estado verificado |
|---|---|
| Produto `main` | `1878ae1057ce7c6190e0c8cb08a1f3baadd49463` — **intocada pela PR #230** |
| Design System `main` | `50f7273ec44808abf091cc26aabce5779ded5592`; NAV-005 já corrigido (commits `8cd24e2`, `6d330bc`, `50f7273`) |
| Produto PR [#230](https://github.com/EAKerber/MobiliPresenter2D/pull/230) | **open / draft**, head `24bbeadba8ec231c8c9f603c4da5116ab8a5ce3e`, branch `integration/ux-auth-viewer-preview-20261021`, **17 commits à frente / 0 atrás** de main, 13 paths no diff; GitHub `mergeable_state=unstable` (checks diversos não verdes) |
| Gate integrado do head atual | [Actions #39627779877](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627779877) **SUCCESS**, veja detalhe `3` |
| Netlify / publicação | site `mobilipresenter2d` / domínio `https://casaemmodulos.casa`; produção estava com deploy `ready`. **Não há no checkpoint URI/ID do Deploy Preview verificado de forma independente pelo conector.** O usuário enviou captura do estado que examinou; não inferir URL por número da PR |
| DS PR [#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) | ainda **draft / open**, branch de plano arquitetura/CSS divergente de main (última comparação: ~54 commits à frente / 11 atrás); **não assumir merge seguro** |
| DS PR [#41](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/41) | **draft / open**, auditoria de navegação privada; não tratar como integrada |
| Preço base público | **Não implementado**. [Issue #228](https://github.com/EAKerber/MobiliPresenter2D/issues/228) é backlog futuro com requisito aprovado |

Não criar segunda PR/preview para atualizar status. O preview foi autorizado **somente quando necessário**; manter a PR #230 como referência única e economizar builds.

## 2. Feedback do usuário: o que foi aceito e o que falta

**Revisão visual recebida:** no estado apresentado da PR #230, o usuário declarou o restante da aparência **dentro do esperado**, ressalvados o **posicionamento do retorno contextual no header** e a **ausência do preço base** (funcionalidade futura). Isso é aceite visual do **recorte visto pelo usuário** — **não** é aprovação de login real, de autorização pública de preços, de acessibilidade completa, de todas as resoluções ou de merge.

**Ordem exata aprovada para o Viewer, largo e compacto:**

`LOGO                        [espaço flexível]                        ← Ambientes   TEMA (Auto/Claro/Escuro)   MENU`

- **Marca isolada à esquerda.** O link `← Ambientes` pertence ao **grupo direito**, imediatamente **antes** do seletor de tema. **Hambúrguer é o último controle no extremo direito**.
- Viewer é página pública **secundária (profundidade 2)**. Os links globais ficam disponíveis no menu; a identificação específica do ambiente e controles de cena permanecem **fora do cabeçalho**; não marcar “Ambientes” como a página corrente do Viewer.
- Não deslocar o retorno à esquerda da marca e **não** mantê-lo junto à marca. A composição vale nos layouts amplo e compacto; regra de encaixe estreito homologada em NAV-005 continua aplicável.
- Esta ordem **já foi gravada** em `decisions.json > NAV-005.wideLayoutPatternsApproved.secondaryNavigationPages` e `NAV-005.compactLayoutPatternsApproved.secondaryNavigationPages`, indexada no documento de profundidade e no `DECISION_APPLICATION_MAP.md`.
- **Já aplicada na PR #230:** `app/viewer/index.html` separa `viewer-header__context` (só marca) de `viewer-header__actions` (retorno → tema injetado por `ui-theme.js` → toggle/menu); `viewer.css` aplica alinhamento; testes atualizados exigem ordem e responsividade; query da folha é `viewer.css?v=viewer-nav005-p2`. Commits recentes da branch `164aeaeca89e`, `71ca08c05567`, `4475d5f01131`, `24bbeadba8ec`.
- **PENDENTE:** verificar que o usuário está vendo **o deploy atualizado desse commit** (cache/propagação) e fazer inspeção visual final do alignment; não refazer código por basear-se apenas na captura **anterior** à correção.
- O usuário informou que, quando existir, o controle de preço será esperado na **aba Preços do Admin**. Registrar essa preferência como interface planejada, **não** supor que o toggle já esteja disponível.

## 3. O que a PR #230 contém (sem preço)

| Incremento | Código / finalidade | Teste e limitação |
|---|---|---|
| P0 [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212) + [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213) | `app/admin/admin.js` + `app/core/admin-bootstrap-retry.mjs` + `app/core/private-navigation.js`: retry **somente GET 401 transiente** com usuário ainda autenticado, `403` terminal, botão de retry explícito, reconciliação do menu por revisão sem reaproveitar lookup anônimo anterior | **11/11 Node PASS e bundle em branch isolada**; gate integrado 11/11. **Não comprova primeira autenticação real com Netlify Identity**; login, menu e bootstrapping exigem sessão de teste autorizada |
| P1 [#226](https://github.com/EAKerber/MobiliPresenter2D/issues/226) | `how-it-works.css`: apenas grades de 3 colunas `.foundation-list` e `.study-topics` recebem `align-items:start`, preservando `<details>` nativo | **8/8 funcional PASS** (Chromium/WebKit × 390/1366 × claro/escuro), mas **2 diferenças de pixel WebKit 390** (`.study-topics` claro e escuro) com DOM/computed/geometry equivalentes; **inspeção visual PENDING** |
| P1 [#225](https://github.com/EAKerber/MobiliPresenter2D/issues/225) | Viewer: cabeçalho secundário NAV-005, tema inserido no shell, retorno à direita antes do tema, menu público, fechamento por Escape/clique fora, sem refatorar cena | **20/20 gate browser PASS** em Chromium/WebKit, 320/390/486/768/1366 claro/escuro. Captura humana do usuário aprovou restante; **alinhamento revisto após captura precisa readback visual atualizado** |
| P2 [#227](https://github.com/EAKerber/MobiliPresenter2D/issues/227) | `viewer.js`, `viewer.css`: fonte e marcadores dos benefícios maiores; `overview-footer`, dimensões inferior-esquerda, sem dado comercial | **32/32 browser PASS** (2 engines × 390/1366 × 2 temas × 0/1/3/4 benefícios com dados públicos de teste). Usuário considera resultado visual esperado no recorte visto. Não contém preço |
| P2 [#228](https://github.com/EAKerber/MobiliPresenter2D/issues/228) | **FORA DA PR #230**. Uma flag global de publicação de preço base no Admin, OFF por padrão, com preço autorizado apenas em payload público validado | Gate de arquitetura **PENDING**: publicação V5, DTO público versionado, mapeamento itemBase, revogação/cache e política de zero; não usar fallback de dados privados |

**Evidência final combinada:** [Actions #39627779877](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627779877) `SUCCESS`, relatório das etapas: 11/11 Node, `HOW_ACCORDION_GRID_RESULT functionalPassed=8, chromiumPixelParity=true, webkitPixelReviewPending=2`, `VIEWER_NAV005_RESULT PASS 20/20`, `VIEWER_OVERVIEW_EDITORIAL_RESULT PASS 32/32`. Não confundir o verde **desta suíte dedicada** com “todos os checks da PR verdes”.

### Outros checks da PR #230

No head `24bbeadb`, `current-build`, `current-asset-gates` e `variants` passaram. Há **falhas** em outros workflows: mobile, public routing, summary pricing e stone browser; na observação mais recente o workflow admin hierarchy ainda estava em execução. Algumas falhas de suites antigas e infraestrutura apareceram em etapas anteriores, mas **as causas dos checks atuais não foram todas classificadas**; comparar exatamente com `main` e logs antes de chamar de preexistentes ou de regressão. `mergeable_state=unstable` impõe **HOLD de merge**.

## 4. Pendências, prioridades e dependências

### Gate imediato: fechar #230 sem custos desnecessários

1. **Verificar preview corrente** por ID/URL real e SHA: se for `24bbeadb` (ou descendente), conferir o header na ordem acima, largura estreita, foco/teclado, tema e retorno; se preview atrasado, aguardar atualização/corrigir cache antes de criar nova publicação. A captura original não é o teste do ajuste mais recente.
2. **Inspecionar os screenshots WebKit** da grade `.study-topics` a 390px claro/escuro, 2 casos pixel-diferentes; apenas classificar equivalência após revisão. Os testes funcionais passaram.
3. **Auth real:** testar primeiro login anônimo→admin e menu privado sem recarga, `/api/admin-bootstrap`, logout, expiração e retentativa, em sessão segura, sem publicar cookies/tokens/identidades. Testar Chrome/Safari iPad quando possível. **Bloqueador de PR pronta/merge**, independentemente dos mocks 11/11.
4. **Classificar checks restantes da PR** em regressão introduzida / falha preexistente / ambiente / provider; não assumir que falha fora do fileset seja irrelevante sem prova.
5. Garantir que cena/seleção do Viewer e projeção pública existente permanecem corretas, menu não duplica event listeners e não marca rota falsa. Conferir o destino do item “Fale conosco” (na branch ainda aparece `https://wa.me/` sem destinatário, **verificar** link oficial; não inventar número).
6. Somente após os gates e revisão explícita propor tornar a PR pronta ou mesclar. **Não houve autorização de merge automático**.

### Após #230: preço base (#228) em incremento separado

**Direção de produto resolvida:** controle global único `Mostrar preços base no Viewer`, **desligado por padrão**, **aba Preços do Admin** como localização esperada, permite publicar **somente os valores base válidos** de módulos elegíveis/visíveis. Sem flag individual por módulo e sem exceções na v1. Card Viewer: **dimensões inferior-esquerda; “Valor base do módulo” + BRL inferior-direita**, ênfase semelhante ao resumo de contas. **Ausência/desligado = campo de preço ausente também do HTTP público**, não apenas oculto em CSS.

**Gate bloqueante de contrato:** `netlify/functions/configuration.mjs` rejeita escrita geral V4/V5 (422 `hierarchy_publication_required`, salvo exceções limitadas), `PublicModulePresentation2D 0.1` exclui preço deliberadamente, `netlify/functions/public-modules.mjs` projeta apenas dados publicados permitidos. Definir mecanismo de autorização global persistida, forma de publicação/rollback controlada, compatibilidade de versões, política de valor zero, cache/invalidação ao desligar e DTO novo mínimo sem `priceBook`/custos/margens/regras privadas. Preview fallback fail-closed. **Não resolver abrindo publicação V5 irrestrita ou enviando priceBook ao browser.**

### Outros débitos sem misturar no patch

- [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218) NAV-005, header primário compacto (contrato diferente do Viewer profundidade 2).
- [#224](https://github.com/EAKerber/MobiliPresenter2D/issues/224) Landing, grupo ativo do carrossel pode esconder Lavanderia selecionada; bug reproduzido, causa ainda não provada.
- DS [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) contém plano diretor CSS G0–G8 e matriz R01–R20, mas está em branch draft defasada; conferir conflitos com main antes de recuperar/integrar. DS [plano corrente](ROADMAP_AND_CURRENT_STAGE_2026-10-21.md) já está integrado.
- Outras branches anteriores `experiment/ui-declarative-landing-benefits-20261020` e `experiment/shared-public-header-controller-20261020` **não são base da PR #230**; não misturá-las silenciosamente.

## 5. Critérios de parada / política de execução

- **Não executar merge, publicar produção, habilitar preços, modificar dados administrativos nem criar previews extras sem gate e necessidade.** O usuário autorizou preview **quando necessário** e solicitou baixo volume; um PR integrado já existe.
- Se revisor sinalizar apenas layout de Viewer, evitar tocar auth, schema ou CSS global no mesmo patch.
- Se auth real falhar, priorizar reprodução causal/sessão/server; não usar refresh automático como maquiagem e não expor credenciais em logs.
- Decisão homologada → rota/contrato → diff do produto → teste → evidência visual → autorização. **Nunca o inverso.**
- Marcar explicitamente `PASS`/`FAIL`/`PENDING`/`BLOCKED`/`OUT-OF-SCOPE` por gate; aprovação visual de uma imagem não é aprovação automática de fluxo não fotografado.

## 6. Comandos e ponteiros de retomada

**Ler nesta ordem:**
1. Este handover e [produto #229](https://github.com/EAKerber/MobiliPresenter2D/issues/229).
2. `decisions.json NAV-005` e [gate de profundidade](NAVIGATION_DEPTH_AUTHORITY_GATE_2026-10-21.md), comparando com [issue #225](https://github.com/EAKerber/MobiliPresenter2D/issues/225).
3. [PR #230](https://github.com/EAKerber/MobiliPresenter2D/pull/230): revisar head **atual**, diff, checks, comentários e preview existente. Confirmar `main`/`head` novamente; SHAs acima são snapshot e podem mudar.
4. [Actions #39627779877](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627779877) e suas evidências; avaliar testes de browser e flakes.
5. [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212), [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213), [#226](https://github.com/EAKerber/MobiliPresenter2D/issues/226), [#227](https://github.com/EAKerber/MobiliPresenter2D/issues/227), [#228](https://github.com/EAKerber/MobiliPresenter2D/issues/228), e bloqueios acima.
6. [DS roadmap](ROADMAP_AND_CURRENT_STAGE_2026-10-21.md), [DS #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) apenas se for retomar arquitetura CSS.

**Checklist curto para novo agente:** o Viewer esperado é **LOGO [flex] ← Ambientes | Tema | Menu**; código já ajustado em #230; preço **não existe ainda** e toggle deverá ficar em Admin → Preços; quatro incrementos automatizados passam, mas login real/CI alheia/screenshots WebKit não fecharam; PR draft sem merge; evitar novos previews. Em dúvida, consultar contratos canônicos antes de alterar.

**Este documento é recuperação de contexto e não solicita ação de release.**


## 7. Readback de persistência pós-interrupção (21/10/2026)

Este checkpoint foi reconferido no GitHub depois da interrupção do chat, sem alterar o código do produto:

- **Produto:** `main@1878ae1057ce7c6190e0c8cb08a1f3baadd49463` permanece inalterada. PR [#230](https://github.com/EAKerber/MobiliPresenter2D/pull/230) continua aberta em **draft**, `head@24bbeadba8ec231c8c9f603c4da5116ab8a5ce3e`, 17 commits à frente/0 atrás, `mergeable_state=unstable` devido a checks não verdes. Nenhum merge nem deploy foi solicitado nesta retomada.
- **Confirmação do código existente:** `app/viewer/index.html` do próprio head já contém `viewer-header__context` (logo isolada) e `viewer-header__actions` (retorno `← Ambientes`, tema inserido por `ui-theme.js`, botão/menu); `viewer.css?v=viewer-nav005-p2` está versionado. Não criar nova alteração antes de conferir o preview do SHA correto.
- **Contratos de design:** o `decisions.json` atual segue com a correção explícita em `NAV-005.wideLayoutPatternsApproved.secondaryNavigationPages` e `NAV-005.compactLayoutPatternsApproved.secondaryNavigationPages`. Não iniciar nova rodada de homologação apenas para relembrar a ordem.
- **Persistência recíproca no produto:** a [issue-mestra #229](https://github.com/EAKerber/MobiliPresenter2D/issues/229) agora começa com **HANDOVER PRIORITÁRIO**, incluindo SHA, arquivos, testes, fluxos e bloqueios; a [issue #225](https://github.com/EAKerber/MobiliPresenter2D/issues/225) documenta o readback da posição já aplicada; o body da [PR #230](https://github.com/EAKerber/MobiliPresenter2D/pull/230) contém a mesma orientação e permanece **HOLD**.
- **Produção:** site Netlify `mobilipresenter2d` / `https://casaemmodulos.casa`, último deploy publicado identificado `6ad6c3b51b6be05647167f94` (`ready`). **Esse ID refere-se à produção, não ao preview da PR**; a URL de preview específica continua sem readback independente neste checkpoint.
- **Teste relevante mais recente do head:** [GitHub Actions #39627779877](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627779877), integrado, PASS 11/11 auth unit, 8/8 accordion funcional (2 screenshots WebKit diferentes para revisão), 20/20 Viewer NAV-005, 32/32 Viewer editorial. CI geral do PR **não está toda verde**; classificar as outras falhas antes de merge.
- **Produto #228:** preço base ainda **não implementado**, controle global OFF aprovado e esperado em **Admin → Preços**; publicação V5/projeção allowlisted, revogação e valor zero permanecem gate separado.

**Estado do handover:** recuperação documental concluída em **ambos os repositórios, sem novo preview e sem commits de produto**. Novos agentes devem começar pela issue #229 e pelo presente documento, confirmar se os SHAs ainda são atuais e resolver gates de preview/autenticação/CI antes de pedir merge.

## 8. Retomada verificada — preview e CI (21/10/2026, após checkpoint)

**Fontes observadas diretamente:** GitHub PR #230, Netlify deploy ID `6ad8df92e3607a308457c73f`, Actions #39627779877 e logs dos workflows da PR comparados com execuções de `main`. Esta seção atualiza os fatos da seção 7; não altera homologações nem autoriza merge.

### Deploy Preview agora identificado (readback independente)

- URL oficial: [deploy-preview-230--mobilipresenter2d.netlify.app](https://deploy-preview-230--mobilipresenter2d.netlify.app).
- Deploy Netlify: [`6ad8df92e3607a308457c73f`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad8df92e3607a308457c73f), `context=deploy-preview`, `review_id=230`, `state=ready`, `commit_ref=24bbeadba8ec231c8c9f603c4da5116ab8a5ce3e`. **Não é deploy de produção.**
- O head da PR segue `24bbeadb` e `main` do produto segue `1878ae1`; logo, não há justificativa para novo deploy apenas para propagar a correção NAV-005.
- **Distinção do gate:** deploy pronto e SHA conferido **não** equivalem a inspeção visual do Viewer atualizado, teste WebKit real, login real ou autorização de publicação. Inspeção visual externa em navegador permanece **PENDING**.

### Classificação por comparação com baseline

| Check da PR #230 | Evidência em PR | Evidência prévia na main | Classificação |
|---|---|---|---|
| Mobile browser | [#39627788582](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627788582) `getLayoutProfile` ausente | [#39353608197](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39353608197) mesmo TypeError | **BASELINE FAIL**; não atribuir ao diff da #230 |
| Stone browser | [#39627788371](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627788371) timeout `waitForFunction` | [#39353608149](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39353608149) timeout idêntico | **BASELINE FAIL** |
| Summary pricing | [#39627788381](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627788381) timeout `waitForFunction` | [#39353608435](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39353608435) timeout idêntico | **BASELINE FAIL** |
| Admin hierarchy | [#39627788356](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627788356) selector `cabinet-finishes` timeout e job cancelado | [#39353608218](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39353608218) mesmo selector timeout, cancelamento | **BASELINE FAIL / CANCELLED** |
| Public routing static | [#39627788439](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627788439), 3/7 tests fail: `publicState.entities` indefinido e allowlist divergente | [#39200818054](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39200818054) mesmos testes e erros | **BASELINE FAIL**, fileset de teste/projeção igual na main e na branch |
| Public routing browser | no preview a rotina exige `class="workspace"` em `/config/`, após esperar 5 min | baseline do mesmo workflow não fornece prova de sessão privada real | **TEST CONTRACT BLOCKED**: pré-condição incompatível com rota autenticada; não converter em PASS artificialmente |
| `current-build`, `current-asset-gates`, `variants` e suíte integrada | PASS; suíte isolada [#39627779877](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39627779877) | checks protegidos/isolados | **PASS no recorte testado** |

**Leitura correta:** os checks vermelhos conhecidos são preexistentes e merecem dívida de manutenção própria, mas isso não homologa login real nem prova ausência total de regressão. Falhas dos browser checks de domínio envolvem pré-condições antigas de acesso a `/config/`, hoje privado; corrigir a **estratégia de teste** com sessão autorizada/fixtures locais explícitas, sem abrir a rota nem omitir a autenticação.

**HOLD final da PR #230:** 1) inspeção visual real do preview SHA `24bbeadb` para NAV-005, telas estreitas e foco; 2) WebKit 390 claro/escuro em `how-it-works` (diferenças de pixels sem diferença funcional conhecida); 3) fluxo controlado de primeiro login/reauth/menu/logout, incluindo iPad quando possível; 4) `https://wa.me/` sem destinatário no Viewer: validar contato oficial antes de substituir; 5) aprovação explícita para merge. Não criar preview adicional, não alterar preços, não permitir GET privado.
