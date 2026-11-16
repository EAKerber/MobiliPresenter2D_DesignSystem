# ARC-13 — Parecer Common Sense Judge sobre delta público após #273

**Data:** 2026-11-15  
**Snapshot avaliado:** Product `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`  
**Inventário:** SHA-256 `b3739e5ff57005600665cc6c1a04fbe986649b8f8e8e9b80a6fb09b2d3adf178` — 1.021 sinks e 359 fontes JavaScript  
**Objeto de revisão:** os dez sinks alterados ou novos listados na triagem pós-#273 da Draft #274.

## Escopo e limite

Este parecer recomenda categorias de conteúdo e função. Ele separa a escolha explícita do owner, a evidência de texto, recomendações semânticas e decisões ainda abertas sobre chaves, compartilhamento entre rotas e extração runtime. Não altera `ownerDisposition`, não cria chave canônica nem autoriza migração.

Fontes: [triagem de sinks pós-#273](https://github.com/EAKerber/MobiliPresenter2D/blob/docs/arc13-post-273-reconciliation-20261114/docs/architecture/arc13/sink-triage-post-273-2026-11-14.md), revisada contra Product `main@46a52e76`; [WAI-ARIA 1.2 — generic](https://www.w3.org/TR/wai-aria-1.2/#generic) e [group](https://www.w3.org/TR/wai-aria-1.2/#group).

## Parecer por sink

| ID | Origem e conteúdo observado | Categoria / parecer | Pendente |
|---|---|---|---|
| `fef001dc224c5527` | Home: alt “Ambiente planejado com uma apresentação da Casa em Módulos no celular” no snapshot #274, relativo à arte pós-#273 | Texto alternativo da arte daquele snapshot. A Draft #275 propõe arte e alt mais recentes; não transferir automaticamente a decisão para a nova versão. | Owner confirmar o alt correspondente à arte mais recente; decidir a chave separadamente. |
| `fbd72115b1e559f2` | Como funciona: botão visível “Expandir em tela cheia” | Texto fixo de controle. | Chave e extração. |
| `bda52494adf51488` | Home: `aria-label="Mais informações"` num `div` genérico | Não catalogar enquanto o nome não tiver semântica exposta válida. O papel genérico não aceita nome acessível. | Corrigir a semântica antes de catalogar. A Draft #275 propõe `role="group"`; é recomendação técnica ainda não integrada nem validada com leitor de tela, não uma decisão de conteúdo do owner. |
| `e185d906c6f85858` | Home: “Saiba mais” → `/about/` | O owner escolheu explicitamente texto e destino; texto fixo de link. | Chave e extração continuam decisões separadas. |
| `0c5db734ff22f8ae` | Home: “Assistir no YouTube ↗” | Parecer semântico: “Assistir no YouTube” é o texto do link; `↗` funciona como indicador visual decorativo de link externo. Hoje a seta integra o nome acessível. | Se essa recomendação for adotada, ocultar a seta do nome acessível. A recomendação não é decisão explícita do owner. Chave e extração continuam pendentes e específicas da rota. |
| `1deb819af5cc5953` | Home: nome do grupo “Vídeo de apresentação no celular” | Nome acessível fixo. | Chave e extração. |
| `3abe647cf8ac759d` | Home: botão “Reproduzir o vídeo de apresentação” | Nome acessível fixo de ação. | Chave e extração. |
| `e84c51cae0cd9c6e` | Home: tooltip `title="Tela cheia"` | Tooltip/metadado do controle. | Chave e extração; considerar junto do nome acessível do mesmo controle. |
| `fd28c05616bfb437` | Home: nome acessível “Abrir vídeo em tela cheia” | Nome acessível fixo de um controle. | Chave e extração. |
| `93f686ffaaeffa8e` | Home: título do iframe “Casa em Módulos — apresentação institucional” | Metadado acessível do vídeo. A ocorrência análoga em Como funciona sustenta uma categoria comum, não uma chave de rota compartilhada. | Chave e extração específicas da rota. |

## Disposições e decisões

O parecer recomenda classificações para os dez sinks, sem aprovar strings por categoria nem criar chaves. A única revisão de conteúdo do owner identificada aqui é a confirmação do alt, pois a arte foi atualizada. A correção do nome no `div` genérico é uma pendência técnica de semântica/acessibilidade antes de catalogar, não uma escolha de conteúdo do owner. A aprovação explícita “Saiba mais” → `/about/` cobre somente texto e destino.

“Tela cheia”, “Abrir vídeo em tela cheia” e “Expandir em tela cheia” pertencem a superfícies e controles distintos; a evidência disponível não demonstra inconsistência que exija decisão do owner. Permanecem pendentes apenas as chaves e a extração. O cabeçalho “Casa em Módulos, início” — incluindo a vírgula aprovada pelo owner — fica fora destes dez sinks.

Nenhuma disposição do owner foi alterada: os dez registros continuam com `ownerDisposition: pending` no snapshot da triagem. O código de runtime não foi alterado por este parecer.

## Delta posterior na Draft #275

O head atual da Draft #275 (`80d6024901f8a0827ce2f3e67bbe83f793e65f42`) mantém e alterna os rótulos de controles da Home, incluindo “Controles do vídeo”, “Reproduzir o vídeo”, “Pausar o vídeo”, “Tela cheia” e “Sair da tela cheia”. Esses valores não pertencem ao conjunto de dez sinks do snapshot #274. O commit mais recente ajusta o enquadramento da mídia 9:16 e fixa a faixa de controles em 42 px, sem alterar os rótulos. Se #275 for integrada, recapturar o inventário ARC-13 no novo head antes de tratar qualquer um deles como coberto, criar chaves ou extrair runtime. A PR continua Draft e esses valores não receberam disposição neste parecer.

## Resultado

O parecer recomenda classificações, mas não altera `ownerDisposition`, inventário, chaves ou código. Nenhum sink foi removido, nenhuma chave foi criada e nenhum teste foi executado.

## Adendo — reconciliação de inventário após #277 (16/11/2026)

O relatório ARC-13 atualizado está em Product #274, head `dc3e55f4b930e241d0c921eb95055c8a97429543`, sobre `main@efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`. Seu JSON válido tem SHA-256 `abce38889ad6d78c634fadad5d6f0c63fd9706ac3e0c13bcdf13f78010caeb9e`: 1.026 sinks, 360 fontes JavaScript, 420 ocorrências HTML mapeadas e zero ocorrências sem owner/rota. O crosswalk pós-#277 preserva o snapshot de 15/11 e registra os remapeamentos por posição, os registros novos/removidos e a fonte dinâmica de estados do controle. O JSON antigo versionado na revisão de 15/11 tinha um marcador literal de truncamento e não passava parse estrito; a comparação usa a referência válida reconstruída do código exato, com SHA-256 `4e5c81e286cbab81b3b6a69ad7fe899d4e10c940df629aed34a090ed6e38a819`.

### Disposição de conteúdo e semântica

- **Home, alt da arte:** agora “Cozinha planejada com uma mão segurando um celular” (`dcd455a9fecf63aa`). O resultado visual foi aprovado pela pessoa decisora, mas isso não confirma que a descrição textual seja factual nem que seja o melhor alt. Manter a confirmação de conteúdo pendente; nenhuma chave é inferida.
- **Tela cheia nas duas páginas:** os nomes acessíveis e tooltips foram normalizados para “Abrir vídeo em tela cheia”; o estado imersivo atualiza `aria-label` e `title` para “Sair da tela cheia”. Esses quatro pontos de escrita são anotados como suplemento porque o scanner não expõe os valores condicionais em `sourceEntries`; não os somar novamente como sinks. A classe do controle e o estado `aria-pressed` não são copy.
- **Home, “Mais informações”:** `role="group"` agora fornece semântica compatível com nomeação no markup. Isso resolve a incompatibilidade anterior do `div` genérico no nível estático; revisão com tecnologia assistiva, chave e extração continuam pendentes.
- **Home, “Saiba mais” → `/about/`:** mantém a autorização explícita somente para texto e destino. Ela não aprova compartilhamento de chave nem extração.
- **Erro de player do YouTube:** “Não foi possível carregar o player do YouTube.” é lançado e descartado pelo fluxo de fallback, não apresentado ao usuário; classificar como diagnóstico, sem propor localização com base apenas no texto literal.
- **Fallback de imagem:** o diagnóstico “Imagem indisponível” mudou de origem/ID na árvore atual e não deve ser tratado como texto visível sem uma nova ligação a sink consumidor.

O adendo substitui apenas o status live do antigo delta pós-#273. As classificações do snapshot main46 e as aprovações textuais mantêm a proveniência original. Não houve alteração em `ownerDisposition`, aprovação de catálogo, alteração do runtime ou validação assistiva nesta atualização. Evidência detalhada: [reconciliação](https://github.com/EAKerber/MobiliPresenter2D/blob/dc3e55f4b930e241d0c921eb95055c8a97429543/docs/architecture/arc13/inventory-reconciliation-post-277-2026-11-16.md) e [crosswalk](https://github.com/EAKerber/MobiliPresenter2D/blob/dc3e55f4b930e241d0c921eb95055c8a97429543/docs/architecture/arc13/inventory-crosswalk-post-277-2026-11-16.json).
