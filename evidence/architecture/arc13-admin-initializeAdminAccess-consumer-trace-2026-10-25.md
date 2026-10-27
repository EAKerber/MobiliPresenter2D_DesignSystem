# ARC-13 — rastreio de `initializeAdminAccess`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer e fallback

Na inicialização do Admin, a função prioriza `recovery_token` no fragmento; senão trata callback de autenticação, abre ação de convite quando aplicável ou carrega o usuário. A ocorrência candidata é “Não foi possível concluir o acesso.”, exibida com tipo `error` quando `error.message` não está presente. Em seguida, o catch tenta recuperar/exibir o usuário com `getUser()`.

O texto fixo é fallback público de falha de inicialização. O caminho também exibe a mensagem dinâmica do erro quando existente, que não foi classificada aqui; validar com owner/auth se esse valor é seguro para apresentação. O segundo `getUser()` após o catch não tem um catch local no trecho e merece teste separado caso essa recuperação também possa falhar.

## Limites

Rastreio estático da inicialização; não exercitei callback, convite, recuperação, usuário existente ou falha dupla; sem validação de runtime/AT. Nenhuma chave foi proposta; código, índice ARC-13 e `decisions.json` permanecem inalterados.
