# Mapa de aplicação das decisões

**Produto mapeado:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D) no commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`.  
**Deploy runtime verificado:** `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`, observado em 2026-10-18.  
**Fonte canônica das decisões:** [decisions.json](decisions.json).  
**Inventário estático:** [visual-inventory.json](visual-inventory.json).

## Como interpretar

Este mapa liga IDs de decisão às rotas, arquivos HTML e folhas CSS efetivamente carregadas no snapshot. A ligação não significa que a implementação já esteja conforme nem transforma valores atuais em tokens homologados. A inspeção do JavaScript e a atribuição de cada comportamento dinâmico a seus seletores/componentes continuam fora do escopo desta etapa.

As folhas foram lidas dos elementos `<link rel="stylesheet">` nas oito páginas do commit do produto acima. Para regras, propriedades e seletores por folha, consulte o inventário JSON. Seletores são indicados como alvo direto apenas quando aparecem na evidência específica de VIS-002; não inferimos os demais vínculos a partir de nomes parecidos.

## Rotas, fontes visuais e evidência

| URL | Superfície | HTML | CSS carregado | Decisões mapeadas | Evidência runtime |
|---|---|---|---|---|---|
| `/` | Landing / ambientes | `app/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002 | Observada; sem overflow em 390/768/1440 px |
| `/how-it-works/` | Como funciona | `app/how-it-works/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/how-it-works/how-it-works.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002, VIS-003 | Observada; sem overflow em 390/768/1440 px |
| `/about/` | Quem somos | `app/about/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/about/about.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002 | Observada; sem overflow em 390/768/1440 px |
| `/viewer/` | Viewer de ambiente | `app/viewer/index.html` | `app/public-theme.css`<br>`app/viewer/viewer.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002, EST-01, EST-02, EST-03 | Observada; sem overflow em 390/768/1440 px |
| `/config/` | Configurador | `app/config/index.html` | `app/styles.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, PRIVATE-HEADER-001, VIS-002, EST-01, EST-02, EST-03, EST-04, EST-05, EST-06, NAV-005 | Redireciona sem sessão para `/access/`; área protegida não verificada |
| `/admin.html` | Administração / login | `app/admin.html` | `app/admin/admin.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, EST-02, EST-04, EST-05, EST-06, EST-07, EST-08, EST-09, EST-10, NAV-005 | Login sem sessão; sem overflow em 390/768/1440 px |
| `/access/` | Login de acesso | `app/access/index.html` | `app/public-theme.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, NAV-005 | Página aberta; link não enviado/validado; sem overflow em 1440 px |
| `/access/manage.html` | Gerenciar acessos | `app/access/manage.html` | `app/public-theme.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, EST-02, EST-04, EST-05, EST-06, NAV-005 | Redireciona sem sessão para `/admin.html?returnTo=%2Faccess%2Fmanage.html`; área protegida não verificada |

O estado de `/config/` e `/access/manage.html` foi redirecionado sem sessão. Isso valida o comportamento de acesso observado, não o conteúdo protegido, seu cabeçalho autenticado ou seus dados.

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
| VIS-003 | `/how-it-works/` | Tratamento da legenda escolhido para `.study-art figcaption` no tema escuro; cores/opacidade finais e correção continuam pendentes |
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

**NAV-005:** o padrão largo público A aplica-se às rotas públicas; o padrão privado B aplica-se a `/config/`, `/admin.html`, `/access/` e `/access/manage.html`; o padrão contextual tipo viewer aplica-se a `/viewer/`. Para larguras compactas, a opção A está aprovada estruturalmente: linha única, marca e identificador/contexto à esquerda, tema antes do menu na extremidade direita; páginas públicas agrupam navegação e contato no menu. Os critérios exatos estão em `decisions.json`. Breakpoints, alturas, espaçamento, tipografia, cores, ícones/estilo dos controles e comportamento de rótulos longos permanecem abertos.

**VIS-002 — alvos de seletor com pares aprovados:** `.hero-description` em `/`, `.how-hero-note` em `/how-it-works/` e `.about-scale p:not(.eyebrow)` em `/about/` usam o par contextual claro aprovado `#675F55` sobre `#F0EDE8` (5,38:1). `.study-band .eyebrow` em `/how-it-works/` usa o par contextual aprovado `#70522F` sobre `#E8E3DC` (5,60:1). Os pares não são tokens globais e não aprovam variantes escuras.

**VIS-003 / FIND-004:** em `/how-it-works/`, `.study-art figcaption` no tema escuro deve permanecer integrada à ilustração sobre uma faixa escura na base (opção B escolhida). A aprovação cobre apenas a composição; valores finais de cor e opacidade/gradiente exigem medição. A prancha e a decisão não representam correção aplicada no produto.

## Capturas e limites

Capturas runtime persistidas nesta etapa: [landing claro](visualEvidence/public/landing/landing-light.jpg), [landing escuro](visualEvidence/public/landing/landing-dark.jpg), [viewer escuro](visualEvidence/public/viewer/viewer-dark.jpg), [login administrativo claro](visualEvidence/private/admin-login/admin-login-light.jpg), [login administrativo escuro](visualEvidence/private/admin-login/admin-login-dark.jpg) e [menu do login aberto](visualEvidence/private/admin-login/admin-login-menu-dark.jpg).

Não há captura atual de superfícies autenticadas. Estados de teclado completos, movimento reduzido, foco/hover/pressionado/seleção/carregamento, camadas transparentes e leitura de assets referenciados apenas por JavaScript ficam **não verificados**. O inventário futuro de JavaScript poderá completar a ligação de eventos e estados aos componentes depois da etapa visual.
