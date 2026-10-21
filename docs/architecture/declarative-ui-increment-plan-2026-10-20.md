# UI-P0/P1 — Checkpoint e plano de implementação incremental

> **Aviso de versão (20/10/2026):** este arquivo documenta o plano P0/P1 originalmente formulado e contém estados textuais históricos que podem estar superados (por exemplo, P0-R “pendente” na matriz inicial). O estado **mais recente e canônico** desta trilha está no [plano diretor](DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md), no [gate atual CSS/P4-NAV](CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md) e em [UI-ADR-002](ui-adr-002-landing-component-pilot-2026-10-20.md)–[UI-ADR-005](ui-adr-005-public-header-controller-2026-10-20.md). Preservar a matriz histórica para proveniência; não repetir procedimentos agora marcados como concluídos.


**Data:** 2026-10-20  
**Estado confirmado:** P0 inventário de ownership estático **documentado**, P1 prova de contrato **isolada** com 13 testes Node 22 nativos passando; **nenhum código de produção alterado**.  
**Decisão técnica:** [UI-ADR-001](ui-adr-001-declarative-boundaries-2026-10-20.md).  
**Auditoria fonte:** [P0 DOM+JS](dom-js-component-ownership-2026-10-20.md).  
**Experimento:** [registry.mjs](../../experiments/declarative-ui/registry.mjs), [Landing fixture](../../experiments/declarative-ui/landing-benefits.mjs), [testes](../../experiments/declarative-ui/registry.test.mjs).

## Gates realizados

| Gate | Evidência | Resultado |
|---|---|---|
| P0-A — ownership estático de DOM, JS, dados e CSS | 8 páginas, fontes e renderers principais, classes HTML e JS, diferenças de CSS por contexto | **PASS documental / limitado** |
| P0-B — classificação de autoridade | domínio/admin v5 vs DTO público vs composição da página vs renderer vs tema/estado | **PASS documental** |
| P1-A — componente tipado | `landing/benefit-strip@1` com variante `standard`, fonte `landing.benefits`; renderer só retorna descritores | **PASS experimental** |
| P1-B — fail-closed | tipo e variante não admitidos, duplicação de ID, `dataRef` inexistente/unsafe, estilo extra no manifesto, URL externa de ícone | **PASS experimental** |
| P1-C — sem montagem parcial | compilar/validar seções antes de renderizar; teste de erro na segunda seção verifica zero chamadas de renderer | **PASS experimental** |
| P1-D — snapshot de dados | copia JSON portátil antes da validação e renderização; mutação posterior no objeto-fonte não altera descritor | **PASS experimental** |
| P0-R — DOM real/computed CSS nos estados e viewports | requer instrumentação de navegador/fixtures + contraste + interação | **PENDENTE** |
| P1-E — execução `node --test` nativa | Node 22 GitHub Actions: [pull_request](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39502842741) e [push](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39502842309); 13 testes, 0 falhas. Nenhum navegador exercitado pelo teste P1. | **PASS Node; browser separado** |

**Precisão da evidência de testes:** os 11 casos foram executados in-memory usando exatamente as três fontes recuperadas do GitHub, com transformação de `import/export` para um executor JS e pequeno shim de `node:test`; todos passaram. **Isso não equivale a** `node --test` nativo, Playwright, Safari/iPad, DOM real nem inspeção visual. Uma tentativa de baixar as fontes diretamente no container para rodar Node falhou por DNS; não alegar suíte Node passada.

## Contrato do piloto P2, quando autorizado no repositório de produto

**Escopo positivo:** apenas a faixa `data.benefits` ↔ `.benefit-item` da Landing, sem mexer nas três `.mini-benefit`, no carrossel de ambientes, no header, na projeção pública de módulos, no Editor Admin, na configuração v5, no Viewer ou no deploy.

**Separação operacional:**
1. Entrada de dados: `CASA_PUBLIC_LANDING.benefits`, já local e declarativa.
2. Manifesto de código: único nó `landing/benefit-strip@1` com `dataRef='landing.benefits'`; **não** salvar no backend/admin.
3. Validação + snapshot: dados e ordem validados em uma etapa pura.
4. Renderer: cópia funcional do DOM atual (um `div.benefit-item`, `img[alt='']`, `span` por benefício), sem `innerHTML`.
5. Encaixe: só substituir o miolo de `#benefits` em flag/local de teste; manter antiga função reversível até passar gate.
6. CSS: manter inicialmente `.benefit-item` e `landing.css` **inalterados**, para isolar arquitetura do estilo.
7. Testes: comparar a árvore gerada atual com a nova em fixture e runtime (tag, classe, texto, ordem, `src`, `alt`), estado claro/escuro, 390/768/1366px, zoom e reduced-motion quando houver; confirmar que render não cria interação, não altera benefícios ausentes nem altera imagem inválida silenciosamente.
8. Após teste em página pública e preview **explicitamente autorizado**, remover apenas duplicação de render desse componente, mantendo rollback simples por PR/revert.

