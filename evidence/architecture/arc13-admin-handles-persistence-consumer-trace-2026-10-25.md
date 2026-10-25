# ARC-13 — rastreio do bucket Admin persistHandlesButton — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`. Foram rastreadas as 21 ocorrências do mapa lexical `event click on persistHandlesButton`, linhas 1858–1943.

O call site é uma operação de reparo exclusiva do schema v3 para persistir a atribuição de Puxadores em Acabamentos. Ela relê o estado publicado, pede confirmação se há rascunho local, verifica que o delta contenha somente a atribuição, valida o candidato, grava, compara a resposta e exige readback. O caminho não é a publicação hierárquica v5. Nenhuma chave foi proposta ou gravada; sem alteração no índice, catálogo, runtime ou `decisions.json`.

## Rastreio das ocorrências

| Linha(s) | Texto estático | Condição / sink | Contrato / valor dinâmico |
|---|---|---|---|
| 1858 | A configuração publicada ainda não foi carregada. | Precondição; erro chega ao catch e `saveMessage`. | Também aparece no handler `saveButton`; reuso não é automático, precisa confirmar owner/consumer/contrato. |
| 1859 | A persistência isolada de Puxadores é exclusiva do v3. | Bloqueia schema diferente do legado. | Explicar limite de versão do caminho; não sugerir que v5 é publicado aqui. |
| 1864 | Há alterações locais no painel. Esta operação publicará somente Puxadores no schema v3 e recarregará o painel; outras alterações locais não serão publicadas. Continuar? | `window.confirm` antes de continuar quando há draft local. | Confirmação de escopo e descarte das alterações locais não incluídas; preservar “somente Puxadores” e a pergunta explícita. |
| 1867 | Persistência de Puxadores cancelada; nenhuma alteração foi publicada. | Usuário cancela a confirmação; feedback em `saveMessage`. | Estado sem escrita; manter negação clara de publicação. |
| 1872 | Relendo a configuração publicada antes de persistir Puxadores… | Progresso antes do GET com `no-store`. | Estado transitório. |
| 1874 | Não foi possível reler a configuração publicada. | GET inicial não-ok. | Falha antes de gravar. |
| 1882 | A configuração mudou desde que o painel foi aberto. O painel foi recarregado; revise o estado antes de tentar novamente. | Readback inicial difere da fonte mantida; recarrega o painel e aborta. | Concorrência/staleness; preservar que houve reload e que o usuário deve revisar. |
| 1886 | Não foi possível preparar a atribuição de Puxadores. | Fallback se `handlesRepairPlan` não retorna `ok`. | `plan.message` dinâmico tem precedência; literal cobre apenas ausência de detalhe. |
| 1892 | Puxadores já está persistido em Acabamentos. | `plan.needed === false`; readback e estado local são atualizados. | Sucesso idempotente/no-op, não uma nova gravação. |
| 1897 | A alteração proposta não é exclusivamente a atribuição de Puxadores. | Fallback se verificação do delta isolado falha. | `delta.message` dinâmico tem precedência; manter limite de mudança. |
| 1902 | Persistindo apenas Puxadores em Acabamentos no schema v3… | Progresso antes do PUT com operação nomeada. | Estado transitório; enfatiza operação restrita. |
| 1913 | Sua sessão não tem permissão para persistir Puxadores. | 401/403. | Negação de autorização; mensagem específica para a operação. |
| 1914 | A configuração mudou durante a gravação. Recarregue o painel antes de tentar novamente. | 409. | Conflito de concorrência no PUT. |
| 1915 | A API recusou a gravação isolada de Puxadores. | Fallback para HTTP não-ok. | `payload.message` dinâmico tem precedência. |
| 1920 | A resposta da gravação não corresponde ao candidato v3 esperado. | PUT OK, JSON diverge do candidato normalizado. | Integridade da resposta; não confirmar. |
| 1924 | Puxadores foi gravado, mas a releitura de confirmação falhou. | PUT confirmado, GET de readback não-ok. | Não confundir gravação aceita com persistência verificada. |
| 1927 | A releitura não corresponde exatamente ao v3 esperado após persistir Puxadores. | JSON de readback diverge do esperado. | Falha de confirmação; manter comparação exata e estado não confirmado. |
| 1932 | `Versão ${model.revision} · editor hierárquico` | Atualiza `revisionLabel.textContent` após readback idêntico. | Consumer compartilhado com `saveButton`; manter `model.revision` como parâmetro. |
| 1938 | Puxadores foi persistido em Acabamentos no v3 publicado. O painel foi recarregado a partir do publicado; outras alterações locais não foram enviadas. | Sucesso se havia draft local. | Indica gravação bem-sucedida e descarte das alterações locais restantes. |
| 1939 | Puxadores foi persistido em Acabamentos no v3 publicado. A publicação hierárquica v5 continua bloqueada. | Sucesso sem draft local. | Distingue reparo v3 de publicação hierárquica v5; preservar a limitação. |
| 1943 | Falha ao persistir Puxadores. | Fallback do catch para erro sem `error.message`. | Mensagem dinâmica de erro prevalece. |

## Resultado e próximos passos

O fluxo mistura confirmação de escopo, leitura fresca, no-op idempotente, validação de delta, escrita autorizada, comparação de resposta e readback. Os valores `plan.message`, `delta.message`, erros de validação, `payload.message` e `error.message` são dinâmicos e não devem virar chaves estáticas só por chegarem a `saveMessage`.

A mensagem de revisão (`model.revision`) também aparece em `saveButton` com o mesmo sink e contrato de parâmetro, candidata a reuso semântico após conferência com índice/owner. O texto de precondição da linha 1858 se repete nos dois fluxos, mas a equivalência de consumer e ownership deve ser confirmada antes de compartilhar chave. O prompt de confirmação é único e requer preservação rigorosa do escopo da operação.

Próximo bucket: `createDetailCarousel` (18 ocorrências). Antes de propor chaves, distinguir instruções permanentes, placeholders, conteúdo vindo do catálogo, parâmetros de navegação e fallbacks de mídia. Nenhuma migração de produto foi feita.
