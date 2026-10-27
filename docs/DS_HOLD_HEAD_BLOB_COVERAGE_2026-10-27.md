# D04 — pool deduplicado dos HEADs divergentes restantes (27/10/2026)

**Objetivo:** preservar as versões de conteúdo dos sete heads HOLD ainda não cobertas pela árvore principal, sem alterar as normas homologadas ou reativar código/workflows antigos. [Manifesto SHA e origens](DS_HOLD_HEAD_BLOB_POOL_2026-10-27.json). Base: `main@a762825e02f3ce06d0f499c08447ff17c0d59968`.

## Prova de origem e economia de cópias

A comparação árvore-a-árvore dos sete heads abaixo encontrou **54 ocorrências de blobs históricos não alcançáveis pela árvore da main**, correspondentes a **45 blobs Git distintos**. Os nove usos duplicados são consolidáveis por identidade exata de SHA; **não** se fez deduplicação apenas por nome ou texto aparente.

| Referência de origem | Blobs do head ainda ausentes antes do pool |
| --- | ---: |
| `architecture/dom-css-consolidation-20261020` | 9 |
| `audit/access-confirmation-runtime-20261020` | 8 |
| `audit/approved-contrast-runtime-20261021` | 9 |
| `audit/auth-session-flow-2026-10-19` | 9 |
| `docs/handover-reconcile-20261023` | 3 |
| `docs/reconcile-approved-focus-record` | 6 |
| `proposal/vis002-semantic-state-colors-2026-10-19` | 10 |

Total distinto: **45 blobs**, 2.744.271 bytes de origem, copiados com a mesma SHA para `docs/historical-branch-blobs/hold-pool/<sha>.txt`. O manifesto lista todas as **54** ligações branch/head/path → pool. A versão original de cada documento, índice de teste ou decisão antiga continua rastreável sem ocupar múltiplos arquivos por branch quando os bytes são iguais.

## Autoridade e segurança

- **Jamais substituir** `decisions.json` atual, índices runtime/visual, mapeamentos, registros ou README por variantes históricas.
- O pool utiliza somente arquivo **texto inerte `.txt`**, fora de `.github/workflows/`. Não habilita CI, configurações, migração, CSS, traduções ou produto.
- Estas versões datadas não são prova de bugs presentes, do estado de autenticação ou de CSS atual. `decisions.json@main` permanece canônico.
- A [PR #102](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/102) preservou separadamente os 11 blobs divergentes da #51; os 0 exclusivos da #51 já foram resolvidos nas PRs D04 anteriores. Após este pool, **todos os blobs que compõem os HEADs das oito refs HOLD terão uma entrada de mesmo SHA na árvore da main**.

## O bloqueio que permanece após preservar o conteúdo

Preservar os objetos de conteúdo na `main` é diferente de preservar a cadeia de commits `HEAD → parents → trees` de cada branch. O gate homologado do executor requer ancestralidade ou equivalência de squash/PR merged exata, **não apenas blobs acessíveis**. Nenhum dos sete HEADs recebeu um merge de ancestralidade nesta PR; a ref #51 também continua divergente.

Portanto, a classificação correta é **CONTENT_PRESERVED, BRANCH_RETIREMENT_BLOCKED**, e não `SAFE_TO_DELETE`. A retirada segura ainda precisa de procedimento de retenção do histórico aprovado e de execução SHA-pinned via branch hygiene; não usar `merge -s ours` para parecer integrado.

Nenhuma branch foi excluída. O caminho de retorno ao repositório do produto deve começar somente depois de decisão de governança sobre o destino da história, sem bloquear trabalho de análise já autorizado.
