# MobiliPresenter2D Design System

> **P-TOKEN-01B/02A (22/10, execução comprovada):** [pin DS→produto e auditoria CSSOM 32/32](docs/P_TOKEN_01B_02A_PRODUCT_INTEGRATION_AND_COMPUTED_AUDIT_2026-10-22.md). Exportador DS em `main@70f0eab`; cópia versionada em branch independente do produto, **fora de `app/`**, sem CSS ativo, PR do produto, merge ou Deploy Preview. Prova lexical de 54 correspondências, sem autorizar mapeamento global ou mudança visual.


> **P-TOKEN-01 — fonte executável de tokens de referência:** [exportador e contrato de ativação VIS-002](docs/P_TOKEN_01_EXECUTABLE_REFERENCE_PALETTE_2026-10-22.md). A geração é determinística e validada em CI; os tokens `--ds-reference-*` ainda **não** são aplicados no CSS do produto por falta de mapeamento de componentes homologado.


> **P-COMP-01 validado em branch (21/10):** [implementação Vanilla, 40 diferenciais + 16 funcionais + NAV-005 20/20 PASS](docs/P_COMP_01_PUBLIC_MENU_IMPLEMENTATION_GATE_2026-10-21.md). Branch de produto `architecture/p-comp-01-public-menu-20261021@4ba9384` permanece **sem merge, PR ou deploy**; próximo gate é revisão de integração, independente do P-TOKEN-01.


> **V0-B auditado (21/10):** [fontes JS, co-carregamento CSS, pontos cegos i18n e primeiro piloto](docs/V0B_SOURCE_COVERAGE_CSS_OWNERSHIP_AND_FIRST_PATCH_GATE_2026-10-21.md). 54 fontes JS contabilizadas (52 lidas, 2 dados grandes não inspecionados), 84 nomes CSS em múltiplas folhas (69 co-carregados em alguma rota, **não** 69 bugs). P-COMP-01/menu público está **especificado, não implementado**; teste runtime permanece pendente.


> **V0-A realizado (21/10/2026):** [auditoria pós-PR #230, ownership, textos e build](docs/V0A_POST230_OWNERSHIP_LOCALIZATION_AND_BUILD_AUDIT_2026-10-21.md). Foram mapeados 14 contratos/famílias e indexadas 826 ocorrências *candidatas* de localização em 26 fontes; **não** são strings aprovadas nem cobertura integral. V0-B e gates runtime permanecem pendentes. Sem código de produto alterado.


> **Direção arquitetural atual (21/10):** stack de interface exclusivamente **HTML/CSS/JS puros**; tokens e componentes nativos como base de TODAS as páginas (inclusive Landing); configuração por dados para Configurador/Viewer e ferramentas derivadas do seu núcleo. Consultar [arquitetura confirmada, gates e decisões técnicas pendentes](docs/ARCHITECTURE_VANILLA_COMPONENTS_AND_DOMAIN_DATA_2026-10-21.md). O plano experimental da PR #39 não equivale a framework adotado. Produto em `main@840a0cd`, PR #230 mesclada; conferir head ao retomar.


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
