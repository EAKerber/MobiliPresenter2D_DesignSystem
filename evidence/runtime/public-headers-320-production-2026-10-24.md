# Cabeçalhos públicos em 320 px — Production (24/10/2026)

**Alvo:** `EAKerber/MobiliPresenter2D@main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`. Contexto público anônimo, browser isolado temporário. Medições CSS em 320×700 e 335×760; About também foi observado em 360×800 e 390×844. O viewport foi restaurado e a aba temporária fechada. Nenhuma captura foi persistida.

| Rota | 320 px | 335 px | Tema e evidência |
|---|---|---|---|
| `/about/` | `innerWidth=320`, `clientWidth=305`, documento/body/header em 320 px; overflow horizontal de 15 px e barra visível na captura | sem overflow (`clientWidth=scrollWidth=320`) | 320 escuro e claro; em 335, escuro. Também sem overflow em 360 e 390 px no escuro |
| `/viewer/` | `innerWidth=320`, `clientWidth=305`, documento/body/header em 320 px; overflow horizontal de 15 px e barra visível na captura | sem overflow (`clientWidth=scrollWidth=320`) | 320 claro e escuro; em 335, escuro |
| `/how-it-works/` | `html/body` e header em 320 px; `clientWidth=305`, `scrollWidth=320`; `.how-page` usa `overflow-x:clip`, cortando o excesso em vez de exibir barra horizontal | sem overflow (`clientWidth=scrollWidth=320`) | 320 e 335 escuros |

Nesta sessão, uma barra vertical de 15 px reduz a área de layout: `innerWidth=320`, mas `documentElement.clientWidth=305`. About e Viewer mantêm 320 px e mostram rolagem horizontal. Como funciona mantém `min-width:320px` em `html/body` e recorta 15 px da área útil. O ponto sem overflow foi observado em 335 px; isto não determina o breakpoint CSS exato nem implica o mesmo resultado em navegadores com barras sobrepostas.

No About a 320 px, o menu abriu por clique e Escape fechou-o com foco restaurado ao botão. O comportamento do link “Pular para o conteúdo” já está registrado separadamente: muda a âncora, mas termina com foco em `body`. Não abri o menu em Viewer ou Como funciona. Uma amostra por rota/largura; sem alteração de produto, dados ou preferência persistente de tema.
