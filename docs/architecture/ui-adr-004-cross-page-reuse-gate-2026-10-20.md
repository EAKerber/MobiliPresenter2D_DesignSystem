# UI-ADR-004 — Gate de promoção: reuso de apresentação entre rotas versus conteúdo editorial

**Data:** 2026-10-20  
**Status:** decisão de DIREÇÃO: **NÃO PROMOVER** `PageCompositionExperimental 0.1` a registro universal neste checkpoint. Cabeçalho público e menu entram como candidato de componente transversal estático/controlador, **sem implementação ou alteração visual nesta rodada**.  
**Produto verificado:** `EAKerber/MobiliPresenter2D@1878ae1057ce7c6190e0c8cb08a1f3baadd49463` e experimento da Landing `experiment/ui-declarative-landing-benefits-20261020`.  
**Documentos antecedentes:** [UI-ADR-001](ui-adr-001-declarative-boundaries-2026-10-20.md), [UI-ADR-002](ui-adr-002-landing-component-pilot-2026-10-20.md), [UI-ADR-003](ui-adr-003-landing-benefit-variants-2026-10-20.md).

## Aprendizado medido em P3

O compartilhamento `landing/benefits@1` para **4 itens padrão + 3 compactos** funcionou e foi validado em Node, Chromium e WebKit. Isso prova compatibilidade de **um contrato de conteúdo entre duas instâncias da mesma página**. Não prova necessidade de um motor universal.

Leitura do tamanho de quatro arquivos JS afetados (comprimento do texto UTF-16 recuperado do GitHub, **não** bytes de download, bundle ou gzip):

| Arquivo | `main` | Branch candidata | Delta |
|---|---:|---:|---:|
| `app/core/page-composition.js` | 0 | 7079 | +7079 |
| `app/landing/benefit-strip.js` | 0 | 3108 | +3108 |
| `app/landing/landing.js` | 9762 | 9652 | -110 |
| `app/landing/data.js` | 1841 | 2116 | +275 |
| **Total destes JS** | **11603** | **21955** | **+10352** |

A diferença mostra que o piloto pagou custo de infraestrutura relativamente grande para apenas sete itens. Isso não invalida separação de contratos, mas exige cautela ao alegar ganho líquido de manutenção ou performance. **Decisão:** não unificar outras páginas automaticamente, não publicar na `main` e não apresentar P3 como prova de economia de tamanho.

## Candidato de reuso verdadeiramente entre páginas

Os cabeçalhos de `/`, `/about/` e `/how-it-works/` compartilham:
- `header.site-header`, marca com `img[data-brand-variant]`, `nav#primaryNav`, CTA e `button#menuToggle` com `aria-expanded`.
- `app/landing/landing.css` e `app/ui-theme.css` já são reutilizados no shell editorial. O documento HTML estático fornece imediatamente o conteúdo e a navegação; renderização JS para criar todo o header não é necessária.
- Conteúdo/estado `aria-current="page"` diferem intencionalmente conforme a rota; `href` absolutos/relativos também diferem na fonte, mesmo quando destino é equivalente.

**Há duplicação real de comportamento e pequenas diferenças de acessibilidade:**

| Rota | Controlador de menu hoje | Ações verificadas no código | Oportunidade |
|---|---|---|---|
| `/` | `app/landing/landing.js` (funções/menu embutidos no carrossel) | click abre/fecha; click no link fecha; `pointerdown` global usado para `stopHint`, **não** é um fechamento explícito de menu; nenhum handler Escape específico do menu identificado | extrair controlador sem quebrar o carrossel e timing |
| `/about/` | `app/landing/header-menu.js` | click, navegação, Escape e `pointerdown` fora de nav/toggle | consumidor de controlador reutilizável existente |
| `/how-it-works/` | `app/how-it-works/how-it-works.js` no bloco inicial | click, navegação, Escape e `pointerdown` fora de nav/toggle | eliminar duplicação com `header-menu.js`, mantendo restante da página |

**Não alegar automaticamente bug de UI** por essa diferença: ela foi inferida da leitura do código; teste real de foco, teclado, clique fora e comportamento homologado é gate separado. O controlador do About é uma boa **hipótese de base**; não inferir que se aplica indiscriminadamente ao Admin ou ao Viewer, que têm sessões/slots distintos.

## Decisão arquitetural após P3

1. **Separar três modalidades**, sem impor uma tecnologia:
   - *Dados de domínio* (V5, catálogo, preços, cena): mantém schemas e projeções especializadas.
   - *Dados editoriais+variantes de UI* (ex. benefícios da Landing): podem usar contrato tipado de código, mas a complexidade do registro genérico deve ser justificada por outros consumidores.
   - *Shell estático e comportamento transversal* (header/nav): preservar HTML acessível na resposta inicial, compartilhar CSS e controlador JS explícito; se for necessário compartilhar HTML também, avaliar mecanismo build-time sem injetar cabeçalho via JS em runtime.
2. **Não migrar header para `PageCompositionExperimental`** para forçar um segundo consumidor entre rotas. Isso reduziria disponibilidade sem JS e misturaria autoria editorial com navegação.
3. **Não universalizar `.brand`, `.eyebrow` ou `.button` por nome CSS.** Variantes e dados de tema são homologados por contexto; CSS idêntico não demonstra mesmo contrato de interação.
4. **Priorizar o controlador de header**, mas como nova frente com baseline de três rotas, gate de focus/keyboard/aria, visual light/dark/mobile/desktop e teste da animação/ondas da Landing. CSS e markup ficam congelados inicialmente.
5. **Parar a generalização de runtime até medir custo/benefício.** Um segundo consumidor na mesma Landing demonstra viabilidade técnica, não demanda real de um page builder. O experimento de produto permanece em branch isolada, e `main` e Admin V5 continuam intocados.

## Próximo incremento proposto (ainda não executado)

**P4-NAV-0 — Matriz de comportamento atual sem mudar código:** comparar menu com mouse, touch, teclado, Escape, clique fora e scroll para `/`, `/about/`, `/how-it-works/` em 390/1366 e claro/escuro; registrar visual/ARIA e decisões NAV-005 como autoridade.

**P4-NAV-1 — Extrair controlador independente só se gate identificar vantagem:** reutilizar `header-menu.js` ou wrapper com inicialização única e `destroy` se houver reatividade; preservar comportamento da Landing de parar animação ao interagir. Alterar uma rota por vez e testar contra estado anterior; preferir JS clássico já carregado com `defer` para páginas estáticas.

**P4-NAV-2 — Centralização do markup, somente se necessária:** considerar templates/partials em build time depois de provar sincronização e compatibilidade com pipeline Netlify/esbuild; não impor ferramenta de build, JS hydration ou CMS aos HTMLs públicos.

**Gates de promoção:** regra única de propriedade por comportamento, sem double listeners, `aria-expanded` correto, menu funcional com navegação de teclado e ponteiro, sem regressão de foco, sem alteração cromática e sem injeção de texto/HTML arbitrários em dados. Nenhuma dessas ações está autorizada implicitamente para `main` ou deploy.

## Estado governado

- `UI-ADR-003` documenta P3 Node/Chromium/WebKit PASS com baseline idêntico; não significa que o registro tenha sido promovido.
- `UI-ADR-004` mantém a conclusão **NÃO PROMOVER** até ter um consumidor cross-page e um ganho de custo/manutenção demonstráveis.
- `decisions.json` do Design System permanece autoridade de homologação visual; não registrar ADR experimental nele como aprovação.
