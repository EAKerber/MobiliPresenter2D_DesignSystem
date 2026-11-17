# ARC-15 — Inventário de verificações do Produto

**Estado:** primeira passada documental e de overlaps, com baseline em Product main46, concluída; a matriz integral assertion→risco→rota/estado e decisões do owner continuam pendentes. Um recorte pós-publicação em main64 está no [incremento focado de configuração publicada/API](ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md).
**Fonte:** primeira passada em `EAKerber/MobiliPresenter2D` `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`; não representa o inventário pós-#275.
**Método:** leitura dos contratos, comandos, gatilhos e áreas cobertas; classificação por risco/assertion/rota/estado, não por quantidade de arquivos.  
**Execução:** nenhuma suíte foi executada na primeira passada ou na reconciliação de 16/11. Nenhum teste ou workflow foi alterado; branches de PR ficaram fora da baseline main46.

**Reconciliação pós-#275:** a baseline acima permanece pinada em main46. Um recorte independente e não executado de configuração publicada, API, leitor buyer e workflows foi documentado em [matriz ARC-15 main64](ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md). Esse incremento não atualiza a contagem nem a matriz integral dos 21 workflows/21 comandos.
**Incremento de triagem — gate de teclado pós-#277 (16/11/2026):** a PR #269 levou à revisão da falha de Tab em `/config/`. Antes da instrumentação, a asserção e o código do Configurador eram iguais na `main` e na candidata; o CSS da PR atua apenas no header público. O gate usa V5 loopback derivado dos defaults, com checkbox do primeiro módulo habilitado. A falha em `6651342` ocorreu uma vez e o rerun do mesmo SHA passou. No head `8c77350b`, 12/12 Actions passaram após o teste confirmar o foco inicial e manter a expectativa original de Tab para o botão de inspeção. Classificação provisória: falha intermitente/diagnóstico insuficiente do gate, sem evidência de regressão funcional. Este caso é evidência de PR, não altera a matriz de assertions pinada em main46 nem a contagem dos 21 comandos/workflows.

## Parecer Common Sense Judge

**Não há base para remover um teste ou workflow inteiro.** A leitura encontrou reexecuções do mesmo arquivo/comando em workflows distintos e alguns trechos de assertions repetidos, mas cada integração/commit ainda precisa receber sua própria execução e status. Nos pares de assertions, os testes mantêm garantias exclusivas; a sobreposição serve para avaliar eventual compartilhamento de implementação, não para concluir redundância. Os oito arquivos sem chamada localizada têm parecer individual abaixo; sua classificação técnica não substitui a decisão do owner.

O mapa agora cobre os comandos dos 21 workflows e o conteúdo dos 21 comandos de `app/npm test`, com pares de overlap identificados. Ainda não é um crosswalk integral de cada assertion por rota e estado; `test-core.js` é o principal limite semântico por seu escopo amplo. A ausência de um par exato confirmado não prova inexistência de overlap.

## Contagem localizada

O script `app/package.json → scripts.test` contém 19 scripts Node e chama ainda dois validadores Python: `tools/validate-assets.py` e `tools/validate-r5a-pixelperfect.py`. São 21 comandos encadeados na suíte da pasta `app`, não 21 workflows nem a contagem de todos os testes do repositório.

Há 21 workflows YAML no pin analisado. Os comandos variam: alguns executam a suíte completa, outros executam unitários, browser gates, validators ou verificações de produção. A contagem de arquivos não mede repetição de assertions.

## Matriz comando → risco/estado → âncoras

Escopo: os 21 comandos encadeados por `app/package.json → scripts.test` no Product `main@46a52e76`. As âncoras apontam para `app/tools/` e resumem a superfície/estado principal; não substituem a revisão de cada assertion. Workflows e branches de PR são avaliados separadamente.

