# ARC-13 — rastreio de `setStonePackage`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; `app/data/catalog-data.js` blob `b457ec513a7e838e52bbf69b7d7ae10b55d7948e`. O app blob coincide com o mapa ARC-13. Rota `/config/`.

## Consumer

Se o pacote existe no catálogo, a função aplica a seleção global, sincroniza a cena e anuncia `{stone.label} aplicado ao conjunto.` no live region polite. Um id desconhecido não produz alteração ou anúncio. `stone.label` é dado editorial configurável, não texto fixo da interface.

## Achado de gramática que pede correção

Os rótulos canônicos atuais incluem `Clara mineral` e `Preta mineral`; a mensagem resultante usa concordância masculina fixa (“Clara mineral aplicado”, “Preta mineral aplicado”). O suffixo `aplicado ao conjunto.` também aparece no anúncio do puxador, mas não deve ser compartilhado sem considerar o substantivo implícito: puxador é masculino; pedra/acabamento é feminino. Labels futuros podem variar mais.

A correção precisa tornar a gramática independente do nome editorial, por exemplo, formular a mensagem com sujeito fixo (“Acabamento de pedra selecionado para o conjunto”) ou passar uma forma/contrato explícito do catálogo. Confirmar com owner de produto/catálogo antes de alterar a copy; não corrigida nesta etapa.

## Limites

Rastreio manual da função e dos cinco rótulos atuais do catálogo, sem runtime/AT. Nenhuma chave foi proposta; código, catálogo, índice e `decisions.json` permanecem inalterados.
