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

A issue #226 permanece aberta. Esta rechecagem confirma o comportamento em Production, mas não cumpre todos os gates originais: não foi persistida uma comparação visual antes/depois, não houve teste de zoom, e continua pendente inspecionar a diferença de pixels em uma captura WebKit registrada no run de 21/10. As medições acima são observações do browser nesta sessão; não encerram o achado nem autorizam mudança de produto. Nenhum código foi alterado.
