# Preservação verificável do DAG Git — proposta controlada (27/10/2026)

**Status: PROPOSTA DOCUMENTAL E AUDITOR SOMENTE LEITURA.** Não criar tags, excluir branches, reescrever `main`, alterar workflows ou tornar qualquer HOLD `SAFE_TO_DELETE` nesta PR.

## Problema factual

Conforme [auditoria dos oito heads](DS_HOLD_FINAL_HEAD_CONTENT_READBACK_2026-10-27.json), os blobs dos seus HEADs já estão integralmente representados por SHA na `main`. Isso **não preserva o histórico intermediário**: contagens individuais de commits não ancestrais são 54, 3, 9, 12, 814, 6, 2 e 11 (não somáveis por haver sobreposição). A infraestrutura dispõe de 10 branches: `main`, 8 HOLDs e 1 operacional.

O histórico Git de um commit está alcançável enquanto exista uma ref que alcance esse commit. **Uma tag Git leve e estável no HEAD original de cada branch manteria, por seus pais, todo o DAG ancestral do mesmo HEAD**, sem trazer os estados históricos ao working tree do produto e sem simular um merge `ours`. Tags não são branches; portanto este desenho pode ser compatível com a meta de manter apenas `main` como branch. Não é uma garantia contra exclusão/mutação futura de tags sem proteção efetiva.

## Preparação entregue

- [Manifesto de oito refs/SHAs originais e nomes candidatos de tags](DS_DAG_TAG_RETENTION_PROPOSAL_2026-10-27.json) — somente `status: PROPOSAL_ONLY_NEVER_AUTHORIZE_DELETE`.
- `tools/branch_hygiene_retention_audit.py`: lê inventário `BranchObservation 0.1` e `git ls-remote --refs --tags origin`; verifica **SHA exato e duplicatas**. Nunca chama `git push`, não contém método de delete, e mesmo 8/8 retornará `branchDeletionAuthorized=false`.
- `tests/test_branch_hygiene_retention_audit.py`: negativos de SHA drift, tag móvel, PR aberta, tag inesperada, duplicação e status artificialmente aprovado.
- A API GitHub apresentou **0 tags e 0 rulesets** em 27/10 no repositório. Portanto não existe retenção por tag aplicada e não foi verificada qualquer regra de proteção dessas tags.

## Procedimento proposto, não autorizado automaticamente pelo manifesto

1. **Gate de proteção/autoridade**: aprovar explicitamente usar tags permanentes como refs de arquivo; exigir proteção efetiva do namespace `refs/tags/ds-history/*` por ruleset contra deletar/mover tags. Sem regra verificável, manter HOLDs; o auditor atual nunca atesta esse gate sozinho.
2. **Fase de retenção não destrutiva:** obter observação completa, ausência de PRs usando esses refs e heads SHA intactos; criar exclusivamente tags leves em SHAs exatos no namespace do manifesto, `git push` **sem `--force`** e `--force-with-lease` somente para branch delete futura (nunca para tag). Um manifesto divergente, uma tag já existente noutro commit ou uma mudança de branch deve bloquear.
3. **Readback independente:** `git ls-remote --refs --tags`, GitHub API, `git cat-file -t` commit e testes de alcance `git rev-list` em clone completo; conferir 8/8 tags SHA-pinned, proteções, ausência de tag extra, recibo durável por SHA e SHA atual da main.
4. **Gate de retirada separado:** somente então propor extensão explícita do executor atual para `PROTECTED_ARCHIVE_TAG_EXACT_COMMIT`, revisada com testes negativos e lotes de 1–3 refs. Retirar de `preserveBranches` **apenas após** um gate aprovado e comprovado, nunca por mera existência do manifesto. Manter ausência de PR aberta, branch protection, leases, main push, plano fresco, sem workflows referenciando o ref e readback para cada remoção.
5. **Última branch operacional:** o manifest de exclusão dentro da própria PR altera a SHA que tenta piná-la. Resolver separadamente por uma verificação do **segundo pai do merge commit** (head exato da PR), contra a ref remota atual, sem criar uma cadeia de branches; não usar auto-delete genérico.

## Riscos e salvaguardas

- GitHub tags existentes hoje: **nenhuma**; rulesets: **nenhum**. Uma tag não protegida tem risco de ser movida ou apagada posteriormente. O plano não afirma que existe proteção.
- A antiga tentativa de arquivamento alternativo foi bloqueada pela política registrada em [operações](BRANCH_HYGIENE_OPERATIONS.md). Esta etapa é **somente estudo/teste de auditoria**: não repete mecanismo de arquivamento ou bypass nem altera gates atuais.
- A ligação por tags preservaria **ancestralidade inteira**, mas não equivale a aceitar implementações ou alterações de schema contidas no histórico. `decisions.json@main` continua sendo autoridade de homologações.
- A última ref operacional pode ser eliminada *com prova própria* sem tag, pois seu HEAD é ancestral de `main`. Não mudar isso pelo expediente de commits artificiais sem proveniência.

**Resultado deste checkpoint:** desenho executável em fases e auditor read-only; **0 tags criadas; 0 branches eliminadas; 0 mudanças de runtime ou produção.**