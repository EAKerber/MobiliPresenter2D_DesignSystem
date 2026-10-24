# Issue #224 — rechecagem estática do carrossel da Landing (24/10/2026)

## Estado observado

- Issue: [#224 — Carrossel oculta o ambiente selecionado no mobile](https://github.com/EAKerber/MobiliPresenter2D/issues/224), continua aberta.
- Reporte original: 4/4 repetições em Production no commit `1878ae1057ce7c6190e0c8cb08a1f3baadd49463`, viewport 390×844, tema escuro.
- Uma rechecagem runtime posterior em Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, 390×844, selecionou Lavanderia no grupo 2 sem reproduzir o retorno. Essa única passagem não encerra o reporte anterior.
- A ordem atual em `app/landing/data.js` mantém Lavanderia como o quinto e último cartão.

## Comparação de fonte entre o reporte original e main atual

- CSS `app/landing/landing.css`: blob SHA igual nos dois commits, `91a7bc7cd912ac7f0a9e81c16fcee576dc50a4ea`.
- JS `app/landing/landing.js`: a fonte completa mudou (`c85c49c163b0af6d6dda30cd9fb8771f851ec496` no snapshot antigo; `7bcc6931716b7c4b32c4eb8386d1d658fd29a471` em main), mas o trecho relevante de `revealCard()` continua usando as mesmas comparações estritas:
  - se `bounds.right > viewport.right || bounds.left < viewport.left`, escolhe a página com `bounds.left >= viewport.right ? 1 : 0`;
  - não há tolerância explícita para subpixels nem cálculo de área de interseção do cartão.
- Em viewport de 390 px, a regra CSS define largura do cartão por `(100vw - 28px - 14px) / 2.45` (aprox. 142,04 px) com gap de 8 px. Pela conta aproximada, a borda direita do último cartão fica alinhada com a borda direita da janela no scroll máximo. Variação fracionária ou um clique antes do término do scroll suave poderia satisfazer `bounds.right > viewport.right` enquanto o cartão ainda começa dentro da janela, fazendo o seletor apontar para a página 0. **Isto é uma hipótese derivada do código e da geometria CSS; não foi confirmada em runtime.**

## Limite e próximo teste

O Chrome DevTools browser bridge não respondeu durante esta passagem, então não medi `scrollLeft`, retângulos CSSOM ou sequência de eventos no preview/Production. Nenhuma alteração de produto foi feita. Para confirmar ou refutar a hipótese, registrar em 320/335/360/390 px e claro/escuro: `selectedId`, índice de paginação, `scrollLeft/maxScroll`, retângulos do quinto cartão/janela antes e após scroll-snap, e a mesma seleção antes/depois do fim do scroll suave. Manter issue aberta até reproduzir ou acumular repetições suficientes para contradizer o histórico 4/4.
