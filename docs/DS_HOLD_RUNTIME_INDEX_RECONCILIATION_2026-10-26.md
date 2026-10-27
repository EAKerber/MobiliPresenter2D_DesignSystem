# HISTÓRICO — Reconciliação do índice runtime de #41 (26/10/2026)

Confronto do `runtime-evidence.json` de `main@c200aa83bd2fbf7f97696fe7f6693dd381162122` (Git Blob `9679bec7426329f5706409fdd014469f917c0b3b`) com o de `audit/access-confirmation-runtime-20261020@ae58f2199e9b3be5ba4ea313c86e7d26dd60ff37` (Git Blob `3989f7bd0fadb35abd6ea38f63f5579636863905`).

A única chave de objeto presente na versão #41 e **sem a mesma chave no índice main** é `authFlowReview.menu.currentCrossPageObservation`, cujo valor é `evidence/runtime/private-menu-cross-tab-state-2026-10-20.md`. O **documento efetivo já consta na main com blob SHA `d486214a482d7a0e6b78114746f1d476449a177f`**, conforme extração original #78. A ausência do campo na main não representa perda do documento. Por ser observação histórica de 20/10, não reintroduzir uma chave chamada `current*` na autoridade atual e não inferir causa de estado entre abas.

Leituras pontuais dos índices `runtime-evidence.json` das branches #42, #37 e #46 não encontraram outras chaves de objeto exclusivas, porém diferem em valores, listas ou subconjuntos de campos. A proposta #23 contém schema mais antigo sem seção `authFlowReview`, não uma nova observação atual. Isto **não prova igualdade de arrays, conteúdo semântico ou campos textuais** dos 48 blobs divergentes nem autoriza exclusão de qualquer branch.

**Disposição:** INDEX_POINTER_ACCOUNTED_FOR; restante HOLD. Os arquivos históricos preservados permanecem rastreáveis pelo ledger [HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md), a auditoria de [HOLDs](DS_HOLD_BRANCH_DIFFERENCES_2026-10-26.md) e o [índice de diferenças de decisões](DS_HOLD_DECISION_FIELDS_2026-10-26.json). Não houve alteração de decisões, código, runtime real ou produto.
