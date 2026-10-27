# Baseline DOM × CSS e oportunidades de consolidação (2026-10-20)

> **Status:** análise estática preliminar, não homologação e não implementação.  
> **Fonte:** `visual-inventory.json`, `DECISION_APPLICATION_MAP.md`, `FINDINGS_REGISTER.md`, `PALETTE_APPLICATION_MAP.md`, `runtime-evidence.json` da `main` de `EAKerber/MobiliPresenter2D_DesignSystem`, commit `507be364c29d83bda8ed6c772b330ee66122eb44`.  
> **Produto representado pelo inventário estático:** `EAKerber/MobiliPresenter2D` no commit `483ef2e6f76a562a3096516ef68d8dfe072ec21f`. Este registro **não consulta nem altera** o repositório de produto e não presume divergências visuais causadas pelas correções posteriores de autenticação/backend.

## Conclusão inicial

O produto apresenta **80 nomes de classes encontrados em mais de um dos oito arquivos CSS rastreados**. Isso mede compartilhamento lexical, **não** quantidade de colisões em runtime: folhas podem não ser carregadas juntas, regras podem ter escopo distinto e sobrescritas temáticas podem ser intencionais. O inventário cobre oito páginas HTML e oito folhas CSS; markup gerado por JavaScript, cascade computada e estados autenticados exigem um segundo estágio de auditoria.

### Matriz de carregamento por rota e cobertura lexical do HTML estático

As contagens abaixo vêm da interseção entre classes estáticas HTML e classes registradas nas folhas **efetivamente carregadas** por rota, conforme `DECISION_APPLICATION_MAP.md`. Ausência na interseção **não** comprova falta de estilo: há tags, IDs, atributos, herança, classes dinâmicas e seletores combinados.

| Rota | CSS carregado (nomes abreviados) | Classes HTML distintas | Nomes presentes nas folhas | Não encontrados por nome no CSS carregado |
|---|---|---:|---:|---|
| `/` | public-theme, landing, ui-theme | 36 | 33 | environment-art--feature; environment-browser; feature-availability |
| `/how-it-works/` | public-theme, landing, how-it-works, ui-theme | 89 | 86 | comparison-brand-logo; comparison-illustration; study-space-illustration |
| `/about/` | public-theme, landing, about, ui-theme | 27 | 27 | — |
| `/viewer/` | public-theme, viewer, ui-theme | 9 | 9 | — |
| `/config/` | styles, ui-theme | 72 | 69 | module-stage-pane--list; private-header--config; service-section |
| `/admin.html` | admin, ui-theme | 48 | 46 | is-active; object-tab-panel |
| `/access/` | public-theme, ui-theme | 10 | 8 | access-private-header; back |
| `/access/manage.html` | public-theme, ui-theme | 18 | 14 | access-private-header; intro; secondary; toolbar |

**Limitação importante:** `/viewer/` tem somente nove nomes de classe no HTML estático, apesar de uma interface dinâmica extensa. Não concluir cobertura do Viewer nem duplicações de DOM com base apenas no HTML fonte. A inspeção dinâmica do JS/DOM renderizado é indispensável.

### Colisões de nome — classificação por intenção

| Padrão | Evidência CSS | Interpretação preliminar | Ação proposta |
|---|---|---|---|
| Mesmo nome, contratos diferentes: `.module-card` | `how-it-works.css`: flex, disposição editorial, fundo `#f6f1ea`; `styles.css`: grid interativo, 44px + conteúdo, feedback de seleção | **Homonímia semântica**; as duas folhas não se sobrepõem no carregamento atual | Renomear/scopear distintamente quando houver extração, sem fundir num único componente |
| Mesmo nome, várias bases: `.button` | `landing.css`: 46px, raio 3px, uppercase; `admin.css`: 40px, raio 9px; `styles.css`: 36px, raio 9px | Bases de botão com contratos e estéticas diferentes; carregadas em grupos de rotas separados | Definir primitiva funcional e variantes contextuais, preservar diferenças homologadas |
| Mesmo nome, papéis distintos: `.brand` | `landing.css`: largura e `display:block`; `admin.css` e `styles.css`: alinhamento `flex` e gap | Acoplamento entre arte da marca e slot/layout do cabeçalho | Separar logo/asset e container/posicionamento por header |
| Mesmo papel, variação intencional: `.eyebrow` | `admin.css` e `landing.css` têm pequenas diferenças de fonte, spacing e paleta; `about`/`how-it-works` refinam em contextos | Tipografia recorrente, mas dependente de superfícies e temas | Definir família tipográfica e variantes contextuais sem impor cores únicas |
| Mesmo comportamento e declarações: `.scene-hotspot` | `styles.css` e `viewer.css`: `position:absolute`, min-size 28px, border 0, padding 0, background transparent, cursor pointer | Forte candidato para compartilhamento entre cena do Configurador e Viewer | Extrair base após conferir DOM, foco, hit target e overrides por estado |
| Utilitário duplicado: `.visually-hidden` | Regras coincidentes em `admin.css` e `styles.css` | Utilitário de acessibilidade com semântica única | Centralizar uma vez, sem alterar especificidade e !important antes de testar |

