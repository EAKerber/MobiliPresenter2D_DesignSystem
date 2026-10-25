# ARC-13 — revisão de literais técnicos na fila sem chave

**Data:** 25/10/2026  
**Produto observado:** `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
**Índice:** `evidence/architecture/arc13-runtime-js-candidates-main-2026-10-24.json`, blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`.

## Resultado

Seis ocorrências classificadas pelo scanner como interface localizável são valores de implementação, não texto apresentado ao usuário. A recomendação é classificá-las como não localizáveis antes de criar qualquer chave:

| Linhas | Literal | Evidência no código | Reclassificação proposta |
|---|---|---|---|
| 1382, 1390 | `has-module-detail` | Argumento de `document.body.classList.remove/add` em `updateSelection`. | Classe CSS |
| 1462, 1648 | `dl` | Argumento de `document.createElement` para elementos de lista de descrição. | Nome de elemento HTML |
| 1492 | `requirement-hidden` | Comparação de `reason` em condição de controle, sem exibição textual. | Código de estado interno |
| 1697 | `admin-note` | Valor atribuído a `note.className`. | Classe CSS |

Na linha 1697, a mensagem visível “Inclua itens na administração para preencher esta etapa.” também está presente como ocorrência separada no índice; ela continua localizável.

## Limite

Esta é uma recomendação de classificação sustentada pela origem fixada, não uma alteração do índice. Não gerei chaves para esses valores e não modifiquei o produto, o índice nem `decisions.json`. A fila sem chave cai de 364 para 358 candidatos a texto depois que essas exclusões forem incorporadas ao índice; a limpeza no índice permanece pendente.
