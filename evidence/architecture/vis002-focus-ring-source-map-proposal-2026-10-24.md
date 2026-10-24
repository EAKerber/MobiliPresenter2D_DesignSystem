# VIS-002 — mapa de regras de foco e escopo de revisão

**Estado:** proposta para revisão, não canônica. Produto consultado: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. Nenhum CSS, decisão ou runtime foi alterado.

## Fatos de origem

| Fonte | Regra atual | Escopo observado |
|---|---|---|
| `app/public-theme.css`, blob `e2add5053fbc1a897c035eb854b168c9711d2d18`, linha 23 | `:focus-visible { outline: 3px ...; outline-offset: 3px }` | Regra global da folha pública carregada na Landing. |
| `app/ui-theme.css`, blob `b0f04c566183ba1f9c015f5d2a827db9e91dea45`, linha 50 | `.ui-theme-toggle:focus-visible`: 3 px, offset 2 px, cor `--ui-theme-focus` | Exceção específica do controle de tema. |
| `app/ui-theme.css`, linhas 113–114 | `html[data-theme="light"] :focus-visible` força `#6E512E`; tema escuro força `#D8BC7C` | Seletor de cor não restrito a uma classe pública. Não foi inventariado em todas as rotas que carregam esta folha. |
| `app/about/about.css`, blob `b58689554cccd9493810fb66a383be2cb30c595a` | O link aparece em `:focus`, sem declaração própria de contorno | A proposta da PR produto #239 adiciona localmente 4 px/offset 3 px usando `--public-accent`. |

VIS-002 aprova contorno de 4 px/offset 3 px e pares de foco claro `#8B6A40` e escuro `#D8BC7C`. Em Production, a CSSOM desta sessão retornou 2.67 px para regra e elemento de teste com `outline:3px`, apesar das declarações-fonte de 3 px. A causa não foi identificada; os valores computados são mantidos separados dos valores declarados. A amostra de dez focos da Landing e a observação do skip link estão nos registros runtime referenciados no handover.

## Mapa candidato para revisão

| Componente/rota observado | Regra que fornece foco | Aplicação candidata da referência VIS-002 | Evidência/limite |
|---|---|---|---|
| Marca, CTA do cabeçalho, menu, CTA principal e botões de ambiente da Landing | Regra global de `public-theme.css`, cor substituída por `ui-theme.css` | 4 px/3 px; pares de cor aprovados para claro/escuro | Dez paradas de Tab em uma largura; não cobre todas as rotas. |
| Link “Pular para o conteúdo” de About | Regra global atual; a PR #239 propõe regra local 4 px/3 px | Manter o valor aprovado, depois validar a transferência de foco ao destino separadamente | O preview da PR cobre estilo; Production deixa foco no `body` após Enter. |
| Botão de tema | Regra própria 3 px/2 px em `ui-theme.css` | Considerar 4 px/3 px e os pares aprovados, sujeito a revisão do componente | Observado na Landing; outras instâncias do controle não foram mapeadas. |
| Controles de Configurador/Admin e outras rotas | O seletor de cor em `ui-theme.css` é amplo; CSS/DOM de todas as rotas não foi mapeado neste recorte | Não atribuir estilo sem inventário de componentes e superfícies | Evidência insuficiente para aplicar o mapa público a todas as telas. |

## Perguntas de decisão

1. Aprovar o mapeamento 4 px/3 px para os componentes públicos listados ou ajustar escopo/componente.
2. Decidir se o foco do botão de tema segue o mesmo tratamento ou uma regra contextual própria.
3. Definir quais rotas privadas recebem essa folha e quais consumidores precisam de auditoria antes de qualquer regra ampla.
4. Tratar a transferência do foco do link About como comportamento acessível separado da aparência visual.

A decisão canônica VIS-002 continua com implementação global não autorizada. Esta proposta não altera `decisions.json`, tokens, CSS ou produto.


## Mapa de consumo das folhas e exceções locais — leitura estática em 24/10/2026

**Base conferida:** produto main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf. Os hashes abaixo são os blobs lidos nesta revisão. O mapa cobre as oito páginas de entrada citadas no plano; não afirma cobertura de todo elemento dinâmico, sombra, iframe ou estado autenticado.

