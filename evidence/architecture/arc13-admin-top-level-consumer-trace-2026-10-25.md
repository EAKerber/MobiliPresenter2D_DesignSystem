# ARC-13 — rastreio do bucket Admin module/top-level — 25/10/2026

## Base e limite

Produto analisado: `EAKerber/MobiliPresenter2D` em `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`. A árvore de origem de `app/admin/admin.js` corresponde ao blob `79925345e43096df77bef54fe257e483f922edd8`; mapa lexical consultado: `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

A leitura do bucket de 14 ocorrências foi estendida da linha de origem ao primeiro call site/sink observável. Isso confirma consumers diretos no arquivo, mas não certifica todas as rotas autenticadas, mensagens renderizadas, efeitos de fallback, equivalência entre consumidores nem ownership de produto. Nenhuma chave foi proposta ou gravada; sem alteração no índice, catálogo, runtime ou `decisions.json`.

## Ocorrências rastreadas

| Linha(s) | Texto | Consumer e sink observado | Classificação / owner a confirmar |
|---|---|---|---|
| 78 | Valores de módulos e acessórios | `pricingRoles`; `renderPricing` percorre o par role/title e atribui title a `h2.textContent` (1164–1167). | Rótulo estático da interface Admin; sem parâmetros. |
| 80 | Adicional por acabamento | Mesmo consumer `renderPricing`, título do card. | Rótulo estático da interface Admin; sem parâmetros. |
| 81 | Adicionais locais | Mesmo consumer `renderPricing`, título do card. | Rótulo estático da interface Admin; sem parâmetros. |
| 82 | Adicionais globais | Mesmo consumer `renderPricing`, título do card. | Rótulo estático da interface Admin; sem parâmetros. |
| 86 | Valor fixo | `pricingTypeLabels[type]` preenche `option.textContent` no select de regra de preço (1187–1191). | Rótulo de interface Admin para enum conhecido; sem parâmetros. |
| 90 | Base: valor base de cada módulo elegível | `pricingBasisLabels[rule.basis]` preenche `small.textContent` (1214–1217); fallback é `Base: ${rule.basis}`. | Texto de interface Admin associado a contrato de preço. Preservar `rule.basis` como valor/parâmetro no fallback; owner do contrato de preço não confirmado. |
| 1439 | O limite é 12 etapas. | Clique em `addStageButton`; no limite, chama `setMessage(saveMessage, ..., "error")`. | Mensagem estática de erro da interface Admin; sem parâmetros. |
| 1442 | Nova etapa | Valor padrão passado a `window.prompt` para novo estágio customizado; pode ser aceito e persistido como `stage.label`. | Conteúdo inicial de estrutura configurável, não presumir interface-only; confirmar owner antes de colocar no catálogo de conteúdo. |
| 1443 | Nome da nova etapa | Título de `window.prompt` ao adicionar estágio. | Instrução estática do shell Admin; sem parâmetros. |
| 1451 | Nome da nova cor ou textura | Título de `window.prompt` ao adicionar material. | Instrução estática do shell Admin; sem parâmetros. |
| 1451 | Novo material | Valor padrão do mesmo prompt; se aceito, é salvo em `model.materials[].label`. | Valor de catálogo/editorial persistível. Pela decisão do usuário, manter ownership no catálogo e pedir revisão do owner; não substituir por copy localizada nesta etapa. |
| 1618 | Informe seu e-mail para receber o link de recuperação. | Botão `recoveryButton`; email vazio envia texto de erro a `loginMessage`. | Mensagem estática de validação Auth/Admin; sem parâmetros. |
| 1621 | Se a conta existir, você receberá um link para redefinir a senha. | Sucesso de `requestPasswordRecovery`; enviado a `loginMessage`. | Copy de segurança Auth. Manter a redação genérica para não revelar existência de conta; owner de Auth deve revisar. |
| 1623 | Não foi possível solicitar a recuperação. | Fallback de `error.message || literal` em falha da recuperação. | Fallback estático Auth; o texto dinâmico do serviço continua separado e não vira chave por inferência. |

## Resultado e próximos passos

O nome do bucket lexical escondia contexts diferentes: constantes consumidas por `renderPricing`, callbacks de ações de estrutura/material e mensagens de recuperação de conta. O rastreio confirma sinks UI para as frases estáticas, mas dois valores padrão podem virar dados persistidos; não devem ser tratados como simples microcopy.

Próximo lote sem alteração de produto: rastrear os outros buckets com a mesma regra, priorizando sinks reais e distinguindo texto de interface, conteúdo persistível, valores de enum/CSS e mensagens de serviço. Propostas individuais de chave permanecem pendentes de consumer/owner/contrato; não executar migração.
