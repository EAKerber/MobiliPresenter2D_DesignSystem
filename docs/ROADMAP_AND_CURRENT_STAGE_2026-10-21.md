# Plano geral e etapa atual do Design System — 2026-10-21

## Issue #205 — comparação temporária de cartões do Viewer (25/10/2026)

A comparação lado a lado em Production mostrou que a superfície candidata `#F0EDE8` remove o branco puro e harmoniza melhor os três cartões com o contexto claro, mantendo `#514A43` em contraste de 7,46:1. O tema escuro já computa cartão `#20211F` e texto `#F4F1EB` (14,34:1). A evidência é uma simulação DOM transitória, sem alteração de produto: [método, medições e limites](../evidence/runtime/issue205-viewer-detail-card-surface-ab-2026-10-25.md). #205 continua backlog e sem implementação autorizada; foco, zoom, matriz completa e o overflow de 320 px permanecem pendentes.


## Issue #208 — reconciliação DS-04 com `main` (25/10/2026)

Recomparei os 16 achados à base atual do produto `main@5ccb2a8`. DS04-01, 03–05, 07–09 já têm suporte de tema claro no código atual; DS04-11 está delimitado como exceção técnica, com validação visual parcial. Permanecem riscos em DS04-02 (P1), DS04-06 (P1), DS04-10 (P2) e DS04-12 (P3). A rota pública `/access/` respondeu em claro/escuro; `/access/manage.html` redirecionou a login sem sessão, então o CTA de gestão segue sem readback runtime. Uma simulação DOM separada comparou texto atual branco (1,62:1) e `#20211F` (10,01:1), sem constituir decisão canônica. [Reconciliação fonte/runtime e contrastes](../evidence/architecture/issue208-ds04-main-source-reconciliation-2026-10-25.md). Issue #208 continua aberta; nenhum produto ou Production foi alterado.

## Issue #224 — seleção durante scroll real no preview da PR #243 (25/10/2026)

Repeti o cenário com seleção de Lavanderia após 100 ms de animação e confirmei que scrollLeft estava efetivamente em movimento antes do clique, a 320/390 px e em claro/escuro (quatro combinações). A seleção e a página 2 permaneceram sincronizadas; o cartão terminou inteiramente dentro da janela e sem overflow do documento. [Método e medições](../evidence/runtime/pr243-issue224-carousel-in-motion-recheck-2026-10-25.md). A evidência confirma apenas o preview; issue #224 e PR #243 continuam abertas/DRAFT até revisão, integração e readback em Production.


## VIS-002C — complemento de tema escuro em mobile no preview #241 (25/10/2026)

Em 390×844 px, tema escuro, revalidei no preview da PR #241 os dez seletores de texto longo nas rotas Landing, About e Como funciona. Todos computaram #C4BCB2 com tema escuro ativo; cada rota manteve clientWidth=scrollWidth=390. Isso completa a leitura DOM/CSSOM clara e escura em desktop e mobile para os dez seletores; não mede contraste pixel a pixel nem amplia a homologação além das superfícies listadas. [Evidência](../evidence/runtime/vis002c-v03-preview-10-contexts-manual-review-2026-10-25.md).


## NAV-005 — rechecagem pública do cabeçalho privado no preview (25/10/2026)

Na PR de produto [#244](https://github.com/EAKerber/MobiliPresenter2D/pull/244), em contexto isolado sem sessão, revalidei /admin.html e /access/ em claro/escuro a 291, 320, 321 e 288 px. Em 291 px, nome completo, menu à direita e alvos de 44×44 px cabem sem overflow; em 288 px as ações passam à segunda linha, como aprovado. O rótulo “Auto” aparece em 321 px e fica icon-only em 320 px. No Admin, logo mede 74,5 px a 291 px (29,1% menor que a referência de 105 px). A rota /config/ redirecionou para acesso inválido sem sessão; portanto, Configurador e gestão de acesso autenticados continuam sem evidência runtime. PR #244 permanece DRAFT, sem merge/Production. [Evidência](../evidence/runtime/nav005-pr244-public-header-preview-recheck-2026-10-25.md).


## VIS-002 — rechecagem das keylines de foco do Viewer em preview (25/10/2026)

A PR de produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242), head `c2659513c22d886bc4de63074a66ed9228524c0f`, mantém o anel aprovado (4 px, offset declarado 3 px; `#8B6A40` claro / `#D8BC7C` escuro) e testa `box-shadow: 0 0 0 2px #000, 0 0 0 3px #fff` somente em `.scene-hotspot:focus-visible`. Na rechecagem do preview atual, sete hotspots aceitaram foco em claro/escuro e 390×844/1280×800; sem overflow, folga mínima 0,11 CSS px no mobile e 6,29 px no desktop. Sete checks passaram.

A captura composta no tema escuro mediu 7,05:1 no mínimo amostrado da faixa escura do hotspot 01 sobre área clara, mas 2,04:1 no mínimo do hotspot 02 sobre área escura da foto (P10 3,00:1). Portanto a linha dupla não comprova contraste mínimo em todo o contorno; a faixa branca também não teve margem confiável em todos os pontos amostrados. A PR permanece DRAFT e sem merge/Production. [Evidência atualizada](../evidence/runtime/pr242-viewer-hotspot-focus-keylines-preview-2026-10-25.md).

O site isolado associado ao PR carrega o Viewer, mas `GET /api/public-modules` e a rota primária do site retornam 503 `public_modules_unavailable`. A função lê um snapshot publicado no Netlify Blobs e falha fechada se ele estiver ausente/inválido ou se a leitura falhar; isso sugere um problema de snapshot/Blobs, não das variáveis `DATABASE_URL` ou `ACCESS_GATE_SECRET`, que essa função não usa. A causa exata não aparece nos logs. O preview principal retorna 200 e foi suficiente para a validação visual.

## ARC-13 — auditoria cruzada das propostas (25/10/2026)

A auditoria independente comparou 30 lotes documentais com o índice fixado: 517 registros, 507 chaves distintas e quatro reaproveitamentos preexistentes já documentados como intencionais. Não houve colisão não documentada. Uma divergência de rótulo de consumer para o mesmo sink de revisão foi padronizada nos dois lotes. Todas as chaves permanecem candidatas; índice, catálogo, produto e `decisions.json` não foram alterados. [Método, resultado e limites](../evidence/architecture/arc13-semantic-key-proposal-cross-batch-audit-2026-10-25.md).



## Atualização ARC-13 — convenção aprovada (25/10/2026)

O usuário aprovou a convenção operacional de chaves semânticas: preservar namespace de domínio, usar sufixo camelCase estável, tratar valores dinâmicos como parâmetros e compartilhar chaves somente com owner, consumer e contrato de parâmetros coincidentes. A aprovação encerra a revisão da convenção; não aprova automaticamente chaves individuais, ownership, alteração do índice ou migração do produto.

A amostra de 13 substituições numéricas e cinco rótulos administrativos segue auditada como candidata, com proveniência única e sem colisões no índice observado. Próximos passos ARC-13: revisar contexto/owner/consumer e parâmetros da amostra; preparar lotes para as 199 chaves numéricas restantes, as 364 ocorrências sem proposta e os 190 itens de conteúdo deferidos. Nenhum índice ou código de produto foi migrado nesta etapa. decisions.json continua inalterado.


## ARC-13 — reconciliação da fila sem chave (25/10/2026)

Dos 364 candidatos sem chave e com classificação de interface, 19 literais são valores técnicos de DOM/CSS/enum e quatro mensagens são diagnósticos internos que só chegam a debug e console. Restam **341 textos para revisão de consumer/owner/contrato**: 208 no Admin e 133 no Configurador. Índice intacto; exclusões apenas documentais.

O mapa anterior foi substituído porque podia carregar a função anterior através de listeners. O [mapa corrigido de escopos](../evidence/architecture/arc13-unkeyed-consumer-scope-map-2026-10-25.json) traz ocorrências, fontes e limites: escopo léxico direciona a leitura, mas não prova renderização ou equivalência de contrato. Próxima revisão: confirmar buckets, rastrear constantes de topo aos call sites e classificar consumers reais antes de propor chaves. Sem migração do índice ou produto.

## Atualização pós-consolidação CI-BASELINE-01 — 25/10/2026