| Comando (cwd `app/`) | Risco e estado/superfície | Âncoras |
|---|---|---|
| `node tools/test-access-policy.mjs` | Fronteiras de autorização: admin/staff/buyer, sessão temporária, grants e páginas/configurador internos. | `app/tools/test-access-policy.mjs:22–42` |
| `node tools/test-item-capabilities.js` | Compatibilidade entre tipo de item, etapa e ação disponível (seleção/toggle/ação). | `app/tools/test-item-capabilities.js:18–57` |
| `node tools/test-layout-profiles.js` | Seleção dos perfis responsivos compacto/empilhado/lateral e limites de largura. | `app/tools/test-layout-profiles.js:8–34` |
| `node tools/test-presentation-contract.js` | Combinações suportadas entre presentation, behavior e componente. | `app/tools/test-presentation-contract.js:11–172` |
| `node tools/test-flow-model.js` | Ordem e normalização de etapas/grupos/seções/itens; proteção contra mutação do fluxo. | `app/tools/test-flow-model.js:29–209` |
| `node tools/test-administration-v5.js` | Migração/validação do Admin v5, política de apresentação e preço tipado, sem autoridade legada paralela. | `app/tools/test-administration-v5.js:34–402` |
| `node tools/test-published-configuration.js` | Leitura simulada de `published` e normalização de documentos v3/v5. | `app/tools/test-published-configuration.js:22–81` |
| `node tools/test-published-buyer-projection.js` | Projeção buyer v3/v5 preserva hierarquia/etapas e expõe somente preço permitido. | `app/tools/test-published-buyer-projection.js:27–87` |
| `node tools/test-v5-publication-migration.js` | Preflight, ETag/`onlyIfMatch`, falhas, quantidade de writes e readback na migração v3→v5. | `app/tools/test-v5-publication-migration.js:23–131` |
| `node tools/test-v5-normal-save.js` | Concorrência no save v5, rejeição sem write e confirmação por revision/readback. | `app/tools/test-v5-normal-save.js:20–108` |
| `node tools/test-postv5-new-material-roundtrip.js` | Novo material: forma, grupo/acabamento/preço, projeção buyer, save/readback e módulo sem registro. | `app/tools/test-postv5-new-material-roundtrip.js:36–104` |
| `node tools/test-v5-offline-rehearsal.js` | Ensaio local de migração, assinatura/digest, um write exato e inspeção posterior. | `app/tools/test-v5-offline-rehearsal.js:40–162` |
| `node tools/test-v5-publication-inspection.js` | Preflight somente leitura de ETag/revision/digest, blob ausente, JSON inválido e estados de bloqueio. | `app/tools/test-v5-publication-inspection.js:22–92` |
| `node tools/test-v5-endpoint-safety.js` | Endpoint simulado: anônimo 401, staff 403, admin 200; isolamento preview/produção, cache privado, migração aposentada e sem downgrade. | `app/tools/test-v5-endpoint-safety.js:3–216` |
| `node tools/test-legacy-stage-repair.js` | Planejador puro de handles; aceita delta exato e rejeita delta, ordem ou owner inesperados. | `app/tools/test-legacy-stage-repair.js:16–39` |
| `node tools/test-flow-layout.js` | Grupos, spans, componentes e IDs semânticos no layout do fluxo. | `app/tools/test-flow-layout.js:32–208` |
| `node tools/test-hierarchy-administration.js` | Administração hierárquica v4, validação de groups/sections e ausência de autoridade flat paralela. | `app/tools/test-hierarchy-administration.js:29–187` |
| `node tools/test-hierarchy-editor.js` | Reordenação, divisão, mescla e movimento de grupos/seções sem mutar a origem. | `app/tools/test-hierarchy-editor.js:32–160` |
| `node tools/test-core.js` | Integração ampla: cena/seleção, DOM/CSS, configuração/preço/validação, estimativas, projeção buyer, markup/layout responsivo, dock/PiP/hotspots. | `app/tools/test-core.js:44–54, 64–92, 95–420, 541–720, 722–988` |
| `python3 tools/validate-assets.py` | Metadados SHA/canvas/alphaBounds, suporte de máscaras, ownership do módulo 02, bridge e composição golden. | `app/tools/validate-assets.py:27–172` |
| `python3 tools/validate-r5a-pixelperfect.py` | Reconstrução byte-exata, invariantes RGB/alpha da variante/máscara e igualdade de pixels na composição final. | `app/tools/validate-r5a-pixelperfect.py:11–103` |

## Repetições exatas de invocação

Repetir a chamada em workflows diferentes não significa que um resultado de CI possa ser reutilizado: cada SHA e cada integração precisa receber status próprio, e os workflows podem acrescentar contratos distintos.

