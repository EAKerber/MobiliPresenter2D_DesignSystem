# ARC-15 — Inventário de verificações do Produto

**Estado:** primeira passada concluída; auditoria integral de assertions e decisão de redução continuam pendentes.  
**Fonte:** `EAKerber/MobiliPresenter2D` `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`.  
**Método:** leitura dos contratos, comandos, gatilhos e áreas cobertas; classificação por risco/assertion/rota/estado, não por quantidade de arquivos.  
**Execução:** nenhuma suíte foi executada nesta revisão. Nenhum teste ou workflow foi alterado.

## Parecer do Common Sense Judge

**Não há evidência para remover um teste inteiro.** Há repetições exatas de invocação que podem compartilhar a definição do job como trabalho de CI, mas cada SHA/integração ainda precisa receber sua própria execução e status; os workflows também têm garantias adicionais diferentes. Há também verificações parcialmente sobrepostas e um conjunto de arquivos sem invocação automática encontrada. Esses últimos são “sem alocação confirmada”, não obsoletos.

O inventário deve permanecer como primeira passada: não faz uma comparação linha a linha de cada assertion de todos os workflows e não prova que todas as verificações manuais sejam redundantes ou ativas.

## Contagem localizada

O script `app/package.json → scripts.test` contém 19 scripts Node e chama ainda dois validadores Python: `tools/validate-assets.py` e `tools/validate-r5a-pixelperfect.py`. São 21 comandos encadeados na suíte da pasta `app`, não 21 workflows nem a contagem de todos os testes do repositório.

Há 21 workflows YAML no pin analisado. Os comandos variam: alguns executam a suíte completa, outros executam unitários, browser gates, validators ou verificações de produção. A contagem de arquivos não mede repetição de assertions.

## Repetições exatas encontradas

| Contrato/comando repetido | Invocações observadas | Parecer |
|---|---|---|
| `npm test` da pasta `app` | `.github/workflows/app-build-purity.yml`, `candidate-assets.yml` e `variant-fidelity.yml` chamam o mesmo script em eventos de PR. `module02-fidelity.yml` também o chama, mas só por execução manual. | Repetição exata do comando; cada workflow acrescenta um contrato próprio (pureza de build, validação de entrada de assets ou fidelidade de variantes). Candidato a compartilhar a definição da execução via workflow reutilizável, executado para cada SHA aplicável. Manter cada gate adicional e status obrigatório; não remover nem enfraquecer checks. |
| `tests/public-cutover-contract.cjs` | `p-comp-01-public-menu-gate.yml`, `public-routing-before-clerk.yml` e `ux-auth-viewer-integration-gate.yml`. | A mesma assertion está repetida em três integrações. Candidata a compartilhar uma definição via workflow reutilizável, executada separadamente para cada head/integração; nunca reutilizar o status de uma branch em outra. Os testes de integração permanecem separados. |
| `node app/tools/test-core.js` | `summary-pricing-browser.yml`; o mesmo teste também é um dos 19 scripts de `app/npm test`. | Repetição parcial/subconjunto, dentro de um browser gate que verifica preço/resumo/persistência. Não elimina o gate de browser. |
| `npm test` em `module02-fidelity.yml` | Workflow de `workflow_dispatch`, usado para replay/manual. | Não é repetição de execução de PR em cada mudança; manter como ferramenta operacional até o owner classificar seu uso. |

## Sobreposição parcial com garantias distintas

