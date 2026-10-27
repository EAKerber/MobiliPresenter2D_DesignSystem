# D04 — contratos ARC-13 de alto risco e controle negativo (27/10/2026)

Origem: [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), HEAD `28062602a4ddcd1bee090742fe2587fe3837175d`; snapshot de produto `5ccb2a8`. [Manifesto de 6 blobs SHA-exact](DS_ARC13_CONTRACT_REVIEW_2026-10-27.json). A PR #51 foi fechada sem merge anteriormente; sua ref continua HOLD e é fonte histórica, não autoridade de runtime.

## Seleção dirigida por contrato

| Fonte histórica | Evidência materializada | Limite |
|---|---|---|
| [Publicação transacional do Admin](../evidence/architecture/arc13-semantic-key-proposal-admin-transactional-save-2026-10-25.json) | 39 ocorrências/chaves propostas em erros e confirmações de salvamento | `candidate-for-contextual-review-not-canonical`; não converter falha de readback em sucesso nem perder parâmetros |
| [Validação de preços](../evidence/architecture/arc13-classified-pricing-contract-batch-2026-10-24.json) | 27 ocorrências; 25 classificadas como texto localizável, duas como código | Verificar consumidor/mensagens em runtime antes de traduzir; schema/IDs não são UI |
| [Navegação privada](../evidence/architecture/arc13-classified-private-navigation-batch-2026-10-24.json) | 29 ocorrências; 13 textos e 16 valores técnicos | Identificadores ARIA, rotas, atributos CSS e eventos não são textos de tradução |
| [Teclado — controle negativo](../evidence/architecture/arc13-classified-keyboard-navigation-technical-batch-2026-10-24.json) | 35 ocorrências técnicas; **0** texto localizável | Não confundir seletores/valores de controle com strings da UI |
| [Validação do Admin](../evidence/architecture/arc13-classified-admin-validation-batch-2026-10-24.json) | 72 ocorrências; 63 texto localizável e 9 código | Estados de erro/validação e owner precisam ser mantidos, mesmo quando textos se repetem |
| [Carrossel de detalhe do Configurador](../evidence/architecture/arc13-semantic-key-proposal-configurator-carousel-2026-10-25.json) | 26 chaves candidatas ligadas a rótulos, descrições e ações do carrossel | `candidate-for-contextual-review-not-canonical`; não pressupor mesma semântica entre rótulo, ARIA e tooltip |

Todos os blobs foram copiados sem alteração. A aprovação já recuperada da convenção ARC-13 **autoriza a regra de nomeação**, não os exemplos, reclassificações de owner nem o catálogo de tradução. Os seis itens têm rastreabilidade por fonte, commit/hash e contrato, mas **não** são testes funcionais novos.

## Disposição da origem e sequência

A #51 tinha 193 caminhos exclusivos após D04 anterior; estes seis reduzem para **187**: 34 `classified`, 36 outros ARC-13, 69 rastreios de consumer, 3 propostas visuais e 45 notas runtime. As duas propostas de chaves permanecem como candidatas; o lote de teclado é um controle negativo que evita extrair falsos recursos textuais.

O arquivo-mestre `arc13-runtime-js-candidates-main-2026-10-24.json` (~1,34 MB) ainda não foi incorporado porque sua leitura integral pelo conector não foi possível nesta inspeção. Copiá-lo sem validar cobertura/estrutura seria contrariar a seleção por evidência. Próximo gate: reconciliar índices e batches quantitativamente antes de trazer volumes grandes; manter a branch de fonte HOLD. Não adaptar as propostas à versão atual do produto sem nova leitura e consentimento de integração.
