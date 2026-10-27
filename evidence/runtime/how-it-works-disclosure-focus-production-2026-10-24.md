# Como funciona — foco nos seis disclosures nativos em Production (24/10/2026)

## Alvo e contexto

- URL: https://casaemmodulos.casa/how-it-works/
- Deploy revalidado no handover: Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, READY `6adc221479c773577ed45e23`.
- Sessão anônima, viewport 1280×720 CSS px, inspeção em aba temporária.
- Escopo: os seis elementos `summary` da seção “O que sustenta essa nova forma de fazer móveis” e da faixa “Aspectos analisados no estudo”.

## Método e resultado

Usei Enter em cada disclosure, medindo o estilo computado após foco por teclado nos temas escuro e claro. Os seis ficaram com `:focus-visible` ativo, e Enter expandiu ou recolheu o conteúdo conforme o estado inicial.

- Nos seis controles e nos dois temas: contorno sólido de 3 px com offset de 3 px.
- Tema escuro: cor `#D8BC7C`; os cartões de disclosure usam `#1B1C1A`. Contraste calculado: 9,29:1.
- Tema claro, três fundações: cor `#6E512E` sobre cartão branco `#FFFFFF`. Contraste: 7,29:1.
- Tema claro, três aspectos do estudo: cor `#6E512E`; o cartão tem `color(srgb 0.963608 0.953255 0.940078)` (estimado como RGB 246,243,240), dando 6,60:1. Mesmo usando a superfície externa mais escura da faixa, `#E8E3DC`, o contraste é 5,71:1.
- Rótulos: Evoluir a forma de produzir; Eficiência com liberdade; Transparência faz parte do produto; Plantas e dimensões; Circulação e ergonomia; Necessidades de armazenamento.

## Interpretação e limites

Esta amostra não encontrou risco de contraste de cor nos seis disclosures. A geometria de 3 px/offset 3 px difere da referência VIS-002 registrada de 4 px/offset 3 px. O registro amplia a cobertura de foco de “Como funciona”; não altera o achado separado dos seis cartões de economia sobre `#25231F`, onde a cor clara continua com 2,15:1. Não testei leitores de tela, outros navegadores, outras larguras, nem superfícies/rotas adicionais. Os contrastes são cálculos WCAG sobre os pares de cor opacos indicados. Nenhum código, deploy ou decisão canônica foi alterado.
