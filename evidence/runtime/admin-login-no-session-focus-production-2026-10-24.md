# Tela de login administrativa sem autenticação — Production (24/10/2026)

**Alvo:** Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`. Navegar para `/access/manage.html` redirecionou a `/admin.html?returnTo=%2Faccess%2Fmanage.html`, que exibiu o formulário de acesso restrito. A rota direta `/admin.html` exibiu o mesmo formulário. Nenhuma área administrativa autenticada foi aberta.

## Layout responsivo observado

Ajustei o viewport de forma temporária, e o DOM estabilizado confirmou as dimensões CSS correspondentes. O documento não teve overflow horizontal nos três pontos observados:

| Viewport | Largura do documento | Cartão de login |
|---|---:|---|
| 1280 × 720 | 1280 px | 480 px, centralizado |
| 390 × 844 | 390 px | 366 px, margens laterais de 12 px |
| 320 × 700 | 320 px | 296 px, margens laterais de 12 px |

Em 320 px, o cabeçalho cresceu para 104,58 px e o cartão permaneceu inteiro no viewport. O layout permaneceu sem overflow no tema escuro e claro; no tema claro, o viewport de 320 × 700 foi conferido via DOM.

## Foco por teclado e CSSOM

- Em 1280 × 720, o botão de tema recebeu foco por Tab: no escuro, `rgb(216, 188, 124)` com largura computada 2.66667 px e offset 2 px; no claro, `rgb(110, 81, 46)` com largura 2.66667 px e offset 2 px.
- No mesmo viewport, o campo de e-mail recebeu foco por Tab: escuro `rgb(216, 188, 124)`, 2 px/offset 2.66667 px; claro `rgb(110, 81, 46)`, 2 px/offset 2.66667 px.
- Em 320 × 700, tema claro, o campo de e-mail computou outline sólido `2px #6E512E` e offset de 3 px.

Os campos estavam previamente preenchidos pelo navegador. Não li nem registrei os valores, não alterei os campos e não submeti o formulário. Assim, esta evidência descreve o estado renderizado de login, mas não prova perfil limpo nem ausência de dados salvos. O fluxo autenticado não foi iniciado.

Restaurei o tema escuro, removi a substituição temporária do viewport e fechei as abas de auditoria. A captura móvel foi inspecionada, mas não persistida; ela mostrava campos preenchidos e não é anexada a este registro.

## Limites

Uma rota de login, sem acesso autenticado. Não verifiquei leitores de tela, fluxo de recuperação, entrada em áreas privadas, navegação após login ou saída. As leituras CSSOM indicaram dimensões fracionárias em algumas regras; a causa não foi isolada. Não há homologação global de VIS-002. Nenhum valor de campo foi transmitido, nenhum dado de conta foi alterado e nenhum CSS/token ou configuração de produto foi modificado.

## Rechecagem de foco por teclado — 24/10/2026

Na Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf` / deploy READY `6adc221479c773577ed45e23`, uma nova sessão anônima abriu `/access/manage.html` e foi redirecionada ao formulário de login em `/admin.html?returnTo=%2Faccess%2Fmanage.html`. O viewport padrão desta passagem foi 1280 × 720; a largura do documento permaneceu 1280 px, sem overflow horizontal. Nenhuma área autenticada foi aberta.

Tab percorreu a marca, controle de tema, menu, e-mail, senha, mostrar senha, Entrar e Esqueci minha senha. Todos os alvos receberam `:focus-visible` e não tinham sombra de foco. No tema claro, a marca computou contorno sólido de 2 px em `#6E512E` e offset 2,66667 px; o controle de tema computou 2,66667 px e offset 2 px; menu, campos e botões computaram 2 px e offset 2,66667 px. No escuro, menu, campos e botões computaram 2 px em `#D8BC7C` e offset 2,66667 px; o controle de tema computou 2,66667 px e offset 2 px. A marca foi medida em foco por teclado no claro; seu estilo escuro não foi isolado nesta passagem.

A cor clara observada (`#6E512E`) e as larguras de 2–2,66667 px divergem da referência VIS-002 (`#8B6A40`, 4 px/offset 3 px). No escuro, a cor coincide com a referência, mas a geometria observada permanece menor. Isso é uma divergência desta tela/estado, sem avaliação de contraste ou homologação global. Nenhuma alteração de CSS, token ou configuração foi feita.

Os valores dos campos não foram lidos ou copiados; o formulário não foi preenchido, enviado nem usado para recuperação. A árvore de acessibilidade ocultou valores após a troca de tema, e nenhum dado foi registrado. O tema foi restaurado para Claro, que era o estado inicial desta passagem, e a aba isolada foi fechada.
