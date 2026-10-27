# D04 — propostas ARC-13 e VIS-002 preservadas sem promoção de autoridade (27/10/2026)

Origem pinada: [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51) `@28062602a4ddcd1bee090742fe2587fe3837175d`; produto observado `5ccb2a8`. [Proveniência de 35 Git Blobs exatos](DS_D04_ARCHITECTURE_CANDIDATES_BLOBS_2026-10-27.json).

## Disposição dos 35 registros

- **32 arquivos ARC-13:** propostas de chaves semânticas por função/domínio, cross-batch audit, revisão de resíduos e relatórios de reclassificação de códigos e DOM sinks. São provas documentais úteis para futuras traduções, *não* aprovações de cada chave.
- **3 documentos VIS-002:** evidência de superfície escura dos cartões “Por que custa menos?”, mapeamento de rules/foco e keyline nos hotspots Viewer. Dois são candidatos de auditoria/foco, enquanto o terceiro registra autorização contextual **apenas para testes em preview da PR produto #242**, sem merge ou Production.

Os registros ARC-13 citam **517 propostas em 30 arquivos** na auditoria cruzada de 25/10 (o índice dela é histórico; parte dos arquivos já estava integrada por lotes anteriores). Seu cruzamento diferencia **507 chaves distintas** e casos de compartilhamento intencional, mas a aprovação anteriormente confirmada é **somente para a convenção de nomes**, não um catálogo de localização validado.

Uma revisão residual histórica registrou alternativas para pluralização, fragmentos HTML e owners. Isso não estabelece formato de mensagens ou regra de migração autorizada para o produto. Propor chaves sem essa resolução poderia misturar consumidores distintos, falhas de segurança, ARIA e mudanças de idioma.

## Fatos de segurança relevantes

1. **VIS-002/FIND-017:** em um snapshot, foco no cartão sobre superfície escura foi medido com contraste insuficiente no tema claro. A fonte se declara **experimental e não aprovada**. Preservá-la como memória do risco não altera tokens homologados.
2. **Foco dos hotspots do Viewer:** fonte de 25/10 relata opção A, com anel dourado e keylines neutras, aprovada pelo usuário **para teste em preview** de `.scene-hotspot:focus-visible` na PR #242. Não extrapolar para outros componentes, estados, merge ou publicação.
3. **Resíduo de localização:** propostas de configuração e core podem reutilizar texto com parâmetros diferentes; a auditoria indica agrupamentos, mas seu status é `candidate-for-contextual-review-not-canonical` em cada batch. Não promover sem owner e contrato de parâmetros confirmado.

## Gate

A PR documental preserva **35 blobs de origem com SHA inalterada** nos paths históricos e adiciona somente manifesto, relatório e atualizações do handover/ledger de higiene. Não editar `decisions.json`, catálogo, cores CSS, fluxos auth, workflows ou produto.

Saldo exclusivo da fonte #51: **80→45** após merge e conferência da tree; os 45 restantes são evidências runtime históricas. A branch da #51 continua HOLD; resolução de exclusividade documental não garante elegibilidade para apagar commits divergentes.
