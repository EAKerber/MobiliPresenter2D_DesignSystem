# ARC-13 — rastreio de `stagesList` em `change`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer e validação

O listener delegado trata toggles de etapas, geometria de grupos/seções, destinos de itens e estado inicial. A ocorrência mapeada é o ramo `data-module-dimension`: converte o valor para número e rejeita valor não finito, mais de uma casa decimal, menor que 1 ou maior que 5.000. Ao rejeitar, restaura o valor do modelo (ou campo vazio) e apresenta “Informe uma medida nominal entre 1 e 5.000 mm, com até uma casa decimal.” como erro. A medida aceita continua em milímetros e atualiza o eixo correspondente.

A mensagem é feedback de validação para campo de dimensão nominal; os limites, a unidade e a precisão fazem parte do contrato do campo e devem permanecer coerentes caso o texto seja extraído.

## Limites

Rastreio estático do handler; não houve edição runtime dos limites, leitura assistiva nem teste de salvamento para cada eixo. Nenhuma chave foi proposta; produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
