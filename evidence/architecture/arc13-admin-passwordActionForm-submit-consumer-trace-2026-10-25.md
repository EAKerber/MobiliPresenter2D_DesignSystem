# ARC-13 — rastreio do `submit` de `passwordActionForm`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O formulário escolhe a ação a partir do contexto: aceitar convite, recuperar senha ou atualizar a senha da sessão atual. No sucesso limpa o fragmento de URL e recarrega a página. Em falha, exibe `error.message` se presente; “Não foi possível atualizar a senha.” é fallback quando não há mensagem.

A string indexada é copy pública do caminho de erro. Ela é distinta das mensagens fornecidas pela autenticação e não deve absorver conteúdo dinâmico de erro.

## Ponto de segurança/UX a revisar

Assim como no login, o listener exibe diretamente `error.message`. Este rastreio não inspecionou as mensagens geradas por convite, recuperação e atualização de sessão. Confirmar com owner/auth quais erros podem ser apresentados e se precisam de mapeamento para textos seguros.

## Limites

Rastreio estático; não exercitei os três caminhos nem leitor de tela. Nenhuma chave foi proposta; código, índice ARC-13 e `decisions.json` permanecem inalterados.
