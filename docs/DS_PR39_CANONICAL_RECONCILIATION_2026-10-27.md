# D03 — Resolução das nove versões canônicas divergentes da PR #39 (27/10/2026)

**Fonte:** [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39), `8e7d857528c9ea14fa45c3f58b57c07c7036bca0`. **Comparação da main:** `aa21206809e590a249ee12190971d62b72d0ee34`. O [manifesto de reconciliação](DS_PR39_CANONICAL_FIELD_RECONCILIATION_2026-10-27.json) preserva os nove pares de hashes Git e as respectivas disposições.

## Resultado de segurança

A fonte tem 21 caminhos exclusivos: [PR #93](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/93) preservou **19** nos paths originais (12 docs/ADRs e 7 experimentos) e **2** workflows como arquivos de texto **inertes** fora de `.github/workflows`, todos por SHA exato. Não houve fusão indiscriminada do head antigo.

Nos **nove caminhos antigos também existentes na main**, não se deve substituir o conteúdo atual com aquele snapshot:

| Caminho antigo | Gate de comparação | Disposição |
|---|---|---|
| `decisions.json` | 22 IDs coincidem, nenhum novo ID; diferenças em NAV-005, VIS-002, VIS-003 e EST-02, conforme auditoria por campo anterior | Manter **main** com homologações mais recentes |
| `runtime-evidence.json` | 23 chaves raiz antigas aparecem na main; main contém quatro raízes adicionais. Seis interações antigas preservadas como prefixo das sete; follow-ups de contraste 3→5 | Manter índice maior/mais recente, sem reintroduzir statuses `current*` antigos |
| `visual-inventory.json` | Fonte antiga: produto `483ef2e`, 19/10. Main: `1878ae1`, 20/10. Ambos têm oito HTML e mesmo mapa CSS; somente `app/access/index.html` e `app/admin.html` mudaram no `sourceCoverage.html` | Manter inventário mais recente, não substituir hashes/contagens |
| `DECISION_APPLICATION_MAP.md` | Contém texto datado 19/10 sobre statuses de NAV-005/VIS-002/VIS-003 e snapshot anterior | Substituído pela versão mais recente da main |
| `FINDINGS_REGISTER.md` | Registra correções antigas ainda pendentes de verificação pós-deploy; main contém posteriores status e medidas delimitadas | Registro histórico, não estado novo |
| `PALETTE_CONFORMANCE.md` | Snapshot 18/10 com pares/contextos mais antigos | Não sobrepor conformidade atual |
| `VISUAL_INVENTORY.md` | Snapshot 19/10, status antigo da legenda VIS-003 | Não rebaixar evidência pós-deploy |
| `RUNTIME_AUDIT.md` | Linhas substantivas do head antigo encontradas no texto da main por comparação normalizada; main contém adicionais | Preservação textual dos trechos avaliados, sem certificar runtime |
| `README.md` | Índice antigo listava os arquivos da #39; essas fontes estão preservadas na main após #93 | Manter README atual, report histórico ligado pelos manifestos |

## Decisão D03

**A PR #39 pode ser encerrada como substituída sem merge integral**: o material único recebeu destinação explícita e os campos historicamente divergentes não devem sobrepor a autoridade da main. Registrar o motivo no fechamento.

**Isto NÃO autoriza excluir `architecture/dom-css-consolidation-20261020@8e7d857528c9ea14fa45c3f58b57c07c7036bca0`.** O HEAD mantém história divergente e os nove blobs originais permanecem acessíveis pela ref HOLD; um manifesto de hashes e o status CLOSED não são prova de alcançabilidade futura caso a ref desapareça. O mecanismo homologado de higiene continuará recusando uma exclusão sem ancestralidade/tree proof; não falsificar equivalência.

A comparação por linha não prova integralmente identidade semântica de dados embutidos, e a comparação de `visual-inventory.json` foi por chaves e fontes estruturais. Se um detalhe histórico precisar ser recuperado, usar a SHA de origem enquanto a ref HOLD permanecer.

**Gate desta PR documental:** só este relatório, manifesto de nove hashes e handover, nenhuma alteração em decisões, índices runtime/visual, workflows ativos, arquivos do produto nem dispositions de exclusão.
