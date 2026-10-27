# D04 — preservação seletiva de ownership e fluxos críticos (27/10/2026)

**Objetivo:** preservar conhecimento verificável sem fundir propostas, workflows ou código experimental. Todos os nove arquivos deste lote são copiados pelo Git Blob SHA exato e registrados no [manifesto verificável](DS_D04_OWNERSHIP_AND_ADMIN_BLOBS_2026-10-27.json).

## 1. Da PR #39 — ownership e cruzamento estático

Origem imutável: [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39), head `8e7d857528c9ea14fa45c3f58b57c07c7036bca0`.

- [Baseline DOM/CSS](architecture/dom-css-consolidation-baseline-2026-10-20.md): colisões lexicais não são necessariamente colisões de cascade em runtime; estilos equivalentes exigem verificar rota, tema e estado.
- [Crosswalk JSON](architecture/dom-css-static-crosswalk-2026-10-20.json): mapeamento de fonte, classes e folhas, read-only; **não** equivale a DOM computado nem prova de homologação.
- [Ownership DOM/JS](architecture/dom-js-component-ownership-2026-10-20.md): consumidores e donos de markup/JS, advertindo contra compartilhamento artificial entre Landing/Viewer/Admin.

**Classificação:** evidência de arquitetura datada, não plano de implementação aprovado. Propostas de controlador, ADRs e experimentos em `experiments/` continuam na PR #39 sob HOLD; os 2 workflows históricos não devem ser copiados a `.github/workflows/`.

## 2. Da PR #51 — seis rastreios ARC-13 de fronteiras críticas

Origem: [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), head `28062602a4ddcd1bee090742fe2587fe3837175d`; produto observado pelos rastreios: `MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, arquivos identificados individualmente nos próprios documentos.

| Evidência preservada | Contrato/risco a manter na futura refatoração |
| --- | --- |
| [Admin inicialização](../evidence/architecture/arc13-admin-initializeAdminAccess-consumer-trace-2026-10-25.md) | Fallback de erro, callback auth e possível falha do segundo `getUser()`; sem autenticação runtime verificada |
| [Login](../evidence/architecture/arc13-admin-loginForm-submit-consumer-trace-2026-10-25.md) | Diferenciar falha estática de mensagem dinâmica de provider; não presumir que `error.message` é seguro |
| [Senha/convite](../evidence/architecture/arc13-admin-passwordActionForm-submit-consumer-trace-2026-10-25.md) | Diferenciar convite/recuperação de senha e mensagens dinâmicas; sanitização/owner de auth pendente |
| [Carregar configuração](../evidence/architecture/arc13-admin-loadSettings-consumer-trace-2026-10-25.md) | Estado 404 vs erro HTTP genérico; template da revisão; retry é fronteira externa |
| [Publicação](../evidence/architecture/arc13-admin-savebutton-consumer-trace-2026-10-25.md) | Guardrails de v5 vs legado, 401/403, 409, conflitos, resposta inesperada e readback: não anunciar sucesso prematuramente |
| [Persistência específica de puxadores v3](../evidence/architecture/arc13-admin-handles-persistence-consumer-trace-2026-10-25.md) | Operação destrutiva limitada, confirmação de rascunho, preservação de escopo, revisão e readback; **não** promover ao modelo v5 |

**Classificação:** rastreios estáticos e critérios de cuidado; *não* certificam segurança, backend, sessão, textos traduzidos, persistência ou comportamento atual. São particularmente úteis à futura direção data-driven/localização, mas **não contêm chaves de localização homologadas**.

## 3. Gates e próximos lotes

- **Preservação exata:** 9 blobs (3 de #39 + 6 de #51) com paths e SHAs originais; sem alterar `decisions.json`, índice canônico, workflows, código ou repositório de produto.
- Comparação por árvore com base `main@52695179d776009378e96ca4d51667948593a625`: #39 tinha 24 exclusivos, restam **21** após esta extração; #51 tinha 207, restam **201**, contagens válidas enquanto os HEADs das fontes permanecerem fixos.
- Seguem HOLD: demais ADRs/propostas/experimentos de #39; 38 lotes JSON ARC-13 de #51 (~1,78 MB), 69 rastreios consumer não selecionados, outros documentos/JSON, evidências runtime e 11 arquivos divergentes. Não apagar refs sob o argumento de que um manifesto de SHA sozinho preserva bytes.
- O próximo gate deve avaliar a utilidade dos rastreios restantes por contrato (autenticação, foco, acessibilidade, mensagens, preços, domínio, tradução) e conferir os batch JSON por versão do produto e cobertura antes de qualquer seleção volumosa. Não ativar automações ou refatorações por analogia.
