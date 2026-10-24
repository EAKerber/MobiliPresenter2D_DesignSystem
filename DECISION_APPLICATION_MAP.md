# Mapa de aplicação das decisões

**Produto mapeado:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D) no commit `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.  
**Atualização (2026-10-24):** o inventário estático foi regenerado a partir desse `main` e registra oito HTML e oito CSS. A comparação com o baseline anterior mostrou 47 commits de diferença; as rotas, regras, classes, cores e referências de assets do JSON agora refletem o snapshot atual. A cobertura de evidência por rota está em [matriz runtime](evidence/architecture/runtime-inventory-coverage-2026-10-24.md); a associação por folha e família CSS está no [mapa de famílias runtime](evidence/architecture/visual-rule-family-runtime-map-2026-10-24.md). Ambos classificam evidência e lacunas; não certificam conformidade global.  
**Deploy:** o handover verificou Production como READY em `main@5ccb2a8`; nenhum merge ou deploy foi feito por esta atualização.  
**Fonte canônica das decisões:** [decisions.json](decisions.json).  
**Inventário estático:** [visual-inventory.json](visual-inventory.json).

## Como interpretar

Este mapa liga IDs de decisão às rotas, arquivos HTML e folhas CSS carregados no snapshot. A ligação não significa que a implementação está conforme. As observações runtime têm escopo e limites explícitos na matriz de evidência; comportamento não exercitado permanece **não verificado**.

As folhas foram lidas dos elementos `<link rel="stylesheet">` nas oito páginas do commit de produto acima. Para regras, propriedades, seletores e classes, consulte o inventário JSON atualizado. Seletores só são tratados como alvo aprovado quando aparecem na evidência específica da decisão; nomes parecidos não bastam para inferir um vínculo.

## Informação de processo

VIS-002 aprova pares de texto contextuais, sem criar tokens globais. A aplicação medida anteriormente na Administração é `.message[aria-live="polite"][data-kind=""]` em `/admin.html`; demais superfícies, estados, fundos, bordas e ícones precisam de verificação própria.

A PR de produto [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241) continua em DRAFT e não está integrada ao `main`. A proposta v0.3 usa `#292723`, próximo do preto, para texto corrido longo nos sete contextos claros medidos; eyebrows e assinaturas ficam fora. O tema escuro não recebe essa regra e conserva a cor clara existente. A validação DOM/CSSOM em preview e os limites estão em [evidência da PR #241](evidence/runtime/pr241-vis002-measured-copy-contrast-preview-2026-10-24.md). A PR de produto #240 permanece HOLD: há cinco seletores compartilhados com cores divergentes que precisam de reconciliação antes de integrar qualquer uma das branches.

## Rotas, fontes visuais e evidência

