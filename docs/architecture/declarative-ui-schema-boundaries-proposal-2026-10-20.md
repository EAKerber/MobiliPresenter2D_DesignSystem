# Arquitetura candidata — UI declarativa por domínios, schemas separados e migração incremental

**Data:** 2026-10-20  
**Status:** hipótese arquitetural documentada para discussão; NÃO homologada, sem alteração do produto ou dos dados publicados.  
**Repo de produto lido:** `EAKerber/MobiliPresenter2D` em `main`. **Repo de documentação:** `EAKerber/MobiliPresenter2D_DesignSystem`.  
**Relacionado:** [baseline DOM×CSS](dom-css-consolidation-baseline-2026-10-20.md) e [arquitetura de CSS](css-component-architecture-proposal-2026-10-20.md).

## O que já existe e merece reaproveitamento

- `app/core/presentation-contract.js`: `ConfiguratorPresentation2D 1.1`, componentes permitidos `choice-swatches`, `choice-grid`, `choice-cards`, `selection-list`, `toggle-list`, `action-list`; vistas `detail-panel`; relações `companion`; projeções `inline`, `side-panel`, `replace`; validação de política.
- `app/core/administration-v5.js`: `ConfiguratorAdministration2D 5.0` valida componentes, comportamento e `presentationPolicy`; `app/core/flow-model.js` e `flow-layout.js` normalizam e materializam a hierarquia.
- `app/core/published-buyer-projection.js` e `public-module-projection.js`: limites explícitos entre documento privado e DTOs públicos, sem vazamento de preços/documento administrativo completo.
- `app/core/scene-component.js`, `app/viewer/scene-adapters.js`, `app/viewer/technical-views.js`: componentes específicos de cena e vistas técnicas reutilizáveis com contrato próprio; `app/viewer/data.js` declara ordem das áreas e `detailLayout` por fonte.
- `app/landing/data.js` e `app/landing/landing.js`: conteúdo e cartões já declarativos, fora do schema v5. `app/core/ui-theme.js` e `private-navigation.js` continuam responsáveis por estado visual e autenticação/navegação respectivamente.
- Roadmap histórico `docs/backlog/schema-driven-ui-consolidation-roadmap-2026-10-06.md`: CP-SD 00–06 COMPLETE/PASS; diretriz explícita de NÃO colocar CSS no schema e não criar UI semântica ausente a partir de fallback de renderer. Não reabrir v5 por causa de uma refatoração visual.

## Decisão candidata

**Generalizar o pipeline, NÃO o schema de Configurador nem o DOM universal.** Compartilhar quatro mecanismos leves: validação por domínio; construção de modelo de vista/projeção; registro limitado de tipos de componentes; aplicação dos estilos e comportamento por componente. Os dados e autorizações conservam autoridades próprias.

```text
[Dados de produto e Admin v5] --projection allowlist--> [View Model do Configurador/Viewer] --+
                                                                                              |
[Manifest de página em código] + [Conteúdo editorial, quando existir] --> [View Model público] -+--> [Registro de componentes] --> [DOM]
                                                                                              |        |                    |
[Estado de sessão/ações autorizadas] ----------------------------------> [Controladores] -----+        +--> CSS por componente + tokens
```

O registro sabe `type -> validateProps -> render` e, quando preciso, `update/destroy`; nunca recebe strings arbitrárias de código, expressões livres, seletor CSS livre ou HTML não sanitizado. Ações são IDs permitidos e ligados a controladores explícitos. Estado local transitório (hover, foco, carregamento, modal) permanece no componente/controlador, não dentro de dados persistidos de produto. Permissões são validadas no servidor, não por escondê-las via manifesto.

### Fronteiras de schemas propostas (nomes provisórios, não versões adotadas)

| Contrato | Natureza/autoridade | Exemplos | Persistência/migração |
|---|---|---|---|
| `ConfiguratorAdministration2D 5.0` | Documento de domínio existente, editado por Admin | etapas, entidades, materiais, valores, regras de negócio, apresentação permitida | **Preservar**; só nova versão quando houver necessidade do domínio |
| `Scene2D`, `ProductCatalog2D`, preços | Domínios próprios existentes | geometria, assets, catálogo, preços | **Preservar** |
| `PublicModulePresentation2D` e buyer DTO | Projeções derivadas, limitadas por consumidor | módulos públicos, dados visíveis, estado inicial | gerado; nunca autoridade de edição |
| `PageComposition` (candidato) | Manifesto estrutural de página/rota | sequência de seções, tipos registrados, slots, layouts admitidos | preferir versionado **com o código** no início; não colocar todo o site no Admin |
| `EditorialContent` (candidato) | Conteúdo que realmente precisa ser editável | títulos, parágrafos, ilustrações, metadados permitidos | criar somente ao confirmar necessidade de autoria; draft/publicado/versionado separadamente |
| `ComponentContract` (candidato) | Registro de código e validação | tipos, props e variantes permitidas, slots, ações conhecidas, requisitos acessíveis | em código, versionado por tipo; **não** documento administrável |
| `DesignTokens/Theme` | Identidade/tema homologados | papéis de cor, fontes, espaçamento, foco, light/dark | CSS/código, não valores livres vindos do Admin |
| `UI state/interaction` | Estado transitório e lógica | foco, seleção corrente, erro, loading, controle de menu | runtime, exceto configuração persistente de produto já existente |

A política de apresentação do Configurador pode ser **compatível por conceito** com `PageComposition`, sem tornar `ConfiguratorPresentation2D 1.1` a linguagem geral do site. Os perfis atuais `side-rail/stacked/compact` pertencem ao Configurador; uma regra global de layout deve nascer só se houver consumidores reais e sem fixar breakpoints universalmente.

