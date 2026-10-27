# ARC-13 — rastreio do bucket Admin saveButton — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`. A leitura foi limitada às 23 ocorrências atribuídas pelo mapa lexical a `event click on saveButton`, linhas 1955–2057.

O bucket foi rastreado no call site do botão de publicação e em seus dois caminhos: publicação v5 hierárquica e publicação compatível legada. As mensagens estáticas e os valores dinâmicos que podem substituir fallbacks foram separados. Nenhuma chave foi proposta ou gravada; sem mudanças no índice, catálogo, runtime ou `decisions.json`.

## Rastreio das ocorrências

| Linha(s) | Texto estático | Condição / sink | Contrato que deve ser preservado |
|---|---|---|---|
| 1955 | A configuração publicada ainda não foi carregada. | Sem `publishedSource`; `throw Error`, capturado pelo handler e exibido em `saveMessage`. | Estado de precondição; não sugerir que uma publicação ocorreu. |
| 1959 | O rascunho não corresponde à revisão publicada. Recarregue antes de salvar. | Revision mismatch antes de PUT. | Concorrência/staleness; orientar reload e não salvar o rascunho. |
| 1965 | Publicando configuração hierárquica v5… | Progresso antes do PUT v5. | Estado transitório; não apresentar como sucesso. |
| 1974 / 2043 | Sua sessão não tem permissão para publicar esta configuração. | 401/403 no ramo v5 e no ramo legado; propagado ao mesmo catch/sink `saveMessage`. | Negação de autorização; a repetição tem mesma copy e mesmo contrato de consumidor, possível reutilização semântica a confirmar. |
| 1977 / 2044 | A configuração mudou em outra sessão. Recarregue o painel antes de salvar. | 409 nos dois ramos; propagado ao mesmo sink `saveMessage`. | Conflito de revisão; mesma copy/contrato nos ramos. |
| 1979 | A API recusou a publicação v5. | Fallback de `payload.message || payload.error || literal` para resposta v5 não-ok. | O texto dinâmico da API tem precedência; a chave candidata, se aprovada, cobriria somente o fallback. |
| 1981 | A resposta de publicação v5 não corresponde ao documento esperado. | PUT retornou OK, mas payload difere do snapshot projetado. | Falha de integridade da resposta; não anunciar sucesso. |
| 1988 | A publicação v5 foi aceita, mas a releitura de confirmação falhou. | PUT aceito, readback HTTP não-ok. | Aceitação sem confirmação readback; não tratar como falha prévia do PUT nem como publicação verificada. |
| 1992 | A releitura v5 não corresponde à revisão publicada; nenhuma confirmação foi assumida. | Readback JSON diverge do snapshot esperado. | Falha de confirmação/readback; manter sentido fail-closed. |
| 1996 / 2052 | `Versão ${model.revision} · editor hierárquico` | Mesmo `revisionLabel.textContent` atualizado após cada ramo concluir. | Uma mensagem parametrizada com `revision`; não converter a revisão em texto fixo. |
| 1999 | Configuração v5 publicada e verificada por releitura. | Sucesso v5 somente depois de readback JSON idêntico. | Estado de sucesso verificado; não reduzir a “publicado” sem readback. |
| 2004 | O schema publicado não é compatível com este editor. | Versão publicada diferente de v5 e do schema legado conhecido. | Erro de compatibilidade; não tentar salvar por outro caminho. |
| 2020 | A hierarquia foi alterada. Este rascunho não será achatado no schema publicado; publique a hierarquia apenas no checkpoint autenticado. | `projection.code === hierarchy_requires_publication`; feedback direto em `saveMessage`. | Guardrail de publicação autenticada; preservar a proibição de achatar estrutura. |
| 2028 | Este tipo de preço exige a futura publicação consolidada. Nenhuma configuração foi publicada; use Percentual para manter compatibilidade com o schema atual. | `pricing_requires_publication`; feedback direto em `saveMessage`. | Guardrail de preço; preservar “nenhuma configuração foi publicada” e a alternativa Percentual. |
| 2033 | A hierarquia não pode ser publicada com segurança. | Fallback quando `projection.errors[0]` está ausente. | A mensagem dinâmica do projetor tem precedência; fallback apenas para erro sem detalhe. |
| 2036 | Publicando configuração compatível… | Progresso antes do PUT legado. | Estado transitório; não apresentar como sucesso. |
| 2047 | A API bloqueou uma publicação hierárquica antes do checkpoint autorizado. | Erro `hierarchy_publication_required` no ramo legado. | Guardrail de segurança; não traduzir como falha genérica nem sugerir retry. |
| 2048 | A configuração não foi aceita. Confira nomes e itens selecionados. | Fallback `payload.message || literal` para resposta legada não-ok, exceto código de guardrail anterior. | O payload dinâmico prevalece; literal é fallback genérico. |
| 2054 | Configuração compatível publicada. A hierarquia estrutural continua protegida contra publicação prematura. | Sucesso legado após upgrade/readback no fluxo compatível. | Sucesso limitado; mantém explícito que hierarquia segue protegida. |
| 2057 | Falha ao publicar a configuração. | Fallback `error.message || literal` no catch comum. | A mensagem dinâmica do erro prevalece; a chave potencial cobre apenas fallback estático. |

## Resultado e próximos passos

As 23 ocorrências formam um único fluxo de publicação, mas não um único contrato textual. Há pelo menos cinco grupos semânticos: precondição/conflito, progresso, autenticação, confirmação de integridade/readback e guardrails de compatibilidade/publicação. Os erros de `payload.message`, `payload.error`, `projection.errors[0]` e `error.message` são values de runtime e não devem virar chaves estáticas por serem lidos pelo mesmo sink.

Três repetições têm candidato natural a reuso no próprio fluxo: mensagem de 401/403, mensagem de 409 e rótulo de revisão parametrizado por `model.revision`. A convenção aprovada permite esse reuso quando consumer/owner/parâmetros coincidem; a proposta individual segue pendente.

Próximo bucket para rastrear: `persistHandlesButton` (21 ocorrências), que separa gravação de puxadores da publicação hierárquica. Depois, `createDetailCarousel` (18). Manter auditoria de consumer/owner antes de propor chaves e sem migração de produto.
