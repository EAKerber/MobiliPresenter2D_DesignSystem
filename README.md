# MobiliPresenter2D Design System

Registro de decisões de design, estado de homologação e evidências recuperadas dos chats do inventário.

- [`index.html`](index.html): documento visual navegável, independente e sem dependências.
- [`decisions.json`](decisions.json): registro estruturado das decisões, pendências, limites e itens a recuperar.
- [`DECISION_APPLICATION_MAP.md`](DECISION_APPLICATION_MAP.md): cruzamento de decisões com rotas, HTML, CSS carregado e evidência runtime.
- [`RUNTIME_AUDIT.md`](RUNTIME_AUDIT.md) e [`runtime-evidence.json`](runtime-evidence.json): observações de navegação, estados de sessão, capturas e limites da auditoria no site publicado.
- [`FINDINGS_REGISTER.md`](FINDINGS_REGISTER.md): registro de defeitos observados, inconsistências, homologações, decisões incompletas e limites.
- [`PALETTE_CONFORMANCE.md`](PALETTE_CONFORMANCE.md): paleta classificada por estado, mudanças necessárias e critérios verificáveis de conformidade.

## Retomada prioritária — arquitetura CSS e componentes (20/10/2026)

Para retomar a consolidação sem depender de um chat anterior, ler nesta ordem:

1. [**Plano diretor completo**](docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md): objetivos, fases G0–G8, autoridades, limites, gates, publicação e handoff.
2. [**Prontidão do CSS e gate atual**](docs/architecture/CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md): veredito GO/HOLD/NO-GO, estágio P4-NAV/G1-R, testes que faltam, backlog de conformidade G2 e critérios para extração.
3. [**Ownership CSS / riscos R01–R20**](docs/architecture/CSS-OWNERSHIP-RISKS-2026-10-20.md): classes homônimas, mapeamento por folha/rota, lacunas de compatibilidade, issue IDs e critérios de evidência.
4. [UI-ADR-001](docs/architecture/ui-adr-001-declarative-boundaries-2026-10-20.md) a [UI-ADR-005](docs/architecture/ui-adr-005-public-header-controller-2026-10-20.md): decisões técnicas e pilotos independentes (benefícios declarativos e menu público compartilhado). A PR de arquitetura [#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) permanece **draft** e não é homologação visual.

**Veredito:** folhas CSS são baseline utilizável para avançar em JS/contratos/testes **sem mudá-las**; não há evidência suficiente para centralizar todas as folhas nem considerar a paleta/estados globalmente conformes. `decisions.json` prevalece para direções/homologações, e o registro de achados contém pendências reais. Nenhuma migração de CSS ou merge de produto foi feita nesta etapa documental.

## Como ler

- “Direção aprovada” registra acordo conceitual; não significa que todos os valores visuais foram fixados nem autoriza implementar no produto.
- Referências de cor, candidatos e experiências do laboratório permanecem separados dos tokens oficiais.
- Lacunas nos checkpoints são declaradas sem completar conteúdo por inferência.

## Fontes

Chats “Inventário De Design System” e “Continuar Inventário Design System”, incluindo checkpoints cumulativos até EST-08 e decisões EST-09/10, além das direções fornecidas pelo usuário nesta conversa.


## Estado do produto

O [inventário estático](VISUAL_INVENTORY.md) e o mapa de aplicação apontam para o commit do produto `1878ae1`. A reconciliação do delta desde o snapshot anterior e as verificações runtime estão registradas em [INVENTORY_REFRESH_2026-10-20.md](INVENTORY_REFRESH_2026-10-20.md) e [PRODUCT_RECONCILIATION_2026-10-19.md](PRODUCT_RECONCILIATION_2026-10-19.md).

> **Proveniência:** o inventário JSON de 20/10 mapeia o produto `1878ae1`, mas documentos narrativos e evidências de runtime anteriores mantêm intencionalmente snapshots anteriores; para gates recentes consultar o [plano diretor](docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) e os respectivos relatórios datados.
