# VIS-002 — proposta de reforço do foco dos hotspots sobre fotografia — 25/10/2026

## Estado

**Aprovada pelo usuário para teste em preview em 25/10/2026; não canônica.** A autorização cobre somente `.scene-hotspot:focus-visible` na PR de produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242), sem merge, Production, `decisions.json`, outros estados ou tokens globais.

Para tornar A concreta, o preview usa keylines neutras opacas `#FFFFFF` e `#000000`, imediatamente externas ao anel dourado. O anel autorizado continua em 4 px com offset 3 px; as duas keylines são experimentais e não mudam a referência homologada.

O preview da PR #242 implementa corretamente o foco autorizado: contorno de 4 px, offset declarado de 3 px, `#8B6A40` no tema claro e `#D8BC7C` no escuro, restrito a `.scene-hotspot:focus-visible`. A rechecagem por teclado confirmou os sete hotspots em uma cena; a distinção do anel sobre a fotografia continua insuficiente em trechos medidos.

## Evidência que motivou a proposta

A medição aproximada da foto de Cozinha encontrou medianas do anel de:

- Claro: 3,18–3,92:1 no desktop e 3,31–3,94:1 no mobile; alguns pontos ficaram abaixo de 3:1.
- Escuro: 1,24–1,46:1 no desktop e 1,26–1,46:1 no mobile.

A amostra compara pixels da imagem-base com a cor do traçado; não é captura dos pixels compostos nem auditoria WCAG completa. Ela é válida somente para a cena publicada, renderização, viewports e método descritos em [evidência da PR #242](../runtime/pr242-viewer-focus-image-contrast-sample-2026-10-25.md). Não generalizar para outras fotografias.

## Candidatos para um segundo preview

| Opção | Tratamento de foco | Vantagem | Custo visual / risco |
|---|---|---|---|
| A — anel dourado com keylines neutras | Preserva o anel dourado aprovado de 4 px/offset 3 px e acrescenta um fio escuro e outro claro imediatamente ao redor. | Mantém o acento da marca e oferece uma borda luminosa e uma escura contra a fotografia variável. | Aumenta a espessura total do indicador; pode ficar carregado ou colidir com hotspots próximos. |
| B — anel neutro duplo | Usa bordas clara e escura, mantendo a geometria externa, sem o acento dourado no foco sobre a foto. | O contraste passa a depender menos do tema e da luminância local. | Abandona a cor de foco aprovada no componente e reduz a associação visual com a marca. |
| C — suporte opaco atrás do hotspot | Preserva o anel dourado e adiciona um pequeno fundo sólido ao alvo durante o foco. | Separa indicador e fotografia sob o botão. | Altera a aparência do alvo, pode cobrir a cena e requer avaliação do estado selecionado. |

**Candidato preferido para revisão:** A, porque conserva o anel 4 px/offset 3 px e as cores aprovadas, tratando a baixa distinção como uma camada adicional limitada ao estado de foco. Isto é uma recomendação para testar, não uma aprovação de design.

## Gate de validação se A for aprovada

1. Implementar somente em `.scene-hotspot:focus-visible`, sem mudar hover, seleção, scene data, tokens ou tema global.
2. Inspecionar todos os sete hotspots nas cenas/fundos disponíveis, em claro/escuro e desktop/mobile. O único fundo de Viewer atualmente publicado é Cozinha, então registrar explicitamente que não há diversidade de cenas para generalizar.
3. Comparar captura renderizada com e sem foco. Para cada trecho do perímetro, verificar se ao menos uma das duas keylines neutras atinge 3:1 contra o pixel adjacente; não inferir isso a partir da cor do asset original.
4. Confirmar navegação por Tab sem mudar seleção, indicador dentro da cena, sem recorte/overflow e sem sobreposição que apague marcadores vizinhos.
5. Manter DRAFT até inspeção visual humana; não mergear nem publicar em Production sem autorização.

## Decisão e limite

O usuário escolheu **A — testar keylines no preview**. A implementação experimental está na branch da PR #242: outline dourado de 4 px/offset 3 px, acrescido de uma camada branca e outra preta em `box-shadow`, somente em `.scene-hotspot:focus-visible`. Os valores neutros escolhidos são `#FFFFFF` e `#000000`; a revisão renderizada precisa confirmar ordem/espessura visual e a medição de contraste na fotografia.

A seleção autoriza esse segundo preview, não torna a camada canônica e não autoriza merge ou Production. O restante do gate permanece: sete hotspots, temas claro/escuro, desktop/mobile, foco por teclado sem alterar seleção, captura renderizada, recorte/overflow e colisão com marcadores vizinhos. Existe apenas a cena Cozinha publicada; não generalizar a conclusão para outras fotografias.
