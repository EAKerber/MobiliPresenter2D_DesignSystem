# V0-A — reconciliação pós-PR #230, ownership de UI e localização

**Data:** 2026-10-21. **Estado:** V0-A / descoberta estática e indexação de fontes **CONCLUÍDAS**; V0 global **EM ANDAMENTO**, sem implementação ou validação runtime neste incremento.

**Produto observado:** [`EAKerber/MobiliPresenter2D@840a0cd`](https://github.com/EAKerber/MobiliPresenter2D/commit/840a0cda361b3ce215fc934badc26df72dffc6e8). **Baseline histórico do inventário DS:** `1878ae1` de 20/10. **Contrato arquitetural vigente:** [ARC-01…16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md). **Homologações visuais:** [`decisions.json`](../decisions.json), em particular [NAV-005](NAVIGATION_DEPTH_AUTHORITY_GATE_2026-10-21.md). Nenhum valor visual foi homologado por este checkpoint.

## 1. Atividades e fontes verificadas

- Consultados `main` do produto e do Design System, árvore recursiva do produto, `netlify.toml`, `package.json`, `app/scripts/build-static.sh`; amostradas diretamente as **oito entradas HTML**, as **oito folhas CSS** e os controladores JS centrais.
- Comparação GitHub entre `1878ae1` e `840a0cd`: **26 commits à frente**, 0 atrás; alterações relacionadas à UI, auth, pricing, Viewer e How: `app/admin.html`, `app/admin/admin.css`, `app/admin/admin.js`, `app/core/admin-bootstrap-retry.mjs`, `app/core/administration-v5.js`, `app/core/private-navigation.js`, `app/core/public-module-projection.js`, `app/core/ui-theme.js`, `app/how-it-works/how-it-works.css`, `app/viewer/index.html`, `app/viewer/{public-data,scene-adapters,viewer.css,viewer.js}`, `netlify/functions/public-modules.mjs` e gates em `.github/workflows`/`tests/`.
- **Cuidado:** o antigo `VISUAL_INVENTORY.md`, `DECISION_APPLICATION_MAP.md` e `visual-inventory.json` ainda retratam `1878ae1`. Este checkpoint é **um overlay datado**, não substitui automaticamente os snapshots e evidências de renderização desses arquivos.

**Artefatos estruturados deste incremento:**
1. [Matriz de 14 famílias/contratos — ownership, consumidores, risco, duplicação e gates](../evidence/architecture/v0-component-ownership-2026-10-21.json).
2. [Candidatos de localização — HTML e JS público, 543 entradas](../evidence/architecture/v0-text-candidates-public-2026-10-21.json).
3. [Candidatos de localização — JS de core/admin/viewer, 283 entradas](../evidence/architecture/v0-text-candidates-dynamic-2026-10-21.json).

**Interpretação obrigatória:** os 826 registros são **ocorrências candidatas lexicais**, NÃO 826 textos únicos e NÃO cobertura integral dos textos traduzíveis. O scanner pode produzir falsos positivos e duplicados; ele não cobre adequadamente expressões dinâmicas, literais multilinha, arrays utilitários, texto carregado de dados administrativos, componentes gerados em runtime ou frases compostas. Por exemplo, `FULL`/`SHORT` do `app/core/ui-theme.js` podem escapar à heurística contextual. **Não usar esses índices como script para substituição automática.**

## 2. Matriz de rotas e origens de HTML/CSS/JS

| Rota | Entrada HTML | Folhas de estilo | Origem/comportamento principal | Família/contrato |
|---|---|---|---|---|
| `/` | `app/index.html` | `public-theme.css`, `landing/landing.css`, `ui-theme.css` | `landing/data.js` + `landing/landing.js` + `core/ui-theme.js` | Público nível 1; menu em script Landing; carrossel especializado |
| `/about/` | `app/about/index.html` | `public-theme.css`, `landing/landing.css`, `about/about.css`, `ui-theme.css` | `landing/header-menu.js` + `ui-theme.js` | Público nível 1 |
| `/how-it-works/` | `app/how-it-works/index.html` | `public-theme.css`, `landing/landing.css`, `how-it-works.css`, `ui-theme.css` | `how-it-works.js` (inclui menu próprio) | Público nível 1; acordeões e editorial |
| `/viewer/` | `app/viewer/index.html` | `public-theme.css`, `viewer/viewer.css`, `ui-theme.css` | `viewer/viewer.js`, `viewer/public-data.js`, `landing/header-menu.js` e adaptadores de cena | Público nível 2; nav contextual NAV-005 |
| `/config/` | `app/config/index.html` | `styles.css`, `ui-theme.css` | `app.js`, `core/scene-component.js`, V5/projeções, `private-navigation.bundle.js` | Privado; domínio configurável |
| `/admin.html` | `app/admin.html` | `admin/admin.css`, `ui-theme.css` | `admin/admin.bundle.js`, V5, `private-navigation.bundle.js` | Privado; domínio de autoria |
| `/access/` | `app/access/index.html` | `public-theme.css`, `ui-theme.css` | `access/access.js`, `private-navigation.bundle.js` | Privado/acesso; sessão |
| `/access/manage.html` | `app/access/manage.html` | `public-theme.css`, `ui-theme.css` | `access/manage.bundle.js`, `private-navigation.bundle.js` | Privado/acesso; convites e sessões |

**Leituras transversais:**
- **Comportamento de tema já centralizado:** `app/core/ui-theme.js` é carregado nas oito entradas e troca `img[data-brand-variant]`, preferências claro/escuro/auto e estado dos controles. Não recriar esse controlador. Há dispersão de CSS e variações contextuais a auditar.
- **HTML público repetido:** `header.site-header` está presente na Landing, About e How; o Viewer usa **`header.viewer-header`** distinto. A semântica da navegação exige preservar essa variante secundária. 
- **Menu público com controladores concorrentes:** `app/landing/landing.js`, `app/landing/header-menu.js` e `app/how-it-works/how-it-works.js` carregam lógica relacionada. Essa é **duplicação de responsabilidade comprovada por código**, mas sua consolidação requer reconciliar o pós-#230, o contrato NAV-004 e issues de menu.
- **Navegação privada separada:** `app/core/private-navigation.js` integra `@netlify/identity`, roles, logout e estado de sessão. Não substituir pelo controlador público nem assumir que somente o DOM esconde rotas.
- **CSS compartilhado não equivale a classe semanticamente comum:** `ui-theme.css` contém regras para público, Viewer e privado; `styles.css` e `admin.css` têm regras locais. Nomes coincidentes como `.button` ou `.visually-hidden` exigem **comparação de cascade/computed styles** antes de extrair ou declarar equivalência.
- **Domínio da cena:** `app/core/scene-component.js`, adaptadores do Viewer e `app/app.js` já compartilham infraestrutura; manter `ConfiguratorAdministration2D 5.0`, projeções, cena, catálogo e preços sob autoridades específicas. Nenhum teste com móvel fictício integra o gate.

## 3. Indicadores estáticos de CSS no head verificado

| Folha | Linhas | Definições `--var` (ocorrências lexicais) | Literais hexadecimais (ocorrências lexicais) |
|---|---:|---:|---:|
| `public-theme.css` | 27 | 11 | 9 |
| `ui-theme.css` | 351 | 27 | 112 |
| `landing/landing.css` | 197 | 0 | 9 |
| `about/about.css` | 51 | 1 | 1 |
| `how-it-works/how-it-works.css` | 287 | 1 | 23 |
| `viewer/viewer.css` | 171 | 0 | 18 |
| `styles.css` | 854 | 11 | 65 |
| `admin/admin.css` | 218 | 40 | 56 |

Contagens feitas lexicalmente sobre o conteúdo atual e **não comparáveis diretamente** aos 43 nomes de propriedades e 467 ocorrências documentadas no inventário antigo, cuja normalização/contagem é diferente. Uma definição de variável pode reaparecer em múltiplos contextos/temas. **Cores e propriedades observadas não se tornam tokens homologados.** Ainda faltam cascata, CSSOM, DOM real e dados de tema/viewport/estado.

## 4. ARC-13 — cobertura e fronteira de textos

O índice preliminar cobriu **8 entradas HTML e 18 arquivos JS**:
- HTML inclui nós de texto e atributos `aria-label`, `aria-description`, `placeholder`, `alt` e `title` não vazios.
- JS inclui literais em linhas com `textContent`, `label`, `title`, `description`, `placeholder` e propriedades semanticamente próximas; não é parser completo.
- Exemplos atuais: `app/viewer/viewer.js` tem textos de vazio/carregamento/erro; `app/access/access.js` possui mensagens de validação de convite; `app/core/private-navigation.js` inclui menu e erros de permissão; `app/app.js`/`app/admin/admin.js` produzem texto dinâmico de configuração e autoria.
- **Não extrair automaticamente:** identificadores de catálogo, nome técnico de parâmetro, dados V5 editados pelo Admin, preços e mensagens derivadas de usuários. Estes têm autoridade de domínio; serão classificados como `domain`, `UI`, `editorial`, `dynamic-interpolated`, `accessibility`, `nonlocalizable` ou `review`.
- A geração de chaves `pt-BR` e substituição em HTML/JS **não foi iniciada**. O gate próximo exige scanner mais confiável, reconciliação humana/semântica, IDs determinísticos e prova de cobertura; utilizar comparação de texto/atributo por DOM e testes de interpolação segura.

**Quantidade por origem, como prioridade de revisão (não volume real de traduções):**

| Origem | Índice inicial | Exemplos de natureza |
|---|---:|---|
| Oito páginas HTML | 472 | conteúdo editorial, navegação, títulos, formulário, atributos acessíveis |
| JS Landing + How | 39 | conteúdo estruturado, carrossel, estado de menu |
| JS Viewer (`viewer.js` + `data.js`, `public-data.js` sem captura) | 32 | mensagens, títulos, seleção e vistas |
| Outros JS de Core/Config/Admin/Acesso | 283 | mensagens dinâmicas, UI de autoria, controles e estados |
| **Total** | **826** | ocorrência lexical não revisada |

**Correção aritmética de rastreabilidade:** a partição pública contém HTML 472 + JS público 71 = **543**; a partição dinâmica contém JS adicional **283**. A categorização por família acima serve apenas para orientar revisão, não define autoridade do texto.

## 5. Build e distribuição: risco real antes de ARC-02/03

- `netlify.toml` possui `[build] command = "npm run build"` e `publish = "app"`.
- O `package.json` **da raiz** implementa atualmente `npm run build` bundlando `admin/admin.js`, `access/manage.js` e `core/private-navigation.js` com `esbuild`, gravando `*.bundle.js` em `app/`.
- **Distinto:** `app/scripts/build-static.sh` (acionado por caminhos históricos no `app/package.json`) gera `app/dist` para seu próprio pipeline e **não é a saída declarada de publicação Netlify**.
- Para ARC-03, precisamos definir fonte HTML canônica e destino de fragmentos de build de modo que o gerador **não sobrescreva arbitrariamente os HTML de autoria, não duplique fontes de verdade e não dependa de runtime JS** para header/páginas estáticas.
- Para ARC-02/14, exportar tokens homologados do DS com versão/commit pinado para CSS no produto, importado **na ordem controlada da cascata** e revisado por PR; não usar fetch ao DS no navegador nem atualizar produção automaticamente.
- **Ainda não há build novo**. Antes de mudar `npm run build`, elaborar fixture e comparar artefatos de oito rotas, script idempotente e integração Netlify com rollback, sem deploy preview nesse gate.

## 6. Priorização orientada por risco/benefício

| Prioridade | Incremento candidato | Justificativa e gate |
|---|---|---|
| **V0-B / imediato** | Reconciliação de cobertura por **fonte semântica + DOM dinâmico**, revisão de classificação de textos e ownership de CSS | O scanner inicial é somente heurístico; localizar verdadeiros consumidores antes de migrar. Atualizar inventário antigo por overlay, sem apagar evidência histórica |
| **P0 operacional independente** | [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212) e [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213) | Auth/login e estado de sessão; não misturar refatoração de UI com correção transacional |
| **P1 funcional independente** | [#224](https://github.com/EAKerber/MobiliPresenter2D/issues/224) e [#215](https://github.com/EAKerber/MobiliPresenter2D/issues/215) | Carrossel e primeiro clique do menu; não encerrar sem confirmação pós-merge |
| **P1 apresentação NAV** | [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218), [#225](https://github.com/EAKerber/MobiliPresenter2D/issues/225) | Classificar público primário vs Viewer secundário; alterações #230 precisam ser testadas e issues re-triadas |
| **V2 primeiro patch arquitetural** | Gerador DS→tokens CSS + integração **para uma família aprovada** | O menor recorte com consumidor real; garantir equivalência computada e escopo de decisão |
| **V3 primeiro componente compartilhado** | Menu público/controlador + fragmentos por variante ou utilitário pequeno | Compartilhamento já comprovado; só após NAV/bug gates; preservar auth privada e header secundário |
| **V4 localização** | Inventário integral + `pt-BR` e extração em lotes reversíveis | ARC-13 B com execução incremental; não antecipar CMS nem tradução de domínio |

**Compatibilidade iPad legado** é baixa prioridade conforme atualização do usuário após testes recentes; **não** fechar #212/#213 por isso. Extensão real de móveis será avaliada quando houver material real, **sem móveis fictícios como condição de V0**.

## 7. Condição de conclusão V0-B (ARC-16)

1. **Coverage**: todos os caminhos de HTML, JS e dados UI classificados `visited/excluded/unverified`, inclusive strings via `FULL/SHORT`, templates, markup dinâmico, placeholders e textos carregados; markup dinâmico e estados críticos sob prova representativa.
2. **Ownership**: cada componente/variante relevante com responsável, consumidor e origem declarada; duplicações iguais, variantes intencionais, homônimos e casos indeterminados classificados.
3. **Autoridade**: consulta verificável a `decisions.json`, sem novos tokens visuais não aprovados nem mistura com V5/comercial.
4. **Build**: roteiro reproduzível para tokens e fragmentos com entrada/saída/caminho de publicação e proteção de HTML autoral; nenhuma implementação sem verificar a origem correta.
5. **Gate técnico inicial**: um primeiro patch pequeno especificado com cenários de regressão, rollback e benefício concreto; nenhuma duplicação do escopo abandonada sem resolução/exceção/backlog owner.
6. **Persistência**: evidência revisável, instruções de retomada e status; não afirmar browser PASS nem deploy validado a partir desta inspeção estática.

**Veredito V0-A:** **PASS documental para origem de código, versão, partição de scripts/rotas e indexação preliminar; HOLD para promover tokens/componentes e traduzir strings automaticamente**. V0-B ainda aberto. Não houve mudanças no runtime, schema V5, autenticação, preços, assets, PRs ou Deploy Previews.
