# D04 — preservar versões canônicas divergentes da #51 sem sobrescrever a main (27/10/2026)

## Baseline verificável

Fonte: [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), `28062602a4ddcd1bee090742fe2587fe3837175d`; `main@6984276f08b8214bda1502886ccf3431e4555677`. Comparação entre árvores confirmou **zero paths exclusivos** após #101, mas **11 paths com blob distinto**. [Manifesto dos 11 arquivos: nome, SHA antigo, SHA atual e destino inerte](DS_D04_PR51_OLD_CANONICAL_BLOBS_2026-10-27.json).

Estes não são novos recursos aprovados. Cada blob antigo é reencaminhado para `docs/historical-branch-blobs/pr51/` preservando **exatamente o Git Blob SHA original**, e ganha sufixo `.txt` para evitar que um índice, Markdown canônico ou GitHub Actions o trate como documento/workflow ativo.

## Classificação por risco

- **Dois workflows** antigos de export P-TOKEN: guardar sob `docs/historical-branch-blobs/pr51/.github/workflows/*.yml.txt`; não instalar em `.github/workflows/`. A main mantém versões posteriores de gate/export.
- **Registros de decisão e documentação:** `DECISION_APPLICATION_MAP.md`, `FINDINGS_REGISTER.md`, `README.md`, `RUNTIME_AUDIT.md` e três handovers/roadmaps datados. A main continua fonte operacional, e `decisions.json@main` autoridade homologada. Os snapshots antigos não devem restaurar status de PR, issues ou aprovação.
- **Índices de evidência:** `runtime-evidence.json` e `visual-inventory.json` antigos ficam em `.json.txt`; não substituir os atuais, não reutilizar contagens/medidas em runtime sem rechecagem.

## O que esta prova fecha

**Cobertura de conteúdo por caminho/blob do head #51:** todos os paths exclusivos já estão na main pelos lotes D04, e os 11 blobs antigos divergentes passam a estar alcançáveis por paths inertes na árvore da main. Isto resolve a diferença de **conteúdo de arquivos do head**.

**O que NÃO fecha:** commit objects e grafos de ancestrais da branch antiga não ficam alcançáveis apenas porque o conteúdo dos blobs foi copiado. O executor de branch hygiene homologado exige ancestralidade ou prova de squash-tree/PR merged e continuará recusando exclusão dessa ref. Não usar `git merge -s ours`, trocar branch por tag ou suprimir os gates para simular integração.

Este lote não altera código, pipelines ativos, settings, produto, Netlify, autenticação nem tokens. Seu objetivo é tornar possível discutir separadamente a retenção do **histórico de commits**, agora que a retenção do **conteúdo** foi comprovada por blobs.

**Próximo gate:** validar os 11 SHAs arquivados e 0 exclusivos com readback de main; então inventariar refs HOLD restantes e decidir procedimento explícito de aposentadoria de branches que preserve a história, antes de qualquer operação destrutiva.
