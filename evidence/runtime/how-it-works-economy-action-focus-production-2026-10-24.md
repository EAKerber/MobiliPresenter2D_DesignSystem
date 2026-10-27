# Como funciona — foco dos cards de economia em Production

**Estado:** observação runtime; não é homologação visual. **Produto:** main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf. **Deploy principal:** 6adc221479c773577ed45e23, READY.

## Execução observada

- Rota pública `/how-it-works/`, em aba isolada e sem login. Captura em viewport 1251 × 713.
- A navegação por Tab chegou ao botão “Compra em escala” (estado `aria-expanded=false`); não abri o card nem acionei conteúdo.
- No tema escuro, a captura mostrou o contorno externo do card focado. No tema claro, após mover o mesmo foco para a seção e exibir o alvo, também se via um contorno ao redor do card.
- Restaurei o tema escuro que estava ativo no início e fechei a aba isolada. Não alterei dados de conta ou negócio. As capturas foram inspecionadas, mas não persistidas.

## Fonte e limite da evidência

Em `app/how-it-works/how-it-works.css` (blob `52f36d212d286ef5157a20fc822cbfab25e09b2f`, linha 271), `.economy-action:focus-visible` declara `outline: 2px solid var(--public-accent-highlight)` e offset 3 px. A folha `ui-theme.css` também contém uma regra ampla de cor por tema. Não medi a cor computada nem contraste do anel sobre o painel escuro; a aparência visível nas capturas não substitui essa medição.

Amostra limitada a um card, uma rota e um viewport nos dois temas. Não verifiquei leitores de tela, outros cards/fundos, recorte, mobile ou outros navegadores. O resultado confirma a presença de contorno na amostra; não declara conformidade com o padrão VIS-002 de 4 px/3 px.

## Leitura CSSOM e contraste no tema claro — Production (24/10/2026)

Em uma nova passagem anônima e isolada na mesma rota e deploy, “Compra em escala” recebeu foco real por Tab; `document.activeElement` confirmou o botão focado e `aria-expanded=false`. Sem ativar o card, a leitura de `getComputedStyle` no tema claro retornou:

- `outline: 2px solid rgb(110, 81, 46)` (`#6E512E`);
- `outline-offset`: uma leitura CSSOM nesta sessão retornou `2.66667px`; uma segunda passagem, no mesmo controle em viewport desktop 1280×720, retornou `3px`, igual à regra fonte. A discrepância entre leituras não foi explicada;
- o botão computa preenchimento `rgba(255, 255, 255, 0.05)`, mas seu contêiner `.economy-grid` é transparente e a seção atrás é opaca `rgb(37, 35, 31)` (`#25231F`). Com o offset positivo de 3 px na leitura mais recente, o traço do outline fica fora do preenchimento do botão, sobre a superfície da seção;
- tema: `light`.

A razão de contraste calculada entre as cores CSSOM do outline e da superfície opaca realmente atrás do traço é **2,15:1** (2.15065:1 antes do arredondamento). Portanto a cor prevista pela cascata foi confirmada no runtime e o risco de contraste para o foco neste tema está observado, não apenas inferido. Uma captura mostrou o anel; o registro visual não substitui a leitura CSSOM.

A amostra cobre somente este botão, nesta rota e em viewport desktop no tema claro. Não mede a cor CSSOM do tema escuro, outros cards/superfícies, estados adicionais, mobile, leitores de tela ou outros navegadores. A razão é uma comparação de cores computadas; a avaliação normativa e qualquer correção visual permanecem pendentes do processo canônico VIS-002. Nenhum CSS ou token do produto foi alterado.
