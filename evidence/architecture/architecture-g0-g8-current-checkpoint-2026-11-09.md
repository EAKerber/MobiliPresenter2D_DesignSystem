# Checkpoint atual da arquitetura G0–G8 — 2026-11-12

**Última atualização:** 2026-11-12 (BRT).

**Escopo:** reconciliação documental do plano de consolidação de Design System, CSS e componentes. Este checkpoint atualiza a fotografia operacional, não aprova mudanças visuais, migrações em lote, merge de código de produto ou publicação.

**Plano de referência:** [Plano diretor G0–G8](../../docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · [reconciliação anterior](master-plan-g0-g8-current-crosswalk-2026-10-25.md) · [handover e governança](../../docs/HANDOVER_CURRENT.md).

## Fotografia operacional live — 2026-11-12 (BRT)

Esta fotografia prevalece sobre contagens, heads e resultados de CI anteriores no arquivo. Os recibos datados abaixo continuam como histórico de evidência.

- **Design System:** `main@79db735d6f05177b0c406e383d35832f3d72fdef`; 2 refs (`main` + `docs/architecture-status-20261109`), dentro da meta/soft cap de 2. Dois refs não são uma regra rígida: ao atingir 5, revisar se um hard cap é útil. A PR #119 continua Draft no ramo documental existente; o check de Branch hygiene deve ser revalidado a cada novo head. O ramo contém documentação e evidências, sem CSS de runtime ou código do produto.
- **Produto:** `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`; 7 refs (`main`, `development` e cinco branches de trabalho). O soft cap de 5 está excedido por 2 e exige revisão de crescimento, não exclusão automática. Quando estável, a meta é 2 refs (`main` + `development`). #273 continua Draft, baseada exatamente no SHA estável de `main`, no head `016b33f9315620ee09b28c4e2c9ba5752b858471` e 8 commits à frente; as mudanças de hero/vídeo e comparativos estão isoladas na PR. #270 está fechada sem merge. A #272 pinou a remoção exata de #270 e a limpeza condicional da própria branch após integração; se concluída, reduziria 7→5. Não houve integração ou exclusão.
- **PRs do produto:** #269 Draft (`2e202e4d7d36f29bfb62508bc15f40cdc18f130b`; Preview pronto); #271 aberta (`d699fb1911046dfbbc475fad9415f3ff3fca1cc8`; 4 arquivos; 9/9 Actions workflow runs e status do Netlify Deploy Preview concluídos com sucesso; `/config/` continua sem configuração publicada válida; o subgate visual/CSSOM dos labels do Admin já passou no Preview); #272 aberta (`227fcc86578833a9cf43d275de3e6bafc5eba1a9`; gates de higiene e Preview prontos); #273 Draft (`016b33f9315620ee09b28c4e2c9ba5752b858471`; 11 workflows aprovados e Preview pronto, revisão visual final pendente). A revisão visual da #273 não constitui fechamento dos gates G0–G8.
- **Estabilidade de `main`:** a comparação GitHub confirma #273 com base exata em `main@221b54b`, 8 commits à frente, 0 atrás; #269, #271 e #272 também permanecem sem merge. O conteúdo transitório das PRs não está em `main`. As regras de proteção de branch estão desativadas nas duas `main`; portanto, essa estabilidade ainda depende do fluxo de revisão, e não de uma regra técnica do GitHub.
- **G0–G8:** G0 contínuo; G1 parcial (UX-04 runner Linux/Node 22 e critérios touch/zoom/Safari/iPad de #218 pendentes); G2 em andamento (#208/#216, 98 pares UNCERTAIN, configuração de Preview inválida e DS-05A incompleto/HOLD); G3 parcial, com recaptura local de 28 casos em 7 rotas, 2 viewports e 2 temas, sem fixture privada; G4 HOLD; G5 parcial/HOLD; G6 HOLD; G7 pendente (#232/fixture autorizada); G8 release não iniciado.
- **Operações:** nenhuma branch de produto foi removida ou integrada nesta fotografia. Sem merge, deploy de produção, alteração de regra de proteção ou operação de banco.
## Estado operacional das fases

| Fase | Estado nesta retomada | Próximo gate verificável |
|---|---|---|
| **G0 — evidência e documentação** | **PASS como base de rastreabilidade; contínuo.** O handover local de 06/11 registra G0 PASS; esta retomada atualiza HEADs/issues live, mantendo os snapshots datados. | Continuar reconciliando mapas por domínio sem reescrever evidências históricas nem promovê-las automaticamente. |
| **G1 — navegação e foco** | **PARCIAL.** A PR draft #269 está no head 2e202e4d7d36f29bfb62508bc15f40cdc18f130b; Preview do mesmo commit pronto e 12/12 Actions passaram. A matriz hospedada cobriu 486, 321/320, 291/290, 900/901 e 1366 CSS px; Enter/Space, Tab, Escape e foco visível foram observados em Chromium. Detalhes no adendo G1 abaixo. #218 permanece aberta para toque real, zoom de navegador e Safari/iPad; UX-04 segue gate separado e não foi executado no SHA atual de development. | Executar UX-04 no SHA exato de development quando o workflow chegar a main; completar a validação em dispositivo/toque/zoom e fechar apenas os critérios comprovados de #218. |
| **G2 — CSS e acessibilidade** | **EM ANDAMENTO.** #271 continua aberta. **Admin:** o label claro de 10px mede 4,229:1 em Product `main`, 9,092:1 na regra candidata. Revisão autenticada no Preview #271, head `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`, conferiu 18 labels visíveis; CSSOM confirmou `#403A34`/`#EAE7E2` (9,092:1) em light e `#C4BCB2`/`#232321` (8,384:1) em dark. Nenhuma checkbox foi alterada ou salva. **Anel:** a recaptura A/B local corrigida inclui 32 capturas: 16 sem hover (`transform:none`) e 16 com hover (`matrix(1.06, 0, 0, 1.06, 0, 0)`); todos os casos Buyer V5 são válidos e mantêm seleção real; relatório, JSON e PNGs estão vinculados em [G2 selected ring](g2-selected-finish-ring-2026-11-12.md). A recaptura anterior de 8 combinações de tema/viewport continua documentando headings e `#viewerHint`; não é a evidência do anel. `/config/` hospedado ainda não valida sua configuração publicada, portanto o anel aguarda revisão hospedada. #208/#216, 98 pares UNCERTAIN e DS-05A permanecem pendentes. | Resolver a configuração publicada/obter fixture autorizada para revisar o anel em hospedagem e concluir os critérios restantes de #208/#216; manter 98 pares e DS-05A em HOLD até resolver suas incertezas. |
| **G3 — ownership CSS/DOM** | **PARCIAL.** A recaptura local fixada em main@221b54b cobriu 7 rotas, 2 viewports e 2 temas (28 casos): preferência, tema do documento e API concordaram; os src das imagens de marca corresponderam ao tema; o logo do cabeçalho carregou em todos; 0 exceções de página. O controle percorreu as transições previstas. Slots e caixas continuam contextuais por shell. O recibo também registra 28 HTTP 404 de bundles/APIs sem fixture; configuração publicada, sessão autenticada, menu privado, foco/hover e revisão visual não foram validados. [Relatório e recibo G3](g3-theme-controller-slots-recapture-2026-11-11.md). | Validar foco/hover no Preview público/Viewer e shell privado com fixture autorizada; considerar cobertura cross-platform. Preservar slots contextuais e não extrair CSS antes de evidência adicional. |
| **G4 — foundations, tokens e acessibilidade compartilhável** | **HOLD.** Fonte de referência e decisões aprovadas não demonstram integração abrangente; o handover local de 06/11 mantém G4 em HOLD. | Retomar somente após resolver as incertezas visuais/runtime de G2/G3 e definir o consumidor autorizado. |
| **G5 — famílias de componentes CSS** | **PARCIAL na candidata; HOLD na baseline.** O handover local de 06/11 mantém probes/famílias e incertezas sem consolidação homologada. | Fechar associação de probes e incertezas por família e obter comparação funcional/visual antes de compartilhar regras. |
| **G6 — composição e arquitetura de páginas** | **HOLD.** A direção Vanilla e ownership por domínio continua documentada; a composição declarativa segue experimental. Evidência local recente mantém G6 em HOLD enquanto G4/G5 e cobertura de domínio não fecham. | Reavaliar um piloto mínimo depois de G1–G5, com autoridade de dados explícita e sem criar framework genérico. |
| **G7 — hardening entre plataformas** | **PENDENTE.** #232 permanece aberta; o crosswalk anterior registra que WebKit headless não substitui Safari/iPad real e que validação autenticada exige fixture autorizada. | Resolver a fixture/CI protegida e completar jornadas críticas sem contornar autenticação. |
| **G8 — aceitação e release** | **NÃO INICIADO COMO RELEASE.** Não há autorização de publicação neste checkpoint. | Somente após revisão humana, integração autorizada, validação na base integrada e readback pós-release. |

## UX-04 — foco após redesenho do puxador

A varredura dos subdiretórios localizou o relatório de trabalho `docs/work/DEVELOPMENT_UX04_GEOMETRY_FOCUS_2026-10-28.md`. O gate dedicado mais recente verificado no GitHub é [#41344513485](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/41344513485), **success** no SHA `c7c2822d5b651ae0bcfcf0ac28c66cb61b645e98`; os jobs de intenção estática/proveniência e browser local passaram, incluindo geometria V5, restauração de foco e a suíte completa de teclado. O HEAD remoto atual de `development` é `1a69ff76a5f36e3245a288773bb409aa662e4e62`; a leitura da fonte confirma a chamada de retorno ao foco com `section:handles`. [O run exato deste HEAD](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/42720598449) passou 124 cenários públicos NAV-004/005, que são outro gate. Não há run GitHub Actions UX-04 nesse SHA. Como reexecução local do mesmo código, foram rodados no worktree isolado em `development@1a69ff76a5f36e3245a288773bb409aa662e4e62` o teste `tests/ci/ux04-geometry-focus-v5.cjs` e a suíte `tests/keyboard-browser.cjs`: **ambos PASS** em Chromium 151.0.7922.34 / Playwright 1.62.1, com fixture local V5 derivada dos defaults versionados e servidor temporário apenas em loopback. A medição confirmou o layout side-rail em 1366 px, o layout lado a lado em 1050 px, o modo compacto sem overflow em 390 px e retorno do foco ao controle selecionado após redraw; a regressão completa de teclado também passou. Não houve erro de página/console no diagnóstico UX-04.

Esta execução local usou Windows, Node 24.20.0 e Python 3.14.6 (o workflow usa Ubuntu e Node 22). Os cinco testes de `test_development_ux04_authority.py` passaram depois de buscar o objeto histórico de origem `5d8347edb6ea247307b6fc27b424117553542f78` para `FETCH_HEAD` (sem mover refs); build, `pages:check`, os três testes Node de flow/model/hierarquia, a checagem sintática do runner e os dois testes de navegador também passaram. Portanto, isto é **evidência local reproduzível no SHA exato**, não resultado de Actions nem validação cross-platform completa. Os recibos JSON locais estão em `work/MobiliPresenter2D-ux04-gate-1a69ff76/artifacts/ux04-local-gate/{geometry,keyboard}/result.json` no workspace do projeto; SHA-256: geometria `e14c57c1be881ff8950bd9b9e1a21cdcca04b937b41433bc9f1284d7440b82d5`, teclado `68c9d7a999d7b703c5ed7d2c75d76f64ddf2a6d0ad14b8ad8fd1fd903629bc91`.

UX-04 é o foco do Configurador após redraw; a issue #218 é a geometria/contrato NAV-005 do cabeçalho público. São gates distintos e não devem ser tratados como resolvidos um pelo outro. O G1 segue parcial até haver execução integral do workflow no runner Linux/Node 22, fechamento dos critérios específicos de #218 e cobertura de touch, zoom e dispositivo real.

### Issue #218 / NAV-005 — crosswalk estático e candidato hospedado

A leitura estática pinada continua mostrando a divergência descrita em #218 em main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95. Em development@1a69ff76a5f36e3245a288773bb409aa662e4e62, a correção candidata permanece escopada ao shell público: rótulo do tema, marca responsiva, CTA dentro do menu compacto e reflow abaixo de 291 px.

A PR #269 seletivamente leva esse contrato ao produto, sem alterar Viewer/headers privados. Seu estado atual e as medições de Preview no head 2e202e4d7d36f29bfb62508bc15f40cdc18f130b estão registrados no adendo G1 no fim deste checkpoint. A inspeção é evidência de Preview, não prova de integração em main/development; #218 permanece aberta para os critérios ainda sem dispositivo real, toque e zoom de navegador. UX-04 continua independente.

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

Esses hashes identificam os objetos existentes no checkout; não comprovam por si só o método de geração, compatibilidade com o pin remoto ou revisão do patch. O runner e o recibo da execução de 2026-11-10 foram preservados em [evidence/ds05a-runtime-2026-11-09](../ds05a-runtime-2026-11-09/README.md), junto com o patch CSS candidato mantido como arquivo inerte. O recibo original veio de checkout local sujo: a árvore app/ coincide com development@1a69ff76a5f36e3245a288773bb409aa662e4e62, exceto pela declaração candidata adicional em .module-number. A versão exata do Chromium/Node não foi registrada no recibo; o pacote preserva os inputs e o limite, mas ainda não é reprodução independente nem gate fechado. O escopo é somente o DOM inicial montado de `/config/`; não cobre Admin, teclado, foco, hover/seleção/erro/loading/dock, tema `auto`, 320/768 px, screenshot review ou dispositivo real. **DS-05A permanece INCOMPLETO/HOLD.** Não promover o ajuste local para produto nem inferir aprovação visual. Errata 2026-11-11: o recibo foi capturado após aplicar essa regra; 13,02:1/8,10:1 são somente pós-patch, sem baseline A/B nem prova do defeito anterior. Não adotar a regra; ver errata no handover.

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

### Atualização do trace local — 2026-11-10

O relatório [VIS-002C cascade winner trace](vis002c-cascade-winner-trace-2026-11-10.md) substitui a delimitação anterior de apenas três consumidores: a captura ampliada resolve dez seletores v0.3 (14 elementos) nas três rotas públicas e a exceção `.study-band .eyebrow`, em light/dark. As regras vencedoras são `landing.css:209`, `how-it-works.css:312` e `about.css:54` para os contextos v0.3 em light; as regras base via `--public-muted` continuam em dark. A exceção conserva `#70522F` em light e `--public-accent` em dark. Os valores computados e razões estão no relatório atualizado.

**Limite que permanece:** as folhas foram carregadas diretamente para inspeção de HTML local `file://`, com dados/JS dinâmicos da Landing carregados de arquivos do mesmo pin. Isto fecha somente a atribuição local dos winners; não prova a rota HTTP/CDN, não conclui #216, e não fecha #208, DS-05A nem os 98 pares UNCERTAIN de `/config/`.

### Issue #208 — atualização estática no main pinado

Leitura estática de `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` indica que DS04-01 já está resolvido conforme a reconciliação da própria issue; DS04-03, DS04-04, DS04-05 e DS04-09 parecem atendidos por variáveis/overrides light em `app/admin/admin.css`; DS04-07 e DS04-08 parecem atendidos por overrides em `app/ui-theme.css` e pelo uso de `--text`. Ainda permanecem como candidatos estáticos DS04-02 (`app/access/manage.html`), DS04-06 (`app/styles.css`), DS04-10 (`app/styles.css`) e DS04-12 (`app/viewer/viewer.css`); DS04-11 continua documentado como exceção técnica intencional. DS04-13–16 são exceções/delimitações, não defeitos automáticos.

Esta reconciliação não executou DOM/CSSOM para Admin, Access/manage, Viewer ou estados interativos; “parece atendido” não confirma contraste final, e os candidatos restantes precisam de verificação contextual. A issue #208 e os 98 pares UNCERTAIN de `/config/` seguem abertos como trilhas separadas dentro de G2.

## Higiene de branches e limite de quantidade — estado live 2026-11-11

A meta quando estável é 2 refs por repositório; 5 refs é o gatilho para revisar o crescimento e considerar se um limite rígido é necessário. Nenhum número autoriza exclusão por contagem. Design System está na meta com 2 refs: `main` e branch ativa da #119. Produto está em 7: `main`, `development` e branches #269–#273, com #270 fechada sem merge; a revisão do inventário está atrasada em relação ao gatilho 5. A #272 prepara somente a retirada da ref fechada #270@`219d9e672bf390a7af4b5815d50f9ea15f723913` e a limpeza condicional da própria branch após integração; segue sem merge/apply/readback. Isso reduziria 7→5, ainda com branches ativas. A PR #273 está Draft, baseada no SHA atual de `main`, e suas mudanças permanecem isoladas; suas duas falhas de CI continuam registradas no bloco live acima.

## Sequência de trabalho — próximo percurso G0–G8

1. G1: preservar o resultado hospedado de #218; fechar o workflow UX-04 em development e completar o recorte de touch/zoom/Safari-iPad que não é reproduzível no Chrome emulado.
2. G2: continuar #208/#216 com CSSOM e revisão visual no estado/configuração válido; obter baseline pareada, hashes de CSS e cobertura de estados antes de adotar qualquer regra DS-05A.
3. G3: completar ownership por consumidor, estado, tema e cascata; classificar igualdade, variante, homônimo, exceção ou incerteza.
4. G4/G5: só extrair tokens/utilitários/famílias quando o contrato e o ganho forem demonstrados; zero extração é resultado válido se não houver duplicação equivalente.
5. G6: manter composição declarativa experimental até haver segundo consumidor editorial com ownership claro; não criar framework genérico.
6. G7/G8: fechar jornadas protegidas e plataforma/dispositivo; somente depois conduzir revisão integrada, aceitação e release autorizado.

## Snapshot operacional anterior — 2026-11-11 (BRT; superseded)

| Fase | Estado confirmado | Próximo gate verificável |
|---|---|---|
| **G0 — evidência e documentação** | **PASS como base de rastreabilidade; contínuo.** Este checkpoint e o handover foram atualizados a partir dos HEADs e Actions atuais. | Continuar por domínio, preservando evidências históricas e limites. |
| **G1 — navegação e foco** | **PARCIAL.** PR #269 draft está em `2533a66376a016bcb8442e401de8933cb5a1edb4`, 19 arquivos e 12/12 Actions success. O único acréscimo desde a UI visualmente revisada (`19bbf9d...`) é `.github/workflows/development-ux04-geometry.yml`, idêntico ao arquivo em `development`; a árvore de produto não mudou. O workflow tem `workflow_dispatch`, mas ainda não está em `main`, então UX-04 continua sem execução no SHA `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`. #218 continua aberta; faltam toque, zoom, foco integral e dispositivo. | Depois que o workflow chegar à branch padrão por revisão da PR, disparar UX-04 no SHA exato então vigente de `development` e concluir os critérios restantes de #218. O Preview da UI em desktop/390 px não substitui Safari/iPad. |
| **G2 — contraste e tokens** | **EM ANDAMENTO.** PR #271, head `6030eec03e8dad0c91672744b59b9c63080ce835`, tem 8 verificações de Actions success. No Preview `6af3e14b24bd296921873555`, após login no mesmo host por Admin, Viewer (390×844, light/dark) e CTA de Access/manage foram revistos pontualmente. A lista de acessos reportou erro de serviço. `/config/` autenticado abriu o shell mas falhou ao validar a configuração publicada; títulos/anel seguem sem revisão hospedada. #208/#216 abertas; 98 pares UNCERTAIN; DS-05A incompleto/HOLD. | Resolver a configuração publicada/serviço do Preview para concluir os critérios restantes; não publicar dados nem inferir a partir do shell transitório. |
| **G3 — ownership** | **PARCIAL.** A matriz cobre cinco famílias iniciais e agora separa menu público e menu privado por HTML/CSS/JS, foco, estado de sessão e consumidores. A análise é estática; variantes e estados de runtime restantes não estão validados. | Prosseguir com marca/ícone/slots e estados de CSS/runtime, sem extração antes do gate. |
| **G4 — tokens compartilhados** | **HOLD.** | Não extrair tokens amplamente antes dos gates G2/G3. |
| **G5 — componentes** | **PARCIAL/HOLD.** | Selecionar piloto após ownership e critérios verificados. |
| **G6 — arquitetura declarativa** | **HOLD.** | Reavaliar após evidência de componentes e propriedades. |
| **G7 — jornadas protegidas/dispositivos** | **PENDENTE.** | Validar em contextos autorizados, incluindo dispositivos pertinentes. |
| **G8 — integração/release** | **NÃO INICIADO como release.** Nenhum PR foi mesclado nem houve deploy de produção. | Gate integrado, revisão e autorização própria. |

**Higiene de branches:** reconsulta retornou 5 branches no produto e 2 no Design System. #270 está fechada sem merge: branch `codex/ds04-208-css-contrast-20261111` em `219d9e672bf390a7af4b5815d50f9ea15f723913`, `protected=false`. A comparação com a branch de #271 (`6030eec03e8dad0c91672744b59b9c63080ce835`) não encontrou arquivos diferentes; #271 é dois commits adiante, mesma árvore. É candidato técnico, ainda sem autorização terminal por SHA. A revisão do método encontrou que `branch_hygiene_plan.py` registra essa disposição, mas `select_bounded_batch()` só aceita ancestralidade com `main` ou prova de squash merge; portanto o executor atual não aceita o #270 fechado/não mesclado. Não apaguei diretamente nem inventei batch. Inventário permanece 5/5 e cap respeitado.

**Limites de validação:** inspeção do #269 foi visual e pontual no navegador do ChatGPT. As Actions medem os gates automatizados configurados para cada SHA; não comprovam UX-04 nem os critérios físicos/assistivos restantes. A tela de acesso do #271 reteve o gate válido; nenhuma autenticação foi tentada ou contornada.


## Adendo — G3 ownership inicial e acesso administrativo (2026-11-11)

O inventário [CSS ownership/risk](../../docs/architecture/CSS-OWNERSHIP-RISKS-2026-10-20.md) agora registra uma primeira classificação por família, baseada em `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`: `.visually-hidden` tem declaração igual em bundles de rota separados, mas ganho de extração não demonstrado; `.eyebrow` e `.button` são variantes/homônimos de domínio; `.scene-hotspot` é indeterminado e de alto risco; `.site-header` é shell público compartilhado com variação por página e #218 ainda aberto. Esta é evidência estática e documental; **G3 permanece parcial** até cobrir estados e consumidores restantes. Nenhuma mudança de CSS ou extração foi feita.

O usuário informou que entrou como administrador. No host #269, `/admin` mostrou a sessão administrativa e `/config/` abriu o shell, mas depois exibiu erro de validação da configuração publicada; isto não confirma estados interativos nem visualização funcional. No host #271, `/admin` ainda exigiu entrada e `/config/` redirecionou ao acesso sem token válido. Não houve revisão visual autenticada do código G2 de #271. Os gates de G2/G7 seguem abertos.


## Adendo — revisão G2 após login administrativo no host #271 (2026-11-11)

O Viewer foi inspecionado no Preview exato #271 a 390×844 CSS px em tema escuro e claro. Os quatro pontos de navegação ficaram visíveis; o ativo e os inativos se distinguiram. Valores CSSOM dos pontos inativos: dark `rgb(196, 188, 178)`, light `rgb(112, 108, 102)`; 7×7 px. Na rota `/access/manage.html`, o CTA de tema escuro computou `rgb(41,39,35)` sobre `rgb(226,201,145)`, razão 9,23:1, e foi visualmente confirmado. A própria página informa falha ao carregar os acessos recentes.

A sessão Admin abriu `/config/`, mas a validação da configuração publicada falhou e a tela ficou indisponível; títulos de seção e anel de acabamento ainda não têm revisão visual hospedada. Não houve envio de convite, mudança de dados ou publicação. Este subgate cobre apenas os pontos observados, não fecha #208 ou G2.


## Adendo — G3: menu público e privado (2026-11-11)

No pin `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, foi ampliada a matriz de ownership: o menu público estático de Landing/How/About usa `landing/header-menu.js` e layout `menu-open`; os menus de Admin e Access são montados pelo controlador de sessão `core/private-navigation.js`. Ambos compartilham tokens/tema, porém usam DOM, controladores, foco e estados de autorização distintos. O detalhamento, ordem das folhas e referências está no inventário CSS ownership. A conclusão é documental/estática: G3 continua parcial, sem promoção de CSS.

**Correção operacional do Preview #271:** o login administrativo foi concluído no host exato. A rota `/admin` carregou a hierarquia; `/config/` autenticado continuou indisponível por falha de validação da configuração publicada. O Viewer e CTA de Access/manage tiveram revisão visual pontual conforme adendo anterior. Nenhuma configuração foi publicada/salva, convite enviado, ou branch removida.


## Adendo — G3: marca e controle de tema (2026-11-11)

A leitura estática do pin `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` confirmou que `core/ui-theme.js` é o dono do modo auto/light/dark, da preferência local/sistema, dos assets de logo e do rótulo/slot do controle. A mesma lógica atende Landing/How/About, Viewer, Config, Admin e Access; os slots e as dimensões continuam contextuais. G3 permanece parcial: falta observar CSSOM/primeira pintura e interação em cada rota/tema, em especial nas telas privadas.



## Evidência hospedada adicional — G2 / issue #216 (2026-11-11, BRT)

No Deploy Preview #271, commit 6030eec03e8dad0c91672744b59b9c63080ce835, viewport 503×667 CSS px, tema alternado explicitamente entre light/dark e restaurado a dark ao final. Rotas públicas /, /how-it-works/, /about/ foram servidas pelo preview atual. CSSOM vencedor, conteúdo visível e contraste calculado no DOM:

| Rota/seletor | Light (foreground / fundo; razão) | Dark (foreground / fundo; razão) |
|---|---|---|
| / · .hero-description | #292723 / #F0EDE8; **12,77:1** | #C4BCB2 / #20211F; **8,61:1** |
| /how-it-works/ · .how-hero-note | #292723 / #F0EDE8; **12,77:1** | #C4BCB2 / #20211F; **8,61:1** |
| /about/ · .about-scale p:not(.eyebrow) (3 parágrafos) | #292723 / #F0EDE8; **12,77:1** | #C4BCB2 / #20211F; **8,61:1** |
| /how-it-works/ · .study-band .eyebrow (exceção) | #70522F / #E8E3DC; **5,60:1** | #D8BC7C / #20211F; **8,78:1** |

Issue #216 lista #675F55 como par aprovado para os três textos claros; o preview atual usa o token #292723, com contraste superior, mas essa diferença não é tratada como equivalência estética aprovada. A inspeção confirma somente esses seletores/temas no preview: não substitui revisão visual integral, não fecha #216, não cobre os cinco consumidores adicionais, #208, Configurador/98 pares UNCERTAIN ou DS-05A. G2 continua em andamento.

## Higiene do produto — lote exato #270 preparado (2026-11-11, BRT)

No momento em que o lote foi preparado, antes da abertura da PR #273, havia 6 refs no produto. A PR #273 elevou o inventário live para 7; ver a fotografia atual no início deste checkpoint. O usuário autorizou preparar o lote exato para codex/ds04-208-css-contrast-20261111@219d9e672bf390a7af4b5815d50f9ea15f723913, head da PR #270 encerrada sem merge e sucedida por #271. A PR [#272](https://github.com/EAKerber/MobiliPresenter2D/pull/272) permanece aberta/mergeável em `5ebe09b8b0fe8c868ed9f26da8b41bb5c4af1326`; os 3 workflow runs Actions e o Deploy Preview passaram, sem review humana observada. Não houve merge nem remoção; o apply do #270 requer integração da #272 e readback PASS. A branch temporária #272 só será removida pelo cleanup condicional após evento de PR merged e revalidação exata. Não considerar o lote executado antes dos recibos/readback.



## G3 — runtime do controlador de tema no Preview (2026-11-11, BRT)

Captura em Deploy Preview #271, head `86c4945cb56c04df31954e2a02f66ca3e703dc67`, Chrome 156, viewport 503×667 CSS px / DPR 1,5, reduced motion. Contexto isolado sem credenciais, limitado às páginas públicas.

- Nas rotas `/`, `/how-it-works/` e `/about/`, o controle teve a mesma classe `ui-theme-toggle ui-theme-toggle--header` e dimensões 44×44 px no slot do cabeçalho.
- `data-theme-mode=auto` acompanhou as preferências do sistema: claro resolveu para `data-theme=light` e `logo-light-380.png`; escuro resolveu para `data-theme=dark` e `logo-dark-380.png`.
- Na Landing, o foco por teclado ficou visível (outline 2,67 px); Enter percorreu `auto → light → dark → auto`, com rótulos acessíveis atualizados. `casa-ui-theme-mode-v1` guardou o modo e `auto` persistiu ao navegar para How/About.
- CSSOM atribuiu a geometria compacta ao seletor compartilhado em `ui-theme.css:61/73`. A ordem das folhas foi pública comum + CSS de página + `ui-theme.css`, variando por rota. Evidência sustenta controlador compartilhado e slots contextuais, não extração CSS nem equivalência de shell.

**Limites:** uma largura/viewport, media preferences simuladas em Chrome, sem toque real, Safari/iPad, dispositivo móvel, Viewer ou páginas privadas. `/config/` no contexto isolado redirecionou a `/access/`; nenhuma autenticação foi contornada. A evidência é pontual do Preview e não fecha G3.

## Errata DS-05A — números dos módulos (2026-11-11, BRT)

O recibo local `runtime_cssom.json` já continha a regra experimental `.module-number` (fundo `rgba(34,33,31,0.08)`). Logo 13,02:1 em light e 8,10:1 em dark descrevem apenas o estado após aplicar a regra; não existe par prepatch nem delta atribuído. O JSON não fixa o blob da folha CSS carregada. A candidata não é finding nomeado em #208, não teve revisão visual e permanece no checkout local. A descrição “corrigir o defeito” foi corrigida para “regra experimental” no relatório DS-05A local. Não copiar para refs do produto sem captura A/B repetível, hashes por braço, cobertura de estados e revisão visual/decisão de design.

## G1 — revisão hospedada NAV-005 / #218 (2026-11-11, BRT)

Pin: produto #269, codex/nav005-public-compact-main-20261110@2e202e4d7d36f29bfb62508bc15f40cdc18f130b, baseado em main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95. Deploy Preview #269 estava ready no mesmo commit (deploy 6af3fe0e739df32bb5500109); os 12 workflow runs de Actions desse SHA concluíram success. Chrome DevTools em emulação desktop CSS/DPR, reduced motion, sem dispositivo físico.

| Contexto | Resultado observado |
|---|---|
| 486×590, light, How | Marca 145,8 px (9% menor que 160 px; limite exigido de redução ≤30% preservado); rótulo visível Auto; toggle tema imediatamente antes do menu, ambos dentro do header; ao abrir, links públicos e WhatsApp ficam no menu e dentro do viewport. |
| 321×844, dark | Marca 112 px; Auto visível; header uma linha; controles dentro da área útil. |
| 320×844, dark | Marca 112 px; scrollWidth=305 ≤ innerWidth=320; menu e CTA do WhatsApp visíveis ao abrir. |
| 291×844, dark | Marca 112 px; header permanece em uma linha; menu/CTA dentro da área útil. |
| 290×844, dark | Header muda para duas linhas (122,6 px); marca 145 px e controles na segunda linha; menu aberto inclui CTA sem overflow horizontal. |
| 900/901×844, light | 900 usa header compacto com CTA no menu; 901 mantém header largo, nav e CTA em .header-actions. |
| 1366×844, dark; /, /about/, /how-it-works/ | Mesma classe/geometry pública do cabeçalho; CTA largo na área de ações; sem overflow horizontal. |
| 390×844, dark; /viewer/ | Continua viewer-header próprio, sem overflow horizontal; a regra pública não mudou o contrato do Viewer. |

Em 486×590, Enter e Space abriram o menu e focaram Ambientes; Tab percorreu os links e chegou ao WhatsApp; Escape fechou e devolveu foco ao botão de menu. O foco visível mediu 2,67 px: marrom no tema claro e dourado no escuro. Os alvos de menu observados tinham 42–44 px de altura.

Mudança aplicada ao candidato: app/landing/landing.css passou de clamp(112px, 36vw, 160px) para clamp(112px, 30vw, 160px) em .site-header--public .brand. Isso reduz a marca progressivamente até o mínimo 112 px (70% da largura-base de 160 px) antes do reflow; a exceção ≤290 px mantém o layout em duas linhas.

Limites: revisão em Preview isolado/Chrome emulado, não em Safari/iPad ou dispositivo touch real; zoom de navegador 200% ainda não observado. Não fecha UX-04, que exige execução no SHA exato de development depois que o workflow estiver na branch padrão. #218 segue aberta até concluir esses critérios. Nenhuma integração, deploy de produção ou mudança em Viewer ocorreu.


## G2 — comparação local pareada do Configurador (2026-11-11, BRT)

Para contornar a configuração inválida do Preview sem tocar em dados hospedados, foi montada uma fixture local anônima a partir dos defaults Buyer V5 versionados em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. O braço candidato usa o CSS da PR #271 com blob `eb346a41ad91f6dc53875cb954e9018fdc1dd713`; a base de `styles.css` é o blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`. Chrome `156.0.8078.82`, DPR 1, viewport 1366×900 e 390×844 CSS px, light/dark. Não houve Netlify, banco ou autenticação nesta fixture.

Nos quatro screenshots pareados, os candidatos mostram legibilidade dos títulos do Configurador e da dica `#viewerHint` no estado claro; a seleção de acabamento passa a ter anel de dois tons. No screenshot escuro 1366×900, os mesmos elementos também aparecem claros sobre superfícies escuras. Porém, a linha correspondente no `result.json` registra cores/fundo equivalentes ao tema claro. O arquivo não registra o `data-theme` efetivo nem associa cada linha ao hash do screenshot; por isso, a linha de contraste do candidato escuro 1366×900 não é evidência válida. O screenshot correspondente tem SHA-256 `63E25279CA9CB2E28FF4106C16CB09C7D83F0D6454EFDFFFB3045AE5B9AC999A`; `result.json` tem SHA-256 `12ACAD647F84F94D1CB92CB6F6B5D88416AC71411F620803B5AB1909A454F0E5`. Os demais dados não são invalidados automaticamente, mas as razões de contraste só devem ser reutilizadas após vinculação inequívoca a estado, viewport e captura.

A fixture registrou uma requisição 404 para `/core/private-navigation.bundle.js` porque a bundle local não foi construída. A página do Configurador renderizou e não houve exceção JavaScript; ainda assim, o diagnóstico não cobre navegação privada nem autenticação. Isto é evidência local exploratória dos contextos capturados, não valida a configuração publicada, não substitui revisão hospedada e não fecha #208, #216, G2 ou DS-05A.
## G2 — recaptura local pareada do Configurador (2026-11-11, BRT)

A divergência entre a linha escura candidata de 1366×900 e a aparência do screenshot na captura anterior não se repetiu na recaptura com o modo escrito no `localStorage` antes da navegação, conferência de `data-theme` e `CASA_UI_THEME.getResolved()`, e SHA-256 registrado em cada screenshot. Não foi atribuída uma causa raiz à discrepância antiga; aquela linha permanece histórica e excluída.

Os oito casos usaram o commit limpo `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `styles.css` base blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868` e o blob exato da PR #271 `eb346a41ad91f6dc53875cb954e9018fdc1dd713`. Edge `157.0.4341.46`, DPR 1; 390×900 e 1366×900, light/dark, base/candidata; Buyer V5 local derivado dos defaults versionados. Em todos, modo solicitado, atributo raiz e API coincidiram; status da configuração = `validated`; zero exceções de página. A mudança aplica os tokens existentes nos dois alvos observados. O 404 de `/core/private-navigation.bundle.js` registra somente a bundle privada ausente no checkout sem build; navegação privada/autenticação não fazem parte desta evidência.

O [relatório G2](g2-configurator-recapture-2026-11-11.md), os oito screenshots e `result.json` preservam valores CSSOM e hashes. Esta recaptura confirma o subgate de pareamento/reprodução; não valida a configuração hospedada, o anel selecionado, os 98 pares UNCERTAIN ou a cobertura completa de #208/#216. **G2 permanece em andamento; DS-05A permanece incompleto/HOLD.**


## G3 — recaptura local do controlador de tema e slots de marca (2026-11-11, BRT)

A matriz local sobre produto main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95 cobriu sete rotas, 390×900 e 1366×900 CSS px, light/dark: 28 casos. A preferência inicial, documentElement.dataset.theme e CASA_UI_THEME.getResolved() concordaram em todos; cada src de marca correspondeu ao asset esperado. O logo de cabeçalho carregou em todos os casos e o botão percorreu duas transições em cada um. Não houve exceções JavaScript de página.

As rotas usaram slots diferentes no shell público, Viewer, Config, Admin e Access, com caixas de controle contextuais. O recibo registrou 28 respostas HTTP 404: bundles e APIs privadas sem fixture, inclusive buyer-configuration em /config/. A sessão foi forçada para anônima. O estado visual de menus privados, configuração publicada, foco/hover, interação autenticada, touch ou Safari/iPad não foi validado. Duas imagens de marca dos cards comparativos em /how-it-works/ a 390 px informaram complete=false no momento da leitura, embora tivessem currentSrc e naturalWidth=380; os logos dos cabeçalhos estavam carregados. Não houve screenshots neste subgate.

O pacote [G3 recapture](g3-theme-controller-slots-recapture-2026-11-11.md), [recibo JSON](g3-theme-controller-slots-recapture-2026-11-11/result.json) e runner local registra os detalhes e limites. A recaptura confirma o comportamento do controlador e a seleção dos assets no shell estático; mantém G3 parcial e não autoriza unificar os slots ou extrair CSS.

## G2 — Admin initial-state labels (2026-11-12, BRT)

The new [local CSSOM recheck](g2-admin-initial-state-labels-cssom-2026-11-12.md) uses Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` and the actual Admin hierarchy renderer. Eighteen labels rendered at 1036×582 CSS px. Light mode resolves `#706C66` over `#EAE7E2` to **4.229:1**, below the 4.5:1 issue #208 threshold; dark mode resolves `#C4BCB2` over `#232321` to **8.384:1**. The later shared-theme rule for the light card background overrides the earlier Admin white-card rule and explains the effective surface.

A local candidate, `html[data-theme="light"] .hierarchy-item .initial-state-option { color: var(--control-text); }`, resolves to `#403A34` over the unchanged `#EAE7E2`, **9.092:1**. It is on the existing Product [#271](https://github.com/EAKerber/MobiliPresenter2D/pull/271) branch at head `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`; checks and the refreshed Preview were pending at capture time. No product code was merged and Product `main` remains unchanged. The fixture stubbed Identity/config fetch and does not replace hosted authentication. #208 and G2 remain open.


## Revalidação após a publicação — Product #271 (2026-11-12, BRT)

A API confirmou nove workflows de PR e o status `netlify/mobilipresenter2d/deploy-preview` com `success` para `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`. O Admin hospedado foi revisado com autenticação: 18 labels, 9,092:1 no light e 8,384:1 no dark, sem alteração de checkbox; veja o [recibo](g2-admin-initial-state-labels-cssom-2026-11-12.md). A rota `/config/` continua falhando na validação da configuração publicada. Product `main` permanece em `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, sem merge, remoção de refs, deploy de produção ou operação de banco.


## Revalidação final — Admin e recaptura sem hover (2026-11-12, BRT)

O subgate visual/CSSOM hospedado dos labels do Admin na Product #271 passou: 18 labels `.initial-state-option` visíveis no Preview autenticado, todos habilitados e já marcados; sem interação ou salvamento. O candidato mediu 9,092:1 no tema claro; o resultado escuro permaneceu 8,384:1. O recibo registra seletores, cascata, dimensões, hashes das capturas e limitações. O valor de `/config/` continua inválido, portanto este resultado não revisa o ring hospedado nem fecha #208/G2.

As 16 capturas no-hover do anel foram substituídas por PNGs com `transform:none`; uma segunda matriz adicionou 16 capturas hover, com `transform=matrix(1.06, 0, 0, 1.06, 0, 0)` estabilizado. Nos 32 casos, a seleção real, `aria-pressed=true`, Buyer V5 e tema corresponderam; 0 erros de página. Os hashes dos PNGs foram conferidos. O resultado cobre hover somente no swatch selecionado; foco/teclado, zoom e Safari/iPad continuam pendentes.
