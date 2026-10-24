# NAV-005 — validação da implementação em preview da PR #244

Data local: 2026-10-24  
Produto: [PR #244](https://github.com/EAKerber/MobiliPresenter2D/pull/244), head `b0a0aaf7762239f52f4a64494209f754b468fca5`, base `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
Deploy Previews: [principal](https://deploy-preview-244--mobilipresenter2d.netlify.app/) e [isolado](https://deploy-preview-244--m2d-auth-ci-isolated.netlify.app/), ambos READY para o mesmo head.  
CSS carregado: `/ui-theme.css?v=private-header-nav005-v2`.  
Contexto: navegador isolado, sem sessão; viewports móveis emulados; leitura DOM/CSSOM sem salvar preferências ou dados.

## Resultado em Administração — `/admin.html`

Os temas claro e escuro tiveram geometria equivalente nos pontos conferidos:

| Viewport | Header | Logo | Tema | Menu | Identificador | Overflow horizontal |
|---:|---:|---:|---:|---:|---|---|
| 291 px | 63 px, uma linha | 74,125 px | 44 × 44 px | 44 × 44 px | “Administração” completo | não |
| 320 px | 63 px, uma linha | 103,125 px | 44 × 44 px | 44 × 44 px | “Administração” completo | não |
| 288 px | 108,58 px, duas linhas | 105 px | 44 × 44 px | 44 × 44 px | “Administração” completo | não |

A 291 px, a logo reduz 29,4% em relação à referência anterior de 105 px, dentro do teto aprovado. A 288 px, as ações migram para a segunda linha.

## Resultado na tela de acesso — `/access/`

A 291 px, em claro e escuro, o documento mede 291 px sem overflow; o header permanece em uma linha, o identificador “Confirmar acesso” fica completo e os alvos do tema e menu medem 44 × 44 px. A logo mede 83,55 px, redução de 20,4% ante a referência de 105 px.

A 320 px em claro, a etiqueta visível do tema é ocultada e o botão permanece 44 × 44 px. A 321 px em escuro, “Auto” volta a aparecer; documento e viewport medem 321 px. Isso confirma o limite de ícone-only em 320 px.

Durante esta verificação, uma regra genérica da tela de acesso impôs altura mínima de 50 px ao botão do menu. A PR adicionou uma exceção limitada a `.private-header .private-menu-toggle`, e o preview final computou 44 × 44 px. O reset de `min-width:320px` também foi limitado a `body.access-page` e seu elemento raiz para que o piso de 291 px funcione sem alterar o restante do shell público.

## CI e limites

Para o head acima, passaram: build purity [#40139439976](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139439976), variants [#40139440062](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139440062), asset gates [#40139439996](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139439996), summary pricing [#40139439980](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139439980), Stone [#40139440036](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139440036), public routing/contracts [#40139440010](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139440010) e mobile [#40139439989](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139439989).

O workflow Admin hierarchy [#40139440003](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40139440003) falha na asserção inicial do harness, antes da interação: o teste exige `admin.bundle.js?v=admin-auth-flow-v2`, mas `main` e a branch da PR usam `admin.bundle.js?v=viewer-price-main-ux230-v2`. O arquivo de teste não foi alterado nesta mudança. A falha é uma incompatibilidade preexistente do harness, não evidência de regressão do CSS.

A rota autenticada do Configurador e a sessão autenticada de gerenciamento não foram testadas neste navegador sem sessão. Não contornei a proteção.

## Escopo e status

A autorização nesta conversa permitiu implementar e validar esta proposta somente em preview. `decisions.json` continua inalterado; sua autorização canônica permanece falsa. A PR #244 segue DRAFT, sem merge ou deploy de produção.