**Critérios de reprovação:** mudança visível não homologada, seção ausente recriada por defaults implícitos, novo ponto de falha de init da Landing, piora de carregamento/layout shift, erro de acessibilidade, dependência de admin ou alteração da cascata CSS.

## Próximos passos por valor/risco

| Ordem | Incremento isolado | Entra | Não entra |
|---|---|---|---|
| 1 | **P0-R** instrumento DOM-CSS real e matching de estilos por componentes | evidência e relatório sobre Landing/Viewer + áreas condicionais | mudanças funcionais |
| 2 | **P1-E** execução Node `--test` no clone CI e browser smoke do protótipo | validação da suíte publicada e suporte de runtime | adoção produtiva |
| 3 | **P2-A** piloto sombra Landing em branch de produto | render lado a lado em fixture e comparação, sem mount principal | backend, Auth, v5 |
| 4 | **P2-B** switch limitado com teste e rollback | `benefit-item` gerado pelo novo registry | header, mini-benefits, catálogo |
| 5 | **P3** um segundo consumidor com contrato equivalente | compartilhamento comprovado ou encerramento NOOP | generalização baseada em nome CSS |
| 6 | **P4** blocos transversais mais sensíveis | header/tema só após NAV-005 e validação de roles | migração em massa |
| 7 | **P5** autoria editorial condicional | apenas se usuário aprovar conteúdo editável, draft, publicação e RBAC | editor universal genérico |

### Interfaces existentes não substituídas

- `CasaModulesPresentation` (componentes de seleção/ação de Configurador) permanece autoridade de capacidade e comportamento no seu domínio.
- `CasaModulesSceneComponent` continua dono da geometria/visibilidade/interação da cena; aplicar abstração não cria um compositor universal de cena.
- `CasaModulesPublicModuleProjection` permanece allowlist do Viewer; nenhum manifesto frontend altera exposição de dados no servidor.
- `CASA_UI_THEME` e navegação autenticada mantêm comportamentos próprios; migrá-los exige contratos explícitos de slots e revisão de NAV-005.
- Páginas editoriais estáticas continuam renderizando conteúdo essencial sem JavaScript até demonstrar progressive enhancement sem regressão.

## Considerações sobre schema

A demonstração `PageCompositionExperimental 0.1` **não** é um schema persistido ou publicado. É um contrato de memória, versionado com o código, com campos **exatos**: `schemaVersion`, `route`, `sections`; cada seção admite `id`, `type`, `variant`, `dataRef`. Essa restrição evita nascer como page builder descontrolado. Se outra página exigir `props` ou slots, abrir uma revisão do contrato com casos de teste concretos, não acrescentar arbitrariamente ao schema.

O protótipo usa cópia de valores JSON com limite de profundidade, rejeita ciclos/acessores/chaves perigosas; proteção contra mutação dos dados após validação é importante. A validação de payload público e IDs de ação continuará na camada que é sua autoridade; não oferecer HTML/CSS/JS por payload.

## Critério de parada arquitetural

Se P3 não demonstrar uso legítimo por uma segunda superfície, **não forçar** a universalização de `benefit-strip`: mantê-lo como módulo de domínio da Landing. O objetivo é reduzir fontes duplicadas e risco de manutenção, não maximizar o número de abstrações nem o tamanho de um catálogo de componentes.

**Não modificar `decisions.json` para registrar estas escolhas:** ele é canônico para homologação de design. Este ADR contém **decisões técnicas experimentais**; promovê-las a padrão de produto requer os gates e eventual aprovação de escopo.

## Atualização de execução — P0-R e P2 shadow

- [P0-R Chromium #39503394834](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39503394834) e [#39503582819](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39503582819): 16/16 observações públicas, quatro rotas, dois temas, duas larguras; HTTP 200, tema resolvido correto, sem erros de recurso/JS registrados.
- [P2 shadow #39503582819](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39503582819): descritores `benefit-strip@1` equivalentes ao DOM público da Landing (4/4 linhas, tags, classes, ordem, imagens e textos); não houve montagem ou substituição no produto.
- [P1 Node nativo #39503470216](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39503470216): 13 testes, 13 PASS, 0 FAIL após endurecer snapshot profundamente congelado e caminhos dataRef sem getters.
- **Próxima fronteira:** se a integração no produto for autorizada, testar o mesmo renderer em modo sombra na branch do produto e depois comparar computed CSS/funcionalidade antes de alterar a montagem real. Testes com acesso privado, WebKit/iPad e mudanças de theme behavior continuam gates independentes.
