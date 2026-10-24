# Auditoria visual em runtime

**Observação:** 2026-10-18  
**Site observado:** [casaemmodulos.casa](https://casaemmodulos.casa/)  
**Snapshot estático relacionado:** `EAKerber/MobiliPresenter2D` `main` em `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`, conforme inventário da etapa anterior.  
**Deploy de produção verificado:** `6ad518d3da1379029e04324f`, pronto em 2026-10-18, commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a` ([commit do produto](https://github.com/EAKerber/MobiliPresenter2D/commit/298c11441f82cacfff2f809fd9e5ad6f1fc33c0a)).  
**Decisões:** `decisions.json` continua sendo a fonte canônica. O cruzamento entre decisões, rotas e folhas carregadas está em [DECISION_APPLICATION_MAP.md](DECISION_APPLICATION_MAP.md).

## Escopo e método

Inspeção somente de leitura no site publicado, cobrindo páginas públicas, a tela de login e rotas privadas em sessão autenticada. O usuário concluiu o login e autorizou a navegação; não registramos o e-mail nem conteúdo de convites. Foram observados DOM, tema, largura do documento, cabeçalhos, comportamento do menu e alguns pares de contraste em superfícies sólidas. A medição de contraste usa cores computadas pelo navegador e luminância relativa; é uma triagem técnica, não uma certificação WCAG nem aprovação visual.

Nenhum código ou dado do produto foi alterado. Não foram enviados links, convites ou configurações, e nenhum teste automatizado foi executado. As capturas privadas autenticadas não foram persistidas no repositório. As capturas públicas persistidas como JPEG em 1265 × 712 são: [landing claro](visualEvidence/public/landing/landing-light.jpg), [landing escuro](visualEvidence/public/landing/landing-dark.jpg) e [viewer escuro](visualEvidence/public/viewer/viewer-dark.jpg). Elas documentam rotas públicas, portanto não demonstram o cabeçalho privado atualizado. Para isso, foram adicionadas capturas do login administrativo em 1280 × 720: [claro](visualEvidence/private/admin-login/admin-login-light.jpg), [escuro](visualEvidence/private/admin-login/admin-login-dark.jpg) e [menu escuro aberto](visualEvidence/private/admin-login/admin-login-menu-dark.jpg). Todas correspondem ao deploy de produção acima; são referências do estado publicado, não propostas homologadas. O conjunto original mostrado inline em 1440 × 900 permanece distinto destas capturas.

## Cobertura de rotas e tamanhos

| Rota solicitada | Estado observado | 390 px | 768 px | 1440 px |
|---|---|---:|---:|---:|
| Landing / ambientes `/` | Página pública | Sem overflow horizontal | Sem overflow horizontal | Sem overflow horizontal |
| Como funciona `/how-it-works/` | Página pública | Sem overflow horizontal | Sem overflow horizontal | Sem overflow horizontal |
| Quem somos `/about/` | Página pública | Sem overflow horizontal | Sem overflow horizontal | Sem overflow horizontal |
| Viewer `/viewer/` | Conteúdo publicado da cozinha carregado; cena e vistas presentes | Sem overflow horizontal | Sem overflow horizontal | Sem overflow horizontal |
| Administração `/admin.html` | Tela de login, sem autenticação | Sem overflow horizontal | Sem overflow horizontal | Sem overflow horizontal |
| Configurador `/config/` | Redireciona para `/access/` sem sessão | — | — | — |
| Gerenciar acessos `/access/manage.html` | Redireciona para `/admin.html?returnTo=%2Faccess%2Fmanage.html` sem sessão | — | — | — |
| Acesso por link `/access/` | Tela “Confirmar acesso ao configurador”; nenhum link foi enviado ou validado | — | — | Sem overflow horizontal |

As medidas observadas do cabeçalho foram: páginas públicas, 71 px em 390 px e 89 px em 768/1440 px; viewer, 65/70/78 px; administração/login, 66/68/78 px. A tela de acesso por link tinha 83 px em 1440 px. As diferenças são evidência do comportamento atual, não uma recomendação de medidas.

A verificação de largura foi feita comparando `scrollWidth` e `clientWidth` do documento. Não houve overflow horizontal nas rotas acima nos tamanhos observados. Isso não valida todos os componentes, todos os estados ou larguras intermediárias.

## Menus e navegação

### Menu privado na tela de login

Em `/admin.html`, no viewport de 390 px, o primeiro clique após o carregamento abriu o menu: `aria-expanded=true`. A navegação mostrou os grupos **Páginas privadas** e **Páginas públicas**. Sem sessão autenticada, a área privada mostrou apenas **Entrar na administração**; os destinos públicos incluíram Ambientes, Cozinha, Como funciona, Quem somos e Fale conosco. Não havia e-mail conectado nem ação de saída.

A mesma estrutura do menu foi observada em 768 px. Isso confirma o comportamento da tela de login naquele momento; não confirma o menu da administração autenticada nem o gerenciamento de convites.

### Menu público durante a abertura da landing

No primeiro carregamento da landing, o primeiro clique no hambúrguer ocorreu enquanto `#introSplash` ainda tinha `opacity: 1` e `pointer-events: auto`; o menu permaneceu fechado. Depois que a abertura terminou (observado após cerca de 1,8 s; `opacity: 0`, `pointer-events: none`), o clique abriu a navegação e mudou `aria-expanded` para `true`.

Isso localiza uma condição reproduzível em que a camada de introdução intercepta a interação inicial. Não prova que seja a causa dos relatos sobre páginas privadas. O menu público foi observado abrir depois que essa camada saiu; Escape, clique fora, retorno de foco, sequência completa por teclado e preferência por movimento reduzido não foram auditados aqui.

### Páginas protegidas: auditoria autenticada

Após o usuário autenticar, `admin.html` carregou o editor e a mensagem de falha de carregamento não estava visível nessa visita. O menu abriu e apresentou Configurador, Administração, Gerenciar acessos e Sair. Em `/config/`, a configuração carregou; o menu mostrou os grupos privado e público e Sair. Em `/access/manage.html`, a página de gerenciamento e o menu também foram observados autenticados, sem ler ou registrar valores de convites.

A sequência identificou uma inconsistência transitória: um estado do menu do Admin observado logo após o login ainda oferecia entrada, mas uma navegação nova para Admin mostrou as opções autenticadas. O menu funcionou nas verificações posteriores em Admin, Configurador e Gerenciar acessos. Isso não descarta a intermitência relatada nem explica sua causa.

No Configurador, o indicador exibiu `8 de 8 itens incluídos` sem módulos selecionados; na etapa Serviços, a iluminação estava desabilitada por dependência e o mesmo total continuou visível. Essa contradição confirma a inconsistência funcional descrita no issue #209. A inspeção foi somente visual/DOM; nenhum estado foi alterado. O novo achado de sobreposição entre a cena e o menu em viewport estreito está em [FINDINGS_REGISTER.md](FINDINGS_REGISTER.md) e no [issue #214](https://github.com/EAKerber/MobiliPresenter2D/issues/214). A inconsistência de sessão do menu está no [issue #213](https://github.com/EAKerber/MobiliPresenter2D/issues/213).

## Contraste: triagem em DOM real

Os seguintes pares foram lidos no DOM, em estado visual estável, sobre fundos sólidos. Para texto comum, valores abaixo de 4,5:1 ficam registrados como candidatos a correção técnica. A triagem não escolhe uma nova cor nem torna qualquer valor um token homologado.

| Tela / seletor | Tema | Viewport | Texto / superfície | Contraste | Leitura |
|---|---|---:|---|---:|---|
| Landing, `.hero-description` | Claro | 390 × 844 | `#706C66` sobre `#F0EDE8`, 16 px | 4,47:1 | Abaixo de 4,5:1 |
| Como funciona, `.how-hero-note` | Claro | 1440 × 900 | `#706C66` sobre `#F0EDE8`, 16 px | 4,47:1 | Abaixo de 4,5:1 |
| Quem somos, parágrafo de `.about-scale` | Claro | 1440 × 900 | `#706C66` sobre `#F0EDE8`, 16 px | 4,47:1 | Abaixo de 4,5:1 |
| Como funciona, `.eyebrow` em `.study-band` | Claro | 1440 × 900 | `#8B6A40` sobre `#E8E3DC`, 11,52 px | 3,89:1 | Abaixo de 4,5:1 |
| Como funciona, legenda de `.study-art` | Escuro | 1440 × 900 | `#C4BCB2` sobre `#FCF9EF` | 1,78:1 | Contraste baixo no painel claro mantido no tema escuro |
| Como funciona, `.launch-badge` “Condição especial” | Escuro | 1440 × 900 | texto branco sobre `#A64D13` | 5,69:1 | Par atual acima de 4,5:1; não aprova outras variantes |

Os três primeiros pares estão próximos do limite de 4,5:1, mas continuam abaixo dele. A legenda da ilustração é o caso mais evidente: a superfície clara da figura persiste no modo escuro, enquanto a legenda muda para um tom claro. O registro é de falha/candidato técnico no contexto observado. A composição foi aprovada em VIS-003: faixa escura opaca `#20211F` na base da ilustração e texto `#F0EDE8` (13,85:1). O produto ainda não foi alterado; dimensões, espaçamento e validação responsiva seguem pendentes.

A amostra promocional atual confirma que branco sobre a base aprovada `#A64D13` funciona neste componente e nesta superfície. Isso não homologa o uso em outros fundos, tamanhos de texto ou temas. As superfícies autenticadas do Admin — incluindo as opções mostradas no inventário estático — não tiveram contraste medido nesta sessão.

## Automação de contraste

O inventário estático não encontrou um gate de contraste conectado às rotas do produto. Os contrastes acima foram medidos nesta inspeção, não detectados por um workflow de CI. A auditoria fixture descrita no histórico do Design System não é evidência de cobertura completa do DOM de produção.

## Estados não verificados

- Teclado completo do menu: Escape, clique fora, retorno de foco e ordem de tabulação.
- Preferência de movimento reduzido no navegador e efeitos runtime correspondentes.
- Estados de foco, hover, pressionado, seleção e carregamento para todas as famílias.
- Contraste de textos sobre imagens, gradientes, pseudo-elementos e camadas transparentes; leituras automáticas nesses contextos podem produzir falsos positivos.

## Próxima etapa recomendada

1. VIS-002 agora registra dois pares contextuais aprovados para texto no tema claro; não são tokens globais e não resolvem os achados do tema escuro.
2. NAV-005 aprova as composições estruturais largas e compactas. No compacto, a opção A mantém uma linha, contexto junto da marca e tema antes do hambúrguer; breakpoints, medidas e tratamento visual continuam em aberto. A evidência runtime em 515 px é somente da rota pública.
3. Revalidar a camada de introdução e o primeiro clique no menu público como comportamento funcional, sem confundir esse achado com a navegação privada.
4. Reproduzir a transição pós-login e reconciliar a triagem estática #208 com o snapshot atual; a primeira inspeção autenticada confirmou o contador incorreto, mas não substitui a auditoria de contraste nos dois temas.
5. Planejar a etapa de aplicação visual no produto após revisar os padrões e fechar as medições restantes.


## Reconciliação da triagem estática DS-04

O issue [#208 do produto](https://github.com/EAKerber/MobiliPresenter2D/issues/208) foi atualizado após comparar seu baseline `67d3197` com o snapshot de produção `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`. No código, DS04-01 (carregamento do tema em `/access/`) e DS04-08 (fundo/texto do dock em tema claro) estão resolvidos. Permanecem candidatos estáticos DS04-02 a DS04-07, DS04-09, DS04-10 e DS04-12; DS04-11 está documentado como exceção técnica intencional. Essa reconciliação não inclui medidas runtime de contraste para cada seletor; os valores do relatório original continuam sendo medições do baseline, não do DOM atual. Veja a classificação detalhada no issue #208 e o [registro de achados](FINDINGS_REGISTER.md).


## Revisão visual do Configurador em tema claro (2026-10-18)

Em viewport estreito, a checagem visual em tema claro confirmou que o menu aberto continua atrás da imagem da cena e cobre parte do link “Como funciona” (também observado no tema escuro; [issue #214](https://github.com/EAKerber/MobiliPresenter2D/issues/214)). Na etapa Resumo, o rótulo “Módulos” em `.price-state__breakdown dt` aparece quase ilegível no cartão claro, confirmando visualmente DS04-07, sem nova razão numérica; registro em [issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208). No painel Serviços, o texto da iluminação indisponível por dependência também parece muito atenuado. Esse controle está desabilitado, então foi anotado como revisão visual, não como falha WCAG confirmada. Nenhuma opção da configuração foi marcada ou alterada. O navegador foi devolvido ao tema escuro, etapa Serviços e menu aberto.


## Confirmação pontual do contador no Configurador (2026-10-18)

Na sessão autenticada já aberta no navegador, em viewport de aproximadamente 500 × 600 px, tema escuro e etapa Serviços, o DOM acessível informou que o cenário estava sem módulos e a iluminação permanecia indisponível por dependência. Mesmo assim, a interface mostrou `8 de 8 itens incluídos`. Isso confirma novamente o estado descrito em FIND-006 / issue [#209](https://github.com/EAKerber/MobiliPresenter2D/issues/209); não identifica a causa do cálculo. O menu foi fechado para a observação, nenhuma opção foi alterada e nenhum dado de conta foi registrado. A captura desta sessão não foi adicionada a `visualEvidence`; as capturas existentes permanecem referências de outros estados e resoluções.


## Observação do cabeçalho compacto atual (2026-10-18)

Na rota pública `/how-it-works/`, a sessão do navegador estava em viewport de 515 × 608 px, tema escuro. O cabeçalho em uma linha mediu aproximadamente 78 px de altura; `.brand` ocupou 160 px a partir de x=14 e `.header-actions` 140 px a partir de x=346. O grupo mostra o atalho de contato, o controle do tema representado por ícone e o menu. Essa observação não cobre os cabeçalhos privados autenticados nem comprova comportamento em outros breakpoints. O screenshot foi observado inline durante a inspeção, mas não foi persistido como imagem nesta etapa.

## Validade das capturas anteriores

O usuário observou que as capturas salvas anteriormente mostram uma versão anterior do cabeçalho. Apesar dos metadados históricos associarem essas imagens ao snapshot/deploy `298c114`, elas não devem ser usadas como referência visual atual dos cabeçalhos. Nesta continuação, o cabeçalho atual do Configurador foi observado no navegador, mas não houve substituição das capturas no repositório. A prancha de FIND-004 é um esquema experimental e não substitui capturas atuais do produto.


### Decisão compacta posterior à captura

Após a observação runtime acima, o usuário escolheu a opção A para a composição compacta de NAV-005. A escolha aprova somente a estrutura: linha única, marca com identificador/contexto à esquerda e tema antes do menu na extremidade direita; navegação e contato públicos ficam no menu. A captura em `/how-it-works/` é uma observação pública separada e não comprova os esquemas privados ou contextuais da prancha. Breakpoints e valores visuais seguem pendentes.


## Cabeçalho compacto no login administrativo (2026-10-18)

A página publicada `/admin.html` foi observada sem sessão iniciada, no tema escuro, usando leituras geométricas do DOM em larguras CSS compactas. Em 390 × 844 px, o header tinha 65,9 px de altura, marca + identificador “Administração” com 216,9 px e ações com 127,1 px, dispostos em uma linha. Em 360 × 760 px e 350 × 760 px, o header media 62 px e permanecia em uma linha. Em 340 × 760 px, 335 × 760 px e 320 × 760 px, media 104,2 px: marca/identificador na primeira linha e controles na segunda. Não houve overflow horizontal nos tamanhos verificados.

A transição observada ocorreu entre 340 e 350 px; isso não determina o breakpoint CSS exato nem recomenda um valor. O registro descreve o comportamento publicado atual, não aprova o empilhamento nem o considera uma falha. A opção A de NAV-005 aprova a estrutura compacta de uma linha; a estratégia para larguras em que marca, contexto e controles não cabem juntos continua pendente. Não foi persistida uma captura de tela desta observação; os números vieram da geometria do DOM.


### Especificação compacta estreita anterior — substituída

A versão anterior usava um limiar de 278 px internos (~306 px de viewport) e piso de uma linha de 288 px. Esses valores foram recalculados após medir os vãos entre marca, ações e header no DOM publicado. Use a especificação corrigida logo abaixo e em `decisions.json`; a versão anterior não deve ser usada como parâmetro atual.


## Validação estreita adicional do cabeçalho (2026-10-18)

O login administrativo publicado foi medido no tema escuro em 288, 306, 313, 320, 340, 350 e 360 CSS px. O header atual ocupa 104,2 px e usa duas linhas até 340 px nos pontos amostrados; em 350 e 360 px ocupa 62 px e usa uma linha. Em 320 px, marca + Administração medem 189,9 px; logo 105 px; identificador 75,9 px; grupo atual de ações 119,1 px. Em larguras até 380 px, o tema mede 74,1 × 40 px e o menu 40 × 40 px. Não houve overflow horizontal. A composição atual, portanto, não segue a linha única compacta aprovada; a medição descreve o produto, não aprova o empilhamento.

A conferência do CSSOM encontrou regras de cor específicas para claro/escuro e geometria compartilhada para este header. A geometria DOM foi medida apenas no tema escuro para não alterar a preferência persistida. Os detalhes e limites estão em [NAV-005_RUNTIME_VALIDATION_2026-10-18.md](NAV-005_RUNTIME_VALIDATION_2026-10-18.md).

A conta da recomendação anterior foi corrigida: com logo no piso (73,5 px), identificador e gaps observados, alvos recomendados de 44 × 44 px, gap de ações de 8 px, gap do header de 8 px e margens totais de 28 px, o tema rotulado cabe a partir de cerca de 321 px; icon-only é necessário em 320 px ou menos. Em icon-only, uma linha requer cerca de 291 px; abaixo disso, permitir duas linhas. São parâmetros calculados para a futura implementação, não dimensões ou breakpoints observados no produto.

## Rechecagem de contraste da legenda de estudo (2026-10-18)

Na rota publicada `/how-it-works/`, em tema escuro e viewport de 515 × 608 CSS px, a varredura DOM avaliou 161 elementos de texto usando cor computada e o ancestral opaco mais próximo. Um único par ficou abaixo de 4,5:1: `.study-art figcaption`, texto “Esquema conceitual de estudo do espaço”, `#C4BCB2` sobre `#FCF9EF`, fonte de 10,88 px, contraste **1,78:1**. Isso reproduz FIND-004, já conhecido; não é uma nova falha nem aprovação de valores. O usuário posteriormente aprovou a alternativa A: faixa opaca `#20211F` com texto `#F0EDE8` (13,85:1), registrada em VIS-003. A aplicação no produto continua pendente. Esta leitura DOM não certifica conteúdo sobre gradientes, transparência, pseudo-elementos ou imagem. Não houve alteração de tema, preferência, estado de conta ou código do produto; nenhuma captura foi persistida nesta checagem.

## Rechecagem ao vivo: cabeçalho público e sessão administrativa (2026-10-18)

**Origem observada:** navegador conectado, site publicado em `https://casaemmodulos.casa/`. O deploy atual foi confirmado como `6ad518d3da1379029e04324f`, commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a` de `main`.

### Página pública compacta

Em `/how-it-works/`, o navegador mostrou a página em viewport de 486 × 590 px. O tema escuro e o claro foram observados; a preferência foi restaurada ao escuro ao fim da comparação. O menu abriu e listou Ambientes, Como funciona e Quem somos. O atalho do WhatsApp permaneceu no cabeçalho, fora do menu, divergindo da estrutura compacta pública homologada em NAV-005, que agrupa navegação e contato dentro do menu.

O controle de tema apareceu apenas como ícone nessa largura da captura. A largura CSS efetiva não foi lida nesta sessão, portanto não classifico o ponto exato como quebra do limiar aprovado. No tema claro, a marca quase se confunde com a superfície do cabeçalho; trata-se de observação visual, sem contraste calculado no DOM e sem causa isolada (asset ou regra CSS). Esses itens estão em FIND-011/012. Nenhum valor novo foi homologado.

### Administração e gerenciamento de acessos

Em `/admin.html`, a autenticação carregou o editor sem a mensagem “Não foi possível carregar os dados administrativos”. Na primeira abertura do menu após o login, o menu ainda mostrava “Entrar na administração”, sem as rotas privadas e sem “Sair”. Recarregar a própria página sincronizou o estado; depois da recarga, o menu mostrou Configurador, Administração, Gerenciar acessos, as páginas públicas e a ação “Sair”. Essa sequência reproduz uma vez a inconsistência de sessão pós-login registrada em FIND-007 e no [backlog do produto, issue #213](https://github.com/EAKerber/MobiliPresenter2D/issues/213). Não determina sua causa nem descarta intermitência.

Em uma aba autenticada de `/access/manage`, o conteúdo carregou e o menu já apresentou corretamente os grupos público e privado e a saída. A tela contém dados de conta e de convites; nenhum valor de destinatário foi copiado para os registros desta auditoria.

### Classificação da mensagem de estado no Admin (2026-10-19)

Na página publicada `/admin.html`, em tema escuro, uma mensagem visível de estado atual tinha `aria-live="polite"` e `data-kind=""`. O usuário confirmou que ela deriva do estado atual, portanto é informação de processo e não sucesso. Na revisão VIS-002, escolheu a opção A: `#A7D1F0` sobre `#211F1C` (10,19:1) no tema escuro, e `#245D87` sobre `#F0EDE8` (6,01:1) no claro. O DOM ainda renderiza o texto escuro em `#C4BCB2` sobre `#111210`, com contraste calculado de 10,00:1: legibilidade suficiente neste par, mas o par azul aprovado não está aplicado. A decisão é contextual e não cria tokens globais. Dois outros elementos de mensagem não estavam visíveis; erro, aviso e outros estados não foram acionados. Registro detalhado em [evidência runtime](evidence/runtime/admin-dark-status-message-2026-10-19.md). Nenhuma configuração ou dado foi alterado.

### Limites e evidências

Nenhum dado do catálogo foi alterado e nenhum convite foi enviado. A comparação de tema alterou temporariamente a preferência visual. O primeiro frame após mudar para claro pareceu desbotar a marca, mas a captura estabilizada persistida em [evidência pública](visualEvidence/public/how-it-works/how-it-works-light-compact-486x590.jpg) e uma captura independente mostram a marca escura legível. Não foi confirmado defeito visual de contraste. O navegador foi restaurado ao tema escuro após a captura.

A captura pública atual estabilizada em tema claro foi persistida em `visualEvidence/public/how-it-works/how-it-works-light-compact-486x590.jpg`. As imagens antigas permanecem referências históricas. Capturas autenticadas não foram gravadas porque expõem informações de conta e acesso. A medição de contraste DOM da marca, a largura CSS real da captura compacta e a identificação dos seletores/asset permanecem pendentes.


## FIND-010 e FIND-006 — etapa Serviços no Configurador (2026-10-19)

**Rota:** `/config/` · **tema:** escuro · **viewport:** 1280 × 720.  
A página foi aberta em uma aba de leitura. Naveguei da etapa Módulos para Serviços e não alterei nenhuma opção intencionalmente.

No estado capturado em Serviços:

- O contador do viewer mostrava **8 de 8 itens incluídos**.
- As sete caixas dos módulos estavam desmarcadas (`Value=0`) na árvore de acessibilidade.
- `#lightingToggle` estava desabilitado e desmarcado. A orientação informa que é necessário incluir a lateral da geladeira e o aéreo da pia.
- A estimativa mostrava `R$ 0,00`.
- A classe do rótulo era `.service-check is-blocked`, com opacidade computada `0.6`; o controle estava `disabled=true`, `checked=false`.
- O muted escuro computado era `rgba(255, 255, 255, 0.48)`; a borda do cartão era `rgba(255, 255, 255, 0.1)`.

No snapshot AX inicial, antes de abrir Serviços, os sete controles de módulo apareciam com `Value=1`. A mudança para `Value=0` coincidiu com a navegação de etapa. A observação confirma a contradição entre contador, seleção e estimativa naquele momento, mas não determina se houve estado inicial desatualizado, reset ao trocar etapa ou outra causa; não foi verificada persistência após recarga.

A captura de tela foi examinada durante a auditoria, mas não foi adicionada como arquivo raster ao repositório. A prancha de revisão persistida em [FIND-010-disabled-control-candidates.svg](visualEvidence/experiments/FIND-010-disabled-control-candidates.svg) é uma comparação vetorial experimental, não uma captura do produto. Ela compara a opacidade atual (.6), uma alternativa menos atenuada (.78) e uma opção sem opacidade no cartão com o texto secundário da paleta aprovada. Os contrastes nela são cálculos sobre superfícies sólidas de referência; não são medições do DOM composto do site.

Nenhum estado de conta foi editado, nenhuma seleção foi salva e nenhum código do produto foi alterado.

A escolha visual de FIND-010 foi registrada após a auditoria: o usuário selecionou A, mantendo a opacidade atual de `.6` para o controle de iluminação observado. Essa decisão é contextual; o padrão geral de estados desabilitados continua pendente.


## NAV-005 e FIND-011 — cabeçalho público compacto (2026-10-19)

**Rota:** `/how-it-works/` · **tema:** claro · **viewport:** 486 × 590 CSS px. O viewport reportado pelo browser era 486 px; a largura útil do documento era 471 px devido à barra de rolagem. O header mediu 470,67 × 77,93 px.

A marca permaneceu com 160 × 57,26 px. O CTA WhatsApp mediu 38 × 38 px e ficou fora do menu. O controle de tema mediu 44 × 44 px, só com ícone, embora a marca não tivesse sido reduzida; o botão manteve nome acessível descrevendo o tema atual e o próximo. O menu abriu na primeira interação e listou Ambientes, Como funciona e Quem somos, sem link de contato.

As regras lidas nas folhas da página foram: navegação pública oculta até 900 px e exposta quando o menu abre; controle de tema do cabeçalho icon-only até 1150 px; CTA WhatsApp icon-only até 520 px. Esse resultado diverge do comportamento compacto aprovado em NAV-005. Correção registrada em [MobiliPresenter2D issue #218](https://github.com/EAKerber/MobiliPresenter2D/issues/218).

Na revisão do tema claro estabilizado, a marca ficou escura e legível. A imagem era `/branding/logo-light-380.png`, com opacidade 1 e filtro `none`. A aparência desbotada do primeiro frame não se repetiu; nenhum defeito estável foi confirmado. O contraste não textual da imagem não foi medido numericamente.

Detalhes e limites em [how-it-works-public-compact-header-2026-10-19.md](evidence/runtime/how-it-works-public-compact-header-2026-10-19.md). Não foi salvo um screenshot raster desta visita e o commit do deploy atual não foi identificado. A preferência anterior de tema escuro foi restaurada; menu fechado. Nenhuma configuração ou código do produto foi alterado.


### Follow-up responsivo — 360–290 CSS px (2026-10-19)

No tema escuro, o tema permaneceu icon-only em 360, 340, 321, 320, 291 e 290 px. A marca foi 129,6 px em 360, 122,4 px em 340 e chegou ao mínimo de 120 px em 321 px. Portanto, em 321 px o rótulo já estava oculto embora a marca estivesse reduzida somente 25% em relação aos 160 px do header compacto de 486 px.

A 291 e 290 px, `html` e `body` mantiveram `min-width: 320px` de `public-theme.css`; `.how-page` aplica `overflow-x: clip`. O header ficou em uma linha com 320 px, sem o fallback de duas linhas. A 290 px, `documentElement.clientWidth=275`, `scrollWidth=320`, e o menu começa em x=264: somente 11 px do alvo de 42 px ficam na área útil. O título também aparece cortado. Isso amplia FIND-012 e o [issue #218](https://github.com/EAKerber/MobiliPresenter2D/issues/218).

Abaixo de 291 px, o padrão aprovado permite duas linhas e requer alvos de 44 × 44 px. A verificação é observacional; ainda é necessária uma validação após a correção. Capturas raster dessa varredura não foram persistidas e larguras entre as amostras não foram medidas.


## FIND-006 e FIND-010 — resumo do Configurador (2026-10-19)

**Rota:** /config/ · **viewport:** 1280 × 720 CSS px · **temas:** claro e escuro. A observação começou em Módulos sem tocar em checkbox. Os sete controles de inclusão da lista estavam em Value=1, as linhas diziam “Incluído”, o viewer mostrava 8/8 e a estimativa R$ 8.740,00. Ao selecionar a etapa Resumo, sem alterar seleção intencionalmente, o Resumo passou a dizer “Nenhum módulo incluído”, 0 incluído(s), R$ 0,00; o viewer continuou em 8/8. A transição coincidiu com a mudança de etapa; causa não isolada. Evidência e limite em [runtime evidence](evidence/runtime/configurator-summary-label-counter-2026-10-19.md), produto [issue #209](https://github.com/EAKerber/MobiliPresenter2D/issues/209).

No mesmo Resumo, .price-state__breakdown dt usa rgba(255,255,255,.68), 11 px / peso 750, vindo de styles.css?v=runtime-v40. O fundo do cartão interno é rgba(203,188,170,.13) sobre #fff em claro e sobre #1B1C1A em escuro. Contraste composto calculado: **1,05:1 em claro** e **6,95:1 em escuro**. O rótulo quase desaparece no cartão claro; falha abaixo de 4,5:1 confirmada em DOM real, [issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208). A medição é uma verificação técnica exploratória, não certificação independente.

Nenhum módulo foi alterado nem salvo, nenhum código foi modificado e a preferência de tema escuro foi restaurada. Nenhum screenshot raster desta visita foi persistido; o commit de deploy não foi identificado.


## Reconciliação após correções publicadas (2026-10-19)

O produto avançou para o commit [483ef2e](https://github.com/EAKerber/MobiliPresenter2D/commit/483ef2e6f76a562a3096516ef68d8dfe072ec21f), publicado no Netlify deploy `6ad5a4e245dad08b373fcbd1` (`ready`). As PRs #219 e #220 corrigiram a semântica e a atualização do contador; a PR #221 conteve as camadas da cena no cartão compacto. A página e o código do produto não foram alterados durante esta auditoria.

No configurador em tema claro, viewport 516 × 800 CSS px, o primeiro estado DOM precedeu a carga assíncrona (7 módulos marcados, 7/7). Após aplicar a configuração publicada, os sete controles ficaram desmarcados e o contador passou a 0/7. Não foram feitas escolhas durante a carga; a interação antes de concluir a carga permanece fora do escopo atual por decisão do usuário.

Com o menu aberto na mesma largura, a cena não cobriu os destinos públicos; a leitura DOM confirmou `isolation: isolate` em `.viewer-card`. A captura raster foi exibida durante a revisão, mas não foi persistida nesta atualização. Issues #209 e #214 foram fechados após a validação. Evidência estruturada e limites em [PRODUCT_RECONCILIATION_2026-10-19.md](PRODUCT_RECONCILIATION_2026-10-19.md).


## Admin: formulário de login e contraste de rótulos (2026-10-19)

Acesse `/admin.html` numa janela de navegador isolada, sem sessão, para verificar o formulário de login; a captura atualizada mostra o cabeçalho privado em sua estrutura atual nos temas claro e escuro. A sessão administrativa autenticada permaneceu em outra aba e não foi encerrada. As capturas foram salvas em `visualEvidence/private/admin-login/admin-login-light-2026-10-19.svg` e `...admin-login-dark-2026-10-19.svg`; são SVGs com a captura JPEG incorporada, para preservar os pixels originais usando o fluxo de arquivos textuais do GitHub.

No editor autenticado do mesmo deploy `483ef2e6f76a562a3096516ef68d8dfe072ec21f`, viewport 1036 × 582 CSS px, a leitura de computed styles e fundo efetivo composto em sRGB mediu `.initial-state-option` (“Iniciar visível no configurador”, 10 px) em **4,22:1 no claro** e **8,36:1 no escuro**. O tema claro fica abaixo do limiar de triagem 4,5:1. Os controles “Ativa” (`.switch`, 12 px) mediram 5,22:1 e 9,11:1; `#saveMessage` (13 px) mediu 4,79:1 e 10,00:1, respectivamente. Assim, não se atribui esta falha aos outros dois pares examinados.

O achado FIND-013 foi registrado no [backlog do produto, issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208), e sua evidência detalhada está em [admin-initial-state-label-contrast-2026-10-19.md](evidence/runtime/admin-initial-state-label-contrast-2026-10-19.md). A medição é técnica e exploratória, não certificação. Nenhuma opção, dado, código ou configuração administrativa foi alterada; não houve tentativa de login ou uso de credenciais. O formulário pode ser visto nas [capturas claras e escuras](../../visualEvidence/private/admin-login/admin-login-light-2026-10-19.svg).


## Revisão do fluxo de login e sessão (2026-10-19)

Na sessão de produção autenticada pelo usuário, as chamadas de Netlify Identity para token e usuário responderam 200. Em /admin.html, o editor carregou na primeira visita; o bootstrap administrativo e as leituras de configuração responderam 200, e a mensagem de falha do issue [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212) não apareceu. Isso não reproduz nem descarta a falha intermitente.

A primeira abertura do menu na mesma página após o login continuou mostrando “Entrar na administração”, sem rotas privadas ou saída. Sem recarregar nem sair, uma navegação nova para /access/manage.html mostrou imediatamente o menu autenticado correto. Em /config/, a configuração publicada carregou sem alerta e indicou 0 de 7 módulos. Reproduções e limites estão em [auth-session-flow-2026-10-19.md](evidence/runtime/auth-session-flow-2026-10-19.md) e no [issue #213](https://github.com/EAKerber/MobiliPresenter2D/issues/213).

A inspeção do JavaScript servido encontrou cópias separadas do barramento de eventos de autenticação em core/private-navigation.bundle.js e admin/admin.bundle.js, com listas de listeners locais por módulo. A hipótese de alta confiança é que o evento emitido pelo bundle administrativo não chega ao listener do cabeçalho; a navegação nova recupera o usuário persistido. Ainda não há correção ou teste isolado, portanto a causa permanece como hipótese técnica, não resolução.

A chamada POST /api/access/session e a URL direta /.netlify/functions/access-session-status retornaram 404 com HTML, embora as rotas e a função estejam declaradas no main consultado. As chamadas equivalentes de configuração e bootstrap administrativo responderam 200. Esta falha de fallback está separada no [issue #222](https://github.com/EAKerber/MobiliPresenter2D/issues/222); não foi criada nem validada uma sessão temporária e esse 404 não explica o caso de Netlify Identity.

Nenhum e-mail, convite, configuração ou dado administrativo foi copiado para a evidência. Nenhum dado ou código de produto foi alterado. O SHA exato do deploy servido nesta visita não foi verificado independentemente.


### Análise estática do caminho de carregamento Admin (#212)

No bundle servido, o login por formulário aguarda a autenticação, obtém o JWT, grava o cookie e somente então emite o evento e retorna o usuário. O listener de autenticação também chama showUser(user), de modo que o listener e o formulário iniciam duas execuções próximas. Porém ensureAdminData mantém adminDataPromise enquanto a leitura está pendente, agrupando os pedidos a /api/admin-bootstrap; após essa leitura, ambas as execuções ainda podem chamar loadSettings.

O texto literal “Não foi possível carregar os dados administrativos.” é disparado quando /api/admin-bootstrap responde fora de 2xx. A função publicada no main consulta getUser() do Netlify Identity e distingue 401 sem usuário, 403 sem permissão e 503 se Identity estiver indisponível; o cliente não preserva essa distinção e exibe a mesma mensagem. Portanto, há concorrência de UI, mas uma corrida simples antes da gravação do cookie não é a hipótese mais forte no caminho normal do formulário, e o bootstrap é coalescido em uma única chamada. Uma divergência transitória na resolução do usuário pelo contexto Netlify continua possível, mas não foi demonstrada. Capturar status HTTP, duração e request ID sem dados pessoais/token na próxima ocorrência separaria essas hipóteses. Nenhuma instrumentação foi implantada.

## Acompanhamento de publicação do FIND-007 (2026-10-20)

A correção de sincronização de sessão foi integrada ao produto pela [PR #223](https://github.com/EAKerber/MobiliPresenter2D/pull/223), commit [`1878ae1`](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463). O deploy de produção [`6ad6c3b51b6be05647167f94`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94) está `ready` e publicou esse SHA. A verificação do menu após login não foi feita: o contexto de navegador disponível estava anônimo. FIND-007/#213 fica como correção publicada, validação autenticada pendente; sem essa validação não é marcado como resolvido.


## Auditoria runtime pública G1 (2026-10-21)

A auditoria G1 exercitou a landing pública e o painel econômico de “Como funciona” no deploy `6ad6c3b51b6be05647167f94`, commit `1878ae1057ce7c6190e0c8cb08a1f3baadd49463`. A [evidência detalhada](evidence/runtime/public-landing-g1-audit-2026-10-21.md) registra método e limites; a captura da divergência está em [visualEvidence](visualEvidence/public/landing/g1-lavanderia-selected-group1-390x844-2026-10-21.svg).

O painel econômico passou nos estados e resoluções observados. Na landing, a seleção de Lavanderia a partir do grupo 2 mudou o painel de detalhe corretamente, mas fez a paginação voltar ao grupo 1 em 4 de 4 repetições a 390×844 CSS px (FIND-016). A inspeção do código aponta uma hipótese de condição de borda fracionária em `revealCard()`; a causa ainda não foi isolada e nenhuma alteração foi feita no produto. O issue #207 cobre a indicação de disponibilidade dos viewers, não esta divergência; o defeito foi registrado separadamente no [issue #224](https://github.com/EAKerber/MobiliPresenter2D/issues/224).

O estado de `prefers-reduced-motion`, a onda de animação ativa e as falhas/rede lenta de imagem permanecem não verificados. Esta observação adiciona evidência funcional, sem decisão estética ou homologação nova.


## Auditoria runtime isolada do preview #234 (2026-10-24)

O Netlify Deploy Preview #234 estava **READY** no deploy `6adc0c519cc524d721abd893`, associado ao commit do produto `fbd00a9628c81b4902a8c679abb7ac72e93ca549`. A observação foi feita em contexto de navegador isolado, sem autenticação ou token; o conteúdo não foi alterado. A tela de acesso foi alcançada somente depois de `/config/` redirecionar para `/access/`.

| Rota | Estado observado | Resultado técnico |
|---|---|---|
| `/` | 390 × 844, tema claro, movimento reduzido | Sem overflow horizontal; 18/18 imagens enumeradas carregadas; conteúdo principal e navegação presentes. |
| `/about/` | 390 × 844, tema claro | Sem overflow horizontal; 3/3 imagens carregadas; primeiro Tab revelou o link “Pular para o conteúdo”. |
| `/how-it-works/` | 390 × 844 claro/escuro e 1366 × 900 escuro | Sem overflow horizontal; após percorrer a página, 28/28 imagens carregadas e nenhuma falha. |
| `/config/` → `/access/` | 1366 × 900, tema escuro | Redirecionamento observado; a página informou token inválido. Não havia campos de entrada visíveis nem valor de acesso fornecido. |
| `/access/` | 390 × 844 claro e 1366 × 900 escuro | Sem overflow horizontal; token inválido; nenhum campo de entrada; logo carregado. |

**Foco de teclado:** no link “Pular para o conteúdo” de `/about/`, o contorno visível foi `3px solid #6E512E` no tema claro e `3px solid #D8BC7C` no escuro, ambos com offset de 3 px. O registro aprovado do Design System especifica `#8B6A40` / `#D8BC7C`, 4 px e offset de 3 px. O preview coincide com a cor escura, mas diverge na cor clara e na espessura nos dois temas. Registra-se como diferença para reconciliação por componente, sem propor nem aplicar novo valor visual.

O browser confirmou `prefers-reduced-motion: reduce`; isso não prova por si só a interrupção de todas as animações. Não foram cobertos ordem completa de teclado, Escape/clique externo em todos os menus, falhas de imagem, rede lenta, contraste de todos os elementos, vídeo, estado autenticado ou produção. Capturas foram inspecionadas durante a sessão, mas não persistidas neste repositório. Este registro é evidência de **preview** e não atualiza a auditoria do deploy de produção nem homologa a implementação.


### Menu e teclado — observação adicional do preview (24/10/2026)

Em `/`, no viewport móvel 390 × 844 em tema escuro, o botão abriu a navegação principal (`aria-expanded=true`) e manteve foco no próprio controle. Com esse foco, Escape foi pressionado duas vezes; após cada tentativa, `aria-expanded` continuou `true` e a navegação permaneceu visível. Portanto, Escape não fechou o menu nestas duas tentativas neste preview. O fechamento por clique externo não foi concluído e permanece sem classificação. Não se infere comportamento em produção nem causa no código.


### Rastreamento da implementação do menu no preview #234 (24/10/2026)

A leitura do código da mesma head confirma o comportamento observado. O `app/index.html` do commit `fbd00a9` carrega `/landing/landing.js`, mas não solicita `/landing/header-menu.js`; o log de rede contém o primeiro arquivo e não o segundo. Em `landing.js`, o menu alterna ao clicar e fecha ao selecionar um link, mas não há listener Escape nem fechamento por `pointerdown` externo. A captura de teclado no contexto isolado confirmou que o evento `Escape` chegou ao documento, com o botão do menu como alvo, enquanto `aria-expanded` permaneceu `true`. A causa no preview fica localizada no caminho de código ativo, sem extrapolar para produção.

Há um candidato experimental já testado no produto: branch [`architecture/p-comp-01-public-menu-20261021@4ba9384`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/p-comp-01-public-menu-20261021) inclui e carrega `header-menu.js`, que fecha com Escape e clique externo e retorna foco ao controle quando pertinente. O gate [#39697470826](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39697470826) concluiu SUCCESS na head `4ba9384`. A árvore desse candidato difere de `main@15e1cfb` em 13 caminhos (2 adicionados, 1 removido e 10 modificados), incluindo `app/index.html` e outras saídas/páginas. Portanto o candidato é uma referência de comportamento, não um patch integrável diretamente: deve ser reconciliado com as fontes ARC-03C e revalidado por `pages:check`. Continua sem PR/merge/release.


## Revalidação de foco no Deploy Preview #239 — 24/10/2026

**Alvo observado:** Deploy Preview #239 de `EAKerber/MobiliPresenter2D@bf82272ba19007b65b1bd23856d182346d2fd634`, deploy Netlify `6adc7acd4f2ed8cfc213cd6f`, READY; página pública `/about/`. Este registro é de preview e não atualiza a observação de produção de 18/10 acima.

- O link “Pular para o conteúdo” recebeu foco por script no DOM e ficou visível na posição superior da página. O snapshot de acessibilidade o identificou como link focável e focado.
- Leitura de estilo computado para tema claro e escuro: contorno sólido de 4 px; cores `rgb(139, 106, 64)` (`#8B6A40`) e `rgb(216, 188, 124)` (`#D8BC7C`). A regra vencedora em `about.css` declara `outline-offset: 3px`; estilo verificado em viewport móvel 390×844, com foco visível e link dentro da tela.
- Uma captura do viewport desktop escuro confirmou visualmente o link e o contorno. O tema claro foi conferido pelo estilo computado, sem captura visual persistida. Não fizemos homologação de outros controles, rotas ou componentes.
- A implementação é local ao skip link de About e usa valores VIS-002 já aprovados. Não é evidência para tokenização ou alteração global de foco. PR #239 segue DRAFT, sem merge.


## Rechecagem de issue #224 no deploy atual (2026-10-24)

O readback do Netlify confirmou Production `READY` em `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy `6adc221479c773577ed45e23`. Em contexto de navegador isolado, tema escuro e viewport 390×844, abri o grupo 2 do carrossel e selecionei Lavanderia. O detalhe mudou para Lavanderia e o cartão selecionado permaneceu visível no grupo 2; não observei retorno ao grupo 1 nesta passagem. A captura foi inspecionada, mas não persistida. Esta é uma única não reprodução na head atual; não encerra a issue #224 nem substitui a reprodução anterior 4/4 no deploy de 21/10. Repetições e outros estados ainda faltam; nenhum estado de produto foi salvo.


## Menu público em Production — teclado, clique externo e movimento reduzido (24/10/2026)

Na Landing pública de Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`, em contexto anônimo isolado e viewport móvel 390×844, o caminho Tab → botão do menu → Enter abriu a navegação e focou “Ambientes”; dois Tabs chegaram a “Quem somos”. Escape fechou a navegação, atualizou `aria-expanded=false` e devolveu foco ao botão. Em outra abertura, um clique no conteúdo fora do menu fechou a navegação. Com `prefers-reduced-motion: reduce`, os estilos de menu/botão tinham `animation-name:none`, transição computada `1e-05s` e nenhuma animação Web estava em execução. Documento sem overflow horizontal; 17/17 imagens observadas carregadas. O clique externo atingiu uma imagem não focável e deixou o foco no body. Escopo limitado a uma rota, tema e largura; não cobre todo o percurso de teclado, todos os elementos animados, breakpoints ou temas. Evidência: [menu público em Production](evidence/runtime/public-menu-production-escape-2026-10-24.md). A observação atual não apaga o resultado distinto do preview #234.


## Link “Pular para o conteúdo” em About — foco no destino em Production (24/10/2026)

Na página pública `/about/` do deploy Production READY `6adc221479c773577ed45e23`, produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, o primeiro Tab revelou e focou o link “Pular para o conteúdo”. Ao pressionar Enter, a URL mudou para `/about/#main`, mas o elemento ativo terminou no `body`; `main#main` existe, mas não recebeu foco. Na leitura DOM, `main.tabIndex` retornou -1 sem atributo `tabindex` explícito e `scrollY` ficou em 0. A observação foi feita anonimamente, em viewport móvel 390×844, tema escuro e movimento reduzido. A aparência do anel já observada em Production continua fora da referência VIS-002; o CSS da PR #239 trata essa aparência, não a transferência de foco. Evidência e limites: [About skip link em Production](evidence/runtime/about-skip-link-production-focus-2026-10-24.md). É uma passagem sem teste de leitor de tela, outros navegadores, temas ou larguras. Nenhum código ou deploy foi alterado.


## Landing e Como funciona — link de salto em Production (24/10/2026)

Em `/` e `/how-it-works/`, no deploy READY `6adc221479c773577ed45e23`, não havia `.skip-link` nem `a[href="#main"]`; o elemento `main` não tinha id e o primeiro Tab focou a marca. Em Como funciona, a CTA `#passos` é navegação interna de seção, não salto ao conteúdo. A CSSOM da marca retornou anel computado de 2.67 px/offset 2.67 px: claro `#6E512E`, escuro `#D8BC7C`. A regra fonte `app/public-theme.css` declara 3 px/offset 3 px; `app/ui-theme.css` aplica as cores por tema. VIS-002 registra 4 px/offset 3 px, claro `#8B6A40`, escuro `#D8BC7C`. Um elemento neutro com `outline:3px` também computou 2.67 px nesta sessão; causa desconhecida. Assim, a diferença de offset não está na regra global declarada. Evidência e escopo: [Landing e Como funciona](evidence/runtime/public-skip-navigation-focus-2026-10-24.md). Uma amostra por rota; nenhuma alteração de produto.


## Anel de foco em componentes públicos — amostra Production (24/10/2026)

Na rota `/`, deploy READY `6adc221479c773577ed45e23`, dez paradas reais de Tab em 390×844 foram medidas nos temas claro/escuro: marca, CTA do header, tema, menu, CTA principal e cinco botões de ambiente. A CSSOM retornou anel de 2.67 px para os dez focos; claro `#6E512E`, escuro `#D8BC7C`; offsets computados de 2.67 px em nove focos e 2 px no tema. As regras fonte declaram 3 px global/offset 3 px e 3 px/offset 2 px no controle de tema (`app/public-theme.css` blob `e2add5053fbc1a897c035eb854b168c9711d2d18`, linha 23; `app/ui-theme.css` blob `b0f04c566183ba1f9c015f5d2a827db9e91dea45`, linhas 50 e 113–114). VIS-002 registra 4 px/offset 3 px, claro `#8B6A40`, escuro `#D8BC7C`. Um elemento neutro com `outline:3px` também computou 2.67 px; causa não identificada. Comparação normativa feita pelas declarações CSS, não pela conversão computada. [Amostra detalhada](evidence/runtime/public-focus-ring-production-component-sample-2026-10-24.md). Escopo limitado; sem mudança de produto ou token.


## VIS-002 — CSSOM do foco em Como funciona, Production (24/10/2026)

Na rota pública `/how-it-works/`, deploy Production READY `6adc221479c773577ed45e23`, produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, o botão “Compra em escala” recebeu foco real por Tab em navegador isolado e sem login. O DOM confirmou o botão como elemento ativo e `aria-expanded=false`; não foi ativado. Em tema claro, a CSSOM retornou `outline: 2px solid rgb(110, 81, 46)` (`#6E512E`), offset computado `2.66667px` (regra fonte: 3 px) e fundo da seção `rgb(37, 35, 31)` (`#25231F`). A razão calculada a partir das cores computadas foi **2,15:1**. Isso confirma em runtime o risco já previsto pela cascata para esta combinação, sem extrapolar a outros componentes. O contorno foi visualmente observado; captura não persistida. No tema escuro, o contorno foi visto, mas cor/offset CSSOM não foram medidos nesta passagem. Uma rota, um botão, um viewport; sem teste de leitor de tela ou outros navegadores. Nenhum CSS/token do produto foi alterado. [Registro detalhado](evidence/runtime/how-it-works-economy-action-focus-production-2026-10-24.md).


## Login administrativa — Production, sem autenticação (24/10/2026)

Navegar para `/access/manage.html` redirecionou a `/admin.html?returnTo=%2Faccess%2Fmanage.html`; a rota direta `/admin.html` exibiu o mesmo formulário de login. Em 1280×720, 390×844 e 320×700 CSS px, o documento ficou sem overflow horizontal e o cartão permaneceu dentro das margens observadas. No tema claro e escuro, CSSOM registrou foco no botão de tema/campo de e-mail; em 320×700 claro, o campo computou outline `2px #6E512E`/offset 3 px. Em 1280×720, as leituras incluíram larguras fracionárias de anel; a causa não foi isolada. A captura não foi persistida.

O navegador havia preenchido os campos; valores não foram lidos/registrados, os campos não foram modificados e o formulário não foi enviado. Isso documenta o estado visual de login, não comprova perfil limpo nem ausência de dados salvos. Não foi aberta área autenticada; recuperação e leitores de tela continuam sem cobertura. [Evidência detalhada](evidence/runtime/admin-login-no-session-focus-production-2026-10-24.md).
