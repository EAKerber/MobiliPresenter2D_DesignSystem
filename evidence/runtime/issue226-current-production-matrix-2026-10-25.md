# Issue #226 — matriz atual de acordeões em Production

**Data:** 25/10/2026  
**Rota:** `https://casaemmodulos.casa/how-it-works/`  
**Estado de produto conferido:** `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
**CSS:** `app/how-it-works/how-it-works.css`, blob `52f36d212d286ef5157a20fc822cbfab25e09b2f`.

Recarreguei a rota pública em contexto isolado e abri os itens pelo `summary` nativo. As medidas cobriram as duas grades `.foundation-list` e `.study-topics` em 1366 × 768, 768 × 1024 e 390 × 844, nos temas claro e escuro. Antes de cada caso os três itens estavam fechados; também abri sequencialmente dois itens e fechei ambos.

| Viewport | Grade | Altura fechada | Primeiro aberto | Irmãos fechados |
|---|---|---:|---:|---:|
| 1366 × 768 | `.foundation-list` | 142 px | 326,05 px | 142 px |
| 1366 × 768 | `.study-topics` | 76,33 px | 134,08 px | 76,33 px |
| 768 × 1024 | `.foundation-list` | 91,33 px | 230,53 px | 91,33 px |
| 768 × 1024 | `.study-topics` | 76,33 px | 134,08 px | 76,33 px |
| 390 × 844 | `.foundation-list` | 110–112,67 px | 293,72 px | 110–112,67 px |
| 390 × 844 | `.study-topics` | 76,33 px | 154,96 px | 76,33 px |

Nos seis pares viewport/tema, somente os itens abertos cresceram; a abertura do segundo item permaneceu independente, fechar restaurou as alturas e não houve overflow horizontal. O tema alterou a aparência, não as dimensões medidas. Em desktop, o CSS computado das duas grades foi `align-items: start`, coerente com o ajuste já presente em Production.

Teclado nativo em `.foundation-list`: Enter abriu e fechou; Espaço abriu e fechou; o foco permaneceu no `summary`. Redimensionamento da janela com um item aberto (769 px → 501 px de viewport interno) preservou o estado aberto e os irmãos fechados mantiveram suas alturas. O limite mínimo da janela do navegador impediu usar este método para chegar a 390 px; essa largura foi verificada com emulação de viewport na matriz acima.

**Limites:** não arquivei capturas antes/depois nesta passagem. A tentativa de zoom pelo atalho do navegador não alterou escala/viewport nesta ferramenta, então zoom permanece não verificado. A divergência de pixels em uma captura WebKit histórica, com DOM/geometria iguais, também não foi reproduzida nem resolvida por esta leitura Chromium. Portanto, a amostra atual não basta para fechar a issue #226; comparação visual WebKit e zoom seguem pendentes.


## Complemento de reflow em viewport CSS equivalente a zoom (25/10/2026)

Rota pública em contexto Chromium isolado, sem sessão, com viewport CSS emulado. As medidas abaixo aproximam a largura efetiva do layout a 200% e 400% sobre uma tela de 1366 px; visualViewport.scale permaneceu 1, portanto isto **não é um teste de zoom real do navegador**.

| Largura CSS emulada | Largura útil / scroll | .foundation-list | .study-topics |
|---:|---:|---|---|
| 683 × 768 (~200%) | 668 / 668 px | Uma coluna; fechado 91,33 px; aberto 252,8 px; irmãos fechados 91,33 px. | Uma coluna; fechado 76,33 px; aberto 134,1 px; irmãos fechados 76,33 px. |
| 341 × 768 (~400%) | 326 / 326 px | Uma coluna; fechado 150/131,33 px; aberto 356 px; os outros fechados mantiveram 131,33 px. | Uma coluna; fechado 76,33/82 px; aberto 155 px; os outros fechados mantiveram suas alturas. |

Não houve overflow horizontal; abrir o primeiro details não alterou a altura intrínseca dos irmãos fechados. Esta emulação confirma o comportamento em larguras CSS equivalentes, mas não substitui a verificação de zoom do navegador nem as capturas antes/depois exigidas pela issue. #226 continua aberta.
## Capturas comparativas arquivadas — 25/10/2026

Production `/how-it-works/`, Chromium isolado, 1366 × 768 CSS px, tema claro. Em cada grupo, os três `<details>` iniciaram fechados; abri o primeiro `summary` nativo e medi todos os retângulos antes de capturar. O grupo fora da tela permaneceu fechado. As quatro capturas mostram baseline fechado e primeiro item aberto em cada grade:

- `.foundation-list` fechado: [captura](issue226-captures/foundation-closed-1366x768-light.webp); alturas 141,33/141,33/141,33 px.
- `.foundation-list` primeiro aberto: [captura](issue226-captures/foundation-first-open-1366x768-light.webp); alturas 325,05/141,33/141,33 px.
- `.study-topics` fechado: [captura](issue226-captures/study-topics-closed-1366x768-light.webp); alturas 76,33/76,33/76,33 px.
- `.study-topics` primeiro aberto: [captura](issue226-captures/study-topics-first-open-1366x768-light.webp); alturas 134,08/76,33/76,33 px.

As caixas dos irmãos fechados não cresceram. Estas capturas completam a evidência antes/depois em desktop claro para ambas as seções; não são zoom do navegador nem cobrem tema escuro. A issue segue aberta até zoom real, revisão da divergência visual WebKit e integração apropriada.
## Capturas comparativas em tema escuro — 25/10/2026

Repiti os quatro estados em contexto isolado de Production, 1366 × 768 CSS px, tema escuro (`body` computou `rgb(17, 18, 16)`). Os retângulos foram idênticos aos do tema claro: `.foundation-list` fechado 141,33/141,33/141,33 px e aberto 325,05/141,33/141,33 px; `.study-topics` fechado 76,33/76,33/76,33 px e aberto 134,08/76,33/76,33 px.

- `.foundation-list` fechado: [captura escura](issue226-captures/foundation-closed-1366x768-dark.webp); aberto: [captura escura](issue226-captures/foundation-first-open-1366x768-dark.webp).
- `.study-topics` fechado: [captura escura](issue226-captures/study-topics-closed-1366x768-dark.webp); aberto: [captura escura](issue226-captures/study-topics-first-open-1366x768-dark.webp).

Com isso, as capturas antes/depois das duas seções estão arquivadas em tema claro e escuro no viewport desktop de 1366 × 768. A evidência de larguras 768/390 e teclado permanece na matriz acima. Um atalho `Control++` enviado ao tab pelo DevTools retornou sucesso, mas não mudou `innerWidth` (1279), largura visual (1264), `devicePixelRatio` (1,5), `visualViewport.scale` (1) nem zoom computado (1); não conta como teste de zoom. Zoom real do navegador segue pendente; o gate de captura WebKit foi revalidado e documentado a seguir.

## Reprodutibilidade do gate visual WebKit — 25/10/2026

A reexecução do gate isolado encontrou dois problemas no próprio teste antes de fechar a comparação: o baseline apontava para `main`, que já continha o ajuste, e o screenshot de elemento do WebKit capturava uma região vizinha de forma variável. Fixei o baseline no commit pré-correção `1878ae1057ce7c6190e0c8cb08a1f3baadd49463` (CSS blob `a65a0f77438b646122b0319d42cb9eef2e8b0dca`, sem `align-items:start`) e mudei as capturas para recorte explícito pelas coordenadas medidas do elemento, registrando também x/y.

A execução [Actions #40222887693](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40222887693) passou 8/8 combinações funcionais: Chromium e WebKit, 390/1366 px, claro/escuro; cada navegador teve paridade pixel a pixel em 4/4 comparações. A captura aberta de WebKit em desktop escuro foi inspecionada: somente o cartão selecionado cresceu, enquanto os dois cartões fechados mantiveram sua própria altura. O artefato #12610361610, digest `sha256:4387d28e6f6164f24a8e65838837ace026bf99908b73eade552cfcf4b816d86f`, retém as capturas por sete dias.

Isso resolve a discrepância do gate de captura; não é teste de zoom real. A issue #226 permanece aberta somente para o zoom do navegador. Esta revalidação modificou o gate isolado, sem alterar produto, merge ou publicação.
