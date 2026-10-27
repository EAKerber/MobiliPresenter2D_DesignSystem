# ARC-13 — rastreio de `productForCurrentConfiguration`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Condição e consumers

A função só cria configuração derivada se existirem dimensões nominais e geométricas. Configurações administrativas positivas podem ajustar nominalmente largura, altura ou profundidade; regras de evento ativas podem alterar nominal e geometria para uma dimensão válida. Sem dimensão aplicada, retorna o produto nominal.

Quando uma ou mais dimensões são alteradas por regra:

- cada mudança é descrita como `{largura|altura|profundidade} ajustada para {valor} mm`, com medida formatada;
- as mudanças são unidas por ponto e vírgula e convertidas em nota `… pela regra de configuração.`;
- o resultado expõe valores numéricos e essa `configurationNote` aos consumers da ficha e dos cartões.

Os nomes de eixo são um enum local; o valor é dado numérico dinâmico. Os três nomes são femininos em português, concordando com `ajustada`. A nota só existe se uma regra válida realmente for aplicada; não é copy de estado vazio ou de falha.

## Limites

Rastreio manual dos ramos, sem teste runtime. Nenhuma chave foi proposta; dados de produto, config e eventos, produto, índice e `decisions.json` permanecem inalterados.
