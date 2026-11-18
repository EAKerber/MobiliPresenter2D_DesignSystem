# MobiliPresenter2D Design System

> **ESTADO ATUAL (18/11/2026, BRT; pins revalidados):** Product `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` permanece publicado após #277; deploy `6afa7bee50b552356a973df4` está READY. Product tem 8 refs, três acima do soft cap 5. #269 permanece Draft; #271 está aberta; #274 segue Draft no head `ff2fd40fdbc40eae2a53f8be6ba4a24af3eaea82`; #278 e #279 também permanecem Draft. A PR Draft #280 está no head `bf685e22338597f47d240c616473085d86a22cb8`; o Mobile browser #802 passou com 256 casos, quatro capturas e zero erros, e os seis workflows associados ao head passaram. O `test.json` e as quatro imagens do artefato no [run #802](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/44213833429) foram revisados: nomes, módulos selecionados e camadas visíveis coincidem; uma faceta vertical translúcida aparece no caso `module-05-off` e fica registrada para acompanhamento visual, sem referência de pixels que permita classificá-la como regressão. A fixture compartilhada termina quando o runner descartável do job termina; não há evidência de vazamento entre jobs. Teardown explícito nos cinco workflows consumidores fica como higiene de TST-006, de baixo risco e sem bloquear TST-007. A PR permanece Draft aguardando integração/readback conforme o plano. O [recibo pós-#277](evidence/architecture/product-main-post-277-readback-2026-11-16.md) registra os limites da publicação. O mapa DOM-001 V5 foi acrescentado à #274 e segue em revisão; no head atual, Current asset gates #1262, About skip-link #65 e Deploy Preview passaram. Design System `main@79db735d6f05177b0c406e383d35832f3d72fdef` mantém 2 refs; [#119](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/119) segue Draft na branch documental; o head e os checks atuais estão no corpo da PR.

> **ARC-13 pós-#277 (17/11/2026):** Product #274, head `7de76978efcc29cbb45cd4df6f6e6d601e32de5d`, usa a base atual e registra 1.026 ocorrências candidatas, 360 fontes JS, 420 ocorrências HTML mapeadas à autoria e zero sem origem técnica no recorte. O relatório válido tem SHA-256 `abce38889ad6d78c634fadad5d6f0c63fd9706ac3e0c13bcdf13f78010caeb9e`; a reconciliação e o crosswalk estão [na PR #274](https://github.com/EAKerber/MobiliPresenter2D/pull/274). “Zero sem origem” não significa aprovação semântica; as 1.026 ocorrências seguem candidatas. Uma errata liga a decisão histórica do owner ao hash válido, sem apagar a escolha da vírgula nem aprovar alt, chaves ou extração. A apresentação visual do vídeo e controles nas duas páginas foi aceita pela pessoa decisora. Pareamento semântico e revisão com tecnologia assistiva continuam separados.

> **ARC-15 live (17/11/2026):** a auditoria focal do `test-core.js` confirmou overlaps parciais entre camadas, sem teste inteiro redundante; a divisão do arquivo fica como dívida de legibilidade. O contrato de tema mantém uma divergência estática de URLs entre shells. A PR Draft #280 agora usa o Configurador `/config/` em loopback; o head `bf685e2` passou nos 256 estados do modelo, nos quatro nomes/cenários de captura, no readback das camadas renderizadas e nos asserts de vidro/z-order/ARIA/erros de página. O manifesto e as quatro imagens foram conferidos; os estados concordam com as camadas visíveis. Uma faceta vertical translúcida no caso `module-05-off` fica anotada sem comparação pixel a pixel. A fixture é sintética, local e anônima; não valida configuração publicada, autenticação ou produção. A fixture compartilhada fica viva durante as etapas do job e o runner descartável a encerra ao final; teardown explícito nos cinco consumidores é melhoria de higiene TST-006, não bloqueio de funcionamento. TST-007 está em revisão com evidência técnica aprovada; GIT-017 ainda depende de integração/readback. Veja [ARC-15](docs/architecture/ARC15_VERIFICATION_INVENTORY_2026-11-15.md) e o [handover atual](docs/HANDOVER_CURRENT.md).

> **ARC-13 do Produto — baseline histórica anterior às #275 e #277:** os números e disposições abaixo pertencem a Product `main@46a52e76` e não descrevem a main atual. O delta foi reavaliado no relatório de ARC-13 linkado no estado atual acima; nenhuma chave canônica ou extração de runtime foi aprovada. Veja também o [recibo de leitura da main após #277](evidence/architecture/product-main-post-277-readback-2026-11-16.md).