### Declarações semelhantes com nomes diferentes

A comparação de regras base (sem media queries, sem selectores agrupados) encontrou equivalência **exata de quatro declarações** entre `.how-hero-art img` (`how-it-works.css`) e `.hero-art img` (`landing.css`): `position`, `width`, `height` e `object-fit`. É possível extrair o tratamento **de mídia**, mas não implica que os dois heros sejam um mesmo componente.

Outras similaridades observadas são **parciais**: `.brand__logo` (`admin.css`) e `.private-header__brand img` (`ui-theme.css`) compartilham quatro de cinco pares propriedade/valor; `.viewer-brand__logo` e `.private-header__brand img` também compartilham quatro de cinco. Isso recomenda uma primitiva de imagem de marca com dimensões e limites definidos pelo slot, não uma substituição global de seletores.

A semelhança entre `.admin-heading__meta` e `.configuration-value` (quatro propriedades coincidentes) pode ser simplesmente convenção de layout/typography, não um componente. Não criar abstrações apenas por coeficiente de similaridade.

## Co-carregamento importa mais que repetição de classe

- Landing: 10 nomes aparecem em mais de uma folha carregada; oito também constam no HTML estático, entre `site-header`, `header-cta`, `eyebrow` e botões temáticos.
- Como funciona: 27 nomes aparecem em mais de uma folha carregada, incluindo ênfase em `study-*`, `process-*`, `site-header` e `eyebrow`. O arquivo `ui-theme.css` participa de muitos overrides.
- Quem somos: 10 nomes se repetem entre folhas carregadas; o cabeçalho público é um compartilhamento intencional.
- Viewer: 10 nomes, com `viewer-header`, `technical-view`, `eyebrow` e outras regras temáticas; boa parte do DOM é gerada.
- Configurador: 18 nomes, incluindo `flow-*`, `panel`, `price-state` e `topbar`.
- Administração: 18 nomes, incluindo `admin-*`, `data-field`, `button--*` e `text-button`.
- Acesso e Gerenciar acessos: nenhuma classe repetida entre `public-theme.css` e `ui-theme.css` na extração; as páginas ainda podem depender de atributos/IDs e conteúdo dinâmico.

**Atenção:** os totais acima são classes lexicalmente repetidas entre arquivos carregados, não elementos DOM em conflito. Os exemplos `.button` e `.module-card` têm maior risco **futuro** caso todas as folhas sejam globalizadas sem escopo. Já `ui-theme.css` exige rastreio de proveniência e da cascata **atual**.

## Modelo de evidência para a próxima etapa

Cada possível componente/estilo terá registro com: `route`; `state` (anônimo/autenticado, conteúdo, loading/erro, seleção); `theme`; `viewport`; `domPath` ou assinatura estrutural sem dados pessoais; `classes`; `matchingSelectors`; `stylesheet`+linha e contexto `@media`; `computedValues` apenas de propriedades relevantes; `role` semântico; `decisionIds`; `candidateOwner`; `collisionType` (`same-name-different-contract`, `different-name-same-contract`, `theme-override`, `utility-duplicate`, `intentional-page-variation`); `confidence` (`static`, `dom`, `visual`, `functional`); `action` e `verification`.

A matriz representativa deve amostrar os dois temas, larguras de risco (incluindo compacto e muito estreito), estados anon./autenticado, fluxo de menu/cabeçalho, Viewer carregado, Configurador com interação, Admin e formulário. Não usar produto cartesiano completo sem evidência de risco. DOM estático, inspeção visual e teste funcional são três verificações distintas.

## Critérios de exclusão do dedupe automático

1. Não unificar homônimos que representam funções diferentes (por exemplo, cartões editorial × configurador).
2. Não generalizar pares cromáticos contextuais para tokens globais (VIS-002/VIS-003); não recolorir cena, ilustrações e assets.
3. Não classificar um seletor como morto por não aparecer no HTML fonte; procurar criação dinâmica, `classList`, templates e estados de sessão.
4. Não alterar `@media`, prioridade de origem, especificidade, `!important`, `@layer` nem escopo ao extrair sem snapshot comparativo.
5. Não tratar markup com classe sem seletor próprio como elemento sem estilo.
6. Não atribuir problemas de estilo às mudanças lógicas recentes sem evidência.
7. Preservar `decisions.json` como autoridade para homologação; este documento contém hipóteses de arquitetura, não decisões aprovadas.

## Gate para considerar o mapeamento DOM completo

Cobertura de classes/seletores do DOM **renderizado** nas oito rotas e nos estados críticos; resolução de origem/cascata e custom properties; mapa de classes dinâmicas; comparação light/dark e largura; separação explícita de duplicação legítima/ambiguidade/acoplamento; nenhuma afirmação de conformidade baseada somente na estrutura textual das regras. O trabalho está **iniciado**, não passou este gate.
