# CI-BASELINE-01 (pendência controlada) e ARC-03 — protótipo de fragmento público

> **Evolução posterior ARC-03B (22/10):** [compilador de três páginas completas e gate visual 60/60 PASS](ARC03B_AUTHORED_PAGES_STATIC_COMPILER_BROWSER_GATE_2026-10-22.md). A branch isolada guarda arquivos-fonte de autoria e gera HTML somente em `artifacts/`; nenhum arquivo de `app/` ou build Netlify foi modificado. O estado ARC-03 descrito abaixo era apenas de fragmento/prova estática; **ARC-03C ainda necessário para cutover de produção**.


**Data:** 2026-10-22. **Estado:** #233 **CORRIGIDA NA MAIN DO PRODUTO**; #232 **PENDENTE, CAUSA CONFIRMADA, NÃO CONTORNAR**; ARC-03 protótipo **PASS estático, ISOLADO SEM RUNTIME/DEPLOY**.

## 1. Pendência explicitamente preservada

[Issue #232](https://github.com/EAKerber/MobiliPresenter2D/issues/232) continua **ABERTA**: os testes de browser do Configurador acessam `/config/` sem sessão. [Diagnóstico não autenticado #39849284220](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39849284220) demonstrou que, em produção e no deploy-preview-231 já existente, ambos redirecionam para `/access/`. Logo, o bootstrap e os objetos `CASA_EM_MODULOS_DEBUG`, `CASA_KEYBOARD_SHORTCUTS` etc. não estão disponíveis naquele contexto.

**Ações ainda não autorizadas/realizadas:** nenhuma fixture de auth, criação de conta/teste privado, segredo CI, relaxamento de acesso, supressão de checks nem conversão de `BLOCKED_AUTH_FIXTURE` em `PASS`. A issue contém evidência, hipóteses descartadas, owner técnico por camada e critérios para diagnóstico autenticado com mínimo privilégio. Não confundir isso com os defeitos reais de login/Admin [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212), [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213) e [#222](https://github.com/EAKerber/MobiliPresenter2D/issues/222).

[P-TOKEN-01B/02B PR #231](https://github.com/EAKerber/MobiliPresenter2D/pull/231) continua **DRAFT/HOLD para merge**, embora o gate de cor contextual 48/48 tenha passado. Nenhum preview novo deve ser criado apenas para repetir o diagnóstico.

## 2. Correção independente de CP-PUBLIC-02a efetivamente integrada

- [Issue #233](https://github.com/EAKerber/MobiliPresenter2D/issues/233) **FECHADA COMO COMPLETED** depois do readback na main.
- [Produto commit `303468b4ddbb07a761316abca28901ccaea219df`](https://github.com/EAKerber/MobiliPresenter2D/commit/303468b4ddbb07a761316abca28901ccaea219df) modificou **somente `tests/public-module-projection.test.cjs`**. Conteúdo do arquivo atualizado tem SHA Git blob `6a8faec2f00e0d7cd26084a1927fb6a5d9c660c3`, igual ao da branch isolada testada.
- [Run #39848703737 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39848703737) validou sintaxe, projeção pública, endpoint, adaptadores e ausência de alteração em `app/`, `netlify/`, `package.json`, `netlify.toml`.
- Mudanças limitadas a asserts `publicState.viewerEntities`, allowlist com `nominalDimensionsMm`, inspeção de dimensões e ausência de `basePriceCents` quando não autorizado. **Não alterou projeção, preços, schema V5, Auth ou build.**
- Integração direta do arquivo **sem abrir PR para evitar um novo Deploy Preview**, após gate isolado. Não transportar para main o workflow efêmero da branch de teste.

## 3. ARC-03 — primeiro fragmento HTML compartilhado (somente prova de compilador)

Decisões arquiteturais [ARC-01..16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md) pedem HTML estático com fragmentos build-time, no contexto Vanilla, sem custo de renderização frontend e sem sacrificar paridade visual.

**Branch produto:** [`architecture/arc03-primary-header-fragment-prototype-20261022@2848dd59db012eb3c9781545998facab8a820be2`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/arc03-primary-header-fragment-prototype-20261022), derivada da main após a correção #233.

**Artefatos e função:**
- `architecture/fragments/primary-header.fragment.html`: estrutura única canônica para o header público de profundidade 1.
- `architecture/fragments/primary-header.routes.json`: três contextos explícitos de `/`, `/about/`, `/how-it-works/`: URLs relativas distintas, `aria-current` por página, estado de `aria-hidden` da imagem WhatsApp tal como hoje renderizada. Essas diferenças **não** foram uniformizadas silenciosamente.
- `scripts/compile-primary-header-prototype.mjs`: preenche slots de strings estáticas validadas, exige exatamente um header primário e compara marcação com a fonte existente usando normalização **apenas de whitespace entre tags**. Exige preservação da página fora do header, falha em divergência. Em `--check`, não escreve arquivo; em `--emit-scratch`, emite somente sob `artifacts/arc03-preview-only` (fora de `app/`).
- `tests/arc03-primary-header-prototype.test.mjs`: verifica 3/3 fontes, `aria-current` único, IDs, exceção acessível da imagem, negativa para entradas e markup inválidos, header de Viewer NAV-005 distinto.
- `.github/workflows/arc03-primary-header-prototype-gate.yml`: CI por push **somente nessa branch**, Node 22 sem dependências externas de browser, sem PR nem Netlify Deploy Preview.

[GitHub Actions #39852406075 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39852406075), commit `2848dd59db012eb3c9781545998facab8a820be2`. **Comparação: cinco arquivos novos, zero arquivos de `app/`, nenhum ajuste de `package.json`/`netlify.toml`/`netlify/`.**

**Limite de evidência fundamental:** markup normalizado idêntico não prova equivalência de DOM sob JS, CSS computado, pixels, foco ou funcionamento mobile. Além disso, as fontes HTML originais continuam em `app/`. Portanto ARC-03 é **POC de compilador e contrato**, e não desduplicação aplicada no site. O Viewer de profundidade 2 **não pode herdar este fragmento primário**; sua variante NAV-005 segue separada. Não mesclar protótipo no build de produção ainda.

## 4. Próximo incremento ARC-03B (independente da auth)

1. Separar arquivos fonte canônicos de HTML e saída publicada `app/`, sem sobrescrever manualmente as páginas existentes no mesmo diretório. Definir regra de transformação determinística e reversível.
2. Transformar o POC em pipeline compilador com **manifesto de entradas/saídas e gate de arquivos gerados obsoletos**, mantendo `npm run build` do Netlify estável até homologar a mudança.
3. Gate automatizado **antes/depois** das três rotas, largura 320/390/486/768/1366, light/dark, Chromium/WebKit para header fechado e menu aberto, keyboard focus, DOM, aria, cor e CSSOM; comportamento do header secundário Viewer e navegação privada como controles negativos.
4. Validar o patch já testado do controlador público **P-COMP-01** separadamente, sem misturar estrutura, CSS ou conflitos de auth.
5. PR explícita só quando houver evidência de produção e plano de rollback; evitar preview redundante.

**Veredito:** pendência de autenticação foi registrada e continua não resolvida por opção deliberada; foi possível avançar de maneira independente com teste público corrigido na main e com protótipo ARC-03 testado sem risco de publicação.
