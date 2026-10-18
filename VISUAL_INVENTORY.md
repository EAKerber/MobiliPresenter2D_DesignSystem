# Inventário visual estático

**Snapshot:** 2026-10-18  
**Produto observado:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D), `main` em `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`.  
**Registro:** `decisions.json`; detalhes por regra e rota em [`visual-inventory.json`](visual-inventory.json).  
**Escopo:** CSS, marcação HTML estática e arquivos de imagem/vetor/fontes. Este inventário não altera o produto nem certifica o comportamento renderizado.

## Resumo do inventário

| Área | Registro estático |
|---|---:|
| Entradas HTML mapeadas | 8 |
| Folhas CSS mapeadas | 8 |
| Nomes de classe encontrados no CSS | 426 |
| Nomes de classe em marcação HTML | 251 |
| Custom properties CSS | 43 |
| Ocorrências de cores literais | 459 |
| Valores literais distintos | 235 |
| Declarações de espaçamento | 750 |
| Declarações CSS de movimento | 36 |
| Keyframes | 8 |
| Arquivos visuais rastreados em `app/` | 128 |

Os seletores e declarações visuais são preservados por folha CSS, com regra, contexto `@media` e linha de origem no JSON. A leitura é lexical: aliases de cor ou classe podem ser usados em runtime, e a cascata final depende de DOM, ordem de importação e estado da aplicação.

## Rotas e decisões relacionadas

| Superfície | Entrada | Decisões mapeadas |
|---|---|---|
| Landing / ambientes | `app/index.html` | NAV-003, NAV-004, NAV-005, VIS-002 |
| Como funciona | `app/how-it-works/index.html` | NAV-003, NAV-004, NAV-005, VIS-002 |
| Quem somos | `app/about/index.html` | NAV-003, NAV-004, NAV-005, VIS-002 |
| Viewer de ambiente | `app/viewer/index.html` | NAV-003, NAV-004, NAV-005, VIS-002, EST-01–03 |
| Configurador | `app/config/index.html` | NAV-003/004, PRIVATE-HEADER-001, VIS-002, EST-01–06 |
| Administração / login | `app/admin.html` | PRIVATE-HEADER-001, VIS-002, EST-02, EST-04–10 |
| Login de acesso | `app/access/index.html` | PRIVATE-HEADER-001, VIS-002 |
| Gerenciar acessos | `app/access/manage.html` | PRIVATE-HEADER-001, VIS-002, EST-02, EST-04–06 |

## CSS, classes e estilos locais

| Folha | Nomes de classe encontrados | Observação |
|---|---:|---|
| `app/about/about.css` | 19 | Layout editorial e capítulos |
| `app/admin/admin.css` | 110 | Formulários, hierarquia, estados e editor administrativo |
| `app/how-it-works/how-it-works.css` | 82 | Conteúdo editorial, comparações e ilustrações |
| `app/landing/landing.css` | 41 | Landing, header público, cards e menu |
| `app/public-theme.css` | 0 | Base pública e regra global de movimento reduzido |
| `app/styles.css` | 130 | Configurador e parte do viewer |
| `app/ui-theme.css` | 86 | Controle de tema e adaptações por contexto |
| `app/viewer/viewer.css` | 48 | Viewer e cena |

Nomes iguais não asseguram estilo comum: regras locais e contexto alteram o resultado. Três páginas mantêm blocos `<style>` inline: `app/access/index.html` (996 bytes), `app/access/manage.html` (2.191 bytes) e `app/config/index.html` (432 bytes). Há ainda quatro atributos `style` em elementos de quatro páginas, incluindo `app/admin.html`; o JSON registra seus seletores/elementos e declarações. O HTML e CSS completos, com seletores, propriedades visuais e referências de assets, estão no JSON.

## Cores e semântica

- **Base promocional terciária aprovada:** `#A64D13` para informação promocional de produto, campanhas e condições comerciais. Essa aprovação não fixa variantes por tema/superfície nem os pares de contraste. A regra `.launch-badge` em `app/how-it-works/how-it-works.css` já usa esse valor; isso é evidência de implementação atual, não aprovação automática de outros usos. O uso comercial não deve ser rotulado como `warning` técnico.
- **Informação de processo aprovada:** usar o azul homologado para orientações sobre funcionamento/processo. Essa categoria não é aviso, erro nem confirmação de sucesso. A administração atualmente define `--info` como `#245d87` no tema claro e `#a7d1f0` no escuro; o mapeamento das ocorrências no produto e a validação em DOM real ficam para a auditoria visual/runtime.
- **Outras cores no CSS:** uso atual observado, não aprovação automática de tokens. A imagem de estados semânticos continua sendo referência candidata para erro, sucesso e aviso.
- A extração encontrou 459 ocorrências de cores literais e 43 custom properties. Não foi encontrado um namespace explícito `--space-*` / `--spacing-*`; o espaçamento está expresso em declarações CSS.

## Responsividade, espaçamento e tipografia

Foram encontrados limites `max-width` em 13 valores: **360, 380, 400, 420, 480, 520, 650, 680, 700, 760, 900, 980 e 1150 px**, além de condições de orientação e regras de movimento reduzido. Há limites equivalentes com espaçamento/formatação diferente e três regras móveis repetidas na folha de administração. Isso é evidência para mapear; não indica que os limites devam ser unificados antes de revisar o layout.

O JSON registra valores e contexto para margin/padding/gap, tipografia, dimensões, grid/flex, bordas, raios, sombras, foco e superfícies. Existem 750 declarações de espaçamento contabilizadas, sem escala única nomeada descoberta nesta leitura.

## Movimento e microinterações

Foram localizadas 36 declarações de `transition`, `animation` ou `scroll-behavior` e oito `@keyframes`. Regras explícitas de `prefers-reduced-motion` aparecem em quatro folhas: `how-it-works.css`, `landing.css`, `public-theme.css` e `styles.css` (duas regras nesta última). A cobertura efetiva depende de quais folhas cada rota carrega; isso será verificado na etapa de navegador, junto de estados hover, foco, pressionado e seleção.

## Assets e ícones

Os 128 arquivos rastreados se agrupam em 46 itens de cena/máscaras do configurador, 9 texturas de materiais, 8 arquivos de marca, 31 imagens/ilustrações de “Como funciona”, 26 assets da landing, 1 placeholder do viewer e 7 imagens em `app/reports` e `app/tools`. O JSON registra cada caminho, extensão e referência encontrada em HTML/CSS. Ausência de referência estática significa **não verificado**, não “sem uso”; referências dinâmicas em JavaScript pertencem ao inventário futuro do código.

## Método e limites

- Snapshot estático do commit indicado, sem alterações ao repositório do produto.
- Seletores, valores e classes foram extraídos de CSS/HTML; não foi executada a aplicação em navegador nesta etapa.
- Não foram calculados contrastes, avaliados screenshots, inferidos estados gerados por JavaScript nem declarados assets como órfãos.
- As capturas e auditoria de DOM real serão uma etapa própria; só serão preparadas imagens para revisão quando restar uma escolha visual não determinada pelas decisões.
- Este inventário documenta o estado observado. A aprovação explícita de `#A64D13` está registrada separadamente em `decisions.json`; presença de outras cores ou métricas no código não as transforma em tokens homologados.
