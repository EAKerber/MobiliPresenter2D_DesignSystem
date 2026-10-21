# Verificação pós-deploy de pares de contraste aprovados

**Data da observação:** 2026-10-20  
**Site:** [casaemmodulos.casa](https://casaemmodulos.casa/)  
**Produto:** [`EAKerber/MobiliPresenter2D@1878ae1057ce7c6190e0c8cb08a1f3baadd49463`](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463)  
**Deploy:** [Netlify `6ad6c3b51b6be05647167f94`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94), `ready`  
**Viewport DOM das medições de 2026-10-20:** 1280x720 CSS px  
**Método:** leitura somente de DOM dos estilos computados de texto e da superfície opaca efetiva, com cálculo de luminância relativa WCAG. Triagem técnica contextual, não certificação independente.

## Resultados

| Decisão / rota | Tema | Seletor | Texto / fundo computados | Contraste |
|---|---|---|---|---:|
| VIS-002 — apoio da landing, `/` | Claro | `.hero-description` | `#705C4B` / `#F0EDE8` | 5,41:1 |
| VIS-002 — apoio de Como funciona, `/how-it-works/` | Claro | `.how-hero-note` | `#705C4B` / `#F0EDE8` | 5,41:1 |
| VIS-002 — apoio de Quem somos, `/about/` | Claro | `.about-scale p:not(.eyebrow)` | `#705C4B` / `#F0EDE8` | 5,41:1 |
| VIS-002 — rótulo eyebrow de Como funciona | Claro | `.study-band .eyebrow` | `#70522F` / `#E8E3DC` | 5,60:1 |
| VIS-003 / FIND-004 — legenda da ilustração | Escuro | `.study-art figcaption` | `#F0EDE8` / faixa opaca `#20211F` | 13,85:1 |

Os quatro contextos VIS-002 correspondem aos pares de texto homologados; o escopo é apenas cada seletor listado no tema indicado. A legenda VIS-003 confirma a alternativa A homologada. Esses resultados não aprovam tokens globais, novos fundos, outras combinações, temas, breakpoints ou estados de interação.

## Revisão visual separada

A composição da legenda em `/how-it-works/`, tema escuro, foi revista novamente em uma captura da página publicada no dia **2026-10-21**. Essa captura foi uma checagem visual separada: seu viewport CSS não foi verificado e o arquivo não foi persistido naquela revisão. Uma nova captura contextual, feita em 2026-10-21 com viewport CSS 1280 × 720 verificado, foi salva em [visualEvidence](../../visualEvidence/public/how-it-works/vis003-caption-dark-2026-10-21.svg). Ela não é a origem dos valores numéricos acima, que correspondem à leitura DOM de 2026-10-20; uma checagem DOM independente da legenda escura em 2026-10-21 também retornou 13,85:1, registrada separadamente em [runtime-evidence.json](../../runtime-evidence.json).

A pasta `visualEvidence/public/how-it-works/` não recebe uma nova imagem nesta revisão; nenhum link de screenshot é publicado sem o arquivo correspondente.

## Limites e backlog

- FIND-002, FIND-003 e FIND-004 referem-se a pares corrigidos no produto; os issues [#216](https://github.com/EAKerber/MobiliPresenter2D/issues/216) e [#217](https://github.com/EAKerber/MobiliPresenter2D/issues/217) permanecem abertos nesta observação.
- O estado responsivo, foco de teclado, hover, carregamento, demais componentes e fundos com transparência/gradiente não foram testados nesta medição.
- A captura real está restrita ao caso FIND-004; não foi usada como evidência para os outros quatro contextos.
- Nenhuma alteração foi feita no produto, em dados de conta, preferência ou configuração durante a auditoria.
