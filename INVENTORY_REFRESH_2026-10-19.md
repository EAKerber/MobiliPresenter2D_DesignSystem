# Atualização do inventário visual — 2026-10-19

**Produto:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D)  
**Snapshot anterior:** `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`  
**Snapshot atual:** [`483ef2e6f76a562a3096516ef68d8dfe072ec21f`](https://github.com/EAKerber/MobiliPresenter2D/commit/483ef2e6f76a562a3096516ef68d8dfe072ec21f)  
**Delta:** três commits, sem commits posteriores ao snapshot anterior no histórico comparado.

## Arquivos reconciliados

A comparação entre os snapshots mostrou sete arquivos alterados:

- CSS: `app/about/about.css`, `app/how-it-works/how-it-works.css`, `app/landing/landing.css`, `app/styles.css` e `app/ui-theme.css`.
- HTML: `app/config/index.html`.
- JavaScript: `app/app.js`.

Os cinco arquivos CSS tiveram bytes, linhas, seletores de classe, regras visuais e agregados de cores atualizados em `visual-inventory.json`. A página do Configurador teve bytes e linhas atualizados; as referências de assets, classes estáticas e estilos inline permaneceram iguais.

## Delta visual registrado

- `about.css`: par contextual claro `#705C4B` para texto da superfície de escala.
- `how-it-works.css`: texto claro `#705C4B`, eyebrow `#70522F` e faixa da legenda escura `#20211F` com texto `#F0EDE8`.
- `landing.css`: descrição do hero clara em `#705C4B`.
- `styles.css`: o estado do contador passou a usar `var(--text)`; o cartão da cena no perfil compacto recebeu `isolation: isolate`.
- `ui-theme.css`: resumo claro usa superfície `#F0EDE8`, divisor `#D6CCC0`, rótulo `#292723`; o cabeçalho privado passou de `z-index: 30` para `60`.
- `config/index.html`: o contador inicial agora exibe travessões e o rótulo “módulos visíveis”.
- `app.js`: a atualização do contador deixa de somar iluminação e recalcula após aplicar configuração. Continua fora do inventário CSS/HTML; nenhuma análise semântica de funções/eventos JS foi incluída.

## Contagens reconciliadas

- Classes CSS distintas: **428** (antes 426).
- Classes estáticas no HTML: **251**.
- Custom properties: **43**.
- Ocorrências de cores literais: **467** (antes 459), em **238** valores distintos.
- Breakpoints, espaçamento, movimento e assets não mudaram nestes arquivos; os totais correspondentes permanecem os do inventário anterior.
- Rotas e folhas carregadas permanecem oito HTML e oito CSS.

A extração estática registra presença e contexto de uso; não homologa valores fora das decisões já registradas nem valida contraste/runtime por si só. As evidências do deploy e seus limites estão em [PRODUCT_RECONCILIATION_2026-10-19.md](PRODUCT_RECONCILIATION_2026-10-19.md).

## Situação de achados homologados

A comparação do CSS atual com as decisões mostra que as correções de FIND-002, FIND-003 e FIND-004 já estão no produto publicado via PR #219. Os issues do produto #216 e #217 continuam abertos porque ainda não foi feita a confirmação pós-deploy dos valores computados e do fundo composto no DOM. Não se reaproveitam os antigos contrastes medidos como resultado da versão nova.

A fonte canônica `decisions.json` também foi reconciliada: VIS-002 e VIS-003 registram que os pares contextuais selecionados estão aplicados no CSS publicado, com confirmação do DOM pós-deploy ainda pendente. Isso registra o estado da implementação e não amplia a homologação nem aprova tokens globais.
