# V0-B — cobertura estática expandida, cascata CSS e primeiro patch de componentes

> **Atualização após este plano — P-COMP-01 IMPLEMENTADO EM BRANCH, TESTADO:** consultar [checkpoint posterior e evidência Actions](P_COMP_01_PUBLIC_MENU_IMPLEMENTATION_GATE_2026-10-21.md). Este documento descreve o estado anterior **ESPECIFICADO/NÃO EXECUTADO**. Na sequência, a branch `architecture/p-comp-01-public-menu-20261021@4ba9384` passou em 40 diferenciais, 16 testes funcionais e 20 NAV-005; ainda sem merge/deploy.


**Data:** 2026-10-21. **Status:** auditoria estática **PASS por fonte**; extração/tradução e promoção de componente **HOLD até gates executáveis/browser**. Não é homologação visual nem implementação. **Produto:** `EAKerber/MobiliPresenter2D@840a0cda361b3ce215fc934badc26df72dffc6e8`. **Design System:** `decisions.json` + [ARC-01..16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md).

**Antecedente:** [V0-A](V0A_POST230_OWNERSHIP_LOCALIZATION_AND_BUILD_AUDIT_2026-10-21.md), com 14 famílias de componentes e índices heurísticos de 826 ocorrências candidatas. Este checkpoint corrige os limites da varredura, mapeia novas fontes, triangula a cascata por rota e especifica o **primeiro patch restrito**. Não executamos o app em browser nem alteramos o produto.

## 1. Evidência reproduzível e escopo

| Evidência persistida | Conteúdo | Limitação vinculante |
|---|---|---|
| [Fontes runtime JS, cobertura e pontos cegos de localização](../evidence/architecture/v0b-source-coverage-and-missed-text-2026-10-21.json) | **54 fontes JavaScript** de runtime (exclui testes/ferramentas/bundles); 18 indexadas lexicalmente no V0-A, **34 adicionais lidas/analisadas estaticamente** no V0-B; dois grandes arquivos de dados de assets não lidos | Leitura orientada a usos visíveis e erros, **não** parser/AST completo, nem prova de alcançabilidade/visibilidade |
| [Mapa de classes CSS e co-carregamento por rota](../evidence/architecture/v0b-css-class-coload-and-ownership-2026-10-21.json) | 8 CSS/8 rotas, ordem observada nos links HTML, nomes de classe repetidos, folhas co-carregadas e 8 hipóteses de ownership | Contagem **lexical**; não calcula cascata real, CSSOM, var() resolvida, computed CSS, DOM ou screenshots |
| [Matriz V0-A das famílias](../evidence/architecture/v0-component-ownership-2026-10-21.json) | 14 famílias, origens, variantes, risco, consumidor, autoridade e gate | Não confundir candidato de extração com componente homologado |
| [Índice A — HTML/JS público](../evidence/architecture/v0-text-candidates-public-2026-10-21.json) + [Índice B — JS dinâmico](../evidence/architecture/v0-text-candidates-dynamic-2026-10-21.json) | **543 + 283 = 826 ocorrências lexicais candidatas** de 26 arquivos HTML/JS | Não inclui todas as strings dinâmicas e possui falsos positivos/repetições |

**Revisão de cobertura:** oito HTML mapeados; 54 arquivos JS de runtime de primeira parte contabilizados por caminho, sendo 52 inspecionados em leitura estática (com granularidade diferente) e **2 grandes dados estáticos não lidos**: `app/data/mask-data.js` (~310 kB na árvore Git) e `app/data/stone-data.js` (~1,30 MB na árvore Git). São dados de máscaras/pedra, **não classificados como catálogo i18n com base apenas no nome**; uso e eventual conteúdo textual exigem verificação separada se impactarem usuário. Funções Netlify/server não entram nessa contagem de `app/`; não confundir ausência de inclusão com evidência de que mensagens servidor nunca aparecem na UI.

**Fronteira ARC-13:** o resultado final de tradução continua sendo **extração abrangente** dos textos localizáveis, mas o índice do V0-A é somente ponto de partida. Não gera cobertura integral nem troca automática de textos.

## 2. Pontos cegos concretos da primeira varredura

