# Proposta v0 — arquitetura CSS por contratos de componentes (2026-10-20)

> **Leitura atual (20/10/2026):** esta é uma proposta conceitual **ainda não implementada** para reestruturação de CSS. A prontidão real, fases e blockers estão no [plano diretor](DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md), no [gate da etapa atual](CSS-READINESS-AND-CURRENT-GATE-2026-10-20.md) e no [registro de riscos](CSS-OWNERSHIP-RISKS-2026-10-20.md). Pilotos de JS concluídos desde sua redação **não** são autorização para aplicar a estrutura proposta aos oito CSS em massa.


> **Estado:** arquitetura candidata para revisão; não homologada, não implementada e sem alteração do repositório de produto.  
> **Base de evidência:** [baseline DOM × CSS](dom-css-consolidation-baseline-2026-10-20.md), `visual-inventory.json`, `DECISION_APPLICATION_MAP.md`, `PALETTE_APPLICATION_MAP.md` e `decisions.json`.  
> **Objetivo:** reduzir duplicação e acoplamento entre páginas mantendo a identidade visual já aprovada. O design de CSS não deve antecipar decisões pendentes de componente.

## Princípio de arquitetura

Separar **identidade de estilo** (`tokens`), **contrato comportamental/semântico do componente**, **composição da página** e **adaptação contextual de tema/responsividade**. Duas regras idênticas não precisam virar um componente; dois componentes com mesmo papel não precisam ter a mesma aparência.

O CSS atual é distribuído em `public-theme.css`, `ui-theme.css`, `styles.css`, folhas próprias de Landing/Como funciona/Quem somos/Admin/Viewer. `ui-theme.css` opera hoje como conjunto transversal de variantes e overrides: sua decomposição deve ser feita **por consumidor**, não por recorte de linhas às cegas.

## Forma lógica proposta (pastas são nomes provisórios)

```text
app/
  styles/
    foundation/
      tokens.css            # somente papéis/valores homologados; tema claro/escuro
      base.css              # defaults globais mínimos e typography
      accessibility.css     # .visually-hidden, foco compartilhado comprovado
    primitives/
      button.css            # núcleo de botão, variantes com contrato definido
      field.css             # campo/controle, sem regras admin-específicas
      media.css             # imagens responsivas, somente comportamento realmente comum
    components/
      navigation/
        public-header.css   # NAV-004/NAV-005; contrato público
        private-header.css  # PRIVATE-HEADER-001/NAV-005; contrato privado
        menus.css           # controle/toggle/overlay; partes compartilháveis
      branding/
        logo.css            # asset e encaixe; slots por header ficam no consumidor
      feedback/
        status.css          # estados semânticos (com escopo e superfícies)
        pending.css         # loading/erro/retry; só após EST quando aplicável
      scene/
        scene-stage.css     # quando contrato de cena compartilhado for comprovado
        hotspot.css         # candidato forte: Configurador + Viewer
    features/
      configurator/
        layout.css
        module-card.css
        selection.css
        summary.css
      viewer/
        layout.css
        technical-view.css
        detail.css
      administration/
        layout.css
        editor.css
        access-controls.css
    pages/
      landing.css
      how-it-works.css
      about.css
      access.css
    entrypoints/
      public.css            # conjunto compartilhado necessário a rotas públicas
      config.css            # shared + features/configurator
      viewer.css            # shared + features/viewer
      admin.css             # shared + features/administration
      access.css            # shared + acesso
```

A estrutura é **lógica**, não uma exigência de criar todas essas pastas agora. Só materializar um módulo quando existir contrato, consumidor e razão concreta para extração. Evitar construir uma biblioteca grande de primitivas antes de provar reutilização.

## Limites e propriedade do CSS

1. **Foundation:** fornece variáveis semânticas e poucos utilitários universais. Não herdar classes amplas como `.button`, `.panel`, `.brand` indiscriminadamente em toda rota.
2. **Componentes compartilhados:** pertencem a contratos efetivamente usados em duas ou mais páginas. Exemplo: cabeçalho público em `/`, `/how-it-works/` e `/about/`; cabeçalho privado em `/config/`, `/admin.html` e páginas de acesso. Viewer tem variante contextual própria.
3. **Features:** domínios com estados e interações próprios. `.module-card` editorial não é `.module-card` selecionável do Configurador; tratar como `editorial-module-card` em `pages/how-it-works.css` e `config-module-card` em `features/configurator/module-card.css` (nomes apenas candidatos).
4. **Páginas:** composição de seções, estruturas editoriais e exceções justificadas; não duplicar header ou botão que já tenham componente estável.
5. **Tokens:** mapear valores homologados de `VIS-002` e pares locais para aliases existentes. Não supor que qualquer `#fff` deve virar `--surface`: assets, desenhos de produto e overlays ficam excluídos.
6. **Variantes de tema e responsividade:** ficam junto ao componente consumidor ou em tokens de tema quando forem papéis globais. Não criar novo `ui-theme.css` monolítico por inércia.

## Normalização lexical — candidatos iniciais

