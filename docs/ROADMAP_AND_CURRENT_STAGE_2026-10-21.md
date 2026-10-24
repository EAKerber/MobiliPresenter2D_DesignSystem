# Plano geral e etapa atual do Design System — 2026-10-21

## Revalidação live do estágio — 24/10/2026

- Produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` inclui ARC-03C e P-COMP-01 via PR #237.
- PR #238 continua DRAFT no head `eb7a64d552ab4b16b70c5615928d8eb10a52d54d`. O gate autenticado [Actions #40120919242 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40120919242) passou: sessão no banco interno, bootstrap do Config, negação do Admin e revogação. O DS-05A verificou readiness, duas alternâncias reversíveis de módulos e progressão por Acabamentos, Serviços e Resumo, com estimativa visível em todas as etapas. Os checks e previews passaram; Supabase Preview foi skipped por não haver branch associada. Só flags foram registradas. A issue #232 continua aberta até revisão e integração dos workflows legados; os cinco fluxos históricos continuam validados em fixture V5 local, não em staging.
- PR #239 permanece DRAFT; seis checks passaram. No preview, tema claro/escuro e teclado confirmaram anéis 4 px com cores VIS-002; CSSOM retornou offset 2,66667 px para a regra declarada 3 px. Enter ainda muda para `#main` e deixa foco em `body`; o diff só altera estilo. [Evidência do preview](../evidence/runtime/pr239-about-skip-link-preview-focus-2026-10-24.md). Sem homologação visual global ou alteração da Production.
- Issue #224 segue aberta: no deploy atual `main@5ccb2a8`, uma passagem em 390×844 não reproduziu o retorno do carrossel; a seleção de Lavanderia permaneceu visível no grupo 2. Isso não invalida a reprodução anterior 4/4; falta repetição e não houve alteração do produto.
- PR do Design System #51 permanece DRAFT no branch de handover; as atualizações desta PR são documentais e não alteram o runtime.
- Menu público na Production `main@5ccb2a8`: em 390×844, Tab/Enter abriu e levou foco ao primeiro link, Tab percorreu a navegação, Escape fechou e devolveu foco ao botão; clique externo também fechou. Com movimento reduzido, menu e controle não tinham animação em execução. A passagem cobre um recorte de rota/tema/largura; evidência em [`RUNTIME_AUDIT.md`](../RUNTIME_AUDIT.md).
- ARC-13: as oito entradas HTML têm 480 ocorrências/392 valores distintos, com 464 localizáveis, quatro identificadores excluídos e 12 itens comerciais deferidos. Em JS, o heurístico inicial achou 2.176 ocorrências em 52 fontes; uma busca direcionada por sinks DOM encontrou mais cinco rótulos de uma palavra. O índice atualizado liga e classifica **2.181 referências**: 728 textos de interface localizáveis, 1.263 trechos técnicos/identificadores e 190 decisões de conteúdo/domínio deferidas (17 de apresentação e 173 autorais/configuráveis/comerciais). Não restam referências indexadas sem classificação; a busca direcionada não prova cobertura completa da geração DOM. Evidências: [inventário suplementar de cinco sinks](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json), [cobertura de chaves](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) e [proposta de convenção](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json). No índice, 369 textos ainda não têm chave, cinco deles têm proposta em lote separado e 364 seguem sem proposta; 212 chaves usam sufixo de linha, das quais 13 têm exemplos de substituição propostos. A convenção não foi aprovada e não houve extração, migração ou alteração do produto.
- Os deploys Production atuais do Netlify principal e isolado estão READY em `main@5ccb2a8`, com nove Functions e uma Edge Function reportadas; a inspeção não executou a função.
- A estimativa geral ~22% permanece histórica/provisória e não foi recalculada sem pesos por entregável.
- VIS-002 ganhou uma leitura estática das folhas em oito entradas (Landing, Como funciona, About, Viewer, Configurador, Admin e duas rotas de acesso): exceções 2 px/2 px e 2 px/3 px aparecem em controles de Configurador/Admin/Como funciona; Viewer e Configurador têm hotspots que removem outline e exibem outras pistas visuais. São candidatos para revisão runtime, não falhas homologadas; mapa [proposto](../evidence/architecture/vis002-focus-ring-source-map-proposal-2026-10-24.md), sem CSS ou decisão canônica alterados.
- VIS-002 runtime: em Production, Tab percorreu os sete hotspots do Viewer sem ativá-los em 390 × 844. Os perímetros 02–07, em claro/escuro, tiveram medianas idênticas de 1,148:1–1,322:1; poucos pontos ≥3:1 aparecem nos módulos 04/07. O módulo 01 selecionado teve mediana 1,076:1 nos dois temas. Também comparei módulos 02–07 selecionados e focados em claro/escuro: a borda ficou transparente, o preenchimento mudou 19% e as medianas ficaram entre 1,045:1 e 1,141:1, praticamente iguais nos dois temas. Alertas locais; outros viewports e cenas seguem pendentes. [Evidência](../evidence/runtime/viewer-hotspot-focus-contrast-production-2026-10-24.md). Nenhum CSS, token ou produto foi alterado.
- VIS-002 runtime /access/: no estado anônimo de link inválido, Tab alcançou marca, tema, menu e retorno. Nos dois temas, os contornos computaram 2,66667 px; offset 2,66667 px, exceto tema com 2 px. Cores #6E512E/#D8BC7C. O botão de confirmação estava oculto; sessão válida, Configurador e Admin seguem sem cobertura runtime nesta passagem. [Evidência](../evidence/runtime/access-public-invalid-link-focus-production-2026-10-24.md). Nenhum token ou código foi alterado.
- Runtime em Production: o botão “Compra em escala” recebeu foco por Tab e exibiu contorno em claro e escuro. A cor computada e o contraste sobre o painel escuro não foram medidos; a fonte declara 2 px/offset 3 px. [Evidência](../runtime/how-it-works-economy-action-focus-production-2026-10-24.md).
- VIS-002 / disclosures nativos de “Como funciona”: 6/6 receberam foco visível por teclado nos temas claro/escuro; anel 3 px/offset 3 px nos seis. Nenhuma falha de cor na amostra (mínimo conservador 5,71:1 no claro; 9,29:1 no escuro). A largura diverge da referência de 4 px; achado e cobertura dos cartões de economia permanecem separados. [Evidência](../evidence/runtime/how-it-works-disclosure-focus-production-2026-10-24.md).


