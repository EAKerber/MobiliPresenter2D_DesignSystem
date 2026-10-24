# Plano geral e etapa atual do Design System — 2026-10-21

## Revalidação live do estágio — 24/10/2026

- Produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` inclui ARC-03C e P-COMP-01 via PR #237.
- PR #238 de autenticação permanece DRAFT; o gate autenticado passou em `a9129e1`, e os commits posteriores até `a2835c6` alteraram apenas documentação. Gates anônimo/assets passaram no head atual. A issue #232 continua aberta até integrar os workflows legados.
- PR #239 permanece DRAFT; os seis checks e a validação localizada do skip link About passaram. Não implica aprovação visual global.
- Issue #224 segue aberta: no deploy atual `main@5ccb2a8`, uma passagem em 390×844 não reproduziu o retorno do carrossel; a seleção de Lavanderia permaneceu visível no grupo 2. Isso não invalida a reprodução anterior 4/4; falta repetição e não houve alteração do produto.
- PR do Design System #51 permanece DRAFT no branch de handover; as atualizações desta PR são documentais e não alteram o runtime.
- Menu público na Production `main@5ccb2a8`: em 390×844, Tab/Enter abriu e levou foco ao primeiro link, Tab percorreu a navegação, Escape fechou e devolveu foco ao botão; clique externo também fechou. Com movimento reduzido, menu e controle não tinham animação em execução. A passagem cobre um recorte de rota/tema/largura; evidência em [`RUNTIME_AUDIT.md`](../RUNTIME_AUDIT.md).
- ARC-13: as oito entradas HTML têm 480 ocorrências/392 valores distintos, com 464 localizáveis, quatro identificadores excluídos e 12 itens comerciais deferidos. Em JS, o heurístico inicial achou 2.176 ocorrências em 52 fontes; uma busca direcionada por sinks DOM encontrou mais cinco rótulos de uma palavra. O índice atualizado liga e classifica **2.181 referências**: 728 textos de interface localizáveis, 1.263 trechos técnicos/identificadores e 190 decisões de conteúdo/domínio deferidas (17 de apresentação e 173 autorais/configuráveis/comerciais). Não restam referências indexadas sem classificação; a busca direcionada não prova cobertura completa da geração DOM. Evidências: [inventário suplementar de cinco sinks](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json), [cobertura de chaves](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) e [proposta de convenção](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json). No índice, 369 textos ainda não têm chave, cinco deles têm proposta em lote separado e 364 seguem sem proposta; 212 chaves usam sufixo de linha, das quais 13 têm exemplos de substituição propostos. A convenção não foi aprovada e não houve extração, migração ou alteração do produto.
- Os deploys Production atuais do Netlify principal e isolado estão READY em `main@5ccb2a8`, com nove Functions e uma Edge Function reportadas; a inspeção não executou a função.
- A estimativa geral ~22% permanece histórica/provisória e não foi recalculada sem pesos por entregável.
- VIS-002 ganhou uma leitura estática das folhas em oito entradas (Landing, Como funciona, About, Viewer, Configurador, Admin e duas rotas de acesso): exceções 2 px/2 px e 2 px/3 px aparecem em controles de Configurador/Admin/Como funciona; Viewer e Configurador têm hotspots que removem outline e exibem outras pistas visuais. São candidatos para revisão runtime, não falhas homologadas; mapa [proposto](../evidence/architecture/vis002-focus-ring-source-map-proposal-2026-10-24.md), sem CSS ou decisão canônica alterados.
- VIS-002 runtime: em Production, o Viewer mostrou borda dourada e marcador do hotspot focado por Tab nos temas claro/escuro; a amostra não mediu contraste nem cobre outros componentes. [Evidência](../evidence/runtime/viewer-scene-hotspot-keyboard-focus-production-2026-10-24.md).
- Runtime em Production: o botão “Compra em escala” recebeu foco por Tab e exibiu contorno em claro e escuro. A cor computada e o contraste sobre o painel escuro não foram medidos; a fonte declara 2 px/offset 3 px. [Evidência](../runtime/how-it-works-economy-action-focus-production-2026-10-24.md).


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


### ARC-13 — cobertura e pendências em 24/10/2026

As oito entradas HTML do produto `main@5ccb2a8` foram reconciliadas por ocorrência: 480 registros e 392 valores distintos, com 464 textos localizáveis, quatro identificadores excluídos e 12 trechos comerciais deferidos. O inventário inicial continha 2.176 candidatos JS heurísticos em 52 fontes. A revisão direcionada dos sinks textuais nas 52 fontes encontrou cinco rótulos de uma palavra omitidos pelo heurístico; o índice passou a ligar e classificar 2.181 referências: 728 textos de interface, 1.263 trechos técnicos e 190 itens de conteúdo/domínio deferidos. Não restam referências indexadas sem classificação. A busca de sinks foi direcionada e não prova cobertura completa de toda construção de DOM; os cinco acréscimos estão em [lote suplementar](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json). Os três scripts inline de `app/config/index.html` (2.343 bytes) foram revisados e não contêm literais de interface localizáveis. `stone-data.js` e `mask-data.js` foram revisados nos hashes registrados, sem texto humano localizável. Permanecem pendentes a revisão de strings geradas no DOM, ownership dos 190 itens de conteúdo/domínio deferidos, chaves semânticas estáveis, extração e migração. A checagem de chaves encontrou 369/728 ocorrências localizáveis sem chave e outras 212 com identificadores terminados no número da linha; esses valores não são tratados como chaves estáveis. Cinco rótulos administrativos receberam propostas contextuais separadas, ainda não canônicas, sem alterar o índice. Ver [cobertura e qualidade inicial](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) e [propostas de cinco rótulos](../evidence/architecture/arc13-semantic-key-proposal-admin-sinks-2026-10-24.json). Isso fecha a triagem lexical documentada, não conclui V0/V1 nem cria bundles. Qualquer extração deve preservar owner/consumer/chave semântica e ocorrer em lotes revisáveis; não substituir texto em massa por regex.


### Gates DS-05 e NAV-005 revalidados — 24/10/2026

- **DS-05A permanece incompleto.** O run autenticado da PR produto #238 passou e o fixture alcança `/config/`, inicia o workspace e depois confirma revogação; porém o teste não inspeciona o contador nem a barra de preço/próxima etapa. Ele espera 401/403 de `/api/admin-bootstrap`, então não monta as opções administrativas. Evidências: [limite da fixture autenticada](../evidence/runtime/ds05a-ci-auth-fixture-limit-2026-10-24.md) e [limite de acesso anônimo](../evidence/runtime/ds05a-anonymous-access-gate-2026-10-24.md). Os alvos do Config podem ser observados pela fixture existente; para o Admin, falta sessão administrativa de teste ou fixture separado explicitamente autorizado. Não ampliar permissões do papel `access_ci_fixture` por inferência.
- **DS-05B/DS-05C permanecem pendentes**, conforme a sequência canônica de `decisions.json`; nenhum detector genérico ou integração com o laboratório v0.3 foi homologado por esta observação.
- **NAV-005:** a proposta compacta foi exercitada temporariamente no DOM público e está registrada em [evidência de 24/10](../evidence/runtime/nav005-public-compact-header-proposal-2026-10-24.md). Isso valida viabilidade da composição em amostras, mas não substitui revisão visual completa nem altera o registro canônico, que mantém `implementationAuthorized: false`. Não houve alteração do produto.


### About / Production — destino do link de salto (24/10/2026)

A auditoria anônima da Production confirmou que Enter em “Pular para o conteúdo” altera a URL para `#main`, mas deixa o foco em `body`; `main#main` não recebe foco nesta passagem. O estilo do link também diverge da referência VIS-002, e PR produto #239 cobre apenas o CSS, não o foco no destino. Evidência: [auditoria de foco em Production](../evidence/runtime/about-skip-link-production-focus-2026-10-24.md). Isso fica como diferença runtime descoberta; nenhuma implementação ou aprovação de comportamento foi inferida.


