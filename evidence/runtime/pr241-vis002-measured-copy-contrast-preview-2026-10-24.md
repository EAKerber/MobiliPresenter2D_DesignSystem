# VIS-002 — contraste de texto medido no preview da PR #241 (24/10/2026)

## Origem e escopo

- Produto: `EAKerber/MobiliPresenter2D`, PR [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241), head `f0fd9465d17ec30ab80932ecc048bf1e0c7b7532`.
- Preview: https://deploy-preview-241--mobilipresenter2d.netlify.app/
- Autorização registrada no corpo da PR #241: correção limitada aos contextos medidos em tema claro; para texto corrido longo, usar cor próxima do preto. Essa autorização de implementação pontual não altera a decisão canônica da paleta/tokens VIS-002.
- Rotas: Landing `/`, About `/about/` e Como funciona `/how-it-works/`. Viewer não apresentou pares reprovados e ficou fora da mudança.
- Viewports CSS: 1280×720 e 390×844; temas claro e escuro. Sessões de preview em contexto isolado e sem autenticação.
- CSS adicionado somente a essas três folhas; nenhuma atualização de token global, conteúdo, dados ou deploy de produção.

## Cores e pares confirmados no DOM/CSSOM

| Papel no contexto medido | Foreground | Background | Contraste |
|---|---:|---:|---:|
| Eyebrow em superfície clara marfim | `#70522F` | `#F0EDE8` | 6,12:1 |
| Eyebrow em superfície clara quente | `#70522F` | `#E8E3DC` | 5,60:1 |
| Texto corrido em superfície clara marfim | `#22211F` (via `var(--public-text)`) | `#F0EDE8` | 13,78:1 |
| Texto corrido em superfície clara quente | `#22211F` (via `var(--public-text)`) | `#E8E3DC` | 12,60:1 |

## Seletores alterados

- Landing: `html[data-theme="light"] .hero-copy > p.eyebrow`; `.environment-feature .feature-copy > p.eyebrow`; `.story-section > p.eyebrow`; parágrafos medidos da feature e da story section.
- About: `html[data-theme="light"] .about-scale__stat > span` e parágrafos medidos de `.about-closing`.
- Como funciona: eyebrows medidos em hero, acabamentos, produção, qualidade e clareza comercial; parágrafos medidos de acabamentos, clareza comercial e lançamento.
- No grupo `.finish-copy`, o parágrafo de assinatura `.finish-signature` conserva a regra mais específica existente (#6E512E no tema claro, #E2C991 no escuro); o texto corrido longo usa #22211F. A assinatura não é tratada como texto corrido longo.
- H1 em itálico que já atendia ao limiar de texto grande e todos os pares escuros foram mantidos.

## Verificação

- Nos três caminhos, a leitura DOM/CSSOM confirmou os valores esperados em 1280×720 e 390×844.
- Tema escuro: cores computadas nos seletores medidos permaneceram iguais ao baseline do preview.
- Em 390 px, documentElement/body não apresentaram overflow horizontal nas três rotas.
- Checks aplicáveis do produto passaram após retry dirigido do browser job: o primeiro GET de `/api/public-modules` recebeu 404 durante cutover; a leitura seguinte retornou 200 no Preview e em produção, e o retry passou por projeção, respostas negativas de endpoint e smoke visual desktop/mobile. Os dois Deploy Previews Netlify estão READY.
- Supabase Preview foi skipped porque branches de banco por PR estão desabilitadas. O produto continuou usando o banco interno existente; nenhum schema/dado foi alterado por esta mudança.

## Limites

Essa evidência prova somente os contextos/rotas/temas/viewports medidos na PR #241. Não certifica contraste sobre imagens, gradientes, transparências, estados dinâmicos, rotas não listadas, requisitos de leitor de tela ou conformidade visual global. A PR permanece DRAFT e não foi mergeada nem publicada em produção.
