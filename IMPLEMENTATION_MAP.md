# Mapa de impacto: sistema visual e decisões homologadas

**Snapshot:** 2026-10-18  
**Repositório de produto observado:** `EAKerber/MobiliPresenter2D`, `main` no commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`.  
**Registro de decisões observado:** `EAKerber/MobiliPresenter2D_DesignSystem`, `main` no commit `712d0e4291bc9569e6aaab3869c1604de23a921a`.

Este documento mapeia o que uma padronização visual poderá atingir, separa direções aprovadas de valores ainda abertos e registra os bloqueios encontrados. É um inventário de fontes; não declara cores existentes como tokens oficiais nem mede novamente o contraste do produto.

## 1. Estado dos repositórios

O repositório DesignSystem contém três arquivos na raiz:

- `decisions.json` — registro estruturado, aproximadamente 18 KB.
- `index.html` — documento independente, aproximadamente 29 KB, com cerca de 8,3 KB de CSS e um script inline.
- `README.md` — descreve proveniência, limites e a diferença entre direção conceitual e token aprovado.

O conteúdo visual do `index.html` repete manualmente decisões que também estão em `decisions.json`. Isso pode divergir com o tempo. Na próxima etapa de organização, a opção preferida é manter o JSON como fonte canônica do estado das decisões e fazer a página consumir esse registro, em vez de manter duas cópias editoriais.

O produto é uma aplicação estática com múltiplas páginas HTML e folhas CSS por área. Há um arquivo compartilhado de tema, mas componentes de cabeçalho ainda têm marcação em cada página. O controle de tema é criado pelo runtime `app/core/ui-theme.js`; a navegação privada é montada por `app/core/private-navigation.js`. A existência de regras compartilhadas não significa que toda a marcação já seja um componente reutilizável.

## 2. O que pode avançar agora

1. Manter e melhorar o mapa entre IDs de decisão, páginas, componentes, classes e arquivos.
2. Inventariar variáveis e cores já presentes no produto com o rótulo **uso atual / não homologado**. O inventário ajuda a medir e comparar; não cria tokens oficiais.
3. Agrupar classes existentes por família e contexto para encontrar duplicações e colisões antes de propor uma arquitetura CSS.
4. Documentar os contratos funcionais já aprovados de navegação, cabeçalhos privados e estados, incluindo o que já está implementado no produto.
5. Preparar um relatório de cobertura por rota e estado, marcando evidência real, candidato, exceção e não testado.
6. Organizar o laboratório como espaço de comparação controlada, mantendo alternativas visuais identificadas como experimentais até haver homologação explícita.

## 3. Decisões aplicáveis e limites

| Decisão | Estado no registro | Pode orientar o mapeamento | Limite para implementação visual |
|---|---|---|---|
| NAV-003 | Direção acordada | Conferir uso do favicon de “Como funciona” em todas as páginas | Confirmar cobertura e exceções antes de alterar páginas |
| NAV-004 | Contrato funcional aprovado | Verificar abrir/fechar, Escape, clique fora, teclado, foco, `aria-expanded` e movimento reduzido | Não determina a estética do cabeçalho |
| NAV-005 | Direção organizacional aprovada | Mapear header público, destinos, contexto do viewer e indicação de página ativa | Altura, tipografia, cores, logo, apresentação e estética do menu público continuam em aberto |
| VIS-002 | Direção conceitual aprovada | Definir papéis semânticos e contextuais para informação, erro, sucesso, aviso, foco, seleção, hover, pressionado e desabilitado | Não fixa hexadecimais, pares de contraste, variantes, medidas, aparência ou tema por rota |
| EST-01 | Direção acordada | Localizar controles de seleção no configurador e verificar indicador explícito mais destaque moderado | Forma, cores, espessura e contraste ainda não definidos |
| EST-02 | Direção acordada | Mapear foco de teclado separado da seleção | Cor, espessura, afastamento, clipping e contraste em cada superfície ainda não definidos |
| EST-03 | Direção acordada | Separar hover, pressionado, seleção e conclusão; mapear movimento por família | Duração, easing, escala, deslocamento, cores e sombras ainda não definidos |
| EST-04 | Direção acordada | Catalogar desabilitado, somente leitura, publicação, disponibilidade, permissão e seleção como dimensões distintas | Regras e apresentações por tela ainda precisam de especificação |
| EST-05 / EST-06 | Direção acordada | Mapear carregamento, edição local, salvamento, confirmação, falha, estado desconhecido e publicação | Retry, recuperação, concorrência, hierarquia de feedback e publicação parcial exigem decisão de produto/arquitetura |
| EST-07 / EST-08 / EST-09 / EST-10 | Direções acordadas | Preservação de rascunho, conflitos, retry seguro e histórico entram no mapa do admin | Mecanismo, retenção, política de recuperação e sincronização não estão definidos como solução técnica |
| PRIVATE-HEADER-001 | Direção registrada a partir do pedido atual | Conferir posição da marca, identificador, tema, reiniciar e menu; documentar páginas privadas | Estética global, medidas e extração do HTML duplicado precisam de decisão de arquitetura visual |
| VIS-001 | Pendente | Manter no backlog | Não inferir direção |
| GOV-001, NAV-001, NAV-002 | Definidos/acordados sem texto de origem no registro | Preservar os IDs e localizar a fonte | Conteúdo não pode ser inferido |
| CMP-001 | Em andamento / revisar, sem nota | Registrar a lacuna | Não inferir governança de componentes |
| ENV-001 | Futuro | Preservar como futuro | Não antecipar generalização multiambiente |

O pedido atual autoriza avançar a padronização das decisões homologadas. Para os itens marcados como direção conceitual, a implementação pode seguir apenas até onde a direção é determinada; valores estéticos e comportamentos ainda em aberto não devem ser tratados como homologados.

## 4. Superfícies e código afetados no produto

| Área | Fontes CSS/HTML/runtime | Famílias e classes relevantes | Relação com decisões |
|---|---|---|---|
| Tokens públicos | `app/public-theme.css`, adaptações em `app/ui-theme.css` | `--public-bg`, `--public-surface`, `--public-text`, `--public-muted`, `--public-line`, `--public-accent*` | VIS-002, NAV-005; paleta atual é referência de uso, não especificação homologada |
| Landing e navegação pública | `app/index.html`, `app/landing/landing.css`, `app/landing/header-menu.js` | `.site-header`, `.header-actions`, `.header-cta`, `.menu-toggle`, `.menu-open`, `.hero`, `.environment*`, `.site-footer` | NAV-003, NAV-004, NAV-005, VIS-002 |
| Quem somos | `app/about/index.html`, `app/about/about.css` | `.about-hero`, `.about-chapter`, `.about-scale`, `.about-closing`, `.about-text-link` | Tipografia, editorial e cor pertencem à aplicação contextual de VIS-002; o conteúdo e layout foram incorporados na PR #210 |
| Como funciona | `app/how-it-works/index.html`, `app/how-it-works/how-it-works.css` | `.how-hero`, `.comparison-card`, `.module-card`, `.process-flow`, `.integration-callout`, `.closing-copy` | NAV-003 e VIS-002; preservar ilustrações e fotografia ao mapear superfícies |
| Viewer | `app/viewer/index.html`, `app/viewer/viewer.css`, trechos de `app/styles.css` | `.viewer-header`, `.viewer-brand`, `.scene-hotspot`, `.selection-frame`, `.view-counter`, `.detail-panel`, `.dimension-pill`, `.module-detail__price` | EST-01/02/03, VIS-002, NAV-005; destaque de seleção discreto e cena protagonista |
| Configurador | `app/config/index.html`, `app/styles.css`, adaptações em `app/ui-theme.css` | HTML nomeia `.topbar`, `.topbar__inner`, `.topbar__actions`, `.flow-nav`, `.flow-actions`, `.flow-group-grid`, `.module-stage-panes`, `.module-list`, `.module-detail`, `.global-options`, `.handle-options`, `.finish-controls`, `.services-checklist`, `.summary-panel`, `.viewer-pip-controls`, `.scene-hotspots`, `.selection-frame`; estado também usa classes geradas como `.is-selected`, `.is-active`, `.is-blocked` | EST-01/02/03/04/05/06, VIS-002, PRIVATE-HEADER-001; CSS principal é `app/styles.css` (853 linhas), mais regras da camada de tema |
| Administração | `app/admin.html`, `app/admin/admin.css`, `app/ui-theme.css` | `.admin-topbar`, `.admin-topbar__actions`, `.auth-card`, `.admin-form`, `.button--primary/secondary`, `.stage-card`, `.stage-items`, `.hierarchy-group/section/item`, `.hierarchy-choice-options`, `.item-option`, `.material-availability-*`, `.editor-card`, `.admin-tabs`, `.editor-actions`, `.message[data-kind]` | VIS-002, EST-02/04/05/06/07/08/09/10, PRIVATE-HEADER-001; folha base contém 211 linhas e declara tokens locais dark/light |
| Gerenciar acessos | `app/access/manage.html`, `app/access/manage.js`, `app/ui-theme.css` | Página tem `<style>` inline (~2,2 KB): `.access-page`, `.access-private-header`, `.toolbar`, `.panel`, `.grant`, `.eyebrow`, `.intro`, `.secondary`; a marcação também usa `.private-header__*` e `.private-menu__*` | VIS-002, EST-02/04/05/06, PRIVATE-HEADER-001; primeira candidata para retirar CSS inline depois de inventariar dependências |

| Controle de tema | `app/core/ui-theme.js`, `app/ui-theme.css` | `.ui-theme-toggle`, `.ui-theme-toggle__glyph`, `.ui-theme-context-row`, `.ui-theme-utility` | VIS-002; preferências light/dark/auto e posicionamento são runtime e CSS, não apenas tokens |
| Navegação privada | `app/core/private-navigation.js`, marcação em `admin.html`, `config/index.html`, `access/manage.html` | `.private-header`, `.private-header__brand`, `.private-header__page-name`, `.private-header__actions`, `.private-menu-toggle`, `.private-menu__*` | PRIVATE-HEADER-001 e NAV-004. Menu/estilos são compartilhados, mas parte da marcação do header é repetida entre páginas |

### Classes transversais para inventário

- Ações: `.button`, `.button--primary`, `.button--secondary`, `.button-copper`, `.button-dark`.
- Identidade: `.brand`, `.brand__logo`, `.eyebrow`, `.site-footer`.
- Estado: `.is-active`, `.is-selected`, `.is-blocked`, `.is-hidden`, `.is-current`.
- Informação e feedback: `.message`, `.admin-note`, `.intro`, `.private-menu__note`, `.private-menu__email`.
- Controles densos: `.global-option`, `.handle-option`, `.item-option`, `.hierarchy-choice-option`, `.material-availability-option`.
- Foco e cena: `:focus-visible`, `.scene-hotspot`, `.selection-frame`, `.viewer-pip-control`.

Essas classes têm escopos diferentes. Nomes repetidos como `.button`, `.brand`, `.eyebrow` e `.is-selected` não garantem aparência uniforme; regras locais e o contexto visual continuam aplicando estilos distintos.

## 5. Cores e variáveis observadas

### Canais semânticos existentes

- Público: `--public-bg`, `--public-surface`, `--public-surface-soft`, `--public-text`, `--public-muted`, `--public-line`, `--public-accent`, `--public-accent-dark`, `--public-accent-highlight`.
- Configurador: `--background`, `--surface`, `--surface-raised`, `--text`, `--muted`, `--border`, `--accent`, `--accent-strong`.
- Administração: `--bg`, `--surface`, `--raised`, `--text`, `--muted`, `--border`, `--accent`, `--label`, `--control-text`, `--control-bg`, `--inset-bg`, `--subtle-bg`, `--primary-bg`, `--primary-text`, `--success`, `--error`, `--info`, `--warning`.
- Controle de tema: `--ui-theme-focus`, `--ui-theme-control-bg`, `--ui-theme-control-border`.

### Leitura do estado atual

Há vocabulários distintos e variáveis com o mesmo nome em áreas diferentes. `app/styles.css` ainda contém cores literais de interface; `app/admin/admin.css` define uma paleta própria e valores de estados; `app/ui-theme.css` adiciona substituições light/dark por rota e componente. A unificação exige primeiro decidir o mapa semântico e medir combinações em superfícies reais. Renomear variáveis ou substituir hexadecimais em lote pode mudar contrastes e significado.

### Cores explicitamente não homologadas

- `#A64D13`: base aprovada da cor terciária promocional de produto/campanhas (2026-10-18). Variações e pares por tema/superfície ainda requerem contraste em contexto real.
- Amostras da imagem “Exemplos de estados”: erro, sucesso, aviso e informação identificados como candidatos, não aprovados. Os ratios ilustrados não homologam seus hexadecimais.
- Informação de processo usa o azul homologado. A administração atualmente mapeia `--info` para `#245d87` no tema claro e `#a7d1f0` no escuro; a auditoria visual/runtime confirmará a aplicação em telas reais. Outros hexadecimais no produto seguem como uso atual, sem aprovação automática.