| Origem / ponto | Achado | Encaminhamento |
|---|---|---|
| `app/core/ui-theme.js` | `FULL={auto:"Automático",light:"Claro",dark:"Escuro"}`, `SHORT={...}`, mensagens ARIA compostas por concatenação | Interface/localização, **ausentes ou subcapturados** na heurística anterior |
| `app/landing/landing.js` | Mini-benefícios `["Modular", "Inteligente", "Para a sua vida"]`, fora de atribuição literal de `label` | Conteúdo editorial localizável, salvo se autoria comercial decidir outra coisa |
| `app/how-it-works/how-it-works.js` | Mapa `explanations` com seis pares de título e explicação para painel dinâmico | Conteúdo editorial localizável; não traduzir IDs `escala/coletivas/...` |
| `app/core/technical-drawings.js` | `Vista lateral`, `Vista frontal`, `Projeção isométrica orientativa`, legendas construídas com medidas | Texto de vista técnica; separar rótulos de números/unidades/cálculo |
| `app/core/admin-bootstrap-retry.mjs` | Mensagens de sessão, carregamento, permissão e erro exibidas no Admin | Localizáveis se apresentadas ao usuário; códigos/status não |
| `app/core/pricing.js` | Fallback `Estimativa da composição` | Localizável apenas na apresentação; contrato comercial e números continuam no domínio |
| `app/data/catalog-data.js`, `hierarchy-defaults.js`, `scene-data.js`, `core/configuration.js` | Rótulos e descrições de entidades, materiais e fluxo existentes | Autoridade de catálogo/V5/cena, **não** migrar para UI translation bundle sem design de domínio explícito |
| `app/core/flow-layout.js`, `flow-model.js`, `administration-v5.js` | Strings de diagnóstico/invariantes do Core | Diagnóstico técnico; classificar se alguma atravessa UI, sem convertê-lo automaticamente em mensagem editorial |
| `app/core/legacy-stage-repair.js` | Mensagens v3 de recuperação, aparentemente legadas | Preservar; avaliar alcançabilidade e proprietário antes de extrair |

**Próxima exigência de completude:** scanner reproduzível no ambiente Node já existente, com tokenização/AST JS, elementos/atributos HTML, template literals, concatenações e literais em mapas/arrays; separar `UI-facing`, `editorial`, `accessibility`, `domain-owned`, `diagnostic`, `security-sensitive` e `unknown`. Medir cobertura de arquivos, expressões não resolvidas e strings residuais; não presumir que a ausência de candidato é ausência de texto.

## 3. CSS: duplicação lexical ≠ duplicação de autoridade

Sobre as **8 folhas CSS reais** do produto no SHA fixado, a indexação lexical encontrou **435 nomes de classe distintos**, **84 nomes presentes em mais de uma folha** e **69 nomes que aparecem em ao menos duas folhas carregadas simultaneamente por alguma rota**. Os valores não são comparáveis 1:1 às estatísticas antigas: a metodologia de contagem difere e não executou CSSOM. **NÃO alegar 69 conflitos CSS.**

| Família/regra | Evidência atual | Classificação e política de extração |
|---|---|---|
| **Menu público** `.site-header`, `.menu-open`, `.menu-toggle` | `landing.css` compõe header e menu; `ui-theme.css` modifica estados, tema, compactação; How acrescenta estilos contextuais | **Contrato partilhado confirmado**, CSS/layout não extrair até NAV-005 e regressões #215/#218 estarem mapeados; controlador JS é o primeiro recorte seguro |
| **Viewer** `.viewer-header`, `.ui-theme-toggle` | `viewer.css` e `ui-theme.css` co-carregados; NAV-005 exige logo esquerda, no grupo direito `← Ambientes → tema → menu` | **Variante de profundidade 2**, não clonar header Landing; comparar geometria por largura/tema |
| **Botões** `.button`, `.button--primary`, `.button--secondary` | Bases em `landing.css`, `styles.css`, `admin.css` têm dimensões e estados diferentes, com overrides de `ui-theme.css` | **Homônimos/variantes potenciais**; não fundir globalmente por nome |
| **Cards** `.module-card` | How tem card de exposição editorial; Config usa card de escolha/seleção; `ui-theme.css` contém seletor transversal | **Contratos distintos**; investigar alcance do seletor de tema em How/Config sem declarar regressão sem browser |
| **`.visually-hidden`** | Regra textual idêntica em `styles.css` (config) e `admin.css` (Admin); folhas não se co-carregam | **Candidato utilitário de baixo risco**, porém ganho limitado e mudança de import exigiria medição/rollback |
| **Hotspots de cena** `.scene-hotspot` | Viewer e Config possuem regras próprias, sem carregar as duas folhas na mesma rota | **Não extrair agora**: geometria, camada, seleção/foco e touch são contratos sensíveis |
| **`.eyebrow`** | Muitas fontes e superfícies; cores/tamanhos mudam por About/How/Viewer/Admin | **Variante contextual**; não promover a token visual universal a partir de uso |
| **Foco/tema** | `ui-theme.css` contém `--ui-theme-focus` light `#6e512e`, dark `#d8bc7c` e `.ui-theme-toggle:focus-visible` com **3px/offset2**, enquanto DS documenta foco homologado claro `#8B6A40`, escuro `#D8BC7C`, **4px/offset3** para o escopo aprovado | **Desvio de declaração candidato a correção separada**; confirmar alcance da homologação e regra vencedora em computed CSS antes de alterar. Não misturar correção visual com refatoração ARC-04 |

