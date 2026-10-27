# ARC-13 — rastreio de consumers de `showUser`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/admin/admin.js`, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, blob `79925345e43096df77bef54fe257e483f922edd8`.  
**Escopo:** três ocorrências do mapa lexical em `/admin.html`; rastreio manual do fluxo e dos ramos de autorização.

## Consumers e condições

- **`userLabel`:** depois do tratamento de `returnTo=/access/manage.html`, que redireciona somente se `canManageAccess(user)`, e após o gate `isAdmin(user)`. Só um usuário autorizado chega ao label. O e-mail é dado dinâmico; `Administrador` é o fallback estático quando não há e-mail.
- **Falha de dados administrativos:** no `catch` de `ensureAdminData()` ou `loadSettings()`, a mensagem prefere `error.message` fornecida pelo serviço e usa `Falha ao carregar os dados administrativos.` como fallback. A mensagem dinâmica não é proposta como chave aqui. Erros de uma execução obsoleta são ignorados por `runId`; `forbidden` mostra a falha, mas não adiciona retry.
- **`Tentar novamente`:** botão criado apenas para outras falhas do carregamento administrativo. Fica dentro do painel de erro, desabilita após o primeiro clique, atualiza a sessão por `getUser()` e chama `showUser` novamente.

A tela de login é exibida sem usuário, usuários não-admin seguem para o painel de acesso negado e o editor só aparece após carregar os dados de um admin. Esse bucket contém dois textos candidatos de interface; e-mail e mensagens específicas do serviço são valores dinâmicos e ficam fora deles.

## Limites

O escopo é uma leitura de código em `main`, não uma captura de runtime nem uma análise AST/call graph. Não foram propostas chaves, nem alterados índice, catálogo, produto ou `decisions.json`. O próximo bucket de três ocorrências selecionado para rastreio é `event click on stagesList`, cujas ações dependem da etapa selecionada.