### CI-BASELINE-01 — configuração Netlify e GitHub Actions (24/10/2026)

O deploy isolado `m2d-auth-ci-isolated` está READY em `main@5ccb2a8` e inclui `access-check`. A execução autenticada da PR produto #238 recebe o banco de `CI_STAGING_DATABASE_URL` no GitHub Environment `ci-auth-isolated`, separado do `DATABASE_URL` Netlify. O readback encontrou a conexão interna de teste no contexto Netlify `dev`, mas não em `production`/ `deploy-preview`, que ainda espelham o projeto principal. As Functions de grant/sessão leem o contexto Netlify; alinhar antes de considerar o host isolado pronto para o runtime autenticado. [Registro seguro de contextos](../evidence/runtime/netlify-ci-auth-environments-2026-10-24.md). Nenhum segredo, valor ou deploy foi alterado.


### ARC-13 — convenção de chave semântica proposta, sem canonização

Foi preparada uma convenção revisável para substituir sufixos numéricos por nomes semânticos estáveis, preservando namespaces atuais e contratos distintos de parâmetros. A proposta contém 13 exemplos, incluindo mensagens de Configuração, Hierarquia, Apresentação, Fluxo, Preços e reparo legado. Não modifica o índice nem o produto; faltam revisão/aprovação da convenção, 199 chaves numéricas restantes sem exemplo e 364 ocorrências sem proposta de chave (cinco sinks já têm lote separado). [Proposta e perguntas de revisão](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json).


