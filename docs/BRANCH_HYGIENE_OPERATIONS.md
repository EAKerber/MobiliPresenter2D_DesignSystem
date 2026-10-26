# Branch hygiene — procedimento canônico do Design System

**Escopo e fonte:** `EAKerber/MobiliPresenter2D_DesignSystem` exclusivamente. Implementação portada do mecanismo `EAKerber/MobiliPresenter2D` (arquivos `tools/branch_hygiene_{observe,plan,apply}.py`, testes e workflow), em 26/10/2026. Sem `gh`, sem credencial do usuário fora do `GITHUB_TOKEN` efêmero do Actions.

## Objetivo e política

A estrutura desejada é `main` como **única branch permanente**. Isso é objetivo de governança, **não** autorização para destruir trabalho ainda exclusivo. PRs abertas, evidências únicas, referências nominais em workflow e heads cujo conteúdo não esteja comprovadamente integrado ficam retidos. Excluir uma *ref* não exclui o histórico de commits já alcançável pela `main`; a prova de que a árvore estava completamente integrada fica registrada no recibo do lote. Uma PR marcada “merged”, por si só, **não** garante equivalência: squash, rebases e movimento posterior da branch exigem rechecagem.

Autoridade das informações: `decisions.json` para decisões; `dist/*.manifest.json` para tokens exportados e escopo; `docs/APPROVALS_D01_D04_2026-10-26.md` para decisões D01–D04; `docs/HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md` para evidências seletivas da PR #51. Snapshot e evidência histórica não substituem uma aprovação atual. A página `index.html` ainda duplica decisões manualmente e **não é** fonte primária.

## Ferramenta ativa

| Caminho | Responsabilidade |
| --- | --- |
| `tools/branch_hygiene_observe.py` | Consulta Git e GitHub com paginação, inventário completo de refs/SHAs/trees, proteção e heads/bases das PRs abertas; emite `BranchObservation 0.1` com hash. |
| `tools/branch_hygiene_plan.py` | Plano determinístico `BranchHygienePlan 0.1`; classifica candidatos e retenções sem efeitos colaterais. **Nenhum prefixo/nome é prova de exclusão.** |
| `ops/branch-dispositions.json` | Política versionada de preservação; decisões terminais só com evidência explícita e SHA exato. |
| `ops/branch-hygiene-batch.json` | **Única autorização operacional por lote**, 1–3 refs SHA-pinned; `squashMerge` só com PR/merge explícitos. |
| `tools/branch_hygiene_apply.py` | Reobserva e verifica hash do plano, integração, relação de PR, proteção, inventário, workflow ativo, lease e readback por exclusão. |
| `.github/workflows/branch-hygiene-bounded.yml` | Audit sem escrita em PR; apply **somente** em push `main` que altera manifesto de batch. |
| `tests/test_branch_hygiene_*.py` | Negativos de segurança; verificações antes de audit/apply. |

### Rotina de um lote

1. **Ler e reconciliar** inventário atual de `main`, PRs abertas, `.github/workflows`, e eventual conteúdo exclusivo, inclusive imagens e evidências. Para cada ref candidata, exigir um dos seguintes: (a) head é ancestral da `main`; (b) PR *merged* com head SHA idêntico à ref, commit de squash de um pai integrado à `main`, pai do merge ancestral do head e **árvore Git integral** do head exatamente igual à do merge. No caso (b) colocar `squashMerge` no manifesto. Caso contrário, **HOLD** e ledger de substituição/proveniência, sem delete.
2. Criar branch operacional a partir do SHA observado de `main` **ou reutilizar uma branch operacional cujas PRs anteriores estejam fechadas/merged, sem PR ativa e com divergência reduzida ao novo manifesto**. A reutilização reduz branches temporárias: conferir `compare main...head` antes de cada nova PR e exigir só o manifesto atualizado, sem reaproveitar lotes consumidos. Descrever refs/SHAs/PRs/árvores e riscos no PR em **draft**. Manter 1–3 refs por lote, sem automatizar toda a lista.
3. GitHub Actions `pull_request` calcula observação e plano, executa testes, e faz **audit-only** se o manifesto mudou. Conferir logs/artefato `m2d-ds-branch-batch-audit-<run>` e status **PASS** antes de marcar a PR pronta.
4. Comparar novamente SHA da PR e da `main`, checks e ausência de drift. Mesclar por **merge commit**. O push para `main` do manifesto aciona `apply` com `MOBILIPRESENTER2D_DESIGNSYSTEM_BRANCH_HYGIENE_AUTHORIZED=1` dentro do job; não expor essa flag como permissão generalizada.
5. Exigir log/artefato `m2d-ds-branch-batch-receipt-<run>` com `status=PASS`, `mode=apply`, `count=N`, `readback=PASS`. Consultar GitHub novamente e confirmar a ausência de **cada** ref. Atualizar o handover com PR, commits, SHA das refs, runs e contagem; não reutilizar manifesto consumido.
6. Se o gate abortar, **não** tentar delete manual e **não** fazer force-push. Investigar causa (SHA alterado, PR aberta, workflow dependente, árvore não idêntica, paginação, head de `main` ou autorização) e rever lote em nova PR. Geração de branch operacional pode neutralizar parcialmente a redução líquida; não criar lotes para trocar uma branch operacional por outra sem vantagem real.

