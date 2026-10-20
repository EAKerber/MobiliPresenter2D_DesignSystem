# Revisão do fluxo de login e sessão

**Data local:** 2026-10-19  
**Site:** [casaemmodulos.casa](https://casaemmodulos.casa/)  
**Natureza:** observação autenticada, somente leitura. A autenticação foi concluída pelo usuário no navegador; nenhuma credencial foi enviada ou registrada nesta evidência.

## Sequência observada

1. A tela /admin.html recebeu a autenticação. As solicitações POST /.netlify/identity/token e GET /.netlify/identity/user responderam 200.
2. Sem recarregar nem sair da página, o editor administrativo carregou. GET /api/admin-bootstrap e as duas chamadas observadas a GET /api/configuration responderam 200. A mensagem “Não foi possível carregar os dados administrativos” não apareceu nesta visita.
3. A primeira abertura do menu na mesma página continuou mostrando “Entrar na administração” e omitiu as páginas privadas e a ação de saída.
4. Na mesma sessão, uma navegação nova para /access/manage.html carregou e exibiu o menu autenticado com páginas privadas, páginas públicas e ação de saída.
5. /config/ carregou a configuração publicada sem mensagem de erro; o indicador inicial mostrou 0 de 7 módulos visíveis.

A divergência do menu é uma reprodução nova do relato do issue [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213). Ela separa o estado do menu na página onde a autenticação ocorreu do estado reconstruído numa navegação posterior.

## Evidência de código servido e hipótese

Os scripts carregados nessa tela são módulos separados: core/private-navigation.bundle.js e admin/admin.bundle.js. A inspeção do JavaScript servido encontrou uma cópia do módulo de autenticação/eventos em cada bundle, com listeners locais ao próprio módulo. O módulo do cabeçalho consulta o estado inicial e assina seu próprio barramento; o Admin publica a mudança de login na cópia do bundle administrativo.

**Hipótese de alta confiança:** os barramentos separados não propagam a mudança de login entre o Admin e o cabeçalho. Isso explica o editor autenticado com menu anônimo e a recuperação numa nova navegação, que volta a consultar o usuário persistido. A causa ainda não foi corrigida nem confirmada por teste isolado; nenhuma implementação foi feita nesta revisão.

## Falha independente no fallback de sessão temporária

A consulta POST /api/access/session retornou 404 com HTML da página de erro. Repeti a chamada sem dados de sessão e testei a URL direta /.netlify/functions/access-session-status; ambas responderam 404. No mesmo site, /api/configuration, /.netlify/functions/configuration, /api/admin-bootstrap e /.netlify/functions/admin-bootstrap responderam 200.

No código consultado de main, netlify.toml declara a rota para a função e netlify/functions/access-session-status.mjs existe. A observação confirma que a rota/função não está acessível no deploy visto, mas não isola se o problema é divergência de deploy, empacotamento ou roteamento. O registro de backlog independente é [issue #222](https://github.com/EAKerber/MobiliPresenter2D/issues/222).

Esse endpoint é usado como fallback de leitura da sessão temporária. Nenhuma sessão temporária foi criada ou validada nesta visita; o impacto nesse fluxo ainda precisa de confirmação. O 404 não explica a divergência reproduzida de Netlify Identity.

## Sintoma de carregamento administrativo (#212)

Não reproduzi a mensagem de falha de dados nesta visita. A autenticação, o bootstrap administrativo e as leituras de configuração responderam 200 e o editor carregou. Isso não prova que a falha intermitente foi resolvida, pois a sequência que a dispara não foi identificada.

## Limites e segurança

- A visita não identificou independentemente o SHA exato do deploy servido. O Design System já registra a última referência Netlify conhecida; ela não é atribuída automaticamente a esta reprodução.
- Os menus autenticados foram observados funcionalmente, mas os valores de e-mail e convites não foram copiados, persistidos nem incluídos nesta evidência.
- Nenhum dado de catálogo, convite, configuração, tema ou sessão foi salvo/alterado pela inspeção.
- Não foi executada suíte automatizada nem houve correção de código.
- Validar o caso da sessão temporária requer uma sessão temporária válida; ela não foi criada durante esta auditoria.


## Análise estática do caminho do issue #212

O caminho normal de login do bundle aguarda Identity, obtém o JWT e grava o cookie antes de emitir o evento e retornar o usuário. Em seguida, o formulário chama showUser(user). O listener do mesmo bundle também chama showUser(user), portanto há duas execuções próximas. ensureAdminData, entretanto, compartilha adminDataPromise e deve agrupar a chamada a /api/admin-bootstrap. As duas execuções podem seguir para loadSettings após a promessa ser resolvida.

A mensagem literal observada pelo usuário é emitida quando /api/admin-bootstrap retorna não-2xx. A função admin-bootstrap diferencia 401 (Identity não resolve usuário), 403 (sem permissão) e 503 (Identity indisponível), mas o cliente transforma todos esses casos na mesma mensagem. O código enfraquece a hipótese simples de a chamada ocorrer antes do cookie no fluxo normal; ainda permite investigar desacordo temporário do contexto Identity no Netlify, indisponibilidade ou outra resposta HTTP. Sem status/duração da execução que falhou, a causa permanece aberta.

Registro seguro sugerido para futura captura: marcos da autenticação e bootstrap, presença do cookie apenas como booleano, status HTTP, duração e request ID. Não registrar token, e-mail, corpo de resposta ou conteúdo administrativo. Nenhuma instrumentação foi implantada.
