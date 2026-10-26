# PR #241 — auditoria de falha das imagens públicas (2026-10-26)

## Escopo observado

- Produto: `EAKerber/MobiliPresenter2D`, branch `a11y/vis002-measured-copy-contrast-20261024`, head `45e532b444967bdd901ac2f49fc8d0548daa881a`.
- Deploy Preview: [PR #241 — Como funciona](https://deploy-preview-241--mobilipresenter2d.netlify.app/how-it-works/).
- Contexto isolado de navegador, viewport mobile 390 × 844 CSS px, tema claro.
- Auditoria limitada às imagens desta rota; não é certificação geral de acessibilidade nem leitura por tecnologia assistiva.

## Método e reversibilidade

A auditoria em lote selecionou 16 imagens com texto alternativo não vazio, excluindo logos e a ilustração `estudo-espaco.webp`, que já tem o fallback dedicado. Cada `src` foi substituído temporariamente por uma URL same-origin única e inexistente. Os 16 requests terminaram em HTTP 404 no painel de rede. Todos os `src` originais foram restaurados; a leitura final encontrou as imagens carregadas (`complete=true`, largura natural positiva).

Depois, confirmei em quatro contextos uma ocorrência de erro real e o estado antes/durante/depois:

| Contexto | Caixa da imagem antes e durante a falha | Caixa do container | Resultado |
| --- | ---: | ---: | --- |
| Comparação de planejados | 352,67 × 104 px | 354 × 445,38 px | Sem placeholder; `alt` mantido |
| Cartão de módulo aéreo | 170,67 × 190 px | 172 × 229,33 px | Sem placeholder; `alt` mantido |
| Ícone do cartão de economia | 88 × 90 px | 354 × 115 px | Sem placeholder; `alt` mantido |
| Hero de encerramento | 390 × 520 px | 390 × 520 px | Sem placeholder; `alt` mantido |

A abertura da página também já havia recebido 404 real nesta sessão; o frame permaneceu 390 × 320 px e não exibiu fallback. Em cada prova, o asset original voltou a carregar e as dimensões permaneceram estáveis.

## Achado no código da head observada

A origem `architecture/pages/how-it-works.page.html` contém o wrapper `data-image-fallback` somente em torno da ilustração do estudo do espaço. Em `app/how-it-works/how-it-works.js`, o handler percorre esses wrappers e exige `.study-space-illustration`. Portanto, o placeholder não é um componente de uso geral: as outras imagens da página não entram nesse fluxo.

## Próximo passo recomendado

Para cumprir o pedido de um placeholder padrão escalável com descrição sobreposta, extrair o tratamento para uma rotina compartilhada, preservar a proporção/caixa de cada mídia e usar a descrição `alt` apenas para imagens informativas. Imagens com `alt=""` devem continuar decorativas para leitores de tela. Aplicar essa expansão no preview e medir os diferentes formatos antes de ampliar a alegação de cobertura.

Nenhum arquivo do produto, asset, estado de produção ou dado remoto foi alterado nesta auditoria.