| Arquivo/comando chamado | Workflows e localizações observadas | Leitura |
|---|---|---|
| `npm test` em `app/` | `app-build-purity.yml:44–46`, `candidate-assets.yml:52–54`, `module02-fidelity.yml:34–36`, `variant-fidelity.yml:38–40` | Mesma cadeia de 21 comandos. Os quatro workflows executam em contextos distintos; `module02-fidelity` é manual e mantém replay de baseline. Os outros acrescentam verificações próprias. |
| `tests/public-cutover-contract.cjs` | `p-comp-01-public-menu-gate.yml:41–47`, `public-routing-before-clerk.yml:39–45`, `ux-auth-viewer-integration-gate.yml:41–48` | Mesma fonte de assertions em três gates de integração. Pode-se avaliar compartilhar a definição do job, mantendo execução/status por head e as verificações próprias de cada workflow. |
| `tests/viewer-secondary-header-browser-gate.mjs` | `p-comp-01-public-menu-gate.yml:60–63`, `ux-auth-viewer-integration-gate.yml:61–66` | Mesmo browser gate em fluxos diferentes; cada fluxo mantém seus outros contratos. |
| `app/tools/test-public-modules-endpoint.js` | `public-routing-before-clerk.yml:39–45`, `viewer-base-price-contract-gate.yml:27–28` | Mesmo teste de endpoint chamado em gates com eventos e verificações adicionais diferentes. |
| `app/tools/test-core.js` | Incluído em `app/npm test` e chamado diretamente em `summary-pricing-browser.yml:38–45` | O browser gate acrescenta fluxo de browser; a chamada direta repete a execução do script, não elimina o gate. |
| `test-administration-v5.js`, `test-v5-normal-save.js`, `test-v5-endpoint-safety.js` | Incluídos em `app/npm test`; chamados diretamente por `viewer-base-price-contract-gate.yml:27–28` | Subset da suíte repetido no gate de preço, que acrescenta publicação, build e browser. |
| `tests/test_branch_hygiene_plan.py` | Chamada direta em `branch-hygiene.yml:35–39`; incluída pela descoberta `test_branch_hygiene_*.py` de `branch-hygiene-bounded.yml:42–45` | A mesma unidade de plano é executada em dois workflows. O bounded também cobre limpeza pós-merge; a lista completa incluída pelo glob não foi confirmada. |
| `tools/validate-baseline.py` | `module02-fidelity.yml:32–33`; também chamado por `tools/check-r0-contract.py:35–36` quando o manifesto está `READY` | Repetição condicional da validação de baseline; o estado efetivo do manifesto neste parecer é UNKNOWN. |

## Assertions repetidas ou parcialmente repetidas

| Par verificado | Repetição encontrada | Garantias próprias que permanecem |
|---|---|---|
| `app/tools/test-administration-v5.js:278–280` ↔ `test-hierarchy-administration.js:184–186` | Três source guards iguais para schemas, `hierarchy_publication_required` e `persist-handles-all`. | O restante dos contratos V5/V4 difere; `app/tools/test-hierarchy-administration.js:187` ainda verifica `legacyStageRepair.verifyHandlesOnlyDelta`. Manter ambos os testes. |
| `app/tools/test-administration-v5.js:193` ↔ `app/tools/test-hierarchy-administration.js:93` | A mesma invariável preserva a linha de preço em duas projeções. | Os caminhos de projeção V5 e V4 continuam distintos; é uma assertion compartilhada em cenários diferentes. |
| `app/tools/validate-assets.py:61–67,142–151` ↔ `app/tools/validate-r5a-pixelperfect.py:36–63,65–76,89–95` | Reconstrução da máscara do módulo 02 e comparação do golden PNG. | Os validadores usam fontes diferentes para ordem da composição; o R5A também prova reconstrução byte-exacta, imutabilidade RGB/alpha e semântica da máscara. Não remover nenhum arquivo por este overlap parcial. |
| `flow-layout-browser.cjs:143` ↔ `mobile-pip-main-browser.cjs:179` | A ordem dos slots do dock é verificada em ambos. | Os viewports, geometria do dock e a interação PiP mantêm provas próprias. |
| `test_gap_parallelism_gate.py` ↔ `test_perspective_editorial_gate.py` | Regras semânticas próximas, como rejeitar direção invertida. | Schemas, referências e inputs são diferentes; não é fixture nem assertion idêntica. O pixel test mede arte real e preserva garantia própria. |
| Projeção pública, endpoint, Preview e produção read-only | Schema/allowlist e rejeição de entradas inválidas têm interseções parciais em testes unitários, função com stores simulados, probes do Preview e GET de produção. | Camada/alvo distintos. Sem base para remover uma camada. |
| Fallback de imagem, menus, fluxo de pedra/preço e runtime do rodapé | Alguns estados/ações aparecem em testes puros e browser. | Browser acrescenta geometria, acessibilidade, canvas ou interação; as saídas verificadas diferem. |
| `app/tools/validate-assets.py` e validadores de arte | Máscara, golden, provenance e alguns dados de entrada são compartilhados. | Inventory/hash/canvas/alpha bounds/front masks/seam bridge e invariantes R5A específicas preservam cobertura distinta. |

