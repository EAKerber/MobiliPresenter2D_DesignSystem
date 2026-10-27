# Revisão local de contraste do foco em hotspots — PR #242 — 25/10/2026

## Alvo e método

- Produto PR [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242), head `af2166df42019b273c27d672149ebe49b143c0fb`.
- Deploy Preview: [Viewer](https://deploy-preview-242--mobilipresenter2d.netlify.app/viewer/).
- Sessão isolada, rota `/viewer/`, cena Cozinha, hotspots 01–07.
- A sequência por teclado chegou a um hotspot com `:focus-visible=true`. Em cada alvo, o CSSOM computou contorno de 4 px e offset de 3 px; claro `#8B6A40`, escuro `#D8BC7C`.
- Comparei a cor do traçado com pixels da imagem `assets/kitchen/base.png` sob o perímetro aproximado do contorno, excluindo os cantos arredondados. A imagem de base tem 1536 × 1024 px. Este cálculo amostra a foto subjacente; não é leitura dos pixels compostos de uma captura nem auditoria WCAG completa.

## Amostra observada

| Tema / viewport | Medianas por hotspot 01–07 | Amplitude |
| --- | --- | ---: |
| Claro / desktop 1280 px | 3,85; 3,23; 3,38; 3,34; 3,92; 3,63; 3,18 | 3,18–3,92:1 |
| Escuro / desktop 1280 px | 1,45; 1,24; 1,25; 1,24; 1,46; 1,36; 1,25 | 1,24–1,46:1 |
| Claro / mobile 390 px | 3,70; 3,36; 3,37; 3,31; 3,94; 3,60; 3,32 | 3,31–3,94:1 |
| Escuro / mobile 390 px | 1,38; 1,34; 1,40; 1,26; 1,46; 1,37; 1,32 | 1,26–1,46:1 |

A distribuição dentro de cada contorno varia com a foto. Mesmo no claro, alguns pontos amostrados ficaram abaixo de 3:1. Em 390 px, os limites externos aproximados dos sete indicadores permaneceram dentro da cena e o documento ficou com 390 px de largura, sem overflow horizontal.

## Interpretação e limites

A implementação usa corretamente as cores e a geometria autorizadas para o preview. Nesta cena clara de cozinha, porém, a cor escura do contorno se aproxima muito das regiões luminosas da foto; a diferença local é baixa nos dois temas, sobretudo no escuro. Isso deixa pendente a aprovação visual final desta amostra.

O resultado vale somente para esta cena, imagem, renderização e método de amostragem. Não generaliza para as outras cenas/fotos, nem determina conformidade WCAG do Viewer. Alterar cor, acrescentar camada de contraste ou modificar a geometria exige uma proposta revisada e nova validação; nada disso foi feito nesta revisão.

## Estado

PR #242 permanece DRAFT, sem merge ou deploy de Production. A evidência complementa a revisão visual anterior e mantém aberta a avaliação de contraste sobre as demais fotos.
