# Plano geral e etapa atual do Design System — 2026-10-21

## Revalidação live do estágio — 24/10/2026

- Produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` já inclui o merge da PR #237: ARC-03C e reconciliação do controlador público P-COMP-01 estão presentes. Portanto, os avisos históricos abaixo que indicam ARC-03C como próximo incremento estão superados.
- A PR produto #239 aplica VIS-002 somente ao skip link de About; seis checks passaram e a observação direta do Deploy Preview confirmou foco/estilo no claro, escuro e viewport móvel. A PR permanece DRAFT; isso não representa integração ou homologação global.
- A PR produto #238 continua DRAFT e a issue #232 aberta. O gate autenticado isolado não substitui a integração dos workflows legados.
- V0/V1 continua aberto. Os índices de localização são heurísticos e foram produzidos em `840a0cda`; dos 26 arquivos indexados, 7 hashes divergem no produto atual. A árvore atual contém 8 HTML e 77 JS sob `app/` (inclui dados e testes); ainda é necessária classificação por papel e extração integral de strings realmente localizáveis. A próxima etapa executável é atualizar esse mapa contra a main atual e completar a cobertura ARC-13, sem misturar dados V5/autoria ou mensagens técnicas.
- ARC-13 já tem classificação manual documental de 162 ocorrências / 129 valores distintos entre lotes em quatro entradas HTML: `/about/`, `/viewer/`, `/access/`, `/access/manage.html` e `/admin.html`, além das 60 entradas em sete arquivos JS; nenhum bundle ou código de produto foi alterado. A cobertura estática das seis outras entradas HTML e o restante do runtime seguem pendentes.
- A estimativa de ~22% permanece somente histórica/provisória; não foi recalculada sem pesos por entregável e inventário atualizados.


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

A auditoria pública G1 foi registrada e integrada pela [PR #45](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/45). Em produção, o painel econômico de “Como funciona” passou nos estados amostrados; a Landing reproduziu em 4/4 uma divergência entre ambiente selecionado e página do carrossel no viewport 390×844. O defeito permanece aberto no [issue #224 do produto](https://github.com/EAKerber/MobiliPresenter2D/issues/224); a causa técnica ainda não foi isolada. Movimento reduzido, animação ativa, rede lenta e falha de imagem seguem sem verificação. Ver [`RUNTIME_AUDIT.md`](../RUNTIME_AUDIT.md) e [`runtime-evidence.json`](../runtime-evidence.json).

O registro de foco foi alinhado à paleta já aprovada pela [PR #47](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/47): contorno claro/escuro `#8B6A40` / `#D8BC7C`, 4 px com offset 3 px. Aplicação por componente, visibilidade em teclado, recorte e fundos reais continuam pendentes; não são tokens globais nem autorização de implementação.

### Próximos trabalhos desta etapa

1. Atualizar evidências visuais de cabeçalhos cujo material persistido pertence a versões anteriores; cobrir rotas públicas e a tela de login sem sessão em temas e larguras representativas, sem persistir dados de conta.
2. Completar verificações públicas de teclado, movimento reduzido, animações e estados de carregamento/erro em imagens; separar limitações de ferramenta de falhas do produto.
3. Revalidar no DOM temas, superfícies e estados dinâmicos dos achados visuais. Medir contrastes efetivos com transparência/ancestrais e registrar cada caso como aprovado, falha, exceção ou não verificado.
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


### ARC-13 — avanço da cobertura bruta em 24/10/2026

A varredura contra produto `main@5ccb2a8` agora inclui oito entradas HTML e 52 fontes JS runtime legíveis. Os índices separados registram 480 candidatos HTML e 2.176 ocorrências JS heurísticas; não são cobertura completa nem strings prontas para bundles. Permanecem sem triagem semântica e owner/chave, fora dos scripts inline, dados de máscaras/pedra deferidos, strings produzidas no DOM e dados comerciais V5. Próximo gate: classificação rastreável por arquivo/linha/consumidor/owner/status, leitura do conteúdo dinâmico e tratamento explícito das fontes ainda não verificadas. Não substituir strings em lote com base em regex.
