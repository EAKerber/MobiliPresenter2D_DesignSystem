# ARC-13 — classificação por destino sintático dos textos sem chave

**Data:** 25/10/2026  
**Produto fixado:** `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
**Índice fixado:** `evidence/architecture/arc13-runtime-js-candidates-main-2026-10-24.json`, blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`.

## Contagem após revisão dos falsos positivos técnicos

O índice contém 364 referências sem chave e consumer “unclassified” em `app/admin/admin.js` e `app/app.js`. A inspeção das linhas de origem confirmou 19 valores técnicos (classes/IDs CSS/DOM, tags HTML, enum, nome de atributo e role ARIA) que não devem receber chaves de localização. Permaneciam **345 candidatos de texto**: 208 de Admin e 137 do Configurador. A reconciliação removeu quatro diagnósticos sem saída de interface; a fila atual tem **341 candidatos**: 208 no Admin e 133 no Configurador. O índice ainda não foi editado.

## Destino sintático na linha de origem

| Pista no código fonte | Ocorrências |
|---|---:|
| Texto atribuído diretamente a textContent, innerText ou createTextNode | 106 |
| aria-label, descrição ARIA ou alt | 33 |
| Atributo title usado como tooltip | 14 |
| Valores de mapas/arrays ou dados de composição | 66 |
| HTML/template de markup | 3 |
| Outras expressões/constantes sem sink explícito na mesma linha | 123 |
| **Total na revisão inicial** | **345** |

Essas classes descrevem apenas o padrão sintático da linha. Os 66 valores em mapas/arrays e os 123 em outras expressões ainda precisam ser ligados ao renderer/consumer real. As pistas não substituem ownership, não autorizam compartilhar chaves e não constituem cobertura de chamadas DOM construídas indiretamente.

## Repetições

Após excluir as 19 referências técnicas, há 21 grupos de texto repetido. A revisão deve decidir separadamente se cada grupo tem o mesmo consumer e contrato de parâmetros; igualdade textual não é suficiente para compartilhar uma chave.

Nenhuma sugestão de chave foi criada para estes 345 itens nesta auditoria. O índice, runtime e decisions.json permanecem inalterados.


## Releitura do escopo de consumo — 25/10/2026

O mapa anterior foi descartado: a heurística podia manter o escopo anterior ao atravessar listeners. O mapa corrigido associa as **341** ocorrências a escopos lexicais reconhecíveis, sem afirmar que isso prova o consumer. Há **75 buckets lexicais**. Owners, consumers e contratos ainda precisam de revisão.

Na distribuição sintática inicial de 345 itens, quatro diagnósticos sem saída direta foram removidos da classe sem sink:

| Pista sintática | Ocorrências atuais |
|---|---:|
| Escrita textual direta | 106 |
| ARIA/alt | 33 |
| Tooltip `title` | 14 |
| Mapas/arrays | 66 |
| Markup | 3 |
| Outras expressões após remoção dos diagnósticos | 119 |
| **Total** | **341** |

Há 21 grupos de texto repetido; igualdade textual não basta para compartilhar chave. Índice, runtime e `decisions.json` permanecem inalterados.


## Correção adicional — identificadores dinâmicos (25/10/2026)

A revisão dos formatos semelhantes a identificadores encontrou três falsos positivos adicionais: um slug que vira `stage.id`, o ID do carrossel referenciado por `aria-controls` e o ID de status referenciado por `aria-describedby`. A fila atual passa de 341 para **338** (207 Admin, 131 Configurador). A reclassificação é somente documental e está registrada no [mapa corrigido](arc13-unkeyed-consumer-scope-map-2026-10-25.json); a busca dirigida não atesta cobertura completa.

Após excluir os três itens da categoria “outras expressões”, a distribuição heurística fica: 106 escrita textual direta, 33 ARIA/alt, 14 tooltips, 66 mapas/arrays, 3 markup e **116 outras expressões** — total 338. As categorias continuam sendo pistas de sintaxe, não consumidores comprovados.


## ARC-13 — primeiro lote com consumer confirmado (25/10/2026)

Rastreei `createDetailCarousel` no Configurador: o lote reúne **26 ocorrências** de títulos/rótulos curtos/descrições, nomes acessíveis, tooltips e ações de recolher. A proposta contém 16 chaves novas e quatro reutilizações intencionais de chaves já atribuídas ao mesmo carrossel; usa parâmetros `pageLabel`, `shortLabel`, `pageNumber` e `pageCount`. Anterior/próximo continuam mensagens distintas. A auditoria encontrou zero colisões com significado diferente e zero conflito de texto entre chaves. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-configurator-carousel-2026-10-25.json). O índice e o produto não mudaram; os itens continuam sem chave canônica até reconciliação.


## Reclassificação de valor de enum — 25/10/2026

O literal `Estrutural` em `app/app.js:1435` é comparado com `product.category` para escolher uma das duas descrições. Não é exibido por essa linha. Com essa exclusão, a fila de revisão cai de 338 para **337** (207 Admin, 130 Configurador); a categoria sem sink direto cai de 116 para **115**. Trata-se de reclassificação documental, ainda não aplicada ao índice.


## ARC-13 — ajuste após revisão do consumer do Viewer (25/10/2026)

O literal `Estrutural` em `updateSelection` é um valor comparado para escolher uma descrição, não um rótulo renderizado. A fila documental atual fica em **337 textos** (207 Admin, 130 Configurador), com 23 valores técnicos e quatro diagnósticos internos separados. [Reclassificação](../evidence/architecture/arc13-unkeyed-code-literal-reclassification-2026-10-25.md). O índice permanece em 369 textos sem chave no total; os lotes contextualizados continuam propostas até reconciliação canônica.


## ARC-13 — segundo lote com consumer confirmado (25/10/2026)

O consumer `updateSelection` foi revisado até os sinks DOM. Dos 13 registros do bucket, **12** têm proposta de chave em `configurator.moduleDetail`, sem colisão; `product.title` é parâmetro nomeado. O décimo terceiro item, ` · ${product.configurationNote}`, ficou deferido porque combina pontuação de composição com conteúdo vindo do catálogo; a ownership/mensagem final precisa ser confirmada antes de localizar. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-module-detail-2026-10-25.json). Nenhum índice ou runtime alterado.


## ARC-13 — lote Admin de materiais com consumer confirmado (25/10/2026)

`renderMaterials` foi rastreada até os labels, opções, alt da prévia, disclosure de destinos e ação de remoção. O lote tem **10 ocorrências**, dez chaves candidatas no namespace `admin.materials` e zero colisões. O nome do material no alt é parâmetro; o espaço inicial do texto da checkbox precisa ser preservado ou normalizado deliberadamente na extração. [Proposta não canônica](../evidence/architecture/arc13-semantic-key-proposal-admin-materials-2026-10-25.json). Sem mudança do índice ou do produto.