## 6. Organização recomendada para a próxima etapa

1. **Fonte decisória:** preservar `decisions.json` para status, notas, evidências, limites e rastreabilidade.
2. **Mapa de aplicação:** manter este inventário separado das decisões canônicas. Cada linha deverá indicar ID, rota, seletor/classe, arquivo, comportamento atual, evidência e pendência.
3. **Vocabulário de tokens:** propor nomes sem atribuir valores. Separar papéis semânticos de valores por tema e de adaptações por contexto.
4. **Especificação visual homologável:** apresentar componente, light/dark quando aplicável, foco/seleção/hover/pressionado/desabilitado, contraste calculado e evidência em DOM real.
5. **CSS do produto:** após homologação dos valores relevantes, reduzir duplicação por uma folha de tokens compartilhados e regras de componente escopadas; migrar por família, sem substituição global automática.
6. **Exemplos visuais:** laboratório separado de produção, com candidatos rotulados e vínculo ao ID de decisão. Não misturar experiências experimentais com o catálogo de tokens homologados.
7. **Consolidação do registro:** depois da migração, fazer o `index.html` refletir o JSON canônico para evitar divergência.

Possível organização futura do repositório DesignSystem, sujeita a revisão:

```text
decisions.json                 # status e texto decisório canônico
README.md                      # regras de leitura e proveniência
IMPLEMENTATION_MAP.md          # mapa entre decisões e produto
index.html                     # visão navegável derivada do registro
docs/                          # governança, auditoria e orientações
tokens/                        # apenas tokens homologados, após decisão
laboratory/                    # comparações experimentais, isoladas
```

