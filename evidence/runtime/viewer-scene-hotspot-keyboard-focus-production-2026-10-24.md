# Viewer em Production — foco de teclado nos hotspots da cena

**Estado:** observação runtime; não é homologação global. **Produto:** main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf. **Deploy:** 6adc221479c773577ed45e23, READY, publicado em 2026-10-24 03:12:38 UTC.

## Execução observada

- Rota pública `/viewer/`, sem login, em uma aba isolada do navegador; não usei sessão ou credenciais da conta.
- Viewport observado: 1265 × 713. Inspecionei os temas escuro e claro alternando o controle da própria página.
- A ordem de teclado chegou ao container da cena e, em seguida, aos controles dos módulos. O foco foi movido para o checkbox “Ver ficha de Módulo 02, Inferior do fogão”, sem ativar ou selecionar esse módulo.
- Nos dois temas, a captura mostrou uma borda dourada contornando visualmente o módulo 02 e seu marcador “02” visível. O módulo 01 continuou selecionado; isso separa visualmente o estado de foco do estado selecionado nesta passagem.
- A captura foi inspecionada durante a sessão, mas não foi persistida neste repositório. Nenhum dado ou estado do produto foi salvo.

## Relação com a fonte

Em `app/viewer/viewer.css` (blob `90d23678630c17f63ac343bfd7e5e1ce3bbcb1b2`), `.scene-hotspot:focus-visible` zera `outline` (linha 47); o pseudo-elemento `::after` muda borda e fundo (linhas 45–46), e o marcador fica visível (linha 49). O que foi visto corresponde a essas pistas alternativas. O anel de foco do container `.scene-stage` é declarado separadamente.

## Limites

Uma rota, viewport, cena e hotspot em cada tema; sem medição de contraste, teste com leitor de tela, teste em mobile, avaliação de recorte ou variação de navegadores. A evidência mostra que há uma pista visual na amostra; não prova adequação para todos os fundos, módulos ou estados. O mapa VIS-002 continua sujeito a revisão, sem alteração de CSS, tokens ou produto.