| URL | Superfície | HTML | CSS carregado no produto main | Decisões mapeadas | Evidência runtime e limite |
|---|---|---|---|---|---|
| `/` | Landing / ambientes | `app/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002 | Menu foi operado por teclado e imagens/movimento foram amostrados. Corte em 290–310 px e issue #224 continuam abertos; correção de contraste v0.3 está apenas no preview #241. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |
| `/how-it-works/` | Como funciona | `app/how-it-works/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/how-it-works/how-it-works.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002, VIS-003 | Disclosures e amostra de imagens/movimento passaram; corte em 290 px permanece. Três grupos de texto claro abaixo de 4,5:1 foram medidos e corrigidos somente no preview #241. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |
| `/about/` | Quem somos | `app/about/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/about/about.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002 | A 290 px, título/menu são cortados. Production deixou foco em `body` após link de salto; #239 corrige em preview. Correção de contraste v0.3 também está apenas no preview #241. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |
| `/viewer/` | Viewer de ambiente | `app/viewer/index.html` | `app/public-theme.css`<br>`app/viewer/viewer.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002, EST-01, EST-02, EST-03 | Sete hotspots foram percorridos por Tab sem ativação; contraste de foco permanece parcial, e há corte de conteúdo em 290 px. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |
| `/config/` | Configurador | `app/config/index.html` | `app/styles.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, PRIVATE-HEADER-001, VIS-002, EST-01–EST-06, NAV-005 | CI autenticada #238 cobriu readiness, dois toggles e progressão parcial. Timeouts anteriores seguem sem causa; estados, larguras e contraste completos não verificados. [Gate parcial](evidence/runtime/ds05a-ci-stage-progression-2026-10-24.md) |
| `/admin.html` | Administração / login | `app/admin.html` | `app/admin/admin.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, EST-02, EST-04–EST-10, NAV-005 | Apenas login sem sessão foi observado; foco e contraste têm medições locais. Sessão autenticada e estados de envio/erro não foram exercitados. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |
| `/access/` | Login de acesso | `app/access/index.html` | `app/public-theme.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, NAV-005 | Só estado anônimo de link inválido foi observado; token válido, rede e sessão não foram exercitados. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |
| `/access/manage.html` | Gerenciar acessos | `app/access/manage.html` | `app/public-theme.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, EST-02, EST-04–EST-06, NAV-005 | Caminho sem sessão redireciona para login; sessão válida e operações de gestão estão **não verificadas** nesta matriz. [Matriz](evidence/architecture/runtime-inventory-coverage-2026-10-24.md) |

A tabela registra folhas vinculadas no HTML de `main`; os parâmetros de versão/cache foram omitidos. As rotas autenticadas não recebem status de validação por inferência a partir do redirecionamento anônimo.
## Decisões ligadas às rotas

| Decisão | Rotas ligadas pelo inventário | Situação da rastreabilidade |
|---|---|---|
| GOV-001 | — | Governança, origem não recuperável, componente sem especificação ou direção futura; sem tela concreta inferida |
| NAV-001 | — | Governança, origem não recuperável, componente sem especificação ou direção futura; sem tela concreta inferida |
| NAV-002 | — | Governança, origem não recuperável, componente sem especificação ou direção futura; sem tela concreta inferida |
| NAV-003 | `/`, `/how-it-works/`, `/about/`, `/viewer/`, `/config/`, `/admin.html`, `/access/`, `/access/manage.html` | 8 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| NAV-004 | `/`, `/how-it-works/`, `/about/`, `/viewer/`, `/config/` | 5 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| NAV-005 | `/`, `/how-it-works/`, `/about/`, `/viewer/`, `/config/`, `/admin.html`, `/access/`, `/access/manage.html` | 8 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| VIS-001 | — | Sem rota específica no mapa atual; revisar escopo quando a decisão avançar |
| VIS-002 | `/`, `/how-it-works/`, `/about/`, `/viewer/`, `/config/`, `/admin.html`, `/access/`, `/access/manage.html` | 8 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| VIS-003 | `/how-it-works/` | Composição e par contextual aprovados para `.study-art figcaption` no tema escuro (`#F0EDE8` sobre `#20211F`, 13,85:1); CSS publicado e par verificado no DOM do deploy atual |
| EST-01 | `/viewer/`, `/config/` | 2 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-02 | `/viewer/`, `/config/`, `/admin.html`, `/access/manage.html` | 4 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-03 | `/viewer/`, `/config/` | 2 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-04 | `/config/`, `/admin.html`, `/access/manage.html` | 3 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-05 | `/config/`, `/admin.html`, `/access/manage.html` | 3 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-06 | `/config/`, `/admin.html`, `/access/manage.html` | 3 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-07 | `/admin.html` | 1 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-08 | `/admin.html` | 1 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-09 | `/admin.html` | 1 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| EST-10 | `/admin.html` | 1 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| PRIVATE-HEADER-001 | `/config/`, `/admin.html`, `/access/`, `/access/manage.html` | 4 rota(s) no mapa estático; vínculo de tela não afirma conformidade da implementação |
| CMP-001 | — | Governança, origem não recuperável, componente sem especificação ou direção futura; sem tela concreta inferida |
| ENV-001 | — | Governança, origem não recuperável, componente sem especificação ou direção futura; sem tela concreta inferida |

