# ARC-13 — rastreio de `renderSummary`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumers e condições

- **Itens por módulo:** referências, títulos e valores vêm da estimativa/catálogo. Só há complementos de acabamento, puxador rateado ou pedra local quando o respectivo centavo é positivo; os prefixos e a moeda formam copy estruturada com parâmetros, não strings isoladas.
- **Estado vazio:** `Nenhum módulo incluído.` é exibido quando a estimativa não tem itens de módulo.
- **Nota comercial:** informa que cores podem ser globais/locais e que pedra/serviços entram uma vez no conjunto, enquanto a ficha mostra o valor local do módulo. Preservar esse limite contábil.
- **Resumo de valores pronto:** a estimativa fornece label, total, disclaimer e itens globais dinâmicos. Linhas condicionais mostram módulos e contagem, acabamento global, puxador global rateado, pedra de cooktop e impactos globais. Labels e valores são formatados por helpers/estimativa; não substituir por valores fixos.
- **Regras por linha:** acabamento global usa o acabamento selecionado e aplica aos módulos elegíveis; puxador global usa label do catálogo e rateio nas frentes incluídas; impacto global é aplicado uma vez.
- **Preço de cooktop:** `Pedra cooktop` e `Inclusa no Módulo 02.` são textos fixos sob condição de `localCents`. A associação do número de módulo à regra é uma afirmação de domínio hard-coded e deve ser conferida com o owner da tabela de pricing antes de migrar ou generalizar.
- **Estimativa incompleta:** o renderer usa markup estático para `Valor do conjunto` e `Em configuração`; o mapa os agrupou em um literal de HTML, não em uma única frase. Não mostra total estimado nesse estado.
- **Contagem:** `incluído(s).` combina contagem calculada e forma de pluralização provisória; o contrato de plural continua adiado até a etapa de localização.

## Limites e revisão futura

O bucket contém orientação comercial longa, a qual deve manter contraste próximo de preto no tema claro e de branco no escuro conforme preferência do usuário; este rastreio não mede contraste. Dependência de “Módulo 02” e a contagem singular/plural precisam de revisão do owner/contrato antes de uma proposta de chaves.

Rastreio manual de fonte e helpers, sem runtime/AST. Nenhuma chave foi proposta; produto, índice, catálogo e `decisions.json` não foram alterados.
