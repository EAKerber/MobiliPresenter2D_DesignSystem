# ARC-15 — Inventário de verificações do Produto

**Estado:** primeira passada concluída; auditoria integral de assertions e decisão de redução continuam pendentes.  
**Fonte:** `EAKerber/MobiliPresenter2D` `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`.  
**Método:** leitura dos contratos, comandos, gatilhos e áreas cobertas; classificação por risco/assertion/rota/estado, não por quantidade de arquivos.  
**Execução:** nenhuma suíte foi executada nesta revisão ARC-15. Nenhum teste ou workflow foi alterado no pin `Product main@46a52e76`; branches de PR, inclusive #275, ficam fora deste inventário.

## Parecer do Common Sense Judge

**Não há evidência para remover um teste inteiro.** Há repetições exatas de invocação que podem compartilhar a definição do job como trabalho de CI, mas cada SHA/integração ainda precisa receber sua própria execução e status; os workflows também têm garantias adicionais diferentes. Há também verificações parcialmente sobrepostas e um conjunto de arquivos sem invocação automática encontrada. Esses últimos são “sem alocação confirmada”, não obsoletos.

O inventário deve permanecer como primeira passada: não faz uma comparação linha a linha de cada assertion de todos os workflows e não prova que todas as verificações manuais sejam redundantes ou ativas.

## Contagem localizada

O script `app/package.json → scripts.test` contém 19 scripts Node e chama ainda dois validadores Python: `tools/validate-assets.py` e `tools/validate-r5a-pixelperfect.py`. São 21 comandos encadeados na suíte da pasta `app`, não 21 workflows nem a contagem de todos os testes do repositório.

Há 21 workflows YAML no pin analisado. Os comandos variam: alguns executam a suíte completa, outros executam unitários, browser gates, validators ou verificações de produção. A contagem de arquivos não mede repetição de assertions.

## Matriz comando → risco/estado → âncoras

Escopo: os 21 comandos encadeados por `app/package.json → scripts.test` no Product `main@46a52e76`. As âncoras apontam para `app/tools/` e resumem a superfície/estado principal; não substituem a revisão de cada assertion. Workflows e branches de PR são avaliados separadamente.

| Comando (cwd `app/`) | Risco e estado/superfície | Âncoras |
|---|---|---|
| `node tools/test-access-policy.mjs` | Fronteiras de autorização: admin/staff/buyer, sessão temporária, grants e páginas/configurador internos. | `app/tools/test-access-policy.mjs:22–42` |
| `node tools/test-item-capabilities.js` | Compatibilidade entre tipo de item, etapa e ação disponível (seleção/toggle/ação). | `app/tools/test-item-capabilities.js:18–57` |
| `node tools/test-layout-profiles.js` | Seleção dos perfis responsivos compacto/empilhado/lateral e limites de largura. | `app/tools/test-layout-profiles.js:8–34` |
| `node tools/test-presentation-contract.js` | Combinações suportadas entre presentation, behavior e componente. | `app/tools/test-presentation-contract.js:11–172` |
| `node tools/test-flow-model.js` | Ordem e normalização de etapas/grupos/seções/itens; proteção contra mutação do fluxo. | `app/tools/test-flow-model.js:29–209` |
| `node tools/test-administration-v5.js` | Migração/validação do Admin v5, política de apresentação e preço tipado, sem autoridade legada paralela. | `app/tools/test-administration-v5.js:34–402` |
| `node tools/test-published-configuration.js` | Leitura simulada de `published` e normalização de documentos v3/v5. | `app/tools/test-published-configuration.js:22–81` |
| `node tools/test-published-buyer-projection.js` | Projeção buyer v3/v5 preserva hierarquia/etapas e expõe somente preço permitido. | `app/tools/test-published-buyer-projection.js:27–87` |
| `node tools/test-v5-publication-migration.js` | Preflight, ETag/`onlyIfMatch`, falhas, quantidade de writes e readback na migração v3→v5. | `app/tools/test-v5-publication-migration.js:23–131` |
| `node tools/test-v5-normal-save.js` | Concorrência no save v5, rejeição sem write e confirmação por revision/readback. | `app/tools/test-v5-normal-save.js:20–108` |
| `node tools/test-postv5-new-material-roundtrip.js` | Novo material: forma, grupo/acabamento/preço, projeção buyer, save/readback e módulo sem registro. | `app/tools/test-postv5-new-material-roundtrip.js:36–104` |
| `node tools/test-v5-offline-rehearsal.js` | Ensaio local de migração, assinatura/digest, um write exato e inspeção posterior. | `app/tools/test-v5-offline-rehearsal.js:40–162` |
| `node tools/test-v5-publication-inspection.js` | Preflight somente leitura de ETag/revision/digest, blob ausente, JSON inválido e estados de bloqueio. | `app/tools/test-v5-publication-inspection.js:22–92` |
| `node tools/test-v5-endpoint-safety.js` | Endpoint simulado: anônimo 401, staff 403, admin 200; isolamento preview/produção, cache privado, migração aposentada e sem downgrade. | `app/tools/test-v5-endpoint-safety.js:3–216` |
| `node tools/test-legacy-stage-repair.js` | Planejador puro de handles; aceita delta exato e rejeita delta, ordem ou owner inesperados. | `app/tools/test-legacy-stage-repair.js:16–39` |
| `node tools/test-flow-layout.js` | Grupos, spans, componentes e IDs semânticos no layout do fluxo. | `app/tools/test-flow-layout.js:32–208` |
| `node tools/test-hierarchy-administration.js` | Administração hierárquica v4, validação de groups/sections e ausência de autoridade flat paralela. | `app/tools/test-hierarchy-administration.js:29–187` |
| `node tools/test-hierarchy-editor.js` | Reordenação, divisão, mescla e movimento de grupos/seções sem mutar a origem. | `app/tools/test-hierarchy-editor.js:32–160` |
| `node tools/test-core.js` | Integração ampla: cena/seleção, DOM/CSS, configuração/preço/validação, estimativas, projeção buyer, markup/layout responsivo, dock/PiP/hotspots. | `app/tools/test-core.js:44–54, 64–92, 95–420, 541–720, 722–988` |
| `python3 tools/validate-assets.py` | Metadados SHA/canvas/alphaBounds, suporte de máscaras, ownership do módulo 02, bridge e composição golden. | `app/tools/validate-assets.py:27–172` |
| `python3 tools/validate-r5a-pixelperfect.py` | Reconstrução byte-exata, invariantes RGB/alpha da variante/máscara e igualdade de pixels na composição final. | `app/tools/validate-r5a-pixelperfect.py:11–103` |

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

