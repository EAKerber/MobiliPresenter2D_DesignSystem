# Checkpoint atual da arquitetura G0–G8 — 2026-11-09

**Escopo:** reconciliação documental do plano de consolidação de Design System, CSS e componentes. Este checkpoint atualiza a fotografia operacional, não aprova mudanças visuais, migrações em lote, merge de código de produto ou publicação.

**Plano de referência:** [Plano diretor G0–G8](../../docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · [reconciliação anterior](master-plan-g0-g8-current-crosswalk-2026-10-25.md) · [handover e governança](../../docs/HANDOVER_CURRENT.md).

## Evidência verificada nesta retomada

- Design System: `main@79db735d6f05177b0c406e383d35832f3d72fdef` (último commit observado: 2026-10-27). Na leitura anterior à criação desta PR havia **1 branch e 0 PRs**; após sua abertura, a observação live é **2 branches e 1 PR aberta (#119)**.
- O workflow agendado [Branch hygiene #42655241742](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/42655241742) terminou em **success** em 2026-11-09. O endpoint de rulesets ainda lista ativo o ruleset #25953910 para `ds-history/2026-10-27/*`. O último readback documental confirma oito tags históricas protegidas; esta retomada não reenumerou individualmente seus objetos. Nenhuma branch foi removida nesta retomada.
- Produto: `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, **2 branches remotas** e **0 PRs abertas**. Além dos refs e issues, foram lidas as fontes CSS/HTML atuais de `main` para rastrear VIS-002C; nenhum arquivo versionado nem serviço remoto do produto foi alterado. Os recibos locais UX-04 ficaram como artefatos não versionados no worktree isolado.
- Issues observadas no repositório do produto: **#208, #216, #218 e #232 abertas**; **#217, #224 e #226 encerradas**. Isso corrige fotografias mais antigas que ainda listavam #217/#224/#226 como pendentes. Fechamento de issue não equivale a auditoria ampla ou aceitação de release.

## Estado operacional das fases

| Fase | Estado nesta retomada | Próximo gate verificável |
|---|---|---|
| **G0 — evidência e documentação** | **PASS como base de rastreabilidade; contínuo.** O handover local de 06/11 registra G0 PASS; esta retomada atualiza HEADs/issues live, mantendo os snapshots datados. | Continuar reconciliando mapas por domínio sem reescrever evidências históricas nem promovê-las automaticamente. |
| **G1 — navegação e foco** | **PARCIAL.** A execução local dos testes de navegador UX-04 e teclado passou no SHA atual `development@1a69ff76`; não há run Actions UX-04 nesse SHA. O workflow `.github/workflows/development-ux04-geometry.yml` com `workflow_dispatch` existe em `development`, mas está ausente de `main` (branch padrão); por isso a página Actions não oferece `Run workflow`. Esta retomada não publicou o workflow em `main` para habilitar o botão. O run remoto #42720598449 passou 124 cenários NAV-004/005, mas não é o gate UX-04. #218 continua aberta; #224/#226 estão fechadas. | Executar o workflow completo em Linux/Node 22, fechar #218 com evidência específica e completar os critérios restantes de touch, zoom e dispositivo real. |
| **G2 — CSS e acessibilidade** | **EM ANDAMENTO.** #208 e #216 seguem abertas; #217 está fechada. No `main@221b54b`, o DOM/CSSOM local executado nas três rotas originais de #216 confirmou o token/cor computada clara `#292723`, fundo composto `#F0EDE8` e 12,7658:1; no escuro, `rgb(196,188,178)` sobre `rgb(32,33,31)` e 8,6109:1. Seis contextos terminaram sem erros de página/rede. A captura não enumerou regras CSS correspondentes; ordem/precedência permanece sustentada pela leitura das fontes pinadas. As **98 incertezas UNCERTAIN** de `/config/` são outro escopo e continuam abertas. | Completar a captura de regras CSSOM correspondentes e reconciliar separadamente `/config/`, #208 e os critérios restantes de #216. Os seis recortes #216 foram revisados visualmente em 2026-11-10; os textos-alvo aparecem integrais e sem corte aparente, mas as imagens não mostram o contexto completo das seções. Não inferir conformidade global, cobertura de outros contextos v0.3 ou autorização para tokenização. |
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

Esses hashes identificam os objetos existentes no checkout; não comprovam por si só o método de geração, compatibilidade com o pin remoto ou revisão do patch. O runner, o recibo e a mudança de CSS continuam fora do repositório Design System; por isso o resultado ainda não é evidência reproduzível nele. O escopo é somente o DOM inicial montado de `/config/`; não cobre Admin, teclado, foco, hover/seleção/erro/loading/dock, tema `auto`, 320/768 px, screenshot review ou dispositivo real. **DS-05A permanece INCOMPLETO/HOLD.** Não promover o ajuste local para produto nem inferir aprovação visual.

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

**Limite da captura:** `getComputedStyle`, tema resolvido, lista/ordem de folhas carregadas e fundo composto foram obtidos do DOM/CSSOM executado. A coleta de `matchingCssRules` retornou arrays vazios por um erro no coletor ao percorrer `CSSStyleRule`; portanto, a atribuição da regra ativa na tabela acima é reconciliação da fonte e ordem estática, não trace de regra vencedora em runtime. A versão corrigida do coletor está guardada como `capture-next-unverified.cjs`, mas ainda não foi executada neste checkpoint; a enumeração runtime das regras vencedoras segue pendente. O registro é local e pinado; não prova os bytes atualmente servidos pelo CDN, Os seis recortes foram revisados visualmente em 2026-11-10 e mostram os textos-alvo integrais, sem corte aparente; essa inspeção não cobre o contexto completo das seções nem mede contraste por pixels. Abrange somente esses três contextos, nesse viewport e nesses temas explícitos; não fecha #216, os demais sete contextos v0.3, toda a acessibilidade ou a análise separada de `/config/`.

A issue #216 permanece aberta até reconciliar seus critérios com a evidência/runtime atual e registrar a decisão de encerramento.

### Issue #208 — atualização estática no main pinado

Leitura estática de `MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` indica que DS04-01 já está resolvido conforme a reconciliação da própria issue; DS04-03, DS04-04, DS04-05 e DS04-09 parecem atendidos por variáveis/overrides light em `app/admin/admin.css`; DS04-07 e DS04-08 parecem atendidos por overrides em `app/ui-theme.css` e pelo uso de `--text`. Ainda permanecem como candidatos estáticos DS04-02 (`app/access/manage.html`), DS04-06 (`app/styles.css`), DS04-10 (`app/styles.css`) e DS04-12 (`app/viewer/viewer.css`); DS04-11 continua documentado como exceção técnica intencional. DS04-13–16 são exceções/delimitações, não defeitos automáticos.

Esta reconciliação não executou DOM/CSSOM para Admin, Access/manage, Viewer ou estados interativos; “parece atendido” não confirma contraste final, e os candidatos restantes precisam de verificação contextual. A issue #208 e os 98 pares UNCERTAIN de `/config/` seguem abertos como trilhas separadas dentro de G2.

## Higiene de branches e limite de quantidade

Os limites leves informados pelo usuário são até 2 branches no Design System e até 5 no produto. Após abrir a PR #119, a observação atual encontrou **2 branches e 1 PR aberta** no Design System, e **2 branches e 0 PRs abertas** no produto. Ambos permanecem dentro dos limites; nenhuma remoção é necessária para respeitá-los. O procedimento do produto exige observação completa, plano com hash, reobservação, exclusão somente por SHA/lease quando elegível e readback integral. Nomes, idade, número de diretórios locais ou fechamento de PR não autorizam remoção. Os oito DAGs históricos do Design System estão sob tags protegidas conforme o último recibo; preservar essa retenção.

## Sequência de trabalho

1. Incorporar a fonte e os recibos do subgate DS-05A de modo reproduzível, preservando que o ajuste permanece local.
2. Retomar G1/G2 com #218, #208, #216 e o gate DOM/runtime DS-05A, sem ampliar o escopo visual.
3. Concluir ownership de G3 por rota/estado e selecionar um único piloto autorizado para G4/G5.
4. Reavaliar a arquitetura declarativa G6 após evidência dos componentes e manter G7 como gate para jornadas protegidas/dispositivos.
5. Atualizar este crosswalk com SHAs e resultados quando cada gate tiver evidência; não marcar G8 concluído sem validação integrada e autorização de release.
