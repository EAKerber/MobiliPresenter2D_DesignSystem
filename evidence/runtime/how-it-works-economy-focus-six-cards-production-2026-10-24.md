# Como funciona — foco nos seis cartões de economia em Production (24/10/2026)

## Alvo e contexto

- URL: https://casaemmodulos.casa/how-it-works/#economyTitle
- Deploy atual revalidado pela Netlify: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, READY `6adc221479c773577ed45e23`, publicado em 2026-10-24 03:12:38 UTC.
- Viewport: 1280×720 CSS px.
- Sessão anônima. Foram observados os temas escuro e claro; `prefers-reduced-motion: reduce` não foi ativado.

## Método e resultado

Usei Tab para focar cada um dos seis botões da seção “Por que custa menos?”, sem ativá-los. O CSSOM retornou o mesmo contorno nos seis cartões e em ambos os temas:

- Largura: 2 px; offset: 3 px.
- No tema escuro, cor computada `#D8BC7C` sobre a superfície opaca da seção `#25231F`: contraste calculado **8,52:1**.
- No tema claro, cor computada `#6E512E` sobre a mesma superfície escura `#25231F`: contraste calculado **2,15:1**.

A faixa clara e escura foram verificadas nos seis controles: Compra em escala, Compras coletivas, Produção planejada, Aproveitamento de material, Engenharia já estudada e Menos retrabalho. A captura de tela desta sessão mostra o sexto cartão focado em tema claro.

## Interpretação e limites

O valor claro falha no contraste de 3:1 para indicador não textual de foco, e a largura computada de 2 px diverge da referência VIS-002 registrada de 4 px/offset 3 px. O resultado identifica risco nesta família de seis controles e nesta superfície; não prova comportamento em outros componentes, rotas, browsers, temas ou estados. A medição não decide uma cor de substituição nem autoriza implementação. Nenhum código do produto foi alterado; o achado permanece aberto.
