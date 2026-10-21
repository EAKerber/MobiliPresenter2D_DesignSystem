# Contratos de navegação por profundidade e gate de consulta obrigatória

**Registro operacional:** 2026-10-21. **Fonte canônica, não substituída por este documento:** [`decisions.json`](../decisions.json), decisões **NAV-004**, **NAV-005** e **PRIVATE-HEADER-001**. **Mapa por rota:** [`DECISION_APPLICATION_MAP.md`](../DECISION_APPLICATION_MAP.md).  
**Objetivo:** evitar que um agente dependa de memória de conversa para distinguir variantes já aprovadas ao criar issue, plano, código, teste ou PR.

> **Importante:** este documento é um *índice de aplicação e protocolo*, não uma nova homologação estética. Se houver divergência, `decisions.json` prevalece. As direções “aprovadas” não equivalem à implementação/publicação realizada.

## 1. Classificar a página antes de propor o cabeçalho

| Classe de página | Rotas/consumidores conhecidos | Autoridade a consultar | Não confundir com |
|---|---|---|---|
| **Pública de primeiro nível** | `/` (Ambientes/Landing), `/about/`, `/how-it-works/` | `NAV-005.wideLayoutPatternsApproved.publicPages`; `NAV-005.compactLayoutPatternsApproved.publicPages`; `NAV-004` | Cabeçalho contextual do Viewer; menu de páginas privadas |
| **Pública de segunda profundidade / contextual** | `/viewer/`, subpágina de um ambiente | `NAV-005.wideLayoutPatternsApproved.secondaryNavigationPages`; `NAV-005.compactLayoutPatternsApproved.secondaryNavigationPages`; `NAV-005.decision`; `NAV-004` | Cópia da estrutura visual da Landing; breadcrumb “Ambientes › Cozinha” imposto por exemplo |
| **Privada (área/sessão)** | `/config/`, `/admin.html`, `/access/`, `/access/manage.html` no inventário atual | `NAV-005.wideLayoutPatternsApproved.privatePages`; `NAV-005.compactLayoutPatternsApproved.privatePages`; `PRIVATE-HEADER-001`; contrato de sessão/autorização | Menu público e estado de usuário inferido do DOM |
| **Nova rota ou profundidade não classificada** | Futuras áreas, ambientes, profundidade ≥3 | **PENDING:** mapear hierarquia de navegação e verificar se contrato aprovado se aplica | Inferir categoria pela URL ou copiar CSS de página semelhante |

A classificação é por **semântica e navegação**, não pela aparência, nome de arquivo ou quantidade de níveis do path da URL. A regra “subpágina de ambiente” não significa que o Viewer só tenha um destino de retorno nem que seu breadcrumb literal esteja homologado.

## 2. NAV-005: distinções vinculantes, sem inventar layout novo

**Público de primeiro nível, largo:** opção A, marca à esquerda, links principais apresentados horizontalmente e contato/tema no grupo de controles à direita.  
**Público de primeiro nível, compacto:** opção A, uma linha com marca à esquerda; tema imediatamente antes do hambúrguer na extrema direita; navegação pública e contato dentro do menu.

**Viewer/profundidade 2, largo (ajuste do usuário em 21/10/2026):** `secondaryNavigationPages`: **logo isolada à esquerda**; no extremo direito, nesta ordem, **← Ambientes → tema → hambúrguer**. O retorno contextual não pertence ao grupo da marca. Tema fica dentro do header.  
**Viewer/profundidade 2, compacto (ajuste do usuário em 21/10/2026):** opção A, **uma linha** sempre que couber; **marca à esquerda**, com **retorno contextual + tema + hambúrguer à direita**. Respeitar min-width e regra de redução já aprovadas quando aplicáveis, sem inventar uma regra universal de breakpoints. Preservar menu global e retorno.  
**Conteúdo do Viewer:** a identificação específica do ambiente fica separada do header; controles da cena ficam no conteúdo, não no cabeçalho. **Não marcar “Ambientes” falsamente como a página ativa** da subpágina.  
**Não homologado:** o texto/traçado de breadcrumb “Ambientes › Cozinha” é apenas um exemplo. Nem todas as dimensões, tipografia/cores de variantes, breakpoints e labels excepcionalmente longos estão resolvidos. O contrato de um header secundário **não é** idêntico ao da primeira profundidade.

**Privado, largo:** opção B; marca e identificador de área/página à esquerda, tema e hambúrguer à direita.  
**Privado, compacto:** opção A, mesma ordem em linha única inicialmente; aplicar a regra de encaixe estreito de NAV-005 (redução de logo limitada a 30%, preservar identificador e usar tema só com ícone quando ultrapassado o limite; fallback quando necessário). Os valores numéricos calculados no campo `compactNarrowFitImplementationSpec` **não** são tokens globais nem implementação aprovada.

**Interação transversal:** NAV-004 aprova botão, clique fora, Escape, teclado, `aria-expanded`, devolução adequada de foco e respeito a movimento reduzido. Compartilhar essa *lógica* pode ser legítimo entre variantes sem compartilhar markup ou composição CSS.