> **PONTO DE RETOMADA 22/10:** [handover canônico entre repositórios](ARCHITECTURE_CURRENT_HANDOVER_2026-10-22.md). Último gate concluído: ARC-03B **60/60 PASS**, imagens idênticas, zero alteração de `app/`, porém **sem cutover de `npm run build`**. Próximo: ARC-03C (fonte única de HTML de autoria e geração no build publicado), separado de P-COMP, P-TOKEN e auth. PR de tokens #231 permanece draft; #232 é pendência explícita e #233 já entrou na main.


> **Marco ARC-03B — 22/10:** [HTML autoral, fragmento único e teste visual 60/60 PASS](ARC03B_AUTHORED_PAGES_STATIC_COMPILER_BROWSER_GATE_2026-10-22.md), branch de produto `architecture/arc03-primary-header-fragment-prototype-20261022@e459b9b`. `app/` e Netlify inalterados; não tratar POC como cutover. **ARC-03C** é a próxima adoção de fonte gerada no build, após gate e rollback. Progresso do programa ~22% (antes 15%).


> **Checkpoint mais recente (22/10) — CI e ARC-03:** [resolução #233 no produto main@303468b, pendência #232 e protótipo compilador de header primário (3/3 PASS)](CI_BASELINE_01_RESOLUTION_AND_ARC03_HEADER_PROBE_2026-10-22.md). POC sem alteração do runtime e sem Preview. Próximo incremento ARC-03B exige separar fonte/saída e validar browser. PR #231 permanece DRAFT/HOLD.


> **CI-BASELINE-01 — 22/10 (causas identificadas):** [issue #232 (gates protegidos sem sessão), #233 (assertions públicas defasadas), diagnóstico e teste corrigido](CI_BASELINE_01_AUTH_READINESS_AND_PROJECTION_2026-10-22.md). Run anônimo confirmou `/config/→/access/` em produção e preview. Testes CP-PUBLIC-02a passaram isoladamente com fixture atualizada, mas main ainda não foi corrigida. Próximo passo: fixture autorizada de CI para `/config/`, respeitando controle de acesso; não liberar rota pública nem mascarar failures.


> **Estado mais recente P-TOKEN-02B (22/10):** [PR #231 draft/HOLD e baseline CI](P_TOKEN_02B_PR231_INTEGRATION_HOLD_BASELINE_CI_2026-10-22.md). Revisão cruzada dos testes: token 48/48 PASS e build/asset/variant PASS, porém mobile/summary/keyboard/flow/stone e allowlist apresentam falhas com histórico na main. O produto **não foi mergeado**; próxima ação CI-BASELINE-01, não mais tokens por inferência.


> **P-TOKEN-02B — GATE 48/48 PASS (22/10):** [resultado final, SHA, evidências e handover](P_TOKEN_02B_GATE_PASS_AND_INTEGRATION_HANDOVER_2026-10-22.md). Somente os 3 seletores pré-homologados VIS-002, Chromium/WebKit × 4 larguras × 2 temas, **pixelToleranceUsed=0**. A mudança continua em branch do produto sem PR/merge/release; nenhuma aplicação global da paleta.


> **P-TOKEN-01B/02A — checkpoint 22/10:** [pin imutável no produto e 32 observações CSS computadas em Chromium/WebKit](P_TOKEN_01B_02A_PRODUCT_INTEGRATION_AND_COMPUTED_AUDIT_2026-10-22.md). Fonte DS mergeada na PR #49; branch produto `architecture/p-token-01b-reference-pin-20261022` tem artefatos **não carregados** fora de `app` e gates de integridade/P-TOKEN-02A PASS. CSS de produto permanece inalterado. P-TOKEN-02B = mapeamento real por componente e distinção same-value / mudança visual.


> **P-TOKEN-01 — status de fonte de tokens (22/10):** [exportador Node e distribuição de paleta VIS-002](P_TOKEN_01_EXECUTABLE_REFERENCE_PALETTE_2026-10-22.md). A fonte executável é `decisions.json`, a saída de referência não é carregada no produto. A integração de CSS real permanece condicionada ao mapeamento e à prova visual; não confundir geração com implementação dos estados EST/VIS.


> **P-COMP-01 (resultado posterior ao V0-B):** [checkpoint de implementação e gate PASS](P_COMP_01_PUBLIC_MENU_IMPLEMENTATION_GATE_2026-10-21.md), `MobiliPresenter2D/architecture/p-comp-01-public-menu-20261021@4ba9384`. Quatro consumidores de menu público, 40 diferenciais em Chromium, 16 cenários funcionais Chromium/WebKit e 20 de Viewer NAV-005 passaram em Actions [#39697470826](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39697470826). **Código somente em branch, sem merge/release**. Não reabrir ARC/NAV nem inferir que i18n/tokens/fragmentos HTML já foram implementados.


> **V0-B — evidência estática expandida (21/10):** [fonte/cobertura, overlaps CSS e spec do piloto P-COMP-01](V0B_SOURCE_COVERAGE_CSS_OWNERSHIP_AND_FIRST_PATCH_GATE_2026-10-21.md). O índice V0-A de 826 candidatas **não** é cobertura completa; 54 scripts runtime contabilizados (52 fontes lidas, 2 dados grandes não lidos), 84 classes lexicais repetidas entre folhas (69 aparecem em folhas co-carregadas; não inferir erro). Primeiro patch escolhido: controlador público de menu (4 consumidores), **HOLD** para mudanças até gates de quatro rotas e NAV-005; versão experimental antiga divergiu em 26 commits e não deve ser mesclada. Nem tokens nem código do produto foram alterados.


> **V0-A — discovery pós #230 concluído em 21/10/2026:** [matriz de 14 famílias, índice preliminar de 826 candidatas de texto, riscos de build e plano V0-B](V0A_POST230_OWNERSHIP_LOCALIZATION_AND_BUILD_AUDIT_2026-10-21.md). `VISUAL_INVENTORY.md` e `DECISION_APPLICATION_MAP.md` ainda mantêm snapshot histórico em `1878ae1`; NÃO inferir que a auditoria DOM/CSS runtime foi refeita ou que fontes/localizações estejam completas. Autoridade técnica [ARC-01..16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md).


> **MARCO ARQUITETURAL ATUAL (ARC-01…ARC-16, 21/10/2026):** [contrato consolidado e execução V0–V6](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md) é a autoridade de direção para planejamento técnico futuro; o texto histórico abaixo continua útil para o inventário visual e homologações, mas NÃO reabre composição universal, não adia localização indefinidamente e não exige experimentos com móveis fictícios. HTML/CSS/JS puros, componentes no produto, tokens aprovados do DS integrados por PR, fragmentos HTML build-time e localização com **extração abrangente e execução incremental** estão definidos. O caso iPad de versão antiga foi reclassificado como compatibilidade legada de baixa prioridade, sem afetar bugs gerais de autenticação. Critério de parada ARC-16 inclui auditoria de todas duplicações no escopo, resolução ou exceção/backlog explícito.


> **Atualização de direção arquitetural — 21/10/2026:** a stack de interface é **HTML, CSS e JS puros**, sem framework/biblioteca de UI. Tokens semânticos e componentes nativos serão a fundação de **todas** as rotas, inclusive Landing. Data-driven permanece para domínios de móveis e ferramentas derivadas do Core do Configurador/Viewer, com seus schemas/projeções; manifesto universal de páginas não é meta obrigatória. A sequência original abaixo deve ser lida à luz do [plano atualizado e questões abertas](ARCHITECTURE_VANILLA_COMPONENTS_AND_DOMAIN_DATA_2026-10-21.md), que registra V0–V6, gates e ownership. O produto observado está em `main@840a0cd` após PR #230, logo evidências históricas em `1878ae1` precisam de reconciliação. Nenhuma implementação é autorizada por este adendo.


**Estado:** plano de trabalho e checkpoint; não homologa decisões visuais novas nem autoriza implementação no produto.  
**Fonte canônica de decisões:** [`decisions.json`](../decisions.json).  
**Repositório do produto:** [`EAKerber/MobiliPresenter2D`](https://github.com/EAKerber/MobiliPresenter2D).

## Objetivo

Tornar a interface visualmente coerente e verificável, preservando diferenças de domínio entre Landing, Viewer, Configurador, Administração e Acesso. Mapear antes de generalizar; aplicar somente decisões homologadas e rastreáveis ao componente, rota, tema, estado e evidência.

## Etapa atual — evidência runtime e fechamento do inventário visual

O inventário estático inicial está registrado em [`VISUAL_INVENTORY.md`](../VISUAL_INVENTORY.md), [`visual-inventory.json`](../visual-inventory.json) e [`DECISION_APPLICATION_MAP.md`](../DECISION_APPLICATION_MAP.md). Ele cobre as rotas e famílias documentadas, classes/folhas CSS, cores, espaçamentos, tipografia, breakpoints, movimento e assets. É um mapa de código, não uma certificação do DOM dinâmico.

A auditoria pública G1 foi registrada e integrada pela [PR #45](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/45). Em produção, o painel econômico de “Como funciona” passou nos estados amostrados; a Landing reproduziu em 4/4 uma divergência entre ambiente selecionado e página do carrossel no viewport 390×844. O defeito permanece aberto no [issue #224 do produto](https://github.com/EAKerber/MobiliPresenter2D/issues/224); a causa técnica ainda não foi isolada. Na passagem G1 original, esses estados não haviam sido verificados. Revalidações de 24/10 cobriram parcialmente movimento reduzido e Slow 3G em Como funciona, além de uma falha de imagem induzida que expôs uma lacuna visual no fallback; ver evidências runtime abaixo. Ver [`RUNTIME_AUDIT.md`](../RUNTIME_AUDIT.md) e [`runtime-evidence.json`](../runtime-evidence.json).

O registro de foco foi alinhado à paleta já aprovada pela [PR #47](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/47): contorno claro/escuro `#8B6A40` / `#D8BC7C`, 4 px com offset 3 px. Aplicação por componente, visibilidade em teclado, recorte e fundos reais continuam pendentes; não são tokens globais nem autorização de implementação.

### Próximos trabalhos desta etapa

1. Atualizar evidências visuais de cabeçalhos cujo material persistido pertence a versões anteriores; cobrir rotas públicas e a tela de login sem sessão em temas e larguras representativas, sem persistir dados de conta. **Parcial em 24/10:** em Landing, About, Viewer e Como funciona, a 290 px a área útil foi 275 px; About cortou títulos/textos e deixou 11 px do menu visíveis, Viewer cortou conteúdo/preço e deixou 13 px, e Como funciona recortou conteúdo via `overflow-x:clip` deixando 11 px do menu. A 320 px, About/Viewer tiveram overflow horizontal de 15 px na sessão; Como funciona recortou a sobra. Em 335 px as três rotas não tiveram overflow; About também não em 360/390 px. A tela de login foi observada em 1280×720, 390×844 e 320×700; o formulário não foi enviado e o autofill impede afirmar perfil limpo. Uma rechecagem de foco por Tab em 1280×720, nos temas claro/escuro, localizou 2–2,66667 px e `#6E512E` no claro frente à referência VIS-002 de 4 px/`#8B6A40`; sem envio do formulário ou CSS alterado. O estilo escuro da marca não foi medido. No campo de e-mail, a razão calculada outline/superfície opaca foi 7,29:1 no claro e 9,29:1 no escuro; a geometria continua abaixo de 4 px/3 px e a medição não generaliza. [Evidência](../evidence/runtime/admin-login-no-session-focus-production-2026-10-24.md). A Landing continua com problema a 310/290 px. Issue #218 / NAV-005 permanece aberta; nenhuma proposta foi aplicada. [Login](../evidence/runtime/admin-login-no-session-focus-production-2026-10-24.md) · [NAV-005](../evidence/runtime/landing-public-compact-header-production-2026-10-24.md) · [amostra 290/320/335 px](../evidence/runtime/public-headers-320-production-2026-10-24.md).
2. Completar verificações públicas de teclado, movimento reduzido, animações e estados de carregamento/erro em imagens; separar limitações de ferramenta de falhas do produto. **Parcial em 24/10:** em `/how-it-works/` Production, 28/28 imagens carregaram; na Landing, About e Viewer, 18/18, 3/3 e 22/22; todas sem falha e com `alt`, nos viewports registrados. Na Landing, Escape fechou o menu e devolveu foco ao botão após o splash já oculto. Em About, Enter no link de salto mudou a âncora para `#main`, mas o foco terminou em `body`; divergência observada, sem correção. A emulação de movimento reduzido cobre Landing, About e Viewer em 390 × 844 claro: transições visíveis foram reduzidas a 0,00001 s; a Landing menu abriu/fechou, a seleção de ambiente e o avanço do carrossel terminaram sem animação ativa, e a seleção do Viewer por teclado também terminou sem animações em execução. No baseline sem redução, a Landing registrou intro/reveal de 0,32–0,65 s, About não mostrou animações, e Viewer usava transições de 0,16/0,18 s. A cobertura não avalia animações em curso em todos os estados/rotas nem outras dimensões. Rede lenta foi simulada parcialmente em Como funciona, com atraso perceptível e zero falhas na amostra. Uma imagem não decorativa foi quebrada de forma controlada no DOM isolado: o `alt` permaneceu, mas o elemento colapsou para 449 × 43 px, sem handler ou placeholder customizado observado. Restaurada e carregada; a apresentação de erro fica como lacuna visual, não correção aplicada. [Rotas públicas, foco/imagens](../evidence/runtime/public-routes-keyboard-images-production-2026-10-24.md) · [Movimento reduzido nas três rotas](../evidence/runtime/public-routes-reduced-motion-runtime-production-2026-10-24.md) · [Como funciona, Slow 3G e erro](../evidence/runtime/how-it-works-motion-css-runtime-snapshot-production-2026-10-24.md).
3. Revalidar no DOM temas, superfícies e estados dinâmicos dos achados visuais. Medir contrastes efetivos com transparência/ancestrais e registrar cada caso como aprovado, falha, exceção ou não verificado. **Parcial em 24/10:** uma amostra em Landing, About e Como funciona nos dois temas mediu 4,79:1–13,85:1 nos pares de texto opacos selecionados; a faixa escura da legenda em Como funciona está presente e mede 13,85:1. Os valores atuais diferem de medições antigas, mas não fecham issue #216 nem certificam cobertura global. Transparências, imagens, todos os estados de foco/seleção e cobertura de todas as rotas/componentes seguem pendentes. [Evidência da amostra](../evidence/runtime/public-text-contrast-production-themes-2026-10-24.md).
4. Fazer uma sequência autenticada controlada para FIND-007 / issue #213 somente quando o usuário estiver conectado na sessão de produção: menu após login sem recarga, navegação privada, nova aba e saída. Não registrar email, credenciais, tokens ou dados de convite.
5. Revisar cobertura de todos os itens do inventário e encerrar a etapa quando cada rota/família estiver ligada a evidência atual ou explicitamente marcada como não verificada.

## Critério para homologar conformidade

Um item só fica conforme quando seu papel semântico e par de cores estão aprovados para a superfície/tema/estado, o DOM real corresponde ao par, contraste e indicação não cromática atendem aos critérios registrados, interação e teclado funcionam nos estados pertinentes, e as rotas/breakpoints cobertos têm evidência. Um valor existente no CSS não vira token por isso. Ver [`PALETTE_CONFORMANCE.md`](../PALETTE_CONFORMANCE.md).

## Sequência futura

1. **Concluir inventário visual e evidência runtime.** Registrar classes, cores, breakpoints, animações, microinterações, espaçamentos, assets, estados e rastreabilidade. Tratar defeitos como achados separados; não alterar CSS para mascarar comportamento.
2. **Homologar os valores e padrões que ainda dependem de escolha.** Exibir comparações identificadas como experimentais apenas quando as decisões existentes não definirem uma solução. Persistir aprovações e limites em `decisions.json`.
3. **Fundação visual e aplicação gradual.** Organizar apenas tokens aprovados e aplicar por família de componentes no produto. Confirmar diferenças de comportamento antes de reduzir duplicações; executar DOM, interação e revisão visual por PR. Usar preview quando integração comportamental ou risco de efeito em cadeia justificar.
4. **Schema de interface data-driven (futuro).** Projetar schema próprio para estrutura da interface, separado dos dados do configurador e da configuração de etapas. Não mover HTML, CSS, handlers ou lógica arbitrária para dados de cliente.
5. **Textos e tradução (futuro).** Separar conteúdo textual da estrutura visual depois da fundação de interface. Preservar Português do Brasil; escolher estratégia de idiomas quando essa etapa começar.
6. **Inventário completo de JavaScript (futuro posterior).** Mapear módulos, funções, eventos, fluxos e dependências depois do foco visual; usar o mapa para orientar mudanças data-driven, sem ampliar a etapa atual.

## Organização e governança

- `decisions.json` é canônico para decisões. Mapa de aplicação, inventário, auditoria, evidência e laboratório mantêm responsabilidades separadas.
- Cores ou medidas observadas permanecem “uso atual” até homologação explícita.
- VIS-001 e CMP-001 permanecem pendentes onde o conteúdo ou a decisão não foi recuperado; GOV-001/NAV-001/NAV-002 têm lacuna de origem encerrada como não recuperável, sem reconstruir conteúdo.
- PR #39 permanece draft e não deve ser integrada em bloco: está divergente, tem 25 arquivos e combina atualizações documentais com experimentos/workflows. Se partes forem aproveitadas, criar mudanças focadas sobre a `main` atual e reconciliar seus estados com este checkpoint.
- O checkout local do produto está sujo. Qualquer implementação futura deverá usar um checkout isolado e preservar as alterações locais existentes.
- Nenhuma PR ou preview deve ser tratado como decisão estética ou como autorização de publicar produção.


### ARC-13 — cobertura e pendências em 24/10/2026

As oito entradas HTML do produto `main@5ccb2a8` foram reconciliadas por ocorrência: 480 registros e 392 valores distintos, com 464 textos localizáveis, quatro identificadores excluídos e 12 trechos comerciais deferidos. O inventário inicial continha 2.176 candidatos JS heurísticos em 52 fontes. A revisão direcionada dos sinks textuais nas 52 fontes encontrou cinco rótulos de uma palavra omitidos pelo heurístico; o índice passou a ligar e classificar 2.181 referências: 728 textos de interface, 1.263 trechos técnicos e 190 itens de conteúdo/domínio deferidos. Não restam referências indexadas sem classificação. A busca de sinks foi direcionada e não prova cobertura completa de toda construção de DOM; os cinco acréscimos estão em [lote suplementar](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json). Os três scripts inline de `app/config/index.html` (2.343 bytes) foram revisados e não contêm literais de interface localizáveis. `stone-data.js` e `mask-data.js` foram revisados nos hashes registrados, sem texto humano localizável. Permanecem pendentes a revisão de strings geradas no DOM, ownership dos 190 itens de conteúdo/domínio deferidos, chaves semânticas estáveis, extração e migração. A checagem de chaves encontrou 369/728 ocorrências localizáveis sem chave e outras 212 com identificadores terminados no número da linha; esses valores não são tratados como chaves estáveis. Cinco rótulos administrativos receberam propostas contextuais separadas, ainda não canônicas, sem alterar o índice. Ver [cobertura e qualidade inicial](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) e [propostas de cinco rótulos](../evidence/architecture/arc13-semantic-key-proposal-admin-sinks-2026-10-24.json). Isso fecha a triagem lexical documentada, não conclui V0/V1 nem cria bundles. Qualquer extração deve preservar owner/consumer/chave semântica e ocorrer em lotes revisáveis; não substituir texto em massa por regex.


### Gates DS-05 e NAV-005 revalidados — 24/10/2026

- **DS-05A parcialmente verificado.** No gate autenticado da PR #238 [Actions #40120919242](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40120919242), a superfície inicial mostrou contadores coerentes, estimativa e ação seguinte visíveis. Dois toggles alteraram e restauraram a contagem; a estimativa permaneceu visível após cada mudança/restauração. O fluxo padrão abriu Acabamentos, Serviços e Resumo, mantendo a estimativa. Apenas flags foram registradas; grant revogado e Admin negado. Continuam pendentes escolhas de acabamentos/serviços, combinações de preço, envio e cobertura Admin. O fixture não recebeu permissões adicionais. [Evidência de progressão](../evidence/runtime/ds05a-ci-stage-progression-2026-10-24.md) · [limite da fixture](../evidence/runtime/ds05a-ci-auth-fixture-limit-2026-10-24.md).
- **DS-05B/DS-05C permanecem pendentes**, conforme a sequência canônica de `decisions.json`; nenhum detector genérico ou integração com o laboratório v0.3 foi homologado por esta observação.
- **NAV-005:** a proposta compacta foi exercitada temporariamente no DOM público e está registrada em [evidência de 24/10](../evidence/runtime/nav005-public-compact-header-proposal-2026-10-24.md). Isso valida viabilidade da composição em amostras, mas não substitui revisão visual completa nem altera o registro canônico, que mantém `implementationAuthorized: false`. Não houve alteração do produto.


### About / Production — destino do link de salto (24/10/2026)

A auditoria anônima da Production confirmou que Enter em “Pular para o conteúdo” altera a URL para `#main`, mas deixa o foco em `body`; `main#main` não recebe foco nesta passagem. O estilo do link também diverge da referência VIS-002, e PR produto #239 cobre apenas o CSS, não o foco no destino. Evidência: [auditoria de foco em Production](../evidence/runtime/about-skip-link-production-focus-2026-10-24.md). Isso fica como diferença runtime descoberta; nenhuma implementação ou aprovação de comportamento foi inferida.


### CI-BASELINE-01 — configuração Netlify e GitHub Actions (24/10/2026)

O deploy isolado `m2d-auth-ci-isolated` está READY em `main@5ccb2a8` e inclui `access-check` (publicado às 09:18 UTC). Readback de nomes/escopos confirmou `DATABASE_URL` e `ACCESS_GATE_SECRET` nos contextos Netlify registrados; os valores não foram copiados nem validados individualmente, e o readback não exercitou a Edge Function. O gate autenticado da PR #238 usa conexão independente do GitHub Environment `ci-auth-isolated`; no head `eb7a64d`, run [#40120919242 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40120919242) validou a conexão ao banco interno, grant de curta duração, resgate e revogação. Isso não comprova que as variáveis Netlify estão corretas nem que `access-check` foi exercitada. [Registro de contextos](../evidence/runtime/netlify-ci-auth-environments-2026-10-24.md).


### ARC-13 — convenção de chave semântica proposta, sem canonização

Foi preparada uma convenção revisável para substituir sufixos numéricos por nomes semânticos estáveis, preservando namespaces atuais e contratos distintos de parâmetros. A proposta contém 13 exemplos, incluindo mensagens de Configuração, Hierarquia, Apresentação, Fluxo, Preços e reparo legado. Não modifica o índice nem o produto; faltam revisão/aprovação da convenção, 199 chaves numéricas restantes sem exemplo e 364 ocorrências sem proposta de chave (cinco sinks já têm lote separado). [Proposta e perguntas de revisão](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json).


### Foco e salto ao conteúdo — Landing e Como funciona (24/10/2026)

A Production não apresenta link de salto ao conteúdo nessas duas rotas: o primeiro Tab foca a marca, e `main` não possui id. A regra fonte declara 3 px/offset 3 px e cores claro `#6E512E`/escuro `#D8BC7C`; a referência é 4 px/offset 3 px e `#8B6A40`/`#D8BC7C`, portanto a divergência declarada é largura e cor clara, não o offset global. A CSSOM retornou 2.67 px nessa sessão para uma regra de 3 px, inclusive em elemento de teste; causa desconhecida. A CTA interna `#passos` em Como funciona não é um skip link. Evidência: [auditoria em Production](../evidence/runtime/public-skip-navigation-focus-2026-10-24.md). Fica como achado runtime, sem inferir solução ou autorização de implementação.


### VIS-002 — anel de foco em componentes públicos

A amostra Production na Landing mediu dez focos reais em dois temas. As regras fonte declaram 3 px/offset 3 px globalmente e 3 px/offset 2 px no controle de tema; as cores são `#6E512E`/`#D8BC7C`. VIS-002 referencia 4 px/offset 3 px e cores `#8B6A40`/`#D8BC7C`. A CSSOM computou 2.67 px para `outline:3px` na sessão auditada, até em elemento de teste; a causa é desconhecida. A evidência não homologa implementação geral nem mede todas as rotas/controles. [Registro runtime](../evidence/runtime/public-focus-ring-production-component-sample-2026-10-24.md).


### VIS-002 — origem CSS e mapa de escopo proposto

A fonte pública declara contorno 3 px/offset 3 px; `ui-theme.css` troca a cor clara por `#6E512E` e o controle de tema declara offset 2 px. O About da PR #239 propõe localmente 4 px/offset 3 px. Foi preparado um mapa não canônico por componente e rota, preservando o limite de implementação global atualmente não autorizada. [Mapa de origem e revisão](../evidence/architecture/vis002-focus-ring-source-map-proposal-2026-10-24.md).


- VIS-002 / foco em Como funciona: CSSOM em Production confirmou, para “Compra em escala” no tema claro, `#6E512E` sobre a superfície opaca `#25231F`, contraste calculado de 2,15:1. Uma leitura retornou offset 2.66667 px; a passagem de confirmação retornou 3 px, como na fonte; diferença sem causa isolada. Risco observado nesta combinação; tema escuro, outros cards e superfícies seguem sem readback CSSOM. [Detalhe](../evidence/runtime/how-it-works-economy-action-focus-production-2026-10-24.md).


### Como funciona — controles expansíveis por teclado (24/10/2026)

Em Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, viewport 1280×720 escuro, Enter e Espaço alternados expandiram 6/6 disclosures nativos e 6/6 cartões de economia. Os estados abriram e o conteúdo foi exposto à árvore de acessibilidade. É cobertura funcional pontual, sem avaliação com leitor de tela, em outros navegadores/temas/larguras ou aparência do foco; não fecha achados. [Evidência](../evidence/runtime/how-it-works-accordion-keyboard-production-2026-10-24.md).


### VIS-002 — foco nos cartões de economia em Production (24/10/2026)

Tab nos seis cartões de “Por que custa menos?” computou 2 px/offset 3 px nos temas claro e escuro. Em tema claro, `#6E512E` sobre `#25231F` mediu 2,15:1; em escuro, `#D8BC7C` sobre `#25231F` mediu 8,52:1. A amostra identifica falha de indicador de foco na superfície escura sob tema claro e diferença de largura frente à referência de 4 px. Sem decisão de correção ou implementação; restante das rotas/estados segue pendente. [Evidência](../evidence/runtime/how-it-works-economy-focus-six-cards-production-2026-10-24.md).


### Como funciona — movimento reduzido e animações (24/10/2026)

O snapshot inicial não estava com redução ativa e não capturou animações CSS ativas. A emulação posterior em Production confirmou o efeito da regra no CTA hover e no disclosure observados: a duração foi reduzida a 0,00001 s e o disclosure abriu sem animação em curso. Essa cobertura é parcial, conforme a evidência revalidada abaixo. [Evidência](../evidence/runtime/how-it-works-motion-css-runtime-snapshot-production-2026-10-24.md).


### VIS-002 — decisão de foco em superfície escura

O FIND-017 foi confirmado nos seis cartões da economia. Uma proposta experimental compara `#D8BC7C` (8,52:1) e `#8B6A40` (3,16:1) sobre a superfície `#25231F`, mantendo a referência geométrica 4 px/offset 3 px. A opção A tem maior margem numérica, mas nenhuma escolha foi homologada. VIS-002 ainda declara mapeamento por componente pendente e `implementationAuthorized: false`; produto e decisões canônicas permanecem sem alteração. [Proposta A/B](../evidence/architecture/vis002-economy-dark-surface-focus-candidate-2026-10-24.md).


### Viewer — hotspot 02 e foco em Production (24/10/2026)

No Viewer público em Production, Tab focou o hotspot do módulo 02 nos temas Claro e Escuro sem ativá-lo. O `:focus-visible` usa `::after` com borda computada de 2 px na cor aproximada `#DDC48C`, preenchimento semitransparente e marcador numerado; o botão zera o `outline`. A mesma cor foi computada nos dois temas, sobre imagem fotográfica. Em capturas pareadas do screenshot real, no hotspot 02 móvel, o contraste entre o pixel focado e o pixel correspondente sem foco teve mediana 1,41:1 e máximo 1,49:1 nos 200 pontos da borda; nenhum atingiu 3:1. É uma amostra de borda/fotografia, não certificação geral. Não concluir conformidade. A referência geométrica de 4 px e a suficiência das pistas alternativas continuam por avaliar. [Evidência runtime](../evidence/runtime/viewer-hotspot-focus-contrast-production-2026-10-24.md). Nenhum CSS, token ou produto foi alterado.


### Viewer — hotspot 02 em viewport móvel (24/10/2026)

No viewport 390 × 844, o Módulo 02 recebeu foco por Tab em Claro e Escuro, mantendo o Módulo 01 selecionado. Alvo (56 × 57 px) e marcador circular (26 × 26 px) ficaram dentro da cena, sem recorte observado; `scrollWidth` e `clientWidth` foram 375 px. A borda computou 2 px em `#DDC48C`. A amostra inicial de 200 pontos no centro da borda registrou mediana 1,41:1 e máximo 1,49:1; outra amostra de 3.132 pixels no preenchimento do módulo 01 selecionado registrou mediana 1,076:1 e máximo 1,091:1. O complemento posterior amostrou ambas as linhas de pixels dos perímetros dos módulos 02–07, em método distinto; veja seção seguinte. WCAG 2.2 SC 2.4.13 (AAA) usa mudança ≥3:1 entre os mesmos pixels focados e sem foco; estas medições locais não constituem avaliação formal de conformidade. [Critério W3C](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance). [Registro runtime](../evidence/runtime/viewer-hotspot-focus-contrast-production-2026-10-24.md). Tema inicial e viewport foram restaurados e a aba temporária fechada.


### Viewer — foco nos sete hotspots e diferença para seleção (24/10/2026)

No viewport móvel 390 × 844, Tab percorreu os sete hotspots sem ativá-los; todos mantiveram marcador visível e ficaram dentro da cena, sem overflow horizontal. Módulos 02–07 computaram borda de foco de 2 px em `#DDC48C`; no módulo 01 selecionado, a borda ficou transparente e só o preenchimento de 19% mudou (mediana 1,076:1, P95 1,083:1, máximo 1,091:1 em 3.132 px). Para os perímetros 02–07, o pareamento em claro/escuro foi idêntico dentro da foto; medianas de 1,148:1–1,322:1, com poucos pontos ≥3:1 nos módulos 04/07. Também comparei cada módulo 02–07 selecionado e focado nos dois temas: a borda computou transparente e só o preenchimento mudou; as medianas ficaram entre 1,045:1 e 1,141:1, praticamente iguais em claro e escuro. No módulo 06, pontos ≥3:1 se concentram em trechos escuros, embora a mediana seja 1,087:1. São medições locais; outras dimensões e cenas continuam pendentes e não há homologação. [Evidência runtime](../evidence/runtime/viewer-hotspot-focus-contrast-production-2026-10-24.md). Nenhum código de produto ou token foi alterado.


### Como funciona — emulação de movimento reduzido em Production (24/10/2026)

No deploy `6adc221479c773577ed45e23` (`main@5ccb2a8`), em contexto anônimo isolado e viewport 1280 × 720, emulei `prefers-reduced-motion`. Sem redução, o CTA hover declara transição `transform, background` de 0,18 s e termina com deslocamento de −2 px; com redução, as durações computadas caem para 0,00001 s. O disclosure nativo abriu sob redução, mostrou conteúdo e não registrou animação ativa; sem redução, a transição computada do disclosure foi 0 s. A amostra confirma a media query para os elementos vistos, não todos os elementos/iframes da rota. Rede lenta foi simulada parcialmente sem falhas naturais observadas; atraso e imagens lazy pendentes estão registrados. Uma falha artificial numa imagem não decorativa manteve o `alt`, mas sem placeholder customizado observado e com altura reduzida a 43 px; falta avaliar outros estados/elementos. [Evidência revalidada](../evidence/runtime/how-it-works-motion-css-runtime-snapshot-production-2026-10-24.md). Nenhum código do produto foi alterado.


### Como funciona — rede lenta e carregamento de imagens (24/10/2026)

Em Production `main@5ccb2a8` e deploy READY `6adc221479c773577ed45e23`, uma passagem anônima isolada sob Slow 3G, com cache ignorado, registrou `hero-abertura.webp` em ~10,23 s. Em um snapshot, 12/28 imagens estavam carregadas, 16 lazy ainda pendentes e zero falhas; imagens que entraram na viewport carregaram em snapshots posteriores. Isso confirma atraso na amostra, não uma falha. Uma imagem não decorativa quebrou de forma induzida: o `alt` permaneceu, mas o elemento caiu para 449 × 43 px sem placeholder customizado observado; permanece como possível lacuna visual. [Evidência](../evidence/runtime/how-it-works-motion-css-runtime-snapshot-production-2026-10-24.md). Emulações foram removidas e a aba temporária fechada.


### Viewer — comparação desktop do hotspot 01 selecionado (24/10/2026)

Em `/viewer/` Production, 1279 × 663 CSS px, DPR 1,5, comparei em claro e escuro o módulo 01 selecionado com/sem `:focus-visible`. A seleção já mostra moldura e marcador; o foco mantém a borda do pseudo-elemento transparente e acrescenta somente preenchimento `rgba(216, 188, 124, 0.19)`. As capturas pareadas mostram a tonalidade acrescentada apenas pelo preenchimento. A razão de luminância por pixel entre estado focado/sem foco foi medida depois em `/viewer/` móvel, para dois hotspots, usando screenshot renderizado; os valores não generalizam para o desktop nem para outros alvos. A distinção foco/seleção e a cobertura dos demais fundos continuam abertas. [Evidência](../evidence/runtime/viewer-hotspot-focus-contrast-production-2026-10-24.md).
