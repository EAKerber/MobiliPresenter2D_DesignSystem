# ARC-13 — rastreio do change em `pricingList`

**Data:** 25/10/2026  
**Fonte:** produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`.  
**Escopo:** três ocorrências candidatas do listener de mudança da lista de preços.

## Consumers e guardrails

- **Preço base no Viewer ativado:** somente com a fonte publicada no schema suportado a alteração muda `model.viewerPricePublication`. A mensagem esclarece que é rascunho e exige ação explícita de publicar para autorizar valores públicos. Sem schema compatível, o toggle volta para desligado e nenhuma mensagem de sucesso é apresentada.
- **Preço base desativado:** mesmo guardrail; a mensagem esclarece que a alteração ainda é rascunho e que a publicação explícita retira valores da API pública. A mensagem não indica publicação imediata.
- **Tipo de regra de preço alterado:** somente tipos suportados e regras existentes prosseguem. A conversão zera o valor (centavos ou basis points) para evitar conversão implícita entre dinheiro e percentual, mostra confirmação de sucesso e re-renderiza pricing.

Os dois estados do toggle são feedback persistente do Admin e carregam o limite de publicação; o terceiro texto confirma a política de reset, não a quantidade resultante. Nenhum dado de preço é interpolado nesses textos.

## Limites

Rastreio manual do listener em `main`, sem teste de runtime/AST. As três ocorrências são candidatos de interface; nenhuma chave foi proposta e nenhum produto, índice, catálogo ou `decisions.json` foi alterado.
