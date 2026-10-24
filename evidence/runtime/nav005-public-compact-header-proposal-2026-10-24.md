# NAV-005 — validação temporária da proposta compacta

Data: 2026-10-24  
Rota: https://casaemmodulos.casa/how-it-works/  
Produto observado: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
Deploy observado: `6adc221479c773577ed45e23` (Netlify Production, READY)

## O que foi observado

A rota pública foi aberta em contexto isolado de navegador. A proposta foi aplicada apenas ao DOM/CSS temporário da sessão, sem alterar arquivos do produto.

No estado publicado, o controle de tema já fica icon-only em 486 px, embora a marca permaneça em 160 px. Em 321 px, a marca chega a 120 px e o rótulo continua oculto. O contato WhatsApp permanece no grupo de ações, fora do menu. Abaixo de 320 px, os estilos atuais mantêm `html`, `body` e a rota com largura mínima de 320 px, causando overflow horizontal.

## Resultado da composição proposta

A simulação moveu o link de contato para a navegação pública em larguras compactas, manteve tema antes do menu e alternou o controle de tema após a marca passar do limite de redução aproximado de 30%.

| Largura emulada | Marca proposta | Tema | Menu e contato |
| ---: | ---: | --- | --- |
| 486 px | 160 px | rótulo visível | quatro itens dentro do menu |
| 360 px | 129,6 px | rótulo visível | quatro itens dentro do menu |
| 321 px | 115,7 px | rótulo visível | quatro itens dentro do menu |
| 310 px | 111,6 px | icon-only | quatro itens dentro do menu |
| 290 px | 145 px | icon-only | botão completo; sem overflow após remover o mínimo rígido de 320 px |
| 275 px | 130,3 px | icon-only | botão completo; sem overflow após remover o mínimo rígido de 320 px |

Na execução em 310 px, a largura do layout ainda reportou 320 px por causa do mínimo rígido existente; por isso essa linha confirma apenas o ponto de troca de tema e redução da marca. A remoção do mínimo foi simulada somente a 290 px e abaixo.

Em uma verificação separada a 901 px, restaurar o link de contato ao grupo de ações manteve os três links públicos no nav horizontal, o CTA nas ações e o hambúrguer oculto. A proposta não mudou o DOM largo servido pelo produto.

O clique do menu na simulação manteve `aria-expanded` e o nome acessível sincronizados. Em tema claro e escuro, o menu exibiu navegação e contato; a composição não criou rolagem horizontal nas larguras estreitas observadas. Capturas foram apenas inspecionadas na sessão e não foram persistidas como evidência visual.

## Limites e governança

Esta é uma validação de viabilidade da composição, não uma homologação visual completa nem uma implementação. Foi observada apenas a rota `/how-it-works/`, em Chrome/Chromium e numa passagem por largura. Não houve validação em Safari/Firefox, leitores de tela ou navegação completa por teclado; também não foram alterados produto, deploy ou issue #218.

O registro canônico NAV-005 ainda marca implementação no produto como não autorizada. A simulação fornece a proposta DOM que faltava para avaliação; a implementação continua pendente da autorização prevista na decisão.