# ARC-13 — rastreio de `renderHandleControlsFromData`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumers

- **Ajuda global:** `handleHelp` recebe `Escolha global; o total é distribuído pelas 14 frentes aplicáveis. A basculante não entra no rateio.` É orientação comercial/de domínio da seleção global de puxador.
- **Nome acessível:** botão de seleção usa `Selecionar puxador ` + `handle.label`. O prefixo é copy de interface e o nome é dado editorial do catálogo.
- **Descrição de preço por frente:** para valor positivo, a descrição combina `handle.description`, valores formatados e os fragments `por frente; ` e `no conjunto completo.`; com preço zero, usa somente `handle.description`. Os nomes e a descrição continuam dados do catálogo; valores são calculados.
- **Distribuição:** o cálculo obtém `handleFrontTotal` de `pricingRules.allocation` (ou zero se ausente), enquanto a ajuda usa o número literal 14.

## Ponto a reconciliar antes de extrair

A ajuda fixa 14, mas o número de frentes usado no cálculo vem dos dados de pricing. O código revisado não comprova que o valor configurado será sempre 14 em todos os ambientes/planos; tampouco houve readback desses dados no runtime. A documentação de chave deve preservar orientação comercial, parâmetros de catálogo/preço e a diferença entre escopo global e rateio. Antes de propor extração ou reescrita, confirmar que o contrato canônico mantém 14 frentes e que a distribuição exclui a basculante. Não corrigir o texto especulativamente.

## Limites

Rastreio manual de fonte e fluxo do dado; sem teste runtime/AST. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` seguem inalterados.
