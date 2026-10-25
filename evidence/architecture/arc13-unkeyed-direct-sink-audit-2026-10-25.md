# ARC-13 — classificação por destino sintático dos textos sem chave

**Data:** 25/10/2026  
**Produto fixado:** `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
**Índice fixado:** `evidence/architecture/arc13-runtime-js-candidates-main-2026-10-24.json`, blob `1954dfd9a4fe6194812b4fd336281eed39f64ecf`.

## Contagem após revisão dos falsos positivos técnicos

O índice contém 364 referências sem chave e consumer “unclassified” em `app/admin/admin.js` e `app/app.js`. A inspeção das linhas de origem confirmou 19 valores técnicos (classes/IDs CSS/DOM, tags HTML, enum, nome de atributo e role ARIA) que não devem receber chaves de localização. Permanecem **345 candidatos de texto**: 208 de Admin e 137 do Configurador. O índice ainda não foi editado.

## Destino sintático na linha de origem

| Pista no código fonte | Ocorrências |
|---|---:|
| Texto atribuído diretamente a textContent, innerText ou createTextNode | 106 |
| aria-label, descrição ARIA ou alt | 33 |
| Atributo title usado como tooltip | 14 |
| Valores de mapas/arrays ou dados de composição | 66 |
| HTML/template de markup | 3 |
| Outras expressões/constantes sem sink explícito na mesma linha | 123 |
| **Total** | **345** |

Essas classes descrevem apenas o padrão sintático da linha. Os 66 valores em mapas/arrays e os 123 em outras expressões ainda precisam ser ligados ao renderer/consumer real. As pistas não substituem ownership, não autorizam compartilhar chaves e não constituem cobertura de chamadas DOM construídas indiretamente.

## Repetições

Após excluir as 19 referências técnicas, há 21 grupos de texto repetido. A revisão deve decidir separadamente se cada grupo tem o mesmo consumer e contrato de parâmetros; igualdade textual não é suficiente para compartilhar uma chave.

Nenhuma sugestão de chave foi criada para estes 345 itens nesta auditoria. O índice, runtime e decisions.json permanecem inalterados.
