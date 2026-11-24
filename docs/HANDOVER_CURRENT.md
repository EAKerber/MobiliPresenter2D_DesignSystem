# Handover atual — execução do plano v0.9

**Fotografia verificada em:** 24/11/2026 (BRT)  
**Escopo:** repositórios Product e Design System autorizados nesta conversa. Este handover é uma fotografia operacional, não declaração de conclusão do plano.

## Estado canônico dos repositórios

| Repositório | Ref | SHA verificado |
|---|---|---|
| Product | main | 01ded2c100fbfd8b16897e26113dc5068a83e429 |
| Product | development | 5ffe2ef7d6db33bf1a616bf7b500469b6ab725e9 |
| Design System | main | efe754d25466ba3b77dedde04bf1e2d7c0abc0e7 |

A comparação Product main..development usa a base comum 221b54b2a41ecc8c338d1bf2cf67280cf165ce95: development tem 537 commits exclusivos e main tem 17. Essa contagem descreve commits, não divergência semântica de runtime. A política permanece promoção seletiva; não fazer merge integral da árvore sem classificação de consumidores.

Não há PRs abertas nos dois repositórios. Product tem 16 issues abertas; Design System não tem issues abertas. As issues Product ainda precisam ser conciliadas com implementação e contratos atuais antes de receber estado de conclusão.

## Referências remotas preservadas

A API do GitHub reporta 9 branches no Product e 4 no Design System, 13 no total — não 60. O roster de 60 mencionado em handovers antigos pertence a um executor histórico de higiene e não é a contagem atual. Todos os refs abaixo foram lidos diretamente; nenhum foi excluído nesta atualização.

### Product (9)

| Branch | SHA | Leitura operacional |
|---|---|---|
| codex/arc13-localization-menu-theme-20261122 | fc12bb6 | candidata de localização/tema; integração não verificada |
| codex/nav005-development-buffer-20261121 | 9c18dd9 | buffer preservado; não tratar como descartável |
| codex/tst001-current-snapshot-20261124 | a8b31e3 | referência de evidência; pin a revalidar |
| codex/tst001-refreshable-inventory-20261124 | 6f7a0d3 | candidata stale: 3 commits à frente e 41 atrás de development; alteração vista somente no workflow de inventário |
| codex/tst002-buyer-boundary-crosswalk-20261124 | 57b2e96 | head da PR #395, integrada por squash em 5ffe2ef |
| codex/tst004-browser-image-setup-20261124 | c8c7f71 | setup/evidência de browser preservado; integração não verificada |
| docs/arc13-post-273-reconciliation-20261114 | 82cca3b | evidência documental preservada |
| development | 5ffe2ef | ref ativa |
| main | 01ded2c | ref estável |

### Design System (4)

| Branch | SHA | Leitura operacional |
|---|---|---|
| codex/handover-live-readback-20261124 | 5866813 | candidata documental divergente; 4 commits à frente e 3 atrás de main, apenas HANDOVER_CURRENT.md no diff observado |
| codex/plan-v09-post-384-handover-20261124 | 7e7abdd | candidata documental divergente; 1 commit à frente e 2 atrás de main |
| hygiene/ds-squash-124-125-129-20261123 | 1ae986b | finalidade e destino não revalidados nesta fotografia; preservar |
| main | efe754d | ref ativa |

As marcas de proteção reportadas pela listagem de branches são false. Isso não substitui uma auditoria de regras de proteção/regrasets. Não há PR aberta usando refs no momento da leitura. As classificações por nome são provisórias e não autorizam aposentadoria.

## Issues Product abertas

Lista lida em 24/11/2026; nenhum item foi fechado ou declarado resolvido por este handover:

- #232 — gates do Configurador falham antes do bootstrap
- #229 — execução sequencial de ajustes de login, Viewer e Como funciona
- #228 — publicação de preços base com controle global desligado
- #227 — benefícios e dimensões do rodapé do resumo
- #225 — cabeçalho NAV-005 do Viewer
- #222 — endpoint de sessão temporária em produção
- #218 — cabeçalho público compacto NAV-005
- #216 — pares claros homologados em textos públicos
- #215 — primeiro clique do menu da landing
- #213 — estado de sessão do menu após login
- #212 — carregamento Admin após login
- #208 — cobertura light/dark de DOM e CSS
- #207 — estado “Em breve” sem Viewer
- #206 — SVG técnico em dark mode
- #205 — cards de detalhes do Viewer em dark mode
- #192 — Identity Netlify e acesso temporário CP-PUBLIC

A próxima ação de MD-001/MD-002 é classificar cada issue contra o código, contratos ARC, consumidor, branch-alvo e evidência atual. Permanecer aberta no GitHub não prova que a implementação esteja pendente.

## Revisão dos gates e do atrito

- A PR #395 foi integrada somente em Product development, no SHA 5ffe2ef. O run de PR #45388513416 passou no job plan; a validação executou 23 testes, todos aprovados. A mudança foi limitada a testes/metadata CI e ao crosswalk parcial Buyer/DOM-013; não alterou runtime do Viewer, máscaras, imagens, dados de produto, main ou deploy.
- Não há run pós-merge para 5ffe2ef. O workflow test-impact-plan dispara no push apenas para alterações em workflows ou no gerador do inventário; os paths alterados pela #395 não satisfazem esse filtro. O gate de PR passou; isso não deve ser descrito como um gate pós-merge executado.
- O crosswalk Buyer de TST-002 mapeia seis grupos de assertions do endpoint, mas declara explicitamente escopo parcial. Seu sourcePin é 17f345a, anterior ao merge; âncoras foram validadas no head da PR, mas a fotografia do pin precisa ser reconciliada.
- O JSON TST-001 versionado em development ainda aponta para development@29cd75c, não para 5ffe2ef. Ele não é evidência do inventário atual. O branch TST-001 refreshable é divergente e não deve ser integrado sem port seletivo.
- O workflow test-impact-plan está em development e ausente em main. Por isso a opção workflow_dispatch não está disponível como caminho operacional no default branch. A tentativa de executar a partir da interface expirou sem iniciar run. O próximo snapshot precisa ser produzido por um trigger acessível, com main e development SHAs explícitos, antes de atualizar o JSON versionado.
- TST-004 e TST-022 continuam parciais. O seletor é advisory e não substitui nem desativa os workflows existentes. Comandos repetidos não provam assertions redundantes; conservar cobertura até validar trigger, filtros, condições, jobs, steps, assertions e custo representativo.
- TST-005 e a configuração de required checks precisam de nova leitura antes de qualquer decisão de proteção de branch.

## Próximas frentes, em ordem

1. Fechar MD-001 com um snapshot reproduzível: SHAs, árvores, branches, PRs, issues e limites de evidência.
2. Reconciliar o inventário TST-001 com os SHAs atuais e mapear workflow → evento/filtro → condição → job/step → comando → assertion → resultado.
3. Ampliar TST-002 por uma família de risco prioritária, sem ampliar o seletor sem necessidade.
4. Completar a revisão de TST-004/TST-022 com condições e custos; remover cobertura só com equivalência demonstrada.
5. Classificar os 17 commits exclusivos de main e planejar promoção por famílias e consumidores. Não fazer merge integral.
6. Prosseguir MD-002/003 e os pacotes DOM/CMP/ARC pelos respectivos DoDs; nenhuma fotografia aqui declara O0–O6 concluídas.

Netlify, deploy previews e Production não foram alterados. Qualquer avaliação de configuração Netlify deve seguir o caminho de navegador previsto no plano.