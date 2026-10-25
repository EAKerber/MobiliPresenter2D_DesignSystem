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


## Complemento após ampliar a inspeção de sinks — 25/10/2026

A primeira leitura detectou seis literais técnicos; a inspeção de propriedades DOM, classes, IDs, atributos ARIA, elementos e chamadas CSSOM encontrou mais treze ocorrências técnicas no mesmo inventário. Portanto, a recomendação total é excluir **19 ocorrências** da fila sem chave:

| Linha em app/admin/admin.js | Literal | Evidência |
|---:|---|---|
| 825 | `asset-preview${field === "maskAsset" ? " asset-preview--mask" : ""}` | Atribuído a `preview.className`. |

| Linha em app/app.js | Literal | Evidência |
|---:|---|---|
|---:|---|---|
| 617 | `customStage-${stage.id}` | Atribuído a `panel.id`. |
| 618, 1677 | `${panel.id}-heading` | Usado como ID de heading em `aria-labelledby` e `title.id`. |
| 749 | `--handle-swatch` | Nome de custom property CSS em `style.setProperty`. |
| 977 | `module-detail__carousel-content` | Atribuído a `className`. |
| 1144, 1145 | `front`, `side` | Valores de enum passados ao renderer; rótulos visíveis estão em campos separados. |
| 1350 | `legend` | Nome de elemento em `document.createElement`. |
| 1382, 1390 | `has-module-detail` | Nome de classe em `classList.remove/add`. |
| 1417 | `module-detail__close` | Atribuído a `className`. |
| 1462, 1648 | `dl` | Nome de elemento em `document.createElement`. |
| 1492 | `requirement-hidden` | Código interno comparado em condição. |
| 1608 | `title` | Nome de atributo em `removeAttribute`. |
| 1697 | `admin-note` | Atribuído a `className`; a mensagem visível na mesma linha permanece candidata localizável. |
| 2047 | `--mobile-pip-top` | Nome de custom property CSS em `removeProperty`. |
| 2534 | `alert` | Valor do atributo ARIA `role`. |

Os 19 registros têm correspondência única por arquivo/linha/texto no índice fixado. Com essa reclassificação proposta, os 364 itens sem chave caem para **345 candidatos locais**. O índice permanece sem alteração; o número 345 só se tornará canônico após reconciliação do próprio inventário. A lista inicial de seis casos acima permanece como evidência e é complementada por esta revisão ampliada.


## Complemento — diagnósticos internos sem saída de interface (25/10/2026)

Quatro templates restantes foram rastreados. Todos alimentam objetos de erro de layout; `applyBuyerFlowLayout()` os passa a `setFlowLayoutErrors(errors)`, que atualiza `CASA_FLOW_LAYOUT_ERRORS`, registra `console.error("Flow layout invariant failure", errors)` e os expõe por `CASA_EM_MODULOS_DEBUG.getFlowLayoutErrors`. Não encontrei sink de interface para essas mensagens. Recomendo excluí-las da fila de localização, sem alterar o índice:

| Arquivo:linha | Literal | Evidência |
|---|---|---|
| `app/app.js:214` | `missing renderer section: ${stage.id}/${section.id}` | Diagnóstico interno de layout, pelo fluxo descrito acima. |
| `app/app.js:234` | `missing group grid for ${stageId}` | Diagnóstico interno de layout, pelo fluxo descrito acima. |
| `app/app.js:360` | `missing renderer section: ${stageId}/${section.id}` | Diagnóstico interno de layout, pelo fluxo descrito acima. |
| `app/app.js:538` | `missing Modules view adapter: ${view.id}` | Diagnóstico interno de layout, pelo fluxo descrito acima. |

A fila de revisão passa de 345 para **341** textos: 208 no Admin e 133 no Configurador. Exclusão documental; índice canônico inalterado.
