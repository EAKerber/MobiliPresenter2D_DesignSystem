# D04 — preservação dos 45 relatórios runtime históricos da PR #51 (27/10/2026)

**Origem imutável:** [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), head `28062602a4ddcd1bee090742fe2587fe3837175d`; contexto de produto observado nos relatórios `5ccb2a8` e heads específicos de PR, em 24–26/10. [Manifesto com path/tamanho/Git Blob SHA de cada um dos 45 arquivos](DS_D04_RUNTIME_EVIDENCE_BLOBS_2026-10-27.json).

## O que está sendo salvo

Os 45 relatórios cobrem **navegação/teclado**, cabeçalhos NAV-005, contraste e anéis de foco VIS-002/003, imagens e falhas, carrossel, movimento reduzido, além da fronteira de autenticação do DS-05A. Os arquivos originais permanecem imutáveis em `evidence/runtime/`, como **evidências históricas delimitadas**.

Alguns cuidados identificados nas amostras:

- A auditoria DS-05A distingue sessão/grant válido, revogação e presença da workspace das jornadas completas de Configurador/teclado/preço; um fixture PASS não certifica os demais casos.
- O diagnóstico de geometria dos controles de etapas em preview encontrou nav com caixas 0×0. Não pressupor que isso ainda ocorra nem que já foi corrigido sem ler a PR/issue de produto atuais.
- O registro da issue #224 é reprodução transitória de carrossel e uma correção isolada em preview da PR #243; não basta para concluir issue fechada ou correção em Production.
- As medidas de NAV-005 na PR #244 foram coletadas em preview **anônimo** e não cobrem as jornadas autenticadas.
- O foco de hotspots no Viewer e os keylines da PR #242 foram testados em preview, alguns com análise de pixels compostos; não significam homologação visual global/merge/Production. O comportamento autorizado pelo usuário continua limitado ao escopo do preview de origem.
- O screening de contraste público mediu contextos específicos e temas em Production datada; não certifica conformidade completa em todas as rotas/estados.

## Limite de autoridade

**O que uma observação de 24–26/10 permite:** reconstruir como uma decisão técnica foi testada e por quais gates passou naquela revisão. **O que não permite:** atualizar `decisions.json` sem autorização, criar novos tokens/CSS, assumir resultado atual de Actions/Netlify, garantir iPad/Safari/tecnologia assistiva, nem declarar defeito ainda aberto por causa do status antigo.

Esta PR copia **45 objetos Git sem alterar seus bytes** e registra fonte/proveniência. Não envolve cookies, banco, navegador, código do produto, deploy ou workflows ativos.

## Resultado e o bloqueio verdadeiro da poda

Após merge e leitura de árvores, todos os **caminhos exclusivos** do head `docs/current-handover-20261024` estarão representados em `main`: **45→0**. Isso fecha a destinação de caminhos que iniciou em 232 diferenças (#51), após séries D04 seletivas. A ref fonte deve permanecer **HOLD** enquanto não houver prova de preservação dos **blobs canônicos modificados e da história de commits** aceita pelo executor de branch hygiene. Um manifesto de SHA, mesmo completo, não equivale a ancestralidade nem permite eliminar uma ref divergente.

**Próximo gate de higiene (separado deste lote):** reavaliar as 11 versões divergentes que sobrepõem paths canônicos de `main`, preservar suas versões históricas por conteúdo/referência recuperável, verificar merge/squash/ancestralidade sob política homologada e só então considerar exclusão. A PR #39 e os outros HOLDs exigem gates próprios.
