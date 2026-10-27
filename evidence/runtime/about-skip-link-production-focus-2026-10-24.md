# Production About skip-link focus — 2026-10-24

## Alvo e método

- URL: https://casaemmodulos.casa/about/
- Deploy Netlify Production READY: [6adc221479c773577ed45e23](https://app.netlify.com/projects/mobilipresenter2d/deploys/6adc221479c773577ed45e23)
- Produto: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`
- Navegador em contexto isolado, sem sessão autenticada ou token; viewport móvel de 390 × 844 CSS px; tema escuro e `prefers-reduced-motion: reduce`.
- O link de salto foi focalizado via teclado. Enter foi enviado enquanto o link estava focado. O DOM, URL e elemento ativo foram lidos após a navegação.

## Resultado observado

O primeiro Tab focaliza e revela “Pular para o conteúdo” (`.about-skip`, href `#main`). Pressionar Enter navega para `/about/#main`, mas o foco ativo termina em `BODY`; o elemento `main#main` não recebe foco. No readback, o alvo existe, `main.tabIndex` reporta -1 e não há atributo `tabindex` explícito. `scrollY` permaneceu 0 nessa passagem.

Na leitura CSSOM desta auditoria, o contorno computado foi 2.67 px/offset 2.67 px. A regra global carregada de `app/public-theme.css` (blob `e2add5053fbc1a897c035eb854b168c9711d2d18`, linha 23) declara 3 px/offset 3 px; `app/ui-theme.css` (blob `b0f04c566183ba1f9c015f5d2a827db9e91dea45`, linhas 113–114) fornece as cores claro `#6E512E` e escuro `#D8BC7C`. `app/about/about.css` não substitui essa regra de foco. Na mesma sessão, até um elemento de teste com `outline:3px` computou 2.67 px; a causa dessa diferença entre declarado e computado não foi identificada. Portanto, a divergência comprovada pela fonte é largura declarada de 3 px contra a referência VIS-002 de 4 px, mais a cor clara; o offset declarado 3 px coincide. PR produto [#239](https://github.com/EAKerber/MobiliPresenter2D/pull/239) ajusta o CSS do About no preview, mas não implementa a transferência do foco ao destino.

## Limites

É uma passagem em uma rota, viewport e tema. Não houve teste com leitor de tela, outros navegadores ou combinações de tema/largura. Nenhum código, configuração, banco ou deploy foi alterado. O resultado registra comportamento observado e não cria nem aprova uma implementação.
