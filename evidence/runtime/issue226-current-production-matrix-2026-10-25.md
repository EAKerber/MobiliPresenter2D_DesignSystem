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
