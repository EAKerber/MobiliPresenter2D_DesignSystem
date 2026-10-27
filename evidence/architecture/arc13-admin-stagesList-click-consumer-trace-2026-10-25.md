# ARC-13 — rastreio do click em `stagesList`

**Data:** 25/10/2026  
**Fonte:** produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`.  
**Escopo:** três ocorrências candidatas no listener delegado de clique de `stagesList`.

## Consumers e ownership

- **`Nome da nova seção`:** título de `window.prompt` ao dividir um item em seção. O valor inicial é `itemLabel(...)`, dado dinâmico da hierarquia/catálogo. Se confirmado, o texto informado é aparado, limitado a 40 caracteres, convertido em id único e persistido como nome da seção. O valor inicial não pertence ao conjunto de chaves estáticas.
- **`Nome do novo grupo`:** título do prompt que divide uma seção em novo grupo. O valor inicial é o nome atual da seção, ou `Novo grupo` se faltar. O rótulo informado também vira dado de grupo persistido; o fallback é uma semente de conteúdo, além de texto inicial do prompt, e não deve ser migrado sem definição de locale/ownership de dados persistidos.

Cancelar ou enviar valor vazio não muda a hierarquia. Confirmar aplica a operação correspondente e renderiza a hierarquia atualizada. Os dois títulos do prompt são copy da interface Admin; valores de hierarquia permanecem dados.

## Limites

Rastreio manual do listener, sem runtime/AST, sem propostas de chave ou alterações no produto, índice, catálogo ou `decisions.json`. A classificação do default persistido `Novo grupo` requer política de localização de dados existente antes de extração.
