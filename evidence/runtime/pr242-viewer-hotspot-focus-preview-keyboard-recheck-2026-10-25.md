# VIS-002 — rechecagem do foco dos sete hotspots no preview #242

Data: 25/10/2026

## Contexto

- Produto PR #242, head `af2166df42019b273c27d672149ebe49b143c0fb`.
- URL: `https://deploy-preview-242--mobilipresenter2d.netlify.app/viewer/`.
- Única cena de Viewer publicada neste branch: Cozinha (`assets/kitchen/base.png` e camadas relacionadas). Não há segunda cena fotográfica de Viewer disponível para generalizar esta leitura.

## Rechecagem por teclado

- Viewport mobile: 390 × 844 CSS px, DPR 1; tema escuro selecionado pelo controle real de tema.
- Tab percorreu os sete botões de hotspot em ordem. Em cada parada, `:focus-visible` foi verdadeiro, `outline` computou `rgb(216, 188, 124)` (`#D8BC7C`), largura 4 px e offset 3 px.
- Os sete retângulos dos hotspots permaneceram dentro de `.scene-stage`; `documentElement.scrollWidth` e `clientWidth` foram 390 px.
- O hotspot 01 permaneceu selecionado enquanto o foco percorreu 01–07; mover o foco não alterou a seleção.
- A captura da cena mostrou o anel no hotspot focado. Isso confirma renderização/posicionamento nesta cena e viewport, não a suficiência do contraste sobre qualquer fotografia.

## Limites e resultado

- A análise aproximada de pixels da única cena publicada já registrada em [amostra de contraste do Viewer](pr242-viewer-focus-image-contrast-sample-2026-10-25.md) mediu medianas de 1,24–1,46:1 no escuro, abaixo de 3:1. Não generalizar essas amostras para outras fotos ou afirmar conformidade WCAG.
- Esta rechecagem confirma o contrato CSS e a geometria autorizados; não altera cores, seletores ou código de produto.
- PR #242 permanece DRAFT para revisão humana da distinção visual na composição. Sem merge ou deploy de Production.