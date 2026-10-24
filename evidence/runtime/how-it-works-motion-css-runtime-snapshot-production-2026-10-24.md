# Como funciona — movimento e CSS no snapshot de Production (24/10/2026)

## Alvo e contexto

- URL: https://casaemmodulos.casa/how-it-works/
- Production confirmada pela Netlify: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`.
- Viewport: 1280×720 CSS px; tema escuro; sessão anônima.
- `prefers-reduced-motion: reduce` retornou `false`; não foi possível emular a preferência neste escopo.

## Observação runtime

- No snapshot após estabilização da rota, `animation-name` não indicou animação CSS em nenhum elemento ou pseudo-elemento consultado.
- A leitura inicial usava um escopo sem `document.getAnimations`; a revalidação posterior com DevTools e emulação de mídia está registrada abaixo e conseguiu ler animações/transições nos estados observados.
- A leitura não simulou rede lenta nem falha de imagem.

## Origem estática no commit servido

- [`app/public-theme.css`, linhas 24–25](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/public-theme.css#L24-L25) declara uma regra global para `prefers-reduced-motion: reduce`.
- [`app/how-it-works/how-it-works.css`, linhas 251–252](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/how-it-works/how-it-works.css#L251-L252) também declara redução de duração de animação e transição na rota.

A presença estática dessas regras não valida o efeito no DOM com a preferência ativa. Movimento reduzido em runtime, transições em andamento e estados de carga/erro permanecem pendentes; nenhum código do produto foi alterado.


## Revalidação com emulação de movimento — Production (24/10/2026)

- Revalidei `https://casaemmodulos.casa/how-it-works/` no deploy READY `6adc221479c773577ed45e23`, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, em contexto anônimo isolado do navegador e viewport CSS 1280 × 720.
- Com `prefers-reduced-motion: no-preference`, `matchMedia('(prefers-reduced-motion: reduce)')` foi `false`. Após a rota estabilizar, `document.getAnimations({subtree:true})` retornou zero; cinco elementos declaravam transições CSS. Ao passar o ponteiro sobre “Veja como funciona”, o CTA computou `transition-property: transform, background`, `transition-duration: 0.18s, 0.18s` e deslocamento final de −2 px. A captura não mediu a duração ativa da transição; registra o estilo e estado de hover, não uma animação em curso.
- Emulando `prefers-reduced-motion: reduce`, `matchMedia` passou a `true`; no mesmo hover, as durações computadas de transição e animação foram `1e-05s` (0,00001 s), e `document.getAnimations` retornou zero. O deslocamento final de −2 px ainda compõe o estado de hover, mas sua transição ficou praticamente instantânea.
- Abri o primeiro disclosure nativo durante a emulação: `details.open` mudou para `true` e seu conteúdo apareceu; `details`, `summary` e conteúdo computaram `transition-duration: 1e-05s`, sem animação ativa. No modo sem redução, ao fechar esse mesmo disclosure, a duração computada foi `0s` e a lista de animações também ficou vazia.
- A emulação foi removida, a aba de contexto isolado foi fechada e a aba Chrome previamente aberta voltou a ser a selecionada. Nenhum dado ou configuração permanente foi alterado.

A revalidação confirma o efeito da preferência nos elementos observados e substitui a limitação anterior sobre indisponibilidade de `document.getAnimations`. O resultado cobre uma rota, um viewport, um CTA em hover e um disclosure; não certifica todas as transições/animações da página ou de iframes. A falha de imagem continua sem simulação. A observação parcial de rede lenta está registrada abaixo.


## Rede lenta — observação parcial em Production (24/10/2026)

- Em contexto anônimo isolado, com Slow 3G e cache ignorado, a rota concluiu o carregamento. A navegação inicial levou mais que o limite de espera do comando, mas o documento chegou a `readyState=complete` durante a inspeção.
- O recurso `hero-abertura.webp` registrou duração de aproximadamente 10.230 ms (`transferSize` 159.562 bytes; `decodedBodySize` 159.262 bytes). É uma medição desta sessão sob emulação, não um SLA ou comparação de rede real.
- Durante a passagem pela página, houve 28 imagens: 12 carregadas, 16 ainda pendentes por carregamento preguiçoso e zero falhas. Em um instante, duas imagens lazy no limite inferior da viewport estavam pendentes; em snapshots posteriores, as imagens que entraram na área visível apareceram carregadas. O estado é temporal e não indica falha por si só.
- Nenhuma falha de imagem foi induzida; portanto, fallback visual para erro continua sem validação. Preferência de rede e demais emulações foram redefinidas e a aba isolada foi fechada; a aba pré-existente permaneceu selecionada.

Esta evidência confirma atraso perceptível sob Slow 3G e ausência de falhas na amostra observada. Não confirma o comportamento de erro, a experiência completa em rede lenta, nem todas as imagens/estados da rota.
