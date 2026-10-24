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

O indicador estava presente visualmente na amostra, mas a borda atravessa uma fotografia com luminância variável. A limitação inicial do wrapper não expor `document.createElement` foi superada numa revalidação posterior. As medições de capturas pareadas registradas abaixo comparam pixels no mesmo ponto antes e depois de focar; não são uma medição global de contraste de texto nem uma certificação normativa.

A largura computada de 2 px também não foi homologada contra a referência geométrica VIS-002 de 4 px; ainda falta decidir se as pistas alternativas do hotspot (borda, preenchimento e marcador) satisfazem o critério em fundos claros e escuros. Isso amplia a evidência do módulo 02 em dois temas, sem alterar CSS, tokens, produto ou decisão canônica.

## Complemento móvel — 390 × 844

- Repeti em `/viewer/` no viewport 390 × 844 (DPR 1), temas Claro e Escuro, sem login.
- Tab levou ao hotspot 02 com `:focus-visible` verdadeiro nos dois temas. A borda permaneceu em 2 px e a mesma cor computada aproximada `#DDC48C`; o marcador “02” permaneceu visível.
- O alvo ficou em x=129, y=735, 56 × 57 px, dentro da cena (x=22, y=608, 331 × 221 px); o marcador ficou em x=144, y=701, 26 × 26 px. Ambos couberam na cena, sem recorte observado.
- `documentElement.scrollWidth` e `clientWidth` foram ambos 375 px; sem overflow horizontal nesta amostra. O Módulo 01 permaneceu selecionado durante a passagem.
- Ao final restaurei o tema Claro, removi o viewport override e fechei a aba. Capturas foram inspecionadas mas não persistidas. Este recorte móvel inicial não mediu contraste; uma revalidação posterior mediu dois hotspots em 390 × 844, ainda sem cobertura dos demais fundos/dispositivos.


## Complemento móvel — sequência dos sete hotspots

- Em 390 × 844, percorri por Tab os hotspots 01–07 sem ativá-los, no tema Claro. Nos sete, `:focus-visible` foi verdadeiro, o marcador do módulo ficou visível e o retângulo-alvo e marcador permaneceram dentro da cena; não houve overflow horizontal (`scrollWidth=clientWidth=375 px`).
- Hotspots 02–07 computaram borda de foco de 2 px em `#DDC48C` e preenchimento `rgba(216, 188, 124, 0.19)`.
- Exceção do hotspot 01, que já estava selecionado: nos temas Claro e Escuro, a borda do pseudo-elemento computou como transparente, apesar de `:focus-visible=true`; apenas o preenchimento semitransparente diferenciou o estado focado. O quadro de seleção permaneceu com a mesma geometria/estilo quando o foco foi movido ao hotspot 02. O preenchimento difere do estado sem foco, mas sua distinção visual sobre a foto foi apenas parcial; a revalidação pareada abaixo mediu a diferença de pixel desse estado sem extrapolar para outros pontos.
- Tema Claro e viewport padrão foram restaurados; a aba temporária foi fechada. A amostra não cobre outros dispositivos, cenas ou navegadores.


## Recheck comparativo — hotspot 01 selecionado e focado (24/10/2026)

- Netlify confirmou o deploy Production atual `6adc221479c773577ed45e23` READY em `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. Na rota `/viewer/`, comparei o módulo 01 selecionado sem foco e com o estado `:focus-visible` em temas claro e escuro, no viewport CSS 1279 × 663 (DPR 1,5). Não cliquei nem alterei a seleção.
- Nos dois temas, sem foco o quadro de seleção e o marcador “01” já estavam visíveis. Com `:focus-visible=true`, o botão manteve `outline: 0`; `::after` computou `border-color: transparent` e `background: rgba(216, 188, 124, 0.19)`. Portanto, a pista adicionada pelo foco é apenas um preenchimento semitransparente sobre o alvo já selecionado; não aparece uma borda adicional.
- A comparação pareada de capturas em tela mostrou mudança de tonalidade no módulo, sem estabelecer suficiência em todo o fundo fotográfico. A tentativa de recomposição das imagens do DOM foi descartada por omitir máscaras de acabamento e overlays de sombra/highlight; por isso a medição abaixo usa pixels do screenshot real, no mesmo ponto antes/depois, e não uma cena reconstruída.
- A correspondência entre foco e seleção permanece uma questão aberta, sem declarar falha normativa ou aprovar correção. A emulação foi removida, a aba isolada fechada e a aba inicial restaurada. Capturas não foram persistidas; nenhum produto, CSS ou token foi alterado.


## Medição pareada de pixels — estados de foco em 390 × 844 (24/10/2026)

- Produção foi revalidada pelo Netlify: deploy `6adc221479c773577ed45e23` READY, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. Em contexto isolado, capturei a viewport CSS 390 × 844, DPR 1, sem hover e com rolagem idêntica. Comparei screenshots do DOM renderizado antes/depois de `:focus-visible`, sem ativar o módulo. Repeti em Claro e Escuro; a composição da foto e os resultados foram iguais nos dois temas.
- **Hotspot 02, não selecionado:** os 200 pixels centrais amostrados ao longo da borda computada de 2 px mudaram. A razão de luminância entre cada pixel focado e o pixel correspondente sem foco foi min 1,07:1, mediana 1,41:1, P95 1,47:1 e máximo 1,49:1; nenhum dos 200 pontos atingiu 3:1. Isso mede a alteração efetivamente renderizada nesta borda/fotografia e viewport, não classifica por si só conformidade geral.
- **Hotspot 01, já selecionado:** o estilo focado mantém `border-color: transparent` e acrescenta preenchimento `rgba(216, 188, 124, 0.19)`. Na região interna de 3.132 pixels, 3.108 mudaram; a razão de luminância focado/sem foco teve mediana 1,076:1, P95 1,083:1 e máximo 1,091:1; nenhum ponto atingiu 3:1. A moldura de seleção e o marcador “01” já apareciam sem foco.
- As razões acima comparam estado focado ao estado imediatamente anterior em cada mesmo ponto do screenshot; não são contraste de texto nem avaliação completa de conformidade. São alertas locais de baixa distinção percebida no par observado. Outros hotspots, estados de seleção, temas de conteúdo, fundos e dimensões continuam pendentes.

Nenhuma decisão canônica ou código do produto foi alterado. A emulação foi removida e a aba isolada fechada.


## Referência de critério — WCAG 2.2 SC 2.4.13 (24/10/2026)

A W3C descreve o critério **2.4.13 Focus Appearance (AAA)** como exigindo uma área de indicador equivalente a um perímetro de 2 CSS px e mudança de contraste de ao menos 3:1 entre os mesmos pixels focados e sem foco ([W3C, Understanding SC 2.4.13](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance)). No screenshot do hotspot 01 selecionado, toda a região `::after` amostrada ficou abaixo de 1,10:1; portanto nenhum pixel amostrado atingiu a mudança 3:1 do critério nesse estado. No hotspot 02, nenhum dos 200 pixels amostrados no trecho de borda de 2 px atingiu 3:1; a contribuição do preenchimento fora desse trecho e a área completa do indicador não foram auditadas. Isto é uma sinalização local contra o critério AAA, não avaliação formal de conformidade do site nem conclusão sobre WCAG AA. A decisão VIS-002 permanece com `implementationAuthorized: false`; nenhuma correção foi aplicada.