Não criar uma pasta de tokens preenchida com valores de referência ou candidatos. A estrutura só deve ganhar arquivos quando houver conteúdo suficiente e uma fonte de verdade clara.

## 7. Bloqueios e próximos dados necessários

- GOV-001, NAV-001 e NAV-002: origem marcada como não recuperável nesta consolidação; IDs/estados preservados sem inferir texto decisório.
- Resolver VIS-001 antes de assumir que todas as questões de identidade visual estão fechadas.
- Recuperar a definição de CMP-001 antes de fixar uma governança de componentes.
- Deixar ENV-001 no futuro, sem assumir seleção multiambiente.
- Homologar valores de cor, pares de contraste, foco, seleção, estados e variantes por superfície/tema; os exemplos existentes são apenas referências.
- Importar ou localizar os fontes originais v0.2/v0.3 citados no registro se o inventário completo de 43 famílias, os exemplos e o laboratório forem necessários como base canônica.
- Executar a revisão de contraste no DOM real e em estados dinâmicos. O registro DS-04 v2 declara cobertura incompleta; DS-05A/B/C aparece como plano, sem resultado de execução registrado.
- Mapear o CSS inline de `app/access/manage.html` e os seletores de `app/config/index.html` na próxima revisão de código para completar a lista de classes com seus valores e estados.
- Decidir se cabeçalhos públicos devem compartilhar uma composição visual. NAV-005 aprova a organização e navegação, mas deixa estética e medidas abertas.
- Decidir se a marcação de cabeçalhos privados será transformada em componente/template comum. A direção funcional está registrada e a aparência/posição foi implementada, mas a marcação ainda se repete entre páginas.

