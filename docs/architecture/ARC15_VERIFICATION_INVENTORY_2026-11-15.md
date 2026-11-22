## Readback operacional vigente — pós-#305 — 22/11/2026 (BRT)

- Pins: Product `main@2b1c70c049cdcb5e2a75fb2a970d1fd3d112cc98`; Product `development@613f28d9ee3aaa66d7bce24f772100d5f1354732`; Design System `main@cbc4e82fcb0091ae6ee9f449b9b13e226fcbab18` (base antes desta atualização documental).
- #304 e #305 foram integradas seletivamente em Product `development`; as árvores coincidem com os heads validados. Nove gates passaram em cada head; não houve deploy de produto.
- CMP-017 tem sete fatias integradas, mas o DoD do Admin segue parcial: faltam outras famílias de controles, exceções e cobertura abrangente de teclado.
- ARC-13 em `development`: 1.043 ocorrências candidatas `unreviewed`; zero erros de parsing; 420 ocorrências primárias mapeadas e zero sem proveniência; hash `E865C5944928822484B89ADF070D3B9A752A939DE0564164E6FDC6092489B700`.
- As referências técnicas `aria-describedby` permanecem no inventário com hint `non-translatable-reference`; elas não são texto de interface e ainda não têm disposição manual.
- Product tem 9 refs. #274 e NAV-005 permanecem preservadas; #301–#305 foram integradas em development. Compare: 453 commits exclusivos em development, 14 em main, base `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. A PR #290 permanece Draft/dirty; não integrar o merge global.
- A baseline histórica de 21 workflows/comandos não define required checks.

---

## Readback após a publicação da #291 — 22/11/2026

- Product `main@2b1c70c049cdcb5e2a75fb2a970d1fd3d112cc98`; `development@188f5074f60dc35df7aa8c673dbac4a2249813be`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.
- A PR #291 foi integrada à main e a Production está pronta no deploy Netlify `6b033828fda9e5b6e8ced61b`; os quatro gates pós-merge passaram.
- A integração promoveu a ferramenta e o inventário ARC-13 como candidato não revisado; não aprova textos como catálogo nem conclui LOC-002…008.
- #274 segue Draft e preserva material exclusivo para triagem. #290 permanece inadequada para sincronização integral.
- A divergência segue ampla: 14 commits main-only, 446 development-only, base `221b54b2`. Product tem 13 refs; o soft cap é 5.
- A PR #124 permanece documental e sem integração. A tabela de workflows abaixo continua histórica; required checks atuais são UNKNOWN.

---

## Revalidação operacional live — 22/11/2026

- Product `main@5b29934150a8f939057fbd3ae14fd1c1511afd03`; `development@188f5074f60dc35df7aa8c673dbac4a2249813be`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.
- #271/#281 estão integradas na main; Production está ready no deploy `6b01d6e95f50b12695984d74`.
- #297 integrou o porte seletivo do CSS da #271 e o inventário ARC-13 refeito para o HTML corrente. Os 13 gates da PR passaram; os gates pós-merge aplicáveis passaram em development.
- #298 corrigiu a referência desatualizada da main no auditor NAV-005. O gate final passou após a integração, incluindo 48 cenários de header/navegação e 20 do Viewer.
- #291 está pronta, com 12 check runs sem falha e Preview READY, mas ainda aguarda autorização explícita para alterar main.
- #274 permanece Draft e seus documentos/revisões exclusivos foram preservados para triagem; #290 não é seguro para sincronização integral.
- Product tem 13 refs, acima do soft cap 5; nenhuma ref foi excluída nesta rodada.
- A matriz abaixo continua uma baseline histórica, não inventário completo da árvore atual. Required checks permanecem UNKNOWN.

---

## Revalidação live — 22/11/2026 (BRT)

- Pins: Product main@5b29934150a8f939057fbd3ae14fd1c1511afd03; development@9e352dbd2644e4e91c8fe533f92bf0a8827a840d; Design System main@43594dc5723bffd5acb42dad1cd8ee30bcd48778.
- #271 e #281 permanecem integradas em main; Production segue no deploy 6b01d6e95f50b12695984d74.
- #293 foi integrada em development após 14 checks verdes no head de PR. O pacote não recebeu Deploy Preview hospedado. A integração não altera a contagem histórica da baseline de 21 workflows.
- #295 é uma correção de gates, não runtime: atualiza o pin de main e aguarda duas fases de layout após decode/eventos sintéticos no teste de fallback. Head atual 7d6f759337c67d0ffbb5733dfeaa294528708644; Current asset gates passou; workflow VIS-002C ainda estava em execução no último readback. Uma execução anterior falhou com mudança de altura 1246→734 px, evidência de estado inicial não assentado no WebKit; a nova execução deve confirmar o ajuste sem reduzir tolerância.
- #291 continua pendente de autorização para main; #274 segue Draft e preserva 35 caminhos exclusivos para triagem. Required checks permanecem UNKNOWN.

