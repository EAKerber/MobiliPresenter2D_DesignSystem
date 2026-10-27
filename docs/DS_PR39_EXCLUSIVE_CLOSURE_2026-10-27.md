# D03/D04 — Extrato exato da PR #39 e destino de seus 21 arquivos exclusivos (27/10/2026)

## Identidade e regra de não promoção

Origem pinada: [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) — `architecture/dom-css-consolidation-20261020@8e7d857528c9ea14fa45c3f58b57c07c7036bca0`; baseline da main: `aaa30ae97efceaa9ea153cd10055a1a99e8e33f3`. [Manifesto de 21 arquivos, hashes e paths](DS_PR39_ALL_EXCLUSIVE_BLOBS_2026-10-27.json). Este processo **não faz merge da PR antiga**, não reescreve seus 9 caminhos divergentes em `main` e não converte ADRs/experimentos em homologação.

## Itens preservados

| Grupo | Quantidade | Disposição |
|---|---:|---|
| Documentos e ADRs `docs/architecture/` de 20/10 | **12** | Paths originais na main, **históricos**. O plano G0–G8, P4-NAV e propostas CSS refletem o produto `1878ae1`, não o atual. |
| Experimentos `experiments/declarative-ui/` e `experiments/public-dom/` | **7** | Paths originais, para reprodução isolada e estudo; sem importação pelo produto, sem novo workflow automatizado e sem execução neste lote. |
| Workflows `.github/workflows/` na origem | **2** | Git Blobs preservados com os mesmos bytes, mas copiados como **texto inerte** em `docs/architecture/legacy-workflow-sources/*.yml.txt`. Nenhum workflow é criado/ativado. |

Os dois textos inertes eram:
- `.github/workflows/declarative-ui-p1.yml`: teste Node 22 do registro experimental, disparado pelo branch antigo.
- `.github/workflows/public-dom-audit.yml`: Playwright público read-only para DOM/computed CSS, disparado pelo branch antigo; incluir no workflow ativo acionaria CI e novas requisições desnecessariamente.

## Valor preservado e riscos conhecidos

- **Ownership, CSS e cascata**: duplicação lexical de classe não é evidência de compatibilidade visual/comportamental. Um utilitário compartilhado só deve surgir após comparar semântica, estado, escopo, tema, viewport e consumidores reais.
- **UI declarativa**: o registro `PageCompositionExperimental 0.1` foi prova isolada, não schema de produto. `UI-ADR-004` explicitamente **não promove** o registro a sistema universal.
- **P4-NAV**: houve verificações técnicas descritas nas ADRs, mas sem autorização abrangente de publicação, suporte iPad real ou reestruturação CSS em lote. NAV-005 e `decisions.json@main` continuam autoridades mais recentes.
- **Experimentos**: README declara propósito isolado. O auditor público usa Chromium Playwright, GET de URLs públicas, e pode gravar um JSON **local** se executado explicitamente; nenhuma execução ou dependência automática foi acrescentada aqui. Não tratá-lo como gate atual de segurança, acessibilidade ou desempenho.
- **Linhas/links antigos**: caminhos nos 12 docs que citam `.github/workflows/` devem ser interpretados como referências **à branch fonte**, não como workflow disponível na main. Consulte o manifesto para localizar a cópia inerte.

## Prova e limites de encerramento

Conferir exatamente 21 SHAs de blobs de origem nos targets (19 com path original, dois inertes), nenhuma modificação de `.github/workflows/*`, `decisions.json`, `runtime-evidence.json`, `visual-inventory.json` ou arquivos de produto. Ao completar merge + readback: **zero caminhos exclusivos da fonte #39** versus main no escopo de paths originais exceto os **dois workflows**, cujos bytes estão preservados em paths inertes com mesmo blob SHA. Permanecem divergências em 9 arquivos canônicos antigos e commits da branch; isto **não comprova** equivalência de árvore/ancestralidade nem aptidão para exclusão.

A PR #39 pode ser avaliada para **fechamento como substituída**, após revisão de que nenhum de seus nove blobs modificados contém informação única ainda não representada por fontes canônicas ou pelo registro histórico. Fechar PR não apaga a branch. Próximo gate: análise por campo dos nove caminhos divergentes antes de encerrar a PR e eventual branch hygiene independente.
