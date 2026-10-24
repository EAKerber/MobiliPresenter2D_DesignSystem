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