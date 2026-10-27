# Cabeçalhos públicos em larguras móveis — Production (24/10/2026)

**Alvo:** `EAKerber/MobiliPresenter2D@main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`. Contexto público anônimo, browser isolado temporário. Viewports 290×700, 320×700 e 335×760; About também em 360×800 e 390×844. O viewport foi restaurado e as abas temporárias foram fechadas. Capturas observadas inline, não persistidas.

| Rota | 290×700 escuro | 320×700 | 335×760 | Notas |
|---|---|---|---|---|
| `/about/` | `clientWidth=275`, `scrollWidth=320`; overflow 45 px. Título/parágrafos são cortados. Menu ocupa x=264–306; só 11 px cabem na largura útil. Barra horizontal visível. | `innerWidth=320`, `clientWidth=305`, documento/body/header em 320 px; overflow 15 px e barra visível. Mesmo resultado estrutural em tema claro. | sem overflow (`clientWidth=scrollWidth=320`) | Também sem overflow em 360 e 390 px escuros. |
| `/viewer/` | `clientWidth=275`, `scrollWidth=320`; overflow 45 px. Conteúdo do cartão/preço é cortado. Menu x=262–306; só 13 px cabem na largura útil. Barra horizontal visível. | `innerWidth=320`, `clientWidth=305`, documento/body/header em 320 px; overflow 15 px e barra visível. Mesmo resultado estrutural em tema claro. | sem overflow (`clientWidth=scrollWidth=320`) | Cena x=22–298 e o botão/menu ultrapassa a área útil; tema escuro na amostra de 290 px. |
| `/how-it-works/` | Evidência anterior: `min-width:320px` e `overflow-x:clip` cortam conteúdo e deixam 11 px do botão visíveis. | Escuro: `html/body` e header em 320 px; `clientWidth=305`, `scrollWidth=320`; `overflow-x:clip` recorta a sobra, sem barra horizontal visível. | sem overflow (`clientWidth=scrollWidth=320`) | Reproduz o padrão de largura rígida já registrado em NAV-005. |

Nesta sessão, uma barra vertical de 15 px reduz a área de layout: `innerWidth=320`, mas `documentElement.clientWidth=305`; a 290 px, `clientWidth=275`. O ponto sem overflow foi observado em 335 px; isto não determina breakpoint CSS e pode variar em navegadores com barras sobrepostas.

No About a 320 px, o menu abriu por clique e Escape fechou-o com foco restaurado ao botão. O comportamento do link “Pular para o conteúdo” está registrado separadamente: muda a âncora, mas termina com foco em `body`. Não abri menu no Viewer ou em Como funciona. Uma amostra por rota/largura; sem alteração de produto, dados ou preferência persistente de tema.


## Rechecagem em emulação mobile — 24/10/2026

No mesmo deploy Production READY `6adc221479c773577ed45e23`, rota `/how-it-works/`, contexto público isolado, emulação mobile/touch de 290×720 (tema claro e escuro): `visualViewport.width=290`, `documentElement.clientWidth=290`, mas `innerWidth=320` e `scrollWidth=320`. A media query `max-width:300px` corresponde; `html` e `body` computam `min-width:320px`, e `body` usa `overflow-x:clip`. O header permanece em 320 px. O botão de menu ocupa x=264–306; 26 dos 42 px ficam dentro do viewport visual e 16 px são cortados. A geometria medida foi igual nos dois temas.

A passagem anterior em browser com scrollbar vertical clássica encontrou `clientWidth=275` e 11 px do botão visíveis na mesma largura nominal. A diferença corresponde à largura útil disponível/scrollbar do contexto; não invalida o corte confirmado pela emulação mobile. Em 320 e 335 px da amostra emulada, `clientWidth=scrollWidth` e a largura do header acompanha a viewport. A emulação foi removida após a leitura.

Isto confirma um recorte responsivo em 290 px e mantém aberta a investigação NAV-005/#218. A medição não escolhe breakpoint nem autoriza implementação. Sem CSS, dados ou preferência persistente alterados.
