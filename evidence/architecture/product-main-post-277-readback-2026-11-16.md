# Product main readback after PR #277 — 16/11/2026 (BRT)

**Nota temporal:** este recibo registra o estado imediatamente após a integração da #277, quando sua branch ainda estava presente. Ela foi removida depois com autorização específica; a leitura atual de 5 refs está no [recibo de higiene posterior](product-branch-hygiene-post-277-2026-11-16.md). O commit e o tree da `main` permaneceram inalterados.

## Escopo e fonte

Este recibo registra a revisão read-only da integração e publicação do controle de tela cheia nas páginas inicial e “Como funciona”. A alteração é de interface e comportamento do player; não altera dados, configuração publicada ou CSS do Design System.

- PR [#277](https://github.com/EAKerber/MobiliPresenter2D/pull/277), head `1d1f68a19836830f071a153e1a3ee11ca1446410`, foi integrada por squash no commit [`efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`](https://github.com/EAKerber/MobiliPresenter2D/commit/efc40584c3f3ca940cf6cbca408f8fda31e3e1c9).
- A branch `fix/how-video-fullscreen-control-20261116` continua presente em `1d1f68a19836830f071a153e1a3ee11ca1446410`; preservada após a integração.
- Leitura da ref `main`: `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`, árvore `439fb0fc9a3295f9e45486198e9de83fca8376ee`.
- A PR mantém um controle próprio sobreposto. O contêiner da moldura entra em tela cheia, o botão permanece visível e muda seu ícone e nome acessível para sair; o mesmo botão retorna ao modo embutido.

## CI, preview e produção

- Os 11 workflows associados ao head exato da PR terminaram `completed / success`: [43799448351](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448351), [43799448699](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448699), [43799448367](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448367), [43799448359](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448359), [43799448353](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448353), [43799448384](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448384), [43799448417](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448417), [43799448443](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448443), [43799448453](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448453), [43799448357](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448357) e [43799448375](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/43799448375).
- No [Deploy Preview #277](https://deploy-preview-277--mobilipresenter2d.netlify.app/), abrir e sair da tela cheia foram exercitados nas duas páginas.
- O deploy de produção [6afa7bee50b552356a973df4](https://app.netlify.com/sites/mobilipresenter2d/deploys/6afa7bee50b552356a973df4) está `READY`, branch `main`, contexto `production`, commit `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`, publicado em 16/11/2026 às 03:43:58 UTC. Alias: [casaemmodulos.casa](https://casaemmodulos.casa/).
- As páginas de produção inicial e [Como funciona](https://casaemmodulos.casa/how-it-works/) foram lidas de volta e carregaram os assets versionados do novo build. A interação de clique para entrar/sair foi testada na prévia; não foi repetida por clique diretamente na produção.

## Estado do programa e limites

- O Product tem 6 refs: `codex/ds04-208-preview-batch-20261111@a6c64305`, `codex/nav005-public-compact-main-20261110@43c9f566`, `development@1a69ff76`, `docs/arc13-post-273-reconciliation-20261114@68441080`, `fix/how-video-fullscreen-control-20261116@1d1f68a` e `main@efc40584`. Cinco é gatilho de revisão, não hard cap; a branch da #277 fica preservada até revisão própria.
- #269 continua Draft/não mergeável e #274 Draft/não mergeável; #271 está aberta, sem Draft e reporta mergeável. As três seguem com base `main@46a52e76`, anterior à main atual, e precisam de reconciliação com seus gates.
- ARC-13 continua sendo snapshot da main46. Reconciliar o delta de #275 e #277; incluir o rótulo acessível de saída e seus estados sem criar disposição ou chave por inferência.
- ARC-15 segue sendo inventário histórico da main46. Os 11 workflows de #277 validam aquele head de produto, mas não atualizam nem substituem a matriz assertion→risco→rota/estado; required checks continuam UNKNOWN.
- DS-05A identifica proveniência de fonte para main64, mas as capturas CSSOM não foram repetidas sobre `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`. A validação hospedada de `/config/` segue HOLD. Nenhum gate arquitetural se fecha por este recibo.
- Esta atualização documental não executou suítes, não altera runtime, não publica o Design System e não integra a PR #119.
