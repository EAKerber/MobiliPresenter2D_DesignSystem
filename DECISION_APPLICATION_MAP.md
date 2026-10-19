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
| `/how-it-works/` | Como funciona | `app/how-it-works/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/how-it-works/how-it-works.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002, VIS-003 | Reobservada ao vivo em 486 × 590 px, temas claro/escuro: menu abriu; WhatsApp ficou fora do menu; marca quase se confunde com a superfície no claro. Largura CSS e contraste DOM pendentes. |
| `/about/` | Quem somos | `app/about/index.html` | `app/public-theme.css`<br>`app/landing/landing.css`<br>`app/about/about.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002 | Observada; sem overflow em 390/768/1440 px |
| `/viewer/` | Viewer de ambiente | `app/viewer/index.html` | `app/public-theme.css`<br>`app/viewer/viewer.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, NAV-005, VIS-002, EST-01, EST-02, EST-03 | Observada; sem overflow em 390/768/1440 px |
| `/config/` | Configurador | `app/config/index.html` | `app/styles.css`<br>`app/ui-theme.css` | NAV-003, NAV-004, PRIVATE-HEADER-001, VIS-002, EST-01, EST-02, EST-03, EST-04, EST-05, EST-06, NAV-005 | Redireciona sem sessão para `/access/`; área protegida não verificada |
| `/admin.html` | Administração / login | `app/admin.html` | `app/admin/admin.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, EST-02, EST-04, EST-05, EST-06, EST-07, EST-08, EST-09, EST-10, NAV-005 | Login e sessão autenticada observados. Após login, menu ficou anônimo até recarga; depois exibiu páginas privadas e saída. Erro de carregamento administrativo não apareceu. Ver FIND-007 e `RUNTIME_AUDIT.md`. |
| `/access/` | Login de acesso | `app/access/index.html` | `app/public-theme.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, NAV-005 | Página aberta; link não enviado/validado; sem overflow em 1440 px |
| `/access/manage.html` | Gerenciar acessos | `app/access/manage.html` | `app/public-theme.css`<br>`app/ui-theme.css` | NAV-003, PRIVATE-HEADER-001, VIS-002, EST-02, EST-04, EST-05, EST-06, NAV-005 | Redirecionamento sem sessão já observado. Em `/access/manage`, sessão autenticada, conteúdo carregou e o menu mostrou páginas privadas/públicas e saída. Valores de convites não foram registrados. |

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
| VIS-003 | `/how-it-works/` | Composição e par contextual aprovados para `.study-art figcaption` no tema escuro (`#F0EDE8` sobre `#20211F`, 13,85:1); aplicação e validação no DOM pendentes |
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

**NAV-005:** o padrão largo público A aplica-se às rotas públicas; o padrão privado B aplica-se a `/config/`, `/admin.html`, `/access/` e `/access/manage.html`; o padrão contextual tipo viewer aplica-se a `/viewer/`. Para larguras compactas, a opção A está aprovada estruturalmente: linha única, marca e identificador/contexto à esquerda, tema antes do menu na extremidade direita; páginas públicas agrupam navegação e contato no menu. Em cabeçalhos privados estreitos, manter o rótulo do tema enquanto a logo reduz até 30%; se mais redução for necessária, usar tema apenas por ícone, preservando identificador e ordem dos controles. Os critérios exatos estão em `decisions.json`. Breakpoints, interpolação, dimensões, espaçamento, tipografia, cores e glifo do ícone permanecem abertos.

**VIS-002 — alvos auditados:** `.hero-description` em `/`, `.how-hero-note` em `/how-it-works/` e `.about-scale p:not(.eyebrow)` em `/about/` estavam em 4,47:1. O par antes escolhido `#675F55` sobre `#F0EDE8` (5,38:1) foi reaberto após feedback estético e não deve ser aplicado até nova escolha; `#705C4B` está em avaliação, sem homologação. `.study-band .eyebrow` continua com o par contextual aprovado `#70522F` sobre `#E8E3DC` (5,60:1). Nenhum deles é token global nem aprova variantes escuras.

**VIS-003 / FIND-004:** em `/how-it-works/`, `.study-art figcaption` no tema escuro permanece integrada à ilustração sobre uma faixa opaca `#20211F`, com texto `#F0EDE8` (13,85:1). O usuário selecionou A para este caso. É um par contextual, não token global. Aplicação e validação final no DOM do produto continuam pendentes; a prancha não representa uma correção aplicada.

## Capturas e limites

Capturas runtime versionadas de uma etapa anterior: [landing claro](visualEvidence/public/landing/landing-light.jpg), [landing escuro](visualEvidence/public/landing/landing-dark.jpg), [viewer escuro](visualEvidence/public/viewer/viewer-dark.jpg), [login administrativo claro](visualEvidence/private/admin-login/admin-login-light.jpg), [login administrativo escuro](visualEvidence/private/admin-login/admin-login-dark.jpg) e [menu do login aberto](visualEvidence/private/admin-login/admin-login-menu-dark.jpg). O usuário identificou as imagens antigas como anteriores à correção do cabeçalho; a recaptura atual apareceu no navegador, mas não foi persistida no Git neste checkpoint. Capturas autenticadas foram omitidas para não versionar dados de conta e acesso.

Não há captura atual de superfícies autenticadas. Estados de teclado completos, movimento reduzido, foco/hover/pressionado/seleção/carregamento, camadas transparentes e leitura de assets referenciados apenas por JavaScript ficam **não verificados**. O inventário futuro de JavaScript poderá completar a ligação de eventos e estados aos componentes depois da etapa visual.


**NAV-005 — evidência compacta:** a captura do DOM no login sem sessão indica uma linha a 350 px e duas linhas a 340 px (tema escuro; sem overflow nos estados testados). Isso descreve a implementação publicada; não estabelece breakpoint ou solução visual para caber na composição A. Ver [RUNTIME_AUDIT.md](RUNTIME_AUDIT.md).


**NAV-005 — encaixe estreito:** a regra aprovada limita a redução da logo a 30%, preserva o identificador e então troca o tema rotulado por ícone. A validação atual mediu o produto em 288–360 px: duas linhas até 340 px e uma linha em 350/360 px; alvos atuais de 40 px. A recomendação calculada foi corrigida: manter rótulo a partir de ~321 px, icon-only em 320 px ou menos e duas linhas abaixo de ~291 px, com alvos de 44×44 px. Ela ainda não está implementada no produto; requer revalidação posterior nos dois temas. Evidência: [NAV-005_RUNTIME_VALIDATION_2026-10-18.md](NAV-005_RUNTIME_VALIDATION_2026-10-18.md), `decisions.json` e [prancha NAV-005](visualEvidence/experiments/NAV-005-narrow-theme-control-options.svg).


## VIS-002 — paleta-base aprovada

A aprovação de valores e os limites de aplicação estão mapeados em [PALETTE_APPLICATION_MAP.md](PALETTE_APPLICATION_MAP.md). O mapa identifica duplicação entre folhas globais de tema, configurador e administração, distingue os papéis já homologados dos valores de uso atual e orienta a próxima etapa: atribuição por componente e validação runtime.