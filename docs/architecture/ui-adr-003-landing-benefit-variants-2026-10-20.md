# UI-ADR-003 — Segundo consumidor real: benefícios compactos e padrão na mesma Landing

**Data:** 2026-10-20  
**Status:** decisão técnica experimental aplicada na branch isolada do produto; **gates de navegador P3 em validação no momento do primeiro registro**. Este ADR não homologa extensão do registro para outras páginas, não altera `decisions.json` e não aprova publicação/merge.  
**Produto:** `EAKerber/MobiliPresenter2D`, branch [`experiment/ui-declarative-landing-benefits-20261020`](https://github.com/EAKerber/MobiliPresenter2D/tree/experiment/ui-declarative-landing-benefits-20261020), baseada em `main@1878ae1`.  
**Design System:** `EAKerber/MobiliPresenter2D_DesignSystem`, branch `architecture/dom-css-consolidation-20261020`, [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39).  
**Antecedentes:** [UI-ADR-001](ui-adr-001-declarative-boundaries-2026-10-20.md), [UI-ADR-002](ui-adr-002-landing-component-pilot-2026-10-20.md).

## Problema de P3

A abstração do primeiro piloto foi capaz de reproduzir fielmente a faixa inferior `.benefit-item`, mas isso, isoladamente, **não justifica um registro genérico de ~7 KiB** para o site inteiro. O gate P3 exige procurar um segundo consumidor **semanticamente** compatível, sem confundir semelhança de classes/cores ou inflar um contrato universal.

## Alternativas examinadas

| Candidato | Propriedade dos dados / DOM | Reuso do contrato | Decisão |
|---|---|---|---|
| `Landing/#miniBenefits` | Mesmo conceito de vantagens com pares rótulo+ícone. Era hardcoded em `landing.js` com 3 rótulos + nomes de ícone. DOM `.mini-benefit > img + strong`; assets `gold`. | **Sim**, variante de apresentação do mesmo domínio, preservando diferenças de DOM, assets e CSS. | **Adotado em P3 isolado** |
| `Landing/#benefits` | `CASA_PUBLIC_LANDING.benefits` com 4 pares rótulo+ícone. DOM `.benefit-item > img + span`; assets `white`. | Contrato inicial já testado. | Manter |
| `Landing/#environmentTrack` | Cartões clicáveis, seleção, imagens assíncronas, estados e responsividade. | Dados e comportamento **diferentes** dos benefícios. | Não usar como segundo consumidor só para forçar reuso |
| `/about/` e `/how-it-works/` | HTML editorial semântico, publicado no próprio documento, com conteúdo independente. | Forçar componentes JS para ganho aparente prejudicaria a renderização inicial/SEO. | Não migrar nesta fase |
| `/viewer/` | Projeção pública allowlist, cena, vistas técnicas e ações de seleção; `viewer/data.js` controla ordem dos blocos. | Já possui componentes e composição próprios, mas responsabilidade e semântica não equivalentes a vantagens editoriais. | Reavaliar por contrato futuro, **sem adaptar ao manifesto da Landing agora** |
| `/config/` e Admin | Fluxos, política de apresentação, permissões, dados V5 e autoria. | Reuso legítimo já existe dentro do domínio; nova camada universal daria acoplamento e migração arriscada. | Preservar |

**Resultado da procura:** segundo consumidor genuíno **na mesma página/domínio**. Não há até aqui prova de um segundo **consumidor entre páginas**, portanto não promover o runtime experimental a infraestrutura global. Se a única economia é local à Landing, o módulo deve permanecer local e o core não deve contaminar outras rotas.

## Decisões P3 tomadas para o experimento

1. **Autoridade de conteúdo editorial:** mover os três rótulos compactos e seus paths de ícones dourados da função `renderBenefits()` para `app/landing/data.js` como `miniBenefits`. Manter valores exatos: `Modular`, `Inteligente`, `Para a sua vida`, assets `gold/modular.svg`, `gold/inteligente.svg`, `gold/para-sua-vida.svg`. Os quatro benefícios `white/` continuam inalterados.
2. **Um único contrato de conteúdo para as duas instâncias:** itens `{label,icon}` e lista ordenada. Cada `dataRef` é fonte própria, `landing.benefits` e `landing.miniBenefits`; uma falha de conteúdo não inventa valores.
3. **Uma única definição especializada com variantes fechadas:** renomear apenas o **tipo experimental** de `landing/benefit-strip@1` para `landing/benefits@1`, admitindo `standard` e `compact`; formato de HTML/asset e CSS pertencem à variante, não ao usuário/Admin.
4. **Preservar o visual e a semântica de cada consumidor:** `standard` produz `div.benefit-item > img[alt=''] + span` e `compact` produz `div.mini-benefit > img[alt=''] + strong`. Não unificar classes, elementos de texto ou folhas CSS.
5. **Versão/isolamento:** o tipo experimental nunca foi persistido nem publicado. A mudança de nome **não** é migração de contrato produtivo. O JS continua como IIFE/registrador tipado em código, sem alteração do Admin, Netlify, Scene2D, Viewer, preços, configuração ou auth.
6. **Validação:** o parser `dataRef` passou a aceitar chaves camelCase seguras (`miniBenefits`), mas continua bloqueando `constructor`, `prototype`, `__proto__` e getters. Um teste de cutover anteriormente vinculado ao ícone inline em `landing.js` foi refeito para conferir `landing/data.js` + componente registrado; **não enfraquecer a checagem de origem dos assets**.
7. **Duas montagens independentes e falha explícita:** ambas passam por compilação/validação e `DocumentFragment`. Falhas não são compensadas com dados falsos; o componente afetado mostra mensagem e as demais áreas da Landing continuam. Bloqueio do script compartilhado deve deixar **ambas** as faixas indisponíveis, sem derrubar seleção, carrossel e navegação.
8. **CI sem deploy e com proteção de custo:** comparar candidata e `main` servidas localmente, sem PR do produto ou Netlify preview; workflow da branch configura cancelamento de execuções obsoletas. Nenhuma branch de produção será alterada sem novo gate.

## Gates P3 estabelecidos

- `node --test tests/landing-benefit-composition.test.cjs`: 10 testes cobrindo variantes, fonte ausente, payload inválido, DOM semântico e isolamento.
- `node tests/public-cutover-contract.cjs`: manter as garantias de site root/Viewer e validar que paths dos benefícios agora são declarados.
- `tests/landing-benefit-browser-gate.mjs`: `main` vs branch, 390/1366 px, light/dark, **ambos grupos** com igualdade de DOM, CSS computado, geometria e screenshots recortadas (4 cenários).
- `tests/landing-interaction-gate.mjs`: Chromium 390, WebKit 390/1366, menu conforme breakpoint, cozinha, 5 ambientes, 7 benefícios somados; falha de script injetada sem exceções não tratadas.
- Adotar resultado somente após CI **final**, não inferir PASS de workflows intermediários: commits parciais geraram falhas de build/contrato transitórias enquanto o código e os testes estavam sendo atualizados, e devem ser classificados por revisão SHA.

## Critério de promoção / parada

**Se os gates fecharem verdes**, declarar reuso funcional legítimo de um contrato *na Landing*, sem declarar economia líquida de código, UX aprovada ou prontidão de um sitewide page builder. Antes de inserir outro consumidor no runtime, medir custo/coupling e identificar um consumidor de **outra página com mesma semântica de dados e requisitos de acessibilidade**, não meramente semelhança CSS.

**Se os gates divergirem:** restaurar a apresentação anterior na branch experimental; o contrato tem de ser adaptado ao DOM/CSS aceitos, não o inverso.

O foco da etapa é a arquitetura de autoria/leitura de conteúdo, não a criação de um CMS nem adoção de React, CSS Modules ou schema universal de aplicação.
