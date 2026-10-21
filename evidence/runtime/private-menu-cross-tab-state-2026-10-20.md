# Estado do menu entre páginas privadas em produção (20/10/2026)

**Produto:** [`EAKerber/MobiliPresenter2D` `main`, commit `1878ae1057ce7c6190e0c8cb08a1f3baadd49463`](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463)  
**Deploy:** [`6ad6c3b51b6be05647167f94`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94), publicado  
**Privacidade:** nenhuma credencial, email, token ou dado de convite foi copiado.

## Observação

No contexto padrão do navegador, as abas já abertas apresentaram estados diferentes:

| Rota | Estado visível do menu |
|---|---|
| `/config/` (aba autenticada existente) | Configurador, Administração, Gerenciar acessos, cinco destinos públicos e **Sair** |
| `/admin.html` (aba existente) | **Entrar na administração** e destinos públicos; **Sair** ausente |
| `/access/manage.html` (aba existente) | **Entrar na administração** e destinos públicos; **Sair** ausente |
| Nova aba `/admin.html` no mesmo contexto padrão | Formulário de login; estado anônimo |

O menu da aba do Configurador abriu e fechou; Escape devolveu o foco ao botão. Os menus das abas administrativas existentes também foram abertos para leitura e fechados com Escape. Não houve login ou logout nesta observação. As abas antigas não foram recarregadas; a nova aba permite comparar um carregamento novo sem interromper o trabalho que poderia estar aberto nas existentes.

A diferença de menu é observada, mas não estabelece por que a aba do Configurador ainda exibe identidade autenticada ou por que os outros documentos exibem estado anônimo. A cronologia da autenticação anterior e a validade atual da sessão não foram inferidas. O issue [#213](https://github.com/EAKerber/MobiliPresenter2D/issues/213) permanece pendente de um teste controlado de login, propagação entre documentos, navegação e saída.

## Sinal de rede

Na lista de requests da aba `/config/`, havia um `POST /.netlify/identity/token` com status 400. O corpo e os cabeçalhos não foram inspecionados, e nenhum token foi lido. Isso é um sinal sem causa atribuída. Na nova aba administrativa, `POST /api/access/session` respondeu 404 sem token, já rastreado separadamente por FIND-014/#222. Nenhum dos dois resultados, isoladamente, explica o estado misto.

## Limites

Nenhuma tela autenticada foi capturada ou salva porque o menu pode incluir o email da conta. Os dados foram reduzidos aos nomes das rotas e à presença/ausência de **Sair**. Nenhuma configuração, convite ou estado do produto foi alterado.
