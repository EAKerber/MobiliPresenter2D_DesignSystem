# Pacote de revisão visual — NAV-005 e VIS-002

**Status:** candidatos experimentais para revisão; nenhuma nova decisão foi homologada nesta etapa.  
**Base de evidência:** produção em 2026-10-18, deploy Netlify `6ad518d3da1379029e04324f`, commit `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`.  
**Registro canônico:** `decisions.json`. Este pacote não altera decisões ou tokens.

## 1. Cabeçalho público — NAV-005

![Alternativas experimentais para o cabeçalho público](NAV-005-public-header-options.svg)

- **A — navegação exposta:** destinos visíveis em desktop; menu hambúrguer nos viewports estreitos.
- **B — navegação compacta:** controles no cabeçalho e destinos dentro do menu em todos os viewports.

As duas opções preservam o contrato de interação NAV-004. A quarta entrada é mostrada como **Fale conosco**; o cabeçalho publicado direciona essa ação ao WhatsApp. Ainda precisa ser confirmado se isso cumpre a página/destino **Contato** do contrato NAV-004 ou se existe uma rota própria. A amostra de logo é uma aproximação tipográfica/desenhada para comparar composição; não substitui o asset oficial. Cor, altura, tipografia, espaçamentos, ícones e tratamento do CTA são ilustrativos e não foram aprovados. A confirmação que falta é principalmente de composição: links expostos ou menu compacto.

A referência publicada atual está em [landing-dark.jpg](../../public/landing/landing-dark.jpg). Ela mostra o cabeçalho atual; não é uma opção futura aprovada.

## 2. Pares de contraste — VIS-002

![Candidatos experimentais de contraste para dois achados do runtime](VIS-002-contrast-options.svg)

A triagem runtime encontrou texto corrido em `#706C66` sobre `#F0EDE8` (4,47:1) e rótulo pequeno `#8B6A40` sobre `#E8E3DC` (3,89:1). Os candidatos mais escuros atendem ao alvo matemático de 4,5:1 para texto comum nos pares sólidos exibidos. Os valores foram calculados para comparação; precisam ser conferidos nos componentes/temas reais antes de adoção.

- **Texto corrido:** A `#6D675F` (4,79:1) mantém tom mais próximo do atual; B `#675F55` (5,38:1) oferece maior margem.
- **Rótulo quente:** A `#765832` (5,12:1) mantém proximidade com a família terrosa; B `#70522F` (5,60:1) oferece maior margem.

Isso não transforma os candidatos em tokens. O azul homologado para informação de processo e a base promocional `#A64D13` permanecem conforme VIS-002; variantes de cobre por tema/superfície seguem pendentes.

## Revisão solicitada

1. Cabeçalho público: A, B, ou comentários sobre outra composição.
2. Destino público Contato: confirmar se Fale conosco via WhatsApp satisfaz NAV-004 ou se o contrato exige uma rota pública própria.
3. Texto corrido: A ou B; se não houver preferência visual, escolha posterior pode priorizar a menor alteração que alcance contraste suficiente.
4. Rótulo: A ou B; a escolha ainda deve ser validada no componente e tema de origem.

Até essa revisão, `NAV-005` permanece aberto e os quatro hexadecimais candidatos continuam fora de `decisions.json`.
