# ARC-13 — rastreio de `dimensionSummary`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumer

A função retorna `Medidas nominais: {product.dimensions.display}{axes}`. O display contém medidas formatadas; `axes` é opcional e, se `product.dimensions.displayAxes` existir, recebe o fragmento ` ({product.dimensions.displayAxes})`. A sequência de eixos é dado do produto, distinto dos valores dimensionais.

O mapa de escopo registra somente o sufixo de eixos na linha 1064; não lista a parte estática `Medidas nominais: ` da linha seguinte. Essa frase também existe como heading separado em `updateSelection`. A fonte do índice ARC-13 foi localizada pelo SHA canônico `1954dfd9a4fe6194812b4fd336281eed39f64ecf`, mas a ferramenta de leitura devolveu corpo vazio, então não consegui confirmar se o prefixo desta template já tem registro/chave ou se faltou no mapa.

## Pendência de cobertura

Antes de tratar este bucket como integralmente auditado, reler a linha/template no índice fonte acessível e reconciliar o prefixo. O código prova o consumer; a relação dessa ocorrência com o índice continua **UNKNOWN**. Não contar nem compartilhar chaves por inferência.

## Limites

Rastreio manual de fonte; sem runtime. Nenhuma chave foi proposta e nenhum produto, índice ou `decisions.json` foi alterado.
