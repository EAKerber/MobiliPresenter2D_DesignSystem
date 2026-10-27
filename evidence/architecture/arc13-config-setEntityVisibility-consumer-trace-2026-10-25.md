# ARC-13 — rastreio de `setEntityVisibility`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Resultado e feedback

A função altera a visibilidade solicitada e percorre dependências recursivamente:

- Ao incluir um item, liga requisitos ainda ocultos; se algum suporte mudou, anuncia `{nomes} incluído como suporte necessário.`.
- Ao retirar um requisito, desliga dependentes visíveis; se algum foi afetado, anuncia `{nomes} removido porque depende deste módulo.`.

Os nomes são resolvidos de título de módulo, título de acessório ou id como fallback; a lista é concatenada por vírgula. Sem alterações dependentes, nada é anunciado. As mensagens vão ao live region polite.

## Ponto de localização/gramática

`affected` pode conter um ou mais itens, enquanto o texto usa `nomes` em plural e `incluído` no masculino singular. A proposta futura deve receber lista e quantidade como parâmetros e definir concordância/pluralização na etapa de localização, já adiada pelo usuário. Não colapsar os nomes numa string sem contrato de idioma. A gramática atual pode soar incorreta quando há múltiplos ou nomes de gêneros diferentes; não foi corrigida nesta etapa.

## Limites

Rastreio manual do algoritmo e do anúncio, sem runtime/AT. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` permanecem inalterados.
