# P0 — Auditoria de ownership de DOM, JS, schemas e CSS

**Data:** 2026-10-20 · **Status:** P0 estático documentado / validação de DOM renderizado P0-R pendente.  
**Produto lido:** `EAKerber/MobiliPresenter2D@1878ae1057ce7c6190e0c8cb08a1f3baadd49463`, branch `main`. Somente leitura.  
**CSS/HTML de referência:** `visual-inventory.json` do Design System (ver `snapshot.productCommit`) e [crosswalk estático](dom-css-static-crosswalk-2026-10-20.json).  
**Política:** a presente evidência não substitui teste funcional, inspeção visual nem DOM/computed styles em navegador real.

## Superfícies e titulares de cada etapa

| Rota / região | Fonte/contrato dominante | Quem constrói o DOM | Componentes e CSS principais | Estado/controle | Decisão inicial |
|---|---|---|---|---|---|
| `/` Landing | [`landing/data.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/landing/data.js): `CASA_PUBLIC_LANDING` com ambientes e benefícios | [`landing/landing.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/landing/landing.js), `renderBenefits`/`renderCards`; o shell e header são HTML | `.benefit-item`, `.mini-benefit`, `.environment`, `.environment-art`; `landing/landing.css`+`ui-theme.css` | seleção, carrossel, pré-decodificação de imagem, animação/reduced motion | **Piloto preferido** em faixa `.benefit-item` — isolada de outros domínios |
| `/how-it-works/` | conteúdo editorial hoje em HTML | [`how-it-works/index.html`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/how-it-works/index.html), com várias seções/details; comportamento de menu por JS transversal | `.foundation-item`, `.study-*`, `.process-*`, header compartilhado; `how-it-works.css`+`landing.css`+`ui-theme.css` | HTML nativo `<details>`, menu e tema | **Manter HTML semântico** no primeiro piloto; tokens/componentes por intenção comprovada |
| `/about/` | conteúdo editorial hoje em HTML | [`about/index.html`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/about/index.html), com dois `.about-chapter` no documento | `.about-hero`, `.about-chapter`, `.about-scale`; `about.css`+`landing.css`+`ui-theme.css` | links, menu, tema | Não converter página toda a JS; considerar composição de fonte em código e progressive enhancement depois |
| `/viewer/` | [`PublicModulePresentation2D 0.1`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/public-module-projection.js), `Scene2D` e catálogo; `viewer/data.js` controla composição | [`viewer/viewer.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/viewer/viewer.js) monta overview/scene/views/details; [`scene-adapters.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/viewer/scene-adapters.js) e [`technical-views.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/viewer/technical-views.js) especializam DOM | `.viewer-block`, `.technical-view`, `.detail-*`, `.scene-hotspot`; `viewer.css`, `ui-theme.css` | seleção, teclas, disponibilidade, vista/carrossel; erro de API | Preservar adaptador/projeção; candidato de reuso é contrato de componente, não troca de schema |
| `/config/` | Admin V5 → [`published-buyer-projection.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/published-buyer-projection.js) → flow/policy tipados | [`app.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/app.js) e [`scene-component.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/scene-component.js), sobre HTML com slots declarados | `.module-card`, `.flow-*`, `.module-detail__*`, `.scene-hotspot`; `styles.css`+`ui-theme.css` | entidades, preços, dependências, estados, responsividade, teclado | **Não tocar no piloto**; já possui validação de binding `data-render-component`↔schema e regras de falha |
| `/admin.html` | [`administration-v5.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/administration-v5.js), catálogo, cena e políticas | [`admin/admin.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/admin/admin.js): `renderItem` → `renderSection` → `renderGroup` → `renderStages`, além de editores especializados | `.hierarchy-*`, `.data-field`, `.admin-*`; `admin.css`+`ui-theme.css` | autoria, validação, save, auth, roles; alto risco | **Preservar editor específico**; nenhuma edição de página pública adicionada agora |
| `/access/`, `/access/manage.html` | auth/gerência; não são componentes de produto | HTML específico, `access/*.js` e [`private-navigation.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/private-navigation.js) | header privado, formulários, mensagens, tema | sessão temporária/admin, convites, identidade, status | Shell compartilha somente contrato autenticado; ações e permissões especializadas |

**Domínio de cena**: `scene-component.js` tem operações de layers, máscaras, hotspots, seleção e visibilidade. A extração de `.scene-hotspot` como CSS compartilhado é candidata válida, **não** convite a migrar os dados de cena a um manifesto genérico.

**Tema**: [`core/ui-theme.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/ui-theme.js) já é módulo transversal: injeta `.ui-theme-toggle` conforme DOM detectado (`.site-header`, `.viewer-heading`, `.private-header__actions`, etc.). Isso permite padronizar aparência, mas também representa acoplamento via busca estrutural; migrar para **slots explícitos** só depois de revisar NAV-005 e testes por rota.

## Prova de que o DOM fonte não basta

Leitura estática dos JS específicos (contagem lexical aproximada; `createElement` inclui `createElementNS` quando indicado, não é cardinalidade runtime):

