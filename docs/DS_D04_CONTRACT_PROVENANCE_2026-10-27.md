# D04 — decisões restritas e gates críticos da PR #51 (27/10/2026)

**Origem:** [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51) @ `28062602a4ddcd1bee090742fe2587fe3837175d`. [Manifesto com SHAs](DS_D04_CONTRACT_PROVENANCE_2026-10-27.json). Este lote mantém decisões históricas com seus limites, sem atualizar produto ou homologar amostras.

## ARC-13: nomeação aprovada, exemplos ainda propostas

A [convenção original](../evidence/architecture/arc13-semantic-key-convention-proposal-2026-10-24.json) registra `approval.userAuthorized=true` em **25/10/2026** para **a convenção de nomeação**, e não para as 13 sugestões individuais ou a migração do índice. O [histórico de cobertura](../evidence/architecture/arc13-semantic-key-coverage-2026-10-24.md) registra a evolução da fila.

Regras preservadas: manter o namespace de domínio, usar sufixo semântico estável `camelCase` em lugar do número da linha, manter valores dinâmicos como parâmetros e compartilhar chaves apenas com igualdade de *owner*, *consumer* e contrato de parâmetros. **Não criar chaves finais, não substituir traduções nem reescrever `decisions.json` a partir de exemplos.**

O histórico usa o snapshot do produto `5ccb2a8` e referencia batches de propostas que ainda estão na branch HOLD. Preservar o documento não garante que seus links relativos já estejam todos disponíveis na main.

## Viewer: falha de imagem-base/camada visível

O [registro original da decisão](../evidence/architecture/pr242-viewer-scene-image-failure-design-2026-10-26.md) atribui ao usuário a escolha de cobrir a cena e apresentar placeholder descritivo quando falha imagem-base ou camada visível, ocultando composição incompleta e mantendo o frame 3:2. Camadas ocultas não devem bloquear a cena. A implementação foi proposta/testada em PR #242 de produto, **sem aprovação de release ou inspeção visual final** naquele snapshot.

Os dois documentos de suporte citados no contrato **já estavam** na main com exatamente os mesmos blobs que a PR #51:
- [Implementação da cena e 17 testes unitários no head histórico](../evidence/runtime/pr242-viewer-scene-image-failure-implementation-2026-10-26.md).
- [Ensaio de falha 404 em versão anterior de preview](../evidence/runtime/pr241-public-image-failure-coverage-2026-10-26.md).

Esses testes e evidências não certificam a Production de hoje; não duplicar os arquivos.

## DS-05A: gate autenticado ≠ funcional completo

[Registro original](../evidence/runtime/ds05a-authenticated-preview-suites-2026-10-25.md): autenticação restrita, V5 e revogação passaram na PR #238 nos heads registrados; a primeira passagem falhou cinco suítes, a rechecagem subsequente passou Mobile/PiP, Summary/Pricing e Stone e manteve **Keyboard/Flow falhando**, com botões de etapas de caixa 0×0. Não classificar como certificação plena de experiência autenticada. Não inferir estado atual da issue #232 sem verificar o produto.

## Gate deste lote

**4 blobs exclusivos novos** (2 ARC-13, 1 contrato Viewer, 1 registro DS-05A) preservados com SHAs originais e **2 documentos complementares já presentes verificados por SHA**. A PR #51 tinha 201 caminhos exclusivos antes; após integração correta serão **197**, mantendo o head original. Não altera código, workflows, índices, tokens, decisões homologadas ou produção. As demais evidências (propostas volumosas, rastreios, testes, outros caminhos divergentes) continuam HOLD e precisam de classificação antes de fechar PR/retirar branch.