| Família | Área compartilhada | Garantia que continua exclusiva |
|---|---|---|
| ARC03C e P-COMP do header público | Rotas públicas, temas, viewports e navegadores têm interseções. | `arc03c-published-pages-browser-differential.mjs` compara contra snapshot histórico com raster. `public-header-controller-gate.mjs` mede contra a implementação corrente, inclui Viewer, instância compartilhada e interação funcional do menu. |
| Fluxo, teclado e responsividade | Navegação por etapas e fechamento de detalhes; Escape aparece em mais de uma jornada. | `flow-layout-browser.cjs` cobre layout, política e seleção; `keyboard-browser.cjs` cobre teclado/foco/scroll; `nav-flow-responsive-crossbrowser.cjs` cobre perfis e limites de viewport. A interseção não substitui os contratos próprios. |
| Administração hierárquica, persistência e save V5 | Usam o mesmo harness/endpoints simulados do Admin. | Estrutura/opções, cancelamento e leitura após escrita, migração/reparo V3, edição nativa V5 e tratamento de resposta rejeitada são assertions diferentes. |
| Pedra/acabamento e resumo/preço | Percorrem superfícies do Configurador/fluxo V5. | Canvas, ordem de composição e reparo de legado diferem de subtotal/total, cobrança única, sincronização do resumo e persistência. |
| Viewer com preço base e overview editorial | Mesma rota Viewer. | Contrato de dados/fail-closed e toggle ON/OFF não é o mesmo que conteúdo editorial, benefícios, dimensões e layout sem preço. |
| Fallback de imagem, projeção pública e smoke | Leitura da página pública. | Teste unitário de recuperação, geometria/acessibilidade no browser, DTO fail-closed, smoke de preview e leitura GET-only de produção validam camadas distintas. |
| Assets de candidato | Oito testes Python compartilham entrada e dados de revisão. | Canvas/RGBA, hash/ROI, alpha fora da região aprovada, ordem de composição, proveniência, delta vazio/mismatch e direção de geometria são propriedades independentes; a decisão humana continua `PENDING`. |

## Verificações sem invocação automática localizada

A busca nos 21 workflows e em `app/package.json` não encontrou chamada explícita para:

- `tests/public-pages-integrated.cjs`
- `tests/ui-theme-contract.cjs`
- `tests/exposed-sides-glass.cjs`
- `tests/test_mask_semantics.py`
- `tests/test_stone_backing.py`
- `tests/test_stone_cleanplate.py`
- `tests/test_stone_surface_masks.py`
- `tests/validate-exposed-side-pixels.py`

Classificação atual: **destino não confirmado**. Podem ser manuais, históricos ou precisar de gate; não há evidência suficiente para excluí-los.

Há duas discrepâncias concretas entre gatilhos e comandos:

1. `candidate-assets.yml` observa `tests/**` como path trigger, mas sua lista explícita de unittest não executa os cinco testes Python de máscaras/stone/exposed-side listados acima. O trigger faz o workflow iniciar, mas não transforma esses arquivos em verificações executadas.
2. `arc03c-static-page-build-gate.yml` tem gatilho push limitado a branches históricas, sem `pull_request` ou `main`. O path filter inclui `tests/public-header-controller-gate.mjs`, porém o comando do workflow executa `tests/arc03c-published-pages-browser-differential.mjs`, não o controller gate. O controller é executado no workflow P-COMP.
3. `viewer-base-price-contract-gate.yml` executa testes unitários e browser, mas está em `push` para `main`/branch de integração e `workflow_dispatch`; não há trigger de PR.

## Decisões e pendências

| Disposição | Estado |
|---|---|
| Excluir testes por alta contagem ou semelhança de nomes | **Não recomendado.** Nenhum teste foi provado redundante no nível do contrato. |
| Consolidar execuções idênticas de `npm test` | Candidato de CI: compartilhar a definição do job, mantendo uma execução e status válidos para cada SHA aplicável. Antes, confirmar required checks e preservar as garantias extras de cada workflow. |
| Consolidar `public-cutover-contract.cjs` | Candidata a workflow reutilizável; executar separadamente para cada head e preservar os três gates de integração específicos e seus status. |
| Resolver os oito arquivos sem invocação | Owner deve classificar cada um como gate manual, histórico ou contrato que precisa alocação. Sem exclusão até essa disposição. |
| Alinhar path filters, comandos e PR trigger | Decisão do owner sobre intenção de ARC03C, candidate assets e viewer-base-price; depois corrigir os pares divergentes. |
| Fechar ARC-15 | Ainda falta matriz assertion→risco→rota/estado para todos os contratos e decisão dos itens não alocados. |

**Resultado desta passada:** nenhum teste foi removido ou adicionado. O inventário separa repetição de execução, interseção de domínio e lacuna de alocação; as próximas mudanças são decisões de CI/owner, não uma redução automática da suíte.
