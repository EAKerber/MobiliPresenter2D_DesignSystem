# Direção arquitetural — Vanilla Web, componentes/tokens globais e dados por domínio

> **ADENDO NORMATIVO — 16 decisões concluídas (21/10/2026):** [ARC-01…ARC-16 e roadmap de execução](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md) passa a ser o contrato arquitetural atualizado. Este arquivo permanece como contexto e análise anterior ao questionário. ARC-13 adota **extração abrangente de textos localizáveis**, com execução em lotes; ARC-16 exige gate de equivalência/benefício **e** inventário/resolução ou exceção explícita das duplicações reais. HTML compartilhado no build e tokens DS→produto via PR versionada são agora decisões, não hipóteses. Relatos de iPad antigo são melhoria futura baixa prioridade; não usar módulo fictício como experimento obrigatório. Preservar tickets gerais de autenticação e gates reais necessários.


**Data:** 2026-10-21. **Estado:** decisões de direção expressas pelo usuário; desenho técnico de execução e alternativas recomendadas; **nenhuma implementação, token visual novo, migração de dados, merge de PR #39 ou publicação autorizados por este registro**.
**Produto verificado:** `EAKerber/MobiliPresenter2D@840a0cda361b3ce215fc934badc26df72dffc6e8` (PR #230 e controle global de preços integrados).
**Design System:** `EAKerber/MobiliPresenter2D_DesignSystem`, `decisions.json` mantém exclusividade sobre homologações visuais. **Não** incorporar automaticamente documentos experimentais da PR #39, que permanece draft e divergente.

## 1. Direções confirmadas pelo usuário

1. **Stack de interface fixa: HTML, CSS e JavaScript puros.** Não introduzir React, Vue, Angular, Svelte ou bibliotecas/frameworks de UI e CSS-in-JS. APIs nativas do navegador (DOM, `<template>`, módulos JS, CSS custom properties) são a base. Ferramentas existentes de build/teste e dependências de infraestrutura (como Netlify, esbuild nos bundles administrativos e testes) não são, por si, frameworks da interface; eventual alteração dessa fronteira exige decisão própria.
2. **Tokens e componentes são a arquitetura visual de referência de TODO o site**: Landing, Como funciona, Quem somos, Viewer, Configurador, Admin e Acesso. A Landing não recebe exceção arquitetural só porque a investigação `PageCompositionExperimental` começou nela. O objetivo é um proprietário por padrão compartilhado, e variantes explicitamente distintas por contrato.
3. **Data-driven para ferramentas derivadas do núcleo do Configurador**, especialmente Configurador/Viewer e futuras famílias de móveis, onde variações de produto, opções, apresentação declarada e assets justificam schema e projeções. Preservar os contratos existentes e a separação de autoridades: `ConfiguratorAdministration2D 5.0`, `ConfiguratorPresentation2D 1.1`, catálogo/cena, preços tipados, buyer DTO, `PublicModulePresentation2D`, sessão/permissão.
4. **A Landing também consome os componentes e tokens compartilhados**, mas seu conteúdo local em `landing/data.js` não a obriga a adotar um manifesto universal de composição. Dados editoriais simples podem continuar versionados em código.
5. **Objetivo de centralização:** uma alteração compartilhada deve ter **um dono executável**, ser propagada aos consumidores previsíveis e não exigir correções manuais divergentes. Diferentes contratos (ex.: header público nível 1 vs Viewer nível 2 vs privado) continuam variantes distintas mesmo que partilhem elementos e comportamento. A medida é manutenção/consistência por decisão, não percentual da UI em JSON.
6. Generalizar apenas após provar consumidor/variação real ou redução de autoridade duplicada. **Não promover** `PageCompositionExperimental 0.1` a framework obrigatório; aproveitar resultados P1–P4 como evidência e candidatos, não como destino.

## 2. Arquitetura alvo — quatro propriedades, sem motor universal

| Camada | Autoridade | Tecnologia e contrato | Não deve fazer |
|---|---|---|---|
| Decisões de Design System | `decisions.json` + proveniência e matrizes de aplicação | Governança, status, tokens/padrões aprovados por papel, superfície, tema e estado | Tratar valor CSS observado como homologado |
| Fundação e componentes UI | Fonte única para tokens executáveis; componentes HTML/CSS/JS nativos no produto | CSS custom properties semânticas; HTML acessível; módulos/funcões JS responsáveis por `init`/`render`/`update`/`destroy` quando cabível; variantes e estados definidos | Empurrar CSS/markup/handlers arbitrários para JSON de cliente |
| Domínio configurável | V5 + capacidades registradas, catálogo, máscaras/assets, cena, preços, projeções | Variações de famílias conhecidas por dados; novos comportamentos como adaptadores de código sob contratos estáveis; fail closed | Pressupor que qualquer móvel novo exija só máscara ou que exista autor de catálogo completo no Admin |
| Composição de páginas | HTML estático para conteúdo essencial; dados editoriais versionados apenas onde útil | Componentes compartilhados, placeholders/templates estáticos e/ou composição em build time a avaliar; JS apenas onde há comportamento/dinamismo | Universalizar páginas, tornar header dependente de JS para aparecer ou ampliar V5 por motivos de layout |

**Regra de partilha entre repositórios:** Design System define o que é aprovado e onde se aplica. O produto é proprietário da implementação de componentes. Para tokens aprovados e machine-readable, preferir um artefato canônico com exportação determinística e versão/commit rastreável no produto, evitando dois arquivos de valores editados manualmente. Local, formato e gatilho de sincronização são decisões técnicas pendentes; não introduzir geração automaticamente.

**Variantes naturais:** `public-primary`, `public-secondary` (NAV-005 Viewer) e `private` para shell/header são contratos relacionados, mas não um único layout visual. Slots, identidade, tema e menu somente podem ser compartilhados quando preservarem as diferenças aprovadas. Ações por sessão e backend continuam fora de um manifesto de UI.

## 3. Contratos mínimos de componente (direção proposta)

Para cada família compartilhável, inventariar e registrar:
- função semântica, rotas/estados consumidores, dono e variantes suportadas;
- markup HTML acessível e disponibilidade sem JavaScript quando pertinente; `data-*` como hooks estáveis, classes CSS com escopo, atributos ARIA corretos;
- responsabilidades de comportamento (controlador JS puro), eventos, montagem/desmontagem, tema, foco, teclado, toque e `prefers-reduced-motion`;
- tokens de papéis aprovados; nenhuma cor literal promovida automaticamente; cascata, especificidade, @media/container e import order medidos antes de extração;
- garantia de não importar regras comerciais nem permissão no componente de apresentação; ausência de `innerHTML` não confiável, `eval` ou ação arbitrária por string;
- gate de equivalência DOM/computed CSS/geometry/screenshot, interação real, browser e rollback.

**Técnica inicial preferida, não obrigatório no momento:** HTML estático + funções/módulos JS simples + CSS namespaced e custom properties. Web Components/Shadow DOM são opcionais, não requisito; não migrar todos os componentes para Custom Elements apenas por padronização.

## 4. Roadmap reordenado (corrige leitura de G0–G8 e dos experimentos P0–P6)

| Incremento | Resultado mínimo demonstrável | Gate/saída |
|---|---|---|
| **V0 — reconciliar governança e baseline** | Atualizar matriz DS com o produto `840a0cd`, PR #230, preço #228; reconciliar PR #39 (draft/divergente), PR #41 e achados históricos. Classificar decisões por aprovado, direção, candidato, não verificado. | Sem mudança de runtime; um status verificável por rota/família/estado, sem reabrir CP-SD-00–06 |
| **V1 — validar e mapear ownership visual/dinâmico** | Auditar 8 rotas, HTML/CSS + DOM criado por JS, estados e cargas; corrigir regressões confirmadas em PRs pequenos (carrossel #224, splash/menu #215, header compacto #218, contraste #208, auth #212/#213). | Baseline por engine/viewport/tema/estado, causa identificada; não globalizar CSS enquanto cascata/role não estiver mapeado |
| **V2 — tokens e foundation aprovados** | Organizar papéis visuais homologados com tema e componentes consumidores, decidir fonte única/versionamento/export. Extrair candidato pequeno (foco, utilitário ou superfície) e medir diffs. | Nenhuma alteração estética não aprovada; DOM/cascade/contraste e acessibilidade preservados em TODOS consumidores |
| **V3 — componentes compartilhados vanilla** | Padronizar em incrementos independentes: controles de tema, menu/controlador, header por variante, marca, botões, controles/formulários e feedback; incluir Landing, How, About, Viewer, Config, Admin/Acesso explicitamente. | O mesmo ajuste de regra compartilhada passa por uma única implementação; variants intencionais, JS sem duplicação e testes de interação |
| **V4 — layouts e composição específica por domínio** | Padronizar shells/slots/componentes estáticos sem migrar páginas inteiras para JSON. Escolher partials em build time apenas se houver custo real na duplicação HTML; avaliar pilotos Landing P2/P3 por valor/custo, não por investimento histórico. | Páginas essenciais operam sem JS quando apropriado; nenhuma alteração não homologada no layout, na navegação e em auth |
| **V5 — extensibilidade das ferramentas de móveis** | Matriz de `novo móvel` e `nova família`: dados de catálogo, compatibilidade de capacidade, máscaras/alfa, z-order, assets, cena, opções, pricing, DTO Viewer, Admin e testes. Um piloto com nova variante da família existente antes de qualquer schema universal. | Round-trip V5, ausência de dados falsos, cena/Viewer/BOM/valores corretos; alteração de código apenas se nova capacidade real |
| **V6 — hardening e release** | Matriz representativa por risco: 320/390/768/1366, zoom/altura, Chromium/WebKit e iPad real quando possível, claro/escuro, foco/touch, sessão, estados de falha/motion, HTTP autorizado. | Automatizado ≠ screenshot humano ≠ funcional/dispositivo real; CI atual reparado/triado; previews deliberados, rollback, readback |

G0–G8 da PR #39 continuam uma **referência histórica detalhada** a reconciliar, não uma segunda autoridade de roadmap. A direção acima **substitui a meta de universalizar a composição** pela meta de tokens/componentes abrangentes + data-driven restrito aos produtos e ferramentas que justifiquem.

## 5. Pendências técnicas comprovadas ou que exigem descoberta

- **Inventário DS desatualizado:** snapshots mapeiam majoritariamente produto `1878ae1`, embora `840a0cd` esteja em produção. Atualizar mapa de NAV-005, novo preço base, Auth P0 e acordeões antes de afirmar conformidade.
- **PR #39:** documentação e experimentos relevantes, porém draft com conflitos; jamais mesclar todos os arquivos só para trazer este plano. Portar documentos pertinentes para `main` DS com revisões e refs.
- **Headers/menu:** há variações homologadas de profundidade e auth que não devem ser achatadas. Controlador público compartilhado existe em experimento e precisa de reconciliação com #230 e o estado atual. Landing mantém duplicação de menu na fonte atual.
- **Landing:** `landing.js` renderiza benefícios e carrossel; `data.js` já centraliza benefícios padrão. Pilot benefit-strip tipado foi válido, porém custou infraestrutura relevante e não é arquitetura base obrigatória. Bugs `#224` e `#215` exigem correções focalizadas e gate sem introduzir abstração nova.
- **Tokens CSS:** folhas globais `public-theme.css`/`ui-theme.css` e locais de Landing/Viewer/Admin/Config têm valores e papéis repetidos sem confirmação de equivalência. A fundação semântica deve ser materializada após mapear cascata e homologações, não gerar reset global.
- **CI/compatibilidade:** já havia falhas nas suítes móveis, stone/summary/admin e public routing; distinguir regressões novas, fixtures antigas, ambiente e defeitos reais. Real iPad/Chrome/Safari teve relatos de falhas em botões, login e assets; WebKit automatizado não os substitui.
- **Configuração de móveis:** discovery `CP-POSTV5-01` demonstra que criar novo módulo físico só no Admin não é suportado completamente; schema de fluxo aceita IDs registrados, mas catálogo/cena/assets são outras autoridades. O piloto de nova cor/material confirma parte da extensibilidade, não uma família arbitrária. Não prometer `novo móvel = só máscaras` sem um contrato de asset/cena/catalogado e falsificação end-to-end.
- **Preço/segurança:** `viewerPricePublication` OFF na ausência da flag, publicação administrativa explícita, allowlist no DTO; falta homologação manual ON/OFF/HTTP anônimo e cache/revogação, sem ligar preços reais automaticamente.
- **Estados e acessibilidade:** EST-01…10 são direções, não todos os tokens/medidas/controles homologados; mapear disabled/read-only/selection/focus/loading/error/unknown/retry e recuperações antes de criar componente genérico.

## 6. Decisões pendentes e recomendação padrão

| Decisão | Padrão proposto / motivo |
|---|---|
| Fonte executável dos tokens entre os dois repositórios | DS como autoridade de aprovação e artefato de tokens versionado; produto consome exportação gerada/revisada com commit fixado, nunca busca remota em runtime; definir formato e CI ao chegar a V2 |
| Markup comum entre páginas estáticas | Preservar HTML disponível sem JS; usar partials gerados em build time por script Node puro **somente se** a duplicação comprovada justificar. Não incluir engine de template/framework |
| Definição de componente vanilla | CSS escopado por classe + HTML acessível + controlador/módulo JS. Usar `<template>`/Custom Elements apenas em casos com ganhos demonstráveis; não impor Shadow DOM |
| Tradução e conteúdo editorial administrável | Manter textos públicos versionados no código inicialmente; i18n e CMS/autoria de conteúdo são trilhas futuras, exigem justificativa de produto e contrato de publicação separado |
| Pipeline de assets para novos móveis | Primeiro escolher um caso concreto da mesma família e mapear contratos de asset, alfa/geometria, dependências, catálogo, preço e validações. Novo motor de cena só após um caso que o necessite |
| Ordem dos primeiros componentes | Primeiro estabilizar controles/bugs, depois tema/foco e shell/menu por variante; só depois componentes complexos de Config/Viewer. Não editar simultaneamente CSS, JS e V5 sem necessidade |
| Fonte canônica e revisão de roadmap | Este arquivo/index do DS para direção técnica; `decisions.json` continua para homologação estética e estados. PR #39 permanece como laboratório a reconciliar, não autoridade operativa vigente |

## 7. Critério de parada, custos e segurança

Uma extração é GO se elimina uma autoridade duplicada real, tem consumers identificados, mantém HTML/DOM/cascata/ARIA/keyboard/viewport equivalentes ou diferenças explicitamente homologadas, e tem rollback pequeno. É HOLD se depende de decisões visuais, DOM/estado não medido ou teste real indisponível. É NO-GO se depende de framework UI, engine universal sem consumidores, acopla domínio e apresentação, vaza dados, piora confiabilidade ou aumenta custo de manutenção sem ganho demonstrado.

**Retomada:** ler este arquivo, `decisions.json`, `docs/ROADMAP_AND_CURRENT_STAGE_2026-10-21.md`, PR #39 (somente como referência experimental), e consultar o head corrente do produto antes de qualquer implementação. Não supor que os SHAs de 21/10 continuem sendo HEAD em data posterior.
