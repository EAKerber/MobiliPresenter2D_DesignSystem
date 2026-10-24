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
