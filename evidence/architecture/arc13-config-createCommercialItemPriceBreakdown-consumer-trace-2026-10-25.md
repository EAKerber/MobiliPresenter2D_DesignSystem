# ARC-13 — rastreio de `createCommercialItemPriceBreakdown`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer: decomposição do preço local na ficha do módulo, em `/config/`.

## Linhas de valor

- **Base:** linha “Módulo” mostra o valor-base formatado e nota `Valor-base do módulo.`.
- **Acabamento:** somente se `finishCents` for positivo. Exibe adicional formatado e o nome do acabamento selecionado, seguido de `adicional percentual do módulo.`. Nome é conteúdo dinâmico; a frase fixa descreve o contrato de cálculo local.
- **Puxador:** somente se `handleCents` for positivo. Exibe valor e label dinâmico do puxador, mais a distribuição calculada por frente. Quando há cotas, `Cota de N frentes:` lista cada quantia formatada; sem cotas, informa `Sem frentes aplicáveis.`.
- **Pedra de cooktop:** somente se `localCents` for positivo. Exibe a quantia com `Obrigatória neste módulo.`.

Os quatro títulos de linha e seus valores são montados separadamente pelo helper `appendPriceBreakdownRow`; os valores vêm do cálculo e não são strings estáticas. A tabela é local ao item e complementa o total sem substituir o resumo global.

## Ponto de contrato/localização

A frase `Cota de N frentes` usa contagem dinâmica com substantivo fixo no plural; pluralização permanece deferida à etapa de localização. O texto `Obrigatória neste módulo.` é uma regra de produto, condicionada a `localCents`; confirmar sua validade para cada módulo que pode produzir esse valor antes de migrar ou reescrever.

## Limites

Leitura manual de fonte/helper, sem runtime/AST nem verificação dos pricing rows publicados. Texto corrido deve manter o contraste próximo de preto no claro ou branco no escuro conforme preferência do usuário; nenhuma medição visual foi feita. Não houve proposta de chave ou alteração de produto, índice, catálogo ou `decisions.json`.
