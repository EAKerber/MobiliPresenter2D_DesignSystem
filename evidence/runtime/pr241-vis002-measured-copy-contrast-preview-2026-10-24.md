# VIS-002 — contraste de texto medido no preview da PR #241 (24/10/2026)

**Estado:** histórico de uma primeira leitura de preview na head `f0fd9465d17ec30ab80932ecc048bf1e0c7b7532`, preservado abaixo. Ela leu texto base `#22211F` em vez da distribuição candidata final. A revalidação da head atual `baef9acd71bc636db66709d93c0d5cf0ab5d0134`, com a distribuição `#292723`, está na última seção e é a evidência aplicável ao código atual da PR.

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


## Revalidação da head atual — DOM/CSSOM no preview (24/10/2026)

**Produto:** PR [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241), head `baef9acd71bc636db66709d93c0d5cf0ab5d0134`, base `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. O commit e os checks foram relidos durante esta revalidação. Os oito workflows aplicáveis concluíram com sucesso; os status `netlify/mobilipresenter2d/deploy-preview` e `netlify/m2d-auth-ci-isolated/deploy-preview` também estão `success`. Os previews são [principal](https://deploy-preview-241--mobilipresenter2d.netlify.app/) e [isolado](https://deploy-preview-241--m2d-auth-ci-isolated.netlify.app/).

### Procedimento e leitura

- Usei páginas anônimas no contexto isolado `vis002-pr241-current-audit-2026-10-24`; nenhum dado de conta ou negócio foi lido ou alterado.
- Viewport observado: 1279 × 663 CSS px, DPR 1,5. A amostra não foi repetida em outro viewport nesta revalidação.
- Em cada rota, confirmei que o recurso importado `/design-system/vis002c-long-copy-light-v0.3.0.css?v=vis002c-0.3.0` foi carregado. Comparei os seletores do mapeamento v0.3 em `data-theme="light"` e `data-theme="dark"`, lendo cor e fundo computados no DOM/CSSOM. Depois restaurei o tema escuro que estava ativo nas abas isoladas e fechei as abas temporárias.
- Os sete seletores do mapeamento corresponderam a nove elementos nesta renderização. No claro, todos computaram `#292723`: `#E8E3DC` deu 11,68:1 e `#F0EDE8` deu 12,77:1.
- No escuro, os mesmos elementos computaram `#C4BCB2` sobre `#20211F` (8,61:1); o token claro não foi aplicado.

### Cobertura por rota

| Rota | Seletores medidos | Elementos encontrados | Par claro no DOM |
|---|---|---:|---|
| Landing `/` | `.story-section > p:not(.eyebrow)`; `.feature-copy > p:not(.eyebrow):not(.feature-availability)` | 2 | `#292723` / `#E8E3DC` (11,68:1) e `#292723` / `#F0EDE8` (12,77:1) |
| About `/about/` | `.about-closing > p:not(.eyebrow):not(.about-closing__signature)`; `.about-scale__stat > span` | 3 | `#292723` / `#F0EDE8` (12,77:1) |
| Como funciona `/how-it-works/` | `.finish-copy > p:not(.eyebrow):not(.finish-signature)`; `.commercial-clarity > p:not(.eyebrow)`; `.launch-card .launch-copy > p` | 4 | `#292723` / `#F0EDE8` (12,77:1) |

### Limites

Esta leitura confirma a cor, os fundos e a separação de tema nos seletores mapeados nesta head e preview. Não é inspeção de screenshot, auditoria de todas as larguras, validação de Production, certificação de outros componentes nem aprovação de tokens globais. Eyebrows e assinaturas permanecem fora do escopo. A PR está DRAFT e não foi mergeada.
