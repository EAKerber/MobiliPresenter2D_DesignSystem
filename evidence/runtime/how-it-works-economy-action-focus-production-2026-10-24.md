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

## Risco de contraste derivado da cascata — não medido no browser

A entrada `app/how-it-works/index.html` carrega `how-it-works.css` e, depois, `ui-theme.css`. No tema claro, `html[data-theme="light"] :focus-visible` (ui-theme.css, linha 113; especificidade 0,2,1) supera `.economy-action:focus-visible` (how-it-works.css, linha 271; especificidade 0,2,0), que declara `--public-accent-highlight`. A fonte prevê, portanto, outline `#6E512E` no botão focado. O espaço ao redor dele é o fundo opaco `.economy-section { background: #25231f }` (how-it-works.css, linha 69), já que o outline tem offset 3 px.

Com esses dois valores declarados, a razão de luminância relativa calculada é **2,15:1**. É uma inferência da cascata e da superfície declarada; não é um valor computado pelo browser, nem constitui uma decisão normativa sobre correção. A captura confirma que o anel aparece, mas sua cor efetiva e contraste ainda precisam de readback runtime antes de classificar conformidade. O tema escuro usa `#D8BC7C` e a razão calculada para o mesmo fundo é 8,52:1.