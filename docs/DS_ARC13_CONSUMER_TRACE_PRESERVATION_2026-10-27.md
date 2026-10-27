# ARC-13 — rastreios de consumers e mapas de escopo preservados (27/10/2026)

[Manifesto de **71 hashes originais**](DS_ARC13_CONSUMER_TRACE_BLOBS_2026-10-27.json) · origem: [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), head `28062602a4ddcd1bee090742fe2587fe3837175d`; produto de referência `5ccb2a8`. Sem merge integral da branch e sem alteração do produto.

## Por que não descartar esses registros após recuperar os índices

O índice-mestre localiza ocorrências e classificação, mas não demonstra sozinho o **consumer efetivo**, estados, fluxo de erro, condição de exibição, foco/ARIA ou parâmetros. A convenção ARC-13 aprovada em 25/10 **exige owner, consumer e contrato de parâmetros** antes do compartilhamento de chaves. Os 69 rastreios distinguem essas condições por bucket de função.

As amostras inspecionadas nesta rodada mostram riscos concretos:

- **Admin / preços:** o texto sobre valores base é mostrado apenas com configuração válida; a opção começa desligada, e alterá-la não equivale a publicar. Um tradutor não pode fundir estado inicial, disponibilidade e ação de publicação.
- **Admin / autenticação:** `showUser` separa a autorização Admin, a mensagem dinâmica do provedor e o fallback estático, além do retry. Não converter `error.message` em recurso controlado pela UI.
- **Config / estado inválido:** `failClosedPublishedConfiguration` diferencia HTTP 422 internamente mas mantém uma mensagem pública única e a área de trabalho indisponível. Não revelar diagnóstico técnico nem declarar disponibilidade.
- **Config / preços:** a decomposição por módulo distingue adicionais, quantidades e condições, incluindo pluralização futura. Não compartilhar textos por mera igualdade lexical.
- **Config / PiP e carrossel:** ações manuais, deslocamento automático e retornos de foco são estados diferentes; títulos, tooltips, aria-labels e descrições seguem contratos distintos.

Também preservados dois mapas complementares:
- [Escopo léxico](../evidence/architecture/arc13-unkeyed-consumer-scope-map-2026-10-25.json): 336 ocorrências, 75 buckets de escopo e 21 grupos de texto duplicado, com origem SHA fixada.
- [Contexto de consumer](../evidence/architecture/arc13-unkeyed-consumer-context-map-2026-10-25.json): 364 ocorrências, 72 grupos e 22 grupos de texto duplicado; são **pistas estáticas**, não AST nem chamadas em runtime.

## Disposição e limites

Os 69 rastreios da origem ficam preservados nos mesmos paths e bytes, sem alterações. Seus nomes indicam o bucket revisado, **não** homologação de strings ou de implementação. A inspeção qualitativa acima foi feita por amostragem de fluxos críticos; não se afirma que todas as 69 páginas tenham sido revalidadas em runtime. O manifesto declara todos os 71 Git Blobs e seus tamanhos, permitindo recuperar os dados da fonte original.

- Nenhuma tradução, chave `semanticKey`, migração de catálogo ou decisão de paleta foi aplicada.
- Nenhuma suíte de produto, browser, workflow, deploy ou operação autenticada foi executada.
- A #51 sai de **151 para 80 caminhos exclusivos** após merge/readback: 32 outros ARC-13 restantes (antes 34, retirados dois mapas), **3 propostas VIS-002** e **45 relatórios runtime**. Não descartar os 80 sem classificá-los e não apagar a branch HOLD.