**Nota especial de causalidade:** `ui-theme.css` costuma ser carregado depois da folha específica em páginas públicas, enquanto `admin.css` e `styles.css` precedem `ui-theme.css` em páginas privadas. Migrar um seletor apenas por ser repetido altera ordem e especificidade; preservar a aparência requer provar computed style, inclusive hover/foco/disabled, overlays, media queries e preferências.

## 4. Primeiro patch de implementação recomendado: P-COMP-01 — controlador público

**Estado:** **ESPECIFICADO / NÃO EXECUTADO**. É o primeiro ganho de responsabilidade duplicada comprovável com risco de CSS próximo de zero. Sua implementação deve ser feita em **branch nova a partir da main corrente**, sem merge direto de experimento desatualizado e sem alterações de DOM/CSS/tema no mesmo patch.

**Objetivo:** um só controlador JS de menu público para quatro consumidores:
`/` (Landing), `/about/`, `/how-it-works/`, `/viewer/`.
O existente `app/landing/header-menu.js` já é utilizado por About/Viewer; a Landing mantém handlers próprios ao final de `landing.js`, e How mantém IIFE de menu no início de `how-it-works.js`. **Não** substituir `app/core/private-navigation.js`: contém autorização, sessão e logout.

**Fileset positivo (estimativa, validar antes de escrever):**
- `app/landing/header-menu.js`: manter como dono; aperfeiçoar ciclo idempotente quando necessário, NAV-004 (click, Enter, Escape, clique fora, `aria-expanded`, foco), sem transformar em schema de DOM.
- `app/index.html`: incluir o controlador em ordem segura antes de `landing.js`, com versionamento de cache.
- `app/landing/landing.js`: retirar **só** listeners/funcões de menu; preservar `stopHint`, ondas, paginador, seleção, assets e intervalos.
- `app/how-it-works/index.html`: incluir o controlador antes do JS local.
- `app/how-it-works/how-it-works.js`: retirar **só** IIFE inicial do menu; manter intacta a IIFE de explicações e a lógica de grid.
- `app/about/index.html`, `app/viewer/index.html`: atualizar versão do controlador **somente se necessário** para invalidar cache; preservar marcação e NAV-005.
- Testes: reutilizar a intenção, não o merge literal, de `tests/public-header-controller-gate.mjs` da branch experimental histórica e adicionar cobertura do **Viewer**.

**Gate de comportamento**: menu acessível por click, Enter, Escape e clique fora em mobile; link fecha menu; `aria-expanded` acompanha estado; abertura por teclado move foco à primeira opção quando necessário; Escape devolve ao toggle apenas quando apropriado; fechamento por ponteiro não rouba foco. Sem listener duplicado. `prefers-reduced-motion` respeitado. Alteração de funcionalidade na Landing para cumprir **NAV-004 já homologada**, registrada separadamente de equivalência visual.

