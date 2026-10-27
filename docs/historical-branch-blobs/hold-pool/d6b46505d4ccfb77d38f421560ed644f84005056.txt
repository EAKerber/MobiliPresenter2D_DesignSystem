# Mapa de aplicação da paleta aprovada

**Decisão:** VIS-002 em `decisions.json`  
**Valores aprovados:** prancha [PALETTE-candidate-A-v2.svg](visualEvidence/experiments/PALETTE-candidate-A-v2.svg)  
**Produto observado:** `EAKerber/MobiliPresenter2D`, snapshot `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`, inventário de 2026-10-18.  
**Escopo deste arquivo:** relacionar valores aprovados com a implementação atual. Não altera nem autoriza alterações no repositório do produto.

## Critério de leitura

- **Aprovado:** valor e papel da paleta-base foram escolhidos pelo usuário.
- **Uso atual:** cor/token que existe no snapshot; não é homologado só por existir.
- **Mapeamento pendente:** falta definir quais variáveis/componentes recebem cada papel no produto.
- **Runtime pendente:** falta medir o DOM renderizado, os estados e os fundos compostos.

A paleta aprovada não significa que o produto já está conforme. O mesmo papel visual tem implementações duplicadas em folhas globais, administrativas e do configurador. O passo de aplicação começa pela atribuição dos tokens por família e rota, preservando diferenças funcionais e superfícies fotográficas.

## Famílias CSS de maior alcance

| Família e rotas | Origem atual no snapshot | Evidência de uso atual | Mapeamento para a paleta aprovada |
|---|---|---|---|
| Temas públicos: Landing, Como funciona e Quem somos | `app/public-theme.css` e overrides em `app/ui-theme.css` | Claro: `--public-bg #F7F5F2`, `--public-surface #FFF`, `--public-surface-soft #F0EDE8`, `--public-text #22211F`, `--public-muted #706C66`, `--public-line #DED9D2`. Escuro em `ui-theme.css`: `#111210`, `#1B1C1A`, `#20211F`, `#F4F1EB`, `#C4BCB2`, `#4A4843`. | Mapear canvas, superfície, superfície suave, texto, texto secundário e borda para os valores aprovados. Identificar exceções locais nas três folhas de rota. O valor anterior de superfície `#FFF` deve ser substituído na interface por superfície aprovada, não em assets. |
| Configurador | `app/styles.css` e `app/ui-theme.css` | Base escura: `--background #111210`, `--surface #1B1C1A`, `--surface-raised #20211F`, `--text #F4F1EB`; override claro contém `#F7F5F2`, `#FFFFFF`, `#F0EDE8`, `#22211F`, `#706C66`. Há muitas camadas semitransparentes e estados de seleção. | Consolidar os papéis base sem achatar hierarquia de módulos, estados selecionados, superfícies embutidas ou conteúdo de cena. Compor e medir as cores de fundo efetivas antes de validar contraste. |
| Viewer de ambiente | `app/viewer/viewer.css`, `app/styles.css`, `app/ui-theme.css` | Compartilha tokens e estilos de cena/configurador; declarações locais incluem fundo da cena, estrutura, hotspots e detalhe do módulo. | Reusar os papéis aprovados para interface; manter materiais, fotos, desenhos e overlays próprios do viewer fora de uma substituição global automática. |
| Administração, login e gerenciamento de acessos | `app/admin/admin.css`, `app/ui-theme.css`; páginas `admin.html`, `access/index.html`, `access/manage.html` | `admin.css` declara tema claro com `--surface #FFFFFF`, `--control-bg #FFFFFF`, `--raised #F0EDE8`, `--text #22211F`; base escura e diversos controles têm variáveis próprias. | Alinhar os neutros aprovados sem fundir papéis semânticos de formulário, disponibilidade, estado e feedback. Cores de erro/sucesso/aviso continuam por homologar. |
| Cabeçalhos e menus privados compartilhados | `app/ui-theme.css` | Fundo, borda, estado atual, hover, e-mail e ações têm declarações específicas em ambos temas. | Mapear para superfície, borda, texto secundário, foco e seleção; respeitar o contrato NAV-005 já aprovado. Visual de seleção/hover continua sem aprovação específica. |

## Alvos aprovados e atribuição ainda necessária

