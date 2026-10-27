# ARC-13 — rastreio do bucket Configurator createDetailCarousel — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/app.js`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`.

Este registro rastreia as 18 ocorrências do bucket exato `function startConfigurator > function createDetailCarousel`. Chamadas e consumers foram lidos até `createCarouselPage`, o DOM final, dots e navegação. Strings de funções filhas (`updateNavigationLabels`, clique do botão de recolher) pertencem a outros buckets e são apenas relacionadas aqui. Nenhuma chave foi proposta ou gravada; sem alteração de produto ou do índice.

## As 18 ocorrências diretas

| Linha(s) | Texto | Uso e consumer | Contrato / owner |
|---|---|---|---|
| 1143 | Foco | `shortLabel`; vira `title` do dot e rótulo curto dos controles anterior/próximo. | Rótulo compacto da interface; manter curto para tooltip. |
| 1143 (2 ocorrências) | Foco no módulo | `pages[].label` e título passado a `createCarouselPage`; vai ao heading da página e às labels acessíveis da navegação. | Uma copy longa reutilizada em heading/aria; candidatos a chave compartilhada se owner e contrato forem iguais. |
| 1143 | Visual isolado da peça selecionada na cena. | Descrição estática passada como `note`, renderizada em `p.module-detail__carousel-note`. | Copy explicativa da vista; confirmar owner editorial/técnico antes de propor chave. |
| 1144 | Frontal | `shortLabel`; tooltip curto. | Rótulo compacto, sem abreviar além da forma atual. |
| 1144 (2 ocorrências) | Vista frontal | `pages[].label` e heading da página. | Copy longa reutilizada entre navegação e heading. |
| 1145 | Lateral | `shortLabel`; tooltip curto. | Rótulo compacto. |
| 1145 (2 ocorrências) | Vista lateral | `pages[].label` e heading da página. | Copy longa reutilizada entre navegação e heading. |
| 1147 | Interna | `shortLabel`; só existe quando `product.technicalLayout.internalFront` está disponível. | Rótulo compacto condicionado à existência real da vista. |
| 1147 (2 ocorrências) | Vista interna | `pages[].label` e heading; mesmo gate condicional da vista interna. | Copy longa com disponibilidade derivada do dado, não criar texto que prometa a vista sem dados. |
| 1147 | Vãos internos confirmados; não equivalem ao envelope externo do módulo. | Nota exibida somente no estado interno confirmado. | Aviso técnico: preservar a distinção entre vãos internos e envelope externo; owner técnico precisa revisar qualquer localização. |
| 1149 | Isométrica | `shortLabel`; tooltip curto. | Rótulo compacto. |
| 1149 (2 ocorrências) | Projeção isométrica | `pages[].label` e heading da página. | Copy longa reutilizada. |
| 1149 | Painel estrutural em proporção; espessura ampliada somente para leitura. | Nota escolhida quando `product.drawingSpec.kind === "panel"`. | Conteúdo técnico condicionado ao tipo de desenho; não tratar como frase global de toda vista isométrica. |
| 1149 | Projeção isométrica orientativa das cotas nominais. | Nota do outro ramo para desenho não classificado como painel. | Copy técnica orientativa; preservar que cotas são nominais. |
| 1210 | Mostrar ${page.label}, página ${index + 1} de ${pages.length} | `aria-label` de cada dot. | Parâmetros page label/índice/total devem continuar dinâmicos. Pluralização e contrato de localização foram adiados pelo usuário para a etapa de localização. |

Os nomes longos e curtos são dois contratos diferentes; a semelhança de significado não os torna intercambiáveis. Os dois usos de cada rótulo longo têm sink de conteúdo/heading e label da página. A indexação de páginas é outro consumer, com parâmetros próprios.

## Consumers relacionados, em buckets filhos

A mesma função fecha/abre o conteúdo com quatro literals em evento e atualiza os controles de navegação com quatro templates em `updateNavigationLabels`:

- Navegação anterior/próxima: `Mostrar ${previousPage.label}`, `Anterior: ${previousPage.shortLabel}`, `Mostrar ${nextPage.label}`, `Próxima: ${nextPage.shortLabel}`. Os labels ARIA e tooltips usam nome longo/curto distintos e recebem valores da lista de páginas.
- Recolher/expandir: `Expandir visualizações`, `Recolher visualizações`, `Mostrar`, `Recolher`. O par ARIA e o texto visível são controlados pelo mesmo estado `aria-expanded`; manter estado e verbo sincronizados.

Essas oito ocorrências continuam em seus buckets próprios; não foram somadas às 18 directas.

As notas das vistas frontal e lateral vêm de `frontViewNote(product)` e `sideViewNote(product)`, não de literais deste bucket. Em especial, a primeira pode interpolar larguras e segmentos derivados de `product.frontLayout`; tratar medidas como parâmetros/valores de dados e revisar o contrato em seu bucket de origem.

## Resultado e próximo passo

O bucket tem textos de UI, labels compactas e descrições de precisão técnica. A existência de uma página pode depender de dados de produto, e as notas frontal/lateral podem depender de medições do produto. Não converter essas diferenças em uma única chave ou owner. Não propor chaves nesta etapa.

Próximo lote do roadmap: revisar o bucket `renderEvents` (13) ou a função de renderização de materiais (12) com o mesmo rastreio de sinks; manter pluralização para a etapa de localização. Nenhuma migração foi feita.
