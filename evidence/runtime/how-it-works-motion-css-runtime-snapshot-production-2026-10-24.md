# Como funciona — movimento e CSS no snapshot de Production (24/10/2026)

## Alvo e contexto

- URL: https://casaemmodulos.casa/how-it-works/
- Production confirmada pela Netlify: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`.
- Viewport: 1280×720 CSS px; tema escuro; sessão anônima.
- `prefers-reduced-motion: reduce` retornou `false`; não foi possível emular a preferência neste escopo.

## Observação runtime

- No snapshot após estabilização da rota, `animation-name` não indicou animação CSS em nenhum elemento ou pseudo-elemento consultado.
- A consulta `document.getAnimations` não estava disponível no escopo de avaliação (`typeof` retornou `undefined`). Portanto, a ausência de animações/transições ativas não foi provada de forma completa; o estado de transições segue desconhecido.
- A leitura não simulou rede lenta nem falha de imagem.

## Origem estática no commit servido

- [`app/public-theme.css`, linhas 24–25](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/public-theme.css#L24-L25) declara uma regra global para `prefers-reduced-motion: reduce`.
- [`app/how-it-works/how-it-works.css`, linhas 251–252](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/how-it-works/how-it-works.css#L251-L252) também declara redução de duração de animação e transição na rota.

A presença estática dessas regras não valida o efeito no DOM com a preferência ativa. Movimento reduzido em runtime, transições em andamento e estados de carga/erro permanecem pendentes; nenhum código do produto foi alterado.
