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


## Complemento quantitativo — hotspots 02–07, perímetro de 2 px (24/10/2026)

- Revalidei o deploy Production `6adc221479c773577ed45e23`, em `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, em contexto anônimo isolado, viewport CSS 390 × 844, DPR 1, tema claro. Cada hotspot 02–07 foi posto em `:focus-visible` sem ativação; o estado selecionado continuou no módulo 01. O screenshot-base tinha foco fora dos hotspots. A posição dos alvos permaneceu igual entre as capturas pareadas.
- O CSS computou a mesma pista nos seis alvos: `::after` com borda sólida de 2 px em aprox. `#DDC48C`, preenchimento `rgba(216, 188, 124, 0.19)`, raio 6 px e inset 2 px. A sequência de Tab dos sete alvos já havia sido validada na passagem anterior; nesta comparação, confirmei `:focus-visible=true` em cada estado antes de capturar.
- Comparei a luminância dos pixels correspondentes na captura focada e na captura-base, ao longo dos quatro trechos retos do anel de 2 px, excluindo os cantos arredondados de 6 px. A razão de contraste mínimo/mediana/P95/máximo e a quantidade de amostras ≥3:1 foram: Módulo 02, 344 pontos, 1,009 / 1,148 / 1,522 / 1,537, 0 pontos; Módulo 03, 548 pontos, 1,000 / 1,203 / 1,476 / 1,507, 0; Módulo 04, 772 pontos, 1,000 / 1,190 / 1,476 / 10,558, 11; Módulo 05, 368 pontos, 1,000 / 1,155 / 1,822 / 2,421, 0; Módulo 06, 560 pontos, 1,000 / 1,190 / 1,538 / 1,554, 0; Módulo 07, 288 pontos, 1,000 / 1,322 / 2,897 / 4,088, 15.
- O resultado varia muito na fotografia: módulos 04 e 07 tiveram alguns pontos ≥3:1 sobre trechos escuros, mas as medianas de todos os módulos ficaram entre 1,148:1 e 1,322:1. Isso mantém o alerta de pista irregular no fundo variável. A nova amostragem inclui ambas as linhas de pixels da borda e é distinta da amostra anterior de 200 centros do Módulo 02 (mediana 1,41:1); não compare os quantis como se fossem a mesma seleção de pixels. Medições locais; não provam conformidade nem não conformidade do site.
- Repeti os seis pareamentos no tema escuro com o mesmo viewport e a mesma posição. `matchMedia('(prefers-color-scheme: dark)')` retornou true, `data-theme=dark` e o fundo da página computou `rgb(17, 18, 16)`. Os resultados por pixel dos perímetros foram idênticos aos do tema claro, pois a cena fotográfica e a pista do hotspot permaneceram iguais. Os dois temas agora estão cobertos para os módulos 02–07 nesta largura. Não inspecionei estados selecionados dos Módulos 02–07 nem outros viewports, cenas ou dispositivos. Não apliquei correções nem alterei decisão canônica. Emulação removida, aba isolada fechada e aba original da casa preservada.


## Seleção ativa e foco no mesmo hotspot — módulos 02–07 (24/10/2026)

- Em uma nova aba isolada de Production, viewport CSS 390 × 844, DPR 1, tema claro, selecionei cada hotspot 02–07 com Enter. Depois comparei screenshot do hotspot selecionado sem foco (foco em `body`) e com foco novamente em `:focus-visible`, sem nova ativação. Antes de fechar a aba, selecionei de volta o Módulo 01; a seleção ficou nele, tema claro e `scrollY=0`. A página original do usuário permaneceu selecionada e intacta.
- Nos seis hotspots, quando selecionados e focados, o estilo computado manteve `border-color: transparent` e acrescentou `background: rgba(216, 188, 124, 0.19)`; `:focus-visible` era verdadeiro. Portanto, a moldura do estado selecionado não fornece uma borda de foco adicional.
- Nas capturas pareadas, comparei pixels da área interna de preenchimento do `::after`, excluindo a borda e os cantos arredondados, com o mesmo alvo, viewport e estado selecionado. Razões foco/sem foco mínimo/mediana/P95/máximo e pontos ≥3:1: Módulo 02, 2.568 px, 1,001 / 1,141 / 2,671 / 4,145, 23; Módulo 03, 5.220 px, 1,019 / 1,078 / 1,087 / 1,088, 0; Módulo 04, 3.748 px, 1,000 / 1,045 / 1,274 / 4,758, 2; Módulo 05, 2.884 px, 1,001 / 1,088 / 1,738 / 3,215, 1; Módulo 06, 5.523 px, 1,001 / 1,087 / 4,627 / 9,539, 609; Módulo 07, 1.804 px, 1,004 / 1,087 / 1,088 / 1,091, 0.
- A foto produz distribuição desigual: Módulo 06 tem muitos pixels ≥3:1 em partes escuras, mas a mediana é 1,087:1; nos demais, também há trechos isolados com contraste alto e medianas baixas. Isto não homologa a indicação nem equivale a avaliar conformidade normativa; é comparação local do preenchimento adicionado sobre o hotspot selecionado. A amostra selecionada foi feita apenas em tema claro. Tema escuro com seleção ativa, outros fundos, viewports e cenas continuam pendentes. Nenhum dado foi persistido nem código, CSS, token ou decisão canônica foi alterado.
