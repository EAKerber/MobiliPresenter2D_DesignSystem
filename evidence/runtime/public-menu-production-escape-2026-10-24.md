# Menu público: Escape em Production — 24/10/2026

## Alvo e contexto

- Site: [Production](https://casaemmodulos.casa/), branch `main`, commit `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Deploy Netlify lido como READY: `6adc221479c773577ed45e23`.
- Navegador isolado, sem sessão; viewport CSS `390 × 844`, touch/mobile, preferência clara e `prefers-reduced-motion: reduce`.
- A página concluiu o carregamento sem overflow horizontal (`clientWidth=scrollWidth=390`); 17/17 imagens observadas estavam carregadas.

## Interações verificadas

- **Mouse:** clique abriu a navegação (`aria-expanded=true`). Um clique no conteúdo fora do menu fechou a navegação (`aria-expanded=false`, `display:none`). Como o alvo externo era uma imagem não focável, o foco terminou no `body`; não houve perda de foco de um controle ativo.
- **Teclado:** a sequência Tab alcançou o botão `#menuToggle`; Enter abriu o menu e moveu o foco para o primeiro link, “Ambientes”. Dois Tabs percorreram os links até “Quem somos”. Escape fechou o menu (`aria-expanded=false`, `display:none`) e devolveu o foco a `#menuToggle`.
- Com `prefers-reduced-motion: reduce`, o menu e o botão tinham `animation-name:none`, duração de transição computada de `1e-05s`, e não havia animações Web em execução no momento da leitura.

## Escopo

A passagem comprova clique externo e um percurso de teclado no menu público da head de Production, em uma combinação de rota, tema e viewport. Não verifica todos os caminhos de teclado, estados de foco dos links, breakpoints/temas adicionais nem todas as animações da página. Não atualiza o resultado do preview #234 para outras rotas. Nenhum dado ou estado de produto foi alterado.
