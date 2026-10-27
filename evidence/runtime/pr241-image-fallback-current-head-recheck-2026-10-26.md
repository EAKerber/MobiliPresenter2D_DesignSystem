# PR #241 — readback do fallback de imagem no head atual — 26/10/2026

## Contexto

Preview de produto: https://deploy-preview-241--mobilipresenter2d.netlify.app/how-it-works/
Head: `45e532b444967bdd901ac2f49fc8d0548daa881a`
Viewport: 390×844 CSS px, tema escuro, sessão isolada sem credenciais.

## Procedimento e resultado

A ilustração original carregou antes do ensaio. Em seguida, alterei apenas o `src` no DOM de uma aba isolada para um caminho same-origin inexistente. A requisição observada no painel de rede retornou HTTP 404.

O evento `error` ocultou a imagem e revelou o placeholder. O placeholder computou `role="img"` e o nome acessível “Imagem indisponível: Ilustração conceitual de uma planta com medidas e circulação analisadas”; a descrição foi mantida no nó visível. O frame media 352,67×235,10 px antes e depois da falha. A rota permaneceu sem overflow horizontal (`clientWidth=scrollWidth=390`). A captura visual mostrou ícone, estado de indisponibilidade e descrição centralizados sobre o fundo reservado, com legenda preservada.

Restaurei o caminho original; a imagem carregou novamente e o fallback ficou oculto. O ensaio foi temporário no DOM/preview e não alterou código nem dados.

## Limites

A evidência vale para a ilustração principal de `/how-it-works/`, tema escuro e viewport 390×844 no head indicado. Não certifica outras imagens, rotas, temas, viewports, rede lenta, leitores de tela ou Production. Os nove workflows do head atual e os dois status Netlify estavam SUCCESS; esta rechecagem não executou leitura manual nova dos dez seletores de texto da PR #241.
