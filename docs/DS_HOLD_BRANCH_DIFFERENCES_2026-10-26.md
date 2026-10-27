# HOLDs do Design System — triagem por blob e ancestralidade (26/10/2026)

**Baseline:** `main@390bef5ded2fd3bc904de49e8130ebeb514671d4`. Fonte de cada branch: HEAD exato listado no [inventário Git Blob completo](DS_HOLD_BRANCH_BLOBS_2026-10-26.json). Este documento é **diagnóstico documental**, não autorização operacional para poda, merge de propostas, atualização de `decisions.json` ou criação de deploy.

## Resultado

| Ref (PR) | Caminhos exclusivos | Mesmos caminhos, blob divergente | Interpretação |
| --- | ---: | ---: | --- |
| `architecture/dom-css-consolidation-20261020` (#39) | 24 | 9 | Propostas/protótipos em HOLD |
| `audit/access-confirmation-runtime-20261020` (#41) | 0 | 8 | Documentos/registradores divergentes, HOLD |
| `audit/approved-contrast-runtime-20261021` (#42) | 0 | 9 | Documentos/registradores divergentes, HOLD |
| `audit/auth-session-flow-2026-10-19` (#37) | 0 | 9 | Documentos/registradores divergentes, HOLD |
| `docs/handover-reconcile-20261023` (sem PR identificada) | 0 | 6 | Documentos/registradores divergentes, HOLD |
| `docs/reconcile-approved-focus-record` (#46) | 0 | 6 | Documentos/registradores divergentes, HOLD |
| `proposal/vis002-semantic-state-colors-2026-10-19` (#23) | 0 | 10 | Documentos/registradores divergentes, HOLD |

**Seis HOLDS antigos não possuem nenhum *caminho* exclusivo** relativamente à main; entretanto, apresentam **48 divergências de blob, contando repetições entre branches**. *Zero caminhos novos NÃO significa texto/evidência integralmente preservados*. Os seis heads seguem **divergidos no Git** em relação à main (comparação base...main), portanto o executor de higiene **não** os considera ancestrais aptos à exclusão. Não se deve confundir a existência do mesmo caminho com integração de todos os fatos ou SHA idêntico.

### #39 — arquitetura e experimentos

Os 24 caminhos exclusivos se distribuem em **15 docs/JSON de arquitetura**, **7 arquivos de protótipos/experimentos** e **2 workflows experimentais**. Nove arquivos já existentes divergem, incluindo `decisions.json`, `runtime-evidence.json` e registros de aplicação. Experimentos são estáticos e isolados; o próprio [texto da PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) descreve testes sobre módulos ESM adaptados, não gates integrados de navegador ou implementação real. **Não habilitar workflows nem mesclar `decisions.json`**. Próximo recorte: avaliar os contratos de ownership/registry relevantes para o roadmap, preservar fonte/limites e isolar o que não tem aprovação técnica.

### Seis HOLDS antigos sem novos caminhos

- **#41 (8 divergências)**: sete blobs de evidência/captura já extraídos por #78 e FIND-015 por #79. Os arquivos divergentes restantes são principalmente registros consolidados; é necessário verificar o conteúdo de campos antes de qualquer retirada da ref.
- **#42 (9)**: contém `evidence/runtime/contrast-approved-pairs-2026-10-20.md` com **mesmo caminho e blob diferente** na main; comparar a seção original com evidência mais recente, sem revogar homologação.
- **#37 (9)**: `evidence/runtime/auth-session-flow-2026-10-19.md` é idêntico pelo SHA na main, mas registros mais amplos diferem; autenticação real não foi novamente validada nesta rodada.
- **Orphan de 23/10 (6)**: duas versões de workflow e quatro docs/registradores divergentes; não restaurar triggers antigos nem substituir handover atual.
- **#46 (6)**: `PALETTE_CONFORMANCE.md` preservado com blob idêntico; ainda há versão antiga de `decisions.json` e registradores.
- **#23 (10)**: PR mesclada historicamente, mas a ref avançou depois; imagens de estados candidatas constam na main, enquanto os registradores/tokenizações diferem. Não atribuir equivalência de árvore ao mero estado MERGED da PR.

**Gate de descarte:** (1) comparar cada campo relevante com a autoridade main, (2) preservar o que restar por proveniência, (3) conferir vínculo real PR/head e proteção/ancestralidade, (4) somente então reconsiderar elegibilidade pelo executor SHA-pinned. Com heads divergidos, nenhuma destas seis refs foi liberada para exclusão no presente lote.

**Nota de escopo:** o HOLD #51 foi inventariado separadamente em [DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json](DS_PR51_RESIDUAL_INVENTORY_2026-10-26.json); após [PR #83](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/83) são 218 caminhos exclusivos naquela ref. A branch operacional não é um HOLD e foi reutilizada sem abrir uma nova ref.
