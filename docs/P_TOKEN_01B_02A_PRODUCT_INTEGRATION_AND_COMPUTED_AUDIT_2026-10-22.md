# P-TOKEN-01B / P-TOKEN-02A — pin DS→produto e leitura real de CSS, sem redesign

**Data:** 2026-10-22. **Estado:** P-TOKEN-01A **MERGED DS MAIN**; P-TOKEN-01B **BRANCH PRODUTO / CI PASS**; P-TOKEN-02A **BROWSER READ-ONLY PASS**; **CSS ATIVO/RELEASE: NÃO AUTORIZADO**.

## 1. Referências canônicas e estado

| Campo | Fonte verificada |
|---|---|
| Design System `main` após PR #49 | [`70f0eabf609b5b4391459c426d6f7ecaeac070c8`](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/commit/70f0eabf609b5b4391459c426d6f7ecaeac070c8) |
| DS exporter / manifesto | [`scripts/export-approved-palette.mjs`](../scripts/export-approved-palette.mjs), [CSS](../dist/approved-palette-reference.css), [manifesto](../dist/approved-palette-reference.manifest.json) |
| Decisão visual | `decisions.json > VIS-002.approvedPalette`; `implementationAuthorized=false`, fonte blob `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa` |
| Produto `main` analisado | `840a0cda361b3ce215fc934badc26df72dffc6e8` |
| Branch isolada produto | [`architecture/p-token-01b-reference-pin-20261022`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/p-token-01b-reference-pin-20261022), sem merge/PR ou Deploy Preview |
| PIN e auditoria de valores | `design-system/pins/vis-002/v0.1.0/` e `design-system/audits/p-token-01b-current-css-literal-observations.json` na branch de produto |
| Pin source/static CI | [Actions #39770241509 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39770241509) |
| Auditoria computed/browser CI | [Actions #39770637659 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39770637659), SHA `854cc05896523567e503f42af2b8e209c7591b31` |

O primeiro gate de produto confere os **Git blob hashes dos dois artefatos DS**, o commit de origem, o inventário lexical e a não utilização dos tokens nas oito páginas e folhas. O segundo gate confere que `app/`, `netlify.toml` e `package.json` **não mudaram contra a main** e inspeciona o CSS computado em navegador. A saída detalhada da auditoria de navegador foi anexada ao run em `artifacts/p-token-02a/computed-style-observations.json` (retenção do Actions: 14 dias). Os fatos essenciais estão registrados neste documento para não depender do artefato efêmero.

## 2. Artefato executável do Design System

A PR [#49](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/49) introduziu gerador determinístico Node, CSS de **16 variáveis `--ds-reference-*`** e manifesto: 7 papéis de cor × 2 temas + largura e offset de foco. Não se criou uma segunda fonte editável: os valores são derivados da decisão original, conferidos por hash e `--check` em CI.

A distribuição no produto é um **vendor pin fora de `app/`**; NÃO existe import CSS, alias de tema, replacement de valores ou componente consumindo essas propriedades. Este estado satisfaz a integração de proveniência/entrega, **não** a adoção visual de tokens.

## 3. Evidência CSS lexical x computed — não confundir

**Estática:** oito folhas CSS inspecionadas; **54 correspondências hexadecimais exatas** entre declarações existentes e os 14 valores-base de VIS-002. Coincidência de literal não comprova mesmo papel semântico nem substituição segura.

**Navegador em localhost:** **4 rotas** (`/`, `/about/`, `/how-it-works/`, `/viewer/`) × **2 larguras** (390 e 1366 CSS px) × **2 temas** × **2 engines** (Chromium, WebKit) = **32/32 PASS**. JS de tema executado, leitura de CSSOM e elementos; nenhum token `--ds-reference-*` presente em `:root`. O gate é de **observação estática/dinâmica**, não de equivalência antes-depois da migração, autenticação/Admin, pixel capture, acessibilidade com foco real nem dispositivo físico.

| Valor computed/observado | Light | Dark | Observação |
|---|---|---|---|
| `--public-bg` | `#f7f5f2` | `#111210` | Igual nas quatro rotas e engines amostradas |
| `--public-surface` | `#fff` | `#1b1c1a` | Igual nas quatro rotas e engines amostradas |
| `--ui-theme-focus` | `#6e512e` | `#d8bc7c` | Token em `:root`, **não** prova do foco enquanto tecla Tab é pressionada |
| Header público primário | `rgba(255,255,255,0.94)` | `rgba(27,28,26,0.94)` | Landing/About/How |
| Header secundário Viewer | `rgb(255,255,255)` | `rgb(27,28,26)` | Variante NAV-005 distinta |

Em 32 cenários, `--ds-reference-surface-light` computado vazio: **não houve ativação inadvertida**.

### Gaps visuais concretos antes de trocar aliases

| Papel candidato | Produto atual | Paleta homologada como referência | Regra |
|---|---|---|---|
| `canvas.light` | `--public-bg: #F7F5F2` | `#E8E3DC` | **VALORES DIFERENTES**; mudar seria redesign |
| `surface.light` | `--public-surface: #FFFFFF` | `#F0EDE8` | **VALORES DIFERENTES** |
| `textPrimary.light` | `--public-text: #22211F` | `#292723` | **VALORES DIFERENTES** |
| `canvas.dark` | `--public-bg: #111210` | `#171614` | **VALORES DIFERENTES** |
| foco do toggle | CSS local: outline 3px, offset2 | referência: 4px, offset3 | **mudança de aparência**, não generalizar |

Esses resultados **não reabrem** a homologação da paleta A nem autorizam aplicá-la automaticamente. A exceção de alcance faz parte do contrato `VIS-002`: a referência visual aprovada e o CSS atual coexistem enquanto falta mapeamento e validação por componente/superfície.

## 4. Gate honesto ARC-02/04/14/15/16

- **PASS:** origem executável no DS, versão, exportação determinística com integridade, artefato de distribuição produto pinado, controle de não ativação no produto, 54 correspondências lexicais catalogadas, 32 observações CSSOM de páginas públicas sem alteração de runtime.
- **HOLD:** definição de papel por componente/rota/superfície, associações de aliases, correções cromáticas, foco/teclado efetivo, testes de contraste composto e snapshots antes-depois, integração e release de CSS ativo, cobertura funcional privada/Admin autenticada. Não afirmar progresso em tokens aplicados.
- **Fora do escopo:** `P-COMP-01` continua separada em sua branch `architecture/p-comp-01-public-menu-20261021` tecnicamente aprovada mas não merged; i18n/ARC-13 segue própria trilha; não iniciar CMS, schema universal ou móveis fictícios.

## 5. Próximo incremento P-TOKEN-02B (sem pedir decisões prematuras)

1. Montar uma matriz de **uso semântico por seletor/propriedade/tema/rota/superfície/estado** a partir da amostra CSSOM e `decisions.json`; mapear `same-value` apenas quando o **papel** também coincide.
2. Identificar uma primeira propriedade que possa passar de literal aprovado para `var(--ds-...)` **sem alterar pixel** nem trocar autoridade de CSS; caso não exista mapeamento homologado, **parar no plano**.
3. Definir separadamente proposta de mudança visual para os papéis atualmente distintos (`--public-bg`, `--public-text`, outlines), e pedir decisão/homologação só se for necessária para executar.
4. Preparar PR explícita de produto apenas quando houver consumo aprovado e matriz de regressão, evitando previews redundantes.
5. Não importar `dist/approved-palette-reference.css` diretamente: é um artefato de referência; próxima distribuição pode criar aliases nomeados por componente, com gate por contexto, mantendo DS como fonte executável.

**Veredito:** a fundação DS→produto está tecnicamente operacional e isolada; **nenhuma melhoria visual foi aplicada nem publicação realizada**. Próximo ganho real depende de delimitar o primeiro consumidor apto, em vez de usar substituição mecânica de cores.