**Este addendum substitui somente os pins e estados operacionais acima; a matriz abaixo é baseline histórica, não inventário completo da árvore atual.**

---

# ARC-15 — Inventário de verificações do Produto

## Revalidação live — 21/11/2026, atualização após #292

- Product pins: main@5b29934150a8f939057fbd3ae14fd1c1511afd03, development@44c7cb6495540e4038717b26fb2b1e96b02571f4. A matriz tabular e a contagem de 21 workflows/21 comandos abaixo permanecem uma baseline histórica; uma enumeração integral da árvore atual ainda não foi realizada.
- #269, #271 e #281 estão integradas na main; #281 está publicada no deploy Production pronto 6b01d6e95f50b12695984d74.
- A proposta #291 (head 1f34543974ae64abd7d133baffab64f3a238953b) ainda não foi integrada. Seus gates ARC-13, autorização Buyer, assets, NAV-005 e foco de skip-link passaram; o Preview #291 está READY. Não contar seus dois workflows propostos como parte da main.
- A #292 (head ed81efc06973aa78bc874537f2c3702560c9f79e) foi integrada por squash em development@44c7cb6 após ARC-13 e Current asset gates passarem no head exato. O buffer agora tem 1.012 candidatas unreviewed, com 411/411 ocorrências das páginas principais mapeadas; esse gate não altera a contagem histórica de workflows.
- #274 continua Draft e obsoleta como port executável para a base atual; aguarda disposição após #291. #290 não é mergeável e não deve ser usado para reconciliação integral de main e development.
- O UX-04 run 44838594398 passou em development@be743fd98063b19be5ee0614add21b8c85fb4a85; serve àquele SHA, enquanto development hoje está em 44c7cb6. Ele não atualiza a matriz de workflows nem estabelece required checks.
- Required checks e associação de gates a Production continuam UNKNOWN.

**O delta UX-04 de 20/11 abaixo é um snapshot histórico.**

### Snapshot de delta UX-04 — 20/11/2026

- Pins atuais: Product `main@29e824e2f6c44af9c8f04fd9966ec3190f3637b8`; Product `development@be743fd98063b19be5ee0614add21b8c85fb4a85`.
- Product main agora contém 22 arquivos de workflow. A matriz detalhada de 21 workflows/21 comandos abaixo continua sendo a baseline histórica pinada em `main46`; não deve ser lida como contagem atual.
- A #279 foi integrada por squash em `main` e acrescentou somente `.github/workflows/development-ux04-geometry.yml`, blob `96703ca3ae3c195153f10742134dca7aa69b0faf`. O workflow já existe em `development@be743fd` com o mesmo blob e seus arquivos de teste/build estão presentes.
- O workflow usa `workflow_dispatch`, `contents: read`, fixture V5 local e Playwright; não pede secrets nem serviço hospedado. O run atual `44838594398` foi disparado manualmente em `development@be743fd98063b19be5ee0614add21b8c85fb4a85` e terminou `success`: `exact-archive-and-static-intent` e `live-local-browser` passaram. O artefato `development-ux04-geometry-focus-44838594398` (ID `14679149233`, 1.644 bytes, SHA-256 `ecb908825ae970d436b9bc995d9840a5416428edf82129f753345ac4421bf8f7`) expira em `2026-12-04T23:42:21Z`. A execução histórica `41344513485` em `c7c2822` permanece apenas como antecedente; o novo run é a prova vinculada ao SHA atual.
- Para futuras execuções, reler o SHA de `development` imediatamente antes do dispatch e preservar run/artefatos. Este resultado fecha somente o gate UX-04 no SHA citado; não altera a baseline histórica de 21 workflows nem define required checks.


