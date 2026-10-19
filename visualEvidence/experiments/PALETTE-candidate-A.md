# Proposta de paleta A — revisão visual (ajustada)

**Estado:** candidata, não homologada. Esta revisão incorpora o retorno do usuário: o secundário anterior pareceu esverdeado; o foco estava difícil de ler; evitar branco e preto puros.  
**Prancha:** [PALETTE-candidate-A.svg](PALETTE-candidate-A.svg).  
**Produto observado:** inventário estático do snapshot 298c11441f82cacfff2f809fd9e5ad6f1fc33c0a.

## Eixo neutro proposto

| Papel | Claro | Escuro | Estado |
|---|---|---|---|
| Canvas | #F3EFE9 | #171614 | Candidato quente, sem branco/preto puros |
| Superfície | #F8F5F0 | #211F1C | Candidato |
| Superfície suave | #EBE5DD | #2C2924 | Candidato |
| Texto principal | #292723 | #F0EAE1 | Candidato, tons carvão/marfim quente |
| Texto secundário | #705C4B | #C7BBAA | Candidato marrom quente; não é token |
| Borda | #D6CCC0 | #4E4942 | Candidato, validar como controle e separador |

## Foco proposto

- Tema claro: contorno cobre #A64D13 contra superfície #F8F5F0; contraste calculado 5,23:1.
- Tema escuro: contorno dourado #D8BC7C contra superfície #211F1C; contraste calculado 8,93:1.
- Exemplo usa contorno de 4 px e afastamento de 3 px. Esses valores são somente uma visualização para tornar o foco fácil de localizar; a espessura e o offset ainda não estão homologados.
- O foco deve continuar independente da seleção e não depender só de mudança de cor; revisar indicador de teclado em componentes reais.

## Contrastes de texto de referência

Razões calculadas para cores sólidas e não arredondadas para alcançar limites. Não equivalem a teste do DOM.

| Par candidato | Razão |
|---|---:|
| Texto principal claro #292723 em #F3EFE9 | 13,01:1 |
| Secundário claro #705C4B em #F3EFE9 | 5,52:1 |
| Secundário claro #705C4B em #EBE5DD | 5,05:1 |
| Texto principal escuro #F0EAE1 em #171614 | 15,12:1 |
| Secundário escuro #C7BBAA em #211F1C | 8,70:1 |

## Mantidos como papéis separados

- Informação de processo usa azul; promoção de produto/campanha usa cobre com base homologada #A64D13.
- A base promocional não vira aviso técnico; variações por tema e superfície continuam pendentes.
- Cores de erro, sucesso e aviso permanecem candidatas até a revisão de amostras e pares em light/dark.

## Limites

Somente pares contextuais que já constam em VIS-002 e o par específico VIS-003/FIND-004 estão homologados. Os valores desta prancha não mudam a fonte canônica nem o produto. Antes de aprovar a paleta completa, revisar a aparência dos secundários, a leitura do foco nos dois temas, estados semânticos, seleção/desabilitado e a variante promocional escura.