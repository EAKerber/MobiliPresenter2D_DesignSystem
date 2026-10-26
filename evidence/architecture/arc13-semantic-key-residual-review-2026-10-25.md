# ARC-13 — gate de revisão das ocorrências sem proposta (25/10/2026)

## Fonte e contagem

Mapa ARC-13 congelado para o produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, fonte `app/admin/admin.js` e `app/app.js`, com hashes registrados no mapa. Após excluir um seletor CSS e propor lotes contextuais, restam **16 identidades únicas** sem proposta entre 331 identidades distintas (336 linhas candidatas brutas; cinco linhas duplicadas não desambiguáveis). As propostas existentes são documentais e não canônicas; o produto e o índice ARC-13 permanecem intactos.

## Decisões que bloqueiam as próximas chaves

| Grupo | Ocorrências | O que falta decidir |
|---|---|---|
| Plural e listas — 8 | Admin: `admin.js:380`, `1028`, `1048`; Configurador: `app.js:950` (dois fragmentos), `1650`, `2273` (inclusão e remoção). | Definir a forma de pluralização e a composição de contagens/listas sem manter `disponível(is)`/ `selecionado(s)` ou flexões incorretas. A fundação de schema/localização ainda não escolheu formato de mensagem. |
| Strings com HTML — 3 | `app.js:1603` (`Estimativa` em markup), `1607` (estado sem preço em markup), `1661` (estado equivalente em outro consumer). | Definir a fronteira da chave e a montagem segura do DOM. Recomenda-se localizar texto por nó e manter o HTML/estrutura no código; os dois consumers de estado continuam separados pela convenção aprovada. |
| Ownership de catálogo/editorial — 5 | `app.js:1064` (eixos de dimensão), `1639` (explicação longa do resumo), `1653` (declaração sobre Módulo 02), `1725` (rótulo e descrição padrão do puxador ausente). | Atribuir quem responde pelo conteúdo e se cada valor pertence a dados do catálogo/produto ou à interface. O contrato de localização dos dados do catálogo ainda não foi definido. |

## Risco relacionado, já fora da fila de 16

A chave candidata `admin.pricing.basisFallback` localiza somente o prefixo fixo. O fallback ainda exibe `rule.basis` literalmente quando o mapa de rótulos não contém o enum; é preciso definir uma tabela de rótulos humanos ou uma política de fallback seguro antes da migração.

## Estado

A convenção ARC-13 foi aprovada; exemplos individuais continuam candidatos. Não há autorização para alterar `decisions.json`, o índice canônico ou o runtime por este registro. Próximo gate: decidir o contrato de pluralização e nomear owner dos cinco itens de conteúdo; em paralelo, confirmar a abordagem de nós de texto para as três strings misturadas com HTML.


## Readback após decisões do usuário — 25/10/2026

- **Plural/listas (8):** adiadas até a etapa de localização, quando o contrato de mensagens será definido. Permanecem sem proposta por escolha de escopo, não como bloqueio desta triagem.
- **Strings com HTML (3):** proposta documental criada em [arc13-semantic-key-proposal-configurator-html-text-nodes-2026-10-25.json](arc13-semantic-key-proposal-configurator-html-text-nodes-2026-10-25.json). São cinco chaves para três identidades de origem: uma label de estimativa e dois nós de texto em cada um dos dois consumers de preço pendente. A estrutura HTML permanece em código; nenhuma migração foi feita.
- **Catálogo/editorial (5):** permanecem no catálogo e aguardam revisão do owner de conteúdo. Nenhuma chave é proposta até essa revisão.

A medição documental passa a **318/331 identidades (96,1%)** com propostas; **13** seguem sem proposta (8 adiadas + 5 aguardando owner). Convenção aprovada, exemplos ainda não canônicos. Sem alteração de produto, índice ARC-13 ou `decisions.json`. O fallback de enum bruto continua como risco separado antes de migração.

## Verificação do fallback de enum no Admin — 26/10/2026

Readback do produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`:

- O Admin mostra o rótulo conhecido para `eligible-module-base`; o fallback textual em `renderPricing` só seria usado quando `pricingBasisLabels` não tiver o valor. [Origem e chamada no Admin](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/admin/admin.js#L89-L91) · [fallback](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/admin/admin.js#L1216).
- O contrato aceita somente `eligible-module-base` como base percentual, e `validateRule` rejeita qualquer valor diferente. [Enum e capacidades](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/core/pricing-contract.js#L7-L20) · [validação](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/core/pricing-contract.js#L53-L75).
- A projeção do price book valida o contrato antes de produzir o formato legado. A entrada administrativa hierárquica também valida settings V3; a entrada legada passa pela normalização, que valida o mesmo price book. [projeção e validação do price book](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/core/configuration.js#L19-L25) · [upgrade hierárquico](https://github.com/EAKerber/MobiliPresenter2D/blob/5ccb2a8dde6dd16e136f03387dc833aab828c5cf/app/core/hierarchy-administration.js#L67-L78).

**Conclusão delimitada:** no fluxo validado desse head, a tabela de rótulos cobre toda base percentual permitida, então o fallback de enum bruto não é alcançável por dados válidos. Ele permanece uma defesa para dado inválido ou validação contornada; não é uma ocorrência adicional a localizar neste recorte. A proposta [admin.pricing.basisFallback](arc13-semantic-key-proposal-admin-pricing-basis-fallback-2026-10-25.json) continua apenas documental e não deve ser tratada como autorização para mudança de runtime, índice canônico ou `decisions.json`. Se o conjunto de bases permitidas crescer, reavaliar rótulos localizados e o fallback antes da migração.