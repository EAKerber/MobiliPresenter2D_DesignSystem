# HANDOVER — Design System / Branch Hygiene / DAG (27/10/2026)

**Leitura inicial para próximo agente:** este documento e [HANDOVER_CURRENT.md](HANDOVER_CURRENT.md) no repo `EAKerber/MobiliPresenter2D_DesignSystem`. Snapshot verificado em **27/10/2026** (Brasil); `main@14596cbd489c16cb23406d9a5f407b406185916f` antes desta PR. Reconferir a main, tags, rulesets, PRs e heads de branches no momento da retomada. Este é um **handover de operação**, não uma aprovação técnica/visual.

## Objetivo e prioridades

1. **Repositório prioritário:** `EAKerber/MobiliPresenter2D_DesignSystem`, chegar eventualmente a **apenas `main` como branch** sem perder bytes úteis nem histórico Git dos trabalhos antigos. O repo de produto `EAKerber/MobiliPresenter2D` permanece **sem operações de escrita/merge/deploy nesta frente**.
2. O usuário autorizou a continuidade do trabalho de higiene, com preferência por poda agressiva **somente com integridade e reversibilidade comprovadas**. Não reinterpretar a autorização como dispensa de gates técnicos; não reescrever/deletar `main`.
3. Decisões homologadas no `decisions.json@main` têm precedência sobre propostas datadas. D01: integração incremental após gates; D02: testes isolados inicialmente aceitáveis apenas no escopo; D03: extrair conteúdo útil e encerrar PRs substituídas; D04: extrair seletivamente com SHA/proveniência.

## Estado atual observado

