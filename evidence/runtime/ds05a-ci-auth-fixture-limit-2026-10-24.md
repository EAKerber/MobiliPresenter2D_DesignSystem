# Limite de cobertura DS-05A no fixture autenticado — 24/10/2026

## Fonte

- Repositório do produto: [PR #238](https://github.com/EAKerber/MobiliPresenter2D/pull/238), ainda DRAFT.
- Workflow autenticado reportado como SUCCESS: [run #40075575871](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40075575871), attempt 4.
- Arquivo de teste observado no head da PR: `tests/ci/config-auth-isolated-browser.mjs`, blob `6eec281f658ba81125ad6131194bf759805c508e`.

## O que o teste comprova

O fixture valida o host e o papel PostgreSQL limitado, cria um grant temporário de cinco minutos, resgata a sessão pelo endpoint real, usa o cookie HttpOnly para abrir `/config/`, aguarda o bootstrap e confirma `.workspace` e o perfil de layout. Ao final, revoga o grant e confirma que a sessão revogada volta a `/access/`.

Os pontos relevantes estão nas linhas 75–77 (workspace/bootstrap) e 78–82 (negação de Admin).

## Limite para DS-05A

Este run prova que o fixture autenticado alcança e inicializa o Configurador no host de staging. O teste não verifica os nós do contador de módulos nem da barra de preço/próxima etapa, e não mede o detector genérico. Ele consulta `/api/admin-bootstrap` esperando 401/403; portanto, não abre nem monta as opções do Admin. O resultado AUTHENTICATED_FIXTURE_PASS da PR não equivale a DS-05A concluído.

## Próximo passo seguro

Reutilizar o fixture de Config para inspecionar e registrar o DOM real dos dois alvos do Configurador, caso esse incremento seja aprovado no escopo do PR. Para as opções do Admin, é necessária uma sessão administrativa de teste controlada ou um fixture separado explicitamente autorizado; não ampliar o papel `access_ci_fixture` nem suas permissões por inferência.


## Alvos de DOM localizados no código-fonte

A fonte estática atual do produto identifica `#visibleCount` e `#totalCount` em `app/config/index.html` (blob `97c284c9831de05607ede0d024e4d919a898b7fa`, linha 100) e o preço em `#configurationValue` (linha 212). Em `app/app.js` (blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`), o contador é escrito em `textContent` nas linhas 2152–2153 e a apresentação de preço/estado é escrita em `innerHTML` nas linhas 1603 e 1607. Esses são seletores e caminhos de escrita estáticos; ainda precisam de observação no DOM carregado pela fixture autenticada, em estados representativos.
