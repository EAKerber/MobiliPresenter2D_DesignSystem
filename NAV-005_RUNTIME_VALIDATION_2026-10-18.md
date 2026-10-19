# NAV-005 — validação runtime do encaixe estreito

**Data local:** 18/10/2026  
**Página:** [login da Administração](https://casaemmodulos.casa/admin.html), sem sessão  
**Tema medido no DOM:** escuro  
**Método:** leitura somente de geometria DOM no site publicado, em larguras CSS explícitas. O override temporário de viewport foi restaurado ao final. Nenhuma preferência ou dado foi alterado.

## Evidência do comportamento publicado

| Viewport | Altura do header | Composição atual | Logo | Identificador | Ações | Overflow horizontal |
|---:|---:|---|---:|---:|---:|---|
| 288 px | 104,2 px | Duas linhas | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |
| 306 px | 104,2 px | Duas linhas | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |
| 313 px | 104,2 px | Duas linhas | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |
| 320 px | 104,2 px | Duas linhas | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |
| 340 px | 104,2 px | Duas linhas | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |
| 350 px | 62 px | Uma linha | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |
| 360 px | 62 px | Uma linha | 105 px | 75,9 px | 74,1 × 40 + 40 × 40 px | Não |

O header publicado agrupa controles em duas linhas até 340 px nos pontos amostrados; volta a uma linha a partir de 350 px. Não houve overflow horizontal. A logo não encolhe nesses estados e os alvos ficam em 40 px de altura (hambúrguer 40 × 40 px), abaixo dos 44 × 44 px da especificação recomendada.

## Correção da conta recomendada

A especificação anterior subestimou a largura mínima porque omitiu o vão entre a marca e as ações e calculou o piso de uma linha sem considerar o vão do header. Com a evidência e os alvos recomendados de 44 × 44 px:

- Marca no piso: logo 73,5 + vão observado 9 + identificador 75,9 = **158,4 px**.
- Ações com tema rotulado: tema 74,1 + vão recomendado 8 + menu 44 = **126,1 px**. Somando vão do header 8 e margens 28, a composição exige aproximadamente **320,5 px**; arredondar o limite para **321 px**. Portanto, manter o rótulo a partir de 321 px; usar ícone a 320 px e abaixo.
- Ações em modo de ícone: 44 + vão 8 + 44 = 96 px. Com marca no piso, vão do header e margens, a composição exige aproximadamente **290,4 px**; arredondar o mínimo de uma linha para **291 px**. Abaixo desse valor, permitir duas linhas.

A recomendação corrigida é: logo 105–73,5 px (máximo de redução 30%); rótulo do tema até cerca de 321 px de viewport; ícone-only até o piso de uma linha de 291 px; abaixo disso, duas linhas. O menu segue na extremidade e o identificador permanece completo.

## Temas e limites

As folhas CSS carregadas incluem variáveis de cores distintas para claro/escuro, enquanto as regras geométricas compactas do header são compartilhadas. A geometria foi medida somente em tema escuro para não alterar a preferência persistida do usuário. A revisão de CSS confirma as declarações de ambos os temas, mas não equivale a uma captura ou medição DOM renderizada em tema claro.

Esta evidência descreve o produto atual e não demonstra que a recomendação já está implementada. Os valores corrigidos atualizam a especificação do Design System; o produto permanece sem alteração. Ainda é necessária uma nova auditoria runtime depois de uma futura implementação, inclusive em tema claro e com identificadores excepcionalmente longos.
