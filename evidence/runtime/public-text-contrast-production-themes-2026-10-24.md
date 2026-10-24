# Contraste de texto público — Production, dois temas (24/10/2026)

**Alvo:** `EAKerber/MobiliPresenter2D@main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`. Rotas públicas, viewport CSS 1280×720, tema alternado pelo controle da página entre claro e escuro. Leitura somente do DOM/CSSOM; contraste calculado por luminância relativa sobre a superfície opaca computada mais próxima.

| Rota e elemento | Tema | Texto / superfície | Tamanho | Razão |
|---|---|---|---:|---:|
| Landing `.hero-description` | Claro | `#705C4B` / `#F0EDE8` | 16 px | 5,41:1 |
| Landing `.hero-description` | Escuro | `#C4BCB2` / `#20211F` | 16 px | 8,61:1 |
| Como funciona `.how-hero-note` | Claro | `#705C4B` / `#F0EDE8` | 16 px | 5,41:1 |
| Como funciona `.how-hero-note` | Escuro | `#C4BCB2` / `#20211F` | 16 px | 8,61:1 |
| Como funciona `.study-band .eyebrow` | Claro | `#70522F` / `#E8E3DC` | 11,52 px | 5,60:1 |
| Como funciona `.study-band .eyebrow` | Escuro | `#D8BC7C` / `#20211F` | 11,52 px | 8,78:1 |
| Como funciona, legenda `.study-art figcaption` | Claro | `#706C66` / `#FCF9EF` | 10,88 px | 4,95:1 |
| Como funciona, legenda `.study-art figcaption` | Escuro | `#F0EDE8` / `#20211F` | 10,88 px | 13,85:1 |
| Como funciona `.launch-badge` | Ambos | branco / `#A64D13` | 16 px | 5,69:1 |
| About, lead e primeiros parágrafos de `main` | Claro | `#706C66` / `#F7F5F2` | 16–20 px | 4,79:1 |
| About, parágrafos da seção de escala | Claro | `#705C4B` / `#F0EDE8` | 16 px | 5,41:1 |
| About, lead e primeiros parágrafos de `main` | Escuro | `#C4BCB2` / `#111210` | 16–20 px | 10,00:1 |
| About, parágrafos da seção de escala | Escuro | `#C4BCB2` / `#20211F` | 16 px | 8,61:1 |

No recorte de About, também foram lidos rótulos de seção: claro `#70512E` sobre `#F7F5F2` a 6,70:1 e `#F0EDE8` a 6,25:1; escuro `#E2C991` sobre `#111210` a 11,63:1 e `#20211F` a 10,01:1.

## Interpretação e limites

Os pares acima passaram o limiar técnico de 4,5:1 para texto comum nos elementos, temas e superfícies lidas. Eles diferem de algumas medições e valores registrados em auditorias históricas; para estes alvos, o DOM atual é a leitura válida do deploy atual. A faixa opaca da legenda de `.study-art` no tema escuro corresponde à composição aprovada em VIS-003; mediu 13,85:1 nesta leitura.

A amostra não fecha issue #216 nem certifica conformidade global. Não cobre todos os textos, rotas, viewports, estados de foco/seleção, imagens sem fundo opaco, gradientes, pseudoelementos, contraste não textual ou leitores de tela. Em About, foram lidos o lead, os primeiros parágrafos, a seção de escala e rótulos de seção, não o texto inteiro. Uma visita por rota; sem alteração de produto, decisão de token ou deploy.
