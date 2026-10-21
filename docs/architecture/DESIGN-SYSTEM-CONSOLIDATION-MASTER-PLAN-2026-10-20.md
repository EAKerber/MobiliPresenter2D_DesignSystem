# Plano diretor — consolidação de Design System, CSS e componentes do MobiliPresenter2D

**Revisão:** 2026-10-20 / 0.1 — plano operacional e técnico, não homologação visual nem autorização para publicar.  
**Ponto de entrada recomendado:** este arquivo → [etapa atual](CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md) → [matriz de riscos e ownership](CSS-OWNERSHIP-RISKS-2026-10-20.md).  
**Produto tomado como fonte:** [EAKerber/MobiliPresenter2D @ 1878ae1](https://github.com/EAKerber/MobiliPresenter2D/tree/1878ae1057ce7c6190e0c8cb08a1f3baadd49463), `main` observada em 2026-10-20.  
**Design System:** [EAKerber/MobiliPresenter2D_DesignSystem PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39), branch `architecture/dom-css-consolidation-20261020` (draft).  
**Autoridades:** `decisions.json` (decisões homologadas/direções); `FINDINGS_REGISTER.md` (achados datados); `DECISION_APPLICATION_MAP.md` (mapa datado); ADRs UI-001…005 (decisões técnicas experimentais); snapshots/CI (evidência, não homologação).

> **Decisão de prontidão:** o CSS **é suficientemente estável como baseline imutável para o próximo incremento comportamental/documental e refatoração isolada com testes**, mas **não está homologado nem suficientemente validado para dedupe/globalização/migração em lote**. O requisito é preservar e medir, não “arrumar o CSS” ao mesmo tempo que se muda o JavaScript.

## 1. Resultado esperado e critérios de êxito

Um sistema de interfaces com identidade coerente e editabilidade proporcional ao domínio, sem apagar as diferenças deliberadas entre Landing, Viewer, Configurador, Admin e Acesso. “Consolidado” significa:
1. **Cada contrato possui dono explícito** — dados/autoridade, DOM semântico, estados, ações, classes CSS, tokens e variantes; não há duas autoridades concorrentes por comportamento.
2. **As regras visuais homologadas são rastreáveis** do ID de decisão até seletor efetivamente aplicado, contexto, estado, tema, breakpoint e evidência visual.
3. **CSS repetido é removido apenas quando seu contrato é de fato o mesmo**; homonímias e variações intencionais permanecem distintas.
4. **Todos os fluxos críticos ficam utilizáveis** sem regressão de teclado, touch, viewport estreito, zoom, contraste, movimento reduzido, modo claro/escuro, erro assíncrono, estado administrativo e publicação.
5. **Mudanças são pequenas, reversíveis e mensuráveis**: diferenças semânticas e visuais explícitas, testes determinísticos, revisão humana onde automatização não basta, rollback demonstrável.
6. **Sem novo acoplamento ao schema administrativo:** `ConfiguratorAdministration2D 5.0`, contratos de preço/catálogo, `Scene2D`, `PublicModulePresentation2D`/allowlist, auth e sessão mantêm autoridades próprias.

**Métricas de sucesso admissíveis:** redução de donos duplicados do *mesmo comportamento*, redução de regras realmente equivalentes após prova, melhoria em taxa de gates cobertos, diminuição de inconsistências mapeadas, regressões evitadas, limites de payload/rendimento **medidos**. **Não** anunciar “-X% de CSS” sem examinar bytes carregados por rota, cache, cascade, responsividade e regressões.

## 2. Mapa de propriedade e separação de responsabilidades

| Camada | Autoridade e regra | Proibições na presente fase |
|---|---|---|
| Design decisions | `decisions.json`, com escopo, status, aprovação e exemplo; decisões estéticas não surgem de um CSS encontrado | promover paleta incidental a token; preencher lacuna de decisão sem usuário |
| Estilo base/tema | `public-theme.css`, `ui-theme.css`, tokens aprovados por contexto | globais sem escopo; reordenação não medida; tema herdado como permissão |
| Shell público | HTML semântico de cada página, menu compartilhado por controlador | recriar cabeçalhos com JS/JSON; apagar `aria-current` ou contextualização |
| Landing | `landing/data.js` e componentes locais, estado de carrossel/arte/benefícios | CMS, API admin, motor universal só para remover `createElement` |
| Viewer | projeção pública allowlisted, blocos e cena/technical views especializadas | fallback para catálogo privado; schema administrativo na página pública |
| Configurador | projeção da configuração e fluxo semântico do comprador | “ganhar reuso” substituindo lógica de seções/pricing por CSS ou manifest genérico |
| Administração | V5, autorização/salvamento, formulários e indicadores de estados | alteração de backend/persistência misturada com CSS; ícones/status genéricos sem estados |
| Acesso/menus privados | sessão, roles, navegação privada e auth | misturar menu público e privado, vazar estado, inferir sessão por DOM |
| Component contract | tipo/variantes/validação em código quando **realmente útil** | HTML, JS, CSS ou handlers arbitrários em dados de cliente |
| Runtime state | controladores e atributos ARIA/DOM | persistir hover/focus/loading como schema de produto |

O “reuso” tem **classes diferentes**: domínio/projeção; comportamento JS transversal; marca/tokens; contrato CSS/DOM; composição editorial. Uma semelhança lexical entre seletores não une essas classes de responsabilidade.

## 3. Onde estamos: evidência consolidada e limites

| Frente / gate | Estado em 2026-10-20 | Evidência / ressalva |
|---|---|---|
| P0 static CSS × HTML × JS | **Inventário realizado, parcial por natureza** | `visual-inventory.json` representa produto `1878ae1`; crosswalk contém 8 CSS/8 rotas; JS cria DOM dinâmico fora do HTML inicial |
| P0-R público (DOM/CSS real) | **PASS amostral** | Chromium 4 rotas × 2 larguras × 2 temas = 16/16, estilos computados; [baseline](dom-css-runtime-public-baseline-2026-10-20.md). Não inclui Admin autenticado/zoom/iPad |
| P1 contrato de composição | **PASS experimental** | 13/13 testes Node no repo DS; [increment plan](declarative-ui-increment-plan-2026-10-20.md) contém histórico inicialmente anterior aos gates P2–P4 |
| P2 benefícios da Landing | **PASS isolado** | Branch `experiment/ui-declarative-landing-benefits-20261020`: DOM/CSS/pixels equivalentes em recorte |
| P3 duas variantes de benefícios | **PASS isolado, não promovido a framework** | 10/10 Node; duas regiões iguais à main 4/4 Chromium; WebKit interação [Actions #39506584577](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39506584577). +~10.352 unidades de texto JS nos 4 arquivos comparados |
| P4-NAV controller público | **PASS isolado** | Branch `experiment/shared-public-header-controller-20261020`, [Actions #39508130387](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39508130387), 12/12 visual e 12/12 funcional, foco NAV-004. Não houve merge |
| CSS extraído em foundation/components | **NÃO INICIADO** | Proposta de layout lógico é candidata, não árvore de arquivos aprovada. Nenhuma migração CSS em massa |
| Conformidade global visual/acessibilidade | **ABERTA** | NAV-005/FIND-012, contraste Admin/FIND-013, correções FIND-002–004 ainda exigem rechecagem; issues abertas |
| Gate em dispositivo real/iPad | **PENDENTE** | WebKit headless não equivale a Safari/iPad real; relato de problemas em auth/botões/assets precisa isolar rede, sessão, CSP e compatibilidade |
| Produto publicado/main | **INTACTO nesta trilha** | Baseline `main@1878ae1`. Branches não significam release |

**Importante:** documentos históricos de P0/P1 e mapas de 19/10 podem conservar frases como “P0-R pendente” ou SHAs antigos. **Não reinterpretar como falha presente:** consultar este resumo, ADRs datados e resultados de CI; manter textos históricos para proveniência e acrescentar adendos quando necessário.

## 4. Sequência completa por incrementos — prioridade e gates

### Fase G0 — Fundação documental e protocolo de evidência (AGORA)

**Entrada:** snapshots e decisões existentes.  
**Tarefas:** fixar autoridade de cada mapa; indicar versionamento do produto; correlacionar `decisions.json`, issues e seletores DOM; classificar evidência em (a) estática, (b) browser/computed CSS, (c) screenshot/inspeção humana, (d) funcional/dispositivo real, (e) produção autenticada quando admissível. Diferenciar estados PASS / FAIL / PENDING / BLOCKED / OUT-OF-SCOPE / SUPERSEDED.  
**Saídas:** este plano; estágio operacional; risco/ownership; links para traces, CI e SHAs; base comparável por rota/tema/resolução.  
**Gate:** nenhum resultado de 2026-10-19 substituído silenciosamente por inspeção estática atual; checkpoints recuperáveis.

### Fase G1 — Fechar o controlador de navegação pública P4-NAV (ATUAL)

**Feito:** controlador único `landing/header-menu.js`, extraído de Landing/How, mantendo About; apoio de foco (Enter abre/foca primeiro link; Escape devolve foco); cache versionado. Diferenças visuais nulas nos recortes automatizados 12/12.  
**Falta:** testar painel explicativo Como funciona após a extração, interação do splash/animação normal da Landing (gates anteriores usaram principalmente reduced motion), mudança de viewport com menu aberto, teclado/Tab/Shift-Tab/scroll, foco após clique fora, regressão de ícones/caminhos e HTML sem JS; revisão NAV-005 do comportamento geral; dispositivos reais representativos (especialmente iPad quando disponível). Medir carregamento de script/cache no browser suportado.  
**Saídas:** relatório funcional de G1 com PASS/PENDING e captura visual antes/depois; parecer GO/NO-GO para eventual PR *draft* do produto.  
**Gate GO:** nenhum crítico quebrado, diferenças intencionais de interação documentadas; rollback em uma branch sem conflito com P3; sem alterar CSS para compensar JS. **Nenhum merge/publicação por consequência automática.**

### Fase G2 — Conformidade corretiva priorizada do CSS existente (ANTES DE EXTRAÇÃO)

**Objetivo:** corrigir ou classificar problemas **já reproduzidos** sem mascará-los com refatoração:
- NAV-005/FIND-012 [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218): header estreito, visibilidade de rótulo de tema e contato, colapso abaixo de 320px, regras de marca (redução ≤30% antes de reflow aprovado).
- FIND-013 [#208](https://github.com/EAKerber/MobiliPresenter2D/issues/208): contraste de `.initial-state-option` do Admin (4,22:1 claro) e cobertura estática remanescente DS04; confirmar papel visual e corrigir no contexto, não globalmente.
- FIND-002/003 [#216](https://github.com/EAKerber/MobiliPresenter2D/issues/216) e FIND-004 [#217](https://github.com/EAKerber/MobiliPresenter2D/issues/217): revalidar em runtime as correções publicadas e contexto de fundo efetivo antes de fechar issues.
- Estados VIS-002/003 e EST-01–10: converter direções homologadas em matriz de contexto/estado, **não inventar** cores/medidas ainda sem decisão.
**Gate:** tickets atualizados com prova por seletor/estado/tema, sem alteração de paleta em outros contextos; provas de contraste com composição real e inspeção visual. G2 pode ocorrer em paralelo à G1, mas não no mesmo patch.

### Fase G3 — Auditoria de ownership CSS e contratos antes da extração

**Para cada seletor candidato:** registrar consumidor real, arquivos CSS efetivamente carregados na rota, ordem de links e especificidade, variante e estado, fonte de token, DOM gerado por JS, diferenças em @media/@supports, tema, CSS custom properties herdadas, pseudo-elementos, interação e conteúdo. Separar duplicação entre arquivos **co-carregados** de duplicação em rotas isoladas.  
**Focos:** `.visually-hidden`, `.scene-hotspot` (config/viewer), menu público, papel da marca, `.eyebrow`, `.button`, tipografia e estados.  
**Gate:** matriz de ownership por família com classificação **igual / variante intencional / homônimo / indeterminado / exceção**. Nenhuma alteração CSS antes dessa classificação.

### Fase G4 — Foundation/tokens/acessibilidade compartilháveis

**Hipótese** (não pasta decidida): mínimo de foundations para reset, tokens de papéis **aprovados**, foco e utilitários semânticos. Extrair um candidato por vez, medir bytes **efetivamente transferidos e carregados**, CSSOM, estilos computados e ordem/specificity; preservar fallback de navegadores. Evitar @layer, :where, :is e CSS Modules como reordenação incidental; estes recursos exigiriam gate próprio.  
**Candidato inicial:** utilitário `.visually-hidden`, **somente se** equivalência de regras, consumidores, import order e árvore já estiverem demonstradas. Alternativamente zero extração nesta fase se não houver benefício claro.  
**Gate:** equivalência funcional/visual *por consumidor*, com estado de foco/oculto e impressão, sem novas colisões.

### Fase G5 — Componentes CSS por família, não por nome

Sequência sugerida *condicional*, do menor risco ao maior:
1. Controle de menu público: ownership de regras comuns, **sem** tocar na geometria NAV-005 enquanto FIND-012 estiver aberto.
2. Logo/ícone/papel e slots públicos/privados diferenciados; não mesclar CSS só porque nome de asset se repete.
3. Botões e labels comuns **apenas após contratos de variante e estados aprovados** (público/admin/config têm dimensões e papéis distintos).
4. Tipografia `.eyebrow` e utilitários contextuais, tomando cuidado com contraste por página.
5. Cena/hotspots entre Viewer/Configurador **somente após** testes de posicionamento, seleção, focus-visible e interação real.
6. Status/erro/disabled/read-only/loading/retry e superfícies privadas, após cruzar EST-01–10 e confiabilidade de persistência.
**Gate por família:** baseline antes/depois com atributos, computed styles, screenshot, interação, tema/estados/breakpoints, custo de CSS por rota, rollback. Não remodelar dados de domínio junto.

### Fase G6 — Consolidação de páginas e arquitetura de composição

Landing/How/About preservam HTML estático e acessibilidade; Viewer mantém allowlist pública e compositor próprio; Config/Admin V5 mantêm schemas/projeções. `PageCompositionExperimental` fica **restrito ao experimento** enquanto faltar segundo consumidor *entre páginas* de mesmo contrato editorial.  
Avaliar build-time partial de header somente se sincronização manual demonstrar custo real; não introduzir framework, hidratação, SSR, CMS ou editor visual por conveniência do CSS.  
**Gate:** ganho material de manutenção comprovado + schema ownership definido; custo operacional abaixo do benefício. Rejeitar propostas cujo único argumento seja “há muitos createElement”.

### Fase G7 — Integração e hardening cross-platform

Executar matriz representativa baseada em risco (direção CMP-001T: largura, altura, zoom, browser/dispositivo, tema, fluxos/estados e incompatibilidades já vistas; expandir por evidência). Separar **automatizado / screenshot inspecionado / teste funcional real**.  
Testar ao menos fluxos públicos, Viewer, Config e Admin *autenticados* em ambiente controlado, menus privados, sessão, falhas de rede, assets, foco, touch, navegação e impressão se aplicável. Para dados sensíveis, fixture isolada, nunca usar endpoint privado real como teste de permissão inferido de DOM.  
**Gate:** zero bloqueador nas jornadas críticas; riscos residuais assinados com alcance; versão da aplicação e de screenshots/CI rastreáveis.

### Fase G8 — Aceitação, publicação e pós-release

Só propor release após revisão no Design System/PR de produto independente, checks verdes **relevantes ao patch** e baseline dos checks historicamente vermelhos para comparação. Uma PR = uma alteração autorizável e reversível; não abrir PRs sucessivas para gerar previews. Fazer **um** preview deliberado quando o gate realmente precisar da integração Netlify; não usar publicação como método de descobrir erro sintático. Conferir preview, produção, cache/versioning, auth/estado, links/assets e regressões pós-publicação. Encerrar issues com evidência do release, não apenas commit.  
**Gate de saída:** release + readback de versão + evidência publicada + rollback conhecido + documentação/handoff. 

## 5. Princípios de execução e tamanho de lote

- **Uma variável por incremento:** JS *ou* CSS *ou* tokens/tema *ou* layout responsivo *ou* schema. Mudanças acopladas exigem justificativa e teste conjunto explícitos.
- **Branch experimental e diff mínimos**, base imutável anotada, flags apenas quando necessárias, sem manter duas lógicas permanentes de compatibilidade.
- **Sem alteração fora de escopo**, especialmente auth, endpoints, catálogo, preços, fonte de conteúdo ou publicação de dados.
- **Orçamento de CI e Netlify:** testes local/Actions sem deploy; cancelar runs obsoletos; artefatos com retenção e sumário durável em docs; preview único e consciente, somente após gate de necessidade.
- **Evidência compartilhável:** comando, SHA, browser/motor e versão, viewport CSS, DPR, zoom, tema, reduced-motion, estado, horário, seletor/rota, fixture, baseline/candidato, resultado e limitações.
- **Falhas**: marcar preexistente, introduzida, flaky/indeterminada, ambiente/provider, ou dado indisponível; nunca “PASS” por causa de ferramenta que não executou.
- **Política de CSS:** evitar globalização, `!important` compensatório, reordenação de import ou novos estilos de fallback sem classificação de cascade.
- **Homologação:** ADR técnico não substitui escolha visual do usuário nem altera `decisions.json` sozinho.

## 6. Matriz de testes base e expansão por evidências

| Dimensão | Núcleo inicial recomendado (não homologado como cobertura exaustiva) | Expansão obrigatória quando relevante |
|---|---|---|
| Rotas | `/`, `/about/`, `/how-it-works/`, `/viewer/`, `/config/`, `/admin.html`, `/access/`/manage | qualquer nova rota e estado visível |
| Layout CSS | 390×844, 768×1024, 1366×768; 320×568 para mínimo declarado; largura de 486 (FIND-012) | 290–291 e 360 para quebra crítica; 1036×582 para Admin/FIND-013; condições com identificação longa |
| Browser | Chromium e WebKit automatizados; motor Safari físico quando possível | Chrome iPad (WebKit) e Safari iPad, Firefox/Android ou dispositivos exigidos pela incompatibilidade |
| Preferências | claro/escuro, motion normal/reduzido, zoom e fontes ampliadas | contraste forçado, orientação, teclado físico/software, idioma/título longo |
| Interações | click/touch, Tab/Shift-Tab/Enter/Escape, clique fora, foco retornado, seleção, scroll | estado offline/erro, rede lenta, refresh, sessão expirada, dados stale, retry/double-submit |
| Evidência | unidade/contrato, DOM/computed CSS, captura, teste funcional | leitor de tela, dispositivo real, auditabilidade da API e produção após lançamento |

**Cuidado:** larguras como 290 não substituem o mínimo de produto declarado (320) por uma nova homologação; expõem a falha/requisito de encaixe e demonstram limite da regra.

## 7. Checklist de decisão GO / HOLD / NO-GO

**GO somente quando**: ownership + autoridade corretos; patch reversível; gates funcionais e visuais adequados ao recorte; estados críticos exercitados; não há diferença não aprovada; nenhuma falha CSS/auth é atribuída indevidamente ao refactor; impacto de Netlify/caching entendido.

**HOLD**: faltam dados de browser real ou decisão visual, não há fixture segura de sessão, efeito de cascade não explicado, contraste pendente, import order desconhecida, diferença pixel sem investigação, PR base desatualizada.

**NO-GO**: quebra de seleção/teclado/assistive tech, auth involuntariamente pública, fallback revelando catálogo privado, regressão de contraste/foco, conflito com token homologado, mudança grande de CSS para adaptar código sem necessidade, ou custo/complexidade superior ao problema.

Revisar criteriosamente ao fim de cada gate; desistir da extração é resultado válido.

## 8. Handoff e recuperação sem depender do chat

Ler, nesta ordem:
1. Este plano diretor e [estado atual](CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md).
2. [Matriz CSS/riscos](CSS-OWNERSHIP-RISKS-2026-10-20.md), `decisions.json`, `FINDINGS_REGISTER.md` e `PALETTE_CONFORMANCE.md`.
3. [UI-ADR-001](ui-adr-001-declarative-boundaries-2026-10-20.md) a [UI-ADR-005](ui-adr-005-public-header-controller-2026-10-20.md); conferir qual técnica foi experimentada e qual **não** foi promovida.
4. Revalidar `main`/PRs atuais antes de editar. Produto `main@1878ae1` e DS main `0b3e223` são apenas o estado observado em 20/10. A branch DS está **1 commit atrás** de DS main e à frente com docs experimentais. Após mudanças simultâneas no README, o GitHub reportou PR #39 com `mergeable_state=dirty` (conflito) em 20/10; o commit principal alterou `README.md`, mapas e inventário. A branch passou a preservar a redação atual do README de `main`, mas **não foi criada integração da main na branch nem houve merge**. Recalcular conflito e reconciliar com revisão, sem force-push ou sobrescrita de inventário.
5. Escolher um **único incremento/gate**, registrar plan→evidence→result→decision→rollback; anexar prints/relatórios relevantes e persistir sumário no repositório para sobreviver à retenção temporária de artifacts.
6. Não juntar automaticamente as branches do piloto de benefícios e da navegação; manter histórias e decisões separadas.

**Última regra:** sem prova de CSS incompleto não se cria correção genérica; com prova de defeito existente não se declara CSS “pronto globalmente”. Os dois fatos coexistem.
