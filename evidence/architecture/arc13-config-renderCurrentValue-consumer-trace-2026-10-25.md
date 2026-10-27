# ARC-13 — rastreio de `renderCurrentValue`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`, região `#configurationValue[aria-live="polite"]`.

## Estados e consumers

- **Estimativa pronta:** markup combina `estimate.label` dinâmico, total formatado e o sufixo estático `Estimativa`. O tooltip recebe `estimate.disclaimer`; a região é anunciada como mudança de valor.
- **Estimativa indisponível/incompleta:** exibe `Valor do conjunto` e `Em configuração`, e remove o tooltip de disclaimer. Não publica um total parcial nesta superfície.

Os dois candidatos do mapa são fragments dentro de HTML misturado com dados de pricing, não payloads de chave únicos. O resumo usa o mesmo status para mostrar mais detalhes; conservar a distinção entre estimativa vigente e estado incompleto.

## Limites

O rastreio não seguiu a origem nem a sanitização de `estimate.label` e `estimate.disclaimer`; antes de uma futura extração, confirmar que esses campos são controlados pelo contrato de pricing. Também não houve teste com leitor de tela. Nenhuma chave foi proposta; código, pricing, índice e `decisions.json` permanecem inalterados.
