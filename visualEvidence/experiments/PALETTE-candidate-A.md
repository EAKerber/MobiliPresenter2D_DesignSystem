# Paleta A — valores aprovados e aplicação pendente

**Estado:** valores da paleta aprovados pelo usuário; aplicação no produto e validação por componente pendentes. O secundário anterior pareceu esverdeado; o foco estava difícil de ler; evitar branco e preto puros.  
**Prancha aprovada como referência visual:** [PALETTE-candidate-A-v2.svg](PALETTE-candidate-A-v2.svg).  
**Produto observado:** inventário estático do snapshot 298c11441f82cacfff2f809fd9e5ad6f1fc33c0a.

## Eixo neutro proposto

| Papel | Claro | Escuro | Estado |
|---|---|---|---|
| Canvas | #E8E3DC | #171614 | Aprovado como valor de paleta; sem branco/preto puros |
| Superfície | #F0EDE8 | #211F1C | Marfim quente opaco no claro; carvão quente no escuro. Substitui #FFFFFF como valor aprovado para a superfície de interface. |
| Superfície suave | #DED9D2 | #2C2924 | Aprovado como valor de paleta |
| Texto principal | #292723 | #F0EAE1 | Candidato, tons carvão/marfim quente |
| Texto secundário | #705C4B | #C7BBAA | Marrom quente aprovado como valor de paleta; token técnico ainda não criado |
| Borda | #D6CCC0 | #4E4942 | Aprovado como valor de paleta; aplicação em controles/separadores ainda requer validação |

A superfície clara usa #F0EDE8 em vez de branco puro. A proposta substitui valores de superfície #FFFFFF/#FFF na futura padronização visual; não altera brancos necessários dentro de fotografias, logos ou ilustrações.

## Foco proposto

- Tema claro: contorno ocre de marca #8B6A40 contra superfície #F0EDE8; contraste calculado 4,25:1.
- Tema escuro: contorno dourado #D8BC7C contra superfície #211F1C; contraste calculado 8,93:1.
- O usuário aprovou a referência visual com contorno de 4 px e afastamento de 3 px. Aplicação e inspeção do foco de teclado em componentes reais continuam pendentes.
- O foco deve continuar independente da seleção e não depender só de mudança de cor; revisar indicador de teclado em componentes reais.

## Contrastes de texto de referência

Razões calculadas para cores sólidas e não arredondadas para alcançar limites. Não equivalem a teste do DOM.

| Par candidato | Razão |
|---|---:|
| Texto principal claro #292723 em #E8E3DC | 11,68:1 |
| Secundário claro #705C4B em #F0EDE8 | 5,41:1 |
| Texto principal escuro #F0EAE1 em #171614 | 15,12:1 |
| Secundário escuro #C7BBAA em #211F1C | 8,70:1 |

## Mantidos como papéis separados

- Informação de processo usa azul; promoção de produto/campanha usa cobre com base homologada #A64D13.
- A base promocional não vira aviso técnico; variações por tema e superfície continuam pendentes.
- Cores de erro, sucesso e aviso permanecem candidatas até a revisão de amostras e pares em light/dark.

## Limites

Os valores de papel da paleta e o tratamento de foco mostrados nesta prancha foram aprovados e registrados em VIS-002. Isso não cria tokens nem autoriza implementação no produto. Estados semânticos, seleção/desabilitado e variante promocional escura continuam pendentes.

Para os três seletores anteriormente associados a #675F55, o par aprovado de paleta #705C4B em #F0EDE8 calcula 5,41:1; a aplicação ainda exige validação no DOM.
