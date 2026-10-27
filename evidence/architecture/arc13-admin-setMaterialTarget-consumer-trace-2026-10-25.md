# ARC-13 — rastreio de `setMaterialTarget`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer e regra protegida

O helper trata a alteração de destino de um material. Para destinos de puxador, atualiza a lista de materiais do produto. Para um grupo normal, valida material e grupo antes de alterar a associação. A única string candidata aparece ao tentar remover o último material de um grupo: a operação é bloqueada e `saveMessage` recebe “Mantenha pelo menos um material nesta opção.” com tipo `error`.

A frase é feedback de validação do guardrail, não sucesso de gravação. A regra protege a existência de ao menos um material por opção; não é aplicada ao ramo de puxadores, que usa outra estrutura. Após alteração permitida, o helper também sincroniza ids de grupo, opções de acabamento/pricing e materiais iniciais.

## Limites

Rastreio estático do guardrail e de `setMessage`, que grava texto e tipo no elemento; região ARIA e anúncio runtime não foram confirmados. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