## 8. Critério de conclusão do mapeamento

O inventário estará pronto para orientar implementação quando cada decisão aplicável apontar para as rotas e famílias afetadas; cada componente indicar seus seletores e folha CSS; cada cor tiver status explícito (uso atual, referência, candidata ou homologada); os estados avaliados distinguirem evidência real de não testado; e os bloqueios acima tiverem responsável ou decisão seguinte registrada.

**Sem execução de testes nesta etapa.** Este mapa não certifica contraste, acessibilidade nem a implementação runtime atual.


## 9. Inventário visual estático — etapa seguinte

O inventário detalhado está em [VISUAL_INVENTORY.md](VISUAL_INVENTORY.md) e [visual-inventory.json](visual-inventory.json), baseado no produto `main` no commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`. Abrange oito entradas HTML, oito folhas CSS, seletores e declarações visuais por regra, breakpoints, espaçamento, tipografia, cores literais, movimento e assets rastreados.

A leitura documenta código estático; não substitui inspeção do DOM, captura visual, contraste runtime ou verificação de estados gerados por JavaScript. Assets sem referência estática ficam como não verificados. #A64D13 consta como base aprovada para promoção/comunicação comercial; variações e combinações por tema ainda ficam pendentes. Informação de processo usa o azul homologado e permanece separada de aviso, erro e sucesso.
