# Admin: login e contraste dos rótulos — 2026-10-19

**Produto observado:** [MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D), deploy publicado no commit [483ef2e6f76a562a3096516ef68d8dfe072ec21f](https://github.com/EAKerber/MobiliPresenter2D/commit/483ef2e6f76a562a3096516ef68d8dfe072ec21f).  
**Rotas e sessão:** `/admin.html`; formulário de login em contexto isolado sem sessão e editor administrativo na sessão autenticada já existente. Nenhuma credencial foi digitada.  
**Viewports:** 1036 × 582 CSS px (captura raster 1554 × 873 px, DPR 1,5).  
**Escopo:** observação de leitura; nenhum checkbox, dado, publicação ou configuração foi alterado.

## Evidência visual do formulário de login

As capturas mostram o cabeçalho atual e o formulário de login sem dados de conta:

- [Tema claro](../../visualEvidence/private/admin-login/admin-login-light-2026-10-19.svg)
- [Tema escuro](../../visualEvidence/private/admin-login/admin-login-dark-2026-10-19.svg)

A aba isolada foi restaurada para o tema automático após as capturas. A sessão autenticada usada para medir o editor permaneceu separada e inalterada.

## Contraste observado no editor autenticado

Medição de estilos computados no DOM publicado e composição sRGB do texto e dos fundos sólidos dos ancestrais. Limite de triagem: 4,5:1 para texto normal; isto não constitui certificação independente de acessibilidade.

| Elemento | Claro | Escuro | Leitura |
|---|---:|---:|---|
| `.initial-state-option` — “Iniciar visível no configurador”, 10 px | **4,22:1** | 8,36:1 | Abaixo de 4,5:1 somente no claro |
| `.switch` — “Ativa”, 12 px | 5,22:1 | 9,11:1 | Acima do limite nos estados medidos |
| `#saveMessage` — mensagem de configuração carregada, 13 px | 4,79:1 | 10,00:1 | Acima do limite nos estados medidos |

No tema claro, `.initial-state-option` computa texto `#706C66` sobre fundo efetivo aproximado `#EAE7E2`. No escuro, o texto `#C4BCB2` fica sobre fundo efetivo aproximado `#232321`. O rótulo de 10 px é a única falha abaixo de 4,5:1 entre estes três elementos examinados.

O CSS carregado atribui ao rótulo o valor muted no seletor `.initial-state-option` ([admin.css no snapshot observado](https://github.com/EAKerber/MobiliPresenter2D/blob/483ef2e6f76a562a3096516ef68d8dfe072ec21f/app/admin/admin.css#L107)). A medição confirma uma falha de contraste no tema claro; a escolha do tratamento visual corretivo deve seguir as decisões e tokens homologados e ser validada no DOM após implementação. Não foi aplicado patch ao produto.

## Backlog e limites

- Registrado como FIND-013 e vinculado ao issue aberto [#208 — auditoria de cobertura light/dark no Admin](https://github.com/EAKerber/MobiliPresenter2D/issues/208).
- A inspeção confirma que a rota chega ao formulário de login quando não existe sessão no contexto isolado. Ela não testa o envio de credenciais, recuperação de senha nem a transição de login que originou o relato intermitente em [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212).
- As capturas são de uma página privada em estado assinado para fora; não contêm endereço de conta, nomes de clientes ou dados administrativos. Capturas da tela autenticada não foram persistidas.
- A preferência da sessão autenticada ficou em Automático (resolvido pelo sistema como escuro); a janela isolada também foi restaurada para Automático.
