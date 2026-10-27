# ARC-13 — rastreio do bucket Admin renderPricing — 25/10/2026

## Base e limite

Produto: `EAKerber/MobiliPresenter2D@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; fonte `app/admin/admin.js`, blob `79925345e43096df77bef54fe257e483f922edd8); mapa lexical `arc13-unkeyed-consumer-scope-map-2026-10-25.json`, blob `1c675dd30db5b0167e9e07dbda1e3aacb2801983`.

O bucket `function renderPricing` tem oito ocorrências sem chave. O caminho foi seguido até o toggle de publicação e os campos de regra de preço, observando o caminho de draft/publicação documentado no próprio código. Nenhuma chave foi proposta; sem alteração do produto, valores, catálogo ou `decisions.json).

## Os oito textos e seus consumers

| Linha(s) | Texto | Sink / condição | Owner e contrato |
|---|---|---|---|
| 1148 | Exibição pública no Viewer | Heading do cartão de toggle que controla a visibilidade de valores base no Viewer. | Copy de configuração Admin com efeito público; não confundir o rótulo do toggle com a ação de publicar. |
| 1156 | Mostrar preços base no Viewer | Texto do checkbox `viewerBasePricePublication`; o valor é lido de `model.viewerPricePublication.enabled`. O controle é desabilitado quando a configuração publicada não tem schema V5. | Label de setting. O checkbox altera apenas o draft; conservar condição de schema e o fluxo autenticado de publicação existente. |
| 1160 | Esta opção exige uma configuração V5 publicada. | Nota condicional quando o checkbox está desabilitado pela ausência de configuração V5 publicada. | Mensagem de bloqueio com condição técnica explícita; não generalizar para todo erro de publicação. |
| 1161 | Inicialmente desativado. Somente os valores base válidos dos módulos publicados e visíveis serão exibidos; não inclui opções e serviços. Alterar esta opção não publica nada até clicar em Publicar configuração. | Nota quando a configuração atende ao gate V5. Explica estado inicial, escopo de preço e separação de draft/publicação. | Explicação de regra de negócio/contrato; qualquer extração ou reescrita precisa preservar os três limites: somente base válida, somente módulos publicados/visíveis e publicação explicitamente acionada. |
| 1185 | Tipo de preço: ${publicLabel} | `aria-label` do select de tipo quando o papel de preço aceita mais de um tipo. | Template acessível com nome público do item, produzido por `priceLabel(role,id)`; o nome do catálogo permanece parâmetro/dado. |
| 1206 | Valor de ${publicLabel} | `aria-label` do input numérico de valor. | Template acessível com o mesmo nome dinâmico; unidades e quantias são renderizadas por controles separados. |
| 1216 | Base: ${rule.basis} | Fallback textual quando não existe label conhecido em `pricingBasisLabels`; caso haja mapeamento, usa o rótulo do enum. | O valor de basis é contrato técnico/dado. O fallback não deve converter enum em copy livre nem misturar label conhecida com valor bruto sem decisão de localização. |
| 1225 | Os valores publicados são estimativas para clientes. Custos, margens e dados de fornecedores não entram neste painel. | Nota ao final do painel de preços. | Limite de disclosure/comercial: valores exibidos são estimativas e excluem informação interna. Revisão de owner comercial antes de qualquer proposta de chave ou alteração. |

## Fronteiras de dados e estados

- O texto do toggle modifica somente o draft; o código exige a configuração publicada V5 e mantém o fluxo de publicação separado. Mudança neste consumer não deve alterar essa salvaguarda.
- Labels de linha vêm de `priceLabel(role,id)`; nomes de materiais, módulos e opções são dados do catálogo. Tipos, unidades (percentual/BRL), basis, centavos e pontos-base são valores/contratos, não copy.
- O label acessível de tipo só existe para papéis com múltiplos tipos. O label acessível de valor sempre usa o nome público dinâmico.
- A nota sobre estimativas protege informação de custos, margens e fornecedores e não é equivalente ao guidance geral de configuração.

## Resultado e próximo passo

Os oito candidatos incluem controles de setting, explicação de comportamento e divulgação comercial, mais dois templates acessíveis e um fallback de enum. Nenhuma chave foi proposta ou migrada.

Próximo bucket por volume ainda não rastreado no Admin: `renderObjects` (7 ocorrências). Separar labels de edição e textos de regra dos nomes, descrições e conteúdo de catálogo.