## Repetição de precondições e infraestrutura

Fixtures V5 válidas, preflight `ok`, e protocolo dos mocks Blob (`key="published"` e consistência strong) aparecem em vários testes; são precondições e boilerplate dos test doubles, não equivalência dos cenários de migração, leitura, save, projeção e segurança. Também há repetição de build/`pages:check` em workflows públicos; isso é infraestrutura repetida, enquanto os browsers de foco, diferencial do header, preço e tokens verificam contratos diferentes.

## Verificações sem invocação automática localizada

A busca nos 21 workflows e em `app/package.json` não encontrou chamada explícita para os oito arquivos abaixo. Em particular, path filter correspondente não conta como chamada:

- `tests/public-pages-integrated.cjs`
- `tests/ui-theme-contract.cjs`
- `tests/exposed-sides-glass.cjs`
- `tests/test_mask_semantics.py`
- `tests/test_stone_backing.py`
- `tests/test_stone_cleanplate.py`
- `tests/test_stone_surface_masks.py`
- `tests/validate-exposed-side-pixels.py`

A busca não encontrou invocação explícita; o parecer separa destinos prováveis e a decisão concreta ainda pendente para cada família. Nenhuma das oito foi classificada como obsoleta.

Há quatro discrepâncias concretas entre gatilhos e comandos:

1. `candidate-assets.yml` observa `tests/**` como path trigger, mas sua lista explícita de unittest não executa os cinco testes Python de máscaras/stone/exposed-side listados acima. O trigger faz o workflow iniciar, mas não transforma esses arquivos em verificações executadas.
2. `arc03c-static-page-build-gate.yml` tem gatilho push limitado a branches históricas, sem `pull_request` ou `main`. O path filter inclui `tests/public-header-controller-gate.mjs`, porém o comando executa `tests/arc03c-published-pages-browser-differential.mjs`, não o controller gate. O controller é executado no workflow P-COMP.
3. `public-routing-before-clerk.yml` observa `tests/public-*.cjs`, o que inclui `tests/public-pages-integrated.cjs`, mas o workflow executa `tests/public-cutover-contract.cjs`, outros contratos públicos e `tests/public-pages-smoke.cjs`; não executa `public-pages-integrated.cjs`; a fixture da PR #180 não equivale a uma fixture reutilizável de gate.
4. `viewer-base-price-contract-gate.yml` executa testes unitários e browser, mas está em `push` para `main`/branch de integração e `workflow_dispatch`; não há trigger de PR.

## Parecer por arquivo sem invocação localizada

