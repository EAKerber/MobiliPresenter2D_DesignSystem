# Auditoria visual em runtime

**Observação:** 2026-10-18  
**Site observado:** [casaemmodulos.casa](https://casaemmodulos.casa/)  
**Snapshot estático relacionado:** `EAKerber/MobiliPresenter2D` `main` em `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`, conforme inventário da etapa anterior.  
**Deploy de produção verificado:** `6ad518d3da1379029e04324f`, pronto em 2026-10-18, commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a` ([commit do produto](https://github.com/EAKerber/MobiliPresenter2D/commit/298c11441f82cacfff2f809fd9e5ad6f1fc33c0a)).  
**Decisões:** `decisions.json` continua sendo a fonte canônica.

## Escopo e método

Inspeção somente de leitura no site publicado, cobrindo páginas públicas e a tela de login administrativo. Foram observados DOM, tema, largura do documento, cabeçalhos, comportamento do menu e alguns pares de contraste em superfícies sólidas. A medição de contraste usa cores computadas pelo navegador e luminância relativa; é uma triagem técnica, não uma certificação WCAG nem aprovação visual.

Nenhum código do produto foi alterado. Não houve tentativa de login, envio de link, acesso a dados privados ou execução de testes automatizados. As capturas públicas persistidas como JPEG em 1265 × 712 são: [landing claro](visualEvidence/public/landing/landing-light.jpg), [landing escuro](visualEvidence/public/landing/landing-dark.jpg) e [viewer escuro](visualEvidence/public/viewer/viewer-dark.jpg). Elas documentam rotas públicas, portanto não demonstram o cabeçalho privado atualizado. Para isso, foram adicionadas capturas do login administrativo em 1280 × 720: [claro](visualEvidence/private/admin-login/admin-login-light.jpg), [escuro](visualEvidence/private/admin-login/admin-login-dark.jpg) e [menu escuro aberto](visualEvidence/private/admin-login/admin-login-menu-dark.jpg). Todas correspondem ao deploy de produção acima; são referências do estado publicado, não propostas homologadas. O conjunto original mostrado inline em 1440 × 900 permanece distinto destas capturas.

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

### Rotas protegidas

O acesso sem sessão não expôs o configurador nem o gerenciamento de acessos. As páginas que dependem dessas áreas ficam **não verificadas em runtime autenticado**; nenhuma conclusão sobre seus cabeçalhos, controles ou dados privados é inferida do redirecionamento.

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

A amostra promocional atual confirma que branco sobre a base aprovada `#A64D13` funciona neste componente e nesta superfície. Isso não homologa o uso em outros fundos, tamanhos de texto ou temas. A tela autenticada de administração — incluindo as opções mostradas no inventário estático — não pôde ser medida.

## Automação de contraste

O inventário estático não encontrou um gate de contraste conectado às rotas do produto. Os contrastes acima foram medidos nesta inspeção, não detectados por um workflow de CI. A auditoria fixture descrita no histórico do Design System não é evidência de cobertura completa do DOM de produção.

## Estados não verificados

- Administração autenticada, gerenciar acessos e convites, configurador e estados dinâmicos protegidos.
- Teclado completo do menu: Escape, clique fora, retorno de foco e ordem de tabulação.
- Preferência de movimento reduzido no navegador e efeitos runtime correspondentes.
- Estados de foco, hover, pressionado, seleção e carregamento para todas as famílias.
- Contraste de textos sobre imagens, gradientes, pseudo-elementos e camadas transparentes; leituras automáticas nesses contextos podem produzir falsos positivos.

## Próxima etapa recomendada

1. VIS-002 agora registra dois pares contextuais aprovados para texto no tema claro; não são tokens globais e não resolvem os achados do tema escuro.
2. NAV-005 agora aprova a estrutura larga: padrão A para páginas públicas, B para privadas e header contextual tipo viewer para páginas de segunda ordem. Estética final, medidas e layouts compactos continuam em aberto.
3. Revalidar a camada de introdução e o primeiro clique no menu público como comportamento funcional, sem confundir esse achado com a navegação privada.
4. Repetir a auditoria autenticada quando houver sessão permitida para observar o painel e o gerenciamento de acessos.
5. Planejar a etapa de aplicação visual no produto após revisar os padrões e fechar as medições restantes.
