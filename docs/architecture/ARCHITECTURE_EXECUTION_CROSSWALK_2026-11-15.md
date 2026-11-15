# Crosswalk operacional de execução arquitetural — 15/11/2026

**Finalidade.** Este documento amplia o roteiro em uma ponte executável entre decisões ARC-01…ARC-16, fases V0–V6, gates G0–G8, código, evidências, bloqueios e saídas. Complementa, sem substituir, o [contrato arquitetural](../ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md), o [plano diretor histórico](DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md), o [handover corrente](../HANDOVER_CURRENT.md) e os recibos citados.

**Leitura de status.** Decisão aprovada ≠ implementação; código integrado ≠ gate aprovado; PASS de subgate ≠ fechamento da fase; Deploy Preview READY ≠ revisão visual concluída; preview ≠ produção. Os rótulos de progresso e contagens abaixo são snapshots observados em 15/11/2026 BRT. A estimativa de ~30% (faixa 25–35%) é a estimativa datada de 13/11, sem métrica formal e não recalculada.

## Âncoras vivas observadas

| Repositório/ref | SHA observado | Estado relevante |
|---|---|---|
| Product `main` | `46a52e76a0eeae4bed4b567b12da5311ed90b475` | Base atual; inclui PR #273. |
| Product `development` | `1a69ff76a5f36e3245a288773bb409aa662e4e62` | Base de UX-04 e material DS-05A; divergente de `main`. |
| Product #269 | `2e202e4d7d36f29bfb62508bc15f40cdc18f130b` | Draft; base antiga `221b54b…`; `mergeable=false`. |
| Product #271 | `d699fb1911046dfbbc475fad9415f3ff3fca1cc8` | Aberta; base antiga `221b54b…`; revalidar contra `main` atual antes de integrar. |
| Product #274 | `68441080f1ba29f546e6f97926e487a945f7fa2f` | Draft; reconciliação ARC-13 pós-#273; 39 caminhos, sem `app/**`. O compilador e o manifesto agora normalizam CRLF antes dos offsets; 2/2 workflows Actions passam e o Deploy Preview está READY. |
| Product #275 | `49cf98a3600bc13c4131a62775cf881599418bbe` | Draft; 7 caminhos; Preview READY e revisado no SHA atual. 10/11 Actions passam; o gate raster VIS-002C falha no WebKit 390 px (39.542 pixels fora dos limites de texto); sem integração. |
| Design System `main` | `79db735d6f05177b0c406e383d35832f3d72fdef` | Base atual. |
| Design System #119 | `95ad578661154dd95a287bc3e588a901edbd253f` | Draft documental; branch existente; 86 caminhos; a atualização preserva as 2 refs. |