| Arquivo | Evidência examinada | Leitura do juiz | Pendência concreta do owner |
|---|---|---|---|
| `tests/public-pages-integrated.cjs` | E2E real em Deploy Preview, dependente da seed/fixture da PR #180 (módulo e conteúdo fixos); o filtro `public-*.cjs` só o faz acordar, não o executa. | Replay histórico/de integração, preso à fixture; não é gate genérico reutilizável no estado atual. | Recriar fixture estável para replay ou preservar como evidência histórica/manual. |
| `tests/ui-theme-contract.cjs` | Node + VM; cobre sete shells, bootstrap/CSS, marca, navegação, controle de 44 px, estados de tema/storage e hashes dos logos. | Contrato estático plausivelmente ativo e barato, mas acoplado a seletores, literais e hashes. | Confirmar quais valores/seletores continuam normativos e decidir paths de execução. |
| `tests/exposed-sides-glass.cjs` | Browser local `file://`; 256 combinações de sete módulos e serviço global; captura estados e confere z-order, ARIA e erros JS. | Cobertura distinta de testes de pixels; candidato a regressão browser/visual. | Definir captura para revisão manual ou gate automático por paths. |
| `tests/test_mask_semantics.py` | Compara alpha bounds com dados técnicos e bytes da máscara inline com PNG canônico. | Candidato a gate de semântica de máscara/manifest/inline mask. | Selecionar os paths que devem acordá-lo e confirmar invocação explícita. |
| `tests/test_stone_backing.py` | Replay determinístico de geração com donor corrompido fora da máscara; valida hash, zero diffs e oito estados; `semanticReview=PENDING`. | Útil como replay técnico, sem aprovação semântica final. | Preservar a revisão humana pendente; decidir trigger/invocação por família stone. |
| `tests/test_stone_cleanplate.py` | Valida hashes de cleanplate/composição, roundtrip zero e superfícies aceitas. | Candidato a gate da família cleanplate. | Selecionar paths e fluxo de atualização quando os artefatos mudarem. |
| `tests/test_stone_surface_masks.py` | Confere landmarks, máscaras disjuntas dentro da alpha, determinismo e pontes que exigem ambos os hosts. | Candidato a gate de stone masks; contrato diferente da revisão semântica do backing. | Selecionar paths e preservar os dois hosts necessários. |
| `tests/validate-exposed-side-pixels.py` | Pixel smoke de bounds e pontos de vidro, hood e pedras. | Sobreposição parcial com outros checks; cobre pixels de integração específicos que não são totalmente substituídos por eles. | Selecionar paths para pixels/famílias e manter pontos ao atualizar arte. |

**Decisões agrupadas:** (1) destino do E2E preso à fixture #180; (2) valores normativos e paths de `ui-theme-contract`; (3) revisão manual versus gate para o browser glass; (4) triggers por família para os cinco checks Python e preservação explícita de `semanticReview=PENDING`. Recomendação do juiz não remove, adiciona, executa nem aprova mudanças na suíte.
## Decisões e pendências

A consulta de branch protection do Produto não pôde ser lida nesta sessão (HTTP 403 da integração). O conjunto de required checks permanece **UNKNOWN**; sucesso de workflow, isoladamente, não prova que um check seja obrigatório.

| Disposição | Estado |
|---|---|
| Excluir testes por alta contagem ou semelhança de nomes | **Não recomendado.** Nenhum teste foi provado redundante no nível do contrato. |
| Consolidar chamadas repetidas de testes | Candidato de CI: compartilhar definições de job para `npm test`, `public-cutover-contract.cjs` e outros arquivos chamados em mais de um workflow. Executar e publicar status em cada SHA aplicável; preservar as garantias adicionais e required checks de cada fluxo. |
| Consolidar `public-cutover-contract.cjs` | Candidata a workflow reutilizável; executar separadamente para cada head e preservar os três gates de integração específicos e seus status. |
| Resolver as oito classificações | O parecer técnico recomenda destinos por arquivo; o owner ainda decide fixture #180, valores normativos de tema, revisão/capturas do glass e paths dos cinco checks Python. Sem exclusão até a disposição. |
| Alinhar path filters, comandos e PR trigger | Decisão do owner sobre intenção de ARC03C, candidate assets, public-routing e viewer-base-price; depois corrigir os pares divergentes. |
| Fechar ARC-15 | Matriz de comandos e parecer individual dos oito itens documentados; faltam matriz integral por assertion/rota/estado, as quatro decisões agrupadas e confirmação dos required checks. |

**Resultado desta passada:** todos os 21 workflows e os 21 comandos da suíte `app` foram mapeados sem executar suítes. Foram documentadas as invocações repetidas, os overlaps exatos/parciais de assertions e quatro desalinhamentos trigger→invocação. Não há prova de que um teste ou workflow inteiro seja removível. Permanecem abertas a matriz integral assertion→risco→rota/estado, as quatro decisões agrupadas do owner e required checks (UNKNOWN/403). Nenhuma redução, consolidação ou mudança de teste/workflow foi autorizada.