| Verificação | Resultado |
| --- | --- |
| SHA da `main` antes deste checkpoint | `14596cbd489c16cb23406d9a5f407b406185916f` |
| Último merge substantivo | [#106](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/106), DAG owner gate e readback pós-#105 |
| GitHub Actions no SHA `14596cbd489c16cb23406d9a5f407b406185916f` | [run #40452414779](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40452414779), **PASS** |
| PRs abertas | **0** |
| Branches existentes | **10**: `main`, 1 branch operacional, 8 HOLDs |
| PRs históricas #39 e #51 | **CLOSED, NOT MERGED**; suas refs de origem seguem preservadas |
| Cópias dos blobs dos 8 HEADs HOLD na `main` | **100%** por identidade de blob SHA (HEAD somente) |
| Cobertura dos commits intermediários divergentes | **NÃO GARANTIDA pela main**; refs antigas ainda são necessárias |
| Tags de retenção DAG | **0** no readback de #106; nenhuma criação nesta frente |
| Rulesets de proteção retornados pela API | **0** na leitura atual |
| Batch de exclusão vigente | `ops/branch-hygiene-batch.json` ainda aponta ao **P12 já consumido**: **não reexecutar** |
| Branches removidas nesta retomada | **0** |

### Refs HOLD pinadas

| Branch | SHA do HEAD histórico |
| --- | --- |
| `architecture/dom-css-consolidation-20261020` | `8e7d857528c9ea14fa45c3f58b57c07c7036bca0` |
| `audit/access-confirmation-runtime-20261020` | `ae58f2199e9b3be5ba4ea313c86e7d26dd60ff37` |
| `audit/approved-contrast-runtime-20261021` | `e848e079071f4b2ce788e18a10a2284e6a24ff7a` |
| `audit/auth-session-flow-2026-10-19` | `360d2e6d93d93ab74036149b518f22c01d57ecb0` |
| `docs/current-handover-20261024` | `28062602a4ddcd1bee090742fe2587fe3837175d` |
| `docs/handover-reconcile-20261023` | `96093786ed8fb182c604182c37a42681cba8d6c9` |
| `docs/reconcile-approved-focus-record` | `430f4e1c7b376ae08e1788bd3aa365a32f2b76e2` |
| `proposal/vis002-semantic-state-colors-2026-10-19` | `a924c2be0e8b75d90e4faa570a8a9f55f0b6f812` |

Ref operacional: `maintenance/ds-pr41-runtime-evidence-extract-20261026` (HEAD pré-PR `34f6deeb87f10bb8ad50315211d96186b4fd45ae`); atualização/merge desta PR pode mover seu HEAD. Não codificar a SHA operacional pré-PR como alvo de exclusão de seu próprio commit.

## Trabalho entregue — não reproduzir

- PRs **#83–#98** recuperaram seletivamente arquivos, decisões históricas e evidências; #93 trouxe dois workflows apenas como `.yml.txt` **inertes**, sem ativá-los. #39 foi fechada como substituída na trilha #93/#94, sem merge integral.
- #97 recuperou os índices ARC-13 JS/HTML; 27/29 lotes JS e 7/7 lotes HTML coincidiram no multiconjunto de quatro campos, mas dois JS eram composições semânticas e não foram declarados equivalentes.
- #98 conservou 32 batches classificados; #99 conservou 69 consumer traces e 2 mapas; #100 preservou 35 propostas restantes sem homologá-las; #101 terminou a preservação dos últimos 45 registros runtime da #51.
- #102 arquivou **11 blobs canônicos antigos** da #51 como material inerte; #103 preservou **45 blobs distintos** usados em **54 ocorrências de sete outros heads**; #104 confirmou que **nenhum blob do HEAD de oito HOLDs** ficou ausente da main. Isso **não** prova que todos os estados intermediários do DAG estejam na main.
- #105 adicionou protocolo read-only de retenção via tags e auditor `tools/branch_hygiene_retention_audit.py` com testes negativos. #106 registrou **0 tags/rulesets**, mantendo bloqueio de deleção.

Fontes permanentes de prova:

- [Auditoria de 8 heads e cobertura dos blobs](DS_HOLD_FINAL_HEAD_CONTENT_READBACK_2026-10-27.json).
- [Limites de retirada por ancestralidade](DS_HOLD_FINAL_RETIREMENT_GATES_2026-10-27.md).
- [Protocolo de retenção do DAG](DS_DAG_TAG_RETENTION_PROTOCOL_2026-10-27.md).
- [Manifesto PROPOSAL_ONLY dos 8 nomes de tags e SHAs](DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json).
- `ops/branch-dispositions.json`: as oito refs continuam listadas em `preserveBranches`; `terminalBranches` vazio.
- `tools/branch_hygiene_plan.py`, `tools/branch_hygiene_apply.py`: processo de poda com leases/gates. Não contornar.
- [Handover canônico acumulativo](HANDOVER_CURRENT.md) e [histórico de extrações](HANDOVER_SELECTIVE_EXTRACTION_2026-10-26.md).

## Bloqueadores reais (não confundir com falta de documentação)

**HOLD-1 — Git DAG divergente:** apesar de todo conteúdo do HEAD estar preservado por SHA, as refs HOLD contêm commits intermediários não ancestrais da main. Contagens por branch da auditoria são 54, 3, 9, 12, 814, 6, 2 e 11, podendo ter interseções. Excluir a ref sem preservar seu histórico pode tornar esses commits irrecuperáveis.

**HOLD-2 — imutabilidade das tags:** a solução candidata é uma *tag leve protegida* apontando ao HEAD original de cada branch, em `refs/tags/ds-history/2026-10-27/*`. **O dono deve configurar e confirmar uma ruleset efetiva que bloqueie atualizar/deletar tags desse namespace.** No último readback, a lista de rulesets estava vazia. Nenhuma tag foi criada. Não chamar uma mera tag desprotegida de backup seguro.

**HOLD-3 — executor:** o auditor de retenção é somente leitura; seu próprio resultado nunca autoriza delete. O executor requer revisão com novo gate explícito de tag protegida, verificação de commit/tag remotamente alcançável, SHA/leases e testes negativos. Não mudar `terminalBranches` por inferência ou simular merges `ours`.

**HOLD-4 — última branch operacional:** a ref `maintenance/ds-pr41-runtime-evidence-extract-20261026` é absorvida pelos merges, mas um manifesto de exclusão gerado dentro de sua própria PR provoca *self-head SHA drift*. O protocolo propõe prova sobre o segundo pai do merge commit, com check de ref remoto e implementação separada. Não criar branches auxiliares intermináveis e não fazer delete manual sem gate.

## Próxima sequência segura

1. **Ação do proprietário:** criar e validar regra de proteção de tags sobre `ds-history/2026-10-27/*`, bloqueando exclusão e atualização/movimentação. Confirmar a regra ativa; revisar quais atores têm bypass. Caso não seja possível proteger tags, manter HOLD e escolher retenção alternativa verificável.
2. **Após proteção comprovada:** auditar refs/PRs/SHAs atuais e executar, em operação **não destrutiva**, a criação das oito tags leves com nomes e SHAs do manifesto; sem `--force`. Fazer readback do objeto commit, SHA, alcance via DAG e proteção. Não eliminar nenhuma branch nessa fase.
3. **Em PR separada e testada:** ampliar o executor para `PROTECTED_ARCHIVE_TAG_EXACT_COMMIT` com fail-closed, proteção de main, ausência de PR aberta, checks GitHub, leases e gate de segurança. Só depois remover de `preserveBranches` caso a prova de retenção esteja completa.
4. **Poda em lotes de 1–3 refs**, incluindo readback e handover; nenhum bundle de 8 deleções de uma vez. Fechar a questão da branch operacional num último gate independente.
5. Retomar a higiene de `EAKerber/MobiliPresenter2D` **em trilha distinta**, depois de validar o head e o escopo autorizado; não misturar com estas refs históricas do Design System.

## Prompt mínimo de recuperação

> Leia integralmente `docs/HANDOVER_DAG_HYGIENE_2026-10-27.md` e `docs/HANDOVER_CURRENT.md` de `EAKerber/MobiliPresenter2D_DesignSystem@main`. Confirme refs Git, PRs, rulesets, tags, CI e `ops/branch-dispositions.json` antes de agir. Respeite os gates: 8 HEADs têm todos os blobs preservados, **mas não os DAGs intermediários**, e tags ainda não estão protegidas. Prossiga pela proteção/verificação da retenção histórica; não remova branches sem prova de alcançabilidade e executor homologado. Atualize o handover por PR e reporte SHA/link.

## Readback e próximo gate executável — 27/10/2026 (rodada de retomada)

**Snapshot remoto independente antes desta alteração documental:** `main@f5c445224a443ead95961a0bd790f9251af9b774`; CI de branch hygiene `40494975930` **PASS**; **10 branches**, **0 PRs abertas**, **0 tags** em `refs/tags/`, **0 rulesets** em `/repos/EAKerber/MobiliPresenter2D_DesignSystem/rulesets`. Os oito HEADs HOLD ainda correspondem exatamente aos SHAs do manifesto `DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json`; a ref operacional estava em `7a6aab439fe271a00d12005babdd6f6aa91c88a1` e é ancestral da `main` (comparação: `main` 1 commit à frente, nenhum atrás). **0 deleções e 0 tags criadas**.

### Ação humana necessária: proteção do namespace de tags

O conector disponível nesta rodada permite ler rulesets e Git refs, mas **não expõe criação/edição de rulesets nem criação de tag refs**. Isso não pode ser resolvido movendo refs de branch ou simulando tags. Para destravar o próximo gate, o proprietário deverá configurar no GitHub:

1. [Configurações de rulesets do Design System](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/settings/rules): `New ruleset` → `New tag ruleset`. Nome sugerido: `DS historical DAG retention 2026-10-27`; **Enforcement: Active**.
2. **Target tags → Include by pattern:** `ds-history/2026-10-27/*` (a correspondência é sobre nomes de tags, sem prefixo `refs/tags/`; os oito nomes propostos têm somente um segmento depois da última barra).
3. **Tag protections:** ativar `Restrict updates` e `Restrict deletions`. **Não ativar `Restrict creations`**, para permitir o primeiro push das tags leves exatas. Deixar a lista de **bypass vazia** ou documentar e revisar todos os atores com bypass antes de considerar proteção suficiente. Salvar a regra ativa.
4. Fazer readback da regra pelo GitHub: alvo `tag`, `enforcement=active`, padrão de inclusão correspondente, regras de `update` e `deletion` e exceções/bypass. Se a API listar `[]`, regra desativada, escopo diferente ou permissões insuficientes, **manter HOLD**.

Documentação oficial: [criar rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository) e [proteções disponíveis](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets). Esta proteção fornece controle operacional, **não imutabilidade absoluta contra administradores capazes de alterar a própria regra**.

**Depois da confirmação:** retomar fase de **criação não destrutiva** das oito tags leves `refs/tags/ds-history/2026-10-27/*` apontadas por SHA no manifesto, com `git push` sem `--force`, readback independente de SHA/tipo de objeto/ancestralidade/proteção e recibo; somente numa PR e gate posteriores considerar suporte de executor e exclusão em lotes de 1–3. O manifesto `ops/branch-hygiene-batch.json` permanece P12 consumido; **não reaplicar**. A branch operacional ainda exige gate de terminalidade independente. **Não realizar operações no repo de produto nesta frente.**


## Pós-gate — oito tags históricas protegidas criadas e verificadas (27/10/2026)

**Resultado confirmado após PRs #109–#111:** regraset de tags [#25953910](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/rules/25953910), `target=tag`, **Active**, incluindo somente `refs/tags/ds-history/2026-10-27/*`, bloqueando `deletion`, `update` e `non_fast_forward`; **bypass_actors=[]** confirmado pela API com acesso administrativo. Revisão pinada: `2026-10-27T08:49:23.055-03:00`. A regra pode ser alterada por administradores — proteção operacional, não imutabilidade física absoluta.

- **CI de retenção:** [run #40500797873](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40500797873) **PASS** no `main@a2621721a5fad8e453748374d6fc2fc50d9c5fd1`. Recibo Actions: `ds-dag-tag-retention-40500797873`, artifact ID `12732920974`. [CI de hygiene #40500797879](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40500797879) também **PASS**.
- **Readback remoto independente:** **8/8** tags no namespace, **sem extras**; cada `object.type=commit` e `object.sha` exatamente igual ao HEAD original do [manifesto D04/DAG](DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json). Verificação também confirmou **0 PRs abertas, 10 branches, todos os oito HEADs originais inalterados** e ruleset ativa sem bypass. **0 branches excluídas.**
- **Execução controlada:** [#109](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/109) introduziu `tools/ds_dag_tag_retain.py` e workflow `.github/workflows/ds-dag-tag-retain.yml`, testes sintéticos de drift/tags estranhas/PRs/proteção; [#110](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/110) e [#111](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/111) corrigiram divergências de visibilidade e timezone da API no `GITHUB_TOKEN`, **sem relaxar proteção de bypass**. Os dois primeiros dispatches falharam **antes de criar qualquer tag**. A API oculta `bypass_actors` do token de Actions; o criador aceita valor mascarado apenas com revisão temporal idêntica à verificada por autoridade administrativa, demais requisitos completos e nenhum bypass do próprio ator.
- **Intacto:** `ops/branch-dispositions.json` ainda mantém os oito `preserveBranches`, `terminalBranches=[]`; lote `ops/branch-hygiene-batch.json` ainda é o P12 **consumido**; não foi reexecutado. Nenhum deploy, mutação do repositório de produto ou merge de código histórico divergido.

**Próximo gate obrigatório, separado:** desenvolver e revisar em **outra PR** o executor de `PROTECTED_ARCHIVE_TAG_EXACT_COMMIT` com validação efetiva de tag protegida, alcance do DAG via `git rev-list`/commit em clone completo, SHA/lease de branch, readback remoto, nenhuma PR aberta, checks e testes negativos. Somente após prova completa retirar branches específicas de `preserveBranches` e excluir em **lotes de 1–3**. A branch operacional exige gate terminal próprio baseado em ancestralidade do HEAD contra merge real e ref remoto (sem manifesto autorreferente). **Não apagar nenhuma ref nesta fase.**
