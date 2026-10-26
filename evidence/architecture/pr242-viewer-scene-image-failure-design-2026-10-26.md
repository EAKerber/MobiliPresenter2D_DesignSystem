# PR #242 — contrato proposto para falha de asset na cena do Viewer

Data: 2026-10-26 UTC

## Decisão do usuário

Em caso de falha da imagem-base ou de uma camada visível, **cobrir a cena e mostrar um placeholder com descrição**. O usuário também pediu que a solução anterior de placeholder seja padrão, escalável e mostre a descrição sobre a área reservada.

A implementação fica em preview depois da janela de economia de compute indicada pelo usuário. O limite reportado é 233/300 minutos Netlify, ante 200 pela manhã; até o fim do mês, não atualizar a branch do produto nem disparar Deploy Preview.

## Leitura do código na head observada

- Produto branch `fix/viewer-hotspot-focus-approved-vis002-20261024`, head `584c9d3f06896b9c4f44f4437914c9f7b7400d08`, PR #242.
- `app/viewer/scene-adapters.js`, função `renderSurface()`: cria a imagem-base, as camadas, hotspots e frame de seleção; aplica `.is-hidden` às entidades não visíveis; troca o conteúdo do stage. Não registra listener para falha de imagem.
- `app/core/scene-component.js`, função `renderLayers()`: cria um `img` por entidade; os erros não são agregados à cena.
- `app/viewer/viewer.js` trata falha da projeção/API publicada, mas não asset gráfico: essa falha substitui o conteúdo do root com outro estado de erro.
- `app/viewer/viewer.css` reserva `aspect-ratio: 3 / 2` em `.scene-stage`; os assets ocupam o frame inteiro e hotspots são uma camada sobreposta.

## Contrato de implementação proposto

1. Um 404/erro de decode na base ou em qualquer imagem de camada atualmente visível oculta a composição parcial, hotspots e seleção; um erro em uma camada `.is-hidden` não interrompe a cena enquanto ela continuar oculta.
2. Falha de uma camada visível deve manter o estado de erro ativo se a seleção/configuração a tornar oculta; se essa mesma camada voltar a ficar visível e seguir com erro, a cena continua coberta.
3. O placeholder ocupa o frame 3:2 inteiro, com estado “Imagem indisponível” e descrição explícita de que a composição da cozinha não pôde ser exibida por completo. Nome e descrição substituem o nome acessível normal do stage durante o erro.
4. O handler deve capturar eventos de erro das imagens dentro do stage, sem reagir a assets de ícones, marca, desenhos técnicos ou a imagens fora da cena.
5. A recuperação e a confirmação visual ficam pendentes: a implementação, suíte existente, preview, tema escuro/claro e viewport desktop/mobile devem ser verificados após a liberação de compute.

## Evidência runtime disponível

No preview #241, 390 × 844 px, tema claro, a imagem-base e `02_inferior_fogao.png` receberam 404 same-origin. Em ambos os casos `.scene-stage` ficou em 346,7 × 231,1 px, o número de imagens visíveis carregadas caiu de 18 para 17 e não apareceu fallback. Ambos os originais foram restaurados e carregaram. Esta amostra é só a cena Cozinha, um viewport e um tema. Registro completo: [auditoria cross-route de imagens](../runtime/pr241-public-image-failure-coverage-2026-10-26.md).

## Implementação em PR de produto — head `618877e4dc9fcf9376269e15c24bd937ef4e93e9`

A PR #242 implementa a decisão de falha de cena: erro na imagem-base ou em uma camada visível oculta base, camadas, hotspots e seleção, preservando o frame 3:2 e apresentando placeholder acessível com descrição. Erros de camadas ocultas são ignorados; URLs de assets com falha são verificadas em renderizações subsequentes, inclusive se a camada voltar a ficar visível. O listener captura erros de imagem apenas dentro do stage.

A suíte `node --test --test-reporter=dot app/viewer/scene-adapters.test.mjs` passou localmente (17 testes); os sete workflows GitHub do head atual também passaram. A PR permanece Draft e sem merge/Production. Os Deploy Previews por PR foram desativados pelo usuário e nenhum deploy manual foi iniciado; por isso, a confirmação visual do placeholder neste head permanece pendente. Previews anteriores não comprovam o comportamento do código novo.

[Evidência de implementação, CI e limites](../runtime/pr242-viewer-scene-image-failure-implementation-2026-10-26.md).

## Estado

A decisão define o comportamento de preview; não aprova merge, Production nem implantação. A implementação descrita acima está no head atual da PR #242 e aguarda confirmação visual.