**Gate de equivalência:** quatro consumidores × largura pública relevante (pelo menos 320, 390, 486, 768, 1366 conforme risco) × dois temas, estado aberto/fechado; Chromium/WebKit automatizados e inspeção visual/funcional adequada. Viewer mantém NAV-005 de profundidade 2, com `← Ambientes` no grupo da direita e texto/scene intactos. Conserva How painel econômico (seis explicações), carrossel da Landing (5 ambientes; onda/stopHint); bug #224 e possível clique interceptado #215 **não** serão marcados resolvidos sem reprodução/correção própria. Nenhuma mudança não autorizada em preços base, sessão, dados do comprador, V5, cena ou endpoints.

**Evidência preexistente, não transferível automaticamente:** branch do produto `experiment/shared-public-header-controller-20261020` (`fdeb931`) teve gate Actions [#39508130387](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39508130387) PASS; porém comparada à main atual está **10 commits à frente e 26 atrás**; cobre três rotas públicas, não o Viewer pós-#230. A PR #39 DS também permanece draft/divergente. **Não usar essas aprovações como CI PASS da candidata atual nem unir branches antigas.**

**Rollback**: revert dos arquivos JS/HTML acima, sem mover CSS ou DOM; restaurar ordem e URL dos scripts; confirmar ações do menu e integridade Landing/How/Viewer. Não abrir Deploy Preview só para testar sintaxe; CI/servidor local primeiro; preview único deliberado somente após gate de integração quando indispensável.

## 5. Patch seguinte, separado: P-TOKEN-01

**Estado:** candidato preparatório, não implementar junto de P-COMP-01. Entradas: `decisions.json` aprovado/escopo, artefato estruturado com tokens homologados e gerador Node determinístico versionado; saída CSS no **produto**, via PR explícita, commit/manifesto do DS pinado. A primeira família só será escolhida após inventário de token-role, verificação de propriedades computadas e diferenciação entre **correção homologada** e **extração sem alteração visual**.

O CSS atual de foco do tema demonstra por que não podemos deduzir valor canônico a partir do uso observado. Primeiro classificar VIS-002/EST-02 por componente/tema/estado; separar eventual correção do outline do trabalho de arquitetura para preservar ARC-04.

**ARC-03 — HTML fragment build:** terceiro patch, **não** no primeiro controlador. O Netlify `netlify.toml` publica `app` com `npm run build` da raiz (bundles Admin, Access/Manage, private-navigation); `app/scripts/build-static.sh` gera saída histórica `app/dist`, que não é o `publish` efetivo. Especificar separação de fonte HTML e saída gerada antes de editar páginas, prevenir overwrite do HTML de autoria e auditar diff renderizado.

## 6. Critérios ARC-16 e estado do gate

| Check | Status | Próximo passo |
|---|---|---|
| Todas as 8 rotas do produto inventariadas por fontes CSS/HTML | **PASS estático** | Repetir em runtime com JS e estados |
| 54 arquivos JS da pasta `app` contabilizados; 52 lidos | **PASS inventário de fontes** | 2 data-heavy explicitamente ainda não inspecionados |
| Localization tokens/textos já totalmente extraídos | **HOLD** | Scanner robusto/AST + UI-vs-domain + texto DOM, parâmetros/plurais e revisão |
| Ownership CSS e classes co-carregadas mapeados | **PASS lexical** | CSSOM/DOM/cascade/contraste em estados reais antes da extração |
| Reuso de menu público identificado e patch definido | **PASS de especificação** | Branch isolada main atual + testes das 4 rotas |
| Artefatos DS atualizados e sem novo token visual aprovado implicitamente | **PASS documental** | `decisions.json` continua único para estética |
| Implementação/capturas/funcional/browser/integration | **NOT RUN** | Não tratar auditoria estática como verificação real |

**Decisão:** V0-B documental foi concluído e torna o primeiro patch **planejável**. **Promoção para implementação/merge e conclusão de conformidade runtime permanecem HOLD** até verificação contextual. Nenhum requisito de iPad legado como gate global; #212/#213 de auth permanecem separados, e não há piloto com móveis fictícios.

**Próxima execução prática, sem precisar de nova decisão de produto:** (a) revisar o spec do controlador contra o produto main atual; (b) preparar branch isolada e testes de 4 rotas com rollback claro; (c) em paralelo, preparar scanner de localização robusto no build Node existente; (d) só depois considerar token export e fragmentos HTML, em patches independentes. Não iniciar simultaneamente alterações de JS/CSS/V5 por comodidade.