> **GOVERNANÇA ATUAL (14/11/2026):** [Higiene de branches — mecanismo, critérios, operação e HOLDs](docs/BRANCH_HYGIENE_OPERATIONS.md); [D01–D04 aprovadas](docs/APPROVALS_D01_D04_2026-10-26.md); [extração seletiva da PR #51](docs/HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md). `decisions.json` é a fonte de decisões; os documentos abaixo são checkpoints datados, não o estado atual automaticamente. **Política de refs:** no Design System, meta/soft cap de 2; no produto, soft cap de 5 enquanto há trabalho ativo e meta de 2 quando estável (`main` + `development`). Ao chegar a 5, revisar se faz sentido um hard cap; 5 não é hard cap nem autorização para apagar. Toda remoção exige prova, lote aprovado e readback.

## Checkpoints históricos (21–22/10; preservados como evidência datada)

> **CHECKPOINT HISTÓRICO (22/10/2026; não é mais o atual):** [estado verificado de MobiliPresenter2D + Design System, HEADs, PRs, issues, branches, gates e próximo ARC-03C](docs/ARCHITECTURE_CURRENT_HANDOVER_2026-10-22.md). Preservado como observação datada, sem prevalecer sobre decisões e handovers posteriores; **ARC-03B 60/60 PASS somente em branch**, #232 auth test fixture aberta, #233 corrigida, PR produto #231 DRAFT/HOLD. Sempre conferir HEAD live antes de atuar.


> **ARC-03B (22/10):** [páginas de autoria separadas e compilador HTML com diferencial 60/60 PASS](docs/ARC03B_AUTHORED_PAGES_STATIC_COMPILER_BROWSER_GATE_2026-10-22.md). Três headers públicos testados em Chromium/WebKit, cinco larguras e dois temas, sem diferença visual nem mudança do build de produção. Próximo gate: ARC-03C — integração da geração ao build real; #232 auth pendente, #233 resolvida.


> **22/10 — CI-BASELINE-01 e ARC-03:** [#233 concluída na main do produto; #232 (fixture autenticada) permanece aberta; protótipo de fragmento do header público 3/3 PASS sem runtime](docs/CI_BASELINE_01_RESOLUTION_AND_ARC03_HEADER_PROBE_2026-10-22.md). Não confundir protótipo de build-time com migração publicada. PR de tokens #231 continua DRAFT/HOLD.


> **CI-BASELINE-01 (22/10):** [diagnóstico de redirecionamento protegido, correção de testes públicos e issues #232/#233](docs/CI_BASELINE_01_AUTH_READINESS_AND_PROJECTION_2026-10-22.md). Na produção e no preview #231, acessos anônimos a `/config/` vão para `/access/`, explicando gates de navegador que esperavam o Configurador sem sessão. Assertions CP-PUBLIC-02a corrigidas em branch/testes PASS; **nenhuma correção foi integrada ao produto e PR #231 segue DRAFT/HOLD**.


> **Integração P-TOKEN-02B (22/10):** [PR de produto #231 em DRAFT/HOLD após triagem de CI preexistente](docs/P_TOKEN_02B_PR231_INTEGRATION_HOLD_BASELINE_CI_2026-10-22.md). Gate contextual 48/48 PASS, mas checks globais de Configurador e allowlist permanecem vermelhos também na main. Um único Deploy Preview automático foi gerado; nenhum merge/publicação realizado.


> **P-TOKEN-02B — gate 48/48 PASS (22/10):** [evidência e handover definitivo](docs/P_TOKEN_02B_GATE_PASS_AND_INTEGRATION_HANDOVER_2026-10-22.md). Três consumidores textuais VIS-002 no produto, propriedade contextual DS com CSS computado e screenshots idênticos à main (Chromium/WebKit). **Branch técnica validada, sem PR/merge/Deploy Preview de produto**; paleta global NÃO ativada.


> **P-TOKEN-01B/02A (22/10, execução comprovada):** [pin DS→produto e auditoria CSSOM 32/32](docs/P_TOKEN_01B_02A_PRODUCT_INTEGRATION_AND_COMPUTED_AUDIT_2026-10-22.md). Exportador DS em `main@70f0eab`; cópia versionada em branch independente do produto, **fora de `app/`**, sem CSS ativo, PR do produto, merge ou Deploy Preview. Prova lexical de 54 correspondências, sem autorizar mapeamento global ou mudança visual.


> **P-TOKEN-01 — fonte executável de tokens de referência:** [exportador e contrato de ativação VIS-002](docs/P_TOKEN_01_EXECUTABLE_REFERENCE_PALETTE_2026-10-22.md). A geração é determinística e validada em CI; os tokens `--ds-reference-*` ainda **não** são aplicados no CSS do produto por falta de mapeamento de componentes homologado.


> **P-COMP-01 validado em branch (21/10):** [implementação Vanilla, 40 diferenciais + 16 funcionais + NAV-005 20/20 PASS](docs/P_COMP_01_PUBLIC_MENU_IMPLEMENTATION_GATE_2026-10-21.md). Branch de produto `architecture/p-comp-01-public-menu-20261021@4ba9384` permanece **sem merge, PR ou deploy**; próximo gate é revisão de integração, independente do P-TOKEN-01.


> **V0-B auditado (21/10):** [fontes JS, co-carregamento CSS, pontos cegos i18n e primeiro piloto](docs/V0B_SOURCE_COVERAGE_CSS_OWNERSHIP_AND_FIRST_PATCH_GATE_2026-10-21.md). 54 fontes JS contabilizadas (52 lidas, 2 dados grandes não inspecionados), 84 nomes CSS em múltiplas folhas (69 co-carregados em alguma rota, **não** 69 bugs). P-COMP-01/menu público está **especificado, não implementado**; teste runtime permanece pendente.


> **V0-A realizado (21/10/2026):** [auditoria pós-PR #230, ownership, textos e build](docs/V0A_POST230_OWNERSHIP_LOCALIZATION_AND_BUILD_AUDIT_2026-10-21.md). Foram mapeados 14 contratos/famílias e indexadas 826 ocorrências *candidatas* de localização em 26 fontes; **não** são strings aprovadas nem cobertura integral. V0-B e gates runtime permanecem pendentes. Sem código de produto alterado.


> **Direção arquitetural aprovada (21/10; contrato vigente):** stack de interface exclusivamente **HTML/CSS/JS puros**; tokens e componentes nativos como base de TODAS as páginas (inclusive Landing); configuração por dados para Configurador/Viewer e ferramentas derivadas do seu núcleo. Consultar [arquitetura confirmada, gates e decisões técnicas pendentes](docs/ARCHITECTURE_VANILLA_COMPONENTS_AND_DOMAIN_DATA_2026-10-21.md). O plano experimental da PR #39 não equivale a framework adotado. A situação atual do Produto está no bloco datado de 13/11 acima.


Registro de decisões de design, estado de homologação e evidências recuperadas dos chats do inventário.

- [`index.html`](index.html): documento visual navegável, independente e sem dependências.
- [**ARC-01…ARC-16 — contrato arquitetural consolidado e roadmap de execução**](docs/ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md): decisões das quatro rodadas, tokens/componentes Vanilla, extração abrangente de textos, governança e gates de migração. **Ler antes dos planos experimentais da PR #39**.
- [`docs/ROADMAP_AND_CURRENT_STAGE_2026-10-21.md`](docs/ROADMAP_AND_CURRENT_STAGE_2026-10-21.md): plano geral, etapa atual, critérios de conformidade e continuidade.
- [`decisions.json`](decisions.json): registro estruturado das decisões, pendências, limites e itens a recuperar.
- [**Contratos de navegação por profundidade e preflight obrigatório**](docs/NAVIGATION_DEPTH_AUTHORITY_GATE_2026-10-21.md): índice NAV-004/NAV-005 por primeiro nível, Viewer (profundidade 2) e áreas privadas. **Consultar antes de abrir issue, planejar header ou modificar UI**; não usar memória de chat como fonte de homologação.
- [`DECISION_APPLICATION_MAP.md`](DECISION_APPLICATION_MAP.md): cruzamento de decisões com rotas, HTML, CSS carregado e evidência runtime.
- [`RUNTIME_AUDIT.md`](RUNTIME_AUDIT.md) e [`runtime-evidence.json`](runtime-evidence.json): observações de navegação, estados de sessão, capturas e limites da auditoria no site publicado.
- [`FINDINGS_REGISTER.md`](FINDINGS_REGISTER.md): registro de defeitos observados, inconsistências, homologações, decisões incompletas e limites.
- [`PALETTE_CONFORMANCE.md`](PALETTE_CONFORMANCE.md): paleta classificada por estado, mudanças necessárias e critérios verificáveis de conformidade.

- [**Handover MobiliPresenter2D — preview #230 (21/10/2026)**](docs/HANDOVER_MOBILIPRESENTER2D_PREVIEW230_2026-10-21.md): situação atual da PR, ordem NAV-005 corrigida, feedback visual, testes, bloqueios de autenticação, preço e próximos gates. Ler antes de retomar produto ou preparar merge.

## Como ler

- “Direção aprovada” registra acordo conceitual; não significa que todos os valores visuais foram fixados nem autoriza implementar no produto.
- Referências de cor, candidatos e experiências do laboratório permanecem separados dos tokens oficiais.
- Lacunas nos checkpoints são declaradas sem completar conteúdo por inferência.

## Fontes

Chats “Inventário De Design System” e “Continuar Inventário Design System”, incluindo checkpoints cumulativos até EST-08 e decisões EST-09/10, além das direções fornecidas pelo usuário nesta conversa.


## Estado do produto

O [inventário estático](VISUAL_INVENTORY.md) e o mapa de aplicação apontam para o commit do produto `1878ae1`. A reconciliação do delta desde o snapshot anterior e as verificações runtime estão registradas em [INVENTORY_REFRESH_2026-10-20.md](INVENTORY_REFRESH_2026-10-20.md) e [PRODUCT_RECONCILIATION_2026-10-19.md](PRODUCT_RECONCILIATION_2026-10-19.md).
