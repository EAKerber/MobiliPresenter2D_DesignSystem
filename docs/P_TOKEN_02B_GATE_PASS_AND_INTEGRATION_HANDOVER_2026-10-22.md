# P-TOKEN-02B — gate diferencial final PASS e handover de integração

> **Checkpoint posterior obrigatório (22/10):** [PR #231 aberta como DRAFT, com triagem comparativa da CI](P_TOKEN_02B_PR231_INTEGRATION_HOLD_BASELINE_CI_2026-10-22.md). Embora os 48 testes contextuais tenham PASS, múltiplas workflows gerais de Configurador e projection permanecem vermelhas também na main. **Sem merge/release**; esta seção é evidência do gate específico, não autorização de ignorar a CI global.


**Data:** 2026-10-22. **Status:** **implementação em branch produto / validação diferencial PASS / NÃO INTEGRADO NA MAIN / NÃO PUBLICADO**.

## 1. Fonte de autoridade e estado reproduzível

| Item | Estado verificado |
|---|---|
| Design System — fonte contextual VIS-002 | [PR #50 MERGED](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/50) no commit `8f22b610cf45d01d49ca998a4cd08f7b1a097de3` |
| Fonte canônica | `decisions.json` blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`, `VIS-002.approvedRuntimePairs[0].candidateReplacement` |
| Produto main (baseline do gate) | `EAKerber/MobiliPresenter2D@840a0cda361b3ce215fc934badc26df72dffc6e8` |
| Branch do produto | [`architecture/p-token-02b-contextual-copy-20261022@afb80965336083209eac93e2729de77170524ee5`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/p-token-02b-contextual-copy-20261022) |
| Gate de integração CSS/DOM/pixel | [GitHub Actions #39780241560 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39780241560), SHA `afb80965336083209eac93e2729de77170524ee5` |
| Produto em produção | Main **permanece inalterada** no baseline `840a0cda361b3ce215fc934badc26df72dffc6e8` no último readback; **sem PR de produto, merge ou Deploy Preview** |

## 2. O que realmente passou

- **48/48 cenários**: Landing `/`, Como funciona `/how-it-works/`, Quem somos `/about/` × 320/390/768/1366 CSS px × light/dark × Chromium/WebKit.
- **Fonte/escopo/sintaxe PASS** (`P_TOKEN_02B_SOURCE_PASS`): o CSS gerado pelo DS possui hash idêntico ao PIN, declara `--ds-vis002-approved-support-text-light: #705C4B` estritamente nos três contextos homologados, não usa `:root`, nem é importado por Viewer/Admin/Config/Acesso. O JS de verificação não utiliza framework UI.
- **Computed CSS e geometria equivalentes**: cor, fundo, borda, opacidade, família/tamanho/peso/altura de linha, letter-spacing, alinhamento, largura/altura/posição comparados no elemento-alvo antes/depois. No tema claro, cor publicada `rgb(112,92,75)`; no escuro, cor original preservada e propriedade contextual ausente.
- **Screenshots dos elementos-alvo idênticos, sem exceções**: `P_TOKEN_02B_RASTER_DELTA` = **0**; `P_TOKEN_02B_DIFFERENTIAL_PASS {"scenarios":48,"pixelToleranceUsed":0}`.
- **Relatório de evidência** anexado ao run em `p-token-02b-scoped-text-equivalence`, `artifacts/p-token-02b/result.json`. Artefato GitHub Actions tem retenção temporária; os números e limites são preservados aqui.

**Não confundir** prova de 48 cenários de **elementos textuais contextualizados** com homologação global da paleta, screenshot de página inteira, simulação de fluxo V5, auth, iPad legado ou publicação real.

## 3. Por que o gate demorou, e como evitar nas próximas vezes

O job durou ~22 minutos; `Install browser tools only in isolated CI` foi executada de **12:40:21Z até 13:00:35Z** (~20m14s), enquanto `Match DOM CSS layout and text screenshots in Chromium and WebKit` ocorreu de **13:00:37Z a 13:02:04Z** (~1m27s).

A instalação usa `npm install --no-save --no-package-lock playwright@1.56.0 pngjs@7.0.0` e `npx playwright install --with-deps chromium webkit`. Logs comprovam instalação `apt` de numerosas dependências Ubuntu/WebKit/GStreamer, seguida por download do Chromium. Não há evidência de loop/travamento no teste JS nem de problema do produto.

**Proposta de melhoria de infraestrutura, não aplicada ao SHA aprovado:** em uma mudança de CI **separada**, avaliar job rodando na imagem Playwright oficial versionada e pinada (com dependências e browsers) ou runners pré-provisionados; comparar impacto em GitHub Actions, fidelidade dos browsers, segurança do pin e duração. **Não** retirar dependências WebKit sem demonstrar que o gate permanece representativo; evitar refazer 20 minutos de `apt` sem necessidade.

## 4. Integração governada por ARC-04/14/15/16

**O que este patch faz:** substitui o literal **#705C4B** por custom property gerada do DS, **somente** nas três regras já homologadas, mantendo o seletor e a ordem da cascata. A cor é a mesma; não altera Vue/React, HTML estrutural, V5, Viewer, menus, auth, dados nem preços. A distribuição é versionada com PIN apontando para DS `8f22b610` e manifesto. **Não** promove tokens semânticos globais nem libera os usos futuros de VIS-002.

**Dependência da branch:** `architecture/p-token-02b-contextual-copy-20261022` foi criada a partir da branch pinada `architecture/p-token-01b-reference-pin-20261022@854cc05`, que por sua vez saiu da main. Portanto, o diff `main…P-TOKEN-02B` inclui **P-TOKEN-01B (artefatos inertes, CI e auditoria)**. Em integração futura, revisar esse conjunto como duas unidades lógicas e verificar HEAD atual da main.

**Gates remanescentes até release:** revisão do diff inteiro da branch (inclusive pins inertes), confirmação do HEAD e da política de publicação de deploy preview, integração em PR controlada ou equivalente sem disparar múltiplos previews desnecessários, CI de produto corrente, verificação pós-merge/produção onde necessário, rollback pronto. A evidência local atual **não autoriza concluir release**.

**Próximo incremento técnico:** escolher próximo contexto efetivamente aprovado (por exemplo, `VIS-002.approvedRuntimePairs[1]` `.study-band .eyebrow` em light ou `VIS-003` caption dark), sempre separado da substituição genérica de `--public-bg` e do foco 3px vs referência 4px. Não estender VIS-002 a temas, superfícies ou estados sem homologação específica.

**Veredito:** **P-TOKEN-02B GO para revisão de integração**, **HOLD para merger/release até gates de integração**. Não precisa de nova decisão arquitetural do usuário; eventual mudança visual, sim.
