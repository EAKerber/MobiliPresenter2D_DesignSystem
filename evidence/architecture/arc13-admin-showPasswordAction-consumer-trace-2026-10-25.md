# ARC-13 — rastreio do bucket Admin showPasswordAction — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function showPasswordAction` tem quatro ocorrências: duas mensagens de título e dois rótulos de botão, com branch por `type`. O rastreio conferiu os tokens de convite/recuperação para delimitar a ação, sem exibir ou tratar tokens como texto. Nenhuma chave foi proposta; sem alteração de auth, produto, índice ou `decisions.json`.

## As quatro ocorrências

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 1596 | Defina uma senha para concluir o convite de administrador. | Título do formulário quando `type === "invite"`. | Copy de conclusão de convite Admin; ação está vinculada ao token de convite. |
| 1597 | Defina uma nova senha para acessar a administração. | Título quando o tipo é recuperação de senha. | Copy de recuperação; explica que a nova senha dará acesso administrativo. Não tratar como convite. |
| 1598 | Aceitar convite | Label do botão para o branch de convite. | Ação de consumir convite e definir senha; o token não aparece no rótulo. |
| 1598 | Atualizar senha | Label do botão no branch de recuperação. | Ação de recuperação/atualização de senha; não é a ação de aceitar convite. |

## Fronteira do fluxo

A função mostra o formulário de ação, esconde o login e define `inviteToken` ou `recoveryToken` conforme o tipo. Mais adiante, o submit chama `acceptInvite` para convite ou `recoverPassword` para recuperação. As mensagens de sucesso/erro e validação da senha pertencem a outros consumers e não foram incorporadas neste bucket.

## Resultado e próximo passo

Os dois ramos têm finalidade e ação diferentes, ainda que compartilhem o mesmo formulário visual. Preservar essa diferença de semântica e não incluir tokens, email ou ids nos textos. Nenhuma chave foi proposta ou migrada.

Próximo bucket Admin de quatro ocorrências: `syncPasswordReveal`; rastrear o label acessível e estados revelar/ocultar, sem misturar estado visual com senha.
