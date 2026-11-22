Warning: truncated output (original token count: 41811)
Total output lines: 835

## Readback operacional vigente — pós-#302 — 22/11/2026 (BRT)

**Pins conferidos:** Product `main@2b1c70c049cdcb5e2a75fb2a970d1fd3d112cc98`; Product `development@f640f9018e6bc36cbf4ca79313a6576080e9ded4`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.

- #299–#302 foram integradas por squash em `development`. A #302 passou 9/9 workflows no head `6d96342250ac34dc2a945b6794e5a09c67e0cdc7`; sua árvore coincide com o merge `f640f9018e6bc36cbf4ca79313a6576080e9ded4` (`0f927c4f112222c69ed850340073c2f3c4996b24`). Sem Deploy Preview; `main` e Production não mudaram.
- CMP-017 avançou em quatro fatias: cor temática, semântica/save-readback dos estados iniciais, motivos para etapas obrigatórias/vazias e disponibilidade de acabamentos. A última fatia explica por que o último acabamento global ou a última associação local não pode ser removida. O DoD do Admin segue incompleto.
- ARC-13 em `development`: inventário determinístico com SHA-256 `1BEF3227C502FD14FBC60CEDAB9AE837CCCF7116BACC09C12084857A9C3EAD22`, 1.037 candidatas ainda `unreviewed`, zero erros de parsing e zero ocorrências primárias sem proveniência. Isso não decide conteúdo nem conclui LOC-002…008.
- ARC-13 está integrado em `main` como inventário candidato não revisado. Isso não conclui LOC-002…008 nem aprova textos de interface.
- #274 está fechada sem merge; sua branch permanece como arquivo de documentação e evidências exclusivas. #290 continua Draft/dirty, de `main` para `development`; o compare vivo tem 450 commits exclusivos em development e 14 em main. Reconciliar somente mudanças necessárias, sem merge global.
- O Product tem 6 branches: `main`, `development`, arquivo #274, buffer NAV-005 e as branches integradas #301 `codex/cmp017-admin-control-contract-20261122` e #302 `codex/cmp017-finish-availability-20261122`. As 11 exclusões autorizadas continuam confirmadas; as branches #301/#302 foram preservadas.
- DS #124 foi integrada por squash à `main` em `3408f148187c7528b9e8cf0fd7c9e30a61fe9377`; a árvore integrada coincide com o head documental `2203141db9103545cf7cc5914d8a4bf57401a361`. O pacote altera somente os três documentos listados acima; não há runtime ou deploy de produto.
- Required checks e associação de gates a deploy continuam `UNKNOWN`. Os blocos abaixo deste readback são snapshots históricos, não pins operacionais atuais.

---

## Readback após a publicação da #291 — 22/11/2026

- Product `main@2b1c70c049cdcb5e2a75fb2a970d1fd3d112cc98`; `development@188f5074f60dc35df7aa8c673dbac4a2249813be`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.
- A PR #291 foi integrada à main e a Production está pronta no deploy Netlify `6b033828fda9e5b6e8ced61b`; os quatro gates pós-merge passaram.
- A integração promoveu a ferramenta e o inventário ARC-13 como candidato não revisado; não aprova textos como catálogo nem conclui LOC-002…008.
- #274 segue Draft e preserva material exclusivo para triagem. #290 permanece inadequada para sincronização integral.
- A divergência segue ampla: 14 commits main-only, 446 development-only, base `221b54b2`. Product tem 13 refs; o soft cap é 5.
- A PR #124 permanece documental e sem integração. A tabela de workflows abaixo continua histórica; required checks atuais são UNKNOWN.

---

## Estado live — 22/11/2026

**Pins revalidados:** Product `main@5b29934150a8f939057fbd3ae14fd1c1511afd03`; Product `development@188f5074f60dc35df7aa8c673dbac4a2249813be`; Design System `main@43594dc5723bffd5acb42dad1cd8ee30bcd48778`.

- #271 e #281 estão integradas na `main`; a Production está pronta no deploy Netlify `6b01d6e95f50b12695984d74`, vinculada ao SHA `5b299341`.
- #293, #295, #296, #297 e #298 foram incorporadas seletivamente ao buffer `development`. #297 levou os ajustes CSS da #271 e regenerou o inventário após a mudança de fonte. Os 13 gates da PR passaram; o gate ARC-13 pós-merge e os gates de browser/publicação passaram no SHA corrente ou no head exato registrado.
- #298 atualizou a guarda de continuidade NAV-005 para distinguir a `main` corrente da referência histórica. A execução pós-merge `45055266232` passou, incluindo 48 cenários de navegação e 20 do Viewer.
- #291 permanece pronta para revisão: head `1f34543974ae64abd7d133baffab64f3a238953b`, base `main@5b299341`, 12 check runs sem falha e Deploy Preview READY. A integração na `main` aguarda autorização explícita.
- #274 continua Draft: preserva documentação e revisões úteis, mas o inventário está vinculado a snapshot anterior. Seus artefatos exclusivos seguem preservados para triagem; não integrar o pacote inteiro.
- #290 continua não mergeável como sincronização integral. Compare atual: 13 commits exclusivos na `main`, 446 em `development`, base comum `221b54b2`.
- O Product tem 13 branches, acima do soft cap 5. Não foram removidas refs nesta rodada; a triagem de branches integradas continua necessária e depende de autorização para alvos exatos.
- A matriz de 21 workflows abaixo é histórica; a associação atual de required checks permanece UNKNOWN.

**Próxima ordem:** (1) aguardar autorização para #291; (2) após eventual integração, verificar o SHA e o deploy de Production; (3) triar #274 e as branches integradas, preservando proveniência; (4) continuar a promoção seletiva sem sincronizar a árvore divergente inteira.

---

## Revalidação operacional live — 22/11/2026 (BRT)

**Pins:** Product main@5b29934150a8f939057fbd3ae14fd1c1511afd03; Product development@9e352dbd2644e4e91c8fe533f92bf0a8827a840d; Design System main@43594dc5723bffd5acb42dad1cd8ee30bcd48778.

- #281 e #271 seguem integradas na main; a publicação de #281 está pronta em Production no deploy 6b01d6e95f50b12695984d74.
- #293 foi integrada por squash em development@9e352db. Seus 14 checks passaram no head da PR; a PR não recebeu Deploy Preview Netlify, portanto não há revisão visual hospedada desse candidato. O pacote transporta seletivamente o hero/vídeo, tela cheia, comparativos e gate geométrico, preservando ARC-03C.
- A checagem pós-merge revelou pin estático antigo de main e uma diferença real de altura no teste de recuperação da imagem do hero no WebKit. A #295 contém somente dois arquivos de gate, está aberta em development, head 7d6f759337c67d0ffbb5733dfeaa294528708644; a execução que refresca o pin passou e Current asset gates passou, enquanto o workflow raster ainda está rodando. Uma tentativa anterior mediu 1246 px antes do evento e 734 px depois; o candidato atual espera o decode e o assentamento da geometria antes da captura inicial, sem afrouxar a comparação.
- #294 foi fechada sem merge por diff incorreto de 18 arquivos; sua branch foi preservada. A correção limpa está em #295.
- #291 segue fora de main e aguarda autorização explícita. #274 permanece Draft; manter os 35 caminhos exclusivos para triagem após decisão sobre #291. #290 continua inadequada para reconciliação integral main/development.
- O Product tem 10 refs observadas (incluindo main e development), acima do gatilho de revisão de 5; branches integradas/fechadas continuam preservadas até triagem autorizada. O Design System mantém main e a branch documental de #124.
- PR #124 continua documental e sem merge; esta atualização não autoriza sua integração. Os gates verdes da #293 não equivalem a publicação em Production.

**Próxima ordem:** (1) aguardar resultado da #295; (2) atualizar este handover e a matriz novamente com resultado exato do gate e eventual integração em development; (3) seguir a promoção seletiva para main somente após autorização; (4) triar #274 e refs excedentes sem apagar artefatos.

---

## Ponteiro operacional live — 21/11/2026 (BRT)

**Pins revalidados:** Product main@5b29934150a8f939057fbd3ae14fd1c1511afd03; Product development@44c7cb6495540e4038717b26fb2b1e96b02571f4; Design System main@43594dc5723bffd5acb42dad1cd8ee30bcd48778.

- **Publicação estável:** Product #269 (d715f8e) e #271 (9452184) estão integradas. #281 está integrada em main@5b29934; os seis gates passaram no head exato e o deploy Production da Netlify está ready em https://casaemmodulos.casa (deploy 6b01d6e95f50b12695984d74).
- **ARC-13 / #291:** PR para promoção seletiva a main, head 1f34543974ae64abd7d133baffab64f3a238953b, pronta para revisão. ARC-13 (44934586742), Buyer (44934586734), assets (44934586750), NAV-005 (44934586866) e skip-link (44934586728) passaram; o [Deploy Preview](https://deploy-preview-291--mobilipresenter2d.netlify.app) está pronto. O inventário da árvore atual registra 1.026 candidatas (unreviewed), 420/420 ocorrências das páginas principais com proveniência e hash reproduzível beb8f9e9554fca6bdf0f8f884982406a34c99d442768d4374212603ab484667e. A integração permanece pendente de autorização específica para `main`.
- **ARC-13 / #292:** integrada por squash em `development@44c7cb6`. A normalização LF mantém offsets ARC-03C estáveis; o inventário do buffer segue com 1.012 candidatas `unreviewed`, 411 mapeadas e zero sem proveniência. A geração repetida, ARC-03C 4/4, `pages:check` e o workflow ARC-13 passaram no head exato da PR `ed81efc`.
- **#274:** segue Draft e baseada numa main antiga. #291 substitui seu port executável; os 35 caminhos exclusivos da #274 podem conter evidência histórica útil. Após #291 ser integrada e conferida, fechar #274 como substituída, preservar sua branch e fazer a triagem dos artefatos exclusivos. Não excluir refs sem autorização específica.
- **Main → development:** #290 segue Draft e não mergeável. O compare exato aponta 13 commits somente em main, 441 somente em development e merge base 221b54b2a41ecc8c338d1bf2cf67280cf165ce95. A árvore de desenvolvimento ainda não contém a arte aprovada do hero/vídeo nem o fullscreen de Como funciona. Preparar a promoção seletiva desde o development atual; não integrar as árvores inteiras.
- **UX-04:** o run 44838594398 passou em development@be743fd98063b19be5ee0614add21b8c85fb4a85, mas é evidência somente daquele SHA; o development atual está em 44c7cb6. Preservar o run como histórico, sem tratá-lo como gate do head atual.
- **Design System:** main@43594dc contém o Plano Diretor v0.9 canônico. PR documental #124 mantém os três documentos operacionais sincronizados; o merge da PR segue pendente de autorização após a revisão automática bloquear a integração. O DS tem duas refs: main e a branch de #124.

