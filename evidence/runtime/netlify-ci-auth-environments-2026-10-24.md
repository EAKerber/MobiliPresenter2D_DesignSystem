## Alvos e readback

- Netlify principal `mobilipresenter2d`: deploy Production READY `6adc221479c773577ed45e23`, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Netlify isolado `m2d-auth-ci-isolated`: deploy Production READY `6adc77b6603e52a336fe045d`, publicado às 09:18 UTC em `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- O pacote do isolado lista nove Functions, incluindo `access-check`; o campo de presença de Edge Functions está ativo.
- Readback de nomes e escopos confirmou `DATABASE_URL` e `ACCESS_GATE_SECRET` disponíveis nos contextos `dev`, `branch-deploy`, `deploy-preview`, `production` e `dev-server`, com escopos `builds`, `functions` e `runtime`. Os valores não foram copiados para este registro. A leitura confirma existência e escopo, não igualdade/correção dos valores nem conectividade.

## Separação do gate

O workflow `.github/workflows/ci-baseline-01-isolated-authenticated.yml` da PR produto #238 lê `CI_STAGING_DATABASE_URL` como segredo e `CI_STAGING_SUPABASE_REF` como variável do GitHub Actions Environment `ci-auth-isolated`. O alvo é `https://m2d-auth-ci-isolated.netlify.app`. A validação autenticada anteriormente registrada passou no run #40075575871 no commit `a9129e1`; a head atual da PR é `a2835c6`. O readback da head mostra os Deploy Previews do Netlify como SUCCESS, mas não houve nova execução do gate autenticado após o deploy Production mais recente.

Esses valores do GitHub Actions são independentes das variáveis Netlify. As funções usam as chaves de ambiente Netlify em produção/preview, enquanto a fixture autenticada da CI conecta pelo GitHub Environment. O deploy READY não exercitou as funções nem comprovou o valor efetivo, a conectividade ao banco ou a Edge Function.

## Próxima ação e limites

Antes de considerar o runtime de autenticação validado, rodar o gate autenticado da PR #238 contra o host isolado e registrar resultado. O gate CI e as funções Netlify usam conexões separadas. Não substituir a conexão do GitHub Environment por uma variável Netlify.

Este registro verifica metadados do deploy e existência/escopo das chaves, sem copiar valores para o repositório. Não lê dados do banco, não exercita Functions, não valida conectividade e não altera configuração, produto ou deploy.


## Rechecagem da projeção pública isolada — 24/10/2026, 22:00 UTC

- Em `m2d-auth-ci-isolated`, o endpoint de Production `/api/public-modules` respondeu HTTP 503; o Deploy Preview #242 do mesmo site também respondeu 503. No host principal `casaemmodulos.casa`, o mesmo endpoint respondeu 200 com schema `PublicModulePresentation2D 0.1` e sete módulos.
- A observabilidade do deploy isolado identificou invocação da Function `public-modules` e status 503, sem linhas de log da Function. A resposta pública não expõe a exceção interna.
- Releitura de nomes de variáveis confirma `DATABASE_URL` e `ACCESS_GATE_SECRET` no site isolado, escopos `builds/functions/runtime`; nenhum valor foi lido ou validado.
- A fonte de `netlify/functions/public-modules.mjs` não lê `DATABASE_URL`. Ela lê a chave `published` do Netlify Blobs store `configurator-settings`. No contexto Production, dado ausente/não armazenado ou inválido retorna 503; no Deploy Preview, a ausência local tenta buscar a projeção pública do domínio principal do próprio site, que também está retornando 503.

O 503, portanto, não evidencia uma variável adicional de banco faltante. O estado específico do Blob e a exceção interna permanecem desconhecidos; sem logs da Function não foi possível distinguir snapshot ausente/inválido de falha de leitura. Nenhum valor de segredo, dado do banco ou conteúdo privado foi acessado; nenhuma configuração foi alterada.
