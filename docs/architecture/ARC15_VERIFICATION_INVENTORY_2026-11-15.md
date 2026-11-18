# ARC-15 — Inventário de verificações do Produto

**Estado:** primeira passada e parecer Common Sense Judge dos oito itens sem invocação localizada concluídos sobre a baseline Product main46; três overlaps adicionais classificados; quatro grupos de decisão do owner e matriz integral assertion→risco→rota/estado ainda pendentes.
**Fonte:** primeira passada em `EAKerber/MobiliPresenter2D` `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`; não representa o inventário pós-#275.
**Revalidação live (16/11/2026):** Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` foi conferida. Os oito artefatos revistos e `candidate-assets.yml` têm blobs idênticos entre essa main e `main46`, então os pareceres continuam aplicáveis sem mover a baseline histórica.
**Método:** leitura dos contratos, comandos, gatilhos e áreas cobertas; classificação por risco/assertion/rota/estado, não por quantidade de arquivos.  
**Execução:** nenhuma suíte foi executada na primeira passada ou na reconciliação de 16/11. Nenhum teste ou workflow foi alterado; branches de PR ficaram fora da baseline main46.

**Reconciliação pós-#275:** a baseline acima permanece pinada em main46. Um recorte independente e não executado de configuração publicada, API, leitor buyer e workflows foi documentado em [matriz ARC-15 main64](ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md). Esse incremento não atualiza a contagem nem a matriz integral dos 21 workflows/21 comandos.
**Incremento de triagem — gate de teclado pós-#277 (16/11/2026):** a PR #269 levou à revisão da falha de Tab em `/config/`. Antes da instrumentação, a asserção e o código do Configurador eram iguais na `main` e na candidata; o CSS da PR atua apenas no header público. O gate usa V5 loopback derivado dos defaults, com checkbox do primeiro módulo habilitado. A falha em `6651342` ocorreu uma vez e o rerun do mesmo SHA passou. No head `8c77350b`, 12/12 Actions passaram após o teste confirmar o foco inicial e manter a expectativa original de Tab para o botão de inspeção. Classificação provisória: falha intermitente/diagnóstico insuficiente do gate, sem evidência de regressão funcional. Este caso é evidência de PR, não altera a matriz de assertions pinada em main46 nem a contagem dos 21 comandos/workflows.


## Addendum live — 18/11/2026 (BRT)

Esta atualização não altera a baseline histórica `main46` nem as contagens dos 21 workflows/21 comandos.

### Replay de vidro

A antiga pendência de corrigir a rota/fixture já foi atendida na PR #280, ainda Draft, head `bf685e22338597f47d240c616473085d86a22cb8`. O replay abre o Configurador `/config/` em loopback local; o Mobile Browser #802 passou 256 estados, conferiu quatro capturas e registrou zero erros. Os seis workflows associados ao head passaram. TST-007 continua `in_review`; GIT-017 continua aguardando integração e readback pós-merge. A faceta vertical translúcida no caso `module-05-off` fica como observação visual, sem baseline que a classifique como regressão ou aprovação estética.

### Contrato de tema e cobertura

A leitura estática de Product `main@efc40584` confirmou que `ui-theme-contract.cjs` exige os mesmos query versions de JS e CSS em todos os shells, embora Viewer use `viewer-nav005-p1` no JS e Config/Admin/Gerenciar acessos usem `private-header-nav005-v2` no CSS. Esses valores parecem cache-busters por shell; o teste ainda não foi executado e não há requisito demonstrado de igualdade de versão. Além disso, `tests/ui-theme-contract.cjs` não é invocado pelo `app/npm test`, apesar do workflow `candidate-assets.yml` ter triggers amplos.

TST-015 segue pendente. Lote proposto: verificar pathname correto e ordem de carga, preservar assertions semânticas de tema e outras assertions que já cobrem Landing/Viewer, chamar o teste no workflow adequado e executar no SHA exato. Igualdade de query version só deve permanecer se for confirmada como contrato de release.

Os cinco checks técnicos de máscara, pixels e stone também não são invocados por `candidate-assets.yml`. O workflow já acorda para `app/**`, `review-assets/**`, `tools/**` e `tests/**`; um passo agregado seria simples, porém herdaria esses triggers amplos. A decisão de wiring continua aberta para evitar nova branch/workflow sem comparar custo real, e qualquer CI verde mantém `semanticReview=PENDING` e `status=REVIEW`.
## Atualização live pós-#281 — 18/11/2026 (BRT)

Esta atualização acrescenta evidência de uma PR Draft; não muda a baseline histórica `main46`, as contagens de base ou qualquer estado semântico do runtime.

### TST-015 — contrato de tema

A PR Product [#281](https://github.com/EAKerber/MobiliPresenter2D/pull/281), head `b0119376bbeb08ec98e07abce9c3c3194376e7ec`, corrige a comparação incidental de query versions, exige atributos reais `src`/`href` e folha `rel="stylesheet"`, preserva ordem de carregamento e valida as oito páginas HTML que carregam o tema, inclusive a confirmação pública de acesso. Mantém os testes VM de modo automático, preferências explícitas, persistência, mudança do sistema e variante de logo; o contrato da ilustração agora corresponde ao frame normalizado atual. O script foi ligado ao `app/npm test`.

No SHA exato, App build purity, Current variant fidelity, Current asset gates, Mobile browser, Summary pricing browser e Stone browser passaram; o Deploy Preview passou. O gate de tema verifica código e estado VM, mas não mede o alvo de toque no navegador nem exercita foco, duplicação e posição em todos os shells reais. **TST-015 continua `in_progress`**, não concluído.

### Máscaras e custo de CI

No mesmo head, `tests.test_mask_semantics` e `tests/validate-exposed-side-pixels.py` passaram no workflow existente `candidate-assets.yml`. O passo roda depois do upload do artefato para preservar a evidência anterior e agrega os dois resultados sem pular o segundo check se o primeiro falhar. Nenhum workflow novo foi criado. O artefato atual tem 49.335.991 bytes; os filtros amplos `app/**` e `tests/**` fazem mudanças do lote repetirem toda a suíte de assets. Registrar esse custo real no MD-004, sem concluir redundância só pela repetição.

### Stone tests — fonte atual versus outputs pendentes

Os testes `test_stone_backing`, `test_stone_cleanplate` e `test_stone_surface_masks` não foram ligados ao workflow. Seus checks de origem estão pinados em `d324eb0`; a main incorpora mudanças de fonte da PR #35, incluindo composição/bridges, overlays e camadas. A PR #35 sustenta a fonte atual como arte já corrigida, mas não aprova os novos derivados de stone backing, cleanplate e surface masks. Os metadados derivados continuam `status=REVIEW`, `semanticReview=PENDING` ou `runtimePromoted=false`. É necessário regenerar os outputs e revisar as diferenças visuais; alterar hashes isoladamente poderia converter drift em falso aceite. Nenhum hash, golden ou estado semântico foi atualizado neste lote.


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

| `app/tools/test-v5-normal-save.js:93–97` ↔ `app/tools/test-v5-publication-migration.js:96–99` | Ambos cenários verificam os mesmos quatro códigos de falha de CAS/ETag/readback: `source_etag_conflict`, `write_etag_missing`, `readback_etag_mismatch` e `readback_digest_mismatch`; os mocks também usam leitura strong e escrita condicional. | **Assertions compartilhadas, cenários distintos.** O save parte de V5 já publicado; a migração parte de V3 e exige digest/candidate. Mocks não comprovam o provider. Preservar ambos. |
| `app/tools/test-core.js:512–528,588–632` ↔ `tests/summary-pricing-browser.cjs:77,96–112` | O unitário cobre totais globais e cenários com zero/um módulo; o browser verifica linha única de rodapé, total sincronizado e delta exato ao alternar serviço. | **Overlap parcial entre camadas.** Cálculo/alocação e resumo/interação DOM são garantias próprias; preservar ambos. |
| `tests/flow-layout-browser.cjs:251–252,310` ↔ `tests/keyboard-browser.cjs:206–216` | Os dois comparam sections renderizadas com a ordem do flow normalizado; o gate de teclado também reordena o DOM antes de verificar a ordem semântica. | **Modelo compartilhado, contratos distintos.** Renderização/layout e descoberta/navegação por teclado são superfícies diferentes; preservar ambos. |

**Triagem ARC-15 (16/11/2026):** âncoras verificadas por leitura estática de Product `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`. Os overlaps listados não provam redundância de arquivo; nenhuma suíte foi executada ou alterada, e as contagens do baseline permanecem 21 comandos e 21 workflows.

### Revisão focal de `app/tools/test-core.js` — sobreposição por camada (16/11/2026)

Leitura estática dos blocos de `test-core.js` no pin main46; nenhum teste foi executado. Os pares abaixo repetem alguns inputs ou invariantes, mas protegem camadas/saídas diferentes.

| Par | Interseção observada | Contratos exclusivos e disposição |
|---|---|---|
| `test-core.js:45–53` ↔ `tests/exposed-sides-glass.cjs:12–22` | Visibilidade do vidro temperado não depende dos módulos e acompanha seleção global. | `test-core` dá prova rápida de estado/resolvedor; o browser pretende percorrer 256 combinações e verifica DOM, ARIA, z-order e capturas. Manter ambos; o segundo permanece fora da CI até corrigir rota/fixture. |
| `test-core.js:206` ↔ `test-administration-v5.js:214–220` | Percentual inválido para regra de preço-base deve ser rejeitado. | Validação do tipo de regra vs propagação pelo documento V5; manter ambos. |
| `test-core.js:270–316` ↔ `test-administration-v5.js:100–101,264–268` | Ausência/null e preservação de cor em materiais de pedra. | Normalização V3/V3 corrente vs conversão/projeção V5; manter ambos. |
| `test-core.js:235–246` ↔ `test-published-configuration.js:47–57` | Visibilidade inicial do Configurador e do Viewer é preservada. | Normalização local mantém campos independentes e migração antiga; a projeção buyer expõe `viewerEntities` e omite configuração interna; manter ambos. |
| `test-core.js:781–881` ↔ `test-flow-layout.js:45–88` e `flow-layout-browser.cjs:230–252,310–385` | Ownership/ordem de slots e seções do fluxo. | Guards de markup/fonte, modelo fail-closed e DOM renderizado verificam níveis distintos; manter os três contratos. |
| `test-core.js:905–972` ↔ `mobile-pip-main-browser.cjs:30–143,165–209` e `flow-layout-browser.cjs:113–161` | Disponibilidade por perfil, dock/PiP e folga de rolagem. | Guardas de implementação preservam a política; browsers medem bounds e exercitam pin, resize, drag, transparência e foco; manter ambos os níveis. |

**Parecer do juiz:** a contagem não mostra excesso de testes inteiros. Há sobreposição parcial em preço, visibilidade, vidro, flow e PiP, principalmente entre unitários/source guards e browser; as camadas acrescentam garantias verificáveis. `test-core.js` mistura domínios e guards literais, então sua divisão é dívida de legibilidade, não correção necessária para eliminar duplicação. Preservar o arquivo/suíte neste lote; só decompor quando uma mudança concreta de ownership/manutenção justificar mover fixtures e assertions.

## Repetição de precondições e infraestrutura

Fixtures V5 válidas, preflight `ok`, e protocolo dos mocks Blob (`key="published"` e consistência strong) aparecem em vários testes; são precondições e boilerplate dos test doubles, não equivalência dos cenários de migração, leitura, save, projeção e segurança. Também há repetição de build/`pages:check` em workflows públicos; isso é infraestrutura repetida, enquanto os browsers de foco, diferencial do header, preço e tokens verificam contratos diferentes.


Além das precondições comuns, `tests/ci/prepare-local-v5-browser.sh` é chamado pelos workflows `flow-layout-browser.yml:55–64`, `keyboard-browser.yml:51–60`, `mobile-browser.yml:38–47` e `summary-pricing-browser.yml:46–55`. Ele inicia `tests/ci/local-buyer-config-server.mjs:21–29,45–48,65–67` para fixture V5/loopback. É infraestrutura compartilhada, não assertion duplicada nem prova de integração com Blob/Netlify.

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
3. `public-routing-before-clerk.yml` observa `tests/public-*.cjs`, o que inclui `tests/public-pages-integrated.cjs`, mas não o executa. O arquivo depende da fixture sentinela da PR #180, fechada sem merge; manter como replay histórico/manual e não reativar o plugin antigo. Só criar fixture nova, isolada e read-only se o owner voltar a exigir a prova API publicada→Viewer.
4. `viewer-base-price-contract-gate.yml` executa testes unitários e browser, mas está em `push` para `main`/branch de integração e `workflow_dispatch`; não há trigger de PR.

## Parecer por arquivo sem invocação localizada

| Arquivo | Evidência examinada | Leitura do juiz | Pendência concreta do owner |
|---|---|---|---|
| `tests/public-pages-integrated.cjs` | E2E Playwright de Preview que depende de sentinela/fixture exclusiva da PR #180 (fechada sem merge); filtro `public-*.cjs` apenas acorda o workflow, que não chama o arquivo. | Preservar como replay histórico/manual, fora do gate ativo; projeção/endpoint e smoke cobrem as outras camadas. Não reativar o plugin antigo da #180. | Nenhuma ação por padrão. Só se o owner exigir o fluxo API publicada→Viewer, decidir criar fixture nova, isolada, read-only e independente da #180. |
| `tests/ui-theme-contract.cjs` | Node+VM: modos auto/claro/escuro, sincronização com preferência do sistema e storage, troca de logo e alvo de toque nominal de 44 px; também cobre landing, navegação, CTA, comparação e imagens. Uma checagem estática na linha 19 espera o mesmo `ui-theme.css?v=...` em todos os shells, mas `/config/`, Admin e Gerenciar acessos usam versões de query distintas. | Preservar o contrato central de tema; os trechos não provam interação real nem alvo computado. A condição de URL uniforme provavelmente falharia no source atual, mas isso não foi observado em execução. | Antes de invocar, decidir se a query idêntica é normativa ou corrigir a asserção para aceitar revisões por shell; separar verificações não relacionadas. Candidatos de trigger: o teste, `app/core/ui-theme.js`, `app/ui-theme.css`, sete shells HTML e logos padrão claro/escuro. Acrescentar logos splash só se mantiver essa asserção. O filtro `tests/**` atual não executa o arquivo. |
| `tests/exposed-sides-glass.cjs` | Playwright `file://` abre `../app/index.html` (Home), mas exige `CASA_EM_MODULOS_DEBUG`, `.module-card`, `#viewer`, serviço de vidro e `.layer-group`, que pertencem ao Configurador em `app/config/index.html` + `app/app.js`. Percorre 256 combinações e produz quatro capturas. | O contrato browser/ARIA/z-order é distinto e útil; a entrada está errada e `file://` não atende ao `<base href="/">` nem aos assets/API raiz do Configurador. Não é gate válido e deve permanecer fora da CI até corrigir alvo e modo de servir. | Candidato já existente: `tests/ci/local-buyer-config-server.mjs` serve `/config/`, assets de `app/`, resposta anônima e payload V5 local derivado dos defaults. Ele permite exercitar rendering local, mas declara não substituir Blob/configuração publicada. Corrigir o harness para usar servidor loopback e teardown controlado; confirmar os seletores/capturas antes de decidir gate path-specific ou replay manual. |
| `tests/test_mask_semantics.py` | Confere suporte alfa de sete máscaras contra dados técnicos e bytes da máscara inline M02. | Check técnico leve e distinto dos replays de geração. Preservar. | Recomenda-se job de asset por paths exatos: teste, `app/data/technical-data.json`, `app/data/mask-data.js`, `app/assets/kitchen/masks/**`, `tools/requirements.txt`; ou replay manual. |
| `tests/test_stone_backing.py` | Replay de backing/donor em oito estados; exige hash/zero diffs fora da máscara e mantém `semanticReview=PENDING`. | Útil como prova técnica reproduzível, sem aprovação semântica. Preservar o estado pendente. | Recomenda-se job por paths do teste, `tools/build_stone_backing.py`, `tools/materialize_stone_cleanplate.py`, manifest/cases de variante, scene-data/core, `app/assets/kitchen/**`, `review-assets/stone-backing/**`, `review-assets/stone-components/generated/**` e requirements. Alternativa: replay manual; nunca promover `semanticReview`. |
| `tests/test_stone_cleanplate.py` | Valida hashes do cleanplate/composição, máscara de remoção, roundtrip e superfícies aceitas; o metadado mantém `semanticReview=PENDING`, mas o teste não o asserta. | Cobertura de replay técnico distinta; não transforma estado pendente em aceite visual. Preservar. | Paths candidatos: teste, `tools/materialize_stone_cleanplate.py`, `app/assets/kitchen/composicao-completa.png`, `review-assets/stone-cleanplate/**`, `review-assets/stone-masks/generated/**` e requirements. Se automatizar, o estado semântico precisa continuar em fonte separada. |
| `tests/test_stone_surface_masks.py` | Confere landmarks, máscaras reproduzíveis/disjuntas dentro do alpha owner, bridges que exigem ambos os hosts e source-hash drift; configuração marcada `status=REVIEW`. | Contrato técnico próprio de máscaras/hosts; status REVIEW não é aprovação semântica. Preservar. | Paths candidatos: teste; `tools/build_stone_surface_masks.py`, `build_approved_stone.py`, `review_drainer_clean.py`, `render_variant_fidelity.py`; composição, duas variantes e duas bridges stone; `review-assets/stone-masks/{config.json,generated/**}` e requirements. Preservar `status=REVIEW`. |
| `tests/validate-exposed-side-pixels.py` | Pixel smoke de bounds/pontos para vidro, coifa e pedras com oito assertions aproximadas. | Complementa browser glass e validadores de arte; não é coberto por eles. Preservar. | Recomenda-se gate leve pelos paths do teste, `overlays/tempered-glass.png`, `layers/05_aereo_fogao.png`, `layers/02_inferior_fogao.png`, as duas variantes stone expostas e requirements; ou replay manual. |

**Disposições Common Sense Judge (leitura estática, sem editar ou executar):** manter `public-pages-integrated.cjs` como replay histórico/manual; não há decisão agora salvo se o owner exigir novamente API publicada→Viewer. Quatro escolhas concretas permanecem: (1) hashes/selectors e invocação path-scoped de `ui-theme-contract`; (2) corrigir primeiro a rota/fixture do browser glass e depois decidir gate path-scoped versus capturas manuais; (3) invocar automaticamente checks leves de máscara/pixels por paths exatos ou manter replay manual; (4) job stone path-scoped ou replay manual, sempre preservando `semanticReview=PENDING`/`status=REVIEW`. Nenhuma recomendação remove um teste ou altera workflow.
**Matriz de paths e fricção de CI (proposta, não implementada):** os cinco checks Python acima têm fontes e assets próprios. `candidate-assets.yml` usa filtros workflow-wide `app/**`, `review-assets/**`, `tools/**`, `tests/**` e um job único; inserir esses comandos ali faria todos rodarem em mudanças de testes alheias. Preferir uma via de asset com filtros estreitos e jobs/condições por família, ou guardas por diff de paths. O `exposed-sides-glass.cjs` fica excluído até resolver a rota Home vs Configurador.

## Revalidação do controle próprio de tela cheia — PR #277 (16/11/2026)

**Estado integrado.** A PR [#277](https://github.com/EAKerber/MobiliPresenter2D/pull/277) foi integrada como Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` (head `1d1f68a19836830f071a153e1a3ee11ca1446410`). Em ambas as páginas, o botão sobreposto usa “Abrir vídeo em tela cheia” no estado embutido e “Sair da tela cheia” no estado expandido; `aria-label`, `title` e `aria-pressed` acompanham o estado, e o próprio botão solicita/encerra a tela cheia.

- A Home aplica fullscreen ao contêiner `.hero-phone-player`; “Como funciona” aplica ao `.video-embed`. A interação e o rótulo são equivalentes por requisito, mas os alvos e a composição pertencem a cada página. A leitura estática não estabelece benefício de extrair uma abstração compartilhada.
- A descrição da PR registra exercício manual de entrada e saída nas duas páginas na Deploy Preview #277; o head `1d1f68a` teve 11/11 workflows e Deploy Preview success. As nove paths alteradas não incluem teste nem workflow novo. Isso confirma a rodada manual daquele head, não uma asserção automatizada de fullscreen.
- A verificação geométrica do telefone e o browser de navegação pública cobrem outras garantias; não provam a visibilidade/encaixe do controle, mudança de rótulo, `aria-pressed`, entrada/saída ou Escape. A PR #274 já registra esses valores e a proveniência no inventário ARC-13 pós-#277.
- **Disposição:** apresentação visual aprovada e interação exercitada manualmente; cobertura automática específica de fullscreen permanece ausente/UNKNOWN. Se for priorizada, o gate deve cobrir os dois alvos, visibilidade dentro do vídeo, abrir, fechar pelo mesmo controle, Escape e sincronização do nome/estado. Não somar isso aos 21 comandos/workflows do baseline main46 nem tratar um run verde genérico como essa prova.

## Decisões e pendências

A consulta de branch protection do Produto não pôde ser lida nesta sessão (HTTP 403 da integração). O conjunto de required checks permanece **UNKNOWN**; sucesso de workflow, isoladamente, não prova que um check seja obrigatório.

| Disposição | Estado |
|---|---|
| Excluir testes por alta contagem ou semelhança de nomes | **Não recomendado.** Nenhum teste foi provado redundante no nível do contrato. |
| Consolidar chamadas repetidas de testes | Candidato de CI: compartilhar definições de job para `npm test`, `public-cutover-contract.cjs` e outros arquivos chamados em mais de um workflow. Executar e publicar status em cada SHA aplicável; preservar as garantias adicionais e required checks de cada fluxo. |
| Consolidar `public-cutover-contract.cjs` | Candidata a workflow reutilizável; executar separadamente para cada head e preservar os três gates de integração específicos e seus status. |
| Dispor oito arquivos sem chamada localizada | Parecer individual concluído. Default: preservar `public-pages-integrated.cjs` como histórico/manual. As quatro escolhas listadas acima permanecem pendentes; nenhum arquivo é candidato a exclusão. |
| Alinhar path filters, comandos e PR trigger | As quatro discrepâncias concretas seguem para disposição por contrato: decidir invocação/intenção de ARC03C, candidate-assets, public-routing e viewer-base-price; path trigger sem chamada não conta como execução. Preparar mudanças apenas após os paths e owners estarem explícitos. |
| Fechar ARC-15 | Parecer individual dos oito itens concluído e três overlaps adicionados; faltam a matriz integral assertion→risco→rota/estado, as quatro escolhas de disposição, intenção dos quatro triggers divergentes e required checks (UNKNOWN/403). |

**Resultado desta passada:** os 21 workflows e 21 comandos da suíte `app` seguem como baseline main46; houve leitura estática de oito arquivos sem invocação, três pares adicionais de overlap e uma fixture V5 loopback compartilhada. Nenhum teste foi provado redundante, removido, alterado ou executado. `candidate-assets.yml` inicia em mudanças de `tests/**`, mas seu comando não executa os seis artefatos por isso. Permanecem a matriz integral, quatro escolhas do owner, quatro divergências trigger→invocação e required checks (UNKNOWN/403).

## Delta após PR #277 — gate geométrico do hero (16/11/2026)

**Pin e evidência.** Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` inclui as alterações de #275 e #277. O arquivo [`tests/home-hero-phone-geometry-browser.cjs`](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/tests/home-hero-phone-geometry-browser.cjs) é uma nova verificação no delta após main46; blob `9630d2272d39a4c962a66ac1d29b263a84e59e53`. O workflow [Mobile browser](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/mobile-browser.yml), blob `2c1e379faf6e7105ac5f711060d46da7cede2d6a`, continua sendo um dos 21 workflows; o delta adicionou o passo ao fluxo existente, não um workflow YAML adicional.

O run PR [#43799448351](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448351) terminou com sucesso. O job rodou no merge ref sintético `eaf821d54c0c015d7a1a96d376be7f6ea30eecf3` (PR #277 sobre `2cb63cbf`); o passo 7, “Verify home hero phone screen alignment”, passou e produziu `HOME_HERO_PHONE_GEOMETRY_PASS` em 390, 516, 1024 e 1366 px. Os retângulos medidos foram, respectivamente, `206.14×458.83`, `206.14×458.83`, `206.14×458.83` e `252.23×561.42` CSS px. [Artefato do run](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448351/artifacts/14195552207).

**O que a verificação cobre.** Ela exige que as páginas autoral e publicada usem `data-screen-left/top/width/height = 305/617/350/779`; compara o retângulo CSS com essas coordenadas do `viewBox 1024×1536` escaladas pela largura real da arte; mantém a tela dentro do recorte da arte; verifica o recuo de 2 px do player, o preenchimento da mídia/poster, o play central e um viewport de pelo menos 200 px. Também fixa hashes da arte `lifestyle-phone-expanded.svg` e do poster, e confere os controles nativos e a ausência de política forçada para legendas. O asset expandido é uma adição pós-main46, não o desenho antigo.

**Limites importantes.** O gate confirma que o DOM acompanha a calibração escolhida, mas não demonstra que as coordenadas escolhidas coincidem com a borda física do visor: não faz comparação de pixels da moldura nem revisão automatizada da captura. A página é servida localmente; o teste bloqueia origens externas, então não renderiza o iframe/Shorts real. Também não verifica o retângulo/visibilidade do controle sobreposto `heroPhoneFullscreen`, a entrada/saída da tela cheia nem a página “Como funciona”. Essas interações foram revisadas manualmente no Preview #277, fora deste gate. Logo, um pin geométrico incorreto ainda pode passar; esta é uma regressão de alinhamento DOM, não uma prova visual/funcional completa.

**Parecer do ARC-15:** manter esta verificação como gate de geometria responsiva; classificá-la como parcialmente sobreposta ao browser/artefato visual, não redundante. Para fechar a lacuna, uma assertion focada deve conferir bounds/visibilidade dos controles próprios nas duas páginas e a transição de estado fullscreen; a confirmação do encaixe arte→visor continua exigindo julgamento visual ou uma referência de pixels aprovada. Nenhum teste foi removido, executado ou alterado neste lote documental. Esta revisão não recalcula as contagens/21 comandos da suíte `app` e não fecha a matriz integral assertion→risco→rota/estado.

## Revalidação live — gate de teclado e limites de cobertura (16/11/2026)

Product `main` permanece em `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`. A PR #269 foi reconciliada sobre essa base; o head atual é `28b1e2ef4f62b418110ba7694a59dee95969174b`, com 18 caminhos, Preview success e 12/12 workflows Actions verdes. A PR permanece Draft.

**Diagnóstico do teclado.** O workflow usa fixture V5 local derivada dos defaults. O primeiro módulo `module-01` está habilitado; o DOM posiciona o checkbox imediatamente antes do botão de inspeção. A primeira tentativa no head anterior `6651342` falhou em `tests/keyboard-browser.cjs:126`, mas o rerun do mesmo SHA e job passou. O diff de runtime da PR não altera o Configurador; a mudança em `app/ui-theme.css` vale somente para o header público e não muda a rota `/config/`. A evidência não mostra regressão funcional da PR e classifica o sinal anterior como intermitente/insuficientemente diagnosticado.

A mudança de teste em `8c77350` confirma que o checkbox está habilitado e que recebeu foco antes de Tab; mantém a expectativa original de foco no botão de inspeção e imprime o elemento ativo caso a asserção falhe. O gate passou no head exato. Nenhum runtime foi alterado nem a expectativa de navegação foi removida.

**Fronteira dos gates de navegação.** Os dois fluxos abaixo compartilham padrões gerais de teclado/foco, mas cobrem superfícies e riscos diferentes:

| Gate / fonte | Superfície e garantia principal | Relação |
|---|---|---|
| `tests/keyboard-browser.cjs` — Keyboard browser, V5 loopback | Configurador e Admin; atalhos de módulo, checkbox→inspeção, fechar/restaurar foco, navegação de etapas, rolagem e revelar senha. | Exclusivo para a configuração e estados locais V5; não cobre menu público. |
| `tests/ci/public-navigation-semantic-browser.mjs` — NAV-005 public header browser | Header público e Viewer; abrir/fechar menu, sequência de foco e CTA, redimensionamento, skip link e cards econômicos em Chromium/WebKit. | Exclusivo para navegação pública e Viewer; não valida o foco checkbox→inspeção no Configurador. |

Enter, Escape e padrões gerais de foco são interseções de implementação, não garantias duplicadas. Rotas, elementos, estados e fixtures diferem; não há base para unir ou remover qualquer um dos gates. A matriz de configuração publicada/API em `ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md` trata autorização, armazenamento, publicação e projeção buyer, portanto permanece em domínio separado.

O workflow `development-ux04-geometry.yml` está em `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, mas ainda não existe no Product `main`. A PR Draft isolada [#279](https://github.com/EAKerber/MobiliPresenter2D/pull/279), head `ffa288d181f0c53148e5a6b9ba69d3d8a5631651`, adiciona somente o arquivo original (blob `96703ca3ae3c195153f10742134dca7aa69b0faf`) e não executa o gate. Após eventual integração e autorização, revalidar o SHA de development imediatamente antes do dispatch. Product está em 7 refs, duas acima do soft cap 5; a branch #279 foi criada após avaliar a separação de escopo e não deve ser removida por contagem. A matriz integral ARC-15 continua pinada em main46, e required checks permanecem UNKNOWN; esta revalidação de PR não altera as contagens dos 21 comandos nem encerra a matriz geral.

## Reavaliação independente da geometria do hero — 16/11/2026

A suspeita de calibração antiga foi confrontada com os pixels da arte efetivamente usada. O SVG `lifestyle-phone-expanded.svg` está fixado pelo gate no SHA-256 `b87416e232852489fdb310896776c6362aa5eba79d8fe696254a06d4b54fca0d`; a imagem raster embutida é de `1087×1447`, mas o SVG a estica com `preserveAspectRatio="none"` ao `viewBox 1024×1536`. Comparar diretamente os pixels da imagem embutida com as coordenadas do viewBox leva a uma conclusão errada.

No canvas rasterizado `1024×1536`, a região com luminância média RGB `< 20` ocupa `[305,655)` nas linhas internas `y=900,1000,1200`. Nas colunas internas `x=480,500`, começa em `y=617` e se estende até o pixel antialiasado `y=1396`, com a transição para o fundo em `y=1397`. Isso concorda com a caixa DOM `[305,655) × [617,1396)` (`left/top/width/height = 305/617/350/779`), com tolerância vertical de 1 px na borda suavizada. A arte e o layout atuais foram aceitos visualmente; não há evidência para deslocar nem redimensionar o vídeo.

O gate em `main@efc40584` ainda só compara DOM e calibração. A Draft Product [#278](https://github.com/EAKerber/MobiliPresenter2D/pull/278), head `69b98cbd2466338574068898f7755e1f6f68b852`, adiciona scans de pixels independentes ao mesmo arquivo e mantém as quatro larguras responsivas. No SHA exato, os workflows Mobile browser (run `43983142231`) e Current asset gates (run `43983142255`) passaram; o passo “Verify home hero phone screen alignment” também passou. A mudança toca apenas o teste, não o runtime; não altera as coordenadas. Esta evidência corrige a hipótese inicial de leitura do JPEG sem transformação do SVG e confirma a calibração atual.

O gate não renderiza o iframe real do YouTube e ainda não cobre o controle próprio nas duas páginas nem a transição fullscreen; esses contratos seguem como lacunas separadas. Nenhum teste foi removido. Product está temporariamente em 6 refs (soft cap 5) enquanto a PR #278 permanece aberta; reavaliar após integração, sem remoção por contagem.

## Retomada do replay de vidro — 17/11/2026

**Atualização posterior à triagem estática.** A PR Draft [#280 do Produto](https://github.com/EAKerber/MobiliPresenter2D/pull/280), head `ab2d378555afc96557a332cbb33c531c8133922f`, corrige `tests/exposed-sides-glass.cjs`: substitui o alvo `file://app/index.html` (Home) pelo Configurador `/config/` servido em loopback e aguarda o estado V5 `validated`. O teste pode iniciar `tests/ci/local-buyer-config-server.mjs` em porta efêmera, confirma API anônima e encerra browser/servidor em todos os caminhos. O helper agora anuncia a porta efetiva e tem encerramento gracioso.

O arquivo foi ligado ao workflow Mobile browser com filtros por caminho existentes; a execução ocorre somente quando o alvo é a fixture local padrão, e é pulada para um URL externo fornecido por dispatch. As quatro capturas seguem como artefato. Este arranjo é uma proposta de gate local do renderer, não uma asserção de configuração publicada. Não prova Blob, autenticação, deploy ou comportamento de comprador real.

**Estado da evidência:** `node --check` nos dois arquivos Node e `git diff --check` passaram. O replay não pôde ser executado localmente porque Playwright/Chromium não estão instalados nesta máquina. O primeiro run Mobile browser `44001091873`, no SHA `889a8068e6d5a8b1717aaa4c2be98fe1b5177efb`, passou com 256 combinações, sete cartões e zero erros de página. A revisão independente encontrou que a quarta captura chamada `glass-modules-02-05-on` na verdade deixava todos os módulos visíveis; logo, aquele artefato não confirma o estado descrito. O teste agora deixa ativos apenas `module-02`/`module-05` nessa captura e grava manifesto com estado dos quatro cenários, rota, viewport e versão do navegador. O novo head `ab2d3785` está aguardando rerun, portanto a correção continua **UNKNOWN/PENDING** até passar e as capturas serem revistas.

O replay conserva 256 combinações de visibilidade, sete cartões, quatro screenshots, ordem de composição vidro/módulo 05, `aria-hidden` e ausência de erros de página. A contagem base de 21 comandos e 21 workflows do primeiro inventário continua uma referência histórica; o delta #280 acrescenta um passo ao workflow Mobile browser existente, sem criar workflow YAML novo. A tarefa verifica somente o renderer em Chromium desktop com defaults locais; não prova aparência por comparação de pixels, matriz mobile, autenticação, configuração publicada nem estado de comprador real. Revisão visual/semântica das quatro capturas permanece separada do status automatizado. O Product tem agora 8 refs no total, três acima do soft cap 5; não remover branches por contagem.

## Leitura live do gate — 17/11/2026 (BRT)

O head `bf685e22338597f47d240c616473085d86a22cb8` passou no Mobile browser #802 (`44213833429`): o log declara `passed:true`, 256 casos do modelo, quatro capturas e `errors:[]`. O artefato Mobile foi enviado (`14386753961`, digest `sha256:946759d9e771bd9a36b2dddfda48df99d75d0c63efa8cc452e917287131dc9a9`). O teste agora registra a seleção dos controles e os IDs das camadas realmente visíveis, o estado renderizado do vidro, nome, navegador, rota e viewport; exige os quatro nomes esperados e distintos, e confirma os sete IDs de módulo antes de enumerar as combinações. Os outros cinco workflows acionados no mesmo head — Keyboard #436, Summary pricing #796, Stone #1007, Flow layout #423 e Current asset gates #1258 — também terminaram `success`.

Histórico corretivo: o head `889a8068` passou, mas a quarta captura não correspondia ao estado de seu nome. `ab2d3785` falhou por tentativa de atribuição direta ao estado interno protegido (`Cannot assign to read only property 'lighting-08'`). `a7e4da3` trocou a mutação pelos controles da interface e expôs que o nome não era enviado ao `page.evaluate`; a asserção falhou antes de aprovar. `bf685e2` encaminhou o nome e passou. O primeiro PASS não foi reaproveitado como evidência do estado corrigido.

Leitura manual do artefato #802: o manifesto e as quatro imagens concordam nos estados nomeados. Os sete IDs esperados aparecem no modelo; em cada captura, a seleção coincide com as camadas `.layer-group` visíveis e o vidro permanece renderizado. As quatro imagens são coerentes com `glass-all`, `glass-module-02-off`, `glass-module-05-off` e `glass-modules-02-05-on`. A terceira captura tem uma faceta vertical translúcida estreita junto à composição; sem comparação com baseline visual/pixel, fica registrada como observação para eventual revisão do renderer, não como regressão confirmada nem como aprovação estética.

Limites e pendências: a fixture é V5 local, anônima e baseada nos defaults versionados; não valida configuração publicada, autenticação, Production ou pixels contra uma referência. A fixture permanece viva entre etapas do job; a auditoria confirmou que o runner descartável encerra o processo ao fim do job e não há evidência de vazamento entre jobs. Teardown explícito nos cinco workflows consumidores continua como melhoria de higiene de TST-006, que tem escopo mais amplo e permanece em andamento; isso não bloqueia TST-007. A PR #280 continua Draft até integração e readback conforme GIT-017. O head acionou seis workflows e todos passaram; essa observação alimenta a auditoria de triggers de TST-004/MD-004, sem por si só provar duplicação ou justificar remoção de gate.