| Papel aprovado em VIS-002 | Valor claro / escuro | Pontos atuais a mapear | Próxima verificação |
|---|---|---|---|
| Canvas | `#E8E3DC` / `#171614` | `--public-bg`, `--background`, `--bg` | Confirmar qual superfície externa cada rota realmente usa. |
| Superfície | `#F0EDE8` / `#211F1C` | `--public-surface`, `--surface`, `--control-bg`, cartões e controles brancos | Distinguir superfície de cartão, controle e tela; conferir overlays e transparências. |
| Superfície suave | `#DED9D2` / `#2C2924` | `--public-surface-soft`, `--raised`, `--surface-raised`, áreas agrupadas | Identificar níveis de elevação/contexto que precisam preservar contraste entre si. |
| Texto principal | `#292723` / `#F0EAE1` | `--public-text`, `--text`, títulos e controles | Conferir herança, texto sobre imagens e elementos semitransparentes. |
| Texto secundário | `#705C4B` / `#C7BBAA` | `--public-muted`, `--muted`, notas, labels e descrições | Não atribuir indiscriminadamente a todo texto atenuado; medir cada fundo. |
| Borda | `#D6CCC0` / `#4E4942` | `--public-line`, `--border`, bordas opacas atuais | Rever estados de seleção/desabilitado separados. Não converter bordas alpha sem compor a superfície. |
| Foco | `#8B6A40` / `#D8BC7C` | `--ui-theme-focus`; `admin.css` tem outline literal `#E4CEB2`, 2 px, offset 3 px | Atualizar mapeamento da regra de foco ao implementar; validar teclado e contraste em cada tema/componente. A referência aprovada mostra 4 px e offset 3 px. |

## Papéis semânticos preservados

- **Informação de processo:** papel azul aprovado. Valores atuais `--info #245D87` no claro e `#A7D1F0` no escuro em `app/admin/admin.css` são uso atual, não tokens homologados.
- **Promoção de produto/campanha:** base cobre `#A64D13` aprovada. Existe em `app/how-it-works/how-it-works.css`, `.launch-badge`, como fundo. Texto, superfícies e variantes continuam pendentes.
- **FIND-004:** legenda da ilustração usa par aprovado localmente `#F0EDE8` sobre faixa `#20211F`, somente em `.study-art figcaption` no tema escuro.
- **Erro, sucesso e aviso:** pares de texto/fundo aprovados pela regra de maior contraste em cada estado e tema; valores e razão estão na [prancha de pares escolhidos](visualEvidence/experiments/VIS-002-semantic-states-selected.svg) e no bloco `selectedStatusSwatches` de `decisions.json`. Aplicação a componentes, tokens globais, ícones e superfícies compostas ainda não foi homologada. A [prancha A/B](visualEvidence/experiments/VIS-002-semantic-state-candidates.svg) continua como comparação experimental. A [prancha anterior de contraste](visualEvidence/experiments/VIS-002-contrast-options.svg) registra que o antigo par de texto secundário foi reaberto. O cobre promocional não é aviso técnico.


### Estado semântico existente na Administração

Leitura estática de `app/admin/admin.css` no snapshot `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`. “Claro/escuro atual” indica os valores declarados nos temas; não confirma o fundo efetivo no DOM.

| Papel/token atual | Claro atual | Escuro atual | Uso CSS localizado | Par de texto/fundo escolhido | Diferença / trabalho pendente |
|---|---|---|---|---|---|
| Erro · `--error` | `#A32323` | `#FFAAA0` | `.message[data-kind=error]` define apenas a cor do texto | Claro `#8E382F / #F0E5E1` · 6,17:1; escuro `#E7AAA2 / #352522` · 7,41:1 | Os dois valores de texto diferem. A regra atual não define os fundos aprovados. |
| Sucesso · `--success` | `#176344` | `#A9DDB6` | `.message[data-kind=success]` define apenas a cor do texto | Claro `#35634A / #E5ECE6` · 5,76:1; escuro `#A8CAB1 / #223129` · 7,63:1 | Os valores de texto diferem e o fundo não está definido nessa regra. |
| Aviso · `--warning` | `#795000` | `#F4CB80` | Token declarado; sem seletor consumidor encontrado nessa folha | Claro `#70531E / #EEE7D8` · 5,79:1; escuro `#E4C989 / #332C1E` · 8,56:1 | Localizar consumidores dinâmicos, sem presumir que a declaração seja usada. |
| Informação · `--info` | `#245D87` | `#A7D1F0` | Token declarado; sem seletor consumidor encontrado nessa folha | Papel azul aprovado; amostra atual sobre superfície de referência: claro 6,01:1 e escuro 10,19:1 | Valores coincidem com a referência em uso; rota, consumidor e fundo efetivo precisam de verificação runtime. |

