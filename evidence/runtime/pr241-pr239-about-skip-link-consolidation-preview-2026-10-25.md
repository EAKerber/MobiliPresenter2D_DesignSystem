# Rechecagem combinada de About skip link — PRs #239/#241 (25/10/2026)

## Consolidação

A antiga PR de About skip link [#239](https://github.com/EAKerber/MobiliPresenter2D/pull/239) foi incorporada à PR [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241) na head `45e532b444967bdd901ac2f49fc8d0548daa881a`. O commit tem como pais a head anterior da #241 (`ebd67cdd003047543b70d21972173af80da3594e`) e a head da #239 (`e7b02c04308e9fcc7b52f1d09534058a2a0bbc65`). A #239 foi encerrada como supersedida após a validação, preservando sua branch e histórico. Não houve merge em `main` nem publicação em Production.

As mudanças nos arquivos compartilhados foram compostas: a folha About conserva o papel de texto medido da #241 e inclui o foco aprovado do skip link da #239; o manifesto contém os hashes da página About da #239 e da página Como funciona da #241. Conferi os hashes do manifesto contra os blobs fonte e HTML da About.

## Gates da head combinada

Os nove workflows do produto passaram na head combinada: build purity (#40230763530), variantes (#40230763511), assets (#40230763583), Mobile (#40230763564), roteamento público (#40230763575), Summary/Pricing (#40230763557), Stone (#40230763500), gate VIS-002C P-TOKEN v0.3 (#40230763562) e About skip-link destination focus (#40230763613). Os Deploy Previews principal e isolado ficaram SUCCESS, incluindo o preview principal `https://deploy-preview-241--mobilipresenter2d.netlify.app`.

## Leitura manual do preview

Contexto Chromium isolado, rota `/about/`, URL `https://deploy-preview-241--mobilipresenter2d.netlify.app/about/`:

- Tab focou “Pular para o conteúdo” e tornou visível o anel claro `#D8BC7C`, com largura computada de 4 px.
- Enter navegou para `#main` e transferiu o foco para `main#main` (`tabindex="-1"`).
- A regra carregada declara `outline-offset: 3px`, mas o CSSOM reportou `2.66667px`; um botão de controle com `outline-offset: 3px` também computou `2.66667px` no mesmo contexto. Isso indica uma discrepância de leitura do navegador/contexto, mas sua causa não foi isolada. Não alterei a geometria aprovada para ajustar a medição.

A rechecagem cobre a navegação do skip link e a regra de foco em uma rota pública do preview. Não valida rotas privadas autenticadas nem substitui revisão visual ampla. PR #241 permanece DRAFT.
