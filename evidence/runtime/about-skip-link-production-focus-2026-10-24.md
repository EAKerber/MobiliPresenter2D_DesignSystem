# Production About skip-link focus — 2026-10-24

## Alvo e método

- URL: https://casaemmodulos.casa/about/
- Deploy Netlify Production READY: [6adc221479c773577ed45e23](https://app.netlify.com/projects/mobilipresenter2d/deploys/6adc221479c773577ed45e23)
- Produto: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`
- Navegador em contexto isolado, sem sessão autenticada ou token; viewport móvel de 390 × 844 CSS px; tema escuro e `prefers-reduced-motion: reduce`.
- O link de salto foi focalizado via teclado. Enter foi enviado enquanto o link estava focado. O DOM, URL e elemento ativo foram lidos após a navegação.

## Resultado observado

O primeiro Tab focaliza e revela “Pular para o conteúdo” (`.about-skip`, href `#main`). Pressionar Enter navega para `/about/#main`, mas o foco ativo termina em `BODY`; o elemento `main#main` não recebe foco. No readback, o alvo existe, `main.tabIndex` reporta -1 e não há atributo `tabindex` explícito. `scrollY` permaneceu 0 nessa passagem.

A aparência do anel no foco do link havia sido medida antes nesta mesma auditoria de Production: 2.67 px, offset de 2.67 px, claro `#6E512E` e escuro `#D8BC7C`. VIS-002 registra referência aprovada de 4 px, offset 3 px, claro `#8B6A40` e escuro `#D8BC7C`. A PR de produto [#239](https://github.com/EAKerber/MobiliPresenter2D/pull/239) trata somente da aparência CSS; ela não implementa a transferência do foco ao destino. A correção de estilo foi observada no preview #239, não nesta Production.

## Limites

É uma passagem em uma rota, viewport e tema. Não houve teste com leitor de tela, outros navegadores ou combinações de tema/largura. Nenhum código, configuração, banco ou deploy foi alterado. O resultado registra comportamento observado e não cria nem aprova uma implementação.
