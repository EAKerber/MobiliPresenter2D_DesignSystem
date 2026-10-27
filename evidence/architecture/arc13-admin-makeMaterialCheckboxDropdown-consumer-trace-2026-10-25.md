# ARC-13 — rastreio de `makeMaterialCheckboxDropdown`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O helper cria um disclosure de seleção múltipla para materiais/destinos. O texto de `summary` combina o label recebido do grupo com a quantidade de ids selecionados, no formato atual “{label} · {count} selecionado(s)”. Ao expandir, cada opção mostra checkbox, amostra visual e nome do material do catálogo.

A string candidata é o resumo visível do estado do disclosure. Label e contagem são parâmetros; o plural deve seguir a decisão ARC-13 de ser resolvido na etapa de localização, sem tornar “selecionado(s)” uma forma final de chave.

## Limites

Rastreio estático do helper; sem interação runtime, anúncio por leitor de tela, nem validação de atualização do summary após mudar checkboxes. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
