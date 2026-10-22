# CI-BASELINE-01 — diagnóstico reprodutível e correção de testes do MobiliPresenter2D

**Data:** 2026-10-22. **Estado:** causas identificadas, **duas issues rastreáveis**, um gate de projeção pública corrigido (**PASS em branch isolada**) e uma auditoria de proteção do Configurador (**PASS diagnóstico sem autenticação**). **CI global da main continua não homologada**; [PR #231](https://github.com/EAKerber/MobiliPresenter2D/pull/231) permanece **DRAFT/HOLD**. Sem merge ou deploy de correção, sem nova PR/preview.

## Ponto de entrada — issues com evidências e critérios de aceite

| ID | Natureza | Evidência consolidada | Encaminhamento |
|---|---|---|---|
| [#232 — Gates browser do Configurador sem bootstrap](https://github.com/EAKerber/MobiliPresenter2D/issues/232) | **Causa de setup identificada:** navegação anônima a `/config/` leva a `/access/`; testes procuram JS/DOM do Configurador na página errada | [Diagnóstico não autenticado #39849284220 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39849284220): produção e preview #231 redirecionam para `/access/` | Separar **teste negativo de acesso** e **testes positivos autenticados** com fixture segura e revogável; fail-closed sem token |
| [#233 — Assertions CP-PUBLIC-02a defasadas](https://github.com/EAKerber/MobiliPresenter2D/issues/233) | Testes esperam `publicState.entities` e omitem `nominalDimensionsMm`; o projection real já retorna `publicState.viewerEntities` e dimensões públicas nominais | [CI isolada #39848703737 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39848703737) na branch `ci/ci-baseline-01-public-projection-test-20261022@387da6a57c4188dd32ee0c5551e11d15e9140d3f` | Integrar **somente os testes/CI**, mantendo allowlist e proibição de preços sem opt-in; sem alterar V5/runtime |

## 1. Confirmação reproduzível da proteção em /config/

Branch de diagnóstico do produto: [`ci/ci-baseline-01-config-readiness-20261022`](https://github.com/EAKerber/MobiliPresenter2D/tree/ci/ci-baseline-01-config-readiness-20261022). Arquivos exclusivamente de teste/CI: `tests/ci-baseline-config-readiness-diagnostic.mjs`, `.github/workflows/ci-baseline-01-config-readiness-isolated.yml`. No GitHub Actions, um Chromium **incógnito/sem sessão** acessou a URL de produção e o **único** Deploy Preview já existente da PR #231:

| Origem | HTTP final | URL após redirecionar | `main.workspace` do Configurador | `CASA_EM_MODULOS_DEBUG` |
|---|---:|---|---|---|
| `https://mobilipresenter2d.netlify.app/config/` | 200 | `https://mobilipresenter2d.netlify.app/access/` | Ausente | Ausente |
| `https://deploy-preview-231--mobilipresenter2d.netlify.app/config/` | 200 | `https://deploy-preview-231--mobilipresenter2d.netlify.app/access/` | Ausente | Ausente |

Logo, o erro de `getLayoutProfile` e os timeouts dos testes em `/config/` são **explicados pela premissa incorreta de navegação anônima**. Não há evidência que a aplicação esteja quebrada **quando devidamente autenticada**, e não se deve abrir a rota para satisfazer CI.

**Privacidade/segurança:** auditoria somente de leitura; sem login, credenciais, cookies preservados, header de autenticação, token, HTML de páginas privadas ou screenshot. O artefato do run armazena somente paths sem query, status de scripts, classes de erro e indicadores booleanos. Os problemas gerais de autenticação do Admin, sessão e fallback [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212), [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213), [#222](https://github.com/EAKerber/MobiliPresenter2D/issues/222) permanecem **separados e abertos**.

### Correção apropriada da CI de browser

- **Gate negativo público:** usuário anônimo acessando `/config/` deve permanecer fora do Configurador e receber rota de acesso; não exigir `CASA_EM_MODULOS_DEBUG` nesse cenário.
- **Gate funcional protegido:** Mobile PiP, Keyboard, Flow layout, Summary pricing e Stone precisam de **fixture de sessão autenticada** em ambiente apropriado, com mínimo privilégio, credencial não registrada no repositório/logs, ciclo de vida limitado e revogação. Confirmar rota final e readiness antes de interagir.
- Sem fixture: registrar `BLOCKED_AUTH_FIXTURE`, conservar CI como pendência e **não** convertê-la em sucesso ignorando comportamento, nem alterar regras de segurança para o teste. A forma de criar sessão autorizada exige decisão de implementação/infraestrutura concreta, não está homologada neste documento.
- Não juntar essa remediação com P-TOKEN-02B; nenhuma alteração de CSS pode reparar um redirecionamento de autenticação.

## 2. Correção de teste CP-PUBLIC-02a em branch

Falhas antigas na `main@840a0cd`: [Public routing #39655019433](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019433) e [PR #231 #39831366832](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366832) tinham três subtestes vermelhos por expectativas anteriores ao schema:

1. Chave `publicState.entities` foi substituída por `publicState.viewerEntities` nas assertions. **Não** mudar a projeção de produção para satisfazer teste antigo.
2. `nominalDimensionsMm` foi incluído na allowlist esperada dos campos públicos **com conferência explícita de width/height/depth**, mantendo veto a geometria de cena privada e campos doadores.
3. Fixture sem `viewerPricePublication.enabled` continua **sem** `basePriceCents`; este assert também foi adicionado.
4. Testes de `app/tools/test-public-modules-endpoint.js` e `app/viewer/scene-adapters.test.mjs` continuam no gate.
5. Workflow de branch garante **diff nulo** em `app/`, `netlify/`, `netlify.toml` e `package.json`.

**Primeiro run:** [#39848544639](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39848544639) foi vermelho **somente** por falta de merge-base no checkout raso do passo final `git diff`; os testes de contrato passaram. Após adicionar `fetch-depth:0`, **run final #39848703737 PASS** no SHA `387da6a57c4188dd32ee0c5551e11d15e9140d3f`. Correção ainda em branch — **não afirmar que main já está verde**.

## 3. Matriz de rastreabilidade dos gates vermelhos da PR #231

| Workflow | PR #231 | Evidência de baseline | Responsabilidade |
|---|---|---|---|
| Mobile browser | [#39831366833](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366833) FAIL | [main #39655019344](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019344) mesmo `getLayoutProfile` indefinido | #232 |
| Summary pricing | [#39831366834](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366834) FAIL | [main #39655019482](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019482) FAIL | #232 |
| Stone browser | [#39831366831](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366831) FAIL | [main #39655019362](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019362) mesmo timeout 5000ms | #232 |
| Keyboard + Flow | [#39831366830](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366830), [#39831366886](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366886) FAIL | Histórico anterior de timeouts de prontidão e navegação anônima sem sessão | #232 |
| Public routing CP-PUBLIC-02a | [#39831366832](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39831366832) FAIL | [main #39655019433](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39655019433) mesmos 3 subtestes | #233 |

Esses fatos **não** são um waiver automático de testes globais. Não é apropriado fazer merge de #231 ignorando falhas, mesmo preexistentes. Build purity, current asset gates e current variant fidelity já passaram na PR; a conformidade visual contextual está coberta pelo [run #39780241560 (48/48 PASS)](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39780241560).

## 4. Próximas ações e critérios de parada

**CI-BASELINE-01A — diagnóstico e correção da expectativa pública:** **PASS parcial e verificável** (issue #233, branch e gate isolado); falta integrar os testes na main sem gerar preview desnecessário. Não pedir o merge de #231 até que o contrato público da main seja reconciliado.

**CI-BASELINE-01B — autenticação da fixture de testes:** **BLOQUEADO POR DESIGN**, pois a rota privada exige sessão. Antes de implementar, escolher um mecanismo de fixture de testes com escopo, expiração, segregação do ambiente/conta, revogação e validação de acesso; não reutilizar token real de comprador e não colocar segredo em snapshots de CI. O primeiro gate deve comprovar a negativa anônima e a positiva autenticada sem vazamento.

**P-TOKEN-02B:** conservar a [PR #231 DRAFT](https://github.com/EAKerber/MobiliPresenter2D/pull/231), evitando novos previews; primeiro consumo contextual já validado em 48/48 cenários, mas **sem merge na main do produto**.

**Resultado do turno:** duas issues fáceis de localizar, fix de assertions testado e observação determinante de redirecionamento `/config/→/access/`; nenhuma alteração de runtime, dados V5, políticas de acesso ou preços.
