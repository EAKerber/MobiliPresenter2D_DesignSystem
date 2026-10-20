# UI-ADR-005 — Controlador único do menu público sem migrar o HTML para JSON

**Data:** 2026-10-20  
**Estado:** **P4-NAV primeira validação diferencial PASS; verificação final de foco NAV-004 em execução.** Não homologado para merge, publicação ou alteração visual de NAV-005.  
**Produto de referência:** `EAKerber/MobiliPresenter2D@1878ae1057ce7c6190e0c8cb08a1f3baadd49463` (`main`), candidato `experiment/shared-public-header-controller-20261020`.  
**Design System:** `EAKerber/MobiliPresenter2D_DesignSystem`, `architecture/dom-css-consolidation-20261020`, [PR #39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39).  
**Decisão mãe:** [UI-ADR-004](ui-adr-004-cross-page-reuse-gate-2026-10-20.md) — compartilhar controlador do cabeçalho **sem** renderizar cabeçalho por JS nem estender PageComposition.

## Inventário P4-NAV-0 por leitura de código

| Rota pública | Markup/cascata | Controlador antes do experimento | Estado ao clicar, Escape e fora |
|---|---|---|---|
| `/` Landing | `header.site-header`, `#menuToggle`, `#primaryNav`, `landing.css`+`ui-theme.css` | trecho no final de `app/landing/landing.js`, junto ao carrossel | click alterna `.menu-open`; link fecha; **sem fechamento explícito por Escape/fora** |
| `/about/` | mesmo shell semântico e folhas | `app/landing/header-menu.js` como script defer | click alterna; link fecha; Escape fecha; `pointerdown` fora fecha |
| `/how-it-works/` | mesmo shell semântico e folhas | IIFE inicial de `app/how-it-works/how-it-works.js` | click alterna; link fecha; Escape fecha; `pointerdown` fora fecha |

A Landing mantém um `pointerdown` e `keydown` globais com `{once:true}` para parar dicas animadas; essa lógica **não** deve ser confundida com controlador de menu ou removida.

## Decisões P4-NAV-1 experimentais

1. **Selecionar `app/landing/header-menu.js` já existente como autoridade de comportamento** para as três páginas. Não criar novo schema, componente de DOM, framework, duplicata de controller ou dependência do Admin.
2. Preservar integralmente o HTML e a estrutura nativa `nav/a/button`, seus IDs, rotas, `aria-current`, `aria-expanded`, rótulo, tema e CSS. Não alterar `landing.css`, `ui-theme.css`, `about.css`, `how-it-works.css`.
3. Na Landing, carregar um único `header-menu.js` antes de `landing.js`; remover exclusivamente os listeners/procedimentos de menu embutidos, **mantendo stopHint, carousel, animações e dados**.
4. Em Como funciona, carregar o mesmo script antes de `how-it-works.js`; remover apenas a IIFE inicial de menu, **mantendo a IIFE do painel explicativo**.
5. Quem somos já utiliza o controlador selecionado. Preservar todo HTML/CSS do cabeçalho, mas versionar a URL do script compartilhado para atualização de cache quando o foco NAV-004 for aperfeiçoado; testar a rota na mesma matriz.
6. **Mudança deliberada de interação na Landing:** fechar pelo Escape e pelo pointerdown fora, para aderir ao comportamento pré-existente em About/How. Essa uniformização exige gate de foco/teclado/pointer e registro da diferença; não é homologação visual automática.
7. O benefício de simplificação pode ser real sem existir um segundo consumidor de `PageComposition`: compartilhar estado/comportamento transversal é **arquitetura distinta** de compor páginas a partir de dados.
8. Manter piloto em **branch do produto independente** da branch `experiment/ui-declarative-landing-benefits-20261020`, evitando unir duas alterações antes dos respectivos gates. Sem product PR, Netlify Deploy Preview ou merge neste checkpoint.

## Arquivos do experimento no produto

| Arquivo | Alteração |
|---|---|
| `app/index.html` | acrescenta referência ao controlador `/landing/header-menu.js` com versão de cache |
| `app/landing/landing.js` | remove controlador duplicado, mantém eventos independentes do carrossel |
| `app/how-it-works/index.html` | acrescenta referência ao controlador compartilhado antes de `how-it-works.js` |
| `app/how-it-works/how-it-works.js` | remove primeira IIFE de menu, mantendo painel de explicações |
| `app/about/index.html` / `app/landing/header-menu.js` | URL do script com versão de cache e melhoria de foco por teclado, sem alteração de markup estrutural nem CSS |
| `tests/public-header-controller-gate.mjs` | comparação diferencial e testes de comportamento de menu |
| `.github/workflows/public-header-controller-isolated.yml` | CI com baseline main/candidato em dois localhost, Chromium/WebKit, sem deploy |

Contagem das alterações iniciais em fontes HTML/JS, sem registrar custo de gzip/bundle: `landing.js` -663 caracteres, `how-it-works.js` -960, `index.html` +74, `how-it-works/index.html` +94; saldo aritmético local de **-1455 caracteres** nesses quatro arquivos, com uma requisição adicional ao script compartilhado em cada rota migrada. Isto **não é** medição de rede/performance.

## Gates obrigatórios

- **P4-NAV-A:** as três páginas devem carregar em baseline e candidata, em 390 e 1366 px, claro e escuro, sem exceção JS. Uma única referência ao controlador compartilhado por página candidata.
- **P4-NAV-B:** markup de header, ARIA, cores e geometria computados, capturas do header fechado e menu aberto (mobile) comparados bit a bit com baseline equivalente, salvo a nova política de encerramento da Landing.
- **P4-NAV-C:** click no toggle (sem double listener), Enter com foco, Escape, pointerdown fora, link que fecha menu, comportamento desktop inline, `aria-expanded`, class `menu-open`; avaliar Chromium e WebKit.
- **P4-NAV-D:** Landing continua com 5 ambientes, 3 mini-benefícios, 4 benefícios, seleção de cozinha e mecanismos de `stopHint`; `how-it-works` continua carregando os painéis explicativos.
- **P4-NAV-E:** não criar PR de produto/deploy só para descobrir impacto. Trabalhar na branch e em CI local; manter revert simples por fileset.
- **P4-NAV-F:** não concluir compatibilidade iPad físico ou todas as interações a partir de testes WebKit automatizados.

## Regra de parada e evolução

Se a substituição alterar visual, introduzir double listeners, quebrar painel Como funciona ou interromper animação de dicas, corrigir ou reverter na branch; não ajustar CSS nem `decisions.json` para esconder regressão. Se gate PASS, manter como simplificação técnica e avaliar review/PR em checkpoint separado; não acoplar ao schema experimental de benefícios.

**Nota:** este ADR é decisão técnica de experimento. Decisões de comportamento visual homologadas em NAV-005 mantêm prioridade, e qualquer contradição exige revisão explícita antes da publicação.

## Evidência e decisão de foco — NAV-004

**Referência normativa recuperada:** `decisions.json` na `main` do Design System: NAV-004, `functional-contract-approved`, determina que o menu público responda a Escape/clique fora, aceite teclado, mantenha `aria-expanded`, devolva foco quando adequado e respeite `prefers-reduced-motion`. NAV-005 é decisão estrutural e visual separada; não será reaberta para este ajuste.

### Primeiro gate no produto

A execução [Actions #39507803390](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39507803390) passou **12/12 comparações** de DOM, estilo computado, geometria e pixels de header fechado/aberto, para 3 rotas × 2 larguras × 2 temas em Chromium; passou também **12/12 testes funcionais** (3 rotas × 2 larguras × Chromium/WebKit), sem exceções capturadas. Esta execução validou a reutilização do controlador **antes** do acréscimo de restauração explícita de foco.

### Ajuste técnico seguinte

1. Ao abrir o menu móvel pelo teclado (`click.detail === 0`), o controlador agora posiciona foco no primeiro link de navegação. Isso corrige a ordem do DOM móvel, em que o `nav` vem antes do `button`, impossibilitando descobrir os links com Tab imediatamente após o botão de abertura sem manejo de foco.
2. Ao fechar com Escape, se o foco estava dentro do `nav`, devolvê-lo ao botão; se o foco estiver em outro lugar, não forçar a transferência.
3. Cliques de ponteiro continuam sem transferência forçada de foco para o primeiro link. Clique fora apenas fecha; não desloca foco artificialmente. A lógica de `stopHint` da Landing continua independente.
4. `app/about/index.html` recebeu **somente versão da URL** `/landing/header-menu.js?v=nav-controller-p4-1` para evitar que o navegador mantenha controller antigo em cache; HTML estrutural e CSS não foram alterados.
5. O teste foi ampliado para conferir Enter → primeiro link com foco → Escape → botão com foco, além dos gates de visual. A execução final para esse ajuste deve ser registrada **separadamente**; não usar o PASS anterior como prova de comportamento ainda não testado.

**Regra de aceitação:** restaurar foco sem modificar capturas abertas com ponteiro, sem duplo listener e sem prejudicar navegação por mouse ou toque. Não alterar `decisions.json`; o contrato NAV-004 já aprovado é a autoridade.
