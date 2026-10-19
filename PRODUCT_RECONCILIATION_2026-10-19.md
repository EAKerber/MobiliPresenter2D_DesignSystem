# Conciliação runtime após as correções do produto

**Observado:** 2026-10-19  
**Produto:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D)  
**Deploy publicado:** [483ef2e6f76a562a3096516ef68d8dfe072ec21f](https://github.com/EAKerber/MobiliPresenter2D/commit/483ef2e6f76a562a3096516ef68d8dfe072ec21f), Netlify deploy `6ad5a4e245dad08b373fcbd1`, estado `ready`.  
**Inventário estático:** ainda baseado no commit anterior `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`; os números e extrações estáticas não foram regenerados nesta atualização.

## Correções reconciliadas

- [PR #219](https://github.com/EAKerber/MobiliPresenter2D/pull/219) definiu o contador como módulos visíveis, excluiu iluminação, removeu o valor fixo inicial e aplicou a cor legível por tema.
- [PR #220](https://github.com/EAKerber/MobiliPresenter2D/pull/220) recalcula a contagem depois de aplicar a configuração publicada.
- [PR #221](https://github.com/EAKerber/MobiliPresenter2D/pull/221) contém as camadas da cena no cartão compacto para que não cubram o menu.

## Verificação runtime

No configurador publicado, em tema claro e viewport de 516 × 800 CSS px, a primeira leitura ocorreu antes da carga assíncrona: sete módulos selecionados e contador 7/7. Depois de aplicar a configuração publicada, os sete controles estavam desmarcados e o contador atualizou para **0 de 7 módulos visíveis**, com estimativa R$ 0,00. Essa verificação confirma a atualização final do contador; não avalia interações feitas antes da resposta de carregamento, que o usuário decidiu deixar fora do escopo atual.

Na mesma largura, abri o menu. Os grupos de navegação e seus links ficaram visíveis sobre a cena, sem a imagem do forno cobrir “Como funciona”. A leitura DOM do cartão retornou `isolation: isolate`, conforme a correção da PR #221. A captura raster foi exibida durante a revisão, mas não foi persistida como arquivo nesta atualização.

## Estado dos achados

- **FIND-006 / produto #209:** resolvido pelas PRs #219 e #220; o issue foi fechado após a validação em produção.
- **FIND-009 / produto #214:** resolvido pela PR #221; o issue foi fechado após a validação em viewport estreito.

As medições anteriores que descrevem o estado do produto no commit `298c114` permanecem como evidência histórica daquele snapshot; não devem ser lidas como estado atual desses dois achados.

## Próxima atualização do inventário

A próxima regeneração estática deve apontar para o commit de produto `483ef2e` e registrar a nova origem como snapshot atual, atualizando apenas os arquivos afetados e preservando as referências históricas. A auditoria runtime continua pendente para os estados listados em `FINDINGS_REGISTER.md`, inclusive o primeiro clique no menu público, a transição de sessão após login e o cabeçalho público compacto.
