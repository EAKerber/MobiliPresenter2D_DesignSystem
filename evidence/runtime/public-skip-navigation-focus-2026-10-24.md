# Landing e Como funciona — link de salto e foco visível em Production (24/10/2026)

## Alvo e método

- Production: deploy READY `6adc221479c773577ed45e23`, produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Contexto de navegador isolado e anônimo, viewport móvel de 390 × 844 CSS px, temas claro/escuro e movimento reduzido.
- Em cada rota, o DOM foi consultado para links de salto e alvo `main`; o primeiro Tab foi enviado como entrada real de teclado.

## Resultado observado

Nas rotas `/` e `/how-it-works/`:

- Não havia link `.skip-link` nem `a[href="#main"]`. O elemento `main` não tinha id.
- O primeiro Tab focou o link da marca (“Casa em Módulos, início”). Em Como funciona existe uma CTA interna “VEJA COMO FUNCIONA” para `#passos`; ela não é um link de salto para o conteúdo.
- No link da marca, a CSSOM retornou largura/offset computados de 2.67 px. A regra global carregada de `app/public-theme.css` (blob `e2add5053fbc1a897c035eb854b168c9711d2d18`, linha 23) declara 3 px/offset 3 px; `app/ui-theme.css` (blob `b0f04c566183ba1f9c015f5d2a827db9e91dea45`, linhas 113–114) fornece claro `#6E512E` e escuro `#D8BC7C`. Um elemento de teste com `outline:3px` também retornou 2.67 px na CSSOM; a causa permanece desconhecida, então a medição computada não é tratada como valor declarado.
- VIS-002 registra 4 px/offset 3 px, claro `#8B6A40` e escuro `#D8BC7C`. A regra fonte diverge em largura (3 px) e na cor clara; o offset global declarado coincide. A CSSOM computada conserva a anomalia de 2.67 px descrita acima.

A página About tem um caso distinto: possui link `#main`, mas Enter termina com foco no body. Consulte a [evidência de About](about-skip-link-production-focus-2026-10-24.md).

## Limites

Uma passagem por rota e viewport, sem leitor de tela ou outros navegadores. Os resultados descrevem o deploy Production observado; não determinam sozinhos a solução de navegação nem autorizam mudança de produto. Nenhum código, configuração ou deploy foi alterado.
