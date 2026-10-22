# ARC-03B — HTML de autoria separado, compilador e gate de navegador

**Data:** 2026-10-22. **Estado:** **PASS técnico em branch isolada / PRODUÇÃO INALTERADA / CUTOVER DO BUILD NÃO REALIZADO**.

## 1. Autoridade, versão e retomada

- Produto `main` de referência: [`303468b4ddbb07a761316abca28901ccaea219df`](https://github.com/EAKerber/MobiliPresenter2D/commit/303468b4ddbb07a761316abca28901ccaea219df) — #233 corrigida em testes públicos.
- Branch de experimento: [`architecture/arc03-primary-header-fragment-prototype-20261022@e459b9bd85c4e9c8bb96813ae6758789de75dc13`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/arc03-primary-header-fragment-prototype-20261022).
- Gate final: [Actions #39867859774 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39867859774).
- Predecessor: [ARC-03 protótipo e CI baseline](CI_BASELINE_01_RESOLUTION_AND_ARC03_HEADER_PROBE_2026-10-22.md).
- Contrato: [ARC-01…16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md), em particular **ARC-03, 04, 05, 07, 15 e 16**, e homologação NAV-004 para header primário. Viewer NAV-005 com profundidade 2 continua explicitamente excluído.

**Regra fundamental:** a branch contém uma segunda representação *temporária e controlada* do conteúdo de três páginas para testar o mecanismo. Ainda não há fonte única de autoria em produção; isso só acontecerá quando a geração substituir o HTML manual no pipeline publicado, em um próximo gate. **Não afirmar que ARC-03 foi implementado no site.**

## 2. Contrato de fragmentos e fontes

| Arquivo | Função |
|---|---|
| `architecture/fragments/primary-header.fragment.html` | Estrutura compartilhada do header primário público com slots explícitos |
| `architecture/fragments/primary-header.routes.json` | Parâmetros por página (hrefs relativos, aria-current, atributos de acessibilidade) |
| `architecture/pages/root.page.html` | Fonte de autoria da Landing com marcador `<!-- ARC03_PRIMARY_HEADER -->` |
| `architecture/pages/about.page.html` | Fonte de autoria Quem somos, preservando corpo fora do header |
| `architecture/pages/how-it-works.page.html` | Fonte de autoria Como funciona, preservando corpo fora do header |
| `scripts/compile-primary-header-prototype.mjs` | Compilação do fragmento e gate de semântica do header |
| `scripts/compile-primary-pages.mjs` | Compila três páginas completas **somente em** `artifacts/arc03b/pages/` |
| `tests/arc03b-static-pages.test.mjs` | Contrato determinístico, integridade da fonte, exclusões e proteção contra drift |
| `tests/arc03b-primary-header-browser-differential.mjs` | Comparação em dois navegadores com baseline `app/` e overlay de documentos gerados |
| `.github/workflows/arc03b-authored-pages-browser-gate.yml` | Geração e teste em container oficial Playwright mais job independente de proteção do runtime |

**Sem escrita em `app/`**: o compilador reconstrói o HTML somente no diretório isolado de artefatos. O overlay de navegador altera apenas a resposta HTML de documento na sessão de teste; CSS, JavaScript e imagens são servidos do `app/` original. Não existe nova rota pública, novo servidor em produção nem necessidade de Deploy Preview.

**Fail closed por construção:** exige exatamente uma marcação de header em cada página, verifica que o texto/HTML fora do header equivale **byte a byte** ao arquivo existente, compara o header em forma normalizada (apenas espaços entre tags), valida links e atributos e rejeita drift. A geração é determinística; o relatório registra SHA-256 dos arquivos de origem/resultado.

## 3. Evidência verificável

[Run #39867859774 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39867859774), SHA exato `e459b9bd85c4e9c8bb96813ae6758789de75dc13`:

| Gate | Escopo | Resultado |
|---|---|---|
| Sintaxe e testes estáticos `node --test` | 3 páginas, marcadores, ausência de header copiado, Viewer excluído, hashes/determinismo | **PASS** |
| Geração de HTML | 3 fontes de autoria → 3 saídas scratch, manifest de hashes, `--check` | **PASS** |
| Diferencial DOM/CSS/screenshot | **3 páginas × 5 larguras (320/390/486/768/1366) × 2 temas × 2 engines (Chromium/WebKit) = 60 cenários**; header fechado e aberto quando o menu é visível | **60/60 PASS** |
| Rasterização | Sem imagens divergentes: `ARC03B_BROWSER_PASS {"scenarios":60,"rasterCases":0}` | **0 exceções** |
| Proteção do produto e do deploy | `git diff --quiet origin/main...HEAD -- app netlify.toml package.json netlify` em job independente `ubuntu-latest`, `fetch-depth:0` | **PASS** |
| Preview / produção | Nenhum novo Deploy Preview, nenhuma alteração do build Netlify `npm run build` / `publish=app` | **INALTERADOS** |

### Falha metodológica diagnosticada e corrigida

[Run anterior #39867401114](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39867401114) também concluiu **60/60 comparações de navegador sem diferenças**, mas o **último** passo tentou chamar `git diff` dentro do container Playwright sem diretório Git acessível (`warning: Not a git repository`, exit 129). O gate de runtime foi **movido para um segundo job sem container**. O commit seguinte `e459b9b` passou em ambos os jobs. Não houve alteração de comportamento da aplicação para corrigir uma falha do runner.

### Eficiência de CI

A imagem oficial `mcr.microsoft.com/playwright:v1.56.0-noble` fornece browsers e dependências de sistema para rodar Chromium/WebKit, em vez de instalar por `apt` em cada job. O projeto continua Vanilla; Playwright é instalado somente no ambiente isolado de CI (`npm install --no-save --no-package-lock`). Não houve alteração de `package.json` nem dos pacotes de produção. Não confundir tag de container com pin criptográfico de imagem; se essa infraestrutura for promovida, avaliar pin de digest na trilha de CI.

## 4. Decisões pendentes antes da publicação — ARC-03C

1. **Fonte única:** adotar os três HTMLs de `architecture/pages` como fonte autoral, retirar a duplicação de autoria em `app/` mediante geração estrita no pipeline efetivamente publicado; definir checksum, rollback e proteção contra edição manual de `app/`.
2. **Build preservado:** `npm run build` atualmente gera bundles Admin/Access/Navegação privada e publica `app/`. Integrar gerador mantendo a cadeia existente e garantindo que geração não apague recursos nem altere os outros cinco HTML. Não usar `app/scripts/build-static.sh` (saída histórica `app/dist`) como se fosse o build de produção.
3. **Semântica e fidelidade:** repetir gates estáticos, funcionais e visuais depois da alteração real do pipeline; incluir Renderer/Viewer NAV-005 e páginas privadas como controles negativos, e comparar antes/depois do build Netlify.
4. **Governança:** preparar PR única e controlada do incremento quando houver rollback/reprodutibilidade. Evitar gerar previews para cada ajuste; não misturar correções de preços, auth, CSS, menu P-COMP-01 ou i18n no mesmo cutover.
5. **Persistência:** registrar autoridade source-generated e migrar manuais/documentação que apontam diretamente a `app/index.html` como arquivo de autoria. Usar gate de drift para impedir duas fontes de verdade após a adoção.
6. **Retenção de evidência:** o run inclui `arc03b-staged-page-evidence` (artefato temporário de GitHub Actions). Os resultados, SHAs e comandos estão registrados aqui para retomada independente de artefatos efêmeros.

## 5. Bloqueios e fronteiras intactos

- [Issue #232](https://github.com/EAKerber/MobiliPresenter2D/issues/232) permanece **ABERTA**: fixture autenticada dos testes de `/config/`, com redirecionamento legítimo de anônimo para `/access/`. Não abrir acesso nem declarar gates privados PASS.
- [Issue #233](https://github.com/EAKerber/MobiliPresenter2D/issues/233) permanece **FECHADA**, correção de assertions do projection integrada na main do produto em `303468b4`.
- [PR #231](https://github.com/EAKerber/MobiliPresenter2D/pull/231) de tokens continua **DRAFT/HOLD**, gate contextual 48/48 PASS em branch; não fazer merge a partir da aprovação da compilação HTML.
- O controlador de menu P-COMP-01 continua validado em **branch separada**, sem merge. ARC-03B não introduziu nem alterou os listeners desse controlador.
- **Progresso estimado de consolidação do programa:** cerca de **22%**, contra 15% no marco anterior (+7 pontos percentuais), sujeito à faixa de incerteza 18–25% por esforço residual. ARC-03B melhora a prontidão para implementação, mas ainda não representa migração em produção.

**Veredito:** **GO técnico para preparar ARC-03C em branch de integração com build de produção**, **HOLD para merge/deploy até validar cutover completo**.
