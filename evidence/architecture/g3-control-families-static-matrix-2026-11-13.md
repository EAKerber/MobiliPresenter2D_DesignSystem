# G3 — Matriz estática por componente, shell e estado — 2026-11-13

## Pin e método

Fonte: Product main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7. Nesta passagem, GitHub confirmou main idêntica a esse SHA. Leitura estática de CSS, HTML e geradores/listeners JavaScript. Não houve teste, CSSOM, captura de tela ou inspeção com leitor de tela.

## Matriz de ownership

| Família/shell | Owner e estados visíveis na fonte | Classificação G3 |
|---|---|---|
| Botões públicos — Home, Sobre e Como funciona | Base e variantes públicas em app/landing/landing.css:57–61; o padrão também se aplica a links CTA. Foco recebe regra base em app/public-theme.css:23 e cor temática em app/ui-theme.css:113–114. As páginas acrescentam estilos próprios. | Variantes do shell público. Não são o mesmo contrato dos botões Admin ou Configurador. |
| Botões Admin | app/admin/admin.css:27–30,71; foco geral em :6; botão desabilitado reduz opacidade a 0,55 e usa cursor wait em :29. | Família de domínio própria, com tratamento de foco/desabilitado distinto. |
| Botões do Configurador | app/styles.css:82–103,657–658; foco geral em :96 e desabilitado com opacidade 0,35 em :100. | Família própria. A classe .button é homônima entre shells, com dimensões, variantes e estados contextuais. |
| Rótulo eyebrow — público, About, How, Viewer, Admin e Access | Base pública em app/landing/landing.css:48; variações em app/about/about.css:7, app/how-it-works/how-it-works.css:20,77,146, app/viewer/viewer.css:9 e app/admin/admin.css:17. Access define regras inline em app/access/index.html:15 e app/access/manage.html:22. | Rótulo editorial/de contexto com vários donos. Cor, margem e escala são locais; não é controle interativo e não precisa de matriz hover/foco própria. |
| Hotspot de cena — Configurador e Viewer | app/core/scene-component.js:33–60 cria botão nativo, nome acessível e aria-pressed; sincroniza hidden, disabled, tabIndex, aria-disabled e seleção. Chamadas em app/app.js:692,1547 e app/viewer/scene-adapters.js:106,112,157. | Contrato DOM/JS compartilhado; skins CSS diferentes. |
| Skin de hotspot — Configurador | app/styles.css:145–188. | Variante específica do Configurador; foco e z-order precisam de cena real para concluir equivalência. |
| Skin de hotspot — Viewer | app/viewer/viewer.css:47–70; inclui elevação do contêiner em foco e halo dependente do tema. | Variante intencional de shell; não deduplicar junto ao Configurador sem prova visual/funcional. |
| Erro/status — Admin | admin.js usa data-kind=error, estilizado em app/admin/admin.css:30. Status de login/save, feedback de serviço e mensagens ao vivo têm locais/roles próprios em app/admin.html:59,66 e no gerador Admin. | Mensagem de operação e erro de serviço não formam um único componente só por compartilharem cor ou palavra “erro”. Confirmar seus owners/roles em cada fluxo. |
| Erro/status — Configurador | app/app.js:2529–2545 cria role=alert e oculta/deixa inerte o workspace na falha impeditiva. | Erro que bloqueia a configuração; separado do status de operação Admin. |
| Erro/status — Access Manage | app/access/manage.html:76 e app/access/manage.js:123–126 mantêm região polite e atualizam o texto no catch. | Feedback de gerenciamento próprio; não inferir o mesmo anúncio de um alerta impeditivo. |

## Mapa dos estados

| Estado | Público | Admin | Configurador | Viewer/hotspot | Access |
|---|---|---|---|---|---|
| Foco | Regra geral em public-theme.css com cor em ui-theme.css. | Regra geral de 2 px; publicação de preço usa exceção própria de 3 px. | Regra geral de 2 px. | Hotspot é botão nativo com estado de foco e tratamento visual próprio no Viewer; ordem/elevação dependem da cena. | Regras e foco precisam de revisão por consumidor; este passe não fecha CSSOM. |
| Hover | Varia por CTA e navegação pública. | Botões e controles usam regras locais; a intenção entre shells não está consolidada. | Regras locais por controle e região. | Seleção/elevação afeta o palco e precisa de contexto real. | Sem equivalência geral demonstrada. |
| Disabled/hidden | Não há contrato universal para todos os CTAs públicos. | Botão usa opacity 0,55/cursor wait; controles podem ter restrições por dados. | Button usa opacity 0,35; estados são produzidos pelo domínio. | O helper sincroniza hidden/disabled/tabIndex/aria-disabled; não existe uma regra de skin disabled comum demonstrada. | Estados pertencem ao fluxo autenticado/gerenciamento. |
| Erro/status | Fora desta matriz como componente público comum. | data-kind, regiões polite e alert são distintos por fluxo. | role=alert para falha impeditiva com workspace inerte/oculto. | Acessibilidade depende de seleção e contexto da cena, não do erro geral da página. | Região polite própria. |

A classificação do estado de foco/hover/disabled acima descreve ownership e regras encontradas; não é prova de estilos computados, contraste, sequência de teclado ou anúncio real.

## Disposição e próximo gate

- .button: **homônimo por shell**, sem contrato visual global demonstrado.
- .eyebrow: **variante contextual/editorial**, sem estados de interação próprios.
- .scene-hotspot: **contrato JS/DOM compartilhado com skins distintas**.
- erro/status: **contratos semânticos por fluxo**, sem um componente transversal comprovado.
- Nenhuma regra CSS deve ser promovida a compartilhada nesta passagem. G3 ganha classificação estática destas famílias; o gate geral permanece parcial.
- O próximo subgate visual precisa de uma matriz restrita por risco: cada shell × papel do botão × estado base/hover/foco/desabilitado; hotspots nas cenas reais do Viewer e Configurador com seleção, foco e empilhamento; mensagens de erro/status no fluxo autenticado e no erro impeditivo.

## Limites

Este resultado não fecha dimensões computadas, contraste composto, hit-area, sequência de foco, touch, leitor de tela, persistência nem performance por rota. A avaliação de screenshots/CI e de um dispositivo real permanece separada. Não foram alterados código do Produto nem decisões do Design System.
