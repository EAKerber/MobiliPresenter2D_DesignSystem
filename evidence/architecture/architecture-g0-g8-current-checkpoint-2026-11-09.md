# Checkpoint atual da arquitetura G0–G8 — 2026-11-10

**Última atualização:** 2026-11-10 (BRT).

**Escopo:** reconciliação documental do plano de consolidação de Design System, CSS e componentes. Este checkpoint atualiza a fotografia operacional, não aprova mudanças visuais, migrações em lote, merge de código de produto ou publicação.

**Plano de referência:** [Plano diretor G0–G8](../../docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · [reconciliação anterior](master-plan-g0-g8-current-crosswalk-2026-10-25.md) · [handover e governança](../../docs/HANDOVER_CURRENT.md).

## Evidência verificada nesta retomada

- Design System: `main@79db735d6f05177b0c406e383d35832f3d72fdef` (último commit observado: 2026-10-27). Na leitura anterior à criação desta PR havia **1 branch e 0 PRs**; após sua abertura, a observação live é **2 branches e 1 PR aberta (#119)**.
- O workflow agendado [Branch hygiene #42655241742](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/42655241742) terminou em **success** em 2026-11-09. O endpoint de rulesets ainda lista ativo o ruleset #25953910 para `ds-history/2026-10-27/*`. O último readback documental confirma oito tags históricas protegidas; esta retomada não reenumerou individualmente seus objetos. Nenhuma branch foi removida nesta retomada.
- Produto: `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, **3 branches remotas** e **1 PR aberta (draft #269)**. Em 2026-11-10 foi criada a branch `codex/nav005-public-compact-main-20261110` a partir do `main` exato, com backport seletivo do cabeçalho público NAV-005; a PR #269 está aberta em draft, sem integração. `main` e `development` não foram alteradas; não houve deploy nem banco. A PR segue draft e ainda não há Deploy Preview disponível; a leitura Netlify mais recente mostrou apenas deploys `main/production`. Os recibos locais UX-04 e os arquivos de trabalho permanecem isolados.
- Issues observadas no repositório do produto: **#208, #216, #218 e #232 abertas**; **#217, #224 e #226 encerradas**. Isso corrige fotografias mais antigas que ainda listavam #217/#224/#226 como pendentes. Fechamento de issue não equivale a auditoria ampla ou aceitação de release.

## Estado operacional das fases

| Fase | Estado nesta retomada | Próximo gate verificável |
|---|---|---|
| **G0 — evidência e documentação** | **PASS como base de rastreabilidade; contínuo.** O handover local de 06/11 registra G0 PASS; esta retomada atualiza HEADs/issues live, mantendo os snapshots datados. | Continuar reconciliando mapas por domínio sem reescrever evidências históricas nem promovê-las automaticamente. |
| **G1 — navegação e foco** | **PARCIAL.** UX-04 segue sem run Actions no SHA atual `development@1a69ff76`; o workflow `workflow_dispatch` continua apenas em `development`, ausente da branch padrão `main`. A candidata NAV-005 está em PR draft #269; no head `6195e90c012a45a7abf1b8db6de220be03dc9fb4`, o gate browser público passou 124 cenários Chromium/WebKit. O workflow `Public routing before Clerk` passou no job estático; seu browser remoto foi **skipped** por o PR estar draft. O job existente `Flow layout browser` falhou uma vez em `webkit/701/light` após restaurar para 1366 px; a repetição somente desse job (#130257485418) passou os 24 casos. Isso classifica o primeiro resultado como falha não reproduzida, sem provar causa raiz. Nenhum Deploy Preview foi gerado. #218 permanece aberta; cobertura touch/zoom/dispositivo real continua pendente. | Fechar #218 com checklist runtime hospedado e critérios restantes; executar UX-04 no runner Linux/Node 22 quando o workflow estiver acionável na branch padrão; completar touch, zoom e dispositivo real. |
| **G2 — CSS e acessibilidade** | **EM ANDAMENTO.** #208 e #216 seguem abertas; #217 está fechada. A atribuição da regra vencedora agora foi capturada por Chrome DevTools nos seis contextos locais (três consumidores originais × light/dark) em `main@221b54b`; o v0.3 vence os três seletores em light e dark continua em `--public-muted`. A captura usou HTML local e links stylesheet ajustados para `file://`; ela fecha apenas o subgate de atribuição e não substitui preview hospedado/CDN. O coletor Playwright corrigido ainda falha antes da navegação ao iniciar Edge no ambiente. As 98 incertezas UNCERTAIN de `/config/` seguem abertas. | Reconciliar separadamente os critérios remanescentes de #216 (incluindo eyebrow e contextos adicionais), `/config/` e #208; obter preview hospedado autorizado sem promover a evidência local além do seu escopo. |
| **G3 — ownership CSS/DOM** | **PARCIAL.** Existem mapas estáticos, traces e propostas ARC-13, mas proposta contextual e semelhança lexical não provam ownership nem equivalência. | Fechar ownership por consumidor real, folha carregada, cascata, estado, tema e origem do token antes de qualquer extração. |
| **G4 — foundations, tokens e acessibilidade compartilhável** | **HOLD.** Fonte de referência e decisões aprovadas não demonstram integração abrangente; o handover local de 06/11 mantém G4 em HOLD. | Retomar somente após resolver as incertezas visuais/runtime de G2/G3 e definir o consumidor autorizado. |
| **G5 — famílias de componentes CSS** | **PARCIAL na candidata; HOLD na baseline.** O handover local de 06/11 mantém probes/famílias e incertezas sem consolidação homologada. | Fechar associação de probes e incertezas por família e obter comparação funcional/visual antes de compartilhar regras. |
| **G6 — composição e arquitetura de páginas** | **HOLD.** A direção Vanilla e ownership por domínio continua documentada; a composição declarativa segue experimental. Evidência local recente mantém G6 em HOLD enquanto G4/G5 e cobertura de domínio não fecham. | Reavaliar um piloto mínimo depois de G1–G5, com autoridade de dados explícita e sem criar framework genérico. |
| **G7 — hardening entre plataformas** | **PENDENTE.** #232 permanece aberta; o crosswalk anterior registra que WebKit headless não substitui Safari/iPad real e que validação autenticada exige fixture autorizada. | Resolver a fixture/CI protegida e completar jornadas críticas sem contornar autenticação. |
| **G8 — aceitação e release** | **NÃO INICIADO COMO RELEASE.** Não há autorização de publicação neste checkpoint. | Somente após revisão humana, integração autorizada, validação na base integrada e readback pós-release. |

## UX-04 — foco após redesenho do puxador

A varredura dos subdiretórios localizou o relatório de trabalho `docs/work/DEVELOPMENT_UX04_GEOMETRY_FOCUS_2026-10-28.md`. O gate dedicado mais recente verificado no GitHub é [#41344513485](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/41344513485), **success** no SHA `c7c2822d5b651ae0bcfcf0ac28c66cb61b645e98`; os jobs de intenção estática/proveniência e browser local passaram, incluindo geometria V5, restauração de foco e a suíte completa de teclado. O HEAD remoto atual de `development` é `1a69ff76a5f36e3245a288773bb409aa662e4e62`; a leitura da fonte confirma a chamada de retorno ao foco com `section:handles`. [O run exato deste HEAD](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/42720598449) passou 124 cenários públicos NAV-004/005, que são outro gate. Não há run GitHub Actions UX-04 nesse SHA. Como reexecução local do mesmo código, foram rodados no worktree isolado em `development@1a69ff76a5f36e3245a288773bb409aa662e4e62` o teste `tests/ci/ux04-geometry-focus-v5.cjs` e a suíte `tests/keyboard-browser.cjs`: **ambos PASS** em Chromium 151.0.7922.34 / Playwright 1.62.1, com fixture local V5 derivada dos defaults versionados e servidor temporário apenas em loopback. A medição confirmou o layout side-rail em 1366 px, o layout lado a lado em 1050 px, o modo compacto sem overflow em 390 px e retorno do foco ao controle selecionado após redraw; a regressão completa de teclado também passou. Não houve erro de página/console no diagnóstico UX-04.

Esta execução local usou Windows, Node 24.20.0 e Python 3.14.6 (o workflow usa Ubuntu e Node 22). Os cinco testes de `test_development_ux04_authority.py` passaram depois de buscar o objeto histórico de origem `5d8347edb6ea247307b6fc27b424117553542f78` para `FETCH_HEAD` (sem mover refs); build, `pages:check`, os três testes Node de flow/model/hierarquia, a checagem sintática do runner e os dois testes de navegador também passaram. Portanto, isto é **evidência local reproduzível no SHA exato**, não resultado de Actions nem validação cross-platform completa. Os recibos JSON locais estão em `work/MobiliPresenter2D-ux04-gate-1a69ff76/artifacts/ux04-local-gate/{geometry,keyboard}/result.json` no workspace do projeto; SHA-256: geometria `e14c57c1be881ff8950bd9b9e1a21cdcca04b937b41433bc9f1284d7440b82d5`, teclado `68c9d7a999d7b703c5ed7d2c75d76f64ddf2a6d0ad14b8ad8fd1fd903629bc91`.

UX-04 é o foco do Configurador após redraw; a issue #218 é a geometria/contrato NAV-005 do cabeçalho público. São gates distintos e não devem ser tratados como resolvidos um pelo outro. O G1 segue parcial até haver execução integral do workflow no runner Linux/Node 22, fechamento dos critérios específicos de #218 e cobertura de touch, zoom e dispositivo real.

### Issue #218 / NAV-005 — crosswalk estático em main e development

Leitura estática do produto pinado confirma que **main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95 ainda mantém candidatos para os critérios da #218**. Em `app/how-it-works/index.html:22`, o CTA do WhatsApp fica em `.header-actions`, fora de `#primaryNav`, que contém apenas os três links de navegação; `app/landing/header-menu.js` abre e fecha somente `#primaryNav`. `app/core/ui-theme.js` insere o controle antes de `.menu-toggle`, mas `app/ui-theme.css:72-75` o reduz a 44 px icon-only até 1150 px. A marca permanece em 160 px a 486 px (`app/landing/landing.css:158)); o CTA vira ícone fora do menu até 520 px (`landing.css:188-192`). A regra de largura mínima 320 px em `public-theme.css` e o recorte em `how-it-works.css` também deixam pendente a faixa estreita de duas linhas descrita na issue.

Em **development@1a69ff76a5f36e3245a288773bb409aa662e4e62**, a leitura estática indica uma correção escopada para o cabeçalho público: preserva o rótulo até o fallback compacto, reduz a marca até 30%, move o CTA para o menu em larguras compactas e permite duas linhas abaixo de ~291 px sem alterar os cabeçalhos privados/`viewer`. Permanece um candidato em ≤290 px: o CSS oculta o rótulo do tema enquanto o cabeçalho passa a duas linhas e a marca ainda só encolheu cerca de 9% a 290 px.

Este crosswalk começou como leitura estática e não fecha #218 por si só. A PR draft [#269](https://github.com/EAKerber/MobiliPresenter2D/pull/269) usa a branch `codex/nav005-public-compact-main-20261110`, baseada em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; head atual `6195e90c012a45a7abf1b8db6de220be03dc9fb4`, com 17 arquivos alterados. No GitHub Actions, 13 de 15 checks estão em success e dois foram skipped: o browser de `Public routing before Clerk` e `Supabase Preview`. O gate dedicado [NAV-005 local-only](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/42938417264) passou 124 cenários em Chromium e WebKit. O job de layout responsivo que falhou uma vez em `webkit/701/light` passou na repetição isolada #130257485418 (24/24); o primeiro resultado não se reproduziu. A checagem estática de roteamento passou, mas nenhum navegador remoto executou porque o PR permanece draft. O usuário autorizou uma única revisão de preview; ela ainda não foi feita: o preview automático não apareceu e o Netlify não mostrou deploy da branch candidata. Sem preview, #218 permanece aberta. Esses gates não comprovam touch, zoom, Safari/iPad real, foco no cabeçalho ou equivalência visual hospedada; não considerar o candidato integrado nem o PR pronto para merge.

# VIS-002C cascade winner trace — 2026-11-10

## Pin and method

- Product source: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; detached worktree was clean at capture.
- Browser: Chrome 156.0.0.0 through Chrome DevTools; viewport 766×608 CSS px, DPR 1.5.
- The original route HTML was opened from local `file://` URLs. Because its root-relative stylesheet URLs resolve to the drive root under `file://`, the three source pages used the exact CSS files from the pinned `app/` directory, linked in their production order. The v0.3 token stylesheet was loaded separately immediately before Landing CSS to reproduce its `@import` position. The HTML body and target elements were not rewritten.
- `get_css_styles` identified the active declaration and listed overridden declarations. In light mode the token value was also read from `getComputedStyle`; in dark mode the light-only token was absent. The same page DOMs were inspected in explicit `data-theme=light/dark` states.
- This is a local source-cascade trace. It is not an HTTP/Netlify/CDN capture; the browser’s file-scheme path workaround and the failed absolute `@import` request mean it must not be described as a full production-route runtime test.

## Results

| Route / selector | Matches | Light winning foreground rule | Previous light declaration | Dark winning foreground rule |
|---|---:|---|---|---|
| `/` · `.hero-description` | 1 | `landing.css:209` — `color: var(--ds-vis002c-long-copy-light)`; token `vis002c-long-copy-light-v0.3.0.css:6` = `#292723` | `landing.css:53` — `#705C4B` (overridden) | `landing.css:52` — `color: var(--public-muted)`; `ui-theme.css:89` resolves it to `#C4BCB2` |
| `/how-it-works/` · `.how-hero-note` | 1 | `how-it-works.css:312` — `color: var(--ds-vis002c-long-copy-light)`; token `vis002c-long-copy-light-v0.3.0.css:6` = `#292723` | `how-it-works.css:296` — `#705C4B` (overridden) | `how-it-works.css:7` — `color: var(--public-muted)`; `ui-theme.css:89` resolves it to `#C4BCB2` |
| `/about/` · `.about-scale p:not(.eyebrow)` | 3 | `about.css:54` — `color: var(--ds-vis002c-long-copy-light)`; token `vis002c-long-copy-light-v0.3.0.css:6` = `#292723` | `about.css:50` — `#705C4B` (overridden) | `about.css:18` — `color: var(--public-muted)`; `ui-theme.css:89` resolves it to `#C4BCB2` |

All three contexts produced identical computed colors per theme:

| Theme | Computed foreground | Computed background | CSSOM-derived contrast |
|---|---|---|---:|
| Light | `rgb(41, 39, 35)` / `#292723` | `rgb(240, 237, 232)` / `#F0EDE8` | **12.7658:1** |
| Dark | `rgb(196, 188, 178)` / `#C4BCB2` | `rgb(32, 33, 31)` / `#20211F` | **8.6109:1** |

The About selector matched three paragraphs; all three retained the same color, token, background and ratio. The ancestor background inspection found no image, filter, opacity, blend or backdrop-filter caveats for these targets.

## Scope and limits

This resolves the missing **winner-attribution subgate** for the three originally captured #216 consumers in the pinned source, across light and dark. It confirms that the v0.3 token wins in the three light contexts, the former `#705C4B` declarations lose there, and dark text still resolves through the original `--public-muted` rule.

It does **not** close issue #216 or G2. The issue’s `.study-band .eyebrow` and the later five additional contexts are not part of this trace; `/config/` remains a separate 98-pair UNCERTAIN analysis; the trace does not prove current CDN bytes, a whole-page visual review, device behavior, or global accessibility. Existing six screenshots and the earlier CSSOM receipt remain the evidence for their stated limits.

## Limites do subgate CSSOM local DS-05A

O material local de 2026-11-09 registra: regressão de oito fixtures PASS; inicialização real do Configurador em seis estados de `/config/` (390/1050/1366 CSS px × light/dark); 70–74 candidatos de texto por estado sem pares computáveis abaixo do limiar; 98 pares no total mantidos como **UNCERTAIN** por `backdrop-filter`. Um ajuste local dos números dos módulos em light está **não commitado** no checkout de auditoria.

A fonte está em `work/MobiliPresenter2D-dev-static-1a69ff7/docs/design-system/DS05A-static-css-provenance-development-1a69ff76.md` no ambiente desta retomada. O checkout está sujo. A identidade local foi conferida nesta retomada:

| Artefato local | SHA-256 |
|---|---|
| Relatório de proveniência DS-05A | `7c639f7ac39658f06f931c5baa43222de6e24a8efb6c14056d2c4a1adfab6480` |
| Recibo `runtime_cssom.json` (228.554 bytes) | `aad1f18832d988d13ed635216a91db2eeeb3f5f1cb8fce9bb004131828bb1291` |
| Runner `theme_cssom_runtime_v1.cjs` | `27c923948a20e896c8fc59e013523b4baebacbd4e6450f19a738855fe78b48da` |
| Teste de fixtures `test_cssom_v2.cjs` | `3b05d9a06e562816864ca94f9228d397d650f95d142c07ac4745f6810ef9501e` |
| `app/ui-theme.css` local modificado | `5b11afd500f8545d723a87b22f586c2c8f42e4f9b4fc22f4e953e96da4ae0545` |

Esses hashes identificam os objetos existentes no checkout; não comprovam por si só o método de geração, compatibilidade com o pin remoto ou revisão do patch. O runner e o recibo da execução de 2026-11-10 foram preservados em [evidence/ds05a-runtime-2026-11-09](../ds05a-runtime-2026-11-09/README.md), junto com o patch CSS candidato mantido como arquivo inerte. O recibo original veio de checkout local sujo: a árvore app/ coincide com development@1a69ff76a5f36e3245a288773bb409aa662e4e62, exceto pela declaração candidata adicional em .module-number. A versão exata do Chromium/Node não foi registrada no recibo; o pacote preserva os inputs e o limite, mas ainda não é reprodução independente nem gate fechado. O escopo é somente o DOM inicial montado de `/config/`; não cobre Admin, teclado, foco, hover/seleção/erro/loading/dock, tema `auto`, 320/768 px, screenshot review ou dispositivo real. **DS-05A permanece INCOMPLETO/HOLD.** Não promover o ajuste local para produto nem inferir aprovação visual.

## G2/G3 — rastreio de VIS-002C v0.3 em main

O código está pinado em `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; a integração v0.3 entrou pela PR [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241), merge commit `818f165bf0b11b53f5fbaba1417560066bf03637`.

A direção de cor tem uma sequência verificável: o corpo antigo da #216 citava `#675F55`; comentário posterior rejeitou esse valor e registrou `#705C4B` para os três consumidores originais; depois, o mapa v0.3 registrou a preferência autorizada por quase-preto `#292723` e marcou v0.2 como substituído nesses contextos. Portanto `#675F55` e `#705C4B` são históricos para esses três consumidores; a referência atual é v0.3. O eyebrow da faixa de estudo permanece `#70522F`.

| Rota/seletor | HTML e folhas carregadas | Regra consumidora na fonte pinada |
|---|---|---|
| `/` · `.hero-description` | `app/index.html` blob `75f3351ae256d2e5ad45c204af14087cde774104`; `app/landing/landing.css` blob `edccb171404061ff9fd36f503231c09316f24a8a` importa a folha v0.3. | O legado `#705C4B` está na linha 53; a regra posterior nas linhas 209–212 usa `var(--ds-vis002c-long-copy-light)`. |
| `/how-it-works/` · `.how-hero-note` | `app/how-it-works/index.html` blob `956df72c85671e02fda3460900311e15956b85b1`; carrega `public-theme.css`, Landing CSS, `how-it-works.css` blob `c38677d7950b46d7e7027935371dec72d726bcb4` e `ui-theme.css`. | O legado está na linha 296; a regra posterior nas linhas 312–316 usa a variável. |
| `/about/` · `.about-scale p:not(.eyebrow)` | `app/about/index.html` blob `5124d3d930073fdfad1a8602cca999ea3413cd5e`; carrega Landing CSS e `about.css` blob `c1d0b0c01bc2de069f6cf4b8271c2734363aacc8`. | O legado está na linha 50; a regra posterior nas linhas 54–57 usa a variável. |

A folha gerada `app/design-system/vis002c-long-copy-light-v0.3.0.css` (blob `9e7f243039a717d02f897d7320a4c383856f8fa0`) define `--ds-vis002c-long-copy-light: #292723` nos dez contextos claros mapeados por `design-system/pins/vis-002/context-v0.3.0/contextual-mapping.json` (blob `e8f42f76e2732cbcf3e9a68d1dc8f82ea79dd73d`). Ela limita a variável ao tema claro; o mapa exige preservar dark.

### DOM/CSSOM local executado — seis contextos

No checkout detached e limpo de arquivos versionados em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, as páginas foram servidas localmente em loopback e inspecionadas em seis contextos novos: as três rotas acima × temas claros/escuros explícitos, viewport 1440×900 CSS px, DPR 1. Runtime: Windows, Node 24.20.0, Playwright 1.62.1, Edge 157.0.4341.42. A captura contou 1 elemento em Landing, 1 em How-it-works e 3 parágrafos em About. Todos os alvos de cada rota/tema compartilharam os mesmos valores; houve **zero erros de página, console, requisição ou HTTP**.

| Tema | Cor computada | Fundo ancestral composto | Razão recalculada |
|---|---|---|---:|
| claro, três seletores | `rgb(41,39,35)` (`#292723`); token computado `#292723` | `rgb(240,237,232)` (`#F0EDE8`) | **12,7658:1** |
| escuro, três seletores | `rgb(196,188,178)` (`#C4BCB2`); token v0.3 ausente | `rgb(32,33,31)` (`#20211F`) | **8,6109:1** |

As cadeias de pintura dos ancestrais não sinalizaram imagem, filter, opacity, blend ou backdrop-filter para esses alvos. As razões são calculadas a partir das cores CSSOM, não medidas em pixels nem uma avaliação completa de acessibilidade; os PNGs são recortes dos alvos sem contexto visual ao redor. Os recibos e seis capturas estão em `work/MobiliPresenter2D-G2-VIS002C-runtime-20261110/` no workspace desta conversa. `runtime-cssom.json` (43.744 bytes) SHA-256 `1d4a475c3e798ce38bb1b68280a7aac3222db7b7d94080a3af36b865f33161a6`.

**Limites do recibo original e complemento de cascata:** `runtime-cssom.json` continua sendo a captura DOM/CSSOM das seis combinações a 1440×900: seus valores computados e fundos foram medidos, mas a lista `matchingCssRules` original ficou vazia. Uma inspeção separada com Chrome DevTools em 2026-11-10 resolveu os vencedores para esses três consumidores nos dois temas; o relatório e seus limites estão em [VIS-002C cascade winner trace](vis002c-cascade-winner-trace-2026-11-10.md). A inspeção ocorreu em Chrome 156, viewport 766×608/DPR 1.5, com as folhas CSS do mesmo pin carregadas por file URL em ordem correspondente à página; o stylesheet Landing ainda registrou falha na importação absoluta, por isso v0.3 foi carregado explicitamente antes dele. Os vencedores reportados foram confirmados pelo painel CSS do DevTools, e as cores/contraste recalculadas no DOM coincidem com os valores do recibo. Isto fecha a lacuna de atribuição para os três seletores medidos, mas não é prova do CDN nem da navegação HTTP completa. O coletor Playwright `work/MobiliPresenter2D-G2-VIS002C-runtime-20261110/capture-next-unverified.cjs` (SHA-256 `04ba92b11ee983bf0e2295339b8da2e5e6cffc31e34c55835fe46b7996378bc7`) foi tentado em 2026-11-10; Edge encerrou antes da navegação ao falhar acesso ao perfil temporário (`-5`), sem criar CSSOM/capturas. Os seis recortes visuais anteriores mostram texto integral, sem avaliação do contexto completo. Não se inspecionaram `.study-band .eyebrow`, os cinco contextos adicionais da issue, outros contextos v0.3, `/config/`, ou acessibilidade global; #216 e G2 permanecem abertos.

A issue #216 permanece aberta até reconciliar seus critérios com a evidência/runtime atual e registrar a decisão de encerramento.

### Issue #208 — atualização estática no main pinado

Leitura estática de `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` indica que DS04-01 já está resolvido conforme a reconciliação da própria issue; DS04-03, DS04-04, DS04-05 e DS04-09 parecem atendidos por variáveis/overrides light em `app/admin/admin.css`; DS04-07 e DS04-08 parecem atendidos por overrides em `app/ui-theme.css` e pelo uso de `--text`. Ainda permanecem como candidatos estáticos DS04-02 (`app/access/manage.html`), DS04-06 (`app/styles.css`), DS04-10 (`app/styles.css`) e DS04-12 (`app/viewer/viewer.css`); DS04-11 continua documentado como exceção técnica intencional. DS04-13–16 são exceções/delimitações, não defeitos automáticos.

Esta reconciliação não executou DOM/CSSOM para Admin, Access/manage, Viewer ou estados interativos; “parece atendido” não confirma contraste final, e os candidatos restantes precisam de verificação contextual. A issue #208 e os 98 pares UNCERTAIN de `/config/` seguem abertos como trilhas separadas dentro de G2.

## Higiene de branches e limite de quantidade

Os limites leves informados pelo usuário são até 2 branches no Design System e até 5 no produto. Após abrir a PR #119, a observação atual encontrou **2 branches e 1 PR aberta** no Design System, e **3 branches e 1 PR aberta (#269, draft)** no produto. Ambos permanecem dentro dos limites; nenhuma remoção é necessária para respeitá-los. O procedimento do produto exige observação completa, plano com hash, reobservação, exclusão somente por SHA/lease quando elegível e readback integral. Nomes, idade, número de diretórios locais ou fechamento de PR não autorizam remoção. Os oito DAGs históricos do Design System estão sob tags protegidas conforme o último recibo; preservar essa retenção.

## Sequência de trabalho

1. Incorporar a fonte e os recibos do subgate DS-05A de modo reproduzível, preservando que o ajuste permanece local.
2. Retomar G1/G2 com #218, #208, #216 e o gate DOM/runtime DS-05A, sem ampliar o escopo visual.
3. Concluir ownership de G3 por rota/estado e selecionar um único piloto autorizado para G4/G5.
4. Reavaliar a arquitetura declarativa G6 após evidência dos componentes e manter G7 como gate para jornadas protegidas/dispositivos.
5. Atualizar este crosswalk com SHAs e resultados quando cada gate tiver evidência; não marcar G8 concluído sem validação integrada e autorização de release.
