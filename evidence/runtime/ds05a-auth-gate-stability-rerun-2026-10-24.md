# DS-05A — repetição do gate autenticado isolado

Data: 2026-10-24  
Repositório: `EAKerber/MobiliPresenter2D`  
PR: [#238](https://github.com/EAKerber/MobiliPresenter2D/pull/238)  
Head: `abc33d24d0ff34e770feb0e12221fa9ba98870fd)  
Execução Actions: [#40126678308](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40126678308), tentativa repetida do job isolado.

## Resultado

A tentativa repetida do job **“Isolated session redeem, bootstrap and revoke”** terminou em SUCCESS. O readback atual dos steps mostra êxito em: preflight de origem/papel, checagem de variáveis sem exibi-las, conexão com a fixture isolada, resgate do grant, bootstrap autenticado do Config, negação de Admin, revogação, guarda contra escrita nos arquivos protegidos e upload do artefato.

A execução carregou um novo artefato `ci-config-isolated-authenticated` de 553 bytes (SHA-256 informado pelo GitHub: `10989ef25dd31f6815a91967ffac1a48e7cdcc0a8ac6215fc29d08812e2f50ec`). O arquivo não foi baixado nem inspecionado nesta rechecagem; os valores de ambiente, URI, cookies e tokens não foram lidos.

Esta é a segunda tentativa consecutiva observada como sucesso no mesmo head, depois da primeira tentativa de #40126678308. Os quatro timeouts anteriores pertenciam a um head anterior e continuavam sem causa confirmada. A repetição diminui a incerteza sobre o gate atual, mas não prova ausência geral de flutuação.

## Limite de escopo

A reexecução confirma o gate de sessão real, readiness/bootstrap e fronteira de Admin no site de teste com o banco interno autorizado. Os cinco workflows funcionais legados continuam separados: Mobile/PiP, Keyboard, Flow, Summary/Pricing e Stone passam em fixture V5 local; não executam essas cinco suítes autenticadas no Deploy Preview/staging. A issue #232 permanece aberta até reconciliar essa cobertura, preservar o teste anônimo de redirecionamento e revisar/integrar a PR #238. Nenhum merge, alteração de Production ou nova permissão de banco ocorreu.