### Exemplo deliberadamente limitado (não válido ainda como contrato executável)

```json
{
  "schemaVersion": "PageComposition 0.1-candidate",
  "route": "/about/",
  "shell": "public",
  "sections": [
    {
      "id": "intro",
      "type": "editorial-hero",
      "variant": "split",
      "props": {
        "titleRef": "about.intro.title",
        "descriptionRef": "about.intro.description"
      }
    }
  ]
}
```

`type` deve existir no registro; `variant` deve ser suportada **por esse tipo**; `*Ref` deve apontar para conteúdo autorizado da página. Layout, HTML, CSS e interação não vêm do payload. Exemplo para estabelecer fronteiras, não para introduzir um formato em produção.

## Formas de generalização a evitar

1. Schema único de site que inclua Admin, produto, acesso, Viewer, Landing, geometria e tokens. Gera migrações acopladas e configuração administrativa excessiva.
2. Editor universal no Admin em que qualquer página possa injetar `style`, scripts ou componentes. É uma superfície de segurança desnecessária.
3. Trocar todos os `document.createElement` por uma biblioteca genérica de nós antes de identificar contratos compartilhados. Diferenças legítimas (cena, desenhadores técnicos, pricing, auth) devem permanecer especializadas.
4. Reabrir ou republicar schema v5 de produto apenas para mover CSS ou compor uma página pública.
5. Confundir repetição textual de estilos com duplicação de componente/autoridade.
6. Oferecer no Admin controles de layout sem decisão explícita de que aquela dimensão deve ser configurável.

## Plano incremental e gates

**P0 — Documento de propriedade de componentes (sem runtime):** cruzar o inventário DOM/CSS da PR de Design System com `app/app.js`, `app/viewer/viewer.js`, `app/landing/landing.js`, `app/admin/admin.js` e estilos. Registrar para cada bloco: contrato de dados, proprietário, renderer, eventos, CSS, variantes, estados, permissão e tipo de teste. Gate: casos estáticos e dinâmicos distinguidos, sem exigir cobertura universal para prosseguir num componente.

**P1 — Piloto estrutural apenas de leitura, sem schema publicado:** definir um registro mínimo `type -> validator -> render` para uma seção editorial pública não crítica (um bloco de `/about/`, por exemplo) com manifesto **local ao código**. Duas formas de renderização lado a lado em fixture, sem impacto visível. Gate: DOM semântico, textos e estilos computados equivalentes; zero efeitos colaterais.

**P2 — Primeiro componente compartilhado real:** provar reuso num segundo consumidor de contrato equivalente (Landing/Como funciona, se houver mesma semântica); então extrair CSS/renderer da origem com fallback de rollback de código. Não inventar reutilização para justificar abstração. Gate: equivalência de comportamento/tema/responsividade; utilitário `.visually-hidden` pode ser extração independente.

**P3 — Componentes de shell/navegação:** aplicar ownership em header público/privado e marca a partir de NAV-004/NAV-005/PRIVATE-HEADER-001, mantendo diferenças de permissão e layout; migrar a composição dos menus sem mudar o contrato de auth. Gate: menu, sessão, foco, Escape, narrow, reduced-motion, 2 temas.

**P4 — Reaproveitar os adaptadores do Configurador e Viewer:** compatibilizar a forma de registrar renderers/componentes e mapear tokens/classes por componente; NÃO migrar dados v5 ou `scene` ao manifesto. Gate: sem mudança de seleção, visibilidade, preço, projeções públicas, affordances e flows existentes.

**P5 — Conteúdo administrativo opcional:** só se o produto demandar edição de textos/imagens/ordem editorial fora do código, introduzir `EditorialContent` com draft/publish/revision e validação; criar formulários especializados e public projections allowlist. Manter estrutura do manifesto fixa onde não houver necessidade de customização. Gate: publicação atômica/readback, permissões servidor, payload público mínimo, ausência/erro determinísticos e sem perda de rascunhos.

**P6 — Governança e simplificação:** quando consumidores migrarem, remover seletores/markup duplicados comprovadamente obsoletos; conferir `index.html` do Design System com seu `decisions.json` para não duplicar autoridade. Gate: nenhuma mudança não homologada no produto, snapshots visuais e testes funcionais passam.

Cada P é independente quanto possível, PR pequena em branch, comparações automáticas + inspeção visual + teste funcional, rollback local claro. Não adotar framework novo nem CSS-in-JS como pré-requisito.

## Primeiro recorte de implementação sugerido

**Uma única seção editorial pública, com manifesto local, renderizador puro e contrato de props com validação.** Não alterar o Admin, v5, endpoint público, dados de preço, publicações nem a hierarquia do Configurador no piloto. O resultado deve demonstrar que o registro é capaz de servir duas rotas e reduzir CSS duplicado; se não houver segundo consumidor compatível, encerrar como extração local, sem abstração forçada.

### Questões a responder depois da descoberta, não bloqueadores imediatos

- Quais campos da Landing/Como funciona/Quem somos precisam ser editáveis pelo Admin? Se nenhum, manter conteúdo versionado no código.
- Quais seções têm contratos iguais além de semelhança estética? Confirmar com DOM real.
- Editor de layout é desejado ou somente edição de conteúdo? Essa distinção define se precisamos de schema de composição persistido.
- Como versionar/validar valores futuros de `variant` sem romper publicações antigas? O manifesto em código torna a primeira versão segura.

**Estado desta proposta:** separação e direção candidatas para avaliação. Nenhuma migração de dados, gravação de configuração, código de produto ou novo schema de produção foi feita.
