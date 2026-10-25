# Issue #208 — reconciliação DS-04 com o produto main atual

**Data:** 25/10/2026  
**Produto:** `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` (branch `main`, lida pela API de refs).  
**Escopo:** comparar os 16 achados da issue #208 com os arquivos atuais e revalidar o estado público de `/access/` em tema claro/escuro. É uma auditoria de leitura; nenhum código, token ou decisão canônica foi alterado.

## Resultado por achado

| ID | Resultado atual | Base observada |
|---|---|---|
| DS04-01 | **Corrigido no estado observado.** `/access/index.html` carrega `ui-theme.js`, `public-theme.css` e `ui-theme.css`; a rota publicou tema claro e escuro em contexto anônimo de Production. O estado mostrado foi “link inválido”, sem credencial/token e sem overflow horizontal. | DOM Production claro/escuro; `access/index.html` blob `e28c09fd31d81f4cfded3f82a7244f8b10dddb2c`. |
| DS04-02 | **Ainda presente no código; runtime protegido inconclusivo.** `app/access/manage.html` mantém `color:white` sobre `var(--public-accent-dark)`; em dark, `ui-theme.css` resolve o fundo para `#E2C991`. O par calcula **1,62:1**. A rota anônima redireciona a `/admin.html?returnTo=…`, então o CTA de gestão não pôde ser visto na sessão isolada. | `manage.html` blob `c41af2ea77836e56437a8dd646a0e191e9e4f987`; `ui-theme.css` blob `b0f04c566183ba1f9c015f5d2a827db9e91dea45`; análise da rota protegida em Production. |
| DS04-03 | **Correção de fundo/foreground encontrada.** Em light, `.item-option` usa fundo branco e `var(--control-text)`; o token atual é `#403A34`, contraste **11,21:1**. | `admin.css` blob `1b3b41e166d44dbf70c1096db36255398aff8493`; cores do tema claro. |
| DS04-04 | **Tokens claros encontrados.** `.hierarchy-name/.hierarchy-field/.hierarchy-move` usam `--label: #48423B`; opções e resumo usam `--control-text: #403A34`. A opção indisponível usa `#6B6259` sobre `#F0EDE8`, **5,11:1**. A rota autenticada não foi aberta; esta classificação é estática, não leitura de todos os widgets renderizados. | `admin.css` blob acima; tokens light presentes no CSS Admin atual. |
| DS04-05 | **Tokens de feedback claros encontrados.** Default `#6B6259`, sucesso `#176344` (**7,23:1** em branco) e erro `#A32323` (**7,44:1** em branco). Sem sessão, estados Admin de sucesso/erro não foram gerados no browser. | `admin.css` blob acima; tokens light presentes no CSS Admin atual. |
| DS04-06 | **Ainda presente.** `.config-section > h3` permanece `rgba(255,255,255,.58)`; não encontrei override light equivalente no CSS compartilhado atual. O Configurador autenticado não foi exercitado. | `styles.css` blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`; leitura estática em `main`. |
| DS04-07 | **Correção encontrada.** O label `.price-state__breakdown dt` recebe `#292723` sobre o fundo light `#F0EDE8`, **12,77:1**. | Override atual em `ui-theme.css` e `styles.css`. |
| DS04-08 | **Correção encontrada.** No tema light o dock usa `var(--surface)=#FFFFFF`; `.configuration-value strong` usa `var(--text)=#22211F`. | Override light em `ui-theme.css`; seletor em `styles.css`. |
| DS04-09 | **Correção encontrada por token.** O número da etapa usa `--accent: #6E512E` no tema light, **7,29:1** sobre branco. | `admin.css` blob acima. |
| DS04-10 | **Ainda presente como risco.** `.swatch.is-selected` continua com borda branca e sombra branca fixa. A fidelidade de cada textura/cor exige validação em swatches reais; não modifiquei cores de material. | `styles.css` blob acima; revisão estática. |
| DS04-11 | **Exceção técnica explicitada, mas evidência visual limitada.** `.module-detail` permanece em canvas claro e `ui-theme.css` comenta para mantê-lo no canvas técnico validado. Não foi reavaliada a hierarquia visual de cada estado neste follow-up. | Comentário contextual em `ui-theme.css`; código de `.module-detail` em `styles.css`. |
| DS04-12 | **Ainda insuficiente no tema claro.** Em 390 × 844 px, o ponto inativo computa `#C9C3BB` sobre o cartão branco: **1,75:1**, abaixo de 3:1 para indicador não textual. No escuro sobre `#1B1C1A`, mede **9,78:1**. A página ficou sem overflow (390/390). | `viewer.css` blob `90d23678630c17f63ac343bfd7e5e1ce3bbcb1b2`; runtime DOM/CSSOM Production em 390 px, claro/escuro. |
| DS04-13 | **Isenção mantida.** Faixa de benefícios da Landing continua editorial e escura. | `landing.css` blob `91a7bc7cd912ac7f0a9e81c16fcee576dc50a4ea`. |
| DS04-14 | **Isenção mantida.** Faixas Economia/closing continuam escuras e contextuais; sem recoloração automática. | `how-it-works.css` blob `52f36d212d286ef5157a20fc822cbfab25e09b2f`. |
| DS04-15 | **Isenção mantida.** Fotografia, cena e acabamentos do Viewer ficam fora de correção genérica de superfície. | Registro de origem da issue; sem mudança nesta revisão. |
| DS04-16 | **Isenção mantida.** Swatches do Admin continuam recebendo `source.color` e textura do dado de material, preservando fidelidade de produto. | `admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`. |

## Readback runtime

Em Production, contexto Chromium isolado sem sessão, `/access/` permaneceu na própria rota e alternou visualmente entre claro e escuro; exibiu aviso de link inválido. A página mediu `clientWidth=scrollWidth=491`. `/access/manage.html` redirecionou a login Admin, portanto não tratei o resultado dessa tela como evidência do painel de gestão.

Na verificação do Viewer, 390 × 844 px, claro e escuro, os quatro pontos de navegação permaneceram dentro da página (`clientWidth=scrollWidth=390`). A razão de contraste acima usa o cartão ancestral de fundo branco no tema claro e `#1B1C1A` no escuro; comparar o ponto com o ancestral transparente intermediário daria uma razão incorreta.

## Conclusão e próximo gate

A issue #208 **continua aberta**. A base antiga já não representa todos os achados: DS04-01, 03, 04, 05, 07, 08 e 09 têm correções de código/tokens presentes; DS04-11 está explicitamente delimitado como exceção, embora a validação visual seja parcial. Permanecem riscos ativos em DS04-02 (P1), DS04-06 (P1), DS04-10 (P2) e DS04-12 (P3). DS04-02 exige sessão Admin válida para confirmação runtime; não coletei credenciais. O issue não autoriza implementação, então os riscos foram documentados sem CSS, produto, `decisions.json`, merge ou Production alterados.