## 3. Gate obrigatório de pré-implementação: AUTHORITY-FIRST

Antes de editar UI, criar issue, estimar CSS, formular um roadmap ou revisar um PR que altere cabeçalho/navegação:

1. **Ler o repositório do Design System atual**, não reconstruir homologações a partir de memória do assistente. Conferir `decisions.json`, data/status, `DECISION_APPLICATION_MAP.md`, este índice e evidências vinculadas.
2. **Registrar explicitamente classe e rota:** primeiro nível público, segundo nível público, privado, ou não classificado. Para rotas novas, classificar antes de herdar contrato; se não houver decisão homologada, usar status **PENDING**, não inventar.
3. **Apontar o caminho exato no JSON:** p.ex. `NAV-005.compactLayoutPatternsApproved.secondaryNavigationPages`; distinguir `status`, `notApproved`, `examplesNotApproved`, `future`, e direções normativas de valores apenas calculados.
4. **Explicitar o que NÃO pode ser copiado:** diferenciar componente de comportamento reaproveitável de layout visual próprio e identificar elementos contextuais que permanecem na página.
5. **Criar matriz antes/depois por variante:** desktop/compacto, tema, retorno, navegação, contato, foco/teclado, estados de sessão e conteúdo, usando testes/inspeção relevantes.
6. **Bloquear implementação se houver conflito entre proposta e decisão homologada.** Corrigir primeiro issue/plano. Somente novas escolhas visuais necessárias retornam para decisão do usuário; escolhas existentes não são rediscutidas nem aproximadas por memória.
7. **Persistir proveniência do gate no produto:** URL do JSON/mapa, ID e caminho, status de autorização, recorte que foi verificado, gaps de compatibilidade e testes. CI bem-sucedida não substitui homologação visual.

**Falha concreta que motivou o protocolo:** [issue #225 do produto](https://github.com/EAKerber/MobiliPresenter2D/issues/225) foi redigida em 21/10/2026 inicialmente como “copiar header público de primeiro nível da Landing” para o Viewer. Isso contrariava `NAV-005.secondaryNavigationPages`, já aprovado e mapeado. A issue e o [plano #229](https://github.com/EAKerber/MobiliPresenter2D/issues/229) foram corrigidos para implementar a variante **segunda profundidade**.

## 4. Aplicação no produto e evidências

| Origem | Código/issue | Estado |
|---|---|---|
| Primeiro nível público | `app/index.html`, `app/about/index.html`, `app/how-it-works/index.html`; issue [#218](https://github.com/EAKerber/MobiliPresenter2D/issues/218) (compacto) | NAV-005 parcialmente não conforme no compacto observado; não copiar a divergência |
| Segundo nível público | `app/viewer/index.html` + `viewer.css`; [#225](https://github.com/EAKerber/MobiliPresenter2D/issues/225) | Implementação atual não segue integralmente o layout secundário homologado; correção planejada, não executada |
| Controlador comportamental (não layout) | `experiment/shared-public-header-controller-20261020`, Actions [#39508130387](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39508130387) | Experimento isolado PASS em três páginas de primeiro nível; não valida layout de profundidade 2 |
| Privado | `app/core/private-navigation.js`; [#212](https://github.com/EAKerber/MobiliPresenter2D/issues/212), [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213) | Auth/menu têm bugs abertos; não migrar para controller público |
| Visibilidade contextual | `NAV-005`; [evidências de compactação](../NAV-005_RUNTIME_VALIDATION_2026-10-18.md) | Valores estreitos recomendados e amostrais não demonstram layout homologado implementado |

## 5. Política de governança

`decisions.json` é autoridade **para decisões**; este índice ajuda a descobrir o caminho correto **sem duplicar homologações**; `DECISION_APPLICATION_MAP.md` liga contratos a rotas; issues/roadmaps do produto contêm a proposta de implementação; CI e capturas contêm evidência e não alteram aprovações. Alterações de NAV-005 devem atualizar essas ligações na mesma revisão, sem sobrescrever campos aprovados.

O objetivo é impedir o erro antes de escrever, não depender de uma lembrança posterior do usuário para corrigi-lo.


## Complemento 21/10/2026 — correção visual após preview do Viewer

O usuário confirmou que o header da PR [#230](https://github.com/EAKerber/MobiliPresenter2D/pull/230) está aprovado com **uma única exceção de alinhamento**: manter a logo à esquerda e mover o link “← Ambientes” para o grupo da direita, imediatamente antes do seletor de tema, seguido pelo menu. **Ordem: `LOGO      [espaço flexível]      ← Ambientes   TEMA   MENU`.** Isto substitui a redação antiga de `NAV-005.compactLayoutPatternsApproved.secondaryNavigationPages` que colocava marca e retorno juntos à esquerda; `decisions.json` foi atualizado com a redação correta.

*Não inferir desse ajuste uma mudança nos headers de primeiro nível, privados, cena ou controle administrativo. Verificação necessária: inspeção nas larguras de 320–1366 px, temas e foco/teclado.*
