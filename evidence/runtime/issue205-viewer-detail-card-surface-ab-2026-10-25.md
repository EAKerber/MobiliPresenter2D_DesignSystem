# Issue #205 — comparação temporária de superfícies dos cartões do Viewer

**Data:** 25/10/2026  
**Rota conferida:** `https://casaemmodulos.casa/viewer/`  
**Estado observado:** Production, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
**Issue:** [#205](https://github.com/EAKerber/MobiliPresenter2D/issues/205), backlog, sem implementação aprovada.  
**Escopo desta leitura:** comparação visual transitória em contexto isolado; nenhum CSS, decisão canônica ou estado de Production foi alterado.

## Método

Em 1280 × 900 px, no tema claro, comparei lado a lado cópias dos três cartões reais de componentes da seção **Detalhes do módulo**. A sobreposição temporária identificou explicitamente as opções A (valor atual) e B (candidata); os dados, textos, ícones e dimensões foram mantidos iguais. A cópia B recebeu somente `background-color: #F0EDE8`. O restante da página continuou visível para avaliar a superfície em contexto.

A comparação foi feita no DOM da rota de Production dentro de um contexto isolado, com rótulo “Comparação temporária — não canônica”. Portanto, é uma simulação de superfície para avaliação; não é um Deploy Preview de alteração de produto nem uma homologação.

## Observações

- **A — atual:** cada `.detail-row` computa fundo `#FFFFFF`, texto `#514A43`; a superfície ao redor do documento é `#F7F5F2`. O cartão se destaca mais que as superfícies quentes ao redor.
- **B — candidata:** fundo `#F0EDE8`, preservando o texto `#514A43`, ícones, bordas, conteúdo e geometria. Visualmente, os cartões se integram mais ao contexto claro e deixam de ser branco puro.
- A razão de contraste de `#514A43` foi calculada como **8,71:1** sobre branco e **7,46:1** sobre `#F0EDE8`. Ambos superam 4,5:1 para texto normal. A mudança reduz contraste, mas mantém margem ampla.
- O screenshot da comparação mostrou a opção B como uma diferença sutil, coerente com a hierarquia da página; a distinção entre os três cartões permaneceu visível por bordas e espaçamento.
- No tema escuro, o cartão publicado já computa `#20211F` com texto `#F4F1EB` (contraste previamente medido em **14,34:1**); a issue original não se reproduziu nessa superfície.
- Em 390, 768 e 1366 px, a estrutura observada não apresentou overflow horizontal. Em 320 px, a página já apresenta `clientWidth=305` e `scrollWidth=320` (15 px), enquanto as linhas de detalhe permanecem dentro do bloco. Esse overflow é uma lacuna pré-existente que precisa ser separada da mudança de superfície na validação final.
- Ícones de componente continuam sendo `assets/icon-placeholder.svg`, com atributo `alt` vazio. A comparação não alterou nem homologou o conteúdo desses ícones.

## Resultado e limites

A opção B é uma candidata razoável para a direção da issue: aproxima os cartões da paleta clara sem branco puro e preserva contraste textual forte. Esta observação não aprova a implementação, não estabelece token global e não resolve todos os critérios da issue.

Ainda faltam autorização e validação de implementação, temas claro/escuro/auto, estados de foco por teclado, zoom real e matriz completa de 320/390/768/1366 px. A causa do overflow horizontal de 320 px também deve ser atribuída antes de usar esse tamanho como evidência de ausência de regressão.

**Estado:** #205 continua aberta em backlog. Nenhuma alteração de produto, decisão canônica, merge ou deploy foi feita.