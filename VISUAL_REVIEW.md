# Registro da revisão visual — NAV-005 e VIS-002

**Status:** seleções do usuário registradas em `decisions.json`. A aprovação cobre apenas os contextos e o escopo descritos.  
**Base da auditoria runtime:** produção em 2026-10-18, deploy Netlify `6ad518d3da1379029e04324f`, commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`.  
**Este pacote não implementa código do produto.**

## NAV-005 — padrões largos de cabeçalho aprovados

![Estruturas largas aprovadas para páginas públicas, privadas e de segunda ordem](visualEvidence/approved/NAV-005-wide-header-patterns.svg)

- **Páginas públicas:** opção A, navegação exposta como no padrão já usado.
- **Páginas privadas:** opção B, identificador da página/área junto da marca; tema e menu no lado direito.
- **Navegação de segunda ordem:** composição contextual semelhante ao viewer. O controle de tema passa para dentro do cabeçalho e fica antes do menu; se houver hambúrguer, ele ocupa a extremidade direita.

Esta aprovação é para a versão expandida/larga. Breakpoints, composição compacta e medidas não foram definidos. O menu público continua sujeito ao contrato de teclado, Escape, clique fora, aria-expanded, foco e movimento reduzido de NAV-004.

### Experimento de cabeçalhos compactos

![Duas composições experimentais de cabeçalhos compactos](visualEvidence/experiments/NAV-005-compact-header-options.svg)

Na página pública publicada `/how-it-works/`, observei em 18/10/2026 um cabeçalho de uma linha em viewport de 515 × 608 px, tema escuro: marca de 160 px à esquerda e grupo de ações de 140 px à direita, com contato, controle de tema em ícone e menu. O cabeçalho mediu aproximadamente 78 px de altura. É uma observação de um único estado público e não define o layout compacto homologado.

A prancha compara duas estruturas candidatas em largura ilustrativa de 390 px: **A**, uma linha com identificador contextual ao lado da marca, tema antes do menu e contato agrupado no menu público; **B**, marca, tema e menu na primeira linha, com contato público ou identificador contextual numa segunda linha. As estruturas de admin autenticado e navegação contextual são propostas, pois não foram capturadas nesta viewport. Nenhuma opção está aprovada; breakpoint, tipografia, dimensões, ícones, comportamento dos nomes longos e posição do contato permanecem para revisão.

A escolha A mantém o link atual **Fale conosco** via WhatsApp como acesso público de contato. Isso não cria uma rota própria para Contato.

A prancha anterior de opções permanece em [NAV-005-public-header-options.svg](visualEvidence/experiments/NAV-005-public-header-options.svg) como comparação experimental. A prancha simplificada acima ilustra a decisão aprovada, mas não especifica tokens, dimensões nem o logo final.

## VIS-002 — pares exatos aprovados

![Pares de contraste B selecionados](visualEvidence/experiments/VIS-002-contrast-options.svg)

O usuário escolheu a opção B nos dois exemplos. `decisions.json` registra estes pares específicos:

- Texto corrido claro: `#675F55` em `#F0EDE8`, 5,38:1, nos contextos auditados da landing, Como funciona e Quem somos.
- Rótulo quente claro: `#70522F` em `#E8E3DC`, 5,60:1, no rótulo auditado de Como funciona.

A aprovação é contextual: não cria tokens globais, não aprova variações dark nem autoriza extensão automática a outros componentes/superfícies. Os pares já atingem o alvo matemático de 4,5:1 para texto comum nas superfícies sólidas avaliadas; a aplicação deve ser revalidada no DOM antes de qualquer implementação do produto. A base promocional `#A64D13` e o azul de informação de processo mantêm seus papéis previamente homologados.

## Ainda aberto

- Definir breakpoints e comportamento visual compacto/responsivo dos cabeçalhos.
- Homologar dimensões, tipografia, cores, assets e estilo final dos cabeçalhos.
- Medir outros pares e estados; os dois aprovados não se generalizam.


## FIND-004 — tratamento visual escolhido; valores pendentes

![Prancha esquemática com o estado atual e duas alternativas para a legenda](visualEvidence/experiments/FIND-004-caption-contrast-options.svg)

A auditoria runtime mediu 1,78:1 para `.study-art figcaption` clara sobre a superfície clara da ilustração no tema escuro. Após revisar o caso real publicado em `/how-it-works/`, o usuário escolheu **B — faixa escura na base da ilustração**. A legenda permanece integrada à figura sobre um fundo de contraste controlado.

A aprovação cobre somente essa relação de composição. As cores e a opacidade/gradiente da faixa na prancha são amostras experimentais: continuam pendentes de medição e homologação. Também não ficam definidos dimensões, espaçamento, comportamento responsivo, extensão para outros temas/componentes nem implementação no produto. A prancha esquemática não substitui uma implementação fiel nem a auditoria do DOM final.