## Delta após PR #277 — gate geométrico do hero (16/11/2026)

**Pin e evidência.** Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` inclui as alterações de #275 e #277. O arquivo [`tests/home-hero-phone-geometry-browser.cjs`](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/tests/home-hero-phone-geometry-browser.cjs) é uma nova verificação no delta após main46; blob `9630d2272d39a4c962a66ac1d29b263a84e59e53`. O workflow [Mobile browser](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/mobile-browser.yml), blob `2c1e379faf6e7105ac5f711060d46da7cede2d6a`, continua sendo um dos 21 workflows; o delta adicionou o passo ao fluxo existente, não um workflow YAML adicional.

O run PR [#43799448351](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448351) terminou com sucesso. O job rodou no merge ref sintético `eaf821d54c0c015d7a1a96d376be7f6ea30eecf3` (PR #277 sobre `2cb63cbf`); o passo 7, “Verify home hero phone screen alignment”, passou e produziu `HOME_HERO_PHONE_GEOMETRY_PASS` em 390, 516, 1024 e 1366 px. Os retângulos medidos foram, respectivamente, `206.14×458.83`, `206.14×458.83`, `206.14×458.83` e `252.23×561.42` CSS px. [Artefato do run](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448351/artifacts/14195552207).

**O que a verificação cobre.** Ela exige que as páginas autoral e publicada usem `data-screen-left/top/width/height = 305/617/350/779`; compara o retângulo CSS com essas coordenadas do `viewBox 1024×1536` escaladas pela largura real da arte; mantém a tela dentro do recorte da arte; verifica o recuo de 2 px do player, o preenchimento da mídia/poster, o play central e um viewport de pelo menos 200 px. Também fixa hashes da arte `lifestyle-phone-expanded.svg` e do poster, e confere os controles nativos e a ausência de política forçada para legendas. O asset expandido é uma adição pós-main46, não o desenho antigo.

**Limites importantes.** O gate confirma que o DOM acompanha a calibração escolhida, mas não demonstra que as coordenadas escolhidas coincidem com a borda física do visor: não faz comparação de pixels da moldura nem revisão automatizada da captura. A página é servida localmente; o teste bloqueia origens externas, então não renderiza o iframe/Shorts real. Também não verifica o retângulo/visibilidade do controle sobreposto `heroPhoneFullscreen`, a entrada/saída da tela cheia nem a página “Como funciona”. Essas interações foram revisadas manualmente no Preview #277, fora deste gate. Logo, um pin geométrico incorreto ainda pode passar; esta é uma regressão de alinhamento DOM, não uma prova visual/funcional completa.

**Parecer do ARC-15:** manter esta verificação como gate de geometria responsiva; classificá-la como parcialmente sobreposta ao browser/artefato visual, não redundante. Para fechar a lacuna, uma assertion focada deve conferir bounds/visibilidade dos controles próprios nas duas páginas e a transição de estado fullscreen; a confirmação do encaixe arte→visor continua exigindo julgamento visual ou uma referência de pixels aprovada. Nenhum teste foi removido, executado ou alterado neste lote documental. Esta revisão não recalcula as contagens/21 comandos da suíte `app` e não fecha a matriz integral assertion→risco→rota/estado.

## Revalidação live — gate de teclado e limites de cobertura (16/11/2026)

Product `main` permanece em `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`. A PR #269 foi reconciliada sobre essa base; o head atual é `8c77350ba5de38711722fb5af024b90c2f1bd7f9`, com Preview success e 12/12 workflows Actions verdes. A PR permanece Draft.

**Diagnóstico do teclado.** O workflow usa fixture V5 local derivada dos defaults. O primeiro módulo `module-01` está habilitado; o DOM posiciona o checkbox imediatamente antes do botão de inspeção. A primeira tentativa no head anterior `6651342` falhou em `tests/keyboard-browser.cjs:126`, mas o rerun do mesmo SHA e job passou. O diff de runtime da PR não altera o Configurador; a mudança em `app/ui-theme.css` vale somente para o header público e não muda a rota `/config/`. A evidência não mostra regressão funcional da PR e classifica o sinal anterior como intermitente/insuficientemente diagnosticado.

A mudança de teste em `8c77350` confirma que o checkbox está habilitado e que recebeu foco antes de Tab; mantém a expectativa original de foco no botão de inspeção e imprime o elemento ativo caso a asserção falhe. O gate passou no head exato. Nenhum runtime foi alterado nem a expectativa de navegação foi removida.

**Fronteira dos gates de navegação.** Os dois fluxos abaixo compartilham padrões gerais de teclado/foco, mas cobrem superfícies e riscos diferentes:

| Gate / fonte | Superfície e garantia principal | Relação |
|---|---|---|
| `tests/keyboard-browser.cjs` — Keyboard browser, V5 loopback | Configurador e Admin; atalhos de módulo, checkbox→inspeção, fechar/restaurar foco, navegação de etapas, rolagem e revelar senha. | Exclusivo para a configuração e estados locais V5; não cobre menu público. |
| `tests/ci/public-navigation-semantic-browser.mjs` — NAV-005 public header browser | Header público e Viewer; abrir/fechar menu, sequência de foco e CTA, redimensionamento, skip link e cards econômicos em Chromium/WebKit. | Exclusivo para navegação pública e Viewer; não valida o foco checkbox→inspeção no Configurador. |

Enter, Escape e padrões gerais de foco são interseções de implementação, não garantias duplicadas. Rotas, elementos, estados e fixtures diferem; não há base para unir ou remover qualquer um dos gates. A matriz de configuração publicada/API em `ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md` trata autorização, armazenamento, publicação e projeção buyer, portanto permanece em domínio separado.

O workflow `development-ux04-geometry.yml` está em `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, mas não existe no Product `main`; não está disponível para dispatch no SHA-alvo. Uma cópia na PR não equivale a execução em development. A matriz integral ARC-15 continua pinada em main46, e required checks permanecem UNKNOWN; esta revalidação de PR não altera contagens nem encerra a matriz geral.

