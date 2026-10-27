# ARC-13 — rastreio de `updateSelection`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Marcação de `viewerHint` conferida em `app/config/index.html`, blob `97c284c9831de05607ede0d024e4d919a898b7fa`.

## Estados e consumers

- **Sem ficha:** `Selecione um módulo na cena para abrir sua ficha.` aparece quando a entidade selecionada não tem produto de catálogo correspondente.
- **Ficha selecionada:** `Ficha selecionada: ${product.title}` substitui o hint quando há produto. O título é parâmetro editorial do catálogo.
- **Fechar detalhes:** `Fechar detalhes do módulo` nomeia apenas o botão de ícone no cabeçalho.
- **Preço pronto:** exibe o rótulo `Valor atual na simulação` e, dependendo de `product.category`, um aviso local de painel estrutural ou de módulo. Ambos explicam que pedra e serviços aparecem uma única vez no resumo; o valor formatado vem do cálculo.
- **Preço incompleto:** mostra `Em configuração` e `O valor aparece quando a tabela de trabalho estiver completa.`; esse estado vem do status da estimativa, não de um valor zero.
- **Observação de configuração:** `product.configurationNote` é concatenada às dimensões somente quando existe; é texto editorial/configurado, não copy estática.
- **Conteúdo técnico:** `Medidas nominais`, `Destaques` e `Componentes inclusos` são títulos fixos; medidas, benefícios e componentes vêm do produto.
- **Dependência estrutural:** quando a resolução marca `requirement-hidden`, aparece `Indisponível enquanto o módulo estrutural necessário estiver fora da composição.`; em outros casos pode aparecer o primeiro requisito do produto, que é conteúdo dinâmico.

## Ponto de acessibilidade e limites

No HTML, `#viewerHint` é um `<p>` sem `aria-live` ou papel de status. O texto muda quando a ficha muda, mas esta leitura de código não comprova anúncio por leitor de tela. Manter como verificação de acessibilidade/runtime separada; nenhuma alteração foi feita.

A descrição de preço e a mensagem de dependência são texto corrido: ao validar contraste visual, aplicar a preferência do usuário por tons próximos de preto no claro e de branco no escuro. Este rastreio não mediu contraste.

Rastreio manual do renderer e do HTML, sem teste de runtime/AT. Nenhuma chave foi proposta; código, índice, catálogo e `decisions.json` permanecem inalterados.
