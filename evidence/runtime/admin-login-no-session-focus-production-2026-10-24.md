# Tela de login administrativa sem autenticação — Production (24/10/2026)

**Alvo:** Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`. A navegação para `/access/manage.html` redirecionou para `/admin.html?returnTo=%2Faccess%2Fmanage.html`, que exibiu o formulário de acesso restrito. Nenhuma área administrativa autenticada foi aberta.

## Observação visual e de foco

Viewport desktop de 1280 × 720 CSS px; largura do documento permaneceu em 1280 px, sem overflow horizontal. No formulário e cabeçalho, a amostra de tema claro/escuro teve os seguintes valores CSSOM:

| Alvo focado | Tema | Contorno computado | Offset | Fundo do painel |
|---|---|---|---|---|
| Botão de tema | Escuro | `rgb(216, 188, 124)`, sólido, 2.66667 px | 2 px | — |
| Botão de tema | Claro | `rgb(110, 81, 46)`, sólido, 2.66667 px | 2 px | — |
| Campo de e-mail | Escuro | `rgb(216, 188, 124)`, sólido, 2 px | 2.66667 px | `rgb(27, 28, 26)` |
| Campo de e-mail | Claro | `rgb(110, 81, 46)`, sólido, 2 px | 2.66667 px | `rgb(255, 255, 255)` |

Os campos estavam previamente preenchidos pelo navegador. Não li nem registrei seus valores, não alterei os campos e não submeti o formulário. Por isso, esta evidência descreve o estado renderizado de login; não prova que a sessão ou o perfil do navegador estavam sem dados salvos.

Restaurei o tema escuro e fechei a aba temporária. A captura foi inspecionada, mas não persistida.

## Limites

Uma rota e um viewport desktop; não verifiquei mobile, leitores de tela, fluxo de recuperação, autenticação, navegação após login ou conteúdo privado. A medição do foco não homologa conformidade geral com VIS-002: a amostra do botão de tema computou 2.66667 px e offset 2 px; a do campo computou 2 px e offset 2.66667 px. A causa dos valores fracionários não foi isolada. Nenhum dado foi enviado, e nenhum CSS/token ou configuração do produto foi alterado.