- As alterações estáveis que estavam distribuídas entre as PRs de produto #238 e #245 foram consolidadas na PR [#238](https://github.com/EAKerber/MobiliPresenter2D/pull/238), head `1fccf635078aee68aa735caf0df02fdb62402c93`. A PR #245 foi encerrada sem merge como supersedida; seu trabalho está preservado no commit de merge da #238.
- A causa de fragmentação era a trava de fixture que bloqueava qualquer alteração em `app/app.js` e `app/styles.css`. A trava foi ajustada para autorizar somente esses dois arquivos validados e o workflow Stone; o gatilho de CI também cobre esses caminhos. A guarda passou no head consolidado.
- No head consolidado, passaram as cinco suítes autenticadas em Deploy Preview — Mobile/PiP, Keyboard, Flow, Summary/Pricing e Stone — além de grant, papel restrito, revogação e replay negado; build, assets, variantes, gate anônimo e checks de fixture também passaram. Os Deploy Previews principal e isolado estão READY. [Actions #40218470993](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40218470993).
- A PR #238 continua DRAFT e a issue #232 aberta para revisão e integração. Supabase Preview foi skipped porque a validação usa o banco interno de teste autorizado. Nada foi integrado à main nem publicado em Production.
- Naquele checkpoint, a estimativa geral era **~24% (faixa 22–26%)**; após fechar a issue #226, a matriz ponderada abaixo foi atualizada para **25,3 p.p. (~25%, faixa 23–27%)**. A prontidão das PRs continua sem equivaler a integração em `main`. O código integrado permanece estimado em ~18% (15–20%).

### Readiness da PR #238 e auditoria read-only da role — 25/10/2026

- A PR #238 segue DRAFT e mergeable, base `main@5ccb2a8`, head `1fccf635078aee68aa735caf0df02fdb62402c93`; nenhuma review humana ou thread de revisão foi registrada.
- Os nove workflows de PR associados ao head atual concluíram SUCCESS. As cinco suítes Keyboard, Flow, Mobile/PiP, Summary/Pricing e Stone foram executadas na prévia protegida com a fixture V5 sintética publicada pelo plugin restrito aos Deploy Previews #238/#245; o gate autenticado separado verifica grant, bootstrap, negação de Admin, revogação e replay.
- Auditoria somente leitura no Supabase de teste: `access_ci_fixture` está sem atributos elevados e sem memberships que lhe concedam outras roles; não tem SELECT/INSERT/UPDATE/DELETE nas tabelas `access_control`; `PUBLIC` não tem EXECUTE nas funções fixture, e a role só recebeu EXECUTE nas duas funções dedicadas. Nenhuma escrita foi feita nessa consulta.
- Próximo gate: review humana da PR #238, resolver comentários se houver e, depois, autorização de integração. Não há falha de variável identificada no gate atual.

### Prontidão das PRs de produto — readback de 25/10/2026

| PR | Estado atual | Evidência no head | Bloqueio restante |
|---|---|---|---|
| #238 / issue #232 | DRAFT, mergeable; sem reviews ou threads | Nove workflows SUCCESS; cinco suítes protegidas com V5 sintética; gate de grant/revogação e auditoria read-only de privilégios do banco interno. | Review humana e autorização de integração; depois revalidar em `main`. |
| #241 / VIS-002C e fallback | DRAFT, mergeable; sem reviews ou threads | Nove workflows SUCCESS; preview confirmou dez contextos de texto medidos e fallback 3:2 com HTTP 404 real. | Revisão humana do preview; o fallback só cobre a ilustração principal e não homologa outras rotas/assets. |
| #242 / hotspot focus | DRAFT, mergeable; sem reviews ou threads | Sete checks SUCCESS; foco 7/7 em claro/escuro e mobile/desktop; pixel sample 7,05:1 em área clara e 2,04:1 em segmento escuro; site isolado retorna 503 em `/api/public-modules`. | Revisão humana; contraste composto ainda não demonstra 3:1 em todo o contorno. Investigar snapshot/Blobs do site isolado separadamente. |
| #243 / issue #224 | DRAFT, mergeable; sem reviews ou threads | Sete workflows SUCCESS; seleção de Lavanderia preservada no grupo 2 em 320/390 px, temas claro/escuro, inclusive durante scroll suave. | Review humana e integração autorizada; manter #224 aberta até readback após integração. |
| #244 / NAV-005 | DRAFT, mergeable; sem reviews ou threads | Oito workflows SUCCESS; preview confirmou uma linha a 291/320 px e quebra abaixo de 291 px em Admin/acesso. | Runtime autenticado em Configurador e gestão de acesso não foi verificado; review de preview antes de integração. |

Os checks são evidência de branch e não equivalem a aceite final. Nenhuma dessas PRs foi marcada pronta, integrada ou publicada por este readback.

### Pendências e pesos atuais

| Prioridade | Peso do plano | Trabalho ainda necessário | Bloqueio ou critério de saída |
|---|---:|---|---|
| Alta | Dentro de implementação (25%) | Revisão humana da PR consolidada #238 e integração aprovada; depois revalidar o gate em main e fechar #232. | #238 está DRAFT; sem merge nem Production nesta etapa. |
| Alta | Dentro de evidência (30%) | Ampliar a matriz runtime por componente e estados; o zoom real da issue #226 foi confirmado manualmente e a issue foi encerrada. | A confirmação manual não produziu readback automatizado de viewport; rotas privadas ainda exigem sessão autorizada. |
| Alta | Dentro de decisões (20%) | Revisar o foco do Viewer sobre fotografia. A medição da única cena publicada ficou baixa no tema escuro; preparei a proposta de keylines neutras A para manter o anel dourado aprovado e testar um segundo preview. O fallback da ilustração principal foi validado na #241. | A proposta é não canônica; ainda exige escolha explícita antes de alterar o preview. A evidência cobre somente a cena Cozinha; fallback limitado à ilustração principal, sem homologação global. |
| Média | Dentro de evidência (30%) | Ampliar mapa por componente de foco, seleção, carregamento/erro, movimento e tema, incluindo estados e rotas que permanecem não verificados. | Rotas privadas exigem sessão autorizada; não extrapolar medições pontuais. |
| Média | ARC-13 (15%) | Revisar 190 itens de conteúdo deferidos; preparar 199 chaves numéricas restantes (132 templates) em sete módulos; depois revisar 364 textos sem chave (209 em `admin.js`, 155 em `app.js`); aplicar a convenção aprovada e revisar ownership em lotes. | A convenção foi aprovada; oito casos de plural/lista seguem adiados para localização e cinco textos de catálogo/editorial aguardam revisão do owner. A fila está dimensionada por módulo; a amostra 13+5 foi verificada sem colisões. |
| Futura | Etapas seguintes (10%) | Schema de UI, dados de textos/localização e inventário JS, mantendo separados dados de interface e dados do Configurador. | Só começa depois da fundação visual e ARC-13. |


## Registro anterior à consolidação — CI-BASELINE-01 / DS-05A (25/10/2026)

- Produto PR [#245](https://github.com/EAKerber/MobiliPresenter2D/pull/245), head `c41c33e798888f62505e2c7ba8bc3122061975b7`, passou o gate autenticado [Actions #40213836389](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40213836389): fixture verificada, resgate, papel restrito, revogação, replay negado e redirecionamento após revogação.
- As cinco suítes no Deploy Preview passaram: Mobile/PiP, Keyboard, Flow, Summary/Pricing e Stone. Build, assets, variantes e os cinco testes locais de navegador também passaram no mesmo head.
- Deploy Preview #245 está READY no mesmo commit, branch `fix/config-stage-nav-grid-track-20261025`. O conserto evita a perda de geometria da navegação após a troca de perfil responsivo; não foi publicado em Production.
- A correção permanece em PR DRAFT. O PR #245 usa o alias `ci-auth-base-20261025` em `fd61a37...`, exatamente o mesmo commit do head do PR #238, para manter o preview e os checks de runtime isolados do PR de infraestrutura.
- Uma tentativa de avançar a branch #238 com os arquivos de runtime foi rejeitada pelo gate `isolated-fixture-contract`, que permite somente os arquivos de fixture e CI e rejeita `app/app.js` e `app/styles.css` [Actions #40214217098](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40214217098). A branch #238 foi restaurada ao head `fd61a37...`; a proteção não foi relaxada e nenhum código foi perdido, pois o head validado permanece no PR #245.
- Os logs do gate #238 em `fd61a37` identificam `PLAYWRIGHT_TIMEOUT` somente em Keyboard e Flow; Mobile/PiP, Summary/Pricing e Stone, fixture, grant e revogação passaram. O ajuste de navegação em PR #245 passou as cinco suítes autenticadas em `c4d55b7` [Actions #40214596691](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40214596691). A separação fica justificada pelo contrato de fixture e pelo estado distinto dos checks.
- A Issue [#232](https://github.com/EAKerber/MobiliPresenter2D/issues/232) permanece aberta até revisão e integração. Supabase Preview segue skipped por ausência de branch Supabase associada; foi usado o banco interno já existente, sem criar projeto/branch adicional.
- Próximo passo registrado naquela data: revisão separada das PRs #238 e #245. Essa recomendação foi supersedida pela consolidação acima; a decisão atual é revisar a PR #238 consolidada, ainda DRAFT.
- Atualização do head #245 (`dbfbd9a7bca0e9f581e5d8ac4a765e01829d6ce9`): o diff desde `c4d55b7` contém somente `.github/workflows/stone-browser.yml`. O Deploy Preview está READY no SHA atual e todos os checks acionados neste head passaram. Stone concluiu em 54 s: cache criado, instalação do Chromium/dependências em 26 s e teste funcional em 8 s; o cancelamento anterior foi causado pelo limite de 10 min durante o download do Chrome Headless Shell. O gate autenticado no head `c4d55b7` já havia passado as cinco suítes, incluindo grant/revoke/replay. Runtime unchanged from `c41c33e`; sem merge/Production.



## Issue #226 — matriz atual em Production (25/10/2026)

- Complemento em contexto Chromium isolado: nos viewports CSS emulados 683×768 (~200%) e 341×768 (~400%), o scroll width igualou a largura útil; as grades ficaram em uma coluna e os irmãos fechados mantiveram suas alturas após abertura. É uma verificação de largura efetiva, não zoom real (visualViewport.scale=1); capturas antes/depois das duas grades estão arquivadas em 1366×768 nos temas claro e escuro; o zoom real foi confirmado manualmente e a paridade WebKit foi concluída no gate reproduzível. [Matriz atualizada](../evidence/runtime/issue226-current-production-matrix-2026-10-25.md).

A rechecagem após reload confirmou, nas duas grades `.foundation-list` e `.study-topics`, que um item aberto cresce sem esticar irmãos fechados nos viewports 1366 × 768, 768 × 1024 e 390 × 844, em tema claro/escuro. Enter e Espaço preservam o toggle nativo; duas aberturas sequenciais são independentes; o fechamento restaura a geometria sem overflow. A regra `align-items:start` está ativa nas duas grades em Production. [Matriz e limites](../evidence/runtime/issue226-current-production-matrix-2026-10-25.md).

A issue #226 foi encerrada após confirmação manual do usuário em zoom real de 400% na rota `/how-it-works/`. O gate passou 8/8 combinações funcionais em Chromium/WebKit, em 390/1366 px e temas claro/escuro; a divergência anterior era da captura e foi resolvida com recorte pelas coordenadas dos elementos. A automação não leu o zoom manual e não fornece métrica automatizada de viewport a 400%. Ver [confirmação manual e limites](../evidence/runtime/issue226-real-zoom-user-confirmation-2026-10-25.md).

## Plano ponderado de conclusão — avaliação provisória (25/10/2026)

Os pesos abaixo são uma ferramenta de planejamento, não metas ou decisões canônicas. A estimativa mede a conclusão do plano inteiro; mudanças em preview aumentam a evidência e a prontidão, mas não contam como integração.

| Frente | Peso | Conclusão estimada | Contribuição | O que falta para fechar |
|---|---:|---:|---:|---|
| Inventário e evidência runtime | 30% | 38% | 11,4 p.p. | A #226 foi encerrada após confirmação manual de zoom real; falta ampliar cobertura por famílias/estados, mantendo áreas autenticadas não verificadas além do escopo autorizado. O gate WebKit tem paridade 4/4 por navegador e capturas desktop claro/escuro arquivadas. |
| Decisões e homologação visual | 20% | 22% | 4,4 p.p. | Fallback escopado aprovado e validado; ainda revisar foco sobre imagens/superfícies e decisões pendentes. |
| Implementação por componente e integração | 25% | 20% | 5 p.p. | Revisar e integrar previews aprovados, revalidar em Production e resolver conflitos/branches sobrepostos. O código atual integrado segue estimado em 18% (faixa 15–20%). |
| ARC-13: ownership e chaves semânticas | 15% | 30% | 4,5 p.p. | Classificar os 190 itens de conteúdo deferidos, resolver 369 textos sem chave e 212 chaves baseadas em linha; aplicar a convenção aprovada, revisar owners e migrar em lotes revisáveis. |
| Etapas futuras: schema de UI, textos/localização e inventário JS | 10% | 0% | 0 p.p. | Começam depois da fundação visual/etapa atual; preservar Português do Brasil e separar dados de interface dos dados do configurador. |
| **Total ponderado** | **100%** |  | **25,3 p.p.** | **Estimativa geral arredondada: ~25% (faixa 23–27%).** |

### Ordem de trabalho recomendada

1. Revisar a PR consolidada #238 e a PR de produto #241 após leitura humana; integrar somente com autorização para merge, revalidar em main e então fechar #232. PR #245 e a branch v0.2 #240 foram encerradas como supersedidas; a #241 contém os oito seletores da v0.2 mais dois contextos medidos na distribuição v0.3. Nenhum merge ou deploy em Production foi feito.
2. Ampliar a evidência runtime de foco, seleção, carregamento/erro, movimento e temas por componente. A #226 foi encerrada após confirmação manual do zoom real; não há readback automatizado a 400%, e a paridade WebKit automatizada foi resolvida.
3. Continuar o mapa por componente para foco, seleção, carregamento/erro, movimento e temas. O fallback da ilustração principal de estudo de espaço foi implementado na PR #241 e validado com HTTP 404 real no preview; ampliar a cobertura para outras imagens/rotas exige evidência própria.
4. Avançar ARC-13 em lotes de ownership/chaves após revisão da convenção, sem substituição em massa de strings.
5. Só então iniciar schema de UI, localização e inventário funcional de JavaScript, conforme sequência do plano.

**Impedimentos atuais:** PRs de produto seguem DRAFT e aguardam revisão humana antes de qualquer integração; rotas privadas exigem sessão autorizada; foco sobre fotografias/superfícies variadas ainda precisa de revisão. A issue #226 está encerrada com confirmação manual, sem medição automatizada de viewport a 400%. O fallback aprovado da ilustração principal foi validado em preview com HTTP 404 real. Não há falha confirmada de variável no gate autenticado.

## VIS-002C v0.3 — revisão dos dez contextos concluída (25/10/2026)

- PR Design System [#52](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/52) distribui `#292723` nos dez contextos de texto longo medidos em tema claro. A preferência do usuário por quase preto também atualiza os três consumidores previamente preservados na v0.2, já mapeados como pares runtime aprovados. `decisions.json`, tema escuro, eyebrows, assinaturas e seletores globais permanecem inalterados.
- O contraste calculado é 12,77:1 sobre `#F0EDE8` e 11,68:1 sobre `#E8E3DC`. O gate do Design System passou no head `2f11ecf8948c779706a0ce0795e088d29633fb7e`, Actions [#40203905477](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40203905477).
- Produto PR [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241), head `f102c3037e2f64ebb904643bbc076064322f1672`: oito workflows SUCCESS e os Deploy Previews principal e isolado READY.
- A revisão DOM/CSSOM confirmou os dez seletores em Landing, Quem somos e Como funciona: `#292723` em claro; `#C4BCB2` sobre `#20211F` em escuro. Em 390 × 844 px, as três rotas tiveram `scrollWidth` de 390 px; em 1280 × 720 px, `scrollWidth` igualou a largura útil de 1265 px, sem overflow. Eyebrows, assinaturas e tokens globais permaneceram fora da regra.
- Evidência: [revisão manual do preview em dez contextos](../evidence/runtime/vis002c-v03-preview-10-contexts-manual-review-2026-10-25.md). A conferência cobre DOM/CSSOM e uma captura de preview; não é homologação global.
- PRs #241 e #52 permanecem DRAFT. A PR de produto #240 foi fechada como supersedida: seu mapeamento v0.2 dos oito seletores foi substituído na #241 pela distribuição v0.3, que mantém esses oito contextos e acrescenta dois medidos. Não há integração separada da #240; nenhuma PR foi mergeada nem publicada em Production.


## VIS-002 — contraste de foco nos hotspots do Viewer (25/10/2026)

- A PR de produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242), head `af2166df42019b273c27d672149ebe49b143c0fb`, usa o anel aprovado de 4 px/offset 3 px nos sete hotspots.
- Rechecagem por teclado no preview, em mobile 390 × 844 e tema escuro: os sete hotspots receberam `:focus-visible`, `#D8BC7C`, largura 4 px e offset 3 px; todos ficaram dentro da cena, sem overflow. O hotspot 01 manteve sua seleção enquanto o foco percorreu 01–07.
- O branch publica somente a cena da Cozinha. A distinção do anel sobre a fotografia segue como limite: a amostra aproximada anterior mediu medianas de 1,24–1,46:1 no escuro. A nova leitura confirma renderização/posicionamento, não suficiência de contraste nem generalização a outras cenas.
- [Rechecagem por teclado](../evidence/runtime/pr242-viewer-hotspot-focus-preview-keyboard-recheck-2026-10-25.md) · [amostra anterior de contraste](../evidence/runtime/pr242-viewer-focus-image-contrast-sample-2026-10-25.md). Sem mudança de CSS ou decisão. PR #242 permanece DRAFT; sem merge/Production.


## Registro histórico supersedido — revisão inicial do preview VIS-002C v0.3 (head `baef9acd`)

- Naquele ponto, a PR de produto [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241) cobria sete seletores e deixava três consumidores previamente mapeados na distribuição v0.2 com `#705C4B`. Esta leitura correspondia à head e ao escopo então vigentes; não descreve a implementação atual.
- Em 25/10, a preferência do usuário por quase preto em texto corrido levou à reconciliação dos dez contextos medidos na v0.3. O estado atual está no primeiro bloco deste roadmap e na [revisão dos dez contextos](../evidence/runtime/vis002c-v03-preview-10-contexts-manual-review-2026-10-25.md).
- Evidência histórica: [revisão manual do preview da head `baef9acd`](../evidence/runtime/pr241-vis002-v03-preview-manual-review-2026-10-25.md).


## CI-BASELINE-01 / DS-05A — causa do timeout e estado atual (25/10/2026)

- O diagnóstico de #238 identificou a perda de geometria dos botões da navegação: nós existentes ficavam em 0×0 após a troca do perfil responsivo; reinserir o mesmo nó restaurava 44 px. A configuração do Supabase/Netlify não era a causa.
- A correção de runtime foi isolada na PR #245: flex sizing para a navegação, criação em fragmento e reinserção da barra após mudança de perfil, preservando o foco. O gate autenticado em c4d55b7 passou as cinco suítes e os cenários de grant, papel restrito, revoke, replay negado e redirecionamento.
- No head atual #245 dbfbd9a7, o Deploy Preview está READY e todos os checks acionados nesse head passaram. O gate autenticado não foi reexecutado nesse último head porque só mudou o workflow Stone; seu resultado mais recente segue no c4d55b7. A correção de runtime não mudou desde o head autenticado.
- A causa do timeout de Stone também foi removida: o limite de 10 min expirava durante o download do Chromium. Com cache, instalação separada e timeout de 20 min, Stone concluiu em 54 s.
- #238 permanece DRAFT no head fd61a37 e ainda tem o resultado antigo de Keyboard/Flow em timeout, pois sua branch de preview não contém a correção de runtime. Sua trava isolated-fixture-contract rejeita alterações de app/app.js e app/styles.css para manter a extração de CI/fixture limitada ao escopo aprovado.
- As branches não foram fundidas: #238 contém a infraestrutura e o contrato da fixture; #245 contém a correção funcional, depende dessa base para o preview autenticado e adiciona o suporte de fixture ao seu Deploy Preview. Unificá-las agora exigiria alterar a trava e reexecutar a validação do escopo combinado; o ganho de reduzir uma branch não compensa enfraquecer esse limite antes da revisão. Ambas continuam DRAFT, sem merge ou Production.
- Issue #232 permanece aberta até revisão e integração. Supabase Preview segue skipped por falta de branch associada; o banco interno de teste existente foi usado, sem criar outro projeto/branch.

**Próximo passo técnico:** revisão humana do par de PRs e, depois da decisão sobre a infraestrutura, atualizar a base do trabalho funcional para a integração adequada. Não há variável faltando confirmada.
### Rechecagem visual em Production — imagens com `alt=""` (25/10/2026)

- Os oito casos de `alt=""` em `/how-it-works/` foram revisados em DOM e pixels: ícone WhatsApp, ilustração de móveis prontos, logo repetido pelo título e cinco ilustrações das etapas. Os sete itens visuais têm categoria/nome e contexto textual adjacente; o ícone de WhatsApp está oculto da árvore acessível e o link tem nome acessível próprio. A observação sustenta manter `alt=""` nos oito contextos.
- Evidência: [revisão das imagens com alt vazio](../evidence/runtime/how-it-works-step-illustrations-visual-review-2026-10-25.md). Mudança documental somente; nenhum `alt`, CSS ou código do produto foi alterado. O restante do item 2 — verificações de teclado, movimento reduzido e falha de imagem em outros contextos — segue parcial.
- Complemento de erro de imagem em 341×768: Landing 5/5 e Viewer 2/2 imagens com `alt` descritivo preservaram as caixas; em Como funciona, 19/20 preservaram. O único colapso foi a ilustração principal de estudo de espaço (−149,7 px); o mesmo arquivo no cartão compacto manteve sua caixa. Na PR #241, um HTTP 404 real same-origin no preview acionou o placeholder 3:2 em 341×768, sem overflow, mantendo legenda e descrição acessível. A correção segue DRAFT; outros assets, alt vazio, outras cenas do Viewer e leitores de tela continuam sem cobertura. [Evidência e limites da varredura inicial](../evidence/runtime/public-image-failure-runtime-production-2026-10-25.md).


---

## Revalidação de execução — 24/10/2026

- O inventário visual foi regenerado em `visual-inventory.json` a partir de todos os oito HTML e oito CSS do produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; a atualização mantém o escopo estático e não certifica o DOM/runtime.
- As oito rotas do inventário agora têm matriz de evidência runtime ou lacuna explícita em [cobertura de inventário](../evidence/architecture/runtime-inventory-coverage-2026-10-24.md). Isso classifica cobertura; não fecha a auditoria de todas as regras/famílias.
- Permanecem parciais os estados dinâmicos do Configurador e as rotas autenticadas. NAV-005 teve implementação autorizada nesta conversa e validada no preview da PR de produto #244; `decisions.json` permanece inalterado e a PR segue DRAFT. Foco/contraste local também depende de escopo próprio. A issue #224 tem correção limitada na PR #243, validada em preview, ainda DRAFT e não integrada.
- NAV-005 foi rechecado em `/admin.html` na Production, sem sessão, nos temas claro/escuro e em nove larguras (288–360 px): o header atual fica em duas linhas até 336 px e em uma linha a partir de 337 px; a logo não encolhe e o controle do tema mantém 65,7 px. Isso contrasta com a composição aprovada até 291 px e ícone-only em 320 px ou menos; a medição não autoriza implementar. [Evidência atual](../evidence/runtime/nav005-current-production-geometry-recheck-2026-10-24.md).
- `DECISION_APPLICATION_MAP.md` foi reconciliado ao mesmo commit: as oito rotas apontam às folhas CSS efetivamente carregadas e a evidência runtime atual ou às lacunas explícitas.
- O [mapa de famílias CSS/runtime](../evidence/architecture/visual-rule-family-runtime-map-2026-10-24.md) classifica as oito folhas por layout, texto/cor, interação/foco e movimento/assets, com evidência parcial ou `NOT VERIFIED`.
- **Próximo trabalho desta etapa:** revisão humana das PRs DRAFT validadas (#239, #241–#244 e Design System #51/#52). NAV-005 já foi implementado no escopo autorizado e validado no preview #244; a evidência está em [validação do preview #244](../evidence/runtime/nav005-pr244-preview-implementation-check-2026-10-24.md), mas a decisão canônica continua `implementationAuthorized=false`. O próximo trabalho técnico é retomar cobertura autenticada do Configurador (#232/DS-05A), sem inferir cobertura por semelhança de seletor.
- VIS-002C v0.3 e produto #241 têm gates/preview passados, mas seguem em DRAFT. A PR #240 foi encerrada como supersedida pela #241; os cinco seletores compartilhados com divergência foram reconciliados em v0.3, sem manter uma integração v0.2 ativa.

---

## Revalidação live do estágio — 24/10/2026

- Produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` inclui ARC-03C e P-COMP-01 via PR #237.
- PR #238 permanece DRAFT no head `abc33d24d0ff34e770feb0e12221fa9ba98870fd`. O gate autenticado [Actions #40126678308 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40126678308) revalidou bootstrap, Config, dois toggles reversíveis, Acabamentos/Serviços/Resumo com estimativa, negação de Admin e revogação. Tentativas anteriores no head `0c320c0` falharam em estágios variáveis (`services-navigation`, `finishes-estimate-readiness`, `finishes-next-action`, `summary-navigation`); nenhuma execução atual esclareceu a causa dessas falhas. No head atual, a segunda tentativa consecutiva do job autenticado também passou; isso reduz a incerteza do gate, mas não explica retrospectivamente as falhas do head anterior nem prova estabilidade geral. [Repetição e readback](../evidence/runtime/ds05a-auth-gate-stability-rerun-2026-10-24.md). Demais checks e Deploy Previews passaram; Supabase Preview foi skipped por falta de associação de branch, usando-se o banco interno já existente. Issue #232 continua aberta; os cinco fluxos históricos seguem validados em fixture V5 local, não em staging.
- PR #239 permanece DRAFT no head `e7b02c04308e9fcc7b52f1d09534058a2a0bbc65`. Gate browser dedicado, build ARC-03C, `pages:check`, `current-build`, `variants`, `current-asset-gates`, browsers e Deploy Previews principal/isolado passaram/READY. No Preview isolado, Tab → Enter atualizou `#main` e a leitura confirmou foco em `main#main` com `tabindex=-1`. Supabase Preview foi skipped por ausência de associação da branch. A correção está validada em preview, sem homologação visual global nem alteração da Production. [Evidência](../evidence/runtime/pr239-about-skip-link-preview-focus-2026-10-24.md).
- Registro histórico da head `baef9acd71bc636db66709d93c0d5cf0ab5d0134`: naquele momento a PR de produto [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241) cobria sete seletores; oito workflows e os dois status Netlify estavam SUCCESS, com Supabase Preview skipped. Esse checkpoint antecede a preferência por quase preto nos dez contextos. O estado atual e a revisão do head `f102c3037e2f64ebb904643bbc076064322f1672` estão no bloco inicial e na [evidência atualizada](../evidence/runtime/vis002c-v03-preview-10-contexts-manual-review-2026-10-25.md).
- Issue #224: a rechecagem anterior aguardava o scroll estabilizar e não media a janela transitória. Uma reprodução posterior na Production em 390×844 isolou o retorno ao grupo 1 quando Lavanderia era selecionada durante o scroll. A correção em [produto PR #243](https://github.com/EAKerber/MobiliPresenter2D/pull/243) foi repetida no preview em 320 e 390 px, nos temas claro e escuro: nos quatro casos seleção/paginação permaneceram em Lavanderia/grupo 2, sem overflow horizontal. Deploy READY; CI passou após repetição de uma checagem de rota que inicialmente recebeu 404 durante a convergência do deploy. A PR permanece DRAFT, sem integração ou deploy de produção. [Evidência da reprodução e validação](../evidence/runtime/issue224-carousel-transient-repro-pr243-2026-10-24.md); [evidência anterior](../evidence/runtime/issue224-carousel-source-recheck-2026-10-24.md).
- PR do Design System #51 permanece DRAFT no branch de handover; as atualizações desta PR são documentais e não alteram o runtime.
- Menu público na Production `main@5ccb2a8`: em 390×844, Tab/Enter abriu e levou foco ao primeiro link, Tab percorreu a navegação, Escape fechou e devolveu foco ao botão; clique externo também fechou. Com movimento reduzido, menu e controle não tinham animação em execução. A passagem cobre um recorte de rota/tema/largura; evidência em [`RUNTIME_AUDIT.md`](../RUNTIME_AUDIT.md).
- ARC-13: as oito entradas HTML têm 480 ocorrências/392 valores distintos, com 464 localizáveis, quatro identificadores excluídos e 12 itens comerciais deferidos. Em JS, o heurístico inicial achou 2.176 ocorrências em 52 fontes; uma busca direcionada por sinks DOM encontrou mais cinco rótulos de uma palavra. O índice atualizado liga e classifica **2.181 referências**: 728 textos de interface localizáveis, 1.263 trechos técnicos/identificadores e 190 decisões de conteúdo/domínio deferidas (17 de apresentação e 173 autorais/configuráveis/comerciais). Não restam referências indexadas sem classificação; a busca direcionada não prova cobertura completa da geração DOM. Evidências: [inventário suplementar de cinco sinks](../evidence/architecture/arc13-classified-admin-single-word-dom-sink-batch-2026-10-24.json), [cobertura de chaves](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) e [proposta de convenção](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json). No índice, 369 textos ainda não têm chave, cinco deles têm proposta em lote separado e 364 seguem sem proposta; 212 chaves usam sufixo de linha, das quais 13 têm exemplos de substituição propostos. A convenção não foi aprovada e não houve extração, migração ou alteração do produto.
- Os deploys Production atuais do Netlify principal e isolado estão READY em `main@5ccb2a8`, com nove Functions e uma Edge Function reportadas; a inspeção não executou a função.
- Estimativa geral provisória recalculada em 25/10: ~24% (faixa 22–26%); implementação de código do Design System ~18% (faixa 15–20%). A validação autenticada dos cinco fluxos no preview melhora a evidência de DS-05A, mas não conta como código integrado enquanto os PRs seguem DRAFT. Sem pesos oficiais, inventário, documentação e gates não contam como código integrado.
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

1. Atualizar evidências visuais de cabeçalhos cujo material persistido pertence a versões anteriores; cobrir rotas públicas e a tela de login sem sessão em temas e larguras representativas, sem persistir dados de conta. **Parcial em 24/10:** em Landing, About, Viewer e Como funciona, a 290 px a área útil foi 275 px; About cortou títulos/textos e deixou 11 px do menu visíveis, Viewer cortou conteúdo/preço e deixou 13 px, e Como funciona recortou conteúdo via `overflow-x:clip` deixando 11 px do menu. A 320 px, About/Viewer tiveram overflow horizontal de 15 px na sessão; Como funciona recortou a sobra. Em 335 px as três rotas não tiveram overflow; About também não em 360/390 px. A tela de login foi observada em 1280×720, 390×844 e 320×700; o formulário não foi enviado e o autofill impede afirmar perfil limpo. Uma rechecagem de foco por Tab em 1280×720, nos temas claro/escuro, localizou 2–2,66667 px e `#6E512E` no claro frente à referência VIS-002 de 4 px/`#8B6A40`; sem envio do formulário ou CSS alterado. O estilo escuro da marca não foi medido. No campo de e-mail, a razão calculada outline/superfície opaca foi 7,29:1 no claro e 9,29:1 no escuro; a geometria continua abaixo de 4 px/3 px e a medição não generaliza. [Evidência](../evidence/runtime/admin-login-no-session-focus-production-2026-10-24.md). A Landing continua com problema a 310/290 px. Issue #218 / NAV-005 permanece aberta; nenhuma proposta foi aplicada. Rechecagem mobile/touch em 290×720 (claro/escuro) confirmou `visualViewport=290`, `html/body min-width:320px`, `overflow-x:clip` e menu com 16 px cortados; 26/42 px continuam visíveis. A sessão com scrollbar clássica tinha 275 px úteis e 11 px visíveis, diferença contextual registrada. [Rechecagem mobile](../evidence/runtime/public-headers-320-production-2026-10-24.md). [Login](../evidence/runtime/admin-login-no-session-focus-production-2026-10-24.md) · [NAV-005](../evidence/runtime/landing-public-compact-header-production-2026-10-24.md) · [amostra 290/320/335 px](../evidence/runtime/public-headers-320-production-2026-10-24.md).
2. Completar verificações públicas de teclado, movimento reduzido, animações e estados de carregamento/erro em imagens; separar limitações de ferramenta de falhas do produto. **Parcial em 24/10:** em `/how-it-works/` Production, 28/28 imagens carregaram; na Landing, About e Viewer, 18/18, 3/3 e 22/22; todas sem falha e com atributo `alt`, nos viewports registrados. Rechecagem adicional em 1280×669, após percorrer a página, confirmou 28/28 carregadas, zero quebradas ou pendentes e oito atributos `alt=""`; a função decorativa das ilustrações do comparativo e das cinco etapas estava pendente na checagem inicial. A revisão visual posterior em Production, no tema escuro e viewport 851×397, inspecionou os oito casos em contexto: ícone WhatsApp nomeado pelo link, ilustração do comparativo junto de texto, logo redundante ao título e cinco ilustrações de categoria/etapa acompanhadas por nomes e descrições. Não foi encontrado texto único nas imagens; manter `alt=""` é sustentado para esses oito casos nesta rota/amostra, sem homologação de acessibilidade global. [Revisão visual dos oito casos](../evidence/runtime/how-it-works-step-illustrations-visual-review-2026-10-25.md). [Inventário e limites](../evidence/runtime/public-routes-keyboard-images-production-2026-10-24.md). [Rechecagem](../evidence/runtime/public-routes-keyboard-images-production-2026-10-24.md). Na Landing, Escape fechou o menu e devolveu foco ao botão após o splash já oculto. Em About, Enter no link de salto mudou a âncora para `#main`, mas o foco terminou em `body`; divergência observada, sem correção. A emulação de movimento reduzido cobre Landing, About e Viewer em 390 × 844 claro: A rechecagem em tema escuro nas mesmas três rotas e viewport examinou menu, ambiente, carrossel e hotspot; os estados funcionais ocorreram, as transições computaram 0,00001 s e nenhuma permaneceu ativa após 100 ms. A amostra escura usou cliques DOM e ajuste de `data-theme`, sem validar entrada física ou alternância de tema. transições visíveis foram reduzidas a 0,00001 s; a Landing menu abriu/fechou, a seleção de ambiente e o avanço do carrossel terminaram sem animação ativa, e a seleção do Viewer por teclado também terminou sem animações em execução. No baseline sem redução, a Landing registrou intro/reveal de 0,32–0,65 s, About não mostrou animações, e Viewer usava transições de 0,16/0,18 s. A cobertura não avalia animações em curso em todos os estados/rotas nem outras dimensões. Rechecagem adicional em `/how-it-works/` Production, viewport mobile 390 × 844, cobriu claro e escuro: baseline sem redução teve cinco elementos com transições 0,18–0,2 s; com redução não houve duração computada acima de 0,001 s. Enter em claro e Space em escuro abriram/fecharam disclosure mantendo foco no `summary`, com zero animação ativa após os toggles. Após percorrer a página, 28/28 imagens carregaram sem falhas ou pendências; oito tinham `alt=""`, sem classificar aqui sua intenção decorativa. [Addendum 24/10](../evidence/runtime/how-it-works-motion-css-runtime-snapshot-production-2026-10-24.md). Rede lenta foi simulada parcialmente em Como funciona, com atraso perceptível e zero falhas na amostra. Uma imagem não decorativa foi quebrada de forma controlada no DOM isolado: o `alt` permaneceu, mas o elemento colapsou para 449 × 43 px, sem handler ou placeholder customizado observado. Restaurada e carregada; a apresentação de erro fica como lacuna visual, não correção aplicada. [Rotas públicas, foco/imagens](../evidence/runtime/public-routes-keyboard-images-production-2026-10-24.md) · [Movimento reduzido nas três rotas](../evidence/runtime/public-routes-reduced-motion-runtime-production-2026-10-24.md) · [Como funciona, Slow 3G e erro](../evidence/runtime/how-it-works-motion-css-runtime-snapshot-production-2026-10-24.md).
3. Revalidar no DOM temas, superfícies e estados dinâmicos dos achados visuais. Medir contrastes efetivos com transparência/ancestrais e registrar cada caso como aprovado, falha, exceção ou não verificado. **Parcial em 24/10:** uma amostra em Landing, About e Como funciona nos dois temas mediu 4,79:1–13,85:1 nos pares de texto opacos selecionados; a faixa escura da legenda em Como funciona está presente e mede 13,85:1. Os valores atuais diferem de medições antigas, mas não fecham issue #216 nem certificam cobertura global. Transparências, imagens, todos os estados de foco/seleção e cobertura de todas as rotas/componentes seguem pendentes. Triagem DOM ampliada nas quatro rotas públicas (1280/390 px, dois temas) encontrou quatro pares de texto comum abaixo de 4,5:1 no tema claro: `#8B6A40/#E8E3DC` (3,89), `#706C66/#E8E3DC` (4,09), `#8B6A40/#F0EDE8` (4,25) e `#706C66/#F0EDE8` (4,47); todos os nós medidos no tema escuro passaram. Há candidatos contextuais reutilizando pares de paleta já aprovados, mas seletores novos dependem de aprovação: `VIS-002.implementationAuthorized=false` e #216 limita escopo. Evidência e proposta em [contraste público](../evidence/runtime/public-text-contrast-production-themes-2026-10-24.md). Sem alteração do produto. [Evidência da amostra](../evidence/runtime/public-text-contrast-production-themes-2026-10-24.md).
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

- **DS-05A parcialmente verificado.** No head `abc33d2`, a primeira tentativa do gate autenticado [Actions #40126678308 SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40126678308) confirmou readiness, dois toggles reversíveis, progressão por Acabamentos/Serviços/Resumo com estimativa, grant revogado e Admin negado; a repetição do job no mesmo run também passou, totalizando 2/2 tentativas consecutivas no head atual. O relatório contém apenas flags. Quatro tentativas anteriores no head `0c320c0` variaram entre falhas de navegação/readiness e permanecem sem causa confirmada. O gate atual não explica retroativamente essas falhas nem prova estabilidade geral. Permanecem pendentes opções internas de acabamento/serviço, combinações de preço, envio, cobertura Admin e a migração dos cinco fluxos funcionais legados para o staging autenticado; hoje eles seguem em fixture V5 local. [Repetição e limites](../evidence/runtime/ds05a-auth-gate-stability-rerun-2026-10-24.md) · [histórico](../evidence/runtime/ds05a-ci-stage-progression-2026-10-24.md) · [limite da fixture](../evidence/runtime/ds05a-ci-auth-fixture-limit-2026-10-24.md).
- **DS-05B/DS-05C permanecem pendentes**, conforme a sequência canônica de `decisions.json`; nenhum detector genérico ou integração com o laboratório v0.3 foi homologado por esta observação.
- **NAV-005:** a composição aprovada foi implementada e medida no preview da PR de produto [#244](https://github.com/EAKerber/MobiliPresenter2D/pull/244), em `/admin.html` e `/access/`. O header ficou em uma linha até 291 px; abaixo disso, as ações passam para outra linha; os controles medem 44 × 44 px e o texto do tema fica ícone-only em 320 px ou menos. A evidência inclui os limites da rota sem sessão e o único workflow vermelho, incompatibilidade preexistente no harness de hierarquia Admin. A PR continua DRAFT. A autorização desta conversa não alterou `decisions.json`, que mantém `implementationAuthorized: false`; não houve merge ou deploy de produção.


### About / Production — destino do link de salto (24/10/2026)

A auditoria anônima da Production confirmou que Enter em “Pular para o conteúdo” altera a URL para `#main`, mas deixa o foco em `body`; `main#main` não recebe foco naquela passagem. A PR produto #239 agora implementa a transferência para `main#main` e o gate browser/teclado real confirmou o destino no Deploy Preview do head `e7b02c04308e9fcc7b52f1d09534058a2a0bbc65`. A PR continua DRAFT; a validação é limitada a About/preview e não altera a Production. Evidência: [auditoria original de Production](../evidence/runtime/about-skip-link-production-focus-2026-10-24.md) · [Preview atualizado](../evidence/runtime/pr239-about-skip-link-preview-focus-2026-10-24.md).


### CI-BASELINE-01 — configuração Netlify e GitHub Actions (24/10/2026)

O deploy isolado `m2d-auth-ci-isolated` está READY em `main@5ccb2a8` e inclui `access-check`; readback confirma `DATABASE_URL` e `ACCESS_GATE_SECRET` nos contextos Netlify registrados, sem validar valores/conectividade. Rechecagem runtime às 22:00 UTC: `/api/public-modules` retornou 503 tanto em Production quanto no Deploy Preview #242 do site isolado; no host principal retornou 200 e sete módulos. A Function `public-modules` lê a chave `published` do Netlify Blobs store `configurator-settings`, não `DATABASE_URL`; a causa exata permanece desconhecida (snapshot ausente/inválido ou falha de leitura, sem logs internos). Isso não identifica uma variável extra de banco a adicionar. [Registro de ambientes e limites](../evidence/runtime/netlify-ci-auth-environments-2026-10-24.md). O gate autenticado de PR #238 usa conexão independente do GitHub Environment `ci-auth-isolated`; run histórico de sucesso valida a fixture CI, não o Blob Netlify ou a Edge Function. Supabase Preview permanece sem branch associado e o banco interno de teste é o usado pela fixture.


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

### Issue #226 — rechecagem do acordeão em Production (24/10/2026)

A rota publicada `/how-it-works/` atualmente mantém a altura dos cartões fechados quando outros itens abrem, inclusive com dois itens abertos ao mesmo tempo. A regra local `align-items:start` está presente nas duas grades de três colunas; o arquivo no `main` e no branch candidato conhecido tem o mesmo blob SHA. A rechecagem observou 1366 px em claro/escuro e layouts de uma coluna em 768 px e 390 px; Enter abre e Espaço fecha o `summary` nativo mantendo o foco. Detalhes de alturas e medidas: [rechecagem runtime #226](../evidence/runtime/issue226-accordion-grid-current-production-recheck-2026-10-24.md).

A issue [#226](https://github.com/EAKerber/MobiliPresenter2D/issues/226) continua aberta: falta uma comparação visual antes/depois confiável e a verificação de zoom. No workflow atualizado [#39611912828](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39611912828), as oito combinações funcionais passaram; Chromium teve paridade de pixels e WebKit divergência em 390 px nos dois temas. As capturas WebKit inspecionadas mostram conteúdos/regiões diferentes apesar de DOM, estilo computado e geometria iguais; como a regra candidata não se aplica abaixo de 901 px, o artefato é inconclusivo para regressão ou paridade e a causa exata segue aberta. [Evidência atualizada](../evidence/runtime/issue226-accordion-grid-current-production-recheck-2026-10-24.md). Nenhuma alteração foi feita no produto.

### PR #242 — revisão manual pontual do foco do Viewer (24/10/2026)

No Deploy Preview de produto, Tab em 390×844 claro focou o hotspot 06 sem mudar a seleção do hotspot 01; o contorno foi visível e o CSSOM confirmou 4 px/offset 3 px/`#8B6A40`. No escuro, uma checagem pontual por CSSOM confirmou 4 px/offset 3 px/`#D8BC7C`, mantendo o hotspot 01 selecionado. Em 1280×800 escuro, a caixa do foco permaneceu dentro da cena. A validação automatizada da PR cobre a sequência dos sete alvos em dois temas e dois tamanhos. [Revisão runtime pontual](../evidence/runtime/pr242-viewer-hotspot-focus-preview-manual-review-2026-10-24.md).

A PR [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242) continua DRAFT. A evidência não substitui a revisão visual do usuário nem avalia contraste de todas as fotografias; `decisions.json` permanece inalterado e não houve merge ou publicação.

### PR #239 — rechecagem manual do skip link de About (24/10/2026)

No Deploy Preview, Tab focou primeiro “Pular para o conteúdo” e Enter atualizou a URL para `#main`; o foco terminou em `main#main` (`tabindex="-1"`). A observação foi feita com largura de janela 1280 px e sem overflow horizontal. [Readback manual](../evidence/runtime/pr239-about-skip-link-preview-manual-recheck-2026-10-24.md).

A PR [#239](https://github.com/EAKerber/MobiliPresenter2D/pull/239) segue DRAFT. A passagem confirma transferência de foco em About; não substitui revisão visual em outros temas/tamanhos ou homologação global, nem altera Production.



### Issue #226 — complemento runtime Production — 24/10/2026

Nova rechecagem em Chromium de `/how-it-works/` cobriu 1366×768, 768×1024 e 390×844 nos temas claro/escuro. Em três colunas (1366 px), abrir uma fundação ou tópico cresceu apenas o próprio cartão; irmãos fechados da linha variaram 0 px. Em uma coluna (768/390 px), teclado nativo Enter/Espaço abriu/fechou os disclosures com foco mantido no `summary`. Tema foi emulado transitoriamente via DOM. Sem novas capturas, sem WebKit/zoom e sem alteração do produto. Isso complementa a matriz, mas não resolve a divergência de conteúdo das capturas WebKit no run #39611912828; comparação visual reproduzível e zoom continuam pendentes, então #226 fica aberta. [Evidência](../evidence/runtime/issue226-accordion-grid-current-production-recheck-2026-10-24.md).


### NAV-005 — implementação privada em preview, revalidada em 25/10/2026

Produto PR [#244](https://github.com/EAKerber/MobiliPresenter2D/pull/244), head `063796224c55924a8b3a909c9631c6b5f5590972`, continua DRAFT. Previews principal/isolado READY; oito workflows passaram, inclusive Admin hierarchy [#40147009586](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40147009586), que executou com sucesso as três suítes locais de hierarquia, persistência isolada e Save/readback v5 depois de corrigidos harnesses duplicados. Manualmente, `/admin.html` e `/access/` foram medidos no preview a 291 px e seguem o escopo aprovado; a sessão autenticada de Config e gestão de acesso permanece sem verificação. `decisions.json` permanece inalterado/autorização falsa; sem merge ou Production. [Evidência](../evidence/runtime/nav005-pr244-preview-implementation-check-2026-10-24.md).


## ARC-13 — lote de configuração preparado para revisão (25/10/2026)

Foi preparado um arquivo de candidatos para as 64 ocorrências restantes de validação em app/core/configuration.js. São 63 chaves propostas; as duas ocorrências idênticas de conflicting event target compartilham uma chave candidata porque mantêm a mesma mensagem, owner/consumer e parâmetro rule.id. O lote contém 33 templates com os parâmetros preservados, teve zero colisões com as chaves do índice auditado e mantém proveniência por linha e hash do arquivo. As sugestões ainda exigem revisão contextual; não alteram o índice nem o produto.

A fila de chaves numéricas sem proposta passa de 199 para 135. Próximos módulos dimensionados: hierarchy-administration.js (32), flow-model.js (30), presentation-contract.js (29), pricing-contract.js (24), administration-v5.js (13) e legacy-stage-repair.js (7). Também seguem 364 ocorrências sem chave e 190 itens de conteúdo deferidos.


## ARC-13 — chaves numéricas propostas nos sete módulos (25/10/2026)

O lote de configuration.js e o lote dos seis módulos centrais registram propostas para todas as 199 ocorrências que restavam das 212 chaves numéricas. Juntos são 199 ocorrências mapeadas a propostas; os 13 exemplos prévios permanecem candidatos auditados. O lote central cobre 135 ocorrências em hierarchy-administration.js, flow-model.js, presentation-contract.js, pricing-contract.js, administration-v5.js e legacy-stage-repair.js; 133 chaves sugeridas, 99 templates e zero colisões contra o índice atual. Uma mesma chave agrupa três ocorrências de unsupported layout profile, com owner/consumer e parâmetro profile iguais. Propostas não são aprovação de chaves individuais, e o índice/runtime continuam intactos.

A próxima frente é resolver contexto e ownership dos 364 textos sem chave em admin.js e app.js. O inventário não atribui consumer com confiança suficiente para compartilhar ou nomear tudo automaticamente; investigar os call sites antes de preparar sugestões. Os 190 itens de conteúdo deferidos seguem em trilha editorial separada.


## ARC-13 — fila sem chave mapeada por contexto (25/10/2026)

As 364 ocorrências sem chave em admin.js e app.js foram associadas, por análise lexical dos arquivos fonte pinados, a 72 funções candidatas a contexto de consumo. O mapa preserva linha, hash, texto, parâmetros e trecho exato de código. Foram encontrados 22 grupos de texto repetido; seis ocorrências parecem código ou markup e precisam ser reclassificadas. O nome da função é apenas pista, não prova do consumer: por isso ainda não gerei chaves para esta fila. Próximo passo é revisar os contextos de DOM/ARIA e owners, especialmente duplicatas entre funções e possíveis falsos positivos. [Mapa de contexto](../evidence/architecture/arc13-unkeyed-consumer-context-map-2026-10-25.json).

Com isso, todas as 212 referências numéricas têm proposta rastreável; as 364 sem chave agora têm contexto de código indexado, mas ainda não têm proposta de chave. Os 190 itens de conteúdo permanecem em inventário editorial separado. Nenhum índice ou runtime foi alterado.


## Correção de classificação ARC-13 — literais técnicos (25/10/2026)

A revisão dos seis sinais de possível código/markup confirmou que todos são valores técnicos: duas ocorrências de classe CSS, duas tags HTML, um código interno de estado e uma classe CSS adicional. A mensagem de interface na mesma linha do último caso segue separadamente classificada como localizável. Recomenda-se retirar as seis ocorrências técnicas da fila antes de nomear chaves; sem atualizar o índice, a fila atual de 364 cai para 358 candidatos locais após aplicar essa classificação. A decisão de refletir a reclassificação no índice fica para o lote de manutenção do próprio inventário. [Auditoria de origem](../evidence/architecture/arc13-unkeyed-code-literal-reclassification-2026-10-25.md).


## ARC-13 — reclassificação técnica e sinks dos textos sem chave (25/10/2026)

A revisão ampliada encontrou 19 valores técnicos entre as 364 ocorrências sem chave: classes/IDs CSS e DOM, nomes de tags/atributos, enum, código interno e role ARIA. Recomenda-se excluí-los da localização; ficam 345 candidatos de texto (208 Admin, 137 Configurador), sem atualização do índice.

O rastreio sintático da linha de origem encontrou 106 textos enviados diretamente a textContent/createTextNode, 33 em ARIA/alt, 14 em title/tooltip, três templates HTML, 66 valores em mapas/arrays e 123 em expressões sem sink explícito na própria linha. Os 189 valores de mapas/arrays e outras expressões ainda precisam ser ligados a consumers reais. Há 21 grupos repetidos após exclusões; igualdade de texto não basta para compartilhar chaves. [Auditoria de sinks](../evidence/architecture/arc13-unkeyed-direct-sink-audit-2026-10-25.md) · [Reclassificação técnica](../evidence/architecture/arc13-unkeyed-code-literal-reclassification-2026-10-25.md).

A verificação cruzada dos 217 candidatos de chave já propostos (212 ocorrências numéricas + cinco labels) encontrou 214 chaves únicas: três repetições agrupadas por texto/contrato idênticos e zero colisões com o índice fixado. Ainda falta revisão semântica das propostas; índice e produto seguem intactos.


## ARC-13 — revisão adicional de identificadores técnicos (25/10/2026)

A leitura dos textos com formato de identificador detectou três itens que ainda estavam na fila: slug dinâmico de `stage.id`, ID do carrossel usado por `aria-controls` e ID de status usado por `aria-describedby`. A evidência está no relatório de reclassificação e no [mapa atualizado](../evidence/architecture/arc13-unkeyed-consumer-scope-map-2026-10-25.json). A fila documental atual tem **338 textos** (207 Admin, 131 Configurador), após 22 valores técnicos e quatro mensagens diagnósticas internas. O índice/produto continuam sem mudança. A revisão por padrão de identificador é dirigida, então não declaro exaustividade; o próximo impedimento é rastrear consumers indiretos e validar se os demais valores têm contrato de UI.


## ARC-13 — primeiro lote com consumer confirmado (25/10/2026)

Rastreei `createDetailCarousel` no Configurador: o lote reúne **26 ocorrências** de títulos/rótulos curtos/descrições, nomes acessíveis, tooltips e ações de recolher. A proposta contém 16 chaves novas e quatro reutilizações intencionais de chaves já atribuídas ao mesmo carrossel; usa parâmetros `pageLabel`, `shortLabel`, `pageNumber` e `pageCount`. Anterior/próximo continuam mensagens distintas. A auditoria encontrou zero colisões com significado diferente e zero conflito de texto entre chaves. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-configurator-carousel-2026-10-25.json). O índice e o produto não mudaram; os itens continuam sem chave canônica até reconciliação.


## ARC-13 — ajuste após revisão do consumer do Viewer (25/10/2026)

O literal `Estrutural` em `updateSelection` é um valor comparado para escolher uma descrição, não um rótulo renderizado. A fila documental atual fica em **337 textos** (207 Admin, 130 Configurador), com 23 valores técnicos e quatro diagnósticos internos separados. [Reclassificação](../evidence/architecture/arc13-unkeyed-code-literal-reclassification-2026-10-25.md). O índice permanece em 369 textos sem chave no total; os lotes contextualizados continuam propostas até reconciliação canônica.


## ARC-13 — segundo lote com consumer confirmado (25/10/2026)

O consumer `updateSelection` foi revisado até os sinks DOM. Dos 13 registros do bucket, **12** têm proposta de chave em `configurator.moduleDetail`, sem colisão; `product.title` é parâmetro nomeado. O décimo terceiro item, ` · ${product.configurationNote}`, ficou deferido porque combina pontuação de composição com conteúdo vindo do catálogo; a ownership/mensagem final precisa ser confirmada antes de localizar. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-module-detail-2026-10-25.json). Nenhum índice ou runtime alterado.


## ARC-13 — lote Admin de materiais com consumer confirmado (25/10/2026)

`renderMaterials` foi rastreada até os labels, opções, alt da prévia, disclosure de destinos e ação de remoção. O lote tem **10 ocorrências**, dez chaves candidatas no namespace `admin.materials` e zero colisões. O nome do material no alt é parâmetro; o espaço inicial do texto da checkbox precisa ser preservado ou normalizado deliberadamente na extração. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-admin-materials-2026-10-25.json). Sem mudança do índice ou do produto.


## ARC-13 — lote Admin de etapas com consumer confirmado (25/10/2026)

`renderStages` foi rastreada aos sinks da seção de itens não atribuídos e dos cartões de etapa. O lote contém **12 ocorrências**, doze chaves propostas em `admin.stages` e zero colisões. Os nomes dinâmicos de etapa são parâmetros nas labels acessíveis; a ação “Adicionar” permanece específica deste consumer. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-admin-stages-2026-10-25.json). Sem alteração do índice ou do produto.


## ARC-13 — resumo de preços: contratos e limites (25/10/2026)

Revisei 19 registros em `renderSummary` e `createCommercialItemPriceBreakdown`. A proposta cobre **13 mensagens** completas/parameterizáveis, sem colisões. Cinco casos foram deferidos: copy longo com ownership de conteúdo, sufixo de contagem que exige plural, declaração fixa sobre Módulo 02, duas mensagens dentro de uma string HTML e texto de rateio montado em fragmentos/lista. O principal atrito agora é fronteira de mensagem: quatro valores com moeda são concatenados e precisam virar templates com parâmetro formatado; o rateio pede contrato explícito de contagem/lista. [Proposta e casos deferidos](../evidence/architecture/arc13-semantic-key-proposal-configurator-pricing-2026-10-25.json). Isso não muda o índice nem o produto.


## ARC-13 — convenção aprovada e próximos consumers Admin (25/10/2026)

- A convenção de chaves semânticas foi aprovada para uso documental: preservar o namespace existente, trocar o sufixo numérico por camelCase semântico, manter valores dinâmicos como parâmetros e compartilhar chaves somente quando owner, consumer e contrato coincidirem. Os 13 exemplos da proposta continuam não canônicos.
- A proposta [dos fluxos transacionais do Admin](../evidence/architecture/arc13-semantic-key-proposal-admin-transactional-save-2026-10-25.json) rastreia 41 ocorrências em `persistHandlesButton` e `saveButton`; consolida duas mensagens repetidas no mesmo consumer, propõe 39 chaves sem colisões observadas no índice-base e exclui dois rótulos dinâmicos de revisão para auditoria compartilhada.
- O escopo é documental: nenhum código, `decisions.json` ou índice ARC canônico foi alterado. Os textos enviados pela API e os detalhes dinâmicos de validação permanecem fora das propostas.


### ARC-13 — Admin loading e autenticação (25/10/2026)

- Proposta documental rastreia 12 textos de `loadSettings`, `showUser` e `showPasswordAction` até os sinks visíveis no Admin, com 12 chaves sem colisões no índice-base.
- A proposta exclui o rótulo de revisão dinâmico e qualquer texto dinâmico de erro; nenhum arquivo do produto, `decisions.json` ou índice canônico foi alterado. [Detalhes e ocorrências](../evidence/architecture/arc13-semantic-key-proposal-admin-loading-auth-2026-10-25.json).


### ARC-13 — Admin assets e eventos (25/10/2026)

- Foram mapeadas 10 ocorrências em `renderObjectAssets` e 13 em `renderEvents`, sem colisões observadas no índice-base.
- Caminhos de assets, labels de catálogo/alvos e valores de estado continuam dados dinâmicos; as propostas cobrem texto fixo e contratos explícitos para templates. Nenhum arquivo do produto, `decisions.json` ou índice ARC canônico foi alterado. [Assets](../evidence/architecture/arc13-semantic-key-proposal-admin-object-assets-2026-10-25.json) · [Eventos](../evidence/architecture/arc13-semantic-key-proposal-admin-events-2026-10-25.json).


### ARC-13 — Admin pricing e objects (25/10/2026)

- Propostas de `renderPricing` e `renderObjects`: 7 e 7 textos com sinks e contratos de parâmetros registrados, sem colisões observadas no índice-base.
- O template da base de preço ficou deferido porque mistura rótulo com enum e fallback bruto; labels dinâmicos do catálogo permanecem parâmetros. [Pricing](../evidence/architecture/arc13-semantic-key-proposal-admin-pricing-2026-10-25.json) · [Objects](../evidence/architecture/arc13-semantic-key-proposal-admin-objects-2026-10-25.json). Sem alterações no produto, `decisions.json` ou índice canônico.


### ARC-13 — Admin hierarchy, password reveal e finishes (25/10/2026)

- Proposta reúne 20 ocorrências em `syncPasswordReveal`, `appendInitialStateControl`, `appendNominalDimensionControls` e `renderFinishes`, com 18 chaves e zero colisões no índice-base.
- Templates de nomes de item, eixo e acabamento mantêm seus valores como parâmetros. Não altera código, índice canônico ou decisões. [Proposta](../evidence/architecture/arc13-semantic-key-proposal-admin-hierarchy-auth-finishes-2026-10-25.json).


### ARC-13 — Admin hierarchy, dependencies e pagination (25/10/2026)

- Proposta reúne 28 ocorrências dos editores de grupos de materiais, dependências, itens/seções/grupos hierárquicos e paginação. Não foram encontradas colisões no índice-base.
- Títulos de grupo e estado da página usam parâmetros explícitos; ações curtas continuam separadas por consumer. Nenhum arquivo de produto, índice canônico ou decisão foi alterado. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-admin-hierarchy-material-dependency-pager-2026-10-25.json).


### ARC-13 — Admin pricing constants, creation prompts e recovery (25/10/2026)

- Proposta cobre 14 textos em labels de pricing, criação de etapas/materiais e recuperação de senha; não foram encontradas colisões no índice-base.
- Mensagem e valor padrão de prompt são chaves separadas. Erros vindos da API e o fallback dinâmico da base de preço permanecem fora. Sem alteração no produto, índice canônico ou decisões. [Proposta](../evidence/architecture/arc13-semantic-key-proposal-admin-pricing-creation-recovery-2026-10-25.json).


### ARC-13 — Admin interactions and authentication feedback (25/10/2026)

- Proposta reúne 13 ocorrências em mensagens de pricing, divisão de seção/grupo e erros de login/senha; propõe 12 chaves sem colisões no índice-base.
- O rótulo de revisão foi recomposto com parâmetro inteiro; a mensagem de quantidade disponível ficou deferida até definir pluralização. Erros dinâmicos da API permanecem fora. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-admin-interactions-auth-2026-10-25.json).


### ARC-13 — Admin remaining controls and revision label (25/10/2026)

- Proposta reúne 18 literais de origem em controles hierárquicos, selectors, guardrails e acesso, com 14 chaves sem colisões no índice-base; rótulos de revisão compartilham contrato e sink.
- Três mensagens com pluralização e um fallback de enum foram deferidos. Nenhuma alteração no produto, índice canônico ou decisões. [Proposta](../evidence/architecture/arc13-semantic-key-proposal-admin-remaining-controls-2026-10-25.json).


### ARC-13 — Configurator custom stages and module controls (25/10/2026)

- Proposta documenta 12 literais nos consumers `renderCustomStage`, `createModuleNavigationButton` e `createModuleSelectionControl`, com parâmetros explícitos para títulos e labels do catálogo; zero colisões no índice-base.
- Só documentação foi alterada; nenhum código do produto, índice ARC canônico ou decisão foi modificado. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-configurator-custom-stage-and-module-controls-2026-10-25.json).


### ARC-13 — Configurator modules and accessories (25/10/2026)

- Proposta cobre 9 textos de seleção de módulos, estados de cards e controles de acessórios, sem colisões observadas no índice-base.
- Títulos de produto permanecem parâmetros; mensagens iguais em consumers diferentes não foram compartilhadas automaticamente. Sem alteração de código, índice canônico ou decisões. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-configurator-module-and-accessory-controls-2026-10-25.json).


### ARC-13 — Configurator finish and stone controls (25/10/2026)

- Proposta recompõe fragmentos de acabamento em rótulos acessíveis completos e cobre controles de pedra, com 4 chaves sem colisões no índice-base.
- O ramo de descrição “sem adicional” ficou deferido junto da alternativa com valor, para revisão conjunta do formato monetário. Sem alterações no produto ou índice canônico. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-configurator-finish-and-stone-controls-2026-10-25.json).


### ARC-13 — Configurator mobile scene and feedback (25/10/2026)

- Proposta cobre 25 literais de origem nos controles da mini-cena, seleções de acabamento/pedra/puxador, confirmação de reset e alerta fail-closed; 22 chaves, sem colisões no índice-base.
- Labels do catálogo ficam como parâmetros; aviso de disponibilidade emitido por dois caminhos compartilha mensagem e contrato. Sem alteração de produto, índice canônico ou decisões. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-configurator-mobile-scene-and-feedback-2026-10-25.json).


### ARC-13 — Configurator stage and detail messages (25/10/2026)

- Proposta cobre 6 literais de origem em acessibilidade de imagem, navegação entre etapas, abertura de ficha e estado vazio do resumo, com 5 chaves e zero colisões no índice-base.
- Labels de produto/etapa ficam como parâmetros; a mensagem de abertura recompõe dois fragmentos numa frase. Nenhuma alteração no produto ou índice canônico. [Detalhes](../evidence/architecture/arc13-semantic-key-proposal-configurator-stage-and-detail-messages-2026-10-25.json).


### ARC-13 semantic key proposal readback — 25/10/2026

The approved naming convention remains stable. The frozen consumer map has 336 raw candidates, 331 distinct file/line/literal identities, and five duplicate rows. Contextual proposals cover 315/331 distinct identities (95.2%); 16 lack proposals. The residual register groups them into plural/list formatting (8), strings embedded in HTML (3), and catalog/editorial ownership (5), and records the remaining raw-enum fallback risk. No product runtime, canonical index, or decisions.json change was made. The next gate is choosing the pluralization/message format and assigning content owners; see the linked residual register.


### ARC-13 — decisões residuais e nós de texto em HTML (25/10/2026)

- O usuário adiou as oito mensagens de plural/lista para a etapa de localização. Os cinco itens de catálogo/editorial devem permanecer no catálogo e aguardam revisão do owner do conteúdo.
- Proposta documental para as três identidades em `app/app.js:1603, 1607 e 1661`: cinco chaves textuais em nós separados, preservando o markup e mantendo distintos os consumers `renderCurrentValue` e `renderSummary`. Colisões no índice e nos lotes de proposta: zero. [Proposta](../evidence/architecture/arc13-semantic-key-proposal-configurator-html-text-nodes-2026-10-25.json).
- Readback do mapa ARC-13: **318/331 (96,1%)** identidades distintas com proposta; 13 sem proposta (oito adiadas para localização, cinco esperando owner). Risco de fallback bruto de enum segue separado. A porcentagem mede preparação documental, não implementação nem conclusão.
- PR #51 continua DRAFT; sem mudança de runtime, índice canônico, `decisions.json`, merge ou Production.


### Consolidação de preview About/VIS-002 — PR #239 absorvida pela #241 (25/10/2026)

- A PR #239 foi incorporada à branch da #241 como commit de dois pais `45e532b444967bdd901ac2f49fc8d0548daa881a`; o conflito lógico de `about.css` e do manifesto gerado foi composto, e os hashes fonte/HTML da página About conferem. A #239 foi encerrada como supersedida, sem apagar a branch. [Evidência](../evidence/runtime/pr241-pr239-about-skip-link-consolidation-preview-2026-10-25.md).
- A head combinada passou 9/9 workflows e os dois Deploy Previews ficaram SUCCESS. A checagem manual confirmou Tab → foco visível no skip link → Enter → `#main` com foco em `main#main`.
- O CSS declara offset de 3 px, mas o CSSOM retornou 2,66667 px tanto no skip link como num controle. A divergência já se reproduziu fora do seletor; sua causa permanece desconhecida e não alterei o valor aprovado.
- A PR #241 continua DRAFT e sem merge/Production; todas as oito PRs de implementação/revisão consultadas ainda não têm reviews humanos. A consolidação reduziu uma branch redundante, mantendo PRs com escopos independentes separados.