Os pares escolhidos incluem fundos suaves específicos. Não basta substituir as variáveis de texto nas regras atuais: primeiro é necessário identificar a superfície real de cada mensagem e decidir se o componente recebe fundo semântico ou usa o texto sobre a superfície neutra. A inspeção desta folha não cobre estilo inline gerado por JavaScript nem outras folhas CSS.

## Ocorrências que exigem triagem, não substituição automática

O snapshot estático contém valores puros brancos em declarações de interface, incluindo `#FFF` (17 ocorrências) e `#FFFFFF` (5); é necessário confirmar cada ocorrência por seletor e tema. O preto puro `#000` aparece em sombras da estrutura do configurador/viewer, não como cor geral de interface no mapa extraído. Transparências de branco/preto também aparecem em bordas e overlays: devem ser compostas sobre a superfície real antes de decidir conformidade.

Fotografias, logotipos, assets de marca, ilustrações didáticas e materiais de cena não entram numa troca global de superfícies. Os fundos decorativos que pertencem a imagens devem ser avaliados como parte da imagem ou do tratamento local.

## Sequência de aplicação

1. Resolver primeiro a atribuição dos tokens de canvas/superfície/textos/bordas/foco nas quatro famílias globais acima, mantendo os papéis locais.
2. Listar em `visual-inventory.json` as ocorrências literais por seletor para cada rota e tema; separar UI sólida, alpha, imagem e material de cena.
3. Medir os pares resultantes em DOM real e verificar foco, hover, selecionado e indisponível. Valores alfa exigem composição sobre o fundo renderizado.
4. Abrir uma PR no repositório do produto por família transversal, iniciar pelos estilos compartilhados e cabeçalhos; não combinar todas as telas numa troca de busca/substituição.
5. Só depois avançar para componentes específicos e rever os estados semânticos que ainda aguardam decisão.

## Limites conhecidos

O mapa parte de inventário estático do commit indicado. Não prova que todas as regras CSS estão ativas nos estados renderizados nem que a cascata efetiva corresponde ao nome do token. A auditoria de tema claro/escuro, breakpoints, foco e estados runtime permanece necessária. Nenhuma modificação do produto foi feita nesta etapa.

## Mapeamento por seletor — primeira passada estática

Os nomes e linhas abaixo vêm do inventário do snapshot, não de uma nova auditoria runtime. “Mapear” significa determinar a atribuição do papel aprovado; não é instrução para trocar toda declaração pelo mesmo hexadecimal.

