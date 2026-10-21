# Gate atual — prontidão das folhas CSS e fechamento P4-NAV / preparação G2

**Revisão:** 2026-10-20. **Estado:** documentação e decisão de próximo incremento. **Não é aprovação de CSS para refatoração em lote ou publicação do piloto.**  
**Plano pai:** [Plano diretor](DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · **matriz:** [ownership e risco](CSS-OWNERSHIP-RISKS-2026-10-20.md).  
**Produto fonte:** `main@1878ae1057ce7c6190e0c8cb08a1f3baadd49463`, inspecionada em 20/10. **Design System:** `architecture/dom-css-consolidation-20261020` / PR #39 draft.

## 1. Resposta de prontidão (“pronto para quê?”)

| Uso de CSS no próximo passo | Parecer | Condições |
|---|---|---|
| Congelar CSS como baseline e continuar testes/ownership | **GO** | Arquivos e ordem de carregamento imutáveis; snapshots SHA; gates de DOM/computed e testes reais por contexto |
| Avançar no JS compartilhado de menu público sem mexer no visual | **GO técnico em branch**, **HOLD para publicação** | P4-NAV 12/12 visual + 12/12 funcional aprovado em Chromium/WebKit; completar lacunas abaixo |
| Corrigir **um** defeito CSS reproduzido (ex. FIND-012) | **GO condicional** | Issue e decisão correspondente, branch separada, screenshots/contraste antes/depois e teste representativo |
| Extrair um **utilitário comprovadamente equivalente** | **HOLD curto** | Primeiro classificar consumidores/cascade e provar custo/benefício; piloto mínimo reversível |
| Reestruturar todo CSS em foundation/components, globalizar folhas | **NO-GO agora** | Faltam conformidade por superfícies, fechamento do mapa runtime e política de importação específica |
| Promover todos os valores observados a design tokens | **NO-GO agora** | VIS-002 é contextual; estados EST e outras variantes continuam parcialmente não homologados |
| Declarar “responsividade completa”, “acessibilidade completa” ou “iPad compatível” | **NO-GO** | Cenários validados não cobrem esses universos |

**Distinção necessária:** a folha estar estável/funcionando em um recorte não faz seu conteúdo virar contrato homologado. Estilos atuais podem coexistir com defeitos preexistentes e exceções conscientes.

## 2. Reconciliação da evidência com a implementação real

As oito folhas mapeadas em `visual-inventory.json` (produto `1878ae1`) são:

| Folha | Dimensão aproximada do texto fonte | Papel / status de migração |
|---|---:|---|
| `app/public-theme.css` | 1.141 caracteres | base pública e reduced-motion; estabilizar sem reordenar reset global |
| `app/ui-theme.css` | 19.605 | tema/contexto, 120 ocorrências de `data-theme`, muitos overrides; **alto risco de recortar cegamente** |
| `app/landing/landing.css` | 16.407 | Landing + shell editorial usado por About/How; baseline P4-NAV já provado, correções NAV-005 pendentes |
| `app/about/about.css` | 5.202 | composição editorial de About; não mover `.eyebrow` só por nome |
| `app/how-it-works/how-it-works.css` | 29.289 | layout editorial amplo, subgrid e regras com cores/contraste contextuais; exceções de conteúdo |
| `app/viewer/viewer.css` | 12.384 | cena/hotspots/técnicas/detalhes públicos; só extrair após prova de geometria contra Config |
| `app/styles.css` | 46.748 | Configurador, estados de fluxo, cena, interação; alto risco por DOM programático |
| `app/admin/admin.css` | 22.395 | admin/autoria/salvamento/login e detalhes do editor, com várias regras `[data-theme]`; risco de estados autenticados |

As dimensões são caracteres da string recuperada do GitHub, **não** bytes UTF-8, gzip nem custo de rede. `@layer` **não aparece nessas fontes**; introduzi-lo muda ordem de precedência e exigiria teste separado. Há `!important`, @media, `:has`, `color-mix` e `subgrid` em contextos específicos: antes de mover regras, verificar compatibilidade, fallback e custo real por navegador. “O seletor existe” não garante que define a propriedade final.

### Estado concreto de CSS

**Sinais favoráveis**
- A baseline pública mediu DOM/CSS computado real em 4 rotas × 2 larguras × 2 temas: **16/16 carregamentos** no Chromium sem erro/exception registrada, incluindo diferenças reais de cor por tema.
- O controlador de cabeçalho foi migrado em branch isolada **sem alterar CSS**, com [Actions #39508130387](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39508130387): **12/12 verificações visuais** (3 rotas × 2 larguras × 2 temas) e **12/12 funcionais** (Chromium + WebKit × 2 larguras × 3 rotas) PASS.
- Os dois grupos de vantagens da Landing, com variants `standard` / `compact`, preservaram capturas, DOM, estilo e geometria no piloto isolado [#39506584577](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39506584577).

**Bloqueios de conformidade conhecidos (não derivar novo desenho deles)**
- **FIND-012 / #218**: 486 px e 290–291 px, header compacto com divergências de NAV-005, perda/corte de controles abaixo de 320 e rótulo de tema escondido. Não dissolver esse comportamento em novo CSS global; tratar correção específica.
- **FIND-013 / #208**: contraste claro de `.initial-state-option` no Admin autenticado 4,22:1, medido com composição de ancestrais, e riscos DS04 residuais.
- **FIND-002/003 / #216**: pares de texto corrigidos no CSS publicado, mas falta rechecagem conclusiva dos estilos **e fundos efetivos** pós-publicação.
- **FIND-004 / #217**: legenda `.study-art figcaption` escura corrigida com faixa opaca e par contextual 13,85:1 calculado; falta inspeção de aplicação em runtime e leitura sobre arte.
- **Paleta/estados**: VIS-001 permanece pendente; VIS-002 e VIS-003 têm aprovação parcial contextual; EST-01–10 são direções, não manual completo de tamanhos/cores/durações.
- **Risco de compatibilidade**: `min-width:320px` no public-theme, `overflow-x:clip` na página How; efeitos de `:has`, `subgrid`, `color-mix`, custom properties e fallback real em engines/dispositivos não estão resolvidos globalmente.

**Verificação de issues em 20/10:** [#208](https://github.com/EAKerber/MobiliPresenter2D/issues/208), [#216](https://github.com/EAKerber/MobiliPresenter2D/issues/216), [#217](https://github.com/EAKerber/MobiliPresenter2D/issues/217) e [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218) estavam **open**. Abertura não confirma que o defeito ainda ocorre em todas as builds: correlacionar issue, commit, deploy e evidência antes de agir.

## 3. Onde paramos exatamente: P4-NAV / UI-ADR-005

**Produto:** branch [`experiment/shared-public-header-controller-20261020`](https://github.com/EAKerber/MobiliPresenter2D/tree/experiment/shared-public-header-controller-20261020), baseada em `main@1878ae1`, dez commits à frente / zero atrás na última verificação. **Sem PR do produto, merge ou deploy pedido.**  
**Design System:** [UI-ADR-005](ui-adr-005-public-header-controller-2026-10-20.md), PR #39 draft.  
**Mudança:** Landing e Como funciona passaram a usar `/landing/header-menu.js` já compartilhado com About; foram removidas duas implementações de menu, preservados markup e CSS; cache do script versionado para as três. Entraram foco no primeiro link ao abrir pelo teclado e restauração ao toggle ao fechar por Escape se foco estava no nav (NAV-004).  
**Outros subsistemas preservados:** `landing.js` continua com carrossel, dicas/ondas, imagens, seleção; `how-it-works.js` mantém IIFE do painel econômico.  
**Medida estática:** -1.034 unidades de comprimento de texto entre seis fontes HTML/JS em comparação à main (não equivale a menor payload/carregamento). Landing/How fazem nova requisição ao JS comum.

**CI comprovada:** [#39507803390](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39507803390) primeiro gate PASS; [#39508130387](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39508130387) último gate PASS com foco. Capturas do header estático/aberto, geometria, tema e computed styles iguais; menu teclado, Escape, fora, link, aria-expanded, ausência de dupla inicialização e Landing 5 ambientes + grupos de vantagens.

**O que os testes NÃO cobriram**: painel econômico acionado e reposicionado (apenas carregamento), matriz touch/gesture real, animação com motion **normal** (comparadores usam `reducedMotion=reduce`), fechamento via Back/navegação, resize com menu **já aberto**, zoom/reflow extremo e hitboxes a 290–320 CSS px, leitor de tela e retorno de foco em todos os contextos. “WebKit headless PASS” não deve ser chamado de “iPad aprovado”.

## 4. Próximo incremento prescrito: G1-R — fechamento funcional sem mudanças CSS

**Princípio:** usar a branch P4-NAV atual como candidato; **não** unir à branch da Landing declarativa, não mover CSS. Antes de escrever novos testes, confirmar SHA e eventuais alterações de main.

| Ordem | Ação | Oráculo / o que medir | Gate |
|---|---|---|---|
| G1-R1 | Painel de economia em `/how-it-works/`: abrir cartão, trocar seleção, fechar, redimensionar com painel aberto; preservar posição e `aria-expanded` | mesma semântica + layout candidata vs main, 390/768/1366, claro/escuro | PASS automatizado **e** screenshot da área; foco/teclado se componente interativo |
| G1-R2 | Landing motion normal vs reduce: splash, hint wave, parada após pointerdown/keydown, carrossel e CTA cozinha | sem loop inesperado, bloqueio de clique, overlay persistente, duplicação de timers ou listener removido | PASS por simulação + inspeção visual |
| G1-R3 | Menu aberto → resize/orientation, scroll/touch, Tab/Shift-Tab/Enter/Escape, outside pointer, link, return focus | `aria-expanded`, `menu-open`, foco e nav visual sincronizados; evitar trap involuntário | PASS funcional cross-engine |
| G1-R4 | Sem JavaScript, script retardado/ausente, cache alternado entre páginas; conferir conteúdo/navegação HTML e ausência de dupla inicialização | shell mantém hyperlinks acessíveis; JS falhando não expõe auth ou derruba conteúdo editorial | PASS / degradação documentada |
| G1-R5 | Fotografia da matriz estreita (320, 360, 390, 486, 768, 1366), tema claro/escuro e long labels/zoom | separar NAV-005/FIND-012 já preexistente de regressões da branch | baseline com issue rotulado; **não** corrigir CSS aqui |
| G1-R6 | Revisão manual ou em dispositivo real (preferência iPad Chrome/Safari, incl. zoom/keyboard/touch) | logs de acesso/asset e interactions com condição exata | PASS real quando possível, ou PENDING explícito |
| G1-R7 | Verificar todas as pipelines CI relevantes à mudança e se já falhavam em main | diferenciar regressão, issue conhecida, auth/provider não configurado | PASS ou blocker classificado |
| G1-R8 | Documento de decisão de integração (GO/HOLD/NO-GO) + rollback + budget preview | gate cumulativo e autorização de publicação separada | apenas documentação até autorização |

**Menor lote recomendado imediatamente:** G1-R1 + G1-R2 com fixtures/Playwright local na mesma branch; nenhum arquivo CSS alterado. Se houver comportamento divergente, diagnosticar causalmente antes de propor patch.

### Especificação mínima de teste G1-R1 (painel Como funciona)

- Abrir `button[data-economy="escala"]` e esperar `#economyDetail` visível, `aria-expanded=true`, título e texto do item correto.
- Selecionar outro item (`coletivas` ou `producao`), conferir que só um está expandido, que conteúdo mudou e painel foi movido ao final da linha correta segundo a grade; medir posição com `getBoundingClientRect`.
- Clicar no ativo e conferir painel oculto, todos `aria-expanded=false`.
- Abrir novamente, redimensionar, esperar `requestAnimationFrame(place)`, observar reposicionamento sem remover o nó, sem race/erro no console.
- Repetir em tema claro/escuro, viewport pequeno/grande e reduced-motion; contrastar candidate/main. O refactor NAV não deveria afetar esse bloco: qualquer divergência é sinal de alteração de ordem/escopo dos scripts.

### Especificação mínima G1-R2 (Landing hints)

- `prefers-reduced-motion: reduce`: verificar que a onda programada não inicia e não há overlay de splash bloqueante.
- Modo normal: observar onda inicial após temporização real, confirmar que pointerdown **ou** keydown para dicas; interação no menu também tem de parar a onda sem prejudicar fechamento do menu.
- Alternar rapidamente ambientes e simular carregamento de imagem lento/falho sem permitir imagem antiga sobrescrever nova.
- Confirmar diferenças de comportamento **intencionais** e não usar screenshot congelada de motion reduzido como prova de motion normal.

## 5. CSS G2 — backlog executável posterior, separado do patch de JS

| Prioridade | Recorte | Arquivos/lugares | Prerequisito | Saída esperada |
|---|---|---|---|---|
| G2-1 — alto | NAV-005/FIND-012 público compacto | `landing.css`, `ui-theme.css`, HTML/slots se estritamente necessário | decisão NAV-005 exata + reprodução 486/320/291 claro/escuro | fit sem corte, rótulo visível conforme homologação, contato no menu, sem regressão do controle P4 |
| G2-2 — alto | Admin `.initial-state-option` contraste claro | `admin.css` / `ui-theme.css` | acesso seguro ao DOM admin (fixture/sessão permitida); valores VIS-002 | contraste por fundo composto e leitura visual sem afetar disable/read-only |
| G2-3 — médio | FIND-002/003 e FIND-004 recheck | `landing.css`, `how-it-works.css`, `about.css`, tema | release SHA e seletor/contexto conhecido | issue fechado **somente** após readback computado e screenshot |
| G2-4 — médio | DS04 restantes | Admin/Config/Viewer por issue #208 | matriz de telas/estado auth/JS montado, não só HTML | triagem por risco, ownership e prova |
| G2-5 — condicional | extração utilitários, scene hotspot, button | `styles.css`, `viewer.css`, `ui-theme.css`, admin | G2-1…4 e G3 concluídos ou isolados | PRs pequenos de CSS com equivalência antes/depois |

**Regra:** G2-1 e G2-2 são correções funcionais/visuais independentes, não oportunidades para reorganizar import, renomear classes ou criar token universal. Reutilizar a matriz de testes, mas preservar decisões de autoria.

## 6. Preparar “CSS refactor readiness gate” (G3)

Checklist obrigatório antes da primeira regra movida:

- [ ] Seletores e consumidores conhecidos a partir de DOM real e code ownership; pseudoestado e pseudo-elementos incluídos.
- [ ] Lista precisa de CSS **co-carregados** por rota; ordem efetiva e `@media`/`!important`/specificity mapeados.
- [ ] Breakpoints e estados de tela com diferenças medidas; snapshots de tema/light/dark e contraste.
- [ ] CSS atual passa pela matriz necessária **ou** regressões pré-existentes estão reproduzidas e segregadas, nunca ignoradas.
- [ ] Família classificada igual/variante/homônimo/exceção; alvos e páginas que **não** podem mudar explicitados.
- [ ] Proposta não introduz globalidade ou acopla Admin/Viewer/Config sem contrato semântico.
- [ ] Teste antes/depois consegue capturar estilos computados, layout, estados, screenshots e custo real de CSS transferido.
- [ ] Estratégia de rollback testada e PR/preview controlados; não iniciar migração na main.
- [ ] Defeitos NAV-005, VIS e EST relevantes não ficam invisíveis por fallback/cascade nova.

Somente com este checklist completo para **uma família específica** marcar “CSS pronto para extração daquele componente”; não declarar prontidão por repositório inteiro.

## 7. Lacunas de ferramenta, cobertura e governança

- **Navegador automatizado** mede um subconjunto; um device iPad real com Chrome/Safari tem histórico de problemas em login Admin, botões e imagens segundo relato do usuário, não confirmado neste gate. Separar compatibilidade de engine da falha de rede/sessão/auth.
- **320px e menos**: `body min-width:320px` existe, e evidência de 290px mostra corte. Não remover min-width indiscriminadamente; requer política de layout de NAV-005 e inspeção da composição.
- **Zoom/altura**: usar zoom 200%/400% e paisagem/altura limitada ao avaliar reflow; a extensão da matriz depende de risco, não de combinar todos os valores cartesianamente.
- **Estado privado**: captura automatizada sem sessão não exercita Admin. Evitar credenciais no relatório; usar ambiente seguro/fixture. Teste auth não pode ser substituído por query DOM pública.
- **Temas/paleta**: computed style isolado não demonstra contraste composto nem intenção aprovada; tokens VIS-002/003 são contextuais.
- **Movimento reduzido**: para o caso de máquina com configuração de sistema `prefers-reduced-motion: reduce` true, não tratar a supressão de splash/hint como defeito sem reproduzir a preferência.
- **Retenção de artefatos**: CI pode guardar JSON/screenshots só sete dias; persistir suma técnica com SHA e resultados na DS para evitar perda de contexto.
- **CI preexistente**: branch main de produto registrou runs com falhas em workflows não relacionados; comparar por test/run/commit, não pelo número bruto de checks verdes.
- **Conflito de branch DS**: branch PR #39 divergiu de DS main por um commit; rebase/merge deve ser conduzido somente após revisar delta e assegurar não sobrescrever inventário recente. Não tentar sincronização destrutiva.
- **Economia e custo**: P4-NAV reduziu código-fonte medido, mas adicionou script externo a Landing e How; medir requests e parse/cache em browser antes de afirmar ganho de performance.

## 8. Gate de encerramento da etapa atual

**GO para pedir revisão da PR de produto (não significa merge):** G1-R1/R2/R3/R4 cobertos ou justificados, sem regressão; diferenças intencionais registradas; cenário real/zoom PENDING delimitado com plano explícito; impacto de release controlado; DS documento atualizado.

**HOLD:** painel How não testado, iPad relatado sem reprodução quando requisito do release, NAV-005 interage com alterações pretendidas, CSS muda sem medição, estado auth desconhecido.

**NO-GO:** menu injeta conteúdo do Admin/privado, UI trava sem JS, intro/hint nunca cessa, perda de foco/teclado, contraste pior, preço/cena afetado.

**Decisão corrente em 2026-10-20:** **GO para G1-R testes/documentação sem mexer em CSS; HOLD para migração CSS ampla, preview/publicação do controller ou promoção de PageComposition global.**