### Exemplos dos dois tipos de entrada

```json
{
  "schemaVersion": "BranchHygieneBatch 0.1",
  "repository": "EAKerber/MobiliPresenter2D_DesignSystem",
  "wave": "DS-HYGIENE-NEXT",
  "purpose": "Apenas referências comprovadamente integradas, identificadas por SHA",
  "branches": [
    {"branch": "docs/historical-merged", "sha": "0123456789abcdef0123456789abcdef01234567"},
    {"branch": "audit/historical-squash", "sha": "abcdef0123456789abcdef0123456789abcdef01",
     "squashMerge": {"pullRequest": 20, "mergeCommit": "123456789abcdef0123456789abcdef0123456789a"}}
  ]
}
```

*Os valores de exemplo acima são ilustrativos e nunca devem ser aplicados.* `ops/branch-dispositions.json` contém os HOLDs explícitos. **Nenhum comando de exclusão livre** é suportado pelo fluxo.

### Inventário de pendências (26/10, snapshot antes do primeiro batch do novo executor)

- PRs abertas: DS [#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) — experimento DOM/CSS (~25 arquivos); [#41](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/41) — observação autenticada (~12 arquivos); [#51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51) — 236 arquivos diferentes, 7 documentos extraídos, conteúdo residual exclusivo **não classificado**. **HOLD**, sem merge em massa nem poda.
- `audit/approved-contrast-runtime-20261021` (#42), `audit/auth-session-flow-2026-10-19` (#37), `docs/reconcile-approved-focus-record` (#46): PRs fechadas sem merge, preservar até rastrear substituto.
- `docs/handover-reconcile-20261023`: não existe PR associada no inventário inicial; analisar exclusividade.
- `proposal/vis002-semantic-state-colors-2026-10-19`: head atual difere do head merged da PR #23; não supor equivalência.
- `architecture/p-token-01-executable-palette-20261022` e `architecture/p-token-02b-contextual-copy-20261022`: mesmo quando merged/equivalentes, **HOLD** por referências nos workflows de exportação enquanto estes triggers existirem.

### Resultado verificado do ciclo inicial (26/10/2026)

**38 branches iniciais → 10 branches finais: 30 refs eliminadas, duas operacionais criadas, redução líquida de 28.** [PR #64](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/64) portou o executor/observador do produto com testes; [PRs #65–#73 e #75](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pulls?q=is%3Apr+is%3Amerged+DS-HYG) executaram **10 lotes de três SHA-pins cada**. Todas as aplicações publicaram `status=PASS; mode=apply; count=3; readback=PASS`, com verificação adicional de contagem/ref na API. PR [#74](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/74) corrigiu os gates P-TOKEN-01 e 02B para disparar em `main`/PR, e ambos passaram em PR e push `main`; isso permitiu retirar as branches de tokens #49/#50 sem perder a validação.

| Lote | PR | Audit Actions | Apply Actions |
| --- | --- | --- | --- |
| DS-HYG-P01 | [#65](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/65) | [40415693021](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40415693021) | [40415848947](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40415848947) |
| DS-HYG-P02 | [#66](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/66) | [40416068259](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40416068259) | [40416176289](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40416176289) |
| DS-HYG-P03 | [#67](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/67) | [40416400765](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40416400765) | [40416499528](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40416499528) |
| DS-HYG-P04 | [#68](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/68) | [40416656057](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40416656057) | [40416836782](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40416836782) |
| DS-HYG-P05 | [#69](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/69) | [40417012867](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417012867) | [40417109760](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417109760) |
| DS-HYG-P06 | [#70](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/70) | [40417329963](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417329963) | [40417432448](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417432448) |
| DS-HYG-P07 | [#71](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/71) | [40417594199](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417594199) | [40417800017](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417800017) |
| DS-HYG-P08 | [#72](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/72) | [40417953084](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40417953084) | [40418058996](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40418058996) |
| DS-HYG-P09 | [#73](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/73) | [40418234061](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40418234061) | [40418380389](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40418380389) |
| DS-HYG-P10 | [#75](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/75) | [40419192192](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40419192192) | [40419285353](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40419285353) |

Os manifests históricos, nomes e SHAs exatos foram preservados em cada PR. O arquivo `ops/branch-hygiene-batch.json` na `main` tem **apenas o último lote consumido**; não é uma fila contínua nem deve ser repetido.

### Branches remanescentes e impedimentos reais

Snapshot depois do lote P10, **10 refs**:

| Branch | Situação e próximo gate |
| --- | --- |
| `main` | Única referência permanente desejada; toda autoridade documental/token válida deve estar aqui. |
| `maintenance/ds-product-hygiene-batch01-20261026` | Única branch operacional remanescente; não deletar enquanto houver PR usando esta head; remover ao encerrar os lotes via um caminho com auditoria de PR encerrada (nunca força). |
| `architecture/dom-css-consolidation-20261020` | PR #39 OPEN: proposta DOM/CSS e experimentos. Extrair artefatos úteis com hash/proveniência e gates; só então fechar a PR e retirar a ref. |
| `audit/access-confirmation-runtime-20261020` | PR #41 OPEN: auditoria runtime privada. Incorporar evidência válida contextualizada por deploy, sem declarar confirmação atual; fechar após reconciliação. |
| `docs/current-handover-20261024` | PR #51 OPEN: 236 caminhos alterados, 7 textos já extraídos; completar ledger e preservar binários exclusivos antes de fechar, sem merge integral. |
| `audit/approved-contrast-runtime-20261021` | PR #42 CLOSED e não merged. Classificar todos os blobs de evidência/decisões antes de retirar. |
| `audit/auth-session-flow-2026-10-19` | PR #37 CLOSED e não merged. Classificar testes/documentos únicos e achados versus main. |
| `docs/reconcile-approved-focus-record` | PR #46 CLOSED e não merged. Comparar alterações de decisões com #47/main e provar absorção integral. |
| `docs/handover-reconcile-20261023` | Não apareceu PR associada; inventariar diferenciais e reconciliação. |
| `proposal/vis002-semantic-state-colors-2026-10-19` | PR #23 MERGED, mas **head atual da branch difere do head que foi mesclado**. Não presumir equivalência; auditar commits adicionais. |

**Próxima meta:** cada uma das oito refs HOLDS só pode sair depois de materialização seletiva ou prova verificável de cobertura total, comparação de blobs/árvores, revisão da respectiva PR e registro no ledger. Não fazer squash de toda #51, não redatar evidências antigas como atuais e não reabrir homologações visuais CLOSED.

### Portabilidade e desativação do legado

A rotina antiga `tools/retire_merged_branches.py`, seu teste, o manifesto legado `ops/branch-retirement-batch.json` e o workflow `.github/workflows/branch-retirement.yml` foram desativados/retirados do estado corrente; **seu conteúdo permanece no histórico Git** e os recibos em Actions/PRs #59–#63. Só `tools/branch_hygiene_*.py` e os workflows de higiene acima operam a partir da `main`. Não existem duas autoridades de exclusão.