| Hoje | Contrato proposto | Condição antes de implementar |
|---|---|---|
| `.button` (três bases), `.button--primary`, `.button-copper` e afins | `ui-button` básico + variantes semânticas/contextuais de tamanho, forma e ênfase | Comparar usos e estados, não trocar todo HTML de uma vez |
| `.brand`, `.brand__logo`, `.viewer-brand__logo`, `.private-header__brand img` | primitiva logo/imagem + slots de `public-header`, `private-header`, `viewer-header` | Preservar proporções da arte e regras NAV-005 compactas |
| `.eyebrow` | padrão de rótulo/eyebrow com variante editorial/administrativa e tokens próprios | Verificar herança, fundos, contraste e uso semântico |
| `.module-card` em Como funciona e Configurador | dois componentes de domínios distintos | Confirmar escopo no DOM e não exportar CSS global com mesmo nome |
| `.scene-hotspot` | candidato `scene-hotspot` compartilhado, estilos de estado permanecem em features | Conferir hotspots, eventos, target e regressões no Viewer |
| `.visually-hidden` | utilitário único (nome atual pode ser preservado) | Garantir cascade e herança equivalentes |
| `.how-hero-art img` e `.hero-art img` | utilitário ou primitiva de mídia *somente se* houver contrato de imagem comum | Igualdade textual de quatro propriedades não basta |
| `.technical-view`, `.module-detail__*` | potencial compartilhamento Viewer–Configurador de linguagem técnica | Confirmar estrutura gerada por JS e geometria nos dois produtos |

**Não unificar** `.module-card` por homonímia. **Não transformar** `.ui-theme.css` em lista de overrides portados para arquivo novo sem entender o escopo. **Não converter** controles funcionais em `div` para facilitar estilos.

## Carregamento sem introduzir regressão de cascade

Manter entrada CSS explícita por rota e um conjunto compartilhado mínimo. Não inserir todas as folhas globais em todas as páginas. Ordem de carga e regras já publicadas devem ser preservadas enquanto as extrações forem feitas; a primeira fase pode usar **entrypoints que referenciem arquivos componentizados** no mecanismo de build existente, mas não pressupor bundler nem `@import` como solução universal.

A adoção de `@layer` pode simplificar a governança futura; contudo, criar camadas hoje muda precedência da cascata e especialmente a ordem de `!important`. **Não introduzir `@layer` na primeira extração.** Avaliar após medir computed styles e testes de regressão.

O runtime de componentes precisa manter os contratos de eventos/estado existentes (auth/menu, viewer, configurador), evitando criar apenas uma abstração de CSS sem uma fronteira real de marcação e comportamento.

## Primeira sequência de execução proposta

| Gate | Etapa | Artefato / prova | Saída |
|---|---|---|---|
| G0 | Rastreabilidade estática | baseline DOM estático × CSS por rota + homônimos/candidatos | **Iniciada nesta branch** |
| G1 | DOM renderizado e JS dinâmico | match por elemento/regras de origem para light/dark, breakpoints de risco, estados críticos, sessão anon./autenticada; snapshot sem dados pessoais | Classificação estática + DOM + evidência |
| G2 | Ownership e grafo de dependências | por regra: dono, página consumidora, origem, especificidade, custom properties, intenção, variantes | Proposta de mover/renomear sem guesswork |
| G3 | Extrações de risco baixo | `.visually-hidden`; base scene-hotspot se comprovada; imagens simples se houver contrato | Diferença computada zero nos cenários relevantes |
| G4 | Componentes transversais | headers por contrato, botão com variantes, logo + slot, estados | Equivalência funcional/visual e acessibilidade em todos os consumidores |
| G5 | Separação de features | Configurador, Viewer, Admin; renomeação dos homônimos; componentes dinâmicos | nenhum selector leak; sem perda de estilos ou estados |
| G6 | Limpeza e convergência | remover regras duplicadas obsoletas, consolidar aliases, imports e ownership | CSS menor, mais local, rastreável; round-trip de comportamento |

Cada gate precisa de diffs antes/depois em DOM computado para propriedades de risco; inspeção visual real; teste funcional do componente; sem regressão de foco/teclado/reduced-motion. Mudanças de valores visuais fora de correções já aprovadas necessitam homologação própria.

## Pré-requisitos que **não** bloqueiam a arquitetura conceitual, mas bloqueiam migração segura

- DOM renderizado real: há componentes injetados por JS, principalmente `/viewer/`, `/config/`, Admin e navegação. O HTML estático não representa todos os consumers.
- Caminhos de CSS efetivamente carregados por estado, ordem, regra vencedora, custom properties finais e classes introduzidas via `classList` / templates / bundles.
- Reprodução representativa: claro/escuro; mobile estreito e desktop; anonimato e autenticação onde aplicável; seleção/foco/menu/loading/erro; sem registrar dados de conta.
- Revisão explícita do que se considera o mesmo contrato visual/funcional antes de normalizar classes diferentes.
- Baseline do produto e preview para comparar semântica/computed styles, sem alterar `main` e sem extrapolar correções lógicas para decisões visuais.

## Decisão arquitetural que ainda não estamos tomando

Não fixar framework, CSS Modules, CSS-in-JS, Shadow DOM ou nova ferramenta de build. Nenhum deles é necessário para descobrir duplicações e ownership; a escolha dependerá dos contratos reais dos componentes e do mecanismo de empacotamento do produto. A primeira arquitetura pode funcionar com CSS comum, classes prefixadas e entradas por rota.

**Política:** documentar arquitetura no repositório DesignSystem; implementar CSS/HTML/JS somente em fase posterior, no repositório de produto, com autorização específica e gates de regressão.
