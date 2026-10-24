# Rotas públicas — teclado e carregamento de imagens em Production (24/10/2026)

**Alvo:** `EAKerber/MobiliPresenter2D@main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy Netlify READY `6adc221479c773577ed45e23`. Viewport temporário 390×844 CSS px, tema escuro; rotas visitadas em contexto público. O override de viewport foi removido e as abas temporárias foram fechadas.

| Rota | Imagens no documento | Falhas | Sem `alt` | Overflow horizontal |
|---|---:|---:|---:|---|
| `/` | 18/18 completas | 0 | 0 | Não |
| `/about/` | 3/3 completas | 0 | 0 | Não |
| `/viewer/` | 22/22 completas | 0 | 0 | Não |

Em `/`, a camada `#introSplash` já estava oculta (`opacity:0`, `pointer-events:none`) na primeira leitura. Um clique no botão do menu abriu `primaryNav` imediatamente; Escape fechou e o foco retornou ao botão. Isso confirma o caminho depois da saída da camada, não o clique durante sua animação ativa.

Em `/about/`, o primeiro Tab focou “Pular para o conteúdo”. Enter alterou a URL para `/about/#main`, mas o foco terminou em `BODY`; `main#main` não recebeu foco, não tem atributo `tabindex` e `scrollY` permaneceu em 0. Esse comportamento permanece uma divergência observada; não fiz correção no produto.

Nas três rotas, `prefers-reduced-motion: reduce` retornou `false`. Não há emulação de mídia disponível nesta sessão do browser; o teste não confirma o comportamento quando a preferência está ativa. A API de animações também não estava disponível no escopo de leitura, então a execução de animações não foi medida. Nenhuma falha de imagem ou rede lenta foi simulada. Uma leitura de cada rota/viewport; capturas não persistidas; sem alteração de código ou dados.
