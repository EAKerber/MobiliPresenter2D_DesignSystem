# P-TOKEN-01B/02B — PR #231, triagem de CI e bloqueio de integração

**Data:** 2026-10-22. **Estado:** **PR DE PRODUTO ABERTA EM DRAFT / HOLD PARA MERGE E PRODUÇÃO**. O patch contextual de tokens está **tecnicamente validado em sua própria matriz** e **não foi integrado à main**. O Netlify gerou **um único Deploy Preview automático**, nenhum preview foi solicitado manualmente.

## Autoridades e SHAs fixos

- Produto de referência: `EAKerber/MobiliPresenter2D@840a0cda361b3ce215fc934badc26df72dffc6e8`.
- PR produto [#231 — P-TOKEN-01B/02B](https://github.com/EAKerber/MobiliPresenter2D/pull/231) da branch `architecture/p-token-02b-contextual-copy-20261022@afb80965336083209eac93e2729de77170524ee5`; 24 commits à frente/0 atrás em comparação com a main no momento da auditoria.
- Design System fonte de referência [PR #49](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/49) e fonte contextual [PR #50](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/50), ambas **MERGED**; direção [ARC-01…16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md).
- Gate contextual da branch [#39780241560](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39780241560) = **SUCCESS, 48/48** Chromium/WebKit, 3 páginas, 4 larguras, 2 temas, zero diferenças de pixels, `pixelToleranceUsed=0`.
- [Netlify Deploy Preview #231](https://deploy-preview-231--mobilipresenter2d.netlify.app) foi sinalizado **ready** via status `netlify/mobilipresenter2d/deploy-preview`; não se verificou autoria/segurança privada nesse ambiente.

## Escopo de produto da PR

O diff é a composição intencional de **P-TOKEN-01B (cópia pinada DS/manifestos, fora do app)** e **P-TOKEN-02B (CSS de referência contextual consumido por apenas três componentes)**, além dos verificadores, testes e arquivos de CI correspondentes. CSS contextual `--ds-vis002-approved-support-text-light: #705C4B` aplica-se só a:
- `/` → `html[data-theme="light"] .hero-description`;
- `/how-it-works/` → `html[data-theme="light"] .how-hero-note`;
- `/about/` → `html[data-theme="light"] .about-scale p:not(.eyebrow)`.

Não altera `/config/`, Viewer, Admin, Core, dados V5, preço, session/auth, JS, Netlify functions, `netlify.toml` ou `package.json`. **VIS-002 não autoriza alias de paleta global**; não extrapolar este gate.

## Gates globais do produto na PR #231

| Gate | PR #231 | Evidência anterior / diagnóstico |
|---|---|---|
| Current variant fidelity | **PASS** [#39831366936](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366936) | sem regressão |
| App build purity | **PASS** [#39831366837](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366837) | build executável e declarativo intacto |
| Current asset gates | **PASS** [#39831366839](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366839) | referências de assets válidas |
| Mobile browser | **FAIL** [#39831366833](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366833) | `window.CASA_EM_MODULOS_DEBUG` indefinido ao ler `getLayoutProfile` em `/config/`; **o mesmo erro** na main [#39655019344](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019344) |
| Public routing before Clerk / static-and-contract | **FAIL** [#39831366832](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366832) | **os mesmos três testes CP-PUBLIC-02a** de allowlist/projection reprovavam na main [#39655019433](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019433); não houve alteração no domínio/public-projection |
| Summary pricing browser | **FAIL** [#39831366834](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366834) | timeout `page.waitForFunction` na prévia `/config/`; workflow também **FAIL na main** [#39655019482](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019482) |
| Keyboard browser | **FAIL** [#39831366830](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366830) | timeout em `/config/`; histórico de falhas na main (ex.: [#39202634261](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39202634261)) |
| Flow layout browser | **FAIL** [#39831366886](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366886) | timeout em `/config/`; histórico de falhas na main (ex.: [#39202661210](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39202661210)) |
| Stone browser | **FAIL** [#39831366831](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366831) | timeout `page.waitForFunction` 5000ms; **mesma assinatura** na main [#39655019362](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019362) |

**Observação epistemológica:** a falha da main antes do patch, com mesmo teste/assinatura e arquivos fora do escopo inalterados, sustenta fortemente que esses problemas **não foram introduzidos** pelo token contextual. Isso **não** comprova que o Configurador funciona em produção, nem que o baseline esteja saudável; não converter CI vermelho em `PASS` ou desabilitar checks só para integrar.

## Decisão de governança adotada

**PR #231 convertida para DRAFT. NÃO fazer merge enquanto CI global apresentar falhas sem política explícita e triagem independente.** O código funcional e seu gate estrito continuam válidos no SHA `afb8096`; a falha fora do escopo foi documentada com evidência de baseline. A PR permanece pronta para uma revisão sem necessidade de nova preview.

O teste `Mobile browser` acessa `https://deploy-preview-231--mobilipresenter2d.netlify.app/config/` sem preparar sessão/autorização e exige `window.CASA_EM_MODULOS_DEBUG`, que pode não existir se o bootstrap falhou. Uma hipótese é rota privada sem contexto de login/publicação; **não declarar causa confirmada**. Separar autenticidade da URL/HTML, carregamento dos scripts, estado de auth e prontidão do bootstrap antes de adaptar o gate. `#212`/`#213` continuam filas de autenticação correlatas, mas não presumir mesma causa.

## Próximo incremento de desbloqueio — CI-BASELINE-01

1. Capturar baseline CI da `main@840a0cd` com o mesmo ambiente e condições dos checks da PR, sem exigir nova Deploy Preview (usar URL de produção/autenticação adequadas quando permitidas). O histórico acima cobre parte, mas não normaliza todas as variáveis.
2. Classificar gates que acessam `/config/` sem sessão: **erro de preparação de teste**, **bloqueio do produto**, **recurso protegido intencionalmente** ou **flaky**; reproduzir antes de alterar.
3. Para CP-PUBLIC allowlist, validar fixtures/projeções em teste unitário sem tocar na publicação de dados.
4. Corrigir apenas root causes ou preparar política explícita de exceção de baseline com critérios e owner; **não** mascarar erro por remoção arbitrária de testes nem ampliar escopo do PR #231.
5. Quando gates exigidos tiverem evidência suficiente para decisão de merge, promover draft para ready, reconfirmar SHA do código/testes, merge e readback da main; validar único release/produção, sem gerar previews em loop.

**Estado final:** infraestrutura DS⇒produto e 3 usos homologados implantados **somente em branch testada**, PR #231 **DRAFT/HOLD**, produção **não alterada**. A próxima prioridade operacional é confiabilidade dos gates de integração, **não** mais abstração de tokens.