**NAV-005:** os padrões são **diferenciados por profundidade**: primeiro nível público em `/`, `/about/`, `/how-it-works/`; privado B em `/config/`, `/admin.html`, `/access/`, `/access/manage.html`; contextual `secondaryNavigationPages` em `/viewer/`. **Correção explícita do usuário (21/10/2026, após revisar o preview #230): no Viewer a logo permanece na extremidade esquerda e o grupo da direita tem, nesta ordem, “← Ambientes”, seletor de tema e menu/hambúrguer.** A ordem vale nas disposições larga e compacta; o retorno não deve ficar junto da logo. Primeiro nível e privado conservam suas próprias composições NAV-005 (não generalizar esta correção). Em privados estreitos, preservar rótulo do tema enquanto a logo reduz até 30%; somente então usar tema por ícone. Os caminhos específicos estão em `decisions.json` e no [índice de profundidade](docs/NAVIGATION_DEPTH_AUTHORITY_GATE_2026-10-21.md). Breakpoints, tipografia e aspectos não homologados ainda dependem dos gates de layout.

**VIS-002 — rechecagem contextual:** após a homologação da paleta A, `.hero-description` em `/`, `.how-hero-note` em `/how-it-works/` e `.about-scale p:not(.eyebrow)` em `/about/` computam `#705C4B` sobre `#F0EDE8` (5,41:1) no tema claro. `.study-band .eyebrow` computa `#70522F` sobre `#E8E3DC` (5,60:1). Os quatro pares foram verificados no DOM publicado em 20/10, conforme [a evidência runtime](evidence/runtime/contrast-approved-pairs-2026-10-20.md). São contextos delimitados, não tokens globais; outros componentes, superfícies, temas e estados seguem pendentes.

**VIS-003 / FIND-004:** em `/how-it-works/`, `.study-art figcaption` no tema escuro está integrada à ilustração sobre faixa opaca `#20211F`, com texto `#F0EDE8` (13,85:1). O usuário selecionou A; o CSS está publicado e o par foi confirmado no DOM do deploy atual. É contextual, não token global. Uma nova captura contextual em 21/10, com viewport CSS 1280 × 720, está persistida em [visualEvidence](visualEvidence/public/how-it-works/vis003-caption-dark-2026-10-21.svg); tema claro, responsividade, dimensões, espaçamento e extensão a outros componentes permanecem sem verificação.

## Capturas e limites

Capturas runtime versionadas de uma etapa anterior: [landing claro](visualEvidence/public/landing/landing-light.jpg), [landing escuro](visualEvidence/public/landing/landing-dark.jpg), [viewer escuro](visualEvidence/public/viewer/viewer-dark.jpg), [login administrativo claro](visualEvidence/private/admin-login/admin-login-light.jpg), [login administrativo escuro](visualEvidence/private/admin-login/admin-login-dark.jpg) e [menu do login aberto](visualEvidence/private/admin-login/admin-login-menu-dark.jpg). O usuário identificou as imagens antigas como anteriores à correção do cabeçalho; a recaptura atual apareceu no navegador, mas não foi persistida no Git neste checkpoint. Capturas autenticadas foram omitidas para não versionar dados de conta e acesso.

Não há captura atual de superfícies autenticadas. Estados de teclado completos, movimento reduzido, foco/hover/pressionado/seleção/carregamento, camadas transparentes e leitura de assets referenciados apenas por JavaScript ficam **não verificados**. O inventário futuro de JavaScript poderá completar a ligação de eventos e estados aos componentes depois da etapa visual.


**NAV-005 — evidência compacta:** a captura do DOM no login sem sessão indica uma linha a 350 px e duas linhas a 340 px (tema escuro; sem overflow nos estados testados). Isso descreve a implementação publicada; não estabelece breakpoint ou solução visual para caber na composição A. Ver [RUNTIME_AUDIT.md](RUNTIME_AUDIT.md).


**NAV-005 — encaixe estreito:** a regra aprovada limita a redução da logo a 30%, preserva o identificador e então troca o tema rotulado por ícone. A validação atual mediu o produto em 288–360 px: duas linhas até 340 px e uma linha em 350/360 px; alvos atuais de 40 px. A recomendação calculada foi corrigida: manter rótulo a partir de ~321 px, icon-only em 320 px ou menos e duas linhas abaixo de ~291 px, com alvos de 44×44 px. Ela ainda não está implementada no produto; requer revalidação posterior nos dois temas. Evidência: [NAV-005_RUNTIME_VALIDATION_2026-10-18.md](NAV-005_RUNTIME_VALIDATION_2026-10-18.md), `decisions.json` e [prancha NAV-005](visualEvidence/experiments/NAV-005-narrow-theme-control-options.svg).


## VIS-002 — paleta-base aprovada

A aprovação de valores e os limites de aplicação estão mapeados em [PALETTE_APPLICATION_MAP.md](PALETTE_APPLICATION_MAP.md). O mapa identifica duplicação entre folhas globais de tema, configurador e administração, distingue os papéis já homologados dos valores de uso atual e orienta a próxima etapa: atribuição por componente e validação runtime.

## NAV-005 — verificação pública compacta em runtime (2026-10-19)

Na rota pública `/how-it-works/`, a 486 × 590 CSS px, o header manteve a marca em 160 px e exibiu o tema icon-only. O CSS oculta os rótulos do controle de tema até 1150 px. Com o menu aberto, havia os três links públicos, mas nenhum contato; o WhatsApp permanecia como CTA fora do menu. Isso diverge do padrão compacto aprovado. A marca estabilizada no tema claro veio de `logo-light-380.png`, sem filtro/opacidade, e permaneceu legível. Evidência e limites em [how-it-works-public-compact-header-2026-10-19.md](evidence/runtime/how-it-works-public-compact-header-2026-10-19.md); correção do produto em [issue #218](https://github.com/EAKerber/MobiliPresenter2D/issues/218).


### NAV-005 — validação estreita adicional (2026-10-19)

Em /how-it-works/, o tema permanece icon-only a partir de 360 px, inclusive em 321 px, enquanto a marca ainda está entre 120–129,6 px (redução máxima observada de 25%). Em 291/290 px, `html/body` impõem `min-width:320px`, `.how-page` recorta o excesso e o header não adota o fallback de duas linhas. A 290 px, o alvo do menu fica quase todo fora da área útil. Isso amplia FIND-012 e [issue #218](https://github.com/EAKerber/MobiliPresenter2D/issues/218). A medição completa consta em [evidência runtime](evidence/runtime/how-it-works-public-compact-header-2026-10-19.md).


## Configurador — resumo, contador e contraste (2026-10-19)

Em /config/, o selector .price-state__breakdown dt carregado em styles.css?v=runtime-v40 usa texto branco translúcido de 11 px nos dois temas. No resumo claro, a composição sobre #fff com overlay rgba(203,188,170,.13) resulta em 1,05:1; no escuro, 6,95:1. FIND-010 / DS04-07 e a correção visual estão no [issue #208](https://github.com/EAKerber/MobiliPresenter2D/issues/208). O mesmo acesso também reproduziu o contador 8/8 ao lado de um resumo sem módulos e R$ 0,00 após navegar ao Resumo, FIND-006 / [issue #209](https://github.com/EAKerber/MobiliPresenter2D/issues/209). A evidência completa está em [configurator-summary-label-counter-2026-10-19.md](evidence/runtime/configurator-summary-label-counter-2026-10-19.md).
