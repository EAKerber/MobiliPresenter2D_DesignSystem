# Menu público: Escape em Production — 24/10/2026

## Alvo e contexto

- Site: [Production](https://casaemmodulos.casa/), branch `main`, commit `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Deploy Netlify lido como READY: `6adc221479c773577ed45e23`.
- Navegador isolado, sem sessão; viewport CSS `390 × 844`, touch/mobile, preferência clara e `prefers-reduced-motion: reduce`.
- A página concluiu o carregamento sem overflow horizontal (`clientWidth=scrollWidth=390`); 17/17 imagens observadas estavam carregadas.

## Interação verificada

1. O botão do menu foi acionado por clique no navegador.
2. Aberto: `aria-expanded=true`, navegação visível e foco no botão `.menu-toggle`.
3. Após pressionar Escape: `aria-expanded=false`, navegação com `display:none` e não visível; foco permaneceu no botão `.menu-toggle`.

## Escopo

Esta passagem comprova Escape e o estado/foco do menu público na head de Production. Não verifica clique externo, percurso completo de teclado, retornos de foco após navegação, todos os breakpoints/temas nem se todas as animações respeitam movimento reduzido. Não atualiza o resultado do preview #234 para outras rotas. Nenhum dado ou estado de produto foi alterado.
