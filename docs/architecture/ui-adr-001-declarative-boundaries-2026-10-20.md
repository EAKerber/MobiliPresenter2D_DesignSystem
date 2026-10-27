# UI-ADR-001 — Fronteiras da UI declarativa e contratos de componentes

- **Data:** 2026-10-20
- **Status:** DIREÇÃO TÉCNICA ADOTADA PARA P0/P1 EXPERIMENTAL; **não é homologação de produto**, visual ou autorização de migração da aplicação.
- **Escopo de escrita:** repositório `EAKerber/MobiliPresenter2D_DesignSystem`, branch `architecture/dom-css-consolidation-20261020`; produto `EAKerber/MobiliPresenter2D` somente leitura.
- **Revisão consultada do produto:** [`1878ae1057ce7c6190e0c8cb08a1f3baadd49463`](https://github.com/EAKerber/MobiliPresenter2D/tree/1878ae1057ce7c6190e0c8cb08a1f3baadd49463).
- **Relacionados:** [crosswalk estático](dom-css-static-crosswalk-2026-10-20.json), [auditoria de ownership](dom-js-component-ownership-2026-10-20.md), [plano incremental](declarative-ui-increment-plan-2026-10-20.md), [direção CSS](css-component-architecture-proposal-2026-10-20.md).

## Problema

Há renderização declarativa em diferentes pontos, mas seus contratos não são iguais. O Configurador valida componentes semânticos associados a seções de produto; o Viewer projeta conteúdo público seguro e organiza blocos e desenhos por JS; a Landing gera ambientes/benefícios a partir de dados locais; o Admin materializa formulários de autoria. Generalizar o **schema de produto** a todas essas funções criaria dependência artificial de publicação, permissão e versionamento. Repetir apenas `document.createElement` não justifica abstração.

## Decisões técnicas tomadas nesta frente

### UI-ADR-001.A — Generalizar pipeline, não documento administrativo

- **Adotado como limite:** reutilizar validação → view model / projeção → registro explícito de componentes → DOM/estilos/ações.
- Preservar `ConfiguratorAdministration2D 5.0`, `Scene2D`, catálogo, precificação e os DTOs públicos atuais como fontes específicas e com suas autoridades próprias.
- Não criar schema universal de site nem migrar contratos de domínio durante o piloto.
- Projeções públicas permanecem allowlist no backend e devem expor apenas os campos autorizados. Esconder componentes no DOM **não é autorização**.

**Evidência:** [schema v5](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/administration-v5.js), [projeção pública](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/public-module-projection.js), [projeção buyer](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/core/published-buyer-projection.js).

### UI-ADR-001.B — Componentes com IDs explícitos, escopo e contrato

- Criar registro **em código**, não configurável por usuários: `type -> accepted variants -> validate(data) -> renderer`.
- Identidade de componente com namespace/versão apenas para o novo contrato experimental, ex.: `landing/benefit-strip@1`; não renomear os tipos existentes do Configurador sem migração contratada.
- Cada componente possui: estrutura semântica e acessibilidade, entrada validada, CSS pertencente ao componente, variantes permitidas, estados/eventos quando houver e testes.
- Uma classe repetida (`.module-card`) não caracteriza um componente compartilhável; igualdade de DOM/CSS também não prova igualdade de **contrato**.
- Rejeitar tipo desconhecido, variante desconhecida, IDs duplicados e referências ausentes **antes de montar** a composição. Nenhum renderer implícito de fallback ou HTML/CSS arbitrário.
- Elementos operacionais como formulários de acesso, pricing e cena têm controladores especializados; o registro não passa a executar funções arbitrárias vindas dos dados.

### UI-ADR-001.C — Contratos separados conforme autoridade

| Contrato ou camada | Autoridade | Forma inicial | Consequência |
|---|---|---|---|
| Schema administrativo V5 / domínio | dados comerciais/fluxo sob Admin | **existente, inalterado** | sem `schemaVersion` novo nesta frente |
| `PageComposition` | estrutura aprovada da página | **manifesto em código**, experimental e restrito | sem editor visual, banco ou publicação dinâmica |
| `EditorialContent` | texto/imagens que eventualmente forem administráveis | **não criar ainda** | decisão de autoria separada, com draft/revisão/publicação se houver uso real |
| `ComponentContract` | componentes e validação | código versionado e lista fechada | tipos/variantes não são fornecidos como código no JSON |
| Theme / tokens | Design System homologado | CSS e atribuições por componente | nunca aceitar `style` arbitrário em `PageComposition` |
| Estado/transições | controlador de feature/componente | runtime (e estado de produto pré-existente) | não persistir hover, modal ou loading como campos de produto |

Não exigir JSON Schema, Zod, React, web components ou CSS Modules neste checkpoint. Validadores JS puros podem estabelecer o formato; considerar serialização/schema formal quando houver intercâmbio externo e múltiplos consumidores independentes. A decisão é **separar autoridade**, não multiplicar arquivos por regra.

### UI-ADR-001.D — CSS e composição não são a mesma autoridade

- O manifesto declara `component`, `variant`, `dataRef` e ordem; não declara seletor, CSS, HTML ou propriedades arbitrárias.
- Estilos globais mínimos + CSS de componentes + CSS de composição da página. `public-theme.css`/`ui-theme.css` não serão reagrupados indiscriminadamente.
- Preservar precedência/cascata e variantes claro/escuro. Tokens e pares cromáticos locais requerem decisão visual homologada; extrair CSS não reabre automaticamente VIS-002/VIS-003.
- No experimento não usar `@layer`, bundler novo ou framework novo como pré-requisito.

### UI-ADR-001.E — Migração por adaptação e prova, não reescrita

- P0: identificar para cada bloco **origem dos dados, owner, renderer, DOM estático/dinâmico, CSS, ações, tema, risco e teste**.
- P1: definir protótipo isolado do contrato, validar entradas e ordem. Nada no produto é alterado.
- P2: piloto não crítico em componente já gerado por JS, preferencialmente `Landing/benefit-strip` a partir de `CASA_PUBLIC_LANDING.benefits`; não migrar header, Admin, preço ou cena.
- P3: provar um segundo consumidor genuinamente equivalente **antes** de promover para componente compartilhado; caso contrário, manter componente local e encerrar tentativa de abstração.
- P4+: migrar proprietários gradualmente com PRs pequenas, equivalência estrutural/visual/funcional e rollback local.

**Motivo do piloto:** `renderBenefits()` monta `.benefit-item` desde `data.benefits` [landing.js](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/landing/landing.js); caminho sem auth, preços, geometria ou schema comercial. O trio `.mini-benefit` é hardcoded no mesmo `renderBenefits()`; deve ser tratado como **outra fonte e outro contrato**, sem agregação implícita.

### UI-ADR-001.F — Dados ausentes, fallback e riscos de segurança

- Ausência intencional de seção = ausência de UI; dado necessário ausente/contrato inválido = erro determinístico antes da renderização.
- Uma falha de API pública não deve recuperar automaticamente documento administrativo, catálogo completo ou defaults locais para aparentar sucesso. Essa proteção já existe em [viewer/public-data.js](https://github.com/EAKerber/MobiliPresenter2D/blob/1878ae1057ce7c6190e0c8cb08a1f3baadd49463/app/viewer/public-data.js).
- Não aceitar `innerHTML`, `style`, código executável, URLs arbitrárias de ação ou eventos como dados de composição; texto por `textContent`/DOM controlado pelo renderer.
- Props com URLs/arquivos de imagem exigirão política de origens/paths em contrato específico antes de publicação; não inferir que qualquer string seja segura.
- Interface administrativa e autorização no servidor são fronteiras distintas. Nenhum manifesto pode conceder role.

### UI-ADR-001.G — Navegação, tema e progressive enhancement ficam fora do primeiro piloto

- `ui-theme.js` injeta controle de tema por busca de slots/DOM; `private-navigation.js` depende da sessão e de papéis. Ambos precisam de contrato de host/slots explícito antes de serem migrados.
- Header público/privado mantém decisões NAV-005 e PRIVATE-HEADER-001; não usar unificação arquitetural para ignorar diferenças de sessão ou compatibilidade compacta.
- Páginas editoriais estáticas, particularmente `/about/` e `/how-it-works/`, não serão integralmente transformadas em JS no piloto: preservar HTML semântico inicial, acesso sem JS e SEO. Fazer prova isolada ou progressive enhancement só com gate próprio.

## Limites de autoridade deste ADR

**Não** homologa nova identidade visual, nomes finais de CSS, ergonomia do Admin, schema persistente de composição, ferramenta de edição ou direito de escrever `main` do produto. **Não** declara que HTML estático já esteja integralmente coberto pelo CSS nem que DOM real/estados autenticados tenham sido testados. O usuário autorizou prosseguir e registrar decisões arquiteturais no Design System; estas decisões são direção operacional experimental, sujeita a gates, sem alterar decisões previamente homologadas.

## Critérios para promoção da arquitetura

1. Contratos/documentos têm uma única fonte de autoridade e versão.
2. Validadores rejeitam tipos, props/variantes e referências inválidas sem renderização parcial.
3. DOM/atributos de acessibilidade, CSS computado, responsive/tema e interações permanecem equivalentes ao baseline relevante.
4. Segurança: nenhuma superfície pública recebe campos administrativos além de projeções permitidas.
5. Medir economia real de complexidade: tipos novos não devem exigir dois arquivos de regras especiais para cada caso; se abstração não for reutilizável, manter especialização.
6. Gate automatizado, inspeção visual e teste funcional real são evidências **independentes**, não intercambiáveis.
