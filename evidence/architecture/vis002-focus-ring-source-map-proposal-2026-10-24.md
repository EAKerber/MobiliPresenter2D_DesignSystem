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
