# ARC-13 — rastreio do `submit` de `loginForm`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O submit impede a navegação padrão, desabilita o botão e mostra “Entrando…” durante a chamada de autenticação. Em sucesso, limpa a mensagem. Em falha, usa `error.message` do serviço quando presente; o texto indexado “Não foi possível entrar. Confira os dados e tente novamente.” é fallback somente se a exceção não trouxer mensagem. O botão é reabilitado no `finally`.

A ocorrência é copy pública de fallback para uma tentativa de login. A mensagem dinâmica do serviço tem consumer e proveniência distintos e não deve ser substituída por esse fallback na extração.

## Ponto de segurança/UX a revisar

A UI exibe diretamente `error.message` quando preenchido. Este rastreio não verificou os tipos de erro produzidos pela integração nem se algum deles revela detalhe interno. Antes de refatorar esse caminho, confirmar com o owner/auth quais mensagens são seguras para exibição.

## Limites

Rastreio estático do listener, estado de loading, fallback e retorno; sem teste runtime de autenticação nem classificação das mensagens do provider. Nenhuma chave foi proposta; código, índice ARC-13 e `decisions.json` permanecem inalterados.