**Próxima ordem:** (1) aguardar a decisão já solicitada para a #291; (2) promover seletivamente ao buffer o conteúdo público aprovado de hero/vídeo, tela cheia e comparativos, preservando o compilador ARC-03C de development; (3) integrar a #124 somente após autorização específica; (4) depois da #291, triar os 35 caminhos exclusivos da #274 e fechar a PR sem apagar sua branch; (5) continuar LOC-002 por grupos de semântica, conservando unreviewed até decisões verificáveis.

---

# HANDOVER CANÔNICO — MobiliPresenter2D Design System

**Snapshot histórico:** 26/10/2026, fuso `America/Sao_Paulo`.  
**Destino:** recuperação histórica do trabalho daquele checkpoint.  
**Prioridade registrada em 26/10:** estabilizar/reconciliar branches do Design System e não editar o produto até nova orientação. Essa restrição foi superada pela instrução explícita deste chat para continuar o plano de arquitetura nos dois repositórios.  

## Ponteiro operacional — 20/11/2026 (BRT)

**Pins verificados antes desta atualização:** Product `main@dc066f55619824626ea4752ecc0bafc67f9d9110`; Product `development@acf12c4170401ceb822526a613d89657e26c6310`; Design System `main@c128424d8ad48a48d56a753a8fbdf0215113faaf` (PR #121 integrada; base documental com evidência em `c9da1095829cabe63e9ae6618af48b6f3ee1fa1b`).

- **Product #286:** integrada por squash em `development`; a ponta atual de `development` é o commit `acf12c4170401ceb822526a613d89657e26c6310`. Os nove gates únicos passaram no head da PR `4680ddca92ea4cbab0366994e306d3288a4f1151`. A consulta live confirmou que não houve run no SHA do merge; os ajustes são somente de filtros de workflow.
- **Product #287:** Draft, head `26a2da331445ca2901d2851c0d37976a871ea875`, base `main@dc066f55`. Quatro gates passaram nesse head (`44808609053`, `44808609090`, `44808609186`, `44808609027`); o Deploy Preview #287 está READY no mesmo SHA. O diff contém quatro workflows, sem páginas/CSS/runtime.
- ARC-03C foi restaurado exatamente ao estado de `main` e não faz parte do diff da #287. O diagnóstico separado no head pai `30db98d7` passou build/fonte e divergiu da baseline imutável `303468b4` em `/about/320/light` (`rgb(34, 33, 31)` atual vs. `rgb(0, 0, 0)`). Não houve rerun ARC no head atual; a baseline permanece sem alterações.
- **Product #274:** Draft, head `6e0ca09ff7bb9c6255cf7bed2af7964304a3bcb2`, base antiga `efc40584`. LOC-002 classifica tecnicamente 15/15 registros; owners permanecem `null` e destinos `hold`. Quatro gates passaram no head citado; a aprovação semântica/editorial continua pendente.
- **Product #281:** Draft, head `173cb426f623abd7010117f148a0e12ea1edab82`, reconciliada com `main@dc066f55`. Os seis workflows passaram no head exato; o Deploy Preview #281 está READY no mesmo SHA. A validação de navegador usa fixture local anônima; revisão hospedada autenticada dos shells privados ainda não foi comprovada.
- O Product tem 13 branches remotas observadas, acima do soft cap 5. Isto aciona triagem, não exclusão automática; nenhuma branch foi removida nesta atualização. O Design System tem duas refs: `main` e uma branch documental ativa.
- A PR #120, documental, foi integrada por squash em `c9da1095829cabe63e9ae6618af48b6f3ee1fa1b`; a correção do handover #121 foi integrada em `c128424d8ad48a48d56a753a8fbdf0215113faaf`. Nenhuma altera o runtime do Produto. Este lote de atualização documental não executou testes locais nem publicou o Produto. Required checks permanecem `UNKNOWN`.

**Próximos passos:** manter #287 Draft até revisão da mudança de CI; concluir a revisão visual dos shells privados da #281 antes de promoção; reconciliar a baseline ARC-03C sem afrouxar o contrato; fechar pendências editoriais LOC-002 quando houver owners/fontes. Nenhuma branch foi apagada por contagem.

## Continuidade do plano v0.9 — 20/11/2026 (BRT)

### ARC-13 / DOM-001

O DoD documental de DOM-001 está satisfeito no candidato Product #274, head `a9c39c8220bcbccefea4cf74e666445d35ccf1d9`. O mapa associa autoridades, consumidores e verificações; a fronteira Buyer tem uma prova de CI que usa a política e leitura de cookie reais com provedores simulados; o gate ARC-13 regenera o JSON e confirma a proveniência das três páginas primárias. Passaram no head exato os [gates Buyer](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44445664910), [ARC-13](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44445665073), [ativos](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44445664757) e [foco do skip link](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44445664773). Isso não integra o candidato à `main`, não aprova conteúdo e não valida serviços hospedados.

**Parecer Common Sense Judge — checkboxes do Admin (Product main@803c32f7, leitura de 20/11):** “Iniciar ativo” define o estado inicial de cada entidade/serviço; “Ativa/Inativa” define `stage.enabled`, disponibilidade da etapa. As funções e regras de desabilitação são diferentes; ambos são checkboxes nativos, não switches. A diferença de cor vem da cobertura CSS: o checkbox por item não alcança a regra `accent-color: var(--accent)` já usada pelo controle da etapa. O código não demonstra intenção de hierarquia cromática. Julgamento técnico: preservar textos, posição e semântica; reaproveitar o acento existente no checkbox por item para remover o azul nativo e alinhar a família visual, sem criar token ou componente global. A mudança ainda não foi feita. A revisão assistiva dos nomes acessíveis permanece uma validação separada e não bloqueia outros pacotes.


### DS-05A — `.module-number` pareado, candidato local — 20/11/2026 (BRT)

Seis estados do Configurador local cobrem tema claro/escuro em 390, 1050 e 1366 CSS px, com sete badges por estado. No claro, cada largura passa de 1,43:1 para 13,02:1; no escuro, os sete badges mantêm 8,10:1 e nenhum muda. O controle negativo é preservado. A regra foi injetada somente em memória e corresponde ao candidato de escopo limitado da PR #271.

O checkout de medição registrou commit `efc40584`, não o pin canônico `dc066f55`; a árvore `app/` coincide exatamente em `0c4c2aec`, e `app/ui-theme.css` também foi conferido. O runner registrou `appWorkingTree=clean`, mas a pasta temporária do checkout não estava disponível para uma segunda leitura independente de `git status`. A fixture é uma projeção sintética gerada por defaults locais, sem banco, autenticação ou solicitações externas permitidas.

O recibo JSON comprimido e byte-preserving está em [ds05a-module-number-paired-runtime-cssom-2026-11-20.json.gz](../evidence/architecture/ds05a-module-number-paired-runtime-cssom-2026-11-20.json.gz); o [relatório de medição](../evidence/architecture/ds05a-module-number-paired-runtime-cssom-2026-11-20.md) registra método, hashes e limites. As seis capturas PNG são somente do tema claro; dark está medido em CSSOM/JSON. Isso não fecha DS-05A nem comprova a rota hospedada. `#viewerHint` permanece separado.

A PR #271 segue aberta, não integrada e sem revisão hospedada de `/config/` nesse head. O CSS candidato aprovado para validação não se torna token ou regra global por esta medição.

### GIT-018 / validação externa de links

A leitura dos 29 Markdown alterados no SHA `f2ee002722cb39838b429b272ca2097d45ef7501` reproduziu 612 destinos inline: 244 arquivos locais, 15 âncoras e 353 ocorrências externas (256 URLs únicas). A contagem anterior 601/342 estava 11 URLs externos desatualizada. O relatório occurrence-level está em [git-018-external-link-check-2026-11-19.json](../evidence/architecture/git-018-external-link-check-2026-11-19.json).

Dos 245 destinos GitHub únicos, 244 foram resolvidos pelo conector; ele não expõe o código HTTP bruto. Um link de artefato retornou 404 em duas tentativas; a execução pai [#43799448351](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448351) ainda existe e terminou com sucesso, então apenas a disponibilidade do artefato está em dúvida. Entre os 11 destinos não-GitHub, quatro páginas de W3C/Netlify Docs abriram no rastreador, sem confirmação separada do status HTTP ou dos fragmentos. Sete previews/páginas não abriram pelo rastreador e permanecem inconclusivos; quatro desses têm evidência de recurso/deploy no Netlify (preview #275 pronto, deployment de produção pronto e domínio publicado), sem afirmar que cada rota foi buscada. Três aliases antigos de Preview seguem sem confirmação. “Não aberto pelo rastreador” não foi contado como link quebrado.

O scanner original que produziu o total anterior não estava versionado nem identificado. O recibo registra a extração reproduzível, as linhas e URLs exatas, o método de cada consulta e os limites. A resolução local de links (244 destinos para 152 arquivos e um diretório) e das 15 âncoras permanece registrada no snapshot anterior; ainda não foi repetida nesta passagem.

**Estado:** GIT-018 está concluído como pacote documental, integrado por squash na Design System `main` pela PR #119. A validação tem os limites acima — um artefato antigo não encontrado e três aliases de Preview sem status HTTP confirmado. O readback confirmou os 95 caminhos (29 Markdown, 56 imagens, 7 dados, 2 scripts e 1 patch CSS), sem runtime do Produto ou arquivos de aprovação.

### MD-004 / execução e integração — 20/11/2026 (BRT)

O crosswalk dos 21 workflows e 21 comandos está em [MD-004 workflow crosswalk — 20/11](architecture/MD004_WORKFLOW_CROSSWALK_2026-11-20.md). A amostra histórica de 19/11 permanece separada da medição de #286/#287: 12 gates únicos concluídos somaram ~15,7 job-min; a tentativa cancelada do Flow consumiu 18,28 min instalando o browser antes dos testes, para ~34,0 job-min observados. A amostra mistura PRs e gates diferentes e não sustenta remoção de testes.

**Integração em development:** #286 passou 9/9 gates únicos no head da PR `4680ddca` e foi integrada por squash. O readback da branch confirma `development@acf12c4170401ceb822526a613d89657e26c6310`. Não há run de Actions associado ao SHA do merge; o pacote modifica somente arquivos de workflow.

**Port seletivo para main:** #287 permanece Draft em `26a2da33`, base `main@dc066f55`; os quatro gates relevantes e preview passaram no head exato. O diff é somente quatro workflows; ARC-03C foi retirado do diff e seu trigger temporário removido. A divergência no head pai `30db98d7` contra a baseline antiga continua como diagnóstico separado. Nenhuma asserção ou baseline foi afrouxada; #287 não foi integrada.

Required checks permanecem `UNKNOWN`. Passar em workflow de PR não comprova deployment nem validação de comportamento hospedado.

### Frentes restantes e próxima sequência

- **LOC-002:** manter os 15 owners/destinos em `null`/`hold`. A revisão técnica não identifica quem responde pelo conteúdo, e inventar owners ou wording seria uma decisão editorial sem base. Se surgir um owner ou fonte factual, esse é um ponto para pergunta objetiva; a classificação e revisão assistiva podem continuar em paralelo.
- **MD-004:** crosswalk 21/21 concluído. #286 foi integrada em `development@acf12c41` após 9/9 gates verdes no head da PR. #287 tem 4/4 gates verdes em `26a2da33`; Viewer roda em PR para `main` e runner Ubuntu 24.04. Os filtros temporários foram retirados. ARC-03C segue como divergência registrada contra a baseline histórica no head pai, sem alteração de app/CSS. Nenhum teste foi removido.
- **G2 / DS-05A e derivados de pedra:** preservados em HOLD enquanto faltarem configuração hospedada válida e a capacidade de replay por Pillow/DNS; não regravar hashes nem baselines.
- **GIT-014 / integração:** concluída para o pacote documental da PR #119, com readback e retirada da branch. Para cada pacote seguinte, preservar PR, gate, preview e readback como estados separados.

**Snapshot operacional preservado (18/11/2026, BRT):** Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` e Design System `main@79db735d6f05177b0c406e383d35832f3d72fdef` continuam sem mudança. Product #269 está Draft em `8701bf488e0434e98b10defa7473b22cef72238a`; os 12 workflows de Actions passaram, incluindo o gate NAV-005 com integridade ARC-03C e 124 cenários de browser, e o Deploy Preview está READY. A #119 permanece Draft; seu último head validado antes deste handover era `7bab42bce4832a2cfab828759bad8aab1eb2466c`, com `plan` aprovado no run #44435258931. Esta atualização dispara nova execução documental. As sete PRs do Product seguem abertas contra `main`; nenhuma foi integrada nesta retomada.

| PR | Frente | Estado/head revalidado |
|---|---|---|
| #269 | NAV-005 | Draft — `8701bf488e0434e98b10defa7473b22cef72238a` |
| #271 | contraste medido | aberta, sem Draft — `8a67d10fc8911bc146cf28667dd03e445af37f47` |
| #274 | ARC-13 / contratos V5 | Draft — `b57880006c3ffeeb88d9e0daec43057af54c3026` |
| #278 | geometria do hero | Draft — `69b98cbd2466338574068898f7755e1f6f68b852` |
| #279 | despacho UX-04 | Draft — `ffa288d181f0c53148e5a6b9ba69d3d8a5631651` |
| #280 | replay de vidro | Draft — `bf685e22338597f47d240c616473085d86a22cb8` |
| #281 | tema e gates de assets | Draft — `173cb426f623abd7010117f148a0e12ea1edab82` |

Os sete Deploy Previews estão em success/READY; os checks aplicáveis estão verdes, com resultados neutral/skipped conforme os workflows. O Product mantém 9 refs: sete branches ligadas a PRs abertas, `development` e `main`. As branches integradas das PRs #282 e #283 foram retiradas após readback. O Design System mantém 1 ref (`main`); a branch da #119 foi retirada após integração e preservação. O soft cap do Product segue como gatilho de revisão, não hard cap nem autorização para descartar PR ativa.


## Continuidade do plano v0.9 — 18/11/2026 (BRT)

- **GIT-018 permanece em andamento.** #119 segue Draft. O diff atual contém 94 caminhos documentais/de evidência (29 Markdown, 56 imagens, 6 dados, 2 scripts e 1 patch CSS), incluindo a cópia do plano v0.9; não altera runtime do Produto nem arquivos de decisão/aprovação. Na head `546416ea`, 601 links inline em 29 Markdown foram inventariados: 244 destinos locais de arquivo resolvem para 152 arquivos e 1 diretório; 15 âncoras locais apontam para IDs existentes; 342 URLs externos tiveram apenas a sintaxe classificada, sem validação de conteúdo/disponibilidade. Dois caminhos locais quebrados foram corrigidos. A antiga contagem de 205 referências não se reconcilia e foi substituída pelo scanner revisado. Faltam preflight integral, decisão de integração, readback da `main` e disposição segura da branch.
- **LOC-002 avançou em proveniência e classificação parcial.** O relatório com 1.026 ocorrências permanece gerado como `unreviewed`. O overlay da #274 (head `b5788000`) registra dez correspondências de identidade, 14 classes apoiadas pela função exata do sink e uma ocorrência sem classe. Os 15 registros ainda têm owner de conteúdo `null` e destino `hold`; classes não aprovam wording, chaves, extração, tradução, descrição alternativa ou qualidade assistiva.
- **ARC-15 — TST-015 concluído:** a #281 no head 7f107b2566b61410e6f38d6477e4873015346f00 cobre as oito páginas, mantém modo automático/explicito, persistência, preferência do sistema e troca de logo, e acrescenta o gate de navegador ao workflow existente. O [Mobile browser #810](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44425086708) passou 16 casos (oito shells × mobile 375×812 e desktop 1280×900): controle único, posição e ordem, foco visível, ativação por teclado/persistência e medida real dos alvos. As assertions únicas de Landing/Viewer foram auditadas e mantidas onde não há substituto equivalente.
- **ARC-15 — máscaras e pedra:** no head 7f107b2566b61410e6f38d6477e4873015346f00, `test_mask_semantics` e `validate-exposed-side-pixels.py` passaram no workflow existente após upload do artefato de 49.335.991 bytes (sha256 5c7467fc4db0fbafa5fe4796bfedd16fa2e9e2e73d0de9156e14cb3181468764). O passo agrega os resultados sem pular o segundo check em caso de falha. Os três testes de pedra permanecem fora até replay e revisão visual dos derivados após drift de fonte desde a #35. Nenhum hash ou baseline foi regravado.
- **TST-007 / #280:** o replay corrigido usa o Configurador em loopback; seis workflows passaram e quatro capturas foram revisadas. A faceta translúcida em `module-05-off` continua observação, sem baseline pixelar. GIT-017 ainda aguarda integração e readback.
- **TST-008 / CMP-002 — lote isolado em #269:** no head `8701bf488e0434e98b10defa7473b22cef72238a`, os dois negativos de drift usam `mkdtemp`; cinco negativos de fonte cobrem link inseguro, slot duplicado, header público atual duplicado, header de Viewer e status experimental. A guarda do compilador compara tokens de classe, alcançando `site-header site-header--public`; o workflow também observa mudanças no compilador/teste. No head exato, 12/12 workflows de Actions passaram, incluindo NAV-005 (run #44437069731: integridade e 124 cenários Chromium/WebKit), e o Deploy Preview está READY. A PR continua Draft e não alterou runtime. Limites: ainda não há snapshot de toda a árvore privada/Viewer após `--sync`; atributo `class` quebrado por newline não tem caso de teste. O lote conclui este candidato isolado, não o inventário completo de testes mutáveis.
- **MD-004 — avanço parcial:** a ARC-15 lista eventos/escopos dos 21 workflows de Product `main@efc40584`; o recorte identifica seis gates acionados por `app/**`, compartilhamento de fixture e sobreposição de execução sem redundância demonstrada. Nesta retomada, medi uma amostra candidata da #269: 12 workflows/14 jobs, envelope observado de 2,6 min e 11,6 job-min agregados, arredondados a 0,1 min. Esse dado não substitui duração da baseline `main`, que continua `UNKNOWN`. Ainda falta o crosswalk integral workflow→job→comando→fixture→assertion→contrato e medir a baseline comparável; não há fundamento para remover testes.
- **Higiene:** Product tem 9 refs (sete PRs abertas, `development` e `main`); nenhuma branch de trabalho está sem uso. Design System tem 2 refs. A contagem acima do soft cap 5 é gatilho de revisão, não autorização para excluir.
- **Próxima sequência:** (1) manter `owner=null`/`destination=hold` no LOC-002 até decisões e revisão assistiva; (2) completar o crosswalk MD-004 e medir duração/custo sem inferir por tamanho de artefato; (3) fechar o DoD DOM-001 ligando proibições prioritárias a provas executáveis e atualizar o pin documental de #274; (4) retomar replay/revisão visual de pedra quando Pillow/DNS permitirem; (5) terminar preflight GIT-018, com validação dos links externos antes de qualquer decisão de integração. Preservar G2/DS-05A em HOLD enquanto configuração hospedada e pares incertos não tiverem prova válida. Manter PRs Draft/aberta até DoDs e decisão aplicável; retirar branch somente após readback e prova de ausência de trabalho ativo.
## Estado live após publicação da #277 e higiene de branch — 16/11/2026 (BRT)

- **Product publicado:** `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`, árvore `439fb0fc9a3295f9e45486198e9de83fca8376ee`. A PR [#277](https://github.com/EAKerber/MobiliPresenter2D/pull/277) foi integrada por squash. O deploy `6afa7bee50b552356a973df4` está READY e aponta para o mesmo commit. Os 11 workflows da PR terminaram com sucesso; o [recibo post-#277](../evidence/architecture/product-main-post-277-readback-2026-11-16.md) registra a interação de preview e o limite da leitura de produção.
- **Mudança funcional coberta:** o controle próprio sobreposto entra/sai da tela cheia nas páginas inicial e “Como funciona”; o nome acessível acompanha o estado. O Preview #277 foi exercitado nas duas páginas. G3 continua parcial.
- **Branches do Product:** 7 refs remotas: `main@efc40584`, `development@1a69ff76`, `codex/ds04-208-preview-batch-20261111@8a67d10`, `codex/nav005-public-compact-main-20261110@8c77350`, `docs/arc13-post-273-reconciliation-20261114@72ae7c8`, `fix/hero-screen-art-anchor-20261116@69b98cb` e `infra/ux04-dispatch-workflow-20261116@ffa288d`. Sete refs incluem duas acima do soft cap; a segunda é a via isolada de UX-04 em #279. Cinco é gatilho de revisão, não hard cap; revisar novamente após #278/#279 estabilizarem.
- **PRs do Product:** #269 permanece Draft sobre `main@efc40584`, head `28b1e2ef4f62b418110ba7694a59dee95969174b`, 18 caminhos, Preview success e 12/12 Actions; o teste de teclado passa com foco inicial verificado, e o SHA anterior passou no rerun depois de uma falha intermitente. #271 está aberta, sem Draft, head `8a67d10fc8911bc146cf28667dd03e445af37f47`, 9/9 Actions e Preview success. #274 está Draft, head `72ae7c8a7e3a8c89645d91d91482d66c1eb4d764`, ARC-13 documental. #278 está Draft, head `69b98cbd2466338574068898f7755e1f6f68b852`, somente teste, dois gates aprovados. #279 está Draft e mergeável, head `ffa288d181f0c53148e5a6b9ba69d3d8a5631651`, somente o workflow UX-04 copiado do pin de development; Deploy Preview READY, sem execução manual nem alteração de runtime.
- **ARC-13:** a PR [#274](https://github.com/EAKerber/MobiliPresenter2D/pull/274) foi regenerada sobre a main atual. O relatório válido tem SHA-256 `abce38889ad6d78c634fadad5d6f0c63fd9706ac3e0c13bcdf13f78010caeb9e`, 1.026 sinks, 360 fontes JS, 420 ocorrências HTML mapeadas à autoria e zero sites sem owner/rota. O crosswalk inclui remapeamentos, entradas novas/retiradas e estados do controle fullscreen. O alt novo da Home ainda pede confirmação factual; “Mais informações” tem `role=group` no código, porém leitura assistiva e chave/extraction seguem pendentes. A aprovação visual do aparelho não implica aprovação editorial nem catálogo.
- **ARC-15:** matriz pinada em Product main46, agora com revisão focal de `test-core.js`: há overlaps parciais entre preço, visibilidade, vidro, flow e PiP, mas nenhum teste inteiro redundante. O arquivo amplo permanece; separá-lo seria dívida de legibilidade, não redução necessária. Os oito itens sem invocação mantêm pareceres individuais. `ui-theme-contract.cjs` tem uma expectativa uniforme de URL que diverge de três shells atuais (provável falha estática, ainda não executada); `exposed-sides-glass.cjs` abre Home e espera Configurador, com `local-buyer-config-server.mjs` como candidato de fixture. Quatro disposições ainda dependem de decisão sobre invocação e paths. Nenhum teste foi removido, editado ou executado; required checks seguem UNKNOWN/403.
- **DS-05A:** o recibo de CSS compara proveniência até main64; CSSOM não foi recapturado em `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`. `/config/` hospedado e os 98 pares `UNCERTAIN` mantêm G2/DS-05A em HOLD; nenhuma extração ou conformidade visual global é afirmada.
- **Design System:** `main@79db735d6f05177b0c406e383d35832f3d72fdef`, 2 refs. #119 segue Draft na branch documental existente; este lote acrescenta a revisão ARC-15, recibo de higiene e atualiza os overlays, sem alterar runtime nem integrar a PR.
- **UX-04/G1:** o workflow existe em `development@1a69ff76` mas continua ausente de Product `main`. A PR Draft #279 oferece uma via isolada de um arquivo para incluí-lo; seu Preview está READY, mas ainda não há dispatch nem execução no SHA-alvo. Após eventual integração e autorização, revalidar `development` imediatamente antes de dispatch; SHA observado na preparação: `1a69ff76a5f36e3245a288773bb409aa662e4e62`.
- **Próxima sequência:** avançar ARC-15 pelo harness de vidro: mover o replay de `file://`/Home para Configurador em loopback usando a fixture local existente como candidata; só depois decidir gate path-specific ou replay manual, sem conectar à CI antes da validação. Em paralelo, fechar a escolha do contrato de tema e seguir os pareceres de máscara/pixel e stone sem converter estados REVIEW/PENDING em aprovação. UX-04 permanece condicionado à revisão da #279 e releitura do SHA de `development`; G2/DS-05A continua HOLD até CSSOM no pin atual e configuração `/config/` válida/autorizada. G3 permanece parcial. Reavaliar higiene após estabilização, sem excluir refs por contagem.
- **Estimativa geral:** permanece no último registro datado de ~30% (faixa 25–35%); esta atualização localizada não recalcula o avanço ou o calendário.

## Retomada ARC-15 — replay local de vidro — 17/11/2026 (BRT)

- O inventário ARC-13 em Product #274 já contém a aprovação visual do resultado final da #277 e registra “Abrir vídeo em tela cheia” / “Sair da tela cheia” nas duas páginas. O título da PR foi alinhado para indicar reconciliação posterior à #277. Alt da Home, revisão assistiva, chaves e extração continuam pendentes.
- A PR Draft [#280](https://github.com/EAKerber/MobiliPresenter2D/pull/280), Product head `bf685e22338597f47d240c616473085d86a22cb8`, redireciona o replay de `file://`/Home para o Configurador V5 `/config/` em loopback. Em execução standalone, o teste inicia a fixture em porta efêmera, valida as respostas anônimas e fecha browser/servidor em `finally`; no job Mobile browser, reutiliza o servidor local compartilhado e roda somente no alvo loopback padrão. A captura compara os checkboxes com as camadas renderizadas e o estado do vidro, registra os quatro nomes e grava `test.json` mesmo após falha. O manifesto inclui rota, viewport e versão do navegador.
- O histórico dos heads é distinto: `889a8068` passou, mas a captura final não correspondia ao nome; `ab2d3785` falhou por mutar estado interno read-only; `a7e4da3` falhou porque o nome não foi passado ao `page.evaluate`; `bf685e2` corrigiu o fluxo e passou. Mobile browser #802 (`44213833429`) registra `passed:true`, 256 casos, quatro capturas, nenhum erro de página e artefato `14386753961` (`sha256:946759d9e771bd9a36b2dddfda48df99d75d0c63efa8cc452e917287131dc9a9`). Os outros cinco workflows do mesmo head — Keyboard, Summary pricing, Stone, Flow layout e Current asset gates — também passaram.
- A leitura de `test.json` confirmou 256 casos, os sete IDs de módulo, quatro nomes esperados e distintos, estado dos checkboxes igual ao das camadas renderizadas, vidro visível nas quatro capturas e zero incompatibilidades. A revisão das quatro imagens também concorda com os estados registrados; a captura `glass-module-05-off` mostra uma faceta vertical translúcida estreita que fica como observação visual, sem baseline de pixels para afirmar regressão. A auditoria de lifecycle confirmou que os jobs mantêm a fixture viva entre etapas e que o runner descartável encerra o processo ao fim do job; não há evidência de vazamento entre jobs. Falta teardown explícito nos cinco workflows consumidores, uma melhoria de higiene de baixo risco dentro de TST-006. TST-006 continua mais amplo que o lifecycle e não fica concluído por esta leitura. TST-007 não é classificado como falho. O teste usa defaults locais sintéticos e Chromium desktop; não prova configuração publicada, autenticação, Blob, Production nem pixels contra uma referência.
- As verificações locais `node --check` e `git diff --check` passaram; o replay não foi executado localmente porque Playwright/Chromium não estão instalados. O Product mantém 8 refs e Design System 2. A PR #280 continua Draft até integração e readback no destino, como exige o DoD de GIT-017; nenhuma integração é proposta nesta atualização.

**Reconciliação com o plano v0.9 — 17/11/2026:**

- **TST-006 — `in_progress`:** a fixture V5 gera defaults projetados, valida payload/sessão anônima, fica em loopback e é consumida por cinco workflows. O servidor permanece vivo durante as etapas do job; o runner descartável o encerra no fim. Teardown explícito por PID/etapa `always()` segue como melhoria de higiene nos cinco consumidores; readiness completa, conflito entre execuções e o restante do DoD ainda precisam de revisão.
- **TST-007 — `in_review`:** #280 head `bf685e2` passou no replay exato e no conjunto de seis workflows; manifesto e quatro screenshots conferidos. O resultado é limitado à fixture local. A captura `module-05-off` contém uma faceta translúcida a acompanhar sem baseline de pixels. O DoD só fecha após integração e readback no destino.
- **GIT-017 — `in_progress`:** #280 permanece Draft e sem integração; o estado não representa bloqueio de CI. A integração exige preflight e autorização de merge.
- **LOC-001 — `in_progress`:** #274 fornece inventário candidato válido (1.026 sinks, 360 fontes JS, 420 ocorrências autorais mapeadas e zero sem origem no recorte) e reconciliação pós-#277. Isso é proveniência de fonte/rota, não revisão semântica: as 1.026 ocorrências permanecem candidatas; alt da Home, tecnologia assistiva, chaves e extração seguem pendentes. O hash histórico inválido agora tem errata no documento de owner decisions.
- **GIT-014 — `in_progress`:** #274, head `7de76978efcc29c…21811 tokens truncated…ogresso desta retomada:** recapturar G2 localmente e ampliar G3 para 28 casos; ambos seguem parciais por configuração publicada inválida, 98 pares UNCERTAIN e cobertura privada/plataforma ainda ausentes. Meta estável: 2 refs. Ao atingir 5, revisar crescimento e considerar um hard cap; 7 refs do produto exige revisão, sem excluir por contagem. Usar branches existentes #119/#272, sem nova ref. Sem merge, exclusão, deploy de produção ou operação de banco.
## Continuação G2 — recaptura local do Configurador (2026-11-11, BRT)

A captura antiga tinha uma linha candidata escura cujo CSSOM não correspondia à aparência do screenshot; ela não foi usada como evidência. A reprodução mais recente fixa o tema antes da navegação e registra o tema solicitado, `data-theme`, `CASA_UI_THEME.getResolved()` e SHA-256 por screenshot. O conflito antigo não se repetiu, sem atribuir causa raiz.

O pacote [G2 recapture](../evidence/architecture/g2-configurator-recapture-2026-11-11.md), com oito imagens e recibo JSON, fixa produto `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, CSS base `d43e6fb5e66133d2389b5c39b165b76b13cfa868`, candidata #271 `eb346a41ad91f6dc53875cb954e9018fdc1dd713`, Edge `157.0.4341.46`, DPR 1 e 390×900/1366×900 nos dois temas. Todos os oito estados validaram o Buyer V5 local e tiveram os três indicadores de tema coincidentes. Um único 404 da bundle de navegação privada ocorreu em cada carregamento; não houve exceção de página. Esta evidência é local e não cobre autenticação/navegação privada nem substitui a validação hospedada.

G2 continua em andamento: configuração publicada inválida no Preview; anel de acabamento selecionado ainda sem captura deste lote; #208/#216, 98 pares UNCERTAIN e DS-05A permanecem pendentes. A documentação e o pacote foram adicionados à branch já existente da PR #119; nenhuma nova branch, mudança no produto, merge, deploy de produção ou operação de banco foi feita nesta continuação.


## Continuação G3 — recaptura local de tema e marca (2026-11-11, BRT)

A captura em produto main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95 percorreu /, /how-it-works/, /about/, /viewer/, /config/, /admin.html e /access/manage.html em 390×900/1366×900 CSS px e light/dark: 28 casos. A preferência, tema raiz e API concordaram; os src de todos os assets de marca corresponderam ao tema e os logos de cabeçalho carregaram. Os controles completaram duas transições e não houve exceções JavaScript de página.

As requisições às bundles e APIs privadas não foram preenchidas: 28 respostas 404, incluindo /api/buyer-configuration. O shell estático e o controlador foram observados; menu/sessão autenticados, configuração publicada, foco/hover, tela tátil, Safari/iPad e revisão visual não foram validados. Duas imagens de marca nos cards de comparação mobile de /how-it-works/ ainda informavam complete=false, com naturalWidth=380; esse detalhe está registrado no recibo.

Veja [relatório G3](../evidence/architecture/g3-theme-controller-slots-recapture-2026-11-11.md) e seu recibo JSON. G3 permanece parcial; os slots de marca/controle continuam contextuais. Nenhum código do produto foi alterado.


## Retomada live — main estável e política de refs (2026-11-12, BRT)

Esta seção prevalece sobre o snapshot anterior e preserva as entradas anteriores como histórico.

- **Política:** Design System — meta/soft cap de 2 refs, sem hard rule; produto — soft cap de 5 durante trabalho ativo, com alvo de 2 refs (`main` + `development`) quando estável. Ao chegar a 5, reavaliar crescimento e considerar hard cap; a contagem não autoriza apagar refs.
- **Main e hotfix:** produto `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; #273 está Draft no head `016b33f9315620ee09b28c4e2c9ba5752b858471`, baseada exatamente nesse SHA, 8 commits à frente e 0 atrás, com 11 workflows aprovados e Preview pronto. O conteúdo da #273 permanece fora da `main`; a revisão visual final da PR ainda está pendente. #269, #271 e #272 também permanecem sem merge.
- **Refs:** Produto tem 7 refs, acima do soft cap de 5. A #272 prepara a remoção exata da branch obsoleta #270 e a limpeza condicional da própria branch de higiene após integração, com queda prevista de 7 para 5; a PR não foi integrada e nenhuma ref foi removida. Design System tem 2 refs: `main` e a branch documental da #119, que continua Draft.
- **G0–G8:** G0 contínuo; G1 parcial; G2 em andamento; G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente (#232/fixture autorizada); G8 não iniciado. Os gates de arquitetura continuam independentes da revisão do hotfix.
- **Proteção:** GitHub informa que as regras de proteção das branches `main` estão desativadas nos dois repositórios. Nenhuma regra foi alterada neste trabalho; a estabilidade observada é processual.

## Atualização de 12/11 — G2 Admin e refs live

O recálculo local do Admin confirmou uma única lacuna de contraste clara para `.initial-state-option`: 4,229:1 no Product `main@221b54b`, com o dark em 8,384:1. O ajuste scoped em #271 mediu 9,092:1 usando o token já existente; consulte o [recibo completo](../evidence/architecture/g2-admin-initial-state-labels-cssom-2026-11-12.md). #271 está aberta no head `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`; os 9 workflows da PR e o status Netlify Deploy Preview passaram. **Na data desta entrada**, a revisão visual/CSSOM do Admin ainda dependia de autenticação; essa pendência foi superada pela revisão descrita na atualização posterior abaixo. `/config/` segue sem configuração publicada válida. Nada foi integrado à `main`.

Inventário conferido pela API: Produto tem **7 refs** (soft cap 5 excedido por 2; revisar, sem exclusão automática); Design System tem **2 refs**, dentro da meta. A #272 não foi integrada e nenhuma ref foi excluída. A regra vigente continua: Product target 2 quando estável; DS soft target 2; ao chegar a 5, avaliar se um hard cap é útil.


## Revalidação do Preview da Product #271 (2026-11-12, BRT)

Para o head exato `d699fb1911046dfbbc475fad9415f3ff3fca1cc8`, a API confirmou nove workflows de PR com `success` e status do Netlify Deploy Preview com `success`. A publicação está pronta, mas não foi feita revisão visual/CSSOM hospedada da nova regra do Admin nesta revalidação; `/config/` ainda falha ao validar a configuração publicada. Product `main` permanece em `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. Nenhum merge, remoção de refs, deploy de produção ou operação de banco ocorreu.


## Continuação G2 — anel de acabamento selecionado (2026-11-12, BRT)

No checkout detached limpo do Product `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, a comparação base/candidata usou os blobs CSS `d43e6fb5e66133d2389b5c39b165b76b13cfa868` e `eb346a41ad91f6dc53875cb954e9018fdc1dd713`. O fluxo real avançou para Acabamentos e selecionou Base clara e Carvão. Chrome 156.0.8078.82 / DPR 1, 390×900 e 1366×900, temas light/dark: 16 capturas no total. Os 16 casos tiveram configuração Buyer V5 validada, estado selecionado real, `aria-pressed=true` e tema solicitado/documento/API coincidentes.

O CSSOM candidato computou borda `#292723` e anéis `0 0 0 2px #fff, 0 0 0 4px #292723`; a base usa borda branca e anel branco translúcido. As capturas mobile mostram contorno mais visível para Base clara no escuro e Carvão no claro. Relatório, recibo e capturas: [G2 selected ring](../evidence/architecture/g2-selected-finish-ring-2026-11-12.md). Um 404 esperado da bundle privada ausente ocorreu por contexto, sem exceção de página.

O subgate de seleção local avançou; G2 permanece em andamento. A configuração publicada de `/config/` continua inválida, e, **na data desta entrada**, a nova regra do Admin de #271 ainda aguardava revisão autenticada; veja a atualização posterior abaixo. #208/#216, 98 pares UNCERTAIN, DS-05A, teclado/foco, zoom e validação Safari/iPad permanecem fora desta evidência. Nenhuma mudança foi integrada à Product `main`.


## Atualização após revisão autenticada do Admin e correção das capturas G2 — 12/11/2026 BRT

O usuário autenticou no Preview exato da Product #271. A leitura do Admin em 634×652 CSS px / DPR 1,5 encontrou 18 labels `.initial-state-option` com caixas visíveis; as checkboxes estavam habilitadas e marcadas, e não foram alteradas. No CSSOM, light ficou em `#403A34` sobre `#EAE7E2` (9,092:1), dark permaneceu `#C4BCB2` sobre `#232321` (8,384:1). Nenhuma configuração foi salva. Os hashes das capturas de sessão e fonte da regra estão no [recibo Admin](../evidence/architecture/g2-admin-initial-state-labels-cssom-2026-11-12.md). Isso passa só o subgate de labels.

O primeiro lote do anel exibia transform de hover em 15/16 linhas. Ele foi substituído por 16 PNGs recapturados com o ponteiro em `(0,0)` e `transform:none` confirmado antes de cada captura; os hashes dos bytes conferem com o recibo compacto. A seleção real, `aria-pressed=true`, configuração Buyer V5 e tema são válidos em 16/16. **Este parágrafo registra o snapshot anterior ao recapture hover/foco:** naquela etapa, o relatório e o JSON cobriam somente o A/B sem hover; a cobertura foi ampliada nos adendos subsequentes. `/config/` continua sem configuração válida, então a revisão hospedada do ring segue pendente e G2 em andamento. 

Product `main` continua em `221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; DS `main` continua em `79db735d6f05177b0c406e383d35832f3d72fdef`. O ramo DS existente da #119 está em `1f832fc1b2cc8fd2f3ccbf892ab8f9cea43fea15` antes desta atualização; o Branch hygiene run #81 passou nesse SHA. Inventário live: 7 refs no Produto (acima do soft cap 5) e 2 no DS. Nenhuma branch foi criada ou apagada, nenhum PR foi integrado, e não houve alteração de runtime/deploy/DB.


## Adendo G2 — estado hover do anel e coerência do handover (12/11/2026 BRT)

A mesma matriz local foi rodada com o ponteiro sobre o swatch selecionado. Em 16/16 casos, `:hover` permaneceu ativo após estabilização de 200 ms, o transform computado foi `matrix(1.06, 0, 0, 1.06, 0, 0)`, a seleção real persistiu com `aria-pressed=true`, e o Buyer V5/tema permaneceram válidos. O box-shadow base continuou branco translúcido; o candidato conservou o par branco/`#292723`. Não houve exceção de página; o 404 por contexto da bundle privada ausente foi o único erro HTTP. **Snapshot anterior à matriz de foco visível:** naquele ponto, o relatório e o recibo reuniam 16 capturas sem hover + 16 com hover; a seção posterior amplia o pacote para 40 estados. Isto não equivale a cobertura geral de hover/foco nem a revisão hospedada do anel; `/config/` continua inválido.

O subgate do Admin segue aprovado com autenticação, sem interação nas checkboxes. Para eliminar a contradição entre as notas datadas de 12/11, as entradas anteriores que dizem que a revisão do Admin aguardava autenticação são agora explicitamente históricas e apontam para a atualização que registra a conclusão.


## Adendo G2 — foco visível por teclado no swatch selecionado (12/11/2026 BRT)

Com a mesma fixture Buyer V5 local, foram comparados baseline/candidata, light/dark e Base clara/Carvão em 390×900 CSS px: oito capturas. O ponteiro ficou fora dos swatches; Tab/Shift+Tab levou foco ao botão selecionado. Em 8/8, `:focus-visible` foi verdadeiro, `:hover` falso, `transform:none`, a seleção persistiu e `aria-pressed=true`. O outline computado foi `rgb(110,81,46) solid 2px` em light e `rgb(216,188,124) solid 2px` em dark; o `box-shadow` do anel permaneceu específico de base/candidata. A revisão visual das capturas mobile não mostrou clipping. Sem exceções de página; apenas o 404 esperado por contexto da bundle privada ausente. O [relatório e recibo combinados](../evidence/architecture/g2-selected-finish-ring-2026-11-12.md) agora reúnem 40 estados: 16 no-hover, 16 hover e 8 focus-visible. Este recorte não cobre a navegação completa por teclado, outros controles, zoom, Safari/iPad ou o ring hospedado; `/config/` segue inválido.


## Snapshot G3 — ownership de `.swatch` no Configurador (12/11/2026 BRT, pré-captura local; superado pelo adendo final)

A varredura do pin Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` encontrou dois geradores dentro de `/config/`: `renderFinishControlsFromData()` cria os acabamentos globais em `#finishSwatches`, e `createLocalFinishControl()` cria acabamentos locais dentro de `moduleDetail`. Ambos usam `.swatch`, `.is-selected` e `aria-pressed`; os handlers e os domínios de seleção são separados. A rota carrega `styles.css` (`app/config/index.html:30`) antes de `ui-theme.css` (`:41`); a família inclui base/hover/selected/responsivo em `app/styles.css:349–367,692` e foco geral de botão em `:96–98`.

**Snapshot pré-captura, superado pelo adendo final desta página:** a matriz de 40 estados do anel cobria então somente o consumidor global (`data-finish-id`). O consumidor local (`data-local-finish-id`) estava mapeado estaticamente e ainda não tinha prova runtime naquele ponto. A captura posterior de 8 casos abaixo completa a linha `.swatch`; G3 como gate geral permanece parcial. Não extrair CSS nem alterar produto.


## Snapshot G3 — ownership de `.swatch` no Configurador (12/11/2026 BRT, pré-captura local; superado pelo adendo final)

A varredura do pin Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` encontrou dois geradores dentro de `/config/`: `renderFinishControlsFromData()` cria os acabamentos globais em `#finishSwatches`, e `createLocalFinishControl()` cria acabamentos locais dentro de `moduleDetail`. Ambos usam `.swatch`, `.is-selected` e `aria-pressed`; os handlers e os domínios de seleção são separados. A rota carrega `styles.css` (`app/config/index.html:30`) antes de `ui-theme.css` (`:41`); a família inclui base/hover/selected/responsivo em `app/styles.css:349–367,692` e foco geral de botão em `:96–98`.

**Snapshot pré-captura, superado pelo adendo final desta página:** a matriz de 40 estados do anel cobria então somente o consumidor global (`data-finish-id`). O consumidor local (`data-local-finish-id`) estava mapeado estaticamente e ainda não tinha prova runtime naquele ponto. A captura posterior de 8 casos abaixo completa a linha `.swatch`; G3 como gate geral permanece parcial. Não extrair CSS nem alterar produto.


## Atualização G3 — runtime do acabamento local ao módulo (12/11/2026, BRT)

A cópia limpa destacada do Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` gerou um fixture Buyer V5 em memória: `base-light` permaneceu global; `cocoa` e `shadow` ficaram locais e habilitados para `module-01`. O validador e a projeção Buyer V5 aceitaram o fixture. O Playwright abriu `/config/`, selecionou o módulo e clicou os botões locais reais. Nenhuma configuração foi salva ou publicada; não houve API remota ou banco.

- 8 capturas: baseline/candidata × light/dark × `cocoa`/`shadow`, em 390×900 CSS px, Chrome 156.0.8078.82 / DPR 1.
- Em 8/8, o `aria-pressed` local acompanhou a seleção; o acabamento global permaneceu `base-light`. Borda, box-shadow e transform computados coincidiram entre swatch local e global na mesma página. Sem erro de página nem erro HTTP inesperado.
- Relatório, recibo e PNGs: [evidência G3 do consumidor local](../evidence/architecture/g3-module-local-swatch-runtime-2026-11-12.md). Os 40 casos G2 anteriores continuam sendo estritamente a matriz global; as 8 capturas locais são separadas.
- Classificação `.swatch`: aparência do anel compartilhada dentro de `/config/`; escopos de seleção distintos por design; nenhum consumidor cross-route identificado. A linha runtime de G3 agora está coberta e não sugere extração. G3 como gate geral segue parcial; G2 hospedado continua pendente porque `/config/` rejeita a configuração publicada.

Sem alteração do produto, banco, publicação, refs remotas ou `main` do Product.

## Reconciliação live do plano arquitetural geral — 12/11/2026

**Snapshot histórico, superado pela revalidação live de 14/11 registrada no topo deste handover.** Os números, HEADs e próximos passos abaixo descrevem apenas o estado de 12/11; preservar como recibo, sem usar a sequência antiga como instrução corrente.


O objetivo corrente abrange ARC-01…ARC-16 e V0–V6; G0–G8 é outro plano de consolidação e verificação que continua sendo acompanhado. Este adendo compara as afirmações históricas com o Product main confirmado, sem reescrever evidência antiga.

### Entregas arquiteturais já integradas

- O Product main observado é 221b54b2a41ecc8c338d1bf2cf67280cf165ce95. A PR [#237](https://github.com/EAKerber/MobiliPresenter2D/pull/237) está merged; seu merge commit 5ccb2a8dde6dd16e136f03387dc833aab828c5cf e o commit de origem ARC-03C ff5c55c24ef42eb106e6dda6aa7698b00355270a são ancestrais desse main.
- ARC-03C está implementado no build: scripts/compile-primary-pages.mjs gera as páginas a partir de architecture/pages e architecture/fragments; package.json inclui o gate/build; architecture/fragments/primary-header.routes.json declara BUILD_AUTHORITATIVE_ARC03C e exclui Viewer, Config, Admin e Access do escopo. A PR #237 integrou o controlador de navegação pública e preservou a variante Viewer NAV-005. O resultado é integração em main, não apenas uma prova isolada.
- O arquivo de integração ARC-03C e o handover do produto de 22/10 ainda descrevem a etapa como isolada ou como próximo passo. Esses trechos agora são snapshots pré-integração; uma revisão documental focada no Product permanece pendente.

### Entregas e gates ainda abertos

- V0/ARC-13 ainda não tem inventário integral nem catálogo pt-BR consumido pelo runtime. O índice legado de 826 ocorrências em 26 fontes continua como histórico de candidatas. Um scanner local sobre Product `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95` está pronto no branch local `work/arc13-ui-inventory-20261112` (HEAD `c7262cf`, commits locais; sem publicação/PR e com `app/` inalterado). Ele gera um candidato limitado e não classificado com 988 ocorrências (600 HTML, 388 sinks JS; 154 estáticas e 234 dinâmicas/mistas), 17 exclusões explícitas, zero erros de análise e zero lacunas de rota. Símbolos e pontuação dinâmica permanecem para revisão contextual. Isso ainda não prova cobertura integral nem rastreia todas as origens de dados; classificação, origem/owner e reconciliação das lacunas precedem qualquer catálogo de runtime.
- V2/P-TOKEN: há pin e exportações versionadas, mas isso não prova ativação geral de tokens no CSS do produto. A origem e os consumidores precisam ser reconciliados com os pares visuais homologados; nenhuma paleta global deve ser ativada por inferência.
- Os gates G0–G8 permanecem conforme o checkpoint de 12/11: G0 contínuo; G1 parcial; G2 em andamento; G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente; G8 sem release. A conclusão de ARC-03C não fecha esses gates nem o plano geral.
- G4/G5 de CSS compartilhado continuam condicionados à prova de ownership e equivalência por consumidor. A linha .swatch está coberta em G3, mas o inventário de ownership geral está parcial.
- V6/G7/G8 ainda exigem cobertura funcional integrada por risco, evidência de dispositivo e autenticação quando cabível, revisão dos riscos residuais, aceitação e autorização de release. CI, preview e merge não se substituem entre si.

### Próxima sequência de execução

1. Reconciliar a documentação do Product com o main@221b54b, começando por ARC-03C já integrado e preservando a proveniência do snapshot de outubro.
2. Revisar o candidato local V0/ARC-13 já gerado: classificar as 988 ocorrências e 17 exclusões por origem/rota/consumidor/owner, completar a auditoria de sinks e lacunas e reconciliar o resultado com o contrato ARC-13. Só depois planejar substituições pt-BR em lotes reversíveis. Publicar a branch do produto após a higiene autorizada reduzir as refs; não criar catálogo ou alterar runtime antes da revisão.
3. Prosseguir G1–G3 nos gates ainda reproduzíveis; manter hospedado/PENDING o que depender da configuração publicada inválida, e classificar sem adivinhação os 98 pares com backdrop-filter.
4. Só então avançar extrações V2/G4/G5 aprovadas por família, mantendo domínio V5, autorização e publicação independentes; avaliar V5/G6 apenas por consumidores reais e benefício medido.
5. Fechar V6/G7/G8 com validação representativa e readback antes de propor release.

### Refs e operações

A consulta live de 12/11 mostra 2 refs no Design System (main e a branch da PR #119) e 7 no produto. A PR #272 prepara um lote exato para reduzir o produto de 7 para 5 após integração e readback; o lote ainda não foi aplicado. Nenhuma ref deve sair por contagem ou antiguidade. A documentação deste adendo é acrescentada à branch já existente da PR #119, sem criar ref; main, produto e dados publicados permanecem sem alteração nesta atualização.

## Retomada ARC-13 — revisão de fontes e inventário por ocorrência — 12/11/2026, BRT

Este adendo substitui a contagem anterior de 988 ocorrências como estado atual. O Product segue em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`; a ferramenta e o relatório permanecem locais no branch `work/arc13-ui-inventory-20261112`, agora em `04945d6`. Não há PR de inventário nem ref remota do Product; `app/` continua inalterado.

- O scanner passou de 388 para 396 sinks JavaScript ao incluir atribuições compostas a texto e propriedades textuais em `Object.assign`; são 600 ocorrências HTML + 396 sinks JS = 996 registros, 159 valores JS estáticos e 237 dinâmicos/mistos.
- Agrupamento exato: 759 ocorrências com valor estático correspondem a 584 valores distintos; 65 grupos repetidos somam 175 ocorrências além da primeira. Há também 48 referências HTML. Esses valores incluem símbolos, marca e referências; continuam impróprios como estimativa de chaves ou esforço de tradução.
- A revisão manual cobriu 546 registros públicos, 280 de Admin/Acesso e 230 do Configurador; os recortes compartilham módulos de runtime e não são aditivos. O relatório permanece `candidate-unreviewed`; zero erros de parser, owners ou rotas não demonstram cobertura lexical.
- As fontes ainda ausentes incluem a tabela de explicações de Como funciona, labels da navegação compartilhada, mapas/opções/mensagens de erro do Admin e textos em módulos de dados de Landing/Viewer. O próximo trabalho é inventariá-las como fontes com provenance separada dos sinks, e só depois fechar a classificação e planejar o primeiro lote pt-BR.
- O usuário apontou dois checks diferentes no Admin. O check por item (“Iniciar ativo”) e o controle de disponibilidade da etapa (“Ativa/Inativa”) têm responsabilidades distintas. Em `admin.css`, o primeiro não declara `accent-color` e herda o azul padrão do navegador; o segundo usa `var(--accent)`. Manter variantes semânticas faz sentido, mas a hierarquia visual ainda precisa de decisão baseada no contexto.

O recibo local detalhado está em `docs/architecture/arc13-source-review-2026-11-12.md` na branch local indicada. Nenhuma alteração de runtime, catálogo de mensagens, preview, deploy, banco, merge ou ref remota foi feita nesta retomada. A higiene continua em 7 refs no Product (duas acima do soft cap de 5) e 2 no Design System; a PR #272 continua preparada, não integrada.


## Retomada ARC-13 — fontes de texto, testes e controles do Admin (12/11/2026 BRT)

O Product continua ancorado em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. O trabalho ARC-13 permanece isolado na branch local `work/arc13-ui-inventory-20261112`, agora em `fb92edbc84fda44d19a68eed4fedb8326090c8d3` (commit `fb92edb`); não foi criado um ref remoto nem PR do Product.

- A ferramenta local passou a schema 3 e preserva duas listas diferentes: **1.011 ocorrências candidatas de sink** (600 HTML + 411 JavaScript) e **143 literais de origem JavaScript** em `sourceEntries`. As fontes não são somadas aos sinks. Há 167 sinks JS estáticos e 244 dinâmicos/mistos; 22 exclusões; 66 arquivos com hash; zero erros de análise, owners não atribuídos ou rotas JS não atribuídas. Tudo segue `unreviewed`.
- Entre as 143 fontes, 89 têm consumidor ativo documentado, 7 labels de vista são passados ao renderizador mas não usados, 2 campos da Landing não têm consumidor ativo e 45 mensagens de `Error` ainda precisam de rastreio antes de classificar como texto de usuário ou diagnóstico. A cobertura inclui tabelas de Como funciona/navegação/tema, textos da Landing e do Viewer e opções fixas do Admin. Dados editáveis do V5 e conteúdo comercial continuam fora de uma classificação automática.
- O número anterior “988 candidatos” era 600 sinks HTML + 388 sinks JavaScript; não representa 988 testes nem 988 mensagens únicas. A cobertura adicionada aumentou o número de sítios reconhecidos sem alterar o código do produto. Os recortes manuais 546/280/230 pertencem ao snapshot de 996 sinks; compartilham módulos e precisam ser reconciliados antes de virar porcentagem de cobertura.
- A validação padrão do Configurador encadeia 19 scripts Node e 2 validadores de assets. Nenhuma suíte foi executada nesta etapa e não houve auditoria de sobreposição entre asserções; quantidade e nomes de arquivos, sozinhos, não demonstram redundância.
- Os dois checks mostrados no Admin têm funções diferentes: checkbox por item para estado inicial, e toggle de disponibilidade da etapa. O primeiro não declara `accent-color` em `initial-state-option`; o segundo usa `var(--accent)` em `.switch`. A diferença de cor é explicada pelo CSS, mas a intenção de hierarquia visual continua sem decisão. Nenhum checkbox foi alterado.

A revisão detalhada está no checkout local do Product em `docs/architecture/arc13-source-review-2026-11-12.md`. A geração do relatório foi concluída e `git diff --check` passou; a suíte de testes não foi executada. `app/`, runtime, configuração publicada, refs remotas, merges e deploys permaneceram sem alteração. Ref count verificada nesta retomada: Product 7 (2 acima do soft cap 5), Design System 2.


## Retomada ARC-13 — inventário ampliado de fontes (12/11/2026 BRT)

Esta atualização substitui somente as contagens da entrada anterior; os snapshots datados continuam como histórico. O Product permanece em `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`. O scanner e o relatório estão na branch local `work/arc13-ui-inventory-20261112@ca897cb38960e6b10dd40c7574320810fd7c0516`; não há ref remoto nem PR de Product para este lote.

- O relatório separado por proveniência contém **1.012 sinks candidatos** (600 HTML + 412 JavaScript; 167 JS estáticos e 245 dinâmicos/mistos) e **310 fontes JavaScript** (277 ativas, 7 passadas ao renderer mas não usadas, 2 sem consumidor e 24 mensagens de Error sem fluxo resolvido). Há 68 fontes com referências delimitadas a sinks (70 relações); 22 exclusões e zero erros de parser, owners ausentes ou rotas JS sem atribuição.
- A cobertura adicionou campos selecionados de defaults do Configurador, catálogo, cena e PriceBook, além dos quatro rótulos compactos que alimentam `data-compact-label` e CSS `attr()`. São pistas de domínio/consumidor, não classificação de tradução. Todos os registros continuam `unreviewed`; não há catálogo pt-BR no runtime.
- A análise dos dois checkboxes do Admin mantém variantes semânticas separadas: estado inicial do item (accent padrão do navegador) e disponibilidade da etapa (token `--accent`). A intenção da diferença de ênfase segue sem decisão; nenhum controle foi alterado.
- A geração local do inventário concluiu com zero erros de parse e `git diff --check` sem erro de whitespace. Nenhuma suíte de testes foi executada; `app/`, Product main, conteúdo publicado, banco, deploy e merge permaneceram inalterados.
- A contagem live de refs continua em **7 no Product** e **2 no Design System**. Product mantém `main`, `development` e cinco branches de trabalho; #272 segue aberta e não integrada, com o lote exato de #270 e limpeza condicional preparados. Nenhuma ref foi removida. A PR #119 continua Draft na branch documental existente; esta atualização não cria ref.
- G0 contínuo; G1 parcial; G2 em andamento; G3 parcial; G4/G6 HOLD; G5 parcial/HOLD; G7 pendente; G8 sem release. O workflow UX-04 tem arquivo em `development` e a execução local no SHA exato já foi registrada, mas o arquivo não existe em Product `main`; a página do Actions não expõe Run workflow. Não houve execução Linux/Node 22 neste SHA nem novo push para provocá-la.

### Próxima sequência

1. Revisar e classificar fontes por domínio e consumidor, reconciliando os recortes manuais antigos antes de calcular cobertura.
2. Manter G1 marcado parcial até existir execução Linux/Node 22 no SHA apropriado e fechar os critérios de dispositivo/toque/zoom; não criar branch ou empurrar commit só para disparar Actions.
3. Prosseguir o ownership G3 por família e estados. Não extrair CSS, globalizar tokens ou consolidar componentes antes das provas e decisões visuais aplicáveis.
4. Tratar #272 como preparado, não executado; o hardening da limpeza exige integração autorizada e readback exato.

## Reconciliação live do plano arquitetural — 13/11/2026

- **Produto live:** `main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, 5 refs. A #272 foi integrada e removeu somente as refs exatas do lote de higiene; o merge não alterou `app/`. As PRs #269, #271 e #273 permanecem abertas; revalidar comparação e base antes de integrar.
- **Design System live:** `main@79db735d6f05177b0c406e383d35832f3d72fdef`; 2 refs e PR #119 Draft na branch documental existente. Este lote atualiza a mesma PR e não cria uma ref.
- **ARC-13 local:** `work/arc13-ui-inventory-20261112@3b97542482ff9c1bdb2ad45aabf777f97991e60f`, limpo, 17 commits à frente do Product `main@bb3e3a3`, sem ref remota nem PR. O relatório `architecture/arc13/ui-text-candidates.json` tem SHA-256 `8765873a096fe95167e4fba74838258e47428fab0e12d16af9b6c92a3e34a51e`, com 1.012 sinks e 359 fontes. Quatro recibos cobrem exatamente 1.012/1.012 IDs de sink e três recibos cobrem 359/359 IDs de fonte. O parecer reconcilia 27 valores literais compartilhados (65 sinks), sem grupo de sink com classificação conflitante nem colisão entre nomes de chave propostos. As fontes são 110 `ui_copy`, 27 `editorial_copy`, 143 `domain_content`, 4 comerciais, 65 diagnósticos, 1 mensagem de sistema, 7 passadas mas não usadas e 2 sem consumidor.
- **Lacuna de catálogo e locale:** `displayAxes` foi incluído como dado técnico de catálogo e seu consumidor de resumo está ligado ao sink do Configurador. A cobertura desse campo está fechada; ordem dos eixos, unidade, separador, sinal de multiplicação e localização para novos locales continuam decisões de owner. O inventário segue limitado e não afirma cobertura lexical/runtime completa.
- **Controles do Admin — Common Sense Judge:** sete contratos foram separados apesar da primitiva comum. Estado inicial de entidade usa visibilidade no Configurador; serviço registra seleção inicial; Viewer tem visibilidade própria; etapa altera `stage.enabled`; acabamento e puxador compartilham “Disponível para clientes”, mas mantêm regras diferentes; checkboxes de associação/propriedade não são toggles gerais; publicação de preços muda apenas o rascunho. O literal “Iniciar ativo” ocorre tanto no ramo de objeto quanto no de serviço, então o screenshot não identifica o subtipo sem o contexto do item. A diferença azul nativo/marca vem do CSS, mas não prova hierarquia deliberada.
- **Pendências do inventário:** P1 — alinhar nomes acessíveis de módulo/objeto/etapa à função observada e decidir se “Disponível para clientes” deve esclarecer que o rascunho só vale após publicação. P2 — decidir feedback para a regra de última opção; accent e hierarquia entre famílias, incluindo o accent ausente em “Sem cor/tinta base”; e a exceção de foco de 3 px no controle de preços. Antes de aprovar mudança visual, falta revisar claro/escuro, teclado/foco, marcado/desmarcado, disabled por motivo, leitor de tela e contraste computado. O julgamento é estático e não aprova mudanças no produto.
- **Progresso arquitetural:** segue estimado em cerca de 30% (faixa 25–35%), sem métrica formal nem previsão de calendário. A classificação de fontes do inventário avançou; ARC-13 permanece parcial porque cobertura lexical, políticas/owners e gates de consumidores seguem abertos.
- **Validação deste lote:** o gerador ARC-13 foi executado; contagens e os IDs de fonte/sink foram reconciliados, os JSONs foram analisados e `git diff --check` passou. Nenhuma suíte foi executada. O commit Product `3b97542` contém somente documentação, inventário e scanner; nenhum arquivo `app/` mudou. Sem merge, deploy de produção, operação de banco, alteração de ref remota ou mudança em código de runtime.

## Continuação G3 — ownership estático de `.visually-hidden` — 13/11/2026

No Product `main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7`, confirmei duas regras idênticas de `.visually-hidden` em `admin/admin.css:157` e `styles.css:853`, consumidas respectivamente pelo `<strong>` estático no header Admin e pelo `<h1>` do Configurador. As rotas carregam folhas diferentes e nunca co-carregam essas regras; ambas carregam `ui-theme.css` depois, sem override da classe. A declaração não usa tokens, variantes de tema, breakpoint ou estado. `.sr-only` mantém outro contrato no Configurador e não foi agrupado.

**Resultado:** classificação G3 estática concluída para esta família; sem extração G4, pois não há benefício de payload/cache medido e uma regra no stylesheet de tema afetaria mais rotas. O relatório registra os limites (sem CSSOM, leitor de tela, impressão ou waterfall) e os blobs-fonte em [g3-visually-hidden-source-refresh-2026-11-13.md](../evidence/architecture/g3-visually-hidden-source-refresh-2026-11-13.md). G3 geral continua parcial. As matrizes estáticas de marca/logo e dos controles do Admin estão registradas no adendo subsequente; pendências de runtime e decisões de design permanecem abertas. Nenhum código do Produto, teste ou ref remota foi alterado nesta etapa.

## Continuação G3 — slots de marca e estados de checkbox — 13/11/2026

O inventário estático de marca distingue o mecanismo de seleção de variantes claro/escuro dos slots de shell público, Viewer, cabeçalhos privados, splash, comparação e rodapé. O hero da Home é raster independente: a correção do logo inventado pertence à arte, e a composição de vídeo no telefone deve seguir separada do slot de cabeçalho. A auditoria está em [g3-brand-logo-slots-static-audit-2026-11-13.md](../evidence/architecture/g3-brand-logo-slots-static-audit-2026-11-13.md).

O julgamento dos controles do Admin preserva os contratos de estado inicial, visibilidade, disponibilidade, associação e publicação como distintos. Só “Disponível para clientes” pode compartilhar texto/chave nos dois usos observados. A diferença de accent entre .initial-state-option e .switch fica como decisão de design; os nomes acessíveis e a exceção de foco de preços também precisam de revisão. O relatório [g3-admin-control-state-judgment-2026-11-13.md](../evidence/architecture/g3-admin-control-state-judgment-2026-11-13.md) registra decisões pendentes sem alterar a interface. Fonte do Produto: ref local origin/main@bb3e3a3; não verificada contra remoto nesta passagem.

**Estado:** G3 permanece parcial; estas duas famílias têm classificação estática suficiente para orientar o inventário, não para aprovar mudança visual, acessibilidade em runtime ou extração G4. Sem testes, código de Produto ou novas refs remotas.

## Continuação G3 — matriz de componentes e estados por shell — 13/11/2026

A leitura estática no Product main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7 classifica .button como homônimo por shell, .eyebrow como rótulo contextual, .scene-hotspot como contrato DOM/JS comum com skins separadas e status/erro por fluxo. As regras de foco/desabilitado foram mapeadas por dono sem afirmar equivalência visual. A matriz e o plano de validação runtime estão em [g3-control-families-static-matrix-2026-11-13.md](../evidence/architecture/g3-control-families-static-matrix-2026-11-13.md).

**Estado:** subgates de ownership estático avançaram para estas famílias. G3 geral permanece parcial e G4/G5 seguem sem autorização de extração. As pendências agora são específicas: revisão de botão por shell/estado, foco/empilhamento de hotspot em cenas reais e leitura/contraste de mensagens em fluxos representativos. Nenhum código de produto foi alterado e nenhuma suíte foi executada.


## Continuação G3 — baseline CSSOM dos CTAs públicos — 14/11/2026

A baseline local observou CTAs da Home, Sobre e Como funciona em claro/escuro e desktop/mobile (12 combinações, 32 elementos), mais hover e foco visível para quatro famílias representativas (16 estados). O cabeçalho reduz de 176×42 px para 38×38 px mantendo `aria-label`. As variantes preenchidas mantêm tratamentos por shell/classe; o link textual da Home permanece distinto. Na Home, a animação concluída `public-reveal` mantém a propriedade `transform` e neutraliza a elevação de 2 px pedida pelo hover; em Sobre a elevação ocorre. Isto gera uma pendência P2 de intenção, não um bug confirmado. A fonte do foco declara 3 px; o Chromium desta coleta calculou 2,66667 px após estabilização.

A [baseline](../evidence/architecture/g3-public-button-runtime-baseline-2026-11-14.md) e seu [recibo JSON](../evidence/architecture/g3-public-button-runtime-baseline-2026-11-14.json) registram fontes, folhas/ordem CSS, medidas, métodos e limites. A captura PNG do DevTools expirou; não há imagem anexada. A página local usou Product main `bb3e3a3` (mesma árvore `app` no checkout `db908e5`). Sem Deploy Preview, leitor de tela, Tab real, Safari/iPad, alteração UI ou suíte de aplicação. G3 permanece parcial e não há aprovação de extração CSS.


## Revisão de senso comum — estados de controles Admin — 14/11/2026

Uma revisora independente comparou os contratos e conferiu o Product em `work/arc13-ui-inventory-20261112@db908e5`. “Iniciar ativo” permanece ambíguo na imagem: o texto é usado tanto para visibilidade inicial de objeto quanto para seleção inicial de serviço. “Ativa” é produzido pelo controle de disponibilidade de etapa, embora a captura não mostre o cartão. A cor diferente vem das regras de CSS; não há evidência suficiente para dizer que a hierarquia visual foi intencional.

O inventário mantém sete contratos, compartilha apenas a casca/copy que a função permite e conserva pendentes seis decisões: copy/nome acessível por tipo e efeito; nome acessível de etapa em estado marcado; indicação da publicação para “Disponível para clientes”; accent/hierarquia para checks discretos e “Sem cor/tinta base”; feedback para a última opção; exceção de foco 3 px no controle de preço. A revisão detalhada no Product local (`docs/architecture/arc13/reviews/2026-11-14/admin-control-common-sense-review.md`) registra IDs, responsáveis e validação necessária. Nenhuma UI foi alterada e nenhum teste foi executado.
