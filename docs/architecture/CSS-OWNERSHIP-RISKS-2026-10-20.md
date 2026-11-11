# Inventário operacional — ownership CSS, riscos, lacunas e critérios de evidência

**Data:** 2026-10-20 · **Status:** mapa de triagem, não catálogo de tokens homologados e não auditoria exaustiva.  
**Plano diretor:** [master plan](DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · **gate atual:** [CSS readiness](CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md).  
**Baselines:** produto `main@1878ae1`; `visual-inventory.json` atualizado 20/10; auditoria runtime pública/ADRs P0–P4; runtime privado do registro anterior até 19/10. A última validação não cobre automaticamente estados posteriores de backend ou dispositivo físico.

## 1. Critério de propriedade para qualquer regra CSS

Uma “regra compartilhável” tem **cinco condições cumulativas**:
1. Mesmo contrato semântico **e** de estado nos dois consumidores;
2. Mesmo papel visual aprovado, incluindo claro/escuro, superfície, foco/hover/disabled, responsividade;
3. Mesmas condições de implementação real (tag/DOM, pseudo-elementos, layout parent, ordem de CSS, custom properties, breakpoints, engine suportado);
4. Mesmo resultado renderizado/comportamental **após** mudança e ganho concreto de manutenção ou custo;
5. Retirada da duplicata antiga sem fallback silencioso, especificidade compensatória ou regras concorrentes.

Caso uma falhe, a regra pode ser **variante com escopo**, **homônimo não compartilhável**, **exceção editorial** ou **indeterminada**. “80 nomes repetidos” no levantamento estático não equivale a 80 redundâncias reparáveis.

## 2. Ownership provável por folha/família (a confirmar por seletor)

| Fonte | Quem consome, papel | Dependências / fronteira de risco | Primeiro tratamento |
|---|---|---|---|
| `public-theme.css` | páginas públicas e acesso; reset/reduced motion/foco | influencia comportamento global, não só cores; `min-width:320px` | congelar; reproduzir NAV-005 abaixo de 320 sem corrigir globalmente |
| `ui-theme.css` | múltiplas rotas públicas/privadas, tema e slots | **120 referências textuais** a `data-theme`; seletor contextual pode superar folha de página; menu privado diferente do público | mapear overrides por rota/contexto; não quebrar em blocos cegamente |
| `landing/landing.css` | Landing e cabeçalhos editoriais de About/How | header NAV-005, tema e splash/carrossel | baseline do controlador, correção específica do header antes de refatorar |
| `about/about.css` | narrativa About | `.eyebrow`, imagem/texto editorial, contraste/contexto | preservar, validar se realmente comum |
| `how-it-works/how-it-works.css` | storytelling, painel de economia, comparações, ilustrações | `.module-card` não é `.module-card` do Config; `subgrid` e cores de legenda | tratar contratos editoriais isolados; testar painel após P4 |
| `viewer/viewer.css` | Viewer público (blocos, cena, hotspots, vistas) | `.scene-hotspot` se parece com Config, mas seleção/foco/camada podem ser diferentes | comparar geometria + teclado/scene em fixture pública |
| `styles.css` | Configurador: fluxo, cena e controles gerados por JS | DOM dinâmico, schema/autoria separados, CSS base `.button` conflitante | auditoria runtime com configuração real/fixture; não mover global |
| `admin/admin.css` | UI Admin, auth/edit/save, dados V5 | estados privados, alertas, contraste FIND-013 e riscos DS04 | correção estreita + verificação autenticada com segurança |

**Nota:** `app/access/access.css` não existe na main `1878ae1`; login de acesso usa `public-theme.css` e `ui-theme.css` conforme mapa DS. Não inventar uma folha por conveniência.

## 3. Fila de candidatos: triagem, não decisão de extração

| Candidato | Hipótese | Classificação atual | Prova necessária |
|---|---|---|---|
| `.visually-hidden` | utilitário semântico compartilhável | **candidato de risco moderado**; implementações em Admin/Config, páginas dependem de base | comparação de regras e estados de acessibilidade, mudança de loading order, foco, contraste e screenshot |
| `.scene-hotspot` | comportamento de cena Config+Viewer | **candidato de alto valor mas alto risco** | composição/positioning, selection-frame, focus ring, sobreposição/z-index, shape SVG e touch |
| `.button` | CTA/action visual | **homônimo de variantes** público/admin/config | contratos de tipo/estado/tamanho e decisões de tema; não fundir bases |
| `.module-card` | bloco editorial vs seleção de módulo | **homonímia não compartilhável** | manter escopo, não promover a componente global |
| `.eyebrow` | rótulo tipográfico recorrente | **variante contextual** com evidência de computed colors diferentes entre About/How | mapear roles/superfícies, VIS-002, contraste, tamanho, hierarquia |
| `.brand` / `brand__logo` / `private-header__brand` | asset de marca compartilhado | **separar asset de slot/layout** | header público vs privado, label/aria, breakpoints NAV-005 e PRIVATE-HEADER-001 |
| `.site-header` / `.menu-open` | menu público e header estáticos | **contrato transversal confirmado de JS/DOM**, CSS já compartilhado em Landing/About/How | fechar NAV-005 antes de mover regras; header não precisa de PageComposition |
| `.ui-theme-toggle` | controle de tema partilhado | **base transversal com variantes de posição** | slot por rota, estado persistido, OS preference, foco e breakpoint antes de refatorar |
| `.detail-*` / `.viewer-*` | conteúdo técnico público | **específico do Viewer** até prova de segundo consumidor | contrato de dados público, densidade, leitura responsiva, visibilidade |
| `.initial-state-option` | item do Admin | **débito de contraste comprovado** | regra contextual aprovada, validação de fundo composto real |
| `:focus-visible` | foco comum | **tokens parciais EST-02/VIS-002** | diferenciação de foco/seleção simultâneos por controle, tema, claro/escuro |

## 4. Registro de riscos com prioridade, detecção e contenção

| ID / prioridade | Risco ou lacuna concreta | Evidência/status | Mitigação / bloqueia |
|---|---|---|---|
| **R01 / alta** | Alterar CSS enquanto muda contrato/DOM, impossibilitando atribuição causal | UI-ADR-001 e sucesso P4 sem CSS | uma variável por patch; diffs DOM/computed/pixels antes-depois |
| **R02 / alta** | Globalização de seletores homônimos | inventário estático e baseline CSS; `.module-card` / `.button` | classificar por consumidor, escopo explícito; bloqueia G4/G5 |
| **R03 / alta** | Quebra do CSS do header compacto NAV-005 e conteúdo cortado | FIND-012, issue [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218) aberta; 486 e 291/290 px reproduzidos | fix local alinhado a NAV-005, inspecionar temas/larguras/long labels; bloqueia promoção de header CSS |
| **R04 / alta** | Contraste insuficiente em Admin e estados de controles | FIND-013 4,22:1 claro em label 10px; [#208](https://github.com/EAKerber/MobiliPresenter2D/issues/208) aberta | ler fundo composto e controlar sessão; corrigir somente papel aprovado |
| **R05 / média** | Contrastes públicos corrigidos sem confirmação pós-release | FIND-002/3/4, [#216](https://github.com/EAKerber/MobiliPresenter2D/issues/216), [#217](https://github.com/EAKerber/MobiliPresenter2D/issues/217) abertas | computed + composição de fundo + captura da arte; fechar com SHA/evidência |
| **R06 / alta** | Em iPad/Chrome Safari alguns fluxos Admin/inputs/assets não funcionam | relato do usuário; não reproduzido pela CI WebKit dos headers públicos | reproduzir em dispositivo; separar auth, sessão, CSP, cache, preload, engine, eventos; bloqueia afirmação de compatibilidade global |
| **R07 / média** | Mudar sequência de CSS/`@layer` modifica cascade sem modificar valores | nenhum `@layer` no CSS atual; overrides transversais `ui-theme.css` | plano de import order por rota e diff CSSOM; bloqueia reorganização ampla |
| **R08 / média** | Aprisionar foco ou perder navegação por teclado | NAV-004/EST-02; P4 headless PASS amostral | Tab/Shift-Tab/Escape/return focus, leitor de tela real se risco demandar |
| **R09 / média** | Presumir que motion reduzido é bug de animação ou usar screenshots sem motion como prova | media queries e `prefers-reduced-motion`; P4 usa reduce | testar normal + reduced separados; onda/splash e interação |
| **R10 / alta** | Reusar `.scene-hotspot` sem considerar z-index/overlay/foco e scene projection | `viewer.css`, `styles.css`, `scene-component.js` | fixture de cena, seleção, overlay, touch e foco; bloquear dedupe até prova |
| **R11 / média** | Falhas de sessão/estado desconhecido mascaradas como CSS | FIND-007 e relato Admin iPad; EST-07–10 direção | separar erro de rede/auth/persistência/render; nunca inferir sucesso por visual |
| **R12 / média** | Testes só em DOM estático perdem componentes JS | `visual-inventory.json` e P0 real | browser instrumentation após bootstrap, estados async, fixture e screenshots |
| **R13 / média** | JS shared script mais um request/cache stale | P4-NAV muda script tags e versões | testar versão/ordem/missing-script/cache; medir rede/parse real |
| **R14 / média** | Desperdício Netlify por deploy de cada PR | fluxo histórico de previews; limite operacional já discutido | CI local/Actions primeiro; PRs deliberadas e poucos deploys, higiene de deploys |
| **R15 / alta** | Promoção de `PageComposition` universal cria overengineering e confusão de schema | P3 custo estático +10.352 caracteres nos quatro JS | manter local, exigir consumidor entre páginas semanticamente real e benefício medido |
| **R16 / média** | Documentos de vários snapshots divergem e confundem gates | mapas 19/10 vs `main` 20/10; P0-R historical pending | índice canônico, SHAs, superseded/partial, revisão incremental sem apagar histórico |
| **R17 / média** | CI já vermelha na main por questão não relacionada | histórico de workflows de Mobile/Stone/Summary na main | comparar mesmo teste/commit/fixture, classificar preexistência |
| **R18 / alta — bloqueio atual** | Tentar merge de branch DS defasada sobrescreve inventário | PR #39 divergiu 1 commit da DS main e GitHub reportou `mergeable_state=dirty` (conflito) em 20/10; main mudou README, inventário e mapas | reconciliar README e merge-base com revisão explícita, integrar main na branch somente após inspeção; nunca force-push/merge automático |
| **R19 / alta** | Dados públicos ausentes recebem fallback privado | public projection, segurança allowlist | fail closed e teste endpoint sem dados; não permitir catálogo de fallback |
| **R20 / média** | Exportar CSS/layout sem teste de zoom/altura causa overflow invisível | FIND-012 + breakpoints estáticos | 320/390/486/768/1366 + alturas curtas, zoom, orientação e labels longos |

### Pontos cegos relevantes a investigar, sem pressupor defeito

- **Cascade no browser**: regra ativa vs override vs valor herdado por token, shadow/pseudo `::before/::after`, fontes reais, tamanho de fontes localizadas.
- **Assets e formatos**: carregamento tardio e diferenças de CORS/cache/Safari para imagens/ícones; uma resposta HTTP 200 não garante decodificação naturalWidth > 0.
- **Contraste perceptivo**: cores transparentes exigem composição de fundo, inclusive hero images e overlays; WCAG depende de uso/tamanho e foco.
- **Acessibilidade de cena**: `.scene-hotspot:focus-visible {outline:0}` usa pseudo-elemento customizado, verificar a experiência em todos os temas/camadas, não julgá-la sem interação.
- **Hover em touch**: interações por hover podem ficar presas ou tornar indicador de seleção ambíguo, especialmente em iPad.
- **CSS desativado / JS bloqueado**: testar degradação de navegação HTML e informação crítica, sem exigir igualdade estética.
- **Dimensões extremas e tela dividida**: 290–320 CSS px, leitor com fontes aumentadas, título/logo maior, landscape curto, safe areas e zoom 400%.
- **Multi-engine**: WebKit na CI não é idêntico ao Safari iOS físico; Chrome iPad também usa engine WebKit, mas integrações (keychain, cookies, downloads) e configuração podem diferir.
- **Admin**: acesso real/roles, interação com teclado e foco no editor, erro de salvar e estado desconhecido permanecem sem validação generalizada do DS.
- **Perf/Bundle**: medir arquivos CSS por rota, transfer size/gzip, duplicate declarations em CSS realmente co-carregado, request waterfall/cache; tamanho do texto-fonte não determina performance.
- **Autoria e tokens**: um valor literal CSS pode estar correto em um contexto mas ainda não homologado como token; estados EST-01–10 carecem de valores específicos.

## 5. Formato padrão de evidência e aceite

Para cada família proposta usar um registro:

| Campo obrigatório | Exemplo de conteúdo |
|---|---|
| `changeId` e escopo | `CSS-G5-HOTSPOT-01`; somente Viewer/Config |
| base/candidate | SHA produto + branch + SHA DS de decisões |
| decisão | NAV-004/005, VIS-002, EST-02 etc. com alcance e status |
| DOM/seletores | seção, classes, aria, pseudos, dados de entrada e origem |
| cascata | CSS carregados, ordem, especificidade, media, custom props |
| matriz | viewport/altura/zoom/tema/motion/browser/fixture/estado |
| automática | testes exatos + commit/run URL + logs e cobertura |
| visual | captura antes/depois e revisão humana, divergência intencional |
| funcional | cliques/touch/teclado/foco/rede/sessão conforme caso |
| contraste | cor de primeiro plano, fundo composto, tamanho de fonte, limiar aplicável |
| resultado | PASS/FAIL/PENDING/BLOCKED/OUT-OF-SCOPE + prioridade |
| rollback | arquivos exatos, procedimento revertível e validação |
| follow-up | responsável/issue/decisão pendente, sem prometer release |

**Gate de um componente:** PASS só quando não houver regressão estrutural/visual/funcional **na matriz apropriada ao seu contrato**; se faltar navegador, auth ou decisão estética crítica, resultado é HOLD e não aprovação parcial implícita.

## 6. Decisões de não fazer e estratégia de parada

Não:
- criar uma folha “base.css” de todos os seletores semelhantes por coincidência lexical;
- mudar o HTML da página How apenas para casar com Landing;
- mover `.module-card` para global por nome;
- deduplicar `.scene-hotspot` antes de avaliar cena real e overlays;
- transformar configuração/Admin V5 em manifesto universal;
- mover cor de legenda aprovada apenas para `.study-art` a token geral;
- introduzir @layer/CSS Modules/novo build para resolver conflito que sequer foi reproduzido;
- aplicar `!important` ou mais especificidade para ocultar regressão de cascade;
- mesclar PR do produto apenas com Playwright verde em dois viewports.

**Preferir parar** e manter duplicação explícita quando contrato diverge, custo de teste ultrapassa benefício, a correção viola decisão homologada, a migração depende de permissões ou publicação indisponíveis, ou a ausência de evidência seria mascarada como “nenhum problema encontrado”.

## 7. Próximo uso prático

1. Ler [etapa atual](CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md), completar testes G1-R1/R2 em branch pública isolada (sem CSS).
2. Fazer G2-1 e G2-2 como mudanças corretivas separadas apenas com decisão e aprovação de escopo.
3. Preparar a primeira matriz de propriedade G3 para uma família de baixíssimo risco; só então decidir se há ganho para extrair CSS.
4. Persistir evidência e atualizar o status desta tabela a cada gate, não só adicionar comentários soltos em PRs.

**Veredito:** CSS atual é baseline legítimo para avançar no **controle e medição**; a extração arquitetural abrangente ainda não passou pelos gates de conformidade/compatibilidade e deve continuar bloqueada.


## G3 — auditoria inicial por família no pin atual (2026-11-11)

**Fonte:** `EAKerber/MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. Leitura estática de HTML/CSS/JS e ordem declarada de folhas; classificações abaixo são triagem de ownership, não aprovação de extração nem prova de estilo computado/runtime.

| Família/candidato | Consumidores e folhas co-carregadas | Classificação G3 | Evidência e limite |
|---|---|---|---|
| `.visually-hidden` | Admin: `admin.html` carrega `admin/admin.css` e depois `ui-theme.css`; o `strong` escondido rotula a marca e o nome “Administração”. Configurador: `config/index.html` carrega `styles.css` e depois `ui-theme.css`; o `h1` escondido fornece o título da página. | **Mesmo utilitário textual em dois bundles de rota; candidato de contrato compartilhado, ganho não demonstrado.** Os dois seletores têm a mesma declaração de 10 propriedades, todas `!important`, mas nunca são co-carregados entre si. Os elementos também têm semântica distinta (`strong` e `h1`). | Cabeçalhos/fontes: `app/admin.html:14,19`, `app/config/index.html:30,41,49`; regras: `app/admin/admin.css:157` e `app/styles.css:853`. A ordem coloca `ui-theme.css` depois da folha de cada rota. Falta medir bytes/cache em todos os consumidores e confirmar CSSOM, árvore acessível e impressão antes de decidir extração. |
| `.eyebrow` | Landing/How/About compartilham a base em `landing.css`; How e About carregam seus próprios overrides; Viewer e Admin têm folhas e consumidores próprios; `ui-theme.css` acrescenta ajuste para a linha de contexto. | **Variantes contextuais e homônimo privado; não globalizar.** Cor, margem, escala e papel editorial/privado diferem por rota e superfície. | O trace VIS-002C cobre seletores claros/escuros e exceções apenas nos consumidores medidos ([trace](../evidence/architecture/vis002c-cascade-winner-trace-2026-11-10.md)). Não amplia ownership automaticamente ao Viewer/Admin nem a todos os elementos da classe. |
| `.button` | Regras públicas em `landing.css`; contratos separados em `admin/admin.css` e `styles.css` (Configurador); `ui-theme.css` possui overrides temáticos adicionais. | **Homônimo de variantes; sem extração comum.** O tipo/tamanho público é editorial/CTA; Admin e Config usam estados, dimensões, superfícies e ações de domínio distintos. | Em `main@221b54b`, a base pública usa altura mínima 46 px e raio 3 px; Admin 40 px e raio 9 px; Config tem regras e estados próprios. O seletor `.button` coexiste com modificadores/overrides dentro de cada domínio. Não converter igualdade de nome em igualdade de contrato. |
| `.scene-hotspot` | Config: `styles.css` + `core/scene-component.js`; Viewer: `viewer/viewer.css` + `viewer/scene-adapters.js`. As folhas Config e Viewer não são co-carregadas uma com a outra. | **Indeterminado/variantes de domínio; candidato de alto risco.** A proximidade de geometria/nomes não prova igualdade de seleção, foco, sobreposição, etiqueta ou interação. | Regras e geradores pertencem a arquivos separados e contratos de cena diferentes; requer matriz de estado/teclado/touch, bounding boxes, z-index, foco e seleção por consumidor. Sem extração. |
| `.site-header` | Shell público repetido em Landing/How/About; `landing.css` é base co-carregada; How adiciona regra geométrica própria; `ui-theme.css` aplica regras de tema/foco. O controlador é `landing/header-menu.js`. | **Contrato de shell compartilhado com variante de página; G1 ainda aberto.** A implementação em #269 é proposta seletiva para cabeçalho público; não equivale a menu privado nem encerra #218. | Markup/ordem de folha confirmados em `how-it-works/index.html:16–19,22` e `about/index.html:9,13`. Preview #269 foi observado em desktop e 390 px, mas sem teste Safari/iPad, toque, zoom ou dispositivo real; ver [#269](https://github.com/EAKerber/MobiliPresenter2D/pull/269) e [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218). |

### Decisão desta passagem

Não há base suficiente para G4. O `.visually-hidden` é o único candidato desta passagem com declaração igual e consumidores identificados, mas as regras pertencem a folhas distintas e não são baixadas juntas numa mesma rota; mover a regra para `ui-theme.css` pode aumentar o payload nas demais rotas. Medir custo efetivo por rota/cache antes de propor. `.button` e `.eyebrow` permanecem variantes contextuais; `.scene-hotspot` permanece indeterminado; `.site-header` segue G1 até #218 e critérios de plataforma estarem fechados.

**Próxima etapa G3:** aprofundar marca/ícone/slots e estados restantes por rota, incluindo focus-visible, hover, disabled, selected, loading/error. Para estados de runtime protegido, usar somente ambiente/configuração válida. Até lá, nenhum componente ou regra CSS é promovido a shared.


## G3 — menu público e menu privado: ownership e estados (2026-11-11)

**Fonte:** produto `EAKerber/MobiliPresenter2D/main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. Leitura estática de HTML, folhas declaradas, CSS e controladores; não é validação runtime de toda a matriz.

| Contrato | Consumidores e ordem de CSS | Ownership de DOM/JS e estados | Classificação G3 |
|---|---|---|---|
| Menu público | Landing `app/index.html`: `public-theme.css → landing/landing.css → ui-theme.css`. How: acrescenta `how-it-works.css` antes de `ui-theme.css`; About usa `about.css` antes da folha de tema. Os três usam `header.site-header`, `nav#primaryNav` estático, `button#menuToggle` e `landing/header-menu.js`. | A página marca o link corrente com `aria-current="page"`. O controlador alterna `body.menu-open`, `aria-expanded` e o nome do botão; Escape fecha e devolve foco ao botão quando o foco estava no nav; clique em link e pointerdown fora fecham. Abrir por teclado move foco ao primeiro link; abrir por pointer não força esse foco. O CSS base de `.site-header nav` é horizontal; até 900px o nav some e o toggle aparece; `.menu-open` mostra o painel e anima o ícone. How possui uma regra geométrica própria para o header. | **Shell e controlador públicos compartilhados, com variante de página.** Separados do menu privado. G1/#218 e testes de touch, zoom, foco integral e dispositivo continuam abertos. |
| Menu privado | Admin `app/admin.html`: `admin/admin.css → ui-theme.css`. Access/manage `app/access/manage.html`: CSS inline da página → `ui-theme.css`. Ambos incluem o esqueleto `[data-private-header]`, toggle `[data-private-menu-toggle]` e nav `[data-private-menu]`, inicializado por `core/private-navigation.js` (entry agrupado como `private-navigation.bundle.js` no HTML). | O controlador gera os links em runtime e reconcilia Identity/sessão. Admin, staff, sessão temporária, visitante e usuário sem papel recebem conjuntos ou avisos diferentes; `aria-current` é calculado para o link interno. `hidden` e `aria-expanded` acompanham abertura. Abrir foca o primeiro link/botão; Escape fecha e restaura foco; pointerdown fora fecha sem restaurar foco. CSS de tema altera superfície, borda, texto, hover/current; há breakpoints a 650px e 380px. O menu inclui nota de carregamento/indisponibilidade e conteúdo de conta/logout conforme estado. | **Contrato privado compartilhado entre Admin e Access; variantes de conteúdo dependem de sessão e papel.** Não é continuação do menu público nem um componente genérico de navegação. |
| Relação público ↔ privado | Ambas as famílias usam `ui-theme.css`, mas públicos também dependem de `landing.css`, enquanto os privados usam estrutura, classes e controlador próprios. As famílias não co-carregam os respectivos menus numa mesma rota. | O menu público parte de links HTML estáticos e estado de layout; o privado constrói links com dados de sessão e permissões. Há atributos, handlers, estados e geometrias diferentes. | **Contratos distintos; sem extração/mescla entre famílias.** O compartilhamento atual limita-se a papéis de tema/estilos globais já existentes. |

**Evidência-fonte:** `app/index.html:15–18, 24, 59`; `app/how-it-works/index.html:15–19, 22`; `app/about/index.html:9, 13`; `app/landing/landing.css:23–39, 138–144`; `app/landing/header-menu.js:3–26`; `app/how-it-works/how-it-works.css:181`; `app/admin.html:14–26, 113`; `app/access/manage.html:41–52, 82`; `app/core/private-navigation.js:3–23, 37–43, 72–103, 106–133, 169–190`; `app/ui-theme.css:267–350`. A rota Config não foi incluída na matriz de runtime porque a configuração publicada do Preview não valida.

**Limite e decisão:** as linhas acima comprovam ownership declarado e comportamento definido no código pinado; não demonstram estilos computados em todos os temas/breakpoints, ordem final efetiva após build, foco visível após cada interação, falhas reais de autenticação/rede ou equivalência visual por captura. Portanto G3 permanece **parcial**, G1 segue aberto e nenhum CSS foi alterado. A semelhança de botão “hambúrguer” não justifica partilhar controlador ou seletores.
