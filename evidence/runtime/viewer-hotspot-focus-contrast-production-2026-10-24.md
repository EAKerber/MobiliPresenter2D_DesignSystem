# Viewer Production — foco de teclado no hotspot 02

**Estado:** observação runtime pontual; não é homologação global. **Produto:** `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. **Deploy:** `6adc221479c773577ed45e23`, READY, publicado em 2026-10-24 03:12:38 UTC.

## Execução observada

- Rota pública `/viewer/`, sem login, em aba temporária e isolada do navegador; viewport observado de 1265 × 713.
- Foquei por Tab o botão “Ver ficha de Módulo 02, Inferior do fogão”, sem clicar nem ativá-lo. A ficha do Módulo 01 continuou selecionada.
- Em Claro e Escuro, o elemento estava em `:focus-visible` e a captura mostrou o contorno ao redor do hotspot e o marcador “02”.
- Após a amostra, restaurei o tema Claro, que era o estado inicial desta aba, e fechei a aba temporária. Nenhum dado de conta ou negócio foi alterado.

## Estilo computado e fonte

No hotspot focado, os dois temas computaram:

- O botão não tem contorno CSS: `outline: 0`.
- O pseudo-elemento `::after` desenha uma borda de 2 px na cor `color(srgb 0.865412 0.768784 0.547922)` (aprox. `#DDC48C`) e um preenchimento `rgba(216, 188, 124, 0.19)`.
- A cor da borda e do preenchimento foi a mesma nos dois temas; o marcador separado permaneceu escuro com texto claro.
- Fonte: `app/viewer/viewer.css`, blob `90d23678630c17f63ac343bfd7e5e1ce3bbcb1b2` no commit de Production. A regra `.scene-hotspot:focus-visible` zera o outline; `::after` fornece a borda/preenchimento e `.scene-hotspot__tag` mostra o número.

## Limites e leitura

O indicador estava presente visualmente na amostra, mas a borda atravessa uma fotografia com luminância variável. A API de inspeção usada não expôs `document.createElement`, impedindo amostragem de pixels da imagem para calcular contraste; por isso não registro uma razão numérica nem afirmo conformidade. As capturas foram inspecionadas durante a sessão e não foram persistidas.

A largura computada de 2 px também não foi homologada contra a referência geométrica VIS-002 de 4 px; ainda falta decidir se as pistas alternativas do hotspot (borda, preenchimento e marcador) satisfazem o critério em fundos claros e escuros. Isso amplia a evidência do módulo 02 em dois temas, sem alterar CSS, tokens, produto ou decisão canônica.

## Complemento móvel — 390 × 844

- Repeti em `/viewer/` no viewport 390 × 844 (DPR 1), temas Claro e Escuro, sem login.
- Tab levou ao hotspot 02 com `:focus-visible` verdadeiro nos dois temas. A borda permaneceu em 2 px e a mesma cor computada aproximada `#DDC48C`; o marcador “02” permaneceu visível.
- O alvo ficou em x=129, y=735, 56 × 57 px, dentro da cena (x=22, y=608, 331 × 221 px); o marcador ficou em x=144, y=701, 26 × 26 px. Ambos couberam na cena, sem recorte observado.
- `documentElement.scrollWidth` e `clientWidth` foram ambos 375 px; sem overflow horizontal nesta amostra. O Módulo 01 permaneceu selecionado durante a passagem.
- Ao final restaurei o tema Claro, removi o viewport override e fechei a aba. Capturas foram inspecionadas mas não persistidas. Esta observação não mede contraste da borda contra os pixels da fotografia e não prova comportamento em outros tamanhos/dispositivos.


## Complemento móvel — sequência dos sete hotspots

- Em 390 × 844, percorri por Tab os hotspots 01–07 sem ativá-los, no tema Claro. Nos sete, `:focus-visible` foi verdadeiro, o marcador do módulo ficou visível e o retângulo-alvo e marcador permaneceram dentro da cena; não houve overflow horizontal (`scrollWidth=clientWidth=375 px`).
- Hotspots 02–07 computaram borda de foco de 2 px em `#DDC48C` e preenchimento `rgba(216, 188, 124, 0.19)`.
- Exceção do hotspot 01, que já estava selecionado: nos temas Claro e Escuro, a borda do pseudo-elemento computou como transparente, apesar de `:focus-visible=true`; apenas o preenchimento semitransparente diferenciou o estado focado. O quadro de seleção permaneceu com a mesma geometria/estilo quando o foco foi movido ao hotspot 02. Não concluí que esse preenchimento seja imperceptível; a captura móvel mostra o alvo, porém contraste sobre a foto e distinção suficiente entre foco e seleção não foram medidos.
- Tema Claro e viewport padrão foram restaurados; a aba temporária foi fechada. A amostra não cobre outros dispositivos, cenas ou navegadores.


## Recheck comparativo — hotspot 01 selecionado e focado (24/10/2026)

- Netlify confirmou o deploy Production atual `6adc221479c773577ed45e23` READY em `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. Na rota `/viewer/`, comparei o módulo 01 selecionado sem foco e com o estado `:focus-visible` em temas claro e escuro, no viewport CSS 1279 × 663 (DPR 1,5). Não cliquei nem alterei a seleção.
- Nos dois temas, sem foco o quadro de seleção e o marcador “01” já estavam visíveis. Com `:focus-visible=true`, o botão manteve `outline: 0`; `::after` computou `border-color: transparent` e `background: rgba(216, 188, 124, 0.19)`. Portanto, a pista adicionada pelo foco é apenas um preenchimento semitransparente sobre o alvo já selecionado; não aparece uma borda adicional.
- A comparação pareada de capturas em tela mostrou mudança de tonalidade no módulo, mas não estabelece que a diferença seja suficientemente distinguível em todo o fundo fotográfico. Não registro razão de contraste: uma tentativa de recomposição apenas das imagens do DOM foi descartada como incompleta, pois a cena também contém máscaras de acabamento e overlays de sombra/highlight.
- A correspondência entre foco e seleção permanece uma questão aberta, sem declarar falha normativa ou aprovar correção. A emulação foi removida, a aba isolada fechada e a aba inicial restaurada. Capturas não foram persistidas; nenhum produto, CSS ou token foi alterado.
