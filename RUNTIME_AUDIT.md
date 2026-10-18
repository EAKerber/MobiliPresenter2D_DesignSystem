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

Os três primeiros pares estão próximos do limite de 4,5:1, mas continuam abaixo dele. A legenda da ilustração é o caso mais evidente: a superfície clara da figura persiste no modo escuro, enquanto a legenda muda para um tom claro. O registro é de falha/candidato técnico no contexto observado; qualquer ajuste de cor deve respeitar a direção homologada e passar por revisão visual quando houver mais de uma solução.

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
2. NAV-005 agora aprova a estrutura larga: padrão A para páginas públicas, B para privadas e header contextual tipo viewer para páginas de segunda ordem. Estética final, medidas e layouts compactos continuam em aberto.
3. Revalidar a camada de introdução e o primeiro clique no menu público como comportamento funcional, sem confundir esse achado com a navegação privada.
4. Reproduzir a transição pós-login e reconciliar a triagem estática #208 com o snapshot atual; a primeira inspeção autenticada confirmou o contador incorreto, mas não substitui a auditoria de contraste nos dois temas.
5. Planejar a etapa de aplicação visual no produto após revisar os padrões e fechar as medições restantes.


## Reconciliação da triagem estática DS-04

O issue [#208 do produto](https://github.com/EAKerber/MobiliPresenter2D/issues/208) foi atualizado após comparar seu baseline `67d3197` com o snapshot de produção `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`. No código, DS04-01 (carregamento do tema em `/access/`) e DS04-08 (fundo/texto do dock em tema claro) estão resolvidos. Permanecem candidatos estáticos DS04-02 a DS04-07, DS04-09, DS04-10 e DS04-12; DS04-11 está documentado como exceção técnica intencional. Essa reconciliação não inclui medidas runtime de contraste para cada seletor; os valores do relatório original continuam sendo medições do baseline, não do DOM atual. Veja a classificação detalhada no issue #208 e o [registro de achados](FINDINGS_REGISTER.md).
