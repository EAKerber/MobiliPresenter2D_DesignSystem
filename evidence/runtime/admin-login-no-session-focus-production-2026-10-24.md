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
