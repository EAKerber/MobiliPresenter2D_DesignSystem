# ARC-13 — rastreio de `createModuleNavigationButton`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer: navegação entre fichas em `/config/`.

## Consumer, estado e parâmetros

- `direction < 0` produz o estado “anterior”; caso contrário, “próximo”.
- O nome acessível combina `Abrir módulo`, a direção e `targetProduct.title`.
- O tooltip combina `Módulo`, a direção e `targetProduct.referenceLabel`.
- A seta visível é `‹` ou `›` de acordo com a direção; não substitui o nome acessível.

O caller só cria botões se houver produto adjacente. A lista segue a ordem dos módulos configurados no catálogo e a navegação circula no início/fim; ao ativar, seleciona a ficha adjacente. Se o próximo item estiver invisível, uma atenção visual temporária é marcada antes da seleção. Título e referência são parâmetros de catálogo; anterior/próximo são estados de copy.

## Limites

Rastreio manual do renderer e do caminho de ativação, sem runtime/AT. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` seguem inalterados.
