# PR #242 — implementação do placeholder para falha de imagem da cena

Data: 2026-10-26 UTC

## Código e escopo

- Produto: `EAKerber/MobiliPresenter2D`, branch `fix/viewer-hotspot-focus-approved-vis002-20261024`.
- Head: `618877e4dc9fcf9376269e15c24bd937ef4e93e9`, commit `Add accessible Viewer scene failure placeholder`.
- Arquivos: `app/viewer/scene-adapters.js`, `app/viewer/viewer.css`, `app/viewer/index.html`, `app/viewer/scene-adapters.test.mjs`.
- A imagem-base ou qualquer imagem de camada visível que falhe oculta toda a composição parcial, incluindo base, layers, hotspots e frame de seleção. A cena recebe placeholder `role=alert` com “Imagem indisponível” e descrição; o rótulo acessível do stage passa a informar a falha.
- Falhas de grupos `.is-hidden` não cobrem a cena. A lista de URLs com falha permite reavaliar assets em um render subsequente; imagem quebrada já completa também é detectada após render.
- O frame `.scene-stage` conserva proporção 3:2, e o placeholder usa tokens de superfície/texto existentes nos dois temas. As chaves de cache do adapter e da folha foram atualizadas.

## Verificação local e CI

- `node --test --test-reporter=dot app/viewer/scene-adapters.test.mjs`: 17 testes passaram. A fixture exercita erro capturado em fase capture, erro de camada oculta ignorado e falha de camada visível cobrindo o stage. A suíte é unitária; não substitui uma falha HTTP real no browser.
- Todos os sete workflows GitHub observados no head `618877e4dc9fcf9376269e15c24bd937ef4e93e9` concluíram com sucesso: Current variant fidelity, App build purity, Summary pricing browser, Stone browser, Current asset gates, Public routing before Clerk e Mobile browser.
- O status API de commits não lista checks externos separados para esse head.

## Limites e estado de deploy

- Os Deploy Previews por PR foram desativados pelo usuário para controlar consumo de minutos Netlify. Nenhum Deploy Preview desse head foi criado e nenhum deploy manual foi feito.
- Portanto, o comportamento visual do placeholder em browser real, nos temas claro/escuro e viewports mobile/desktop, continua pendente. Capturas e 404s de previews antigos são evidência da falha antes da mudança, não validação da solução atual.
- PR #242 permanece Draft, sem merge e sem Production. Nenhuma mudança foi feita em `decisions.json`.