| Arquivo | `createElement(...)` aproximado | `addEventListener` literal | Razão para mapear em execução |
|---|---:|---:|---|
| `app/app.js` | 123 | 43 | geradores de etapas, detalhes, controles, summary, carrosséis e interações |
| `app/admin/admin.js` | 170 | 35 | editor inteiro depende dos dados, estado e sessão |
| `app/viewer/viewer.js` | 3 | 1 | concentra um helper `element(tag,...)` que encapsula criação de muitos elementos; contagem literal **subestima** DOM |
| `app/viewer/technical-views.js` | 12 | 0 | cria figuras e SVGs a partir de dados técnicos |
| `app/landing/landing.js` | 12 | 11 | cartões e benefícios alimentados por dados |
| `app/core/scene-component.js` | 7 | 1 | camadas/click targets gerados por cena |

**Limitação da métrica:** contagem é ocorrência de expressão no código, não execuções, nem número de nós montados, nem cobertura funcional; funções auxiliares e loops multiplicam DOM. A página `/viewer/` tinha nove classes no HTML estático; esse número não representa a UI que aparece depois da projeção pública.

### Classes atribuídas literalmente no JS versus classes CSS do carregamento

Foi feita uma segunda interseção lexical exploratória de `className=`, `classList.add/remove/toggle` e `setAttribute('class', ...)` com `uniqueClassSelectors` das folhas por rota. **Não** cobre templates dinâmicos, classes aninhadas em seletores compostos, regras por ID, herança ou `data-*`; classes não localizadas **não são necessariamente não estilizadas**.

| Fluxo auditado | Classes distintas detectadas nesse subconjunto | Nomes presentes na lista CSS | Por que o restante exige inspeção |
|---|---:|---:|---|
| Configurador (+ cena, tema e navegação privada) | 105 | 79 | estados como `is-selected`, `is-hidden`; CSS pode conter seletores compostos |
| Admin (+ tema/nav) | 81 | 77 | `is-active`, helpers compostos e variantes no JS |
| Viewer (+ scene/tech/tema) | 25 | 18 | `is-current`, `is-selected` e transições; helper de criação |
| Landing (+ tema/menu) | 18 | 13 | `is-changing`, `wave`, `is-selected`; pseudoestados |
| About (+ tema/menu) | 7 | 7 | shell em HTML principal |
| How it works (+ tema/menu) | 7 | 7 | `details` nativo, estados/tema e header |
| Access/login (+ tema/nav) | 11 | 10 | folha de acesso contém seletores compostos e markup específico |

Isso não é auditoria exaustiva de classe dinâmica. É uma fila priorizada para o instrumento de DOM/computed style em P0-R. Não reportar a diferença aritmética como bugs.

## Reuso confirmado versus parecido

- **Confirmado por código:** `CasaModulesSceneComponent` é consumido por Configurador e adaptador do Viewer; reutilização real de desenho/interação (com estados próprios).
- **Confirmado por código:** `CasaModulesPresentation` explicita lista fechada de componentes de seção do Configurador e valida `behavior`; [`flow-layout.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/flow-layout.js) atribui `component` à apresentação normalizada.
- **Confirmado por código:** `data.layout = ['overview','scene','views','details']` no [`viewer/data.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/viewer/data.js) e `renderers = new Map()` no `viewer.js`; a composição é parcialmente declarativa, embora a escolha estrutural dos blocos use branches por ID.
- **Confirmado por código:** `Landing/renderBenefits()` lê `data.benefits`, mas também cria três `.mini-benefit` com textos e assets inline na própria função; isso é uma autoridade local distinta, não prova duplicação de dados editáveis.
- **Confirmação parcial:** `.button`, `.eyebrow`, `.brand` em várias folhas: requer semântica/variante/slots antes de promover.
- **Homonímia:** `.module-card` no Configurador e em Como funciona possui contratos divergentes; não fundir.
- **Tema/header:** `ui-theme.js` e `private-navigation.js` são cross-page, mas os slots e os papéis de sessão não são equivalentes; evitar composição genérica sem segurança.

## Questões abertas e priorização P0-R

1. **P0-R1:** extrair a árvore DOM efetivamente renderizada no Landing e Viewer e registrar atributos de acessibilidade/HTML esperado; comparar `CSSStyleDeclaration` efetivo por tema e largura representativa.
2. **P0-R2:** confirmar desenho de estados protegidos sem armazenar payload, conta, tokens ou convites; **não bloquear** experimento isolado de Landing por falta de sessão administrativa.
3. **P0-R3:** checar `ui-theme.js` e `private-navigation.js` por ordem de inicialização/injeção e pelo impacto de futuros slots explícitos; NAV-005 deve ser gate separado.
4. **P0-R4:** procurar classes JS construídas em template string, funções que encapsulam DOM (Viewer) e seletores compostos com AST/CSS parser na próxima fase. O cruzamento lexical não basta.
5. **P0-R5:** fechar matriz representativa de estados, CSS e interações (incluindo iPad/Safari quando houver ambiente real) antes de qualquer substituição no produto.

**Conclusão P0 documental:** há base existente para generalização de contratos **sem** migrar schema comercial. Há evidência suficiente para desenhar e provar um **registro experimental isolado**; ainda não há evidência para reorganizar todas as folhas ou substituir renderers do produto.
