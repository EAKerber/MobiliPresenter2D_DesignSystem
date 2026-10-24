# VIS-002 — proposta de foco para cartões sobre superfície escura (24/10/2026)

## Status e escopo

**Proposta experimental; não canônica e não aprovada.** Derivada do achado FIND-017 nos seis cartões de “Por que custa menos?” em `/how-it-works/`. Não altera `decisions.json`, CSS ou código do produto.

O registro canônico VIS-002 aprova a referência visual de foco 4 px/offset 3 px e as cores `#8B6A40` para claro e `#D8BC7C` para escuro. A própria decisão mantém sem especificação o mapeamento componente/superfície e registra `implementationAuthorized: false`; portanto esta proposta não autoriza implementação.

## Contexto medido

No tema claro, a seção dos cartões continua com superfície opaca `#25231F`. A regra atual computa anel `#6E512E`, 2 px/offset 3 px, contraste **2,15:1**. No tema escuro, o anel computa `#D8BC7C` sobre a mesma superfície, **8,52:1**. Os valores foram lidos nos seis cartões em Production; veja [FIND-017](../runtime/how-it-works-economy-focus-six-cards-production-2026-10-24.md).

## Opções calculadas para a superfície escura

| Opção | Cor do anel em `#25231F` | Contraste calculado | Observação |
|---|---|---:|---|
| A — resolver pelo fundo | `#D8BC7C` | 8,52:1 | Reutiliza a cor já aprovada para foco no modo escuro, independentemente do tema da página. |
| B — preservar cor clara por tema | `#8B6A40` | 3,16:1 | Reutiliza a cor já aprovada para foco no modo claro; o contraste calculado nesta superfície é menor. |
| Atual | `#6E512E` | 2,15:1 | A regra atualmente publicada falha no limiar de 3:1 para indicador não textual. |

Ambas as opções propostas usariam a geometria de referência existente: 4 px/offset 3 px. A opção A tem maior margem de contraste nesta superfície; a escolha visual e o mapeamento por contexto ainda requerem aprovação do usuário. Os cálculos usam pares opacos sólidos e não comprovam aparência/área do foco no DOM final.

## Próximo passo proposto

Revisar A e B no contexto visual real e selecionar uma regra por superfície. Só depois atualizar o mapeamento canônico com aprovação explícita e autorizar uma mudança restrita aos seis cartões; validar foco/contraste pós-implementação nos dois temas. Não generalizar a regra para outras rotas ou superfícies.
