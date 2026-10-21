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
| **R18 / média** | Tentar merge de branch DS defasada sobrescreve inventário | PR #39 divergiu 1 commit da DS main na verificação 20/10 | inspecionar diferenças e rebase controlado antes de merge, nunca forçar |
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
