# ARC-13 — rastreio de fallbacks em `applyMaterialLibrary`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; `app/data/catalog-data.js` blob `b457ec513a7e838e52bbf69b7d7ae10b55d7948e`. O app blob coincide com o mapa ARC-13.

## Ownership e caminho de consumo

`Definir depois` e `Sem adicional na simulação.` são fallback em memória para a opção de ausência do puxador quando o catálogo anterior não tem id `none`. O catálogo atual já possui essa mesma opção e as mesmas frases, marcadas como ausência; portanto, a condição de fallback não é o owner canônico do conteúdo.

O fallback preserva `isAbsence`, lista de materiais válidos vazia e ausência de adicional. Se usado, o label e a descrição passam ao renderer das opções de puxador e podem aparecer na interface. São conteúdo/editorial de catálogo e permanecem no catálogo conforme a decisão de ownership existente; não extrair essas duas ocorrências para chave sem revisão do owner. Dados de materiais/acabamentos são transformados a partir da biblioteca em outras linhas do mesmo helper.

## Limites

Leitura manual de fallback e catálogo de `main`, sem runtime do caminho de catálogo ausente. Nenhuma chave foi proposta; catálogo, índice e `decisions.json` não foram alterados.
