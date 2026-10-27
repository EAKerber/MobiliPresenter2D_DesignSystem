# ARC-13 — rastreio de `materialGroupsList` em `change`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer e regra protegida

O listener delegado atualiza destinos de materiais, disponibilidade de puxadores e material inicial. A ocorrência indexada é o erro ao desmarcar o último puxador global: o checkbox é imediatamente marcado de volta e `saveMessage` recebe “Mantenha pelo menos um puxador disponível.” com tipo `error`. A regra mantém pelo menos uma opção disponível na biblioteca de puxadores.

O feedback é distinto do erro “Mantenha pelo menos um material nesta opção.” em `setMaterialTarget`: aquele protege cada grupo de materiais e usa outro consumer/escopo. Não consolidar as duas mensagens apenas porque são guardrails parecidos.

## Limites

Rastreio estático do listener, rollback do checkbox e chamada de `setMessage`; leitura runtime/AT do erro e persistência posterior do estado não foram testadas. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
