# DS-05A — diagnóstico de geometria da navegação autenticada

Data: 2026-10-25  
Produto: [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D)  
Issue: [#232](https://github.com/EAKerber/MobiliPresenter2D/issues/232)  
PR de CI: [#238](https://github.com/EAKerber/MobiliPresenter2D/pull/238), DRAFT  
Head observado: `fd61a37a11dd63b3e537d3d76a2303bfdfc4f06a`  
Ação: [Actions #40201992400](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40201992400) (tentativa 2)

## Resultado de execução

O preflight confirmou as variáveis necessárias sem ler seus valores, a fixture V5 e o ambiente de staging. A segunda tentativa passou por resgate de grant, papel restrito, bootstrap V5, negação de Admin e revogação. O navegador marcou a configuração como `validated`, manteve o workspace visível e não registrou erros de página, rede ou HTTP.

Três das cinco suítes autenticadas passaram: Mobile/PiP, Summary/Pricing e Stone. Keyboard e Flow continuam falhando em timeout durante a navegação de etapas; a issue #232 não está homologada.

## Diagnóstico de layout

No snapshot anterior à sonda, os quatro botões existentes estavam conectados ao DOM e computavam `display: block` e `min-height: 44px`, mas tinham `getClientRects().length = 0` e caixa 0×0.

Na captura sanitizada posterior:

- Um clone fiel do botão existente, com mesma classe, atributos e filhos, recebeu caixa de 44 px dentro da mesma navegação.
- Remover e recolocar o nó existente no mesmo lugar também fez esse mesmo nó receber caixa de 44 px.
- Um botão temporário novo no mesmo `nav` também recebeu caixa de 44 px.
- As folhas `/styles.css` e `/ui-theme.css` estavam habilitadas e continham regra `.flow-step`.

A evidência aponta para um estado de layout que se recupera quando o nó é reinserido. Ela não identifica ainda qual alteração do runtime invalida o layout, nem confirma um patch de produto. A sonda executa apenas após uma falha, atua temporariamente no DOM da página de teste e a página é descartada.

## Limites e próximo passo

O primeiro attempt do mesmo run teve falha genérica transitória durante o resgate do grant; a tentativa 2 passou essa etapa. Não há falta de variável confirmada.

A PR #238 tem guarda de escopo para testes/CI e não contém alteração em `app/` ou `netlify/`. A correção de runtime deve ser feita em PR separada, com preview e as cinco suítes autenticadas reexecutadas. Não foram alteradas decisões canônicas do Design System, produção ou valores de credenciais. PRs #238 e #51 continuam DRAFT; sem merge ou deploy de Production.