| Rota/família | Seletores e origem no snapshot | Uso atual observado | Direção do mapeamento |
|---|---|---|---|
| Landing — topo e navegação | landing.css:20-33: .site-header, navegação, .header-cta, .menu-toggle; public-theme.css:1 | Header tem branco translúcido 94%; navegação usa --public-muted; CTA usa --public-accent com texto branco. | Superfície do header deve ser mapeada para superfície por tema depois de verificar o efeito da transparência. CTA e destaque de navegação dependem de contraste de ação/estado; não inferir que todo acento vira foco. |
| Landing — conteúdo | landing.css:37-58, 98-126: .hero, .hero-description, botões, .environment-feature, .feature-availability, .story-section | Hero usa #F0EDE8; descrições --public-muted; feature usa superfície suave; status informativo usa borda/superfície/texto; seção de história usa #E8E3DC. | Vincular descrições ao secundário aprovado onde a superfície for sólida; atribuir superfícies pela hierarquia canvas/surface/soft. Preservar o status de disponibilidade separado das cores de erro/sucesso. Revisar texto branco em botão no contexto do fundo. |
| Como funciona — cartões e blocos claros | how-it-works.css:14-47, 61-67, 88-115: .story-text-section, .comparison-card, .launch-card, .module-card, .integration-callout, .quality-copy, .production-panel, .process-section | Parte usa variáveis comuns; outros fundos literais incluem #F6F1EA, #E8E3DC e #FFF. | Normalizar só superfícies de interface opacas para surface/soft/canvas após revisar hierarquia. .process-section branco é superfície authored e deve ser triado. Cartões que contêm imagem precisam preservar a área da imagem. |
| Como funciona — conteúdo informativo | how-it-works.css:6, 13, 20, 47, 51, 66, 87, 90, 101, 106-107, 114, 128: notas, parágrafos, disclaimers e listas | Mistura --public-muted, #514D48 e cores de acento; a legenda tem regra própria. | Aplicar secundário aprovado apenas a texto auxiliar sobre superfícies sólidas conhecidas; manter rótulo quente contextual #70522F onde já foi aprovado. Revalidar contrastes no DOM. FIND-004 permanece par local próprio. |
| Como funciona — promoção | how-it-works.css:41, .launch-badge | Fundo #A64D13, texto branco. | Preservar papel promocional e base de cobre homologada; medir texto/fundo e superfícies em uso. Não classificar como aviso técnico nem presumir variante dark aprovada. |
| Quem somos | about.css:1-30: .about-page, textos lead/copy, .about-scale, closing, links | Tokens --public-text, --public-muted, --public-surface, --public-surface-soft, --public-line, acentos. | Bom primeiro consumidor dos tokens partilhados: mapear superfícies e textos para papéis aprovados, conferir seletor de texto corrido FIND-002 e variáveis efetivas por tema. |
| Admin e login | admin.css:1-31, 157-210: :root, cartões, formulário, inputs, botões e mensagens; ui-theme.css:228-251 | Base e override light repetem superfícies/textos em tokens locais; --primary-text usa branco. Mensagens têm --error e --success; existem warning/info. | Alinhar base neutra; medir cada controle, foco e mensagem. Cores de estado semântico continuam pendentes, inclusive cor de texto em botão. --info segue azul processual; seus hex atuais não são tokens homologados. |
| Gerenciar acessos e header privado | ui-theme.css:259-275+: painel de acesso, .private-header, nome da página, botão de menu e grupos do menu | Usa tokens públicos com fallback literal, além de cores de hover/seleção específicas por tema. | Reusar os papéis de superfície/texto/borda/foco; testar estado ativo e hover separadamente. Contrato estrutural NAV-005 permanece aprovado, mas os detalhes cromáticos de seleção ainda não. |
| Configurador — shell e etapas | styles.css:54, 95, 112, 120, 402-447; overrides light em ui-theme.css:198-251: .topbar, foco, painéis, .flow-nav, .flow-step, cards, .module-detail | Base dark, transparências extensas para hover/seleção e múltiplos valores de cards/detalhes. Foco comum é 2 px ligado a --accent-strong; no light há superfícies #FFF e #F0EDE8. | Priorizar tokens de shell, painéis e controles primeiro. Compor todos os fundos alpha; mapear seleção separada do foco e dos estados semânticos. Revisar gradientes antes de medir contraste. |
| Viewer — cena e painel técnico | viewer.css:1-78, 106-107; overrides em ui-theme.css:143-180 | Painel usa tokens partilhados; cena/material contém claros de renderização, fundo #FFF, fotografia de foco e cores internas da ilustração técnica. | Aplicar paleta de UI em header, cartões, textos e controles. Não recolorir scene-stage, máscaras, fotografia, desenho SVG ou materiais apenas por usarem branco/preto; validar camadas de seleção/hotspot como estados próprios. |

## Prioridade proposta para a próxima aplicação

1. **Tokens compartilhados e superfícies planas:** alinhar public-theme.css e ui-theme.css nas rotas públicas e no header privado; registrar aliases necessários antes de alterar seletores locais.
2. **Quem somos e conteúdo público:** maior parte já consome tokens; conferir texto principal/secundário e superfícies claras usando as cores aprovadas.
3. **Administração e acesso:** consolidar duplicação entre admin.css e overrides ui-theme.css; deixar mensagens semânticas para a etapa de homologação de estados.
4. **Configurador/viewer:** atualizar shell/painéis mantendo superfície fotográfica e dados de cena; separar seleção, foco, hover e material de catálogo.
5. Em cada família, comparar light/dark, controles, estados de teclado e fundos alpha. Registrar as exceções por seletor e justificar por função visual.

## Pendências mantidas fora da escolha já aprovada

A paleta-base e a referência de foco estão aprovadas; o papel de uma ocorrência concreta continua dependente de contexto. Esta passada não homologa variantes do cobre, pares de erro/sucesso/aviso, cor de botão primário, hover/seleção, estados indisponíveis, alterações sobre fotografia/ilustração, ou efeitos de alpha/gradiente. Os valores atuais permanecem documentados como uso atual até que o seletor seja atribuído e medido.
