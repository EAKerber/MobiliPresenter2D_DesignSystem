# Registro de achados e decisões

**Atualizado:** 2026-10-18  
**Produto observado:** [site publicado](https://casaemmodulos.casa/) no deploy `6ad518d3da1379029e04324f`, commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`.  
**Decisões canônicas:** [decisions.json](decisions.json). **Auditoria runtime:** [RUNTIME_AUDIT.md](RUNTIME_AUDIT.md).  
Este registro separa defeitos reproduzidos, relatos intermitentes, triagem de snapshot antigo, decisões homologadas e direções acordadas. Nenhum item aqui implementa uma correção no produto.

## Defeitos e inconsistências

| ID | Situação | Evidência / alcance | Próximo passo |
|---|---|---|---|
| FIND-001 | **Falha funcional observada em runtime** | Na landing, o primeiro clique no menu durante a abertura foi interceptado por `#introSplash`; depois que a camada saiu, o menu abriu. É uma condição pública reproduzível e não prova a causa dos relatos em páginas privadas. Backlog: [issue #215](https://github.com/EAKerber/MobiliPresenter2D/issues/215). | Corrigir ou remover a interceptação e validar NAV-004 sem regressão no fluxo da abertura. |
| FIND-002 | **Contraste abaixo do limite; par contextual homologado, ainda não aplicado** | `.hero-description`, `.how-hero-note` e texto de `.about-scale`: 4,47:1 no tema claro. Par escolhido: `#675F55` sobre `#F0EDE8`, 5,38:1 nos contextos auditados. Correção de escopo registrado em [issue #216](https://github.com/EAKerber/MobiliPresenter2D/issues/216). | Aplicar somente nos seletores/superfícies homologados; não generalizar como token global. |
| FIND-003 | **Contraste abaixo do limite; par contextual homologado, ainda não aplicado** | `.study-band .eyebrow`: 3,89:1. Par escolhido: `#70522F` sobre `#E8E3DC`, 5,60:1 nesse rótulo. Correção de escopo registrado em [issue #216](https://github.com/EAKerber/MobiliPresenter2D/issues/216). | Aplicar somente nesse contexto; manter outras superfícies e variações em aberto. |
| FIND-004 | **Contraste baixo medido; solução visual pendente** | Legenda de `.study-art` no tema escuro: `#C4BCB2` sobre ilustração clara `#FCF9EF`, 1,78:1. Não há combinação homologada para o caso. Preparação das alternativas está no [issue #217](https://github.com/EAKerber/MobiliPresenter2D/issues/217). | Comparar soluções na superfície real, medir e pedir revisão visual se a escolha estética continuar aberta. |
| FIND-005 | **Relato intermitente; não reproduzido nesta observação** | [Issue #212](https://github.com/EAKerber/MobiliPresenter2D/issues/212): após login administrativo pode aparecer “Não foi possível carregar os dados administrativos” até recarregar. Após o usuário autenticar, uma navegação nova para `/admin.html` carregou o editor; a mensagem não estava presente. Isso não reproduz o primeiro acesso pós-login nem descarta a falha intermitente. | Reproduzir desde a transição de login, inspecionar sequência de sessão e solicitação, e registrar status sem dados sensíveis. |
| FIND-006 | **Inconsistência funcional reproduzida no site publicado; contraste a reconferir** | [Issue #209](https://github.com/EAKerber/MobiliPresenter2D/issues/209): em `/config/`, a tela mostrou “8 de 8 itens incluídos” enquanto os sete módulos estavam desmarcados e a iluminação estava desabilitada por dependências. A etapa Serviços também preservou esse contador. A captura de runtime foi no tema escuro; o contraste em tema claro do issue vem de baseline estático anterior e não foi revalidado nesta sessão. | Definir o significado do contador e o que entra no total; reconciliar a causa com o snapshot atual. Depois, verificar contraste nos dois temas. Não trocar por número fixo. |
| FIND-007 | **Relato intermitente; inconsistência de sessão observada uma vez, depois navegação funcionou** | Após a autenticação, um estado anterior do menu no admin mostrou opção de entrada em vez das rotas privadas e saída. Após navegação nova, o menu abriu com Configurador, Administração, Gerenciar acessos e Sair. No configurador e em Gerenciar acessos, os grupos público/privado e Sair também apareceram. Uma observação por rota não descarta falha intermitente. Backlog: [issue #213](https://github.com/EAKerber/MobiliPresenter2D/issues/213). | Investigar sincronização de sessão/menu na transição de login e repetir a sequência em cada rota. Não atribuir ao `#introSplash` público. |
| FIND-008 | **Triagem estática antiga aberta; aplicabilidade parcial** | [Issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208) registra 8 P1, 3 P2, 1 P3 e 4 exceções no baseline `67d3197`. O contador incorreto reaparece no runtime atual; os demais itens não foram reconciliados contra `298c114`. | Conferir cada achado remanescente contra o snapshot atual e preservar as exceções editoriais, de cena e de amostras de produto justificadas. |
| FIND-009 | **Falha visual reproduzida em viewport estreito** | No configurador autenticado, com o menu público aberto, a imagem do forno da cena é pintada sobre a lista de páginas públicas e cobre parte do link “Como funciona”. Os links continuam presentes na árvore de acessibilidade. A captura foi fornecida pelo usuário e a sobreposição também foi confirmada visualmente nesta sessão; a regra/camada responsável ainda não foi isolada. Backlog: [issue #214](https://github.com/EAKerber/MobiliPresenter2D/issues/214). | Investigar contexto de empilhamento e hit testing entre cena e menu; confirmar correção em larguras estreitas e largas sem alterar os links ou a cena. |

**Leitura de prioridade:** FIND-006 é a inconsistência reproduzida de maior clareza no configurador. FIND-001 também foi observado em runtime. FIND-002/003 têm pares homologados e escopo limitado, mas seguem sem aplicação. FIND-004 requer escolha visual. FIND-005/007 continuam sem reprodução confiável da intermitência.

## Decisões homologadas

| ID | O que foi homologado | Limite |
|---|---|---|
| NAV-005 | Estrutura larga A nas páginas públicas; B nas privadas; padrão contextual tipo viewer nas navegações de segunda ordem. | Breakpoints, composições compactas, medidas e estilo visual final seguem em aberto. |
| VIS-002 | Papel azul para informação funcional/de processo; base promocional cobre `#A64D13`; pares claros exatos usados em FIND-002/003. | A base cobre não aprova automaticamente combinações; pares claros não são tokens globais nem aprovam tema escuro. |
| PRIVATE-HEADER-001 | Contrato funcional para cabeçalhos privados, grupos de navegação por acesso e ordem dos controles, conforme `decisions.json`. | Observação runtime confirma comportamento em algumas rotas/estados, mas não comprova confiabilidade após login. |

## Direções acordadas e decisões incompletas

- **EST-01–10:** direções conceituais em `decisions.json`; cores, medidas, comportamento por componente e casos limite continuam pendentes em itens específicos.
- **NAV-004:** contrato funcional do menu público definido; FIND-001 demonstra uma condição em que o primeiro clique não é atendido.
- **NAV-005:** somente a estrutura larga está aprovada; apresentação compacta e detalhes visuais permanecem pendentes.
- **VIS-001:** pendente.
- **CMP-001:** origem sem detalhe suficiente; revisão da biblioteca de componentes em andamento.
- **ENV-001:** generalização multiambiente futura, não homologada.
- **GOV-001, NAV-001 e NAV-002:** lacunas de origem encerradas como não recuperáveis; conteúdo desconhecido não foi reconstruído.

## Não verificado nesta etapa

- Causa e frequência do erro pós-login e do estado de menu desatualizado.
- Contraste do contador em tema claro no runtime atual; issue #209 tem evidência estática anterior.
- Quais achados restantes de #208 ainda se aplicam ao código/snapshot atual.
- Teclado completo, movimento reduzido e estados de hover, foco, seleção, pressionado e carregamento.
- Solução para contraste da legenda sobre ilustração clara no tema escuro.
- Não foram persistidas capturas das telas privadas autenticadas; elas contêm estado administrativo e não são necessárias para uma escolha estética nesta etapa.
