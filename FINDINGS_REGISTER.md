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
| FIND-004 | **Contraste baixo medido; tratamento visual B escolhido, valores e correção pendentes** | Legenda de `.study-art` no tema escuro: `#C4BCB2` sobre ilustração clara `#FCF9EF`, 1,78:1. O usuário escolheu faixa escura na base da ilustração para manter a legenda integrada. Cores e opacidade da faixa ainda não foram homologadas. Preparação das alternativas está no [issue #217](https://github.com/EAKerber/MobiliPresenter2D/issues/217). | Medir e homologar a combinação final no DOM real; implementar e revalidar contraste, responsividade e legibilidade da arte. Não generalizar a escolha para outros contextos.
| FIND-005 | **Relato intermitente; não reproduzido nesta observação** | [Issue #212](https://github.com/EAKerber/MobiliPresenter2D/issues/212): após login administrativo pode aparecer “Não foi possível carregar os dados administrativos” até recarregar. Após o usuário autenticar, uma navegação nova para `/admin.html` carregou o editor; a mensagem não estava presente. Isso não reproduz o primeiro acesso pós-login nem descarta a falha intermitente. | Reproduzir desde a transição de login, inspecionar sequência de sessão e solicitação, e registrar status sem dados sensíveis. |
| FIND-006 | **Inconsistência funcional reproduzida no site publicado; contraste a reconferir** | [Issue #209](https://github.com/EAKerber/MobiliPresenter2D/issues/209): em `/config/`, a tela mostrou “8 de 8 itens incluídos” enquanto os sete módulos estavam desmarcados e a iluminação estava desabilitada por dependências. A etapa Serviços também preservou esse contador. A captura de runtime foi no tema escuro; o contraste em tema claro do issue vem de baseline estático anterior e não foi revalidado nesta sessão. | Definir o significado do contador e o que entra no total; reconciliar a causa com o snapshot atual. Depois, verificar contraste nos dois temas. Não trocar por número fixo. |
| FIND-007 | **Relato intermitente; inconsistência de sessão observada uma vez, depois navegação funcionou** | Após a autenticação, um estado anterior do menu no admin mostrou opção de entrada em vez das rotas privadas e saída. Após navegação nova, o menu abriu com Configurador, Administração, Gerenciar acessos e Sair. No configurador e em Gerenciar acessos, os grupos público/privado e Sair também apareceram. Uma observação por rota não descarta falha intermitente. Backlog: [issue #213](https://github.com/EAKerber/MobiliPresenter2D/issues/213). | Investigar sincronização de sessão/menu na transição de login e repetir a sequência em cada rota. Não atribuir ao `#introSplash` público. |
| FIND-008 | **Triagem estática antiga aberta; aplicabilidade parcial** | [Issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208) registra 8 P1, 3 P2, 1 P3 e 4 exceções no baseline `67d3197`. A reconciliação do snapshot `298c114` está registrada no issue #208: DS04-01 e DS04-08 foram resolvidos no código; DS04-02 a DS04-07, DS04-09, DS04-10 e DS04-12 continuam com evidência estática de risco; DS04-11 está explicitado como exceção técnica. Os itens restantes aguardam inspeção DOM/runtime. | Aplicar os itens remanescentes por grupos após revisão e medir o DOM final; preservar as exceções editoriais, de cena e de amostras de produto justificadas. |
| FIND-009 | **Falha visual reproduzida em viewport estreito** | No configurador autenticado, com o menu público aberto, a imagem do forno da cena é pintada sobre a lista de páginas públicas e cobre parte do link “Como funciona”, tanto no tema escuro quanto no claro. Os links continuam presentes na árvore de acessibilidade. A causa CSS/DOM ainda não foi isolada. Backlog: [issue #214](https://github.com/EAKerber/MobiliPresenter2D/issues/214). | Investigar contexto de empilhamento e hit testing entre cena e menu; confirmar correção em larguras estreitas e largas sem alterar os links ou a cena. |
| FIND-010 | **Legibilidade baixa observada em tema claro; revisão visual pendente** | No Resumo do Configurador, o rótulo “Módulos” (`.price-state__breakdown dt`) aparece quase ilegível no cartão claro. Observação visual no site publicado; sem medida numérica nova. A opção de iluminação desabilitada também parece muito apagada, mas é estado indisponível por dependência e não é classificada automaticamente como falha WCAG. Backlog: [issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208). | Corrigir o rótulo já identificado em DS04-07; avaliar separadamente o nível de atenuação do controle indisponível, preservando sua distinção de estado. |

**Leitura de prioridade:** FIND-006 é a inconsistência reproduzida de maior clareza no configurador. FIND-001 também foi observado em runtime. FIND-002/003 têm pares homologados e escopo limitado, mas seguem sem aplicação. FIND-004 tem o tratamento visual escolhido; valores finais e implementação permanecem pendentes. FIND-005/007 continuam sem reprodução confiável da intermitência.

## Decisões homologadas

| ID | O que foi homologado | Limite |
|---|---|---|
| NAV-005 | Estrutura larga A nas páginas públicas; B nas privadas; padrão contextual tipo viewer nas navegações de segunda ordem. Em compacto, opção A: linha única, marca e identificador/contexto à esquerda, tema antes do menu na extremidade direita; páginas públicas agrupam navegação e contato no menu. | Regra para larguras muito estreitas aprovada: manter rótulo do tema enquanto a logo reduz até 30%, depois usar controle icon-only; identificador permanece completo. Breakpoint exato, dimensões, espaçamento, tipografia, cores e glifo seguem em aberto. |
| VIS-002 | Papel azul para informação funcional/de processo; base promocional cobre `#A64D13`; pares claros exatos usados em FIND-002/003. | A base cobre não aprova automaticamente combinações; pares claros não são tokens globais nem aprovam tema escuro. |
| PRIVATE-HEADER-001 | Contrato funcional para cabeçalhos privados, grupos de navegação por acesso e ordem dos controles, conforme `decisions.json`. | Observação runtime confirma comportamento em algumas rotas/estados, mas não comprova confiabilidade após login. |

## Direções acordadas e decisões incompletas

- **EST-01–10:** direções conceituais em `decisions.json`; cores, medidas, comportamento por componente e casos limite continuam pendentes em itens específicos.
- **NAV-004:** contrato funcional do menu público definido; FIND-001 demonstra uma condição em que o primeiro clique não é atendido.
- **NAV-005:** estruturas largas e compacta A estão aprovadas, incluindo regra de logo até -30% e tema icon-only após o limite; breakpoint e detalhes visuais permanecem pendentes.
- **VIS-001:** pendente.
- **CMP-001:** origem sem detalhe suficiente; revisão da biblioteca de componentes em andamento.
- **ENV-001:** generalização multiambiente futura, não homologada.
- **GOV-001, NAV-001 e NAV-002:** lacunas de origem encerradas como não recuperáveis; conteúdo desconhecido não foi reconstruído.

## Não verificado nesta etapa

- Causa e frequência do erro pós-login e do estado de menu desatualizado.
- Contraste do contador em tema claro no runtime atual; issue #209 tem evidência estática anterior.
Contraste no DOM final dos achados restantes de #208; a reconciliação atual é estática e não inclui medição DOM por seletor.
- Teclado completo, movimento reduzido e estados de hover, foco, seleção, pressionado e carregamento.
- Cores e opacidade/gradiente finais da faixa da legenda, após a escolha de composição em FIND-004.
- Não foram persistidas capturas das telas privadas autenticadas; elas contêm estado administrativo e não são necessárias para uma escolha estética nesta etapa.
