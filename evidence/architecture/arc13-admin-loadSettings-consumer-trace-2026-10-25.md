# ARC-13 — rastreio do bucket Admin loadSettings — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function loadSettings` tem sete ocorrências. O rastreio percorreu o GET de configuração, status de revisão, ramo de reparo v3 e os resultados de carregamento v5/legado. O chamador que captura erros e acrescenta retry foi verificado como fronteira externa. Sem alteração do produto, catálogo, índice ou `decisions.json); nenhuma chave foi proposta.

## As sete ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 1285 | A API de configuração ainda não foi publicada. | Erro emitido para resposta HTTP 404 no GET `/api/configuration`. | Falha específica de ausência da API/rota; não agrupar com erro de transporte ou outro status não-OK. |
| 1285 | Não foi possível carregar a configuração. | Erro alternativo para qualquer resposta não-OK que não seja 404. | Falha genérica do endpoint após distinção do 404; payload e status bruto não são parâmetros apresentados neste ramo. |
| 1289 | Versão ; · editor hierárquico | Dois fragmentos do label visível `Versão {revision} · editor hierárquico`. O número é `model.revision || 1). | Prefixo e sufixo de interface; revisão é valor dinâmico. Os dois fragmentos pertencem a um mesmo template visível, não a duas mensagens separadas. |
| 1294 | Puxadores ainda não está atribuído no v3 publicado. Persista Puxadores no v3 antes da futura publicação hierárquica. | Mensagem quando `refreshHandlesRepairState()` retorna reparo necessário e válido. | Estado de recuperação específico de schema v3 e atribuição de Puxadores. Manter alvo, versão e orientação futura; revisão de owner técnico/editorial recomendada. |
| 1296 | Configuração v5 carregada. A hierarquia e os preços tipados podem ser publicados com validação. | Sucesso informativo quando o schema publicado já é a versão hierárquica V5 e não há reparo de Puxadores pendente. | Confirma estado carregado e capacidade com validação; não promete publicação automática. |
| 1297 | Hierarquia carregada. Alterações estruturais permanecem em rascunho até a publicação hierárquica ser habilitada. | Ramo alternativo quando os dados foram elevados ao modelo hierárquico, mas o schema publicado ainda não habilita publicação estrutural. | Estado de draft/guardrail; preservar que a hierarquia está carregada enquanto a publicação estrutural continua bloqueada. |

## Fronteira externa de erro e retry

O chamador `showUser` captura erros de `loadSettings`, exibe `error.message` (ou fallback próprio fora deste bucket) em `adminServiceError` e oferece botão “Tentar novamente”; erro `forbidden` retorna sem esse retry. Portanto, os dois textos de falha desta função preservam causas distintas que chegam ao usuário, mesmo sem código de status no texto.

O GET envia credenciais same-origin e `cache: no-store`; após sucesso, clona a configuração publicada, deriva o modelo base e renderiza as abas. A mensagem de sucesso depende de schema e repair state, não apenas de transporte concluído.

## Resultado e próximo passo

As sete ocorrências são dois erros HTTP distintos, dois fragmentos de um label com revisão dinâmica e três estados de carregamento/recuperação. Não condensar esses estados em “carregado” nem tratar texto de reparo v3 como erro genérico. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin: `appendNominalDimensionControls` (5 ocorrências), relacionado a controles de medidas nominais; preservar unidade, validação e nome do módulo como parâmetro.
