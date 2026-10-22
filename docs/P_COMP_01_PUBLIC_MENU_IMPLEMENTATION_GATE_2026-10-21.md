# P-COMP-01 — Controlador compartilhado do menu público: implementação e gate isolado

**Data do checkpoint:** 2026-10-21 (execução Actions final em 2026-10-22 UTC).
**Estado:** **IMPLEMENTADO EM BRANCH / GATE ISOLADO PASS / SEM MERGE / SEM RELEASE**.
**Produto base:** [`main@840a0cd`](https://github.com/EAKerber/MobiliPresenter2D/commit/840a0cda361b3ce215fc934badc26df72dffc6e8).
**Produto candidato testado:** [`architecture/p-comp-01-public-menu-20261021@4ba9384`](https://github.com/EAKerber/MobiliPresenter2D/commit/4ba9384733a8cb46ad8a6c7c8ef3b9aebe25cd93) — **14 commits à frente, 0 atrás** da base no readback.
**Comparação:** [main…branch](https://github.com/EAKerber/MobiliPresenter2D/compare/main...architecture/p-comp-01-public-menu-20261021).
**Autoridade arquitetural:** [ARC-01..16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md), em particular ARC-04/05/06/07/08/15/16.
**Autoridade NAV:** `decisions.json` NAV-004 e NAV-005; não confundir controlador comportamental compartilhado com header primário ou contextual.

## 1. Escopo implementado

Quatro consumidores de menu público `/`, `/about/`, `/how-it-works/`, `/viewer/` utilizam `app/landing/header-menu.js` como única autoridade de comportamento. Antes, a Landing duplicava o controlador dentro de `landing.js`, Como funciona duplicava outra IIFE, e About/Viewer já usavam o módulo compartilhado.

**Mudanças limitadas ao fileset:**
- `app/landing/header-menu.js`: controle único para click, Enter, Escape, link, pointerdown fora, `aria-expanded` e foco. Ao abrir por teclado, foca o primeiro link; ao fechar por Escape, devolve o foco ao toggle **somente se o foco estiver dentro da navegação**. Abertura por ponteiro não rouba foco.
- `app/landing/landing.js`: removidos só `closeMenu`, variáveis `menuToggle`/`primaryNav` e listeners de menu redundantes; `stopHint`, renderização, carrossel e animações preservados.
- `app/how-it-works/how-it-works.js`: removida apenas IIFE inicial de menu; painel `economyDetail` e explicações mantidos.
- `app/index.html` e `app/how-it-works/index.html`: carregam `/landing/header-menu.js?v=p-comp-01` antes do JS da página.
- `app/about/index.html` e `app/viewer/index.html`: versão da URL de controlador alterada para invalidar cache.
- `tests/public-header-controller-gate.mjs` e `.github/workflows/p-comp-01-public-menu-gate.yml`: teste isolado da branch versus `main` sem Deploy Preview.
- **Sem alterações** em CSS, markup estrutural, layout NAV-005 do Viewer, DOM semântico estático, preços, V5, scene/core, backend, acesso ou navegação privada `app/core/private-navigation.js`.

**Não foi feita a posterior composição por fragmentos HTML no build** (ARC-03), nem a exportação de tokens DS→produto (ARC-02/14). São patches independentes.

## 2. Validação reprodutível — gate final PASS

**GitHub Actions:** [run #39697470826 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39697470826), executado no commit **`4ba9384733a8cb46ad8a6c7c8ef3b9aebe25cd93`**.

| Gate | Cobertura real | Resultado |
|---|---|---|
| Sintaxe Node e `tests/public-cutover-contract.cjs` | fontes JS alteradas + contrato público atual | **PASS** |
| Comparação estrutural/visual base vs candidato | **4 rotas × 5 larguras (320/390/486/768/1366) × 2 temas = 40 casos** em Chromium; DOM do header, classes/ARIA, estilo computado amostrado e geometria equivalentes; captura fechada e menu aberto quando visível | **40/40 PASS** |
| Menu funcional | **4 rotas × 2 larguras (390/1366) × 2 motores (Chromium/WebKit) = 16 casos**; Enter, Escape, foco, pointerdown fora, link, sem double listener, comportamento desktop | **16/16 PASS** |
| Header Viewer NAV-005 independente | `tests/viewer-secondary-header-browser-gate.mjs`: **2 motores × 5 larguras × 2 temas = 20 casos**; ordem logo à esquerda, `← Ambientes` / tema / menu à direita, nav contextual, foco, clique e responsividade | **20/20 PASS** |
| Rastreabilidade / liberação | ação isolated push somente branch; `npm install --no-save` de dependências **apenas no CI**, servidores `localhost`, upload de evidência (retenção 7 dias), ausência de merge/PR/deploy | **PASS** |

**Detalhe do visual:** a rotina exige igualdade **exata** de DOM do header, atributos, CSS computado amostrado e geometria; screenshots passam byte a byte quando idênticos. Excepcionalmente, só tolera ruído de rasterização com **diferença máxima de 1/255 por canal e no máximo 0,1% dos pixels**, registrando imagens e diagnóstico. **No run final, não houve nenhuma aplicação dessa tolerância** (zero `P_COMP_01_RASTER_DIAGNOSTIC`).

### Histórico de execução/diagnóstico anterior (não confundir com regressão confirmada)

- [run #39696112733](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39696112733): interrompido na comparação de pixels Viewer/486 px/light após 34 casos de equivalência. DOM e estilo computado não haviam divergido.
- [run #39696459244](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39696459244): divergência reapareceu no mesmo breakpoint, ainda sem alterações de DOM/CSS; adicionada espera para decodificação das imagens temáticas e registro de evidência.
- [run #39696862122](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39696862122): diagnosticou diferença em Viewer/486 px/dark de **13 pixels sobre 31.590**, diferença máxima **1/255** e caixa de 7×2 pixels, compatível com variação mínima de antialiasing/rasterização. O gate foi formalizado para permitir só esse ruído pequeno, sem relaxar verificação estrutural.
- [run #39697470826](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39697470826): **PASS integral, sem ruído tolerado**. Mudanças subsequentes não podem herdar esse PASS sem readback correspondente.

## 3. O que o gate NÃO prova

- Não testa dispositivo iPad legado (conforme prioridade rebaixada pelo usuário).
- Não afirma compatibilidade funcional completa do Admin/logon; `#212`/`#213` permanecem trilhas separadas.
- Não comprova dados de Viewer ou acesso a endpoints Netlify no localhost, nem permissões, preços base e publicação reais.
- Não encerra automaticamente `#215` (splash interceptando clique) ou `#224` (carrossel mobile).
- Não constitui homologação de alteração visual nem aprovação de produção; publicações exigem fluxo de revisão e readback próprio.

## 4. Veredito e handover

**P-COMP-01: GO para revisão de integração**, mantendo **HOLD para merge e release** até decisão de integrar a branch e executar gates operacionais pertinentes. Não abrir PR de produto apenas para obter Deploy Preview; revisão pode começar pelo [diff direto](https://github.com/EAKerber/MobiliPresenter2D/compare/main...architecture/p-comp-01-public-menu-20261021). Se a integração demandar preview, solicitar um único preview deliberado. Revalidar branch contra a main atual antes do merge, pois o presente gate comprova somente `840a0cd→4ba9384`.

**Critério ARC-16 cumprido no escopo:** duplicações do controlador público eliminadas nos consumidores mapeados; header primário/secundário continuam variantes intencionais e sua duplicação HTML segue como backlog ARC-03 de build-time fragments, não defeito desse patch. Menu privado permanece especializado por contrato. JS centralizado em módulo que já existia: sem runtime de componentes, biblioteca UI ou schema universal.

**Próximo recorte independente:** preparar P-TOKEN-01, fazendo inventário dos tokens **homologados por alcance/estado** e desenho de exportação DS→CSS versionada com PR de integração; não misturar com merge de P-COMP-01, revisão de bugs operacionais ou extração de strings i18n.