| Página | Folhas declaradas pela entrada | Regra que fornece anel / observação |
|---|---|---|
| / | app/index.html 9d025dc; public-theme.css; landing/landing.css; ui-theme.css | Regra pública 3 px/3 px; o seletor de tema substitui a cor por tema. A folha local de Landing não declara anel próprio. |
| /how-it-works/ | app/how-it-works/index.html 02accfa; public-theme.css; landing/landing.css; how-it-works.css 52f36d2; ui-theme.css | A ação econômica declara 2 px/3 px. |
| /about/ | app/about/index.html 0f830a9; public-theme.css; landing/landing.css; about.css b586895; ui-theme.css | A folha local só revela o skip link no foco; o anel vem das regras compartilhadas. |
| /viewer/ | app/viewer/index.html cdb303e; public-theme.css; viewer.css 90d2367; ui-theme.css | Cabeçalho declara 3 px/3 px; .scene-hotspot:focus-visible remove o outline e muda borda/fundo e exibe o rótulo. Exige revisão do indicador visual completo. |
| /config/ | app/config/index.html 97c284c; styles.css na raiz do site; ui-theme.css | <base href="/"> faz styles.css resolver para app/styles.css (d43e6fb). Botões/inputs declaram 2 px/2 px; pontos do carrossel 2 px/3 px; setas 2 px/2 px; controle PiP 2 px/2 px. .scene-hotspot remove outline, com borda/fundo/rótulo como pistas. A folha pública não é carregada nesta página. |
| /admin.html | app/admin.html 60139eb; admin/admin.css 1b3b41e; ui-theme.css | Regra comum de links/botões/inputs: 2 px/3 px; chave de publicação: 3 px/3 px. |
| /access/ e /access/manage.html | app/access/index.html e app/access/manage.html; public-theme.css; ui-theme.css | Regra pública 3 px/3 px com a cor substituída por tema; não há folha local de foco nessas entradas. |

ui-theme.css (blob b0f04c5, linhas 32–38, 50 e 113–114) declara o foco do controle de tema e seletores de cor amplos: claro #6E512E, escuro #D8BC7C. Nas páginas que carregam essa folha, a cor pode prevalecer sobre regras locais de outline; a geometria é mantida pela regra local mais específica ou por public-theme.css conforme a página. O cadastro de componentes e a cascata efetiva ainda precisam de conferência em runtime nas páginas privadas.

**Implicação para a revisão:** a diferença da referência VIS-002 não se limita à regra global 3/3. Existem exceções locais 2 px e offsets de 2 px, além de hotspots sem outline explícito. Não classificar os hotspots como falha sem avaliar em runtime as mudanças de borda, fundo, rótulo, recorte e contraste. Esta ampliação continua proposta, sem aprovação de novo token, alteração de decisions.json, CSS ou produto.

## Evidência runtime associada

- Runtime check em Production: foco por teclado no hotspot do módulo 02 mostrou borda e marcador visíveis em temas claro e escuro, sem ativar o módulo. Esta amostra não homologou contraste ou todos os estados: [registro](../runtime/viewer-scene-hotspot-keyboard-focus-production-2026-10-24.md).


## Evidência runtime adicional — Como funciona

- Runtime em Production: o botão “Compra em escala” recebeu foco por Tab e exibiu contorno. No tema claro, CSSOM confirmou outline `2px solid #6E512E`, leituras do offset retornaram `2.66667px` e, na confirmação, `3px` (a fonte declara 3 px); diferença sem causa isolada e superfície `#25231F`; o contraste calculado pelas cores computadas foi 2,15:1. O risco nesta combinação está observado. No tema escuro, o anel foi visto visualmente, sem readback CSSOM de cor/offset. [Evidência](../runtime/how-it-works-economy-action-focus-production-2026-10-24.md).


## Risco de cascata a confirmar

- Em Como funciona, a regra clara ampla vence a cor local do card. A leitura CSSOM em Production confirmou `#6E512E` sobre `#25231F`, com contraste calculado de 2,15:1. O risco está observado para o botão “Compra em escala” nesta rota/viewport; não generalizar para outros componentes. Uma leitura do offset retornou 2.66667 px e a confirmação retornou 3 px, como a fonte; a diferença não foi explicada. [Evidência e limites](../runtime/how-it-works-economy-action-focus-production-2026-10-24.md).
