# /admin.html: cabeçalho e menu de login em produção

**Observado em:** 20/10/2026  
**Produto:** `EAKerber/MobiliPresenter2D`, `main`, commit [`1878ae1`](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463)  
**Deploy:** [`6ad6c3b51b6be05647167f94`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94), produção publicada  
**Contexto:** navegador isolado e anônimo. Nenhuma credencial foi preenchida ou enviada.

## Capturas

- [Tema claro, menu aberto](../../visualEvidence/private/admin-login/admin-login-menu-light-2026-10-20.jpg)
- [Tema escuro, menu aberto](../../visualEvidence/private/admin-login/admin-login-menu-dark-2026-10-20.jpg)

Viewport CSS de 390 × 844 px, DPR 1. O formulário de login estava visível por trás do menu. O cabeçalho apresenta a marca e “Administração” à esquerda, com tema e menu à direita, conforme a estrutura privada homologada.

## Navegação

O menu abriu no primeiro clique e apresentou uma opção privada para o estado anônimo — **Entrar na administração** — e cinco destinos públicos. Escape fechou o menu e devolveu o foco ao botão. A largura do documento permaneceu em 390 px. Nenhum login foi tentado; acesso autenticado, pós-login e saída não foram avaliados nesta visita.

## Superfícies computadas

| Tema | Cabeçalho | Menu | Fundo da página | Texto |
|---|---|---|---|---|
| Claro | `#F0EDE8` | `#FFFFFF` | `#F7F5F2` | `#22211F` |
| Escuro | `#171816` | `#1B1C1A` | `#111210` | `#F4F1EB` |

O cabeçalho claro coincide com a superfície aprovada `#F0EDE8`; o popover claro usa branco puro. No tema escuro, cabeçalho `#171816` e menu `#1B1C1A` diferem das amostras `#171614` (canvas) e `#211F1C` (superfície). O texto permanece legível nas capturas; não foi declarada falha de contraste. Os usos estão no escopo de FIND-015.

O cabeçalho computou `z-index: 60` e o menu `z-index: 80`. O menu sobrepõe o formulário enquanto expandido, como esperado para um popover; não foi observada sobreposição por camadas da cena.

## Limites

Nenhum código, dado ou configuração do produto foi alterado. Não se conclui sobre falha intermitente de sessão porque não houve autenticação. Para a tela de confirmação de acesso, ver [a evidência de /access/](access-confirmation-menu-2026-10-20.md).