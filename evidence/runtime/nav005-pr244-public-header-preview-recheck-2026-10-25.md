# NAV-005 — rechecagem pública do cabeçalho privado no preview — 25/10/2026

## Escopo

Rechecagem autorizada em preview da implementação NAV-005 na PR de produto [#244](https://github.com/EAKerber/MobiliPresenter2D/pull/244). Chromium em contexto isolado, sem sessão autenticada e sem escrita em conta.

Branch/head: feat/nav005-private-header-20261024@063796224c55924a8b3a909c9631c6b5f5590972. Preview principal: https://deploy-preview-244--mobilipresenter2d.netlify.app/.

## Medidas

Rotas /admin.html e /access/, temas claro e escuro, viewports 291, 320, 321 e 288 × 700 CSS px.

| Rota | Largura | Organização | Identificador | Tema/menu | Overflow |
|---|---:|---|---|---|---|
| /admin.html | 291 | Controles e marca no mesmo eixo; header 62,7 px | “Administração” inteiro | tema 44×44, menu 44×44 à direita | não |
| /admin.html | 320 | uma faixa | “Administração” inteiro | ícone de tema; menu 44×44 à direita | não |
| /admin.html | 321 | uma faixa | “Administração” inteiro | “Auto” visível; menu 44×44 à direita | não |
| /admin.html | 288 | ações na segunda faixa; header 108,2 px | “Administração” inteiro | tema e menu 44×44 | não |
| /access/ | 291 | controles e marca no mesmo eixo; header 74,7 px | “Confirmar acesso” inteiro | tema 44×44, menu 44×44 à direita | não |
| /access/ | 320 | uma faixa | “Confirmar acesso” inteiro | ícone de tema; menu 44×44 à direita | não |
| /access/ | 321 | uma faixa | “Confirmar acesso” inteiro | “Auto” visível; menu 44×44 à direita | não |
| /access/ | 288 | ações na segunda faixa; header 120,2 px | “Confirmar acesso” inteiro | tema e menu 44×44 | não |

No Admin, a logo mediu 74,5 px em 291 px, redução de 29,1% ante a referência de 105 px, dentro do limite aprovado de 30%. Tema claro e escuro tiveram os mesmos resultados geométricos.

## Rota autenticada

Em contexto sem cookies, /config/ redirecionou para /access/ e apresentou estado de link/token ausente ou inválido, sem campos de formulário. Isso confirma o comportamento anônimo observado, mas não valida o cabeçalho do Configurador autenticado nem a área autenticada de gestão de acesso.

## Resultado e limites

A amostra confirma as medidas públicas do preview para /admin.html e /access/; não declara homologação de sessão autenticada, outras larguras, navegadores ou Production. A PR #244 permanece DRAFT; sem merge ou publicação.