## Reavaliação independente da geometria do hero — 16/11/2026

A suspeita de calibração antiga foi confrontada com os pixels da arte efetivamente usada. O SVG `lifestyle-phone-expanded.svg` está fixado pelo gate no SHA-256 `b87416e232852489fdb310896776c6362aa5eba79d8fe696254a06d4b54fca0d`; a imagem raster embutida é de `1087×1447`, mas o SVG a estica com `preserveAspectRatio="none"` ao `viewBox 1024×1536`. Comparar diretamente os pixels da imagem embutida com as coordenadas do viewBox leva a uma conclusão errada.

No canvas rasterizado `1024×1536`, a região com luminância média RGB `< 20` ocupa `[305,655)` nas linhas internas `y=900,1000,1200`. Nas colunas internas `x=480,500`, começa em `y=617` e se estende até o pixel antialiasado `y=1396`, com a transição para o fundo em `y=1397`. Isso concorda com a caixa DOM `[305,655) × [617,1396)` (`left/top/width/height = 305/617/350/779`), com tolerância vertical de 1 px na borda suavizada. A arte e o layout atuais foram aceitos visualmente; não há evidência para deslocar nem redimensionar o vídeo.

O gate em `main@efc40584` ainda só compara DOM e calibração. A Draft Product [#278](https://github.com/EAKerber/MobiliPresenter2D/pull/278), head `69b98cbd2466338574068898f7755e1f6f68b852`, adiciona scans de pixels independentes ao mesmo arquivo e mantém as quatro larguras responsivas. No SHA exato, os workflows Mobile browser (run `43983142231`) e Current asset gates (run `43983142255`) passaram; o passo “Verify home hero phone screen alignment” também passou. A mudança toca apenas o teste, não o runtime; não altera as coordenadas. Esta evidência corrige a hipótese inicial de leitura do JPEG sem transformação do SVG e confirma a calibração atual.

O gate não renderiza o iframe real do YouTube e ainda não cobre o controle próprio nas duas páginas nem a transição fullscreen; esses contratos seguem como lacunas separadas. Nenhum teste foi removido. Product está temporariamente em 6 refs (soft cap 5) enquanto a PR #278 permanece aberta; reavaliar após integração, sem remoção por contagem.
