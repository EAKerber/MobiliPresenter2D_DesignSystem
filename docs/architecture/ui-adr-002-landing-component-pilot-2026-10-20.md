# UI-ADR-002 — Integração incremental real da Landing, sem alteração visual

**Data:** 2026-10-20 · **Estado:** PILOTO TÉCNICO IMPLEMENTADO E GATES AUTOMATIZADOS PASS (escopo restrito); **não homologado para publicação/merge**.  
**Autoridade:** [UI-ADR-001](ui-adr-001-declarative-boundaries-2026-10-20.md), [inventário P0](dom-js-component-ownership-2026-10-20.md), [baseline Chromium público](dom-css-runtime-public-baseline-2026-10-20.md).  
**Produto:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D), branch `experiment/ui-declarative-landing-benefits-20261020`. Base `main@1878ae1057ce7c6190e0c8cb08a1f3baadd49463`, confirmada antes do trabalho.  
**Design System:** branch `architecture/dom-css-consolidation-20261020`, PR #39 draft.  
**Execução:** [GitHub Actions #39504822312](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39504822312), conclusão **success**.

## Decisões de implementação tomadas

1. **Integrar primeiro apenas a faixa de benefícios da Landing**, `#benefits > .benefit-item`. Não alterar `#miniBenefits`, ambientes/carrossel, header, Viewer, Configurador, Administração, preços, sessão ou theme.
2. **Contrato em código / JS clássico** para esta migração: [`app/core/page-composition.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/experiment/ui-declarative-landing-benefits-20261020/app/core/page-composition.js), em IIFE com export opcional CommonJS para testes Node. Evita reconfigurar o bootstrap atual da Landing para ESM e preserva a estratégia de scripts declarados em ordem no fim de `app/index.html`.
3. **Componente de feature especializado** [`app/landing/benefit-strip.js`](https://github.com/EAKerber/MobiliPresenter2D/blob/experiment/ui-declarative-landing-benefits-20261020/app/landing/benefit-strip.js) define `landing/benefit-strip@1`, variante `standard`, `dataRef=landing.benefits`; registro fechado, sem CSS nem handlers arbitrários provenientes de JSON.
4. **Schema `PageCompositionExperimental 0.1` permanece não persistido e experimental.** Não alterar `ConfiguratorAdministration2D 5.0`, `PublicModulePresentation2D` ou contratos de publicação. A Landing continua lendo `CASA_PUBLIC_LANDING.benefits` de `landing/data.js`.
5. **Montagem atômica local:** `compilePage` valida todas as seções, copia e congela o subconjunto JSON, resolve somente `dataRef` por propriedades próprias; o componente cria um `DocumentFragment` destacado; `mountSection` troca os filhos de `#benefits` apenas após retorno válido. Ao falhar, a Landing mostra status mínimo do bloco e preserva a inicialização das outras áreas, sem inventar benefícios ou carregar dados administrativos.
6. **DOM e CSS permanecem invariantes visuais do piloto:** `div.benefit-item > img[alt=''] + span`, sequência original, atributos e classes; nenhuma folha CSS ou asset foi modificado. `landing.js` delega somente esse bloco ao registro. Ordem dos scripts: `landing/data.js` → `core/page-composition.js` → `landing/benefit-strip.js` → `landing/landing.js`.
7. **Sem PR no repositório de produto nesta etapa** para evitar disparar automaticamente um deploy preview desnecessário no Netlify. A branch de teste está no GitHub e possui workflow dedicado; **não** houve merge, publicação ou edição de main.
8. **Não promover `page-composition.js` como padrão global ainda:** o custo adicional do registry (~145 linhas) para quatro benefícios só se justifica como investimento se um segundo consumidor genuíno demonstrar reuso. Não fabricar segundo consumidor apenas para homologar abstração.

## Arquivos alterados no produto (fronteira da branch)

| Caminho | Alteração |
|---|---|
| `app/core/page-composition.js` | Novo contrato/registry JS clássico, versões/tipos permitidos, validação e montagem |
| `app/landing/benefit-strip.js` | Novo componente declarativo de benefícios |
| `app/landing/landing.js` | Substitui somente `data.benefits.forEach` pelo mount do componente; mini-benefícios e demais funções preservados |
| `app/index.html` | Declara scripts novos e ajusta cache version do `landing.js` |
| `tests/landing-benefit-composition.test.cjs` | 7 testes Node do contrato, do DOM representado e de falhas |
| `tests/landing-benefit-browser-gate.mjs` | Comparador DOM, computed CSS, geometria e screenshot da região por viewport/tema |
| `.github/workflows/declarative-landing-benefits-pilot.yml` | CI isolada: baseline main e candidata servidos em localhost, sem deploy |

## Evidências e resultados

- [Actions #39504822312](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39504822312) confirmou `node --test tests/landing-benefit-composition.test.cjs`: **7 PASS, 0 FAIL**.
- O teste existente `node tests/public-cutover-contract.cjs` completou com sucesso, sem alteração dos contratos de rota pública.
- Chromium local comparou `main` e a branch candidata em largura **390** e **1366**, tema **claro** e **escuro**: **4/4 PASS**.
- Em cada cenário houve `domEqual:true`, `computedCssEqual:true`, `geometryEqual:true`, `screenshotEqual:true`, `errors:0` para `#benefits`. Capturas em `artifacts/landing-benefits/` no workflow (retenção de 7 dias).
- Capturas são da **região de benefícios**, não página inteira; foram produzidas no mesmo navegador/contexto de CI com ambas as variantes servidas localmente e sem sessão.
- Os testes cobrem criação de dados válidos, forma do DOM legado, snapshots imutáveis, tipos/variantes/estilos inválidos, ausência de referência, getter bloqueado, falha isolada e impossibilidade de montagem parcial.

## O que NÃO ficou provado

- Fidelidade visual da página inteira em todas as interações, zoom e dispositivos; o teste pixel-a-pixel é apenas da região `#benefits` em Chromium.
- Safari/iPad/Chrome iPad, WebKit e navegadores móveis reais. O JS clássico foi escolhido para minimizar mudança de bootstrap, mas **não** é prova de compatibilidade nesses ambientes.
- Auth, menus, preços, Admin, Viewer e permissão no servidor, que não foram modificados nem testados exaustivamente neste piloto.
- Resiliência da Landing a falha de carregamento de um dos novos scripts em conexões lentas (o bloco possui tratamento de erro, mas essa falha ainda não foi ensaiada com interceptação).
- Ganho líquido de manutenção: precisa de segundo consumidor equivalente antes de extrair camada compartilhada para outras páginas.

## Gate seguinte sugerido

**P2-C, antes de qualquer preview/publicação:** smoke público local da Landing completa com foco, menu, 5 ambientes, CTA, carregamento de imagem, reduced-motion e zoom; teste de falha do script/manifesto sem comprometer carrossel. Usar cenário WebKit/Safari se disponível. Validar que nenhum workflow preexistente de produto foi tornado vermelho pela branch; diferenciar falhas de main que já eram conhecidas. Registrar contagem/duração e screenshots de referência. Só depois avaliar uma PR draft do produto, levando em conta política de deploy preview e orçamento de Netlify.

**Gate de parada:** qualquer divergência visível fora do componente, quebra de menu/ambientes, falha de script que derrube resto da Landing, ou necessidade de alterar dados comerciais interrompe a migração. Sem aceitar mudanças de CSS/tokens/identidade como parte da presente etapa.

## Estado de homologação

Aprovado **tecnicamente para permanecer em branch experimental**, não para `main`. Este ADR registra decisões de implementação e resultados concretos. Não modifica `decisions.json` do Design System, que segue sendo autoridade de homologação visual.
