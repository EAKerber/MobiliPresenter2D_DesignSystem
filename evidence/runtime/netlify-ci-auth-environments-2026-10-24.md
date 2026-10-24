# Netlify e CI autenticado — separação de ambientes (24/10/2026)

## Alvos e readback

- Netlify principal `mobilipresenter2d`: deploy Production READY `6adc221479c773577ed45e23`, `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Netlify isolado `m2d-auth-ci-isolated`: deploy Production READY `6adc77b6603e52a336fe045d`, no mesmo commit `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- O pacote do isolado lista nove Functions, incluindo `access-check`; o campo de presença de Edge Functions está ativo.
- Não foram registrados valores de variáveis ou credenciais.

## Separação do gate

O workflow `.github/workflows/ci-baseline-01-isolated-authenticated.yml` da PR produto #238 lê `CI_STAGING_DATABASE_URL` como segredo e `CI_STAGING_SUPABASE_REF` como variável do GitHub Actions Environment `ci-auth-isolated`. O alvo é `https://m2d-auth-ci-isolated.netlify.app`. A validação autenticada anteriormente registrada passou no run #40075575871 no commit `a9129e1`; a head atual documentada da PR é `a2835c6`, com commits posteriores somente de documentação. O readback da head atual mostrou os dois Deploy Previews Netlify como SUCCESS; não há novo resultado do gate autenticado após o deploy atual.

Esses valores de GitHub Actions são independentes do `DATABASE_URL` do Netlify. No site isolado, o contexto `dev` foi o único em que a variável Netlify correspondeu ao projeto Supabase interno confirmado. Os contextos `production` e `deploy-preview` coincidiram com os valores do projeto Netlify principal e não identificaram esse projeto. As Functions de grants e sessões leem `DATABASE_URL` do ambiente Netlify; portanto essa diferença pode afetar o fluxo servido pelo host isolado mesmo quando a etapa CI conecta diretamente ao banco por meio do GitHub Environment.

## Próxima ação e limites

Alinhar `DATABASE_URL` do Netlify isolado com a conexão interna de teste nos contextos efetivamente usados pelo host isolado (Production para o domínio principal; Deploy Preview se ele for exercitado). Em seguida, executar novamente o gate autenticado por `workflow_dispatch` no GitHub Actions. Não substituir a conexão do GitHub Environment por uma variável Netlify.

Este registro verifica metadados de contexto, deploy e referências do código; não lê dados do banco, não exercita Functions, não lê conteúdo de segredos e não altera configuração, produto ou deploy.