Refs remotas: Produto 6 (gatilho de revisão 5 excedido por uma branch ligada à PR #275); Design System 2 (na meta). Todas as refs de trabalho atuais estão ligadas a PRs abertas. Candidatos remotos à remoção: **zero**. Não excluir worktrees locais sujos ou o commit local do Design System `54d66028…`; a branch local está à frente do rastreamento e não é o head remoto da #119.

## Bloqueios e dependências que determinam a ordem

| ID | Estado comprovado | Consequência e saída exigida |
|---|---|---|
| BLK-01 — ARC-13 owner dispositions | #274 contém 1.021 sinks / 359 fontes JS; hash do inventário `b3739e5ff57005600665cc6c1a04fbe986649b8f8e8e9b80a6fb09b2d3adf178`. Dez sinks alterados/novos continuam `ownerDisposition: pending`; nenhuma chave ou migração runtime foi criada. | Fechar disposição por ID e proveniência antes de criar chaves. Preservar exceções e conteúdo de domínio; lote reversível e sem mudanças de `app/` até a decisão de consumidor. |
| BLK-02 — G2 `/config/` e DS-05A | 98 pares continuam `UNCERTAIN` por `backdrop-filter`; configuração hospedada/fixture e DS-05A permanecem HOLD. O relatório local de desenvolvimento está sujo e é evidência, não baseline. | Não promover a regra candidata `.module-number`. Primeiro atualizar a comparação estática `main@46a52e76` ↔ `development@1a69ff76`, depois preparar baseline/candidato limpos com CSSOM nos dois braços e capturas pareadas. |
| BLK-03 — G1 base antiga | #269 e #271 ainda apontam para `main@221b54b…`, embora Product main esteja em `46a52e76…`. | Recalcular commits e paths contra a base atual, rever conflitos e gates UX-04/NAV-005; não mudar base ou integrar por nome/mergeable isoladamente. |
| BLK-04 — G3 cobertura de runtime | A revisão visual do Preview #275 no SHA atual confirmou o frame enviado como capa, o vídeo 9:16 dentro da tela e controles próprios na faixa livre. A transição aguarda o estado PLAYING do YouTube; a interface Shorts própria ainda aparece durante a reprodução. Estados, teclado real, leitor de tela e demais shells/dispositivos continuam abertos. Um gate raster falha no WebKit 390 px. | Completar por família e risco. Triar o delta do gate sem enfraquecer o escopo de raster; manter G3 parcial até estados de interação e acessibilidade exigidos serem verificados. |
| BLK-05 — G7 autenticação/fixture | Issue #232 e fixture protegida continuam pendentes; acesso anônimo e contexto autenticado são evidências distintas. | Fechar fixture autorizada no SHA e rota exatos; preservar controle de acesso. Não usar sessão herdada como evidência anônima. |
| BLK-06 — ARC-15 inventário de verificações | O histórico cita 19 scripts Node e 2 validadores de assets; nenhum mapa atual de assertions prova sobreposição ou redundância. | Inventariar contrato/assertion/rota/estado antes de reduzir ou acrescentar verificações. Quantidade de scripts sozinha não decide redundância. |

## ARC-01…ARC-16 — decisão, implementação, prova e próxima saída

| ARC | Estado e evidência no pin atual | Próximo lote e condição de saída |
|---|---|---|
| 01 — ownership da implementação | Parcial. A decisão põe componentes no Produto e decisões/provas no Design System; a matriz completa de donos e consumidores ainda não está fechada. | Completar `componente → owner → consumidores → variantes`; cada componente compartilhado tem uma implementação editável. Reverter somente o lote se um consumidor perder seu contrato. |
| 02 — fonte canônica de tokens | Parcial. Exportações/versionamento seletivos existem; integração abrangente está bloqueada por G2/G3/G4. | Selecionar só tokens aprovados em `decisions.json`, pin/hash de saída e consumidores; DoD inclui fallback e rollback por família. |
| 03 — fragmentos no build | Parcial, com integração real: compilador e manifest atendem `/`, `/about/` e `/how-it-works/` em Product main. | Mapear superfícies restantes; cada rota precisa fonte, artefato gerado, verificação de drift e HTML essencial sem depender de JS. Reverter a família de páginas isoladamente. |
| 04 — fidelidade estrita por padrão | Parcial. #273 integrada; #275 segue Draft após refinamento visual/a11y do hero. A capa foi revisada no Preview; não há prova global de todas as rotas/estados, e o gate raster WebKit 390 permanece em falha. | Registrar diff de cada consumidor e estado; mudança deliberada exige aprovação própria. Triar a falha e revisar a regressão visual antes de qualquer integração. |
| 05 — componentes por semântica | Parcial. G3 classifica marca, controles Admin, botões, hotspots, labels e mensagens; estados/variantes de runtime faltam. | Completar contrato e variante por responsabilidade; não unir homônimos. DoD cobre estados e owner em cada shell; rollback só do componente/família afetada. |
| 06 — controladores por componente | Incompleto como programa. Há controladores localizados, sem auditoria ampla de init/event/update/dispose. | Mapear inicialização idempotente e listeners por consumidor; fechar teste/evidência de ciclo de vida antes de reusar. Isolar rollback no módulo. |
| 07 — composição híbrida | Parcial. HTML estático de três páginas e regiões JS dinâmicas coexistem; Configurador/Viewer mantêm renderers próprios. | Declarar por superfície o que nasce no build e o que é dinâmico; DoD preserva renderers, dados e funcionamento sem JS para markup essencial. |
| 08 — tokens semânticos/CSS delimitado | HOLD para extração ampla. G2/G3 e DS-05A não estão concluídos. | Nenhuma consolidação até ownership, cascade, tema e estados medidos. DoD é equivalência por consumidor e payload/cache medidos; rollback por folha/rota. |
| 09 — conteúdo editorial versionado | Parcial. Sem CMS como direção; fronteira UI/editorial/domínio ainda não está completamente classificada. | Completar classificação e catálogo em código versionado; não incluir preço/dados de usuário ou conteúdo comercial em chaves de UI. Rollback por bundle/lote. |
| 10 — estrutura de páginas explícita | Parcial. Fonte HTML e saída são pinadas para três páginas públicas. | Estender apenas onde fragmento é realmente compartilhado; DoD conserva ordem/contexto de navegação e cobertura de drift; reverter a página afetada sem motor universal. |
| 11 — Core comum, projeções próprias | Parcial/não fechado. A direção preserva domínio e apresentação do Configurador/Viewer, sem recibo consolidado de todos os consumidores. | Registrar Core, projeções, consumidores e limites de dados; não migrar schema para obter reuso. Rollback por adaptador/projeção. |
| 12 — autoridade de domínio e aplicação | Parcial. Autorização, validação, persistência e publicação pertencem ao domínio/aplicação; fixture G7 ainda pendente. | Fechar fluxos permitidos/negados e feedback sem alterar permissões ou persistência. Rollback do fluxo, sem mudanças de banco. |
| 13 — inventário e localização abrangentes | Parcial. #274 registra 1.021 sinks / 359 fontes e continuidade pós-#273; dez sinks seguem pendentes, sem catálogo de runtime. | Dispor os dez IDs; fechar cobertura e semântica de chaves; só depois extrair pt-BR em lotes reversíveis. DoD inclui cobertura, fallback e leitura de acessibilidade. |
| 14 — integração DS→Produto versionada | Parcial. Tokens/artefatos seletivos têm pin; a matriz completa de consumidores e rollback ainda falta. | Fixar versão/hash por integração e rastrear folhas/rotas/tema. DoD prova ausência de drift e rollback simples; sem sincronização em produção. |
| 15 — testes proporcionais ao risco | Parcial. Evidências de CSSOM, browser, visual e interação são distintas; não há matriz integral nem conclusão de overlap. | Mapear assertion→risco→rota/estado; manter evidências complementares quando cobrem riscos diferentes. DoD lista lacunas; não reduzir pela contagem de arquivos. |
| 16 — critério de fechamento e duplicações | Incompleto. Não existe fechamento global com owner, benefício, gates e exceções. | Cada lote termina com contrato, consumidores, duplicação real ou exceção, evidência, owner, GO/HOLD e rollback. DoD é reproduzível e ligado a SHA. |

## V0–V6 — estado, dependência e saída

| Fase | Estado | Dependências e condição de saída |
|---|---|---|
| V0 — autoridade e inventários | Parcial | G0/ARC-13: pins atuais, owners, rotas e IDs conciliados; dez sinks pós-#273 dispostos; cobertura lexical delimitada e lacunas nomeadas. |
| V1 — estabilizar e medir | Parcial | G1–G3: bases atuais, defeitos separados de refatoração, baselines por risco e estados; nenhuma evidência antiga apresentada como atual. |
| V2 — tokens/versionamento | Parcial/HOLD | ARC-02/14 + G2–G4: token aprovado, versão/hash, consumidores medidos e rollback demonstrado. |
| V3 — componentes básicos | Parcial inicial | ARC-01/05/06/08 + G3–G5: contratos por semântica, variantes e lifecycle, sem regressão por shell/estado. |
| V4 — composição/localização | Inicial | ARC-03/09/10/13 + G0/G3: fragments só onde compartilhados, pt-BR completo no escopo, conteúdo fixo acessível e fallback. |
| V5 — ferramentas derivadas | Parcial/HOLD | ARC-07/11/12 + G5/G7: projeções e regras existentes preservadas, auth validada; extensão de catálogo só diante de requisito real. |
| V6 — homologação/release | Não iniciado como conclusão | ARC-04/15/16 + G0–G8: gates aplicáveis, evidências, exceções/owners, métricas de duplicação, rollback e readback. Não autoriza produção. |

## G0–G8 — gates e critério de avanço

| Gate | Estado atual | Saída objetiva para avançar |
|---|---|---|
| G0 — governança/evidência | Contínuo; precisa corrigir os snapshots documentais stale. | Uma autoridade por decisão, pin, owner e recibo; datas e limites separados. |
| G1 — navegação/geometria | Parcial. UX-04 passou localmente no SHA de `development`; falta runner Linux/Node 22 e critérios de toque/zoom/Safari/iPad para #218. | Base atual comparada, execução e dispositivos exigidos registrados, divergências classificadas. |
| G2 — conformidade CSS | Em andamento. `/config/`, #208/#216, fixture hospedada, DS-05A e 98 pares `UNCERTAIN` pendentes. | Pares e fundos computados válidos sem ressalvas de composição; visual e CSSOM alinhados, issue por critério fechada. |
| G3 — ownership e contratos | Parcial. Subgates estáticos e baseline de CTAs existem; runtime/interação e shells restantes faltam. | Matriz de ownership completa no escopo e revisão visual/teclado/leitor de tela pelos casos de risco. |
| G4 — foundation/tokens | HOLD. | Primeiro consumidor pequeno passa equivalência, token aprovado e versão/hash rastreável; nenhuma mudança global. |
| G5 — componentes CSS | Parcial na candidata, HOLD na baseline. | Variações semânticas/visuais fechadas e família aprovada; sem compartilhar apenas por nome. |
| G6 — composição | HOLD. | Contratos de build/componentes comprovados por superfície; rollback preserva HTML essencial e domínios. |
| G7 — hardening cross-platform/auth | Pendente, #232/fixture. | Fixture autorizada no head exato; fluxos de acesso e estados de erro documentados sem ampliar acesso. |
| G8 — aceitação/release | Não iniciado. | Aprovação, gates e readback separados; produção requer autorização explícita própria. |

## Ordem operacional recomendada

1. Manter este crosswalk e o handover sincronizados com os SHAs observados; tratar snapshots anteriores como história.
2. Reconciliar as bases antigas de #269/#271 contra Product main atual; não fazer rebase/merge por inferência.
3. Fechar o lote ARC-13 em #274 por ID e owner; manter texto, chave, origem e conteúdo de domínio distintos.
4. Atualizar a comparação de provenance entre Product main e development: o merge-base é `221b54b…`, a comparação está divergente (434 commits à frente / 2 atrás) e as diferenças CSS atuais abrangem `how-it-works.css`, `landing.css`, `styles.css` e `ui-theme.css`. O crosswalk antigo de `2babbeb → 1a69ff76` é histórico.
5. Só então preparar o subgate DS-05A em checkout descartável limpo; preservar a árvore local suja. O runner precisa registrar CSSOM dos braços baseline e candidato com mesmas versões e fixture, além de capturas pareadas.
6. Avançar G2/G3 por consumidor e risco; não extrair CSS/tokens enquanto os gates de proveniência, ownership e contraste estiverem HOLD.
7. Não reduzir nem acrescentar lotes de testes antes do mapa de assertions e riscos; a atualização documental não executa uma suíte.
8. Não remover refs: há zero candidatos remotos seguros. Rever o ponto de crescimento do Product depois que PRs ativas tiverem destino; soft cap não é regra de exclusão.

## Critério de conclusão do programa

ARC-01…ARC-16 implementados conforme contrato, todos os consumidores no escopo cobertos ou com exceção aprovada e owner; V0–V6 concluídos; G0–G8 com PASS/HOLD/fora de escopo justificado em pins exatos; equivalência/benefício demonstrados por lote; localização e fallback fechados; duplicações reais removidas ou justificadas; rollback e readback registrados. Nenhum item isolado, PR merged, preview, porcentagem estimada ou contagem de testes satisfaz por si só esse critério. Produção continua fora da autorização vigente.

## Regras de atualização

Revalidar branches/PRs e o SHA de Product/Design System antes de cada ação remota. Atualizar o status e as referências neste arquivo somente com prova nova; não apagar snapshots históricos. Para cada novo lote, registrar entrada, output esperado, pin, owner, riscos, resultado, limitações e rollback. Registrar método e limites de validação por lote; cada gate avança somente com as evidências que seu contrato exige.
## Comparação atual de CSS entre Product main e development

A comparação foi refeita em pins completos: Product `main@46a52e76a0eeae4bed4b567b12da5311ed90b475` contra `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`. O merge-base é `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; os refs divergem em 434 commits à frente e 2 atrás. O diff completo tem 300 caminhos, dos quais 13 são `.css`; somente quatro estão em `app/**`, os demais pertencem a fixtures/evidências/documentação.

| Folha de runtime | Blob main | Blob development | Diferenças relevantes observadas |
|---|---|---|---|
| `app/how-it-works/how-it-works.css` | `e70439be98b0fc7a705fd541f62e4844f6323472` | `0dff501eb14df78081f35d81ae1eca17abca85ba` | Main mantém o player com `min-width:200px`, link explícito ao YouTube e botão próprio de tela cheia; development tem embed simplificado de 290px e largura mobile `65vw`, além de regra estreita para até 290px. |
| `app/landing/landing.css` | `8df2c39d1993a6e6b4da8bb4dcd2289c7f50eb79` | `3e307c155a406f91337b2e54534e0362d2c21636` | Main contém o scale de `.hero-image-frame` (`.88`, `.84`, `.80`) e overlay/controles de vídeo; development não escala o frame e não contém esse overlay, mas tem regras responsivas próprias para o cabeçalho público. O scale em `main@46a52e76` corresponde à margem bege do screenshot. No head #275 `49cf98a3`, a arte expandida preenche o frame, usa a imagem enviada como poster estático e mantém o vídeo em 9:16; a faixa própria de reproduzir/pausar e tela cheia fica fora do iframe. O poster cruza para o player após `PLAYING` com 240 ms, respeitando movimento reduzido. Elementos do YouTube Shorts ainda aparecem durante a reprodução e não são estilizados pela página. |
| `app/styles.css` | `d43e6fb5e66133d2389b5c39b165b76b13cfa868` | `d1ac2b5701f215de56ff8f7c12b1d5e7dcbe47a8` | Um valor de cor literal em `main` passa a `var(--muted)` em development. Reidentificar seletor e contexto antes de inferir equivalência de contraste. |
| `app/ui-theme.css` | `3114bbfe0a67cbdc53757f5f50a0d035559767a6` | `36137b4264aa5b12999b286284cda227923a606a` | Development muda os seletores do toggle para distinguir header público/privado e usa `--ui-theme-focus` nos dois temas; `main` mantém seletores genéricos e cores de foco literais. O patch candidato `.module-number` segue apenas no checkout local modificado, não está nesses dois blobs remotos. |

**Decisão do gate.** Não tratar `main` e `development` como snapshots CSS equivalentes e não aplicar o relatório antigo `2babbeb → 1a69ff76` como comparação corrente. O subgate `.module-number` ainda pode ser delimitado somente a `development`, mas o gate geral DS-05A precisa dizer isso explicitamente e piná-lo; sua prova candidata deve registrar CSSOM e captura de ambos os braços. A PR #275 tem Preview READY no SHA `49cf98a3600bc13c4131a62775cf881599418bbe` e foi revisada visualmente. Dez de 11 Actions passam; o gate `VIS-002C P-TOKEN v0.3` falha no WebKit 390 com 39.542 pixels alterados fora dos limites autorizados. O preview e a revisão visual não sobrepõem esse gate pendente.

**Limite desta comparação:** são diferenças de fonte e blob entre dois commits, não uma prova de CSSOM, contraste, interação ou equivalência visual. Não houve alteração nesses refs nem execução de testes nesta atualização.