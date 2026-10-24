# Issue #226 — rechecagem do acordeão em Production

Data: 2026-10-24  
Rota: https://casaemmodulos.casa/how-it-works/  
Escopo: observação runtime em Chrome; somente leitura.

## Resultado

O comportamento esperado foi observado na página publicada: abrir um cartão não faz os irmãos fechados da mesma linha crescerem. A regra de alinhamento já está presente na CSS carregada para as duas grades, dentro do breakpoint de três colunas. O CSS do branch candidato conhecido e o arquivo lido em `main` tinham o mesmo blob SHA `52f36d212d286ef5157a20fc822cbfab25e09b2f`; isso confirma igualdade do arquivo, não a origem histórica da regra.

Em 1366×768, claro e escuro, ambas as grades têm três colunas e `align-items: start`. Com a página em claro, abri simultaneamente dois `.foundation-list details` e um `.study-topics details`: os dois abertos da primeira grade mediram 326,05 px e 384,48 px, enquanto o fechado permaneceu 142 px; na segunda, o aberto mediu 134,75 px e os fechados 77 px. Em uma observação anterior em escuro, abrir o último item também manteve os irmãos em 142 px e 77 px.

Em 768×900 claro, as duas grades têm uma coluna. Com dois cartões de fundação e um tópico abertos, os fechados mantiveram alturas próprias (91,66 px e 77 px), sem esticar para acompanhar itens abertos. Em 390×844 escuro, a composição também ficou em uma coluna; fechados mediram 110,31 px e 77 px. O documento não excedeu a largura do viewport nessas observações (a leitura de 390 px reportou 375 px de área de layout, com a scrollbar clássica).

A interação nativa de teclado já foi observada nesta rota: Enter abre e Espaço fecha o `summary`, mantendo o foco nele. Não foi observado uso de JavaScript para substituir `details`.

## Limites e decisão

A issue #226 permanece aberta. A rechecagem em Production confirma o comportamento nas larguras e interações observadas, mas não conclui todos os gates originais: falta uma comparação visual antes/depois confiável e ainda não houve verificação de zoom. A diferença de pixels do WebKit foi revisada no artefato mais recente e agora está delimitada abaixo, mas a captura não permite certificar paridade. Nenhum código do produto foi alterado.

## Revalidação do gate isolado — 24/10/2026

A branch candidata `fix/how-it-works-accordion-grid-20261021` avançou para `4a4ede275ee9f4af1096649d08c841643998eba3`. O workflow [#39611912828](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39611912828) concluiu com 8/8 combinações funcionais, zero erros de página, teclado e abertura independente aprovados. Chromium teve paridade de pixels nas quatro combinações; WebKit teve paridade em 1366 px nos dois temas e divergência em 390 px em claro e escuro, ambas no seletor `.study-topics`. A head atual agora contabiliza essas duas divergências como revisão pendente, sem falso PASS.

As quatro capturas WebKit do estudo em 390 px foram inspecionadas no artefato do run: as imagens `webkit-390-light-closed-main-1.png` e `webkit-390-dark-closed-main-1.png` mostram conteúdo ilustrado; as capturas candidatas `webkit-390-light-closed-candidate-1.png` e `webkit-390-dark-closed-candidate-1.png` mostram os cartões de tópicos. Apesar disso, o gate registrou DOM fechado idêntico e igualdade de estilo computado/geometria para o seletor e seus três `details`. A única regra de produto alterada é `align-items:start` dentro de `@media (min-width:901px)`, inativa a 390 px. Assim, a comparação visual gravada não representa de forma confiável o mesmo conteúdo/região; o artefato não prova regressão visual nem paridade. A causa exata da captura incongruente continua sem confirmação.

Para encerrar #226, ainda é necessário estabilizar/normalizar alvo e estado de captura, obter comparação WebKit reproduzível, salvar a comparação visual antes/depois e concluir zoom. A issue continua aberta, sem alteração ou deploy do produto.
