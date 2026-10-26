# CI-BASELINE-01 — remoção do alvo supersedido e readback da fixture — 26/10/2026

## Escopo

Na PR de produto #238, a PR #245 foi consolidada e fechada sem merge. A branch antiga `fix/config-stage-nav-grid-track-20261025` ainda aparecia na allowlist do workflow e do gerador de fixture. Removi esse alvo: o gate autenticado, o plugin e o teste da fixture aceitam somente a branch e o Deploy Preview #238. O teste agora comprova que a branch antiga com review ID 245 é recusada.

## Evidência atual

- Produto PR #238, head `41dcc1424bdeea5782d977d2b0509c88f76fe156`, segue aberta/DRAFT.
- Os nove workflows de PR passaram; os dois workflows de push também passaram: gate anônimo/isolamento e gate autenticado.
- O gate autenticado cobriu preflight e variáveis obrigatórias sem exibi-las, contrato da fixture, resgate do grant de teste, negação de Admin, revogação e as cinco suítes de navegador.
- Deploy Preview principal e isolado terminaram SUCCESS. O deploy isolado #238 é `6adea0c144bb0ee47add6707`.
- O artefato estático `/ci-validation/published-v5-status.json` no preview confirmou `verified: true`, review ID 238, branch esperada, store `configurator-settings`, chave `published` e schema `ConfiguratorAdministration2D 5.0`. A readback da própria função confirmou o registro; `GET /api/public-modules` respondeu HTTP 200.
- O digest da fixture é `a055dbbee3330b77abd38e5588a1713c3d2a25573fed7ac636829c7279bc0003`. Nenhuma credencial ou URI do banco foi incluída no artefato.

## Limites

A confirmação HTTP 200 vale para o Deploy Preview #238, que recebeu a fixture de validação. Ela não confirma o conteúdo do store primário do site isolado nem muda a Production. Não houve merge; a PR permanece aguardando revisão humana.
