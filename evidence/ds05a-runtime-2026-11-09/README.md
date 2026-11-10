# DS-05A: runtime CSSOM de /config/ (2026-11-10)

## Estado e proveniência

Este diretório preserva uma execução local anterior, sem promovê-la a gate DS-05A concluído. Ela inicializou o Configurador real servido apenas em loopback, usando configuração sintética derivada dos defaults versionados; não chamou Netlify, Supabase, Identity nem endpoints externos.

| Item | Identidade |
|---|---|
| Produto | MobiliPresenter2D |
| Commit remoto de origem | development@1a69ff76a5f36e3245a288773bb409aa662e4e62 |
| Árvore completa desse commit | 6dff4a40f1f10db8e783e3da7604c6e0144d3e10 |
| Árvore app/ pinada | 6b5f66dab510221ebef216a3b0613fec904d10d7 |
| Checkout local que executou a captura | audit/ds05a-static-development-1a69ff76@62bda9cb9ae5bd67b062a1596af179c4071d449e |
| app/ no checkout | árvore acima antes do patch candidato |
| Patch local da captura | somente a regra .module-number abaixo; blob resultante 5c90f1936fedff2e7081018e51fc9c84c9083c14, SHA-256 5b11afd500f8545d723a87b22f586c2c8f42e4f9b4fc22f4e953e96da4ae0545 |
| Recibo | runtime_cssom.json, 228.554 bytes, SHA-256 aad1f18832d988d13ed635216a91db2eeeb3f5f1cb8fce9bb004131828bb1291 |
| Runner | theme_cssom_runtime_v1.cjs, 15.290 bytes, SHA-256 27c923948a20e896c8fc59e013523b4baebacbd4e6450f19a738855fe78b48da |
| Relatório de proveniência local | DS05A-static-css-provenance-development-1a69ff76.md, SHA-256 7c639f7ac39658f06f931c5baa43222de6e24a8efb6c14056d2c4a1adfab6480 |
| Momento gravado pelo recibo | 2026-11-10T01:38:03.548Z |

O checkout de origem estava sujo: app/ui-theme.css tinha a regra candidata; o relatório estava modificado; o runner era não rastreado. A captura incluiu a regra candidata, que não pertence ao commit remoto de development. candidate-module-number-light.css.patch conserva somente essa linha como proposta inerte. Não copiar a regra para main ou development, nem tratá-la como decisão aprovada.

## Reprodução controlada

Para reconstruir a mesma entrada de código em um clone descartável do produto:

1. Crie um worktree limpo em 1a69ff76a5f36e3245a288773bb409aa662e4e62; não limpe nem reutilize um checkout de trabalho sujo.
2. Confirme que git rev-parse HEAD:app retorna 6b5f66dab510221ebef216a3b0613fec904d10d7.
3. Aplique candidate-module-number-light.css.patch somente nesse worktree descartável para reproduzir a variante capturada.
4. Use Node.js com suporte global a WebSocket e aponte CHROMIUM para um binário Chromium local. Execute:
   ```powershell
   $env:CHROMIUM = 'C:\caminho\para\chromium.exe'
   node .\evidence\ds05a-runtime-2026-11-09\theme_cssom_runtime_v1.cjs C:\caminho\para\clone-MobiliPresenter2D C:\caminho\para\saida-local
   ```
5. Compare o novo recibo com este. O script grava timestamp novo; use o SHA-256 para identificar cada execução.

O recibo original não registra as versões exatas de Node.js/Chromium nem o binário escolhido por CHROMIUM; portanto, não se afirma reprodução byte-a-byte nem equivalência de engine. Ele registra apenas o nome da pasta do checkout, então a identidade completa acima foi reconstruída de fontes locais e mantida aqui. O teste test_cssom_v2.cjs (8 fixtures) cobre o runner de fixtures theme_cssom_v2.cjs, não este runner de DOM real; não usar esses 8 PASS como validação deste script. Esta incorporação não executou o runner novamente.

## O que a captura mediu

Seis estados iniciais de /config/: 390, 1050 e 1366 CSS px, em temas light/dark. Foram observados 7 módulos, 4 puxadores e 6 acabamentos; 70–74 candidatos de texto por estado. Não houve par computável abaixo do limiar; 98 pares permaneceram UNCERTAIN por backdrop-filter. A regra local candidata para os números de módulo não é parte da origem remota.

Limites: somente DOM inicial do Configurador, light/dark e três larguras; não cobre 320/768 px, tema auto, hover/foco/seleção/erro/loading/dock, Admin montado, revisão visual completa ou dispositivo real. DS-05A permanece INCOMPLETO/HOLD.