**Estado da baseline histórica main46:** primeira passada e parecer Common Sense Judge dos oito itens sem invocação localizada concluídos sobre a baseline Product main46; três overlaps adicionais classificados. MD-004 tem agora uma amostra da main atual e uma lacuna concreta de trigger do Keyboard corrigida; o crosswalk integral assertion→risco→rota/estado e as demais discrepâncias continuam pendentes.
**Fonte:** primeira passada em `EAKerber/MobiliPresenter2D` `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`; não representa o inventário pós-#275.
**Revalidação live (16/11/2026):** Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` foi conferida. Os oito artefatos revistos e `candidate-assets.yml` têm blobs idênticos entre essa main e `main46`, então os pareceres continuam aplicáveis sem mover a baseline histórica.
**Método:** leitura dos contratos, comandos, gatilhos e áreas cobertas; classificação por risco/assertion/rota/estado, não por quantidade de arquivos.  
**Execução:** nenhuma suíte foi executada na primeira passada ou na reconciliação de 16/11. Nenhum teste ou workflow foi alterado; branches de PR ficaram fora da baseline main46.

**Reconciliação pós-#275:** a baseline acima permanece pinada em main46. Um recorte independente e não executado de configuração publicada, API, leitor buyer e workflows foi documentado em [matriz ARC-15 main64](ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md). Esse incremento não atualiza a contagem nem a matriz integral dos 21 workflows/21 comandos.
**Incremento de triagem — gate de teclado pós-#277 (16/11/2026):** a PR #269 levou à revisão da falha de Tab em `/config/`. Antes da instrumentação, a asserção e o código do Configurador eram iguais na `main` e na candidata; o CSS da PR atua apenas no header público. O gate usa V5 loopback derivado dos defaults, com checkbox do primeiro módulo habilitado. A falha em `6651342` ocorreu uma vez e o rerun do mesmo SHA passou. No head `8c77350b`, 12/12 Actions passaram após o teste confirmar o foco inicial e manter a expectativa original de Tab para o botão de inspeção. Classificação provisória: falha intermitente/diagnóstico insuficiente do gate, sem evidência de regressão funcional. Este caso é evidência de PR, não altera a matriz de assertions pinada em main46 nem a contagem dos 21 comandos/workflows.


## Addendum live — execução e integração de gates — 20/11/2026 (BRT)

Esta atualização preserva a baseline histórica `main46`, a matriz dos 21 workflows/21 comandos e as assertions existentes.

- Product `main@dc066f55`; `development@acf12c4170401ceb822526a613d89657e26c6310`. A PR #286 foi integrada em development por squash depois de 9/9 workflows únicos aprovados no head `4680ddca`. O readback confirma a ponta da branch; não há Actions run no SHA do merge, pois as mudanças são filtros de workflows.
- Product #287 segue Draft no head `26a2da331445ca2901d2851c0d37976a871ea875`, base `main@dc066f55`. Quatro gates passaram no SHA exato e o Preview #287 está READY no mesmo SHA. O diff final contém quatro workflows; o gatilho temporário de branch foi removido.
- Product #281 segue Draft no head `173cb426f623abd7010117f148a0e12ea1edab82`, reconciliada à `main@dc066f55`. Seis workflows e Preview #281 passaram no SHA exato. Revisão hospedada autenticada dos shells privados permanece sem comprovação.
- ARC-03C não foi alterado pela #287 e não foi rerun no head atual. O diagnóstico no head pai `30db98d7` passou build/fonte e divergiu da baseline `303468b4` em `/about/320/light` (`rgb(34, 33, 31)` atual vs. `rgb(0, 0, 0)`). A comparação está fazendo o que foi programado; a validade da baseline visual antiga para o estado atual precisa de reconciliação, sem afrouxar assertions nem atualizá-la por conveniência.
- Product #274 segue Draft, head `6e0ca09f`, base antiga `efc40584`; 15/15 classificações técnicas LOC-002, todos os owners `null` e destinos `hold`; quatro gates passaram no head citado.
- A amostra #286/#287 permanece ~15,7 job-min executados para 12 gates únicos, mais 18,28 min do Flow cancelado antes dos testes. É uma amostra não equivalente à baseline de 7,12 min e não sustenta remoção de testes. Required checks `UNKNOWN`.
- O Product tem 13 refs observadas, acima do soft cap 5; nenhuma ref foi excluída por contagem. A lista de branches deve ser reavaliada com preservação de proveniência.
- Próximos passos: obter revisão visual dos shells privados da #281; decidir a promoção da #287, que altera somente triggers de CI e teve 4/4 gates verdes; reconciliar baseline ARC-03C com autoridade visual, sem enfraquecer o contrato.

## Addendum live — 18/11/2026 (BRT)

Esta atualização não altera a baseline histórica `main46` nem as contagens dos 21 workflows/21 comandos.

### Replay de vidro

A antiga pendência de corrigir a rota/fixture já foi atendida na PR #280, ainda Draft, head `bf685e22338597f47d240c616473085d86a22cb8`. O replay abre o Configurador `/config/` em loopback local; o Mobile Browser #802 passou 256 estados, conferiu quatro capturas e registrou zero erros. Os seis workflows associados ao head passaram. TST-007 continua `in_review`; GIT-017 continua aguardando integração e readback pós-merge. A faceta vertical translúcida no caso `module-05-off` fica como observação visual, sem baseline que a classifique como regressão ou aprovação estética.

### Contrato de tema e cobertura

**Registro da triagem inicial, superado pela execução da #281:** na Product `main@efc40584`, `ui-theme-contract.cjs` comparava as query versions de JS/CSS como se fossem iguais em todos os shells, sem requisito demonstrado. O teste ainda não havia sido executado; a #281 corrigiu a expectativa para permitir versões por shell e ligou o contrato estático ao gate de navegador existente. A evidência atual está na seção “Atualização live pós-#281” abaixo.

**Registro superado pela #281:** naquele ponto da triagem, TST-015 ainda estava pendente e o lote proposto era corrigir pathname/ordem de carga, preservar assertions únicas, conectar o teste e executá-lo no SHA exato. Esse lote foi concluído na Product #281, head `7f107b2566b61410e6f38d6477e4873015346f00`; a prova e seus limites estão documentados na seção “Atualização live pós-#281” abaixo.

**Estado revisado após a #281:** o workflow existente `candidate-assets.yml` agora executa os checks de máscara semântica e pixels laterais, depois de preservar o artefato. Os três testes de pedra continuam fora do CI até replay e revisão visual dos derivados após o drift de fonte. Não foi criado workflow adicional; os filtros amplos ainda repetem a suíte de assets e seu custo deverá entrar na medição MD-004. CI verde continua sem alterar `semanticReview=PENDING` ou `status=REVIEW`.
## Atualização live pós-#281 — 18/11/2026 (BRT)

Esta atualização acrescenta evidência de uma PR Draft; não muda a baseline histórica `main46`, as contagens de base ou qualquer estado semântico do runtime.

### TST-015 — contrato de tema

A PR Product [#281](https://github.com/EAKerber/MobiliPresenter2D/pull/281), head `7f107b2566b61410e6f38d6477e4873015346f00`, corrige a comparação incidental de query versions, exige atributos reais `src`/`href` e folha `rel="stylesheet"`, preserva ordem de carregamento e valida as oito páginas HTML que carregam o tema, inclusive a confirmação pública de acesso. Mantém testes VM de modo automático, preferências explícitas, persistência, mudança do sistema e variante de logo; o contrato da ilustração corresponde ao frame normalizado atual. A auditoria de TST-015 identificou e manteve as assertions únicas de Landing/Viewer; não foram retiradas garantias sem substituto.

No SHA exato, App build purity, Current variant fidelity, Current asset gates, Mobile browser, Summary pricing browser e Stone browser passaram; o Deploy Preview também passou. O [Mobile browser #810](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44425086708) executou o passo TST-015 no fixture local anônimo: 16 casos, oito shells em 375×812 e 1280×900, incluindo unicidade, ordem, foco, ativação e medida do alvo. TST-015 está `done` no escopo do plano; não comprova comportamento autenticado ou configuração publicada. A pequena correção de runtime mantém DOM, ordem visual e foco de teclado alinhados em `/config/`.

### Máscaras e custo de CI

No mesmo head, `tests.test_mask_semantics` e `tests/validate-exposed-side-pixels.py` passaram no workflow existente `candidate-assets.yml`. O passo roda depois do upload do artefato para preservar a evidência anterior e agrega os dois resultados sem pular o segundo check se o primeiro falhar. Nenhum workflow novo foi criado. O artefato atual tem 49.335.991 bytes. O filtro amplo faz o mesmo diff acordar workflows diferentes; isso é sobreposição de trigger, não prova de assertions redundantes.

**MD-004 — recorte operacional observado em #280/#281 (sem alterar a baseline main46):** no SHA #280 `bf685e2`, Mobile browser (#44213833429) e Current asset gates (#44213833512) passaram dentro de seis workflows aprovados. No SHA #281 `7f107b2`, os jobs equivalentes (#44425086708 e #44425086716) também passaram; seis workflows e o Deploy Preview passaram. Ambos os workflows compartilham trigger para mudanças em `app/**`, mas cobrem camadas distintas: Mobile browser executa PiP/interações, geometria e, no alvo loopback local, o contrato de tema; Current asset gates executa unitários de assets, `app/npm test`, renderização/validadores de variantes e proveniência, além de máscara semântica/pixels laterais depois de preservar o artefato. O job de assets inclui unitários focais e `npm test`; não há evidência suficiente aqui para classificar assertions internas como redundantes. Tamanho do artefato não é proxy de duração.

**Crosswalk parcial de fan-out (18/11):** `app/**` aciona seis workflows automáticos: app-build-purity, candidate-assets, mobile-browser, stone-browser, summary-pricing-browser e variant-fidelity. Três executam `app/npm test` (app-build-purity, candidate-assets e variant-fidelity); module02-fidelity também o executa, mas é manual. Candidate-assets e variant-fidelity compartilham derivação/renderização do manifesto de variantes; summary-pricing-browser também chama `test-core.js` diretamente. A sobreposição de execução não demonstra redundância: os seis mantêm garantias distintas e nenhum teste foi removido.

**Amostra de duração — Product #269 candidato, não baseline:** no head `8701bf488e0434e98b10defa7473b22cef72238a`, os 12 workflows concluíram com sucesso. A janela por workflow foi calculada por `jobs.started_at`→`jobs.completed_at` do endpoint de jobs do GitHub, do primeiro job iniciado ao último concluído, arredondada a 0,1 minuto; a amostra contém 14 jobs, envelope de 2,6 min, mediana de 0,8 min por workflow e 11,6 job-min agregados. Inclui setup/checkout/install e não equivale a custo faturado. A tabela registra tempo de parede por workflow:

| Workflow | Minutos |
|---|---:|
| [Public routing before Clerk](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069540) | 0.1 |
| [App build purity](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069464) | 0.3 |
| [Summary pricing browser](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069446) | 0.5 |
| [Current variant fidelity](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069475) | 0.5 |
| [NAV-005 public header browser](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069731) | 1.7 |
| [Stone browser](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069581) | 0.7 |
| [Mobile browser](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069572) | 0.9 |
| [Current asset gates](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069559) | 0.8 |
| [About skip-link destination focus](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069433) | 0.6 |
| [VIS-002C P-TOKEN v0.3 product pin](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069872) | 1.4 |
| [Flow layout browser](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069437) | 1.7 |
| [Keyboard browser](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44437069577) | 2.5 |
A duração da baseline Product `main@efc40584` continua `UNKNOWN`; esta amostra de uma branch candidata não a substitui. Próximo critério MD-004: completar o crosswalk por job, comando, fixture, assertion e contrato, e repetir a medição na baseline quando houver execução compatível; mapear dependências de cada path antes de estreitar triggers. Não remover teste por contagem.

### Stone tests — fonte atual versus outputs pendentes

Os testes `test_stone_backing`, `test_stone_cleanplate` e `test_stone_surface_masks` não foram ligados ao workflow. Seus checks de origem estão pinados em `d324eb0`; a main incorpora mudanças de fonte da PR #35, incluindo composição/bridges, overlays e camadas. A PR #35 sustenta a fonte atual como arte já corrigida, mas não aprova os novos derivados de stone backing, cleanplate e surface masks. Os metadados derivados continuam `status=REVIEW`, `semanticReview=PENDING` ou `runtimePromoted=false`. É necessário regenerar os outputs e revisar as diferenças visuais; alterar hashes isoladamente poderia converter drift em falso aceite. Nenhum hash, golden ou estado semântico foi atualizado neste lote.


## Parecer Common Sense Judge

**Não há base para remover um teste ou workflow inteiro.** A leitura encontrou reexecuções do mesmo arquivo/comando em workflows distintos e alguns trechos de assertions repetidos, mas cada integração/commit ainda precisa receber sua própria execução e status. Nos pares de assertions, os testes mantêm garantias exclusivas; a sobreposição serve para avaliar eventual compartilhamento de implementação, não para concluir redundância. Os oito arquivos sem chamada localizada têm parecer individual abaixo; sua classificação técnica não substitui a decisão do owner.

O mapa agora cobre os comandos dos 21 workflows e o conteúdo dos 21 comandos de `app/npm test`, com pares de overlap identificados. Ainda não é um crosswalk integral de cada assertion por rota e estado; `test-core.js` é o principal limite semântico por seu escopo amplo. A ausência de um par exato confirmado não prova inexistência de overlap.

## Contagem localizada

O script `app/package.json → scripts.test` contém 19 scripts Node e chama ainda dois validadores Python: `tools/validate-assets.py` e `tools/validate-r5a-pixelperfect.py`. São 21 comandos encadeados na suíte da pasta `app`, não 21 workflows nem a contagem de todos os testes do repositório.

Há 21 workflows YAML no pin analisado. Os comandos variam: alguns executam a suíte completa, outros executam unitários, browser gates, validators ou verificações de produção. A contagem de arquivos não mede repetição de assertions.

## Matriz de triggers — Product main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9 (18/11/2026)

Leitura somente estática dos 21 arquivos em .github/workflows na main atual do Produto, pinada ao SHA acima. Esta tabela resume eventos e escopo dos filtros; cada link abre o workflow fonte exato, que continua sendo autoridade para a lista completa de paths. PRs não integradas podem ter comportamento diferente do pin da main. Não alterei filtros nem executei dispatch.

| Workflow | Eventos | Escopo resumido do path filter |
|---|---|---|
| [about-skip-link-focus.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/about-skip-link-focus.yml) | PR na main; push na branch de correção | Sobre/página institucional, manifesto e gate de skip link |
| [admin-hierarchy-browser.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/admin-hierarchy-browser.yml) | PR, push na main e dispatch manual | Admin, contratos de hierarquia/configuração, endpoint e três browser gates |
| [app-build-purity.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/app-build-purity.yml) | PR e push na main | app/** (filtro amplo); build e pureza do app |
| [arc03c-static-page-build-gate.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/arc03c-static-page-build-gate.yml) | push em duas branches históricas; sem PR | Fragments/páginas/gerador e páginas públicas selecionadas |
| [branch-hygiene-bounded.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/branch-hygiene-bounded.yml) | PR lifecycle; push na main | Manifesto de lote; na PR também ferramentas e testes de higiene |
| [branch-hygiene.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/branch-hygiene.yml) | PR, push na main, semanal e dispatch | Ferramentas/disposições/testes de higiene; verificação periódica |
| [candidate-assets.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/candidate-assets.yml) | PR, push na main e dispatch | app/**, review-assets, referências, tools/** e tests/** (filtro amplo) |
| [flow-layout-browser.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/flow-layout-browser.yml) | PR, push na main e dispatch | Flow/layout V5 e fixture/server local compartilhados |
| [keyboard-browser.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/keyboard-browser.yml) | PR, push na main e dispatch | Flow V5, teclado/runtime e fixture/server local compartilhados |
| [mobile-browser.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/mobile-browser.yml) | PR, push na main e dispatch | app/**, PiP/hero e fixture/server local compartilhados |
| [module02-fidelity.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/module02-fidelity.yml) | dispatch manual apenas | Replay histórico exige target_ref explícito |
| [p-comp-01-public-menu-gate.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/p-comp-01-public-menu-gate.yml) | push em branch de integração; sem PR | Header e páginas públicas selecionadas |
| [public-production-readonly.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/public-production-readonly.yml) | PR e push na main | PR: scripts do gate; main: inclui rotas públicas e função; leitura de Production |
| [public-routing-before-clerk.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/public-routing-before-clerk.yml) | PR e push na main | Rotas públicas/Viewer; PR inclui filtros mais amplos de testes |
| [r0-contract.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/r0-contract.yml) | dispatch manual apenas | Replay histórico exige target_ref explícito |
| [stone-browser.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/stone-browser.yml) | PR, push na main e dispatch | app/**, teste de pedra e fixture/server local; dispatch pode receber URL |
| [summary-pricing-browser.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/summary-pricing-browser.yml) | PR, push na main e dispatch | app/**, preço do resumo e fixture/server local; dispatch pode receber URL |
| [ux-auth-viewer-integration-gate.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/ux-auth-viewer-integration-gate.yml) | push em branch de integração; sem PR | Admin/autenticação, Viewer e gates browser associados |
| [variant-fidelity.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/variant-fidelity.yml) | PR, push na main e dispatch | app/**, referências de variantes, tools e dívida visual |
| [viewer-base-price-contract-gate.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/viewer-base-price-contract-gate.yml) | push na main/integração e dispatch | Admin, Viewer, endpoint e contratos de preço |
| [vis002c-v03-product-pin.yml](https://github.com/EAKerber/MobiliPresenter2D/blob/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9/.github/workflows/vis002c-v03-product-pin.yml) | PR na main | Conjunto explícito de CSS, páginas, fallback de imagem, pins e gates VIS-002C |

**Leitura de sobreposição e limites.** Seis workflows filtram app/**: app-build-purity, candidate-assets, mobile-browser, stone-browser, summary-pricing-browser e variant-fidelity. O cluster Browser V5 de flow-layout, keyboard, mobile, stone e summary compartilha o preparador/server local; cada gate mantém assertions de domínio diferentes. Os exemplos #280/#281 mostram triggers coincidentes com resultados verdes, mas não demonstram redundância de assertions. candidate-assets também observa tests/**, tools/** e review-assets; o filtro acorda o workflow, mas só os comandos no job provam quais testes foram executados. ARC03C, p-comp-01 e ux-auth/viewer estão restritos a branches de integração/históricas; module02-fidelity e r0-contract são dispatch-only. A presença de workflow, trigger ou check verde não prova que ele seja required; essa configuração segue UNKNOWN/403. Duração/custo também seguem UNKNOWN. Este é um mapa de triggers, ainda não o crosswalk integral workflow → job/comando → fixture → assertion → contrato.

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


Além das precondições comuns, `tests/ci/prepare-local-v5-browser.sh` é chamado por cinco workflows: `flow-layout-browser.yml`, `keyboard-browser.yml`, `mobile-browser.yml`, `summary-pricing-browser.yml` e `stone-browser.yml`. O helper inicia `tests/ci/local-buyer-config-server.mjs` para a fixture V5/loopback. **Correção de inventário em 20/11:** a lista anterior contava quatro; Stone também chama o mesmo preparador. Isso é infraestrutura compartilhada, não assertion duplicada nem prova de integração com Blob/Netlify.

| Workflow no Product `main@803c32f` | Preparação e comando(s) | Garantia principal | Gatilhos |
|---|---|---|---|
| [Flow layout](https://github.com/EAKerber/MobiliPresenter2D/blob/803c32f7c0d4a7ba86367d6290f740747b667340/.github/workflows/flow-layout-browser.yml) | Fixture V5 local; `flow-layout-browser.cjs`, `buyer-v5-browser.cjs`, `nav-flow-responsive-crossbrowser.cjs`; Chromium + WebKit | Ordem/modelo de fluxo, projeção Buyer V3/V5, invariantes de layout e navegação responsiva | Lista específica de módulos/páginas, CSS, testes e helper |
| [Keyboard](https://github.com/EAKerber/MobiliPresenter2D/blob/803c32f7c0d4a7ba86367d6290f740747b667340/.github/workflows/keyboard-browser.yml) | Fixture V5 local; `keyboard-browser.cjs`; Chromium | Atalhos, ordem das seções, foco/restauração, rolagem e estilos computados | Lista específica de módulos/páginas, `app/styles.css`, teste e helper |
| [Mobile](https://github.com/EAKerber/MobiliPresenter2D/blob/803c32f7c0d4a7ba86367d6290f740747b667340/.github/workflows/mobile-browser.yml) | Fixture V5 local para PiP; `mobile-pip-main-browser.cjs` e replay geométrico local da Home | PiP responsivo/touch e bounds da tela do telefone na arte | `app/**`, testes e helper |
| [Summary pricing](https://github.com/EAKerber/MobiliPresenter2D/blob/803c32f7c0d4a7ba86367d6290f740747b667340/.github/workflows/summary-pricing-browser.yml) | Gate de ownership, `node app/tools/test-core.js`, fixture V5 local e `summary-pricing-browser.cjs`; Chromium | Ownership de resumo/preço, totais e restauração de estimativa | `app/**`, teste e helper |
| [Stone](https://github.com/EAKerber/MobiliPresenter2D/blob/803c32f7c0d4a7ba86367d6290f740747b667340/.github/workflows/stone-browser.yml) | `node app/tools/test-runtime-contracts.js`, fixture V5 local e `stone-browser.cjs`; Chromium | Contratos de runtime e interação de pedra/rodapé | `app/**`, teste e helper |

Os cinco gates passaram na amostra da Product `main@efc40584` de 19/11 (BRT); tempos e limites estão no addendum live abaixo. O preparador comum não une as assertions. Flow layout e Keyboard mantêm listas de caminhos específicas; os outros três usam `app/**`. A lacuna de CSS do Keyboard já foi corrigida. Antes de ampliar mais os filtros estreitos, mapear cada dependência de fixture contra o contrato alvo; isso evita acionar browsers de fluxo/teclado em toda mudança de `app/**` sem evidência de que seus contratos foram afetados.

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

**Snapshot histórico pré-merge da #279:** o workflow existia em `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`; naquele momento a PR Draft adicionava somente o arquivo original e não executava o gate. A recomendação histórica era revalidar o SHA de development imediatamente antes do dispatch. Esse snapshot não representa o estado corrente pós-merge. A matriz integral ARC-15 continua pinada em main46 e required checks permanecem UNKNOWN.

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


## Addendum live — 20/11/2026 (BRT)

A contagem base de 21 workflows e 21 comandos continua sendo a baseline histórica `main46`; a medição operacional abaixo é uma amostra independente da Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` coletada em 19/11 (BRT), antes da promoção da correção de trigger. Ela não atualiza o denominador histórico nem prova redundância.

| Medida | Resultado observado |
|---|---:|
| Execuções concluídas, todas success | 12 |
| Workflows YAML distintos | 11 |
| Registros de job | 13 |
| Jobs executados / pulados | 12 / 1 |
| Tempo agregado de jobs executados | 7,12 job-min |
| Mediana de tempo de parede por execução | 0,46 min |
| Maior tempo de parede | 2,33 min — Flow layout browser |

O job pulado de `Public routing before Clerk` tem timestamps inconsistentes (início posterior à conclusão) e foi excluído do tempo agregado. O recorte de push contém 11 execuções, 11 YAMLs, 12 registros (11 jobs executados e um pulado), 6,95 job-min e mediana de 0,55 min. Esses tempos não são custo faturado.

Os cinco browser gates locais V5 tiveram um job cada: Stone 0,55 min; Summary pricing 0,60; Mobile 0,67; Keyboard 0,82; Flow layout 2,33. O total de 4,97 job-min descreve esta amostra; as assertions continuam cobrindo contratos diferentes.

### Correção de alcançabilidade do gate de teclado

No workflow `keyboard-browser.yml`, os filtros de `push` e `pull_request` não incluíam `app/styles.css`. O teste verifica bounds de foco no viewport e estilos computados de controles/shells; mudanças CSS poderiam alterar essas garantias sem acordar o gate. O caminho foi adicionado aos dois filtros, sem alterar teste ou runtime. A #282 passou no head `14277da630e50dd1cc3bccf7db60a12fb6919fda` e integrou-se à development em `ba45522eb25f9624acc7f262dbfe82f06bd82af0`; a promoção seletiva #283 passou no head `3eb61eafd2f527f1e9b6e625e3ebbd82d1abff42`, integrou-se à main em `803c32f7c0d4a7ba86367d6290f740747b667340`, e o gate pós-merge passou. PRs e refs estão linkadas no handover atualizado.

**Estado MD-004:** este subproblema está fechado. O crosswalk integral dos 21 workflows/comandos e a auditoria das demais discrepâncias de trigger continuam em andamento; nenhum teste foi removido ou consolidado.


## Recorte MD-004 — gatilhos de testes exatos — 20/11/2026 (BRT)

**Pins revalidados:** Product `main@803c32f7c0d4a7ba86367d6290f740747b667340` e `development@ba45522eb25f9624acc7f262dbfe82f06bd82af0` antes da estabilização. As duas folhas de workflow e os oito módulos Python tinham blobs idênticos nos dois pins. A amostra principal de comandos continua sendo `main@efc40584`; este recorte não redefine a baseline histórica de 21 workflows/21 comandos.

| Workflow/job | Invocação | Garantia adicional | Resultado de trigger |
|---|---|---|---|
| `app-build-purity.yml` / `current-build` | `npm run build`, verificação de pureza de `app/**`, `npm test`; replay R5A continua explícito. | Build atual reproduzível sem reescrever fontes e suíte principal do Produto. | Automático para alterações em `app/**` e no workflow; também manual. |
| `candidate-assets.yml` / `current-asset-gates` | Oito módulos Python nomeados, `app/npm test`, manifesto/render de variantes, validações de pedra, torneira, faixa, intake e proveniência. | Evidências e contratos de assets/variantes, incluindo upload do artefato. | A PR #284 substituiu `tests/**` pelos oito caminhos exatos nos filtros de PR e push; manteve `app/**`, `tools/**`, `review-assets/**`, referências e o próprio workflow. |
| `variant-fidelity.yml` / `variants` | `app/npm test`, manifesto e renderizador de variantes, resumo/artefato. | Relatório dedicado de fidelidade de variantes. | Mantidos os caminhos existentes. Não foi adicionado `tools/requirements.txt`: para alterações em `tools/**`, `candidate-assets` já executa a mesma suíte, manifesto e renderizador, além das suas validações. A expansão criaria um segundo job completo sem asserção nova demonstrada; o status obrigatório dedicado não pôde ser verificado (API de proteção 403). |
| `module02-fidelity.yml` / `module02-fidelity` | Checkout de `target_ref`, validação da referência R4 e `app/npm test`; replay R4 somente no baseline identificado. | Reprodutibilidade de checkpoint histórico. | Manual por `workflow_dispatch`; não é gate automático de PR/push. |

**Parecer sobre sobreposição:** os três workflows automáticos executam `app/npm test`, mas cada um mantém uma garantia adicional própria. A derivação/renderização de variantes também se repete entre `candidate-assets` e `variant-fidelity`; no caminho de mudança em `tools/**`, o primeiro já faz a validação e envia o resumo. A repetição de comando, sozinha, não prova redundância de assertion. Nenhum teste, comando, artefato ou garantia foi removido.

A revisão dos oito módulos confirmou a lista completa do comando, sem imports de helpers de `tests/`; dependências persistentes pertencem a `app/**`, `tools/**` e `review-assets/**`, já observados. O risco futuro é de manutenção: sincronizar os filtros sempre que o comando ganhar módulo novo ou helper compartilhado.

A PR [#284](https://github.com/EAKerber/MobiliPresenter2D/pull/284) passou no gate [Current asset gates](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44773413014) no head `7a4be85c87c78bc854710ded9e4476abd76ebb67` e integrou por squash na development `205cc83363e3ace1a0ba7d8b2b44c96c62e1d857`. A promoção seletiva [#285](https://github.com/EAKerber/MobiliPresenter2D/pull/285) passou no head `a65206834488be570a5d2e137c6e0581995ba5b5`; depois do merge, o gate [Current asset gates](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44774445854) e o [plan](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44774445852) passaram na main `dc066f55619824626ea4752ecc0bafc67f9d9110`. O check externo “Supabase Preview” aparecia `in_progress` no readback; não houve mudança Supabase, e esse estado não foi contado como evidência nem como falha.

**Estado:** este recorte resolve uma discrepância trigger→invocação e preserva o custo/garantia dos comandos. MD-004 continua em andamento até concluir o crosswalk integral e revisar os outros gatilhos.

## Addendum live — auditoria e crosswalk MD-004 — 20/11/2026 (BRT)

A baseline histórica de 21 workflows/21 comandos segue pinada em `main46`. A auditoria live de triggers compara Product `main@dc066f55619824626ea4752ecc0bafc67f9d9110` e `development@205cc83363e3ace1a0ba7d8b2b44c96c62e1d857`; o crosswalk evento → job → comando → fixture → assertion → contrato está em [MD004_WORKFLOW_CROSSWALK_2026-11-20.md](MD004_WORKFLOW_CROSSWALK_2026-11-20.md). Required checks continuam `UNKNOWN`.

A PR [#286](https://github.com/EAKerber/MobiliPresenter2D/pull/286) segue aberta e sem integração, agora no head `4680ddca92ea4cbab0366994e306d3288a4f1151`, base `development`: nove workflows YAML, 85 inclusões de caminhos e dois globs amplos substituídos. Oito dos nove gates únicos passaram no último readback; Flow layout (`44789052605`) continuava na instalação de tooling de browser, sem falha registrada. A PR não qualifica `main`.

As duas precisões adicionadas ao lote não removem testes: o filtro de roteamento usa três testes no evento PR e dois no push; o filtro de PR de higiene geral lista os três scripts Python compilados pelo job. Nenhum evento histórico foi reativado e nenhum teste foi removido.

**Estado:** crosswalk 21/21 concluído documentalmente; MD-004 permanece em andamento para o port seletivo das lacunas remanescentes à `main` — build do skip-link, dependência da projeção no smoke, fontes de preço/catálogo/cena e build do pin VIS-002C — e para uma medição de duração comparável ao pin atual. P-COMP e UX/auth continuam dormentes; ARC03C permanece dispatch-only porque as branches antigas não existem. A revisão dos overlaps não encontrou base para remover testes.
