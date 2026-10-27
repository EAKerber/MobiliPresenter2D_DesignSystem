# Encerramento da preservação de conteúdo dos oito heads HOLD (27/10/2026)

[Leitura de máquina SHA-pinned](DS_HOLD_FINAL_HEAD_CONTENT_READBACK_2026-10-27.json) · `main@18e50981c322e153819d7cb1ce80139d8f71c4d9` · higiene observacional [Actions #40448667631](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/40448667631) **PASS**.

## Resultado objetivo

- **Oito heads de branches HOLD inspecionados** contra a árvore de `main`.
- **0 Git Blobs de arquivo do HEAD sem cópia alcançável em algum path da main**.
- A [PR #102](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/102) preservou **11** versões históricas sobrepostas da #51 em paths `.txt` inertes.
- A [PR #103](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/103) preservou **45 blobs distintos** que representavam 54 ocorrências em outras sete branches, sem copiar a mesma SHA várias vezes.
- **0 PRs abertas**, **10 branches físicas**: `main`, uma branch operacional e oito HOLDs; nenhuma referência foi apagada.
- Os caminhos originais da #51 já estavam completos na main após [PR #101](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/101). Dois workflows antigos da #39 foram guardados inertemente em [PR #93](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/93).

## O risco que permanece

Todos os oito heads continuam Git-historicamente **divergentes**, não ancestrais da main. A comparação de commits de origem (base=head histórico → main) encontrou commits do lado da branch que não aparecem na main: 54, 3, 9, 12, 814, 6, 2 e 11, respectivamente, nos heads listados no manifesto.

**Atenção:** não somar esses números como commits exclusivos do conjunto: histories se sobrepõem. A contagem mede divergência *por branch*, não commits únicos e não prova que cada commit histórico contém dado útil. Mas algum commit intermediário pode conter estados que não estão no HEAD final. O pool de blobs preserva **o estado de cada HEAD**, não todas as versões intermediárias.

## Retirada segura: duas condições independentes

**Branches HOLD:** o executor de higiene existente aceita ancestralidade ou squash-tree proof exato de uma PR merged. A cobertura de blobs **não satisfaz** esse gate. A regra de preservação anterior proibiu tratar merge `ours` artificial como integração; esta rodada não muda a regra nem elimina refs. Para atingir a meta `main` única sem perda de história, seria necessário um procedimento autorizado de preservação do DAG de commits (por exemplo, um bundle verificável/recuperável fora da lista de branches, se a infraestrutura permitir) e uma política de retiro revisada, com gate pós-arquivo independente. Não foi executado.

**Branch operacional:** `maintenance/ds-pr41-runtime-evidence-extract-20261026` é ancestral da main (`ahead_by=1`, `behind_by=0` no compare invertido). Seu conteúdo não precisa de preservação extra. Entretanto, o mecanismo atual usa manifesto SHA-pinned num PR vindo da própria branch: o commit que pede sua exclusão altera o próprio SHA e invalida o pin. É um problema de executor terminal, não de conteúdo. Não iniciar cadeia sem fim de branches auxiliares.

## Sequência recomendada

Primeiro definir um mecanismo de preservação e prova de recuperação do **histórico intermediário**; depois adaptar a higiene por uma PR pequena e com testes, mantendo `force-with-lease`, SHA exato, ausência de PR aberta, proteção de main e confirmação após exclusão. Só então agendar lotes curtos até restar exclusivamente `main`. Enquanto isso, o conteúdo consolidado já permite retomar com segurança a higiene do repositório do produto numa trilha independente, sem confundir desbloqueio de branches DS com autorização de merges/deploys do produto.
