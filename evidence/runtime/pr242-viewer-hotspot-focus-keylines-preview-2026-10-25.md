# VIS-002 — keylines de foco dos hotspots no preview — 25/10/2026

## Escopo e autorização

Teste autorizado pelo usuário para preview na PR de produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242). A regra foi limitada a `.scene-hotspot:focus-visible`; sem mudança em tokens, hover, seleção, dados da cena, `decisions.json`, merge ou Production.

Preview testado: https://deploy-preview-242--mobilipresenter2d.netlify.app/viewer/
Head da PR: `2727c85e933f4f17f539a97a263c7845d31efa0b`.

## Iteração e resultado

A primeira versão colocou as keylines fora do contorno e foi rejeitada: a inspeção móvel mostrou recorte na borda direita do hotspot 07. A versão final manteve o anel aprovado — 4 px, offset declarado de 3 px, acento #8B6A40 no claro e #D8BC7C no escuro — e usa keylines neutras fina preta e branca por `box-shadow: 0 0 0 1px #000, 0 0 0 3px #fff`. As keylines ficam dentro da extensão externa já ocupada pelo outline; não aumentam a geometria externa.

## Matriz observada

| Viewport | Tema | Hotspots com foco visível | Keylines preta e branca | Menor folga do indicador ao limite da cena | Overflow horizontal |
|---|---|---:|---|---:|---|
| 390 × 844 | claro | 7/7 | 7/7 | 0,11 px | não |
| 390 × 844 | escuro | 7/7 | 7/7 | 0,11 px | não |
| 1280 × 800 | claro | 7/7 | 7/7 | 6,29 px | não |
| 1280 × 800 | escuro | 7/7 | 7/7 | 6,29 px | não |

A inspeção visual confirmou no preview que os anéis permanecem dentro da cena para os sete hotspots; a leitura DOM/CSS confirmou o estado `:focus-visible`, as duas camadas de cor e ausência de rolagem horizontal. Os checks do commit terminaram com sucesso: App build purity, Current variant fidelity, Summary pricing browser, Stone browser, Mobile browser, Public routing before Clerk e Current asset gates.

## Limites

- A rota contém apenas a cena Cozinha; não generalizar para outras fotografias.
- A folga móvel mínima é pequena (0,11 CSS px) sob a geometria computada nesta sessão.
- A medição anterior de contraste na foto era aproximada e baseada nos pixels da imagem-base. Esta verificação não mede contraste de cada pixel composto do contorno/keylines contra a imagem e não declara conformidade WCAG.
- Não cobre outras cenas, navegadores, zoom do navegador nem revisão humana final de design.
- PR #242 permanece DRAFT. A experiência é candidata para revisão do usuário; sem integração ou publicação.

## Referência

A cor e a geometria do anel continuam conforme VIS-002. As keylines são uma camada experimental específica do estado de foco e não alteram a decisão canônica.
