# D04 — reconciliação por campo de decisões históricas (26/10/2026)

**Fonte canônica:** `decisions.json` na `main@f0417cb3eb243080207efc26b521ccee25e5a91f`, blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`. As cinco versões históricas de `decisions.json` foram obtidas pelos SHAs de cada ref e comparadas por campo, com inventário completo em [DS_HOLD_DECISION_FIELDS_2026-10-26.json](DS_HOLD_DECISION_FIELDS_2026-10-26.json).

| Branch | 22 IDs coincidem? | Decisões com campos divergentes |
| --- | --- | --- |
| `audit/access-confirmation-runtime-20261020` | Sim | NAV-005, VIS-002, VIS-003, EST-02 |
| `audit/approved-contrast-runtime-20261021` | Sim | NAV-005, VIS-002, VIS-003, EST-02 |
| `audit/auth-session-flow-2026-10-19` | Sim | NAV-005, VIS-002, VIS-003, EST-02 |
| `docs/reconcile-approved-focus-record` | Sim | NAV-005 |
| `proposal/vis002-semantic-state-colors-2026-10-19` | Sim | NAV-005, VIS-002, VIS-003, EST-02 |

**Resultado:** nenhuma das cinco versões contém um ID de decisão ausente na main. Os campos divergentes são estados/redações/versionamento de **NAV-005**, **VIS-002**, **VIS-003** e **EST-02**; a branch #46 só diverge em NAV-005. O orphan documental de 23/10 não alterava `decisions.json` relativamente à main e não foi contado aqui.

### Interpretação com proveniência

- **NAV-005:** documentos antigos agrupavam brand e retorno à esquerda no cabeçalho compacto; a main contém o ajuste aprovado de 21/10 (marca à esquerda, retorno no grupo de controles à direita). Não reaplicar proposta antiga.
- **VIS-002 / VIS-003:** estados históricos registravam verificação de contraste/DOM como pendente; a main documenta medições pós-deploy **somente nos contextos delimitados**, sem certificação global. Não regredir `product-CSS-applied`/evidências contextualizadas ao estado antigo.
- **EST-02:** a main detalha cores e medidas da referência de foco aprovada; o snapshot antigo enumerava mais itens como ainda não especificados. Não trocar especificidade posterior por omissões do passado.

**Gate alcançado:** reconciliação estrutural e de campos **apenas do arquivo `decisions.json`** dessas cinco refs. **NÃO** é prova de equivalência de `runtime-evidence.json`, `RUNTIME_AUDIT.md`, outras fontes divergentes ou história Git. Os seis HOLDs sem caminhos exclusivos continuam divergidos da main; este ledger não cria elegibilidade para delete nem altera os estados homologados. Para destravar a poda, ainda é necessário reconciliar os outros 48 diferenciais de blobs (com repetições) e escolher uma política de preservação de histórico compatível com os gates existentes. Nunca usar uma fusão de árvore velha para substituir autoridade atual.
