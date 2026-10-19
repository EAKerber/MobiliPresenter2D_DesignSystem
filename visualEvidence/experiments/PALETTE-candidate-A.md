# Proposta de paleta A — revisão visual

**Estado:** candidata, não homologada. Derivada dos valores mais recorrentes no inventário do produto `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`; não altera o produto.  
**Prancha:** [PALETTE-candidate-A.svg](PALETTE-candidate-A.svg)  
**Registro vigente:** [decisions.json](../../decisions.json). Catálogo observado: [visual-inventory.json](../../visual-inventory.json), campos aggregate.customProperties e uniqueColorLiteralValues.

## Proposta de base

| Papel | Claro | Escuro | Situação |
|---|---|---|---|
| Canvas | #F7F5F2 | #111210 | Valores atuais recorrentes; adoção global proposta |
| Superfície | #FFFFFF | #1B1C1A | Valores atuais recorrentes |
| Superfície suave | #F0EDE8 | #20211F | Valores atuais recorrentes |
| Texto principal | #22211F | #F4F1EB | Valores atuais recorrentes |
| Texto secundário | #675F55 | #C4BCB2 | Claro: par aprovado apenas nos seletores VIS-002. Escuro: uso atual sem homologação global |
| Linha/borda | #DED9D2 | #4A4843 | Valores públicos atuais; confirmar contraste para controles |
| Acento/foco | #6E512E | #D8BC7C | Valores atuais; proposta de unificação; foco precisa de teste não textual |
| Informação de processo | #245D87 | #A7D1F0 | Papel azul aprovado; valores são uso atual do admin e precisam homologação contextual |
| Sucesso | #176344 | #A9DDB6 | Valores atuais do admin; candidatos |
| Erro | #A32323 | #FFAAA0 | Valores atuais do admin; candidatos |
| Aviso técnico | #795000 | #F4CB80 | Valores atuais do admin; candidatos |
| Promoção/campanha | base #A64D13 | variante escura pendente | Base aprovada; não é aviso técnico. Texto branco sobre a base: 5,69:1; harmonização dark requer revisão |

## Contrastes de referência

Contraste calculado por luminância sRGB para pares sólidos. Os números são triagem de candidato, não prova de conformidade do produto.

| Par | Razão | Limite |
|---|---:|---|
| #22211F em #F7F5F2 | 14,78:1 | Candidato de texto principal claro |
| #675F55 em #F0EDE8 | 5,38:1 | Aprovado apenas nos seletores VIS-002 |
| #6E512E em #F7F5F2 | 6,70:1 | Candidato de texto/acento claro; foco requer teste não textual |
| #F4F1EB em #111210 | 16,66:1 | Candidato de texto principal escuro |
| #C4BCB2 em #1B1C1A | 9,11:1 | Candidato de texto secundário escuro |
| #D8BC7C em #111210 | 10,20:1 | Candidato de acento escuro |
| Branco em #A64D13 | 5,69:1 | Referência para este par; não aprova todas as superfícies promocionais |
| Amostras de estado sobre branco/escuro | 7,02:1 a 7,44:1 no tema claro e 10,30:1 a 12,26:1 no escuro | Contraste calculado em amostras; combinações não homologadas |

## Divergências que a proposta pretende resolver

- O produto tem 43 custom properties e 235 valores literais únicos no snapshot estático; isso inclui cores sobrepostas, alpha, sombras, ilustrações e detalhes que não devem virar paleta sem análise.
- A base pública e os temas do configurador/admin repetem tons próximos com papéis e nomes diferentes: public-*, bg, background, surface, raised e surface-raised.
- Valores de texto secundário e acento divergem entre arquivos. No admin, muted inclui #C4BCB2, #6B6259 e #706C66; público usa #706C66/#C4BCB2.
- O admin define valores para quatro estados semânticos, mas combinações reais com fundos e componentes precisam de confirmação no DOM. Não são tokens homologados.
- Cobre e azul têm papéis aprovados distintos; a proposta preserva essa separação.

## Decisões para homologar ou ajustar

1. Aprovar ou ajustar o eixo neutro quente claro/escuro.
2. Aprovar ou ajustar texto secundário, borda e acento/foco como base compartilhada.
3. Rever estados de erro/sucesso/aviso/informação em claro e escuro, com pares e formatos de componente; nenhum estado deve depender apenas da cor.
4. Definir como a promoção em tema escuro usa #A64D13 ou uma variante clara; não inferir preferência apenas pela razão com texto branco.
5. Definir seleção e disabled após revisar seus contextos e os contratos EST-01–06.
6. Após a aprovação visual, registrar pares em decisions.json e só então publicar tokens/aplicar em famílias da UI com verificação runtime.

A proposta A preserva neutros quentes da marca, usa a direção aprovada para promoção e reserva azul para informação de processo. Só os pares contextuais já registrados em VIS-002 e VIS-003 são oficiais.