### Foco e salto ao conteúdo — Landing e Como funciona (24/10/2026)

A Production não apresenta link de salto ao conteúdo nessas duas rotas: o primeiro Tab foca a marca, e `main` não possui id. A regra fonte declara 3 px/offset 3 px e cores claro `#6E512E`/escuro `#D8BC7C`; a referência é 4 px/offset 3 px e `#8B6A40`/`#D8BC7C`, portanto a divergência declarada é largura e cor clara, não o offset global. A CSSOM retornou 2.67 px nessa sessão para uma regra de 3 px, inclusive em elemento de teste; causa desconhecida. A CTA interna `#passos` em Como funciona não é um skip link. Evidência: [auditoria em Production](../evidence/runtime/public-skip-navigation-focus-2026-10-24.md). Fica como achado runtime, sem inferir solução ou autorização de implementação.


### VIS-002 — anel de foco em componentes públicos

A amostra Production na Landing mediu dez focos reais em dois temas. As regras fonte declaram 3 px/offset 3 px globalmente e 3 px/offset 2 px no controle de tema; as cores são `#6E512E`/`#D8BC7C`. VIS-002 referencia 4 px/offset 3 px e cores `#8B6A40`/`#D8BC7C`. A CSSOM computou 2.67 px para `outline:3px` na sessão auditada, até em elemento de teste; a causa é desconhecida. A evidência não homologa implementação geral nem mede todas as rotas/controles. [Registro runtime](../evidence/runtime/public-focus-ring-production-component-sample-2026-10-24.md).


### VIS-002 — origem CSS e mapa de escopo proposto

A fonte pública declara contorno 3 px/offset 3 px; `ui-theme.css` troca a cor clara por `#6E512E` e o controle de tema declara offset 2 px. O About da PR #239 propõe localmente 4 px/offset 3 px. Foi preparado um mapa não canônico por componente e rota, preservando o limite de implementação global atualmente não autorizada. [Mapa de origem e revisão](../evidence/architecture/vis002-focus-ring-source-map-proposal-2026-10-24.md).
