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
- **Erro, sucesso e aviso:** não generalizar cores candidatas nem usar cobre promocional como aviso técnico.

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
