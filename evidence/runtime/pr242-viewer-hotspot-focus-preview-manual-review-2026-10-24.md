# PR #242 — revisão manual pontual do foco dos hotspots

Data: 2026-10-24  
Preview: https://deploy-preview-242--mobilipresenter2d.netlify.app/viewer/  
Head: `af2166df42019b273c27d672149ebe49b143c0fb`  
Escopo: leitura visual/runtime; nenhum arquivo do produto foi alterado.

## Observações

Em viewport mobile 390×844 no tema claro, percorri por Tab até o hotspot 06. O foco foi reconhecido por `:focus-visible`, com contorno computado de 4 px, offset de 3 px e cor `#8B6A40`. O hotspot 01 permaneceu selecionado; o foco em 06 não alterou a seleção. A captura observada mostrou o contorno claramente na cena. O documento não excedeu a largura de layout (390 px de viewport, 375 px reportados para `scrollWidth` devido à scrollbar clássica).

No tema escuro, o CSSOM computou 4 px, offset de 3 px e `#D8BC7C` em um hotspot que correspondia a `:focus-visible`; o hotspot selecionado continuou sendo o 01. Em 1280×800 escuro, o mesmo estilo foi computado e sua caixa projetada (alvo + contorno/offset) permaneceu dentro dos limites da cena. A checagem escura foi pontual por CSSOM; a validação automatizada do PR registra a navegação pelos sete alvos nos dois temas em mobile/desktop.

## Limites e estado

A captura mobile clara foi inspecionada na sessão, mas não foi persistida como arquivo. A revisão não avalia conformidade de contraste contra todas as fotografias nem conclui aceitação estética do usuário. PR produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242) continua DRAFT e sem merge/deploy de Production; esta evidência não altera `decisions.json`.