A busca nos 21 workflows e em `app/package.json` não encontrou chamada explícita para os oito arquivos abaixo. Em particular, path filter correspondente não conta como chamada:

- `tests/public-pages-integrated.cjs`
- `tests/ui-theme-contract.cjs`
- `tests/exposed-sides-glass.cjs`
- `tests/test_mask_semantics.py`
- `tests/test_stone_backing.py`
- `tests/test_stone_cleanplate.py`
- `tests/test_stone_surface_masks.py`
- `tests/validate-exposed-side-pixels.py`

Classificação atual: **destino não confirmado**. Podem ser manuais, históricos ou precisar de gate; não há evidência suficiente para excluí-los.

Há quatro discrepâncias concretas entre gatilhos e comandos:

1. `candidate-assets.yml` observa `tests/**` como path trigger, mas sua lista explícita de unittest não executa os cinco testes Python de máscaras/stone/exposed-side listados acima. O trigger faz o workflow iniciar, mas não transforma esses arquivos em verificações executadas.
2. `arc03c-static-page-build-gate.yml` tem gatilho push limitado a branches históricas, sem `pull_request` ou `main`. O path filter inclui `tests/public-header-controller-gate.mjs`, porém o comando executa `tests/arc03c-published-pages-browser-differential.mjs`, não o controller gate. O controller é executado no workflow P-COMP.
3. `public-routing-before-clerk.yml` observa `tests/public-*.cjs`, o que inclui `tests/public-pages-integrated.cjs`, mas o workflow executa `tests/public-cutover-contract.cjs`, outros contratos públicos e `tests/public-pages-smoke.cjs`; não executa `public-pages-integrated.cjs`. O arquivo segue sem destino confirmado.
4. `viewer-base-price-contract-gate.yml` executa testes unitários e browser, mas está em `push` para `main`/branch de integração e `workflow_dispatch`; não há trigger de PR.

## Decisões e pendências

A consulta de branch protection do Produto não pôde ser lida nesta sessão (HTTP 403 da integração). O conjunto de required checks permanece **UNKNOWN**; sucesso de workflow, isoladamente, não prova que um check seja obrigatório.

| Disposição | Estado |
|---|---|
| Excluir testes por alta contagem ou semelhança de nomes | **Não recomendado.** Nenhum teste foi provado redundante no nível do contrato. |
| Consolidar execuções idênticas de `npm test` | Candidato de CI: compartilhar a definição do job, mantendo uma execução e status válidos para cada SHA aplicável. Antes, confirmar required checks e preservar as garantias extras de cada workflow. |
| Consolidar `public-cutover-contract.cjs` | Candidata a workflow reutilizável; executar separadamente para cada head e preservar os três gates de integração específicos e seus status. |
| Resolver os oito arquivos sem invocação | Owner deve classificar cada um como gate manual, histórico ou contrato que precisa alocação. Sem exclusão até essa disposição. |
| Alinhar path filters, comandos e PR trigger | Decisão do owner sobre intenção de ARC03C, candidate assets, public-routing e viewer-base-price; depois corrigir os pares divergentes. |
| Fechar ARC-15 | A matriz comando→risco/estado→âncoras dos 21 comandos está documentada; falta a matriz integral por assertion/rota/estado, a decisão dos oito itens não alocados e a confirmação dos required checks. |

**Resultado desta passada:** nenhum teste/workflow foi removido, adicionado ou executado no pin `Product main@46a52e76`. A matriz de comandos e os quatro desalinhamentos trigger→invocação estão documentados; as verificações sem destino, a matriz integral de assertions e as decisões do owner permanecem abertas. Nenhuma redução ou consolidação foi autorizada.
