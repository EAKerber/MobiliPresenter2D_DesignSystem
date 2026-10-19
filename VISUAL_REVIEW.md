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

### NAV-005 — composição compacta aprovada

![Opção A escolhida e opção B mantida como comparação para cabeçalhos compactos](visualEvidence/experiments/NAV-005-compact-header-options.svg)

Na página pública publicada `/how-it-works/`, observei em 18/10/2026 um cabeçalho de uma linha em viewport de 515 × 608 px, tema escuro: marca de 160 px à esquerda e grupo de ações de 140 px à direita, com contato, controle de tema em ícone e menu. O cabeçalho mediu aproximadamente 78 px de altura. É uma observação de um único estado público; a escolha estrutural compacta foi registrada separadamente e não pode ser inferida dessa captura.

O usuário escolheu **opção A** para a composição compacta: uma linha; marca e identificador/contexto juntos à esquerda; controle de tema imediatamente antes do hambúrguer, que permanece na extremidade direita. Nas páginas públicas, navegação e acesso de contato ficam agrupados no menu. A opção B permanece na prancha apenas como comparação não selecionada. A estrutura aprovada é composicional; breakpoint, tipografia, dimensões, ícones/estilo dos controles e comportamento de nomes longos continuam pendentes. Admin autenticado e navegação contextual não foram capturados nessa viewport, portanto a prancha é referência esquemática, não evidência runtime dessas rotas.

A escolha A mantém o link atual **Fale conosco** via WhatsApp como acesso público de contato. Isso não cria uma rota própria para Contato.

A prancha anterior de opções permanece em [NAV-005-public-header-options.svg](visualEvidence/experiments/NAV-005-public-header-options.svg) como comparação experimental. A prancha acima registra a escolha estrutural A e mantém B como comparação; não especifica tokens, dimensões nem o logo final.

### Ponto de revisão compacto identificado em runtime

No login administrativo publicado, a estrutura atual usa uma linha em 350 px e duas linhas em 340 px. A seleção da opção A aprovou a composição de uma linha, mas ainda não definiu como acomodar o conjunto quando a largura disponível diminui. A faixa observada delimita a investigação; não é um breakpoint homologado. Medições e limites estão em [RUNTIME_AUDIT.md](RUNTIME_AUDIT.md) e [runtime-evidence.json](runtime-evidence.json). A prancha [NAV-005-narrow-theme-control-options.svg](visualEvidence/experiments/NAV-005-narrow-theme-control-options.svg) compara duas candidatas para 320 px: tema somente por ícone mantendo a marca, ou tema com rótulo e marca reduzida. Ambas preservam o contexto completo e a linha única; as medidas são estimativas, sem homologação.

## VIS-002 — pares exatos aprovados

![Pares de contraste B selecionados](visualEvidence/experiments/VIS-002-contrast-options.svg)

O usuário escolheu a opção B nos dois exemplos. `decisions.json` registra estes pares específicos:

- Texto corrido claro: `#675F55` em `#F0EDE8`, 5,38:1, nos contextos auditados da landing, Como funciona e Quem somos.
- Rótulo quente claro: `#70522F` em `#E8E3DC`, 5,60:1, no rótulo auditado de Como funciona.

A aprovação é contextual: não cria tokens globais, não aprova variações dark nem autoriza extensão automática a outros componentes/superfícies. Os pares já atingem o alvo matemático de 4,5:1 para texto comum nas superfícies sólidas avaliadas; a aplicação deve ser revalidada no DOM antes de qualquer implementação do produto. A base promocional `#A64D13` e o azul de informação de processo mantêm seus papéis previamente homologados.

## Ainda aberto

- Definir o comportamento em larguras muito estreitas: no login administrativo, o header atual quebra entre 340 e 350 px, enquanto a composição A aprovada é de uma linha. Decidir se haverá redução de marca/identificador, truncamento contextual ou um fallback mais estreito; não inferir uma solução a partir da captura atual.
- Homologar dimensões, tipografia, cores, assets e estilo dos controles dos cabeçalhos.
- Medir outros pares e estados; os dois aprovados não se generalizam.


## FIND-004 — tratamento visual escolhido; valores pendentes

![Prancha esquemática com o estado atual e duas alternativas para a legenda](visualEvidence/experiments/FIND-004-caption-contrast-options.svg)

A auditoria runtime mediu 1,78:1 para `.study-art figcaption` clara sobre a superfície clara da ilustração no tema escuro. Após revisar o caso real publicado em `/how-it-works/`, o usuário escolheu **B — faixa escura na base da ilustração**. A legenda permanece integrada à figura sobre um fundo de contraste controlado.

A aprovação cobre somente essa relação de composição. As cores e a opacidade/gradiente da faixa na prancha são amostras experimentais: continuam pendentes de medição e homologação. Também não ficam definidos dimensões, espaçamento, comportamento responsivo, extensão para outros temas/componentes nem implementação no produto. A prancha esquemática não substitui uma implementação fiel nem a auditoria do DOM final.
