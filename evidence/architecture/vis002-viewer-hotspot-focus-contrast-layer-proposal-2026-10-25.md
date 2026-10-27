# VIS-002 — proposta de reforço do foco dos hotspots sobre fotografia — 25/10/2026

## Estado

**Aprovada pelo usuário para teste em preview em 25/10/2026; não canônica.** A autorização cobre somente `.scene-hotspot:focus-visible` na PR de produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242), sem merge, Production, `decisions.json`, outros estados ou tokens globais.

O anel autorizado continua em 4 px com offset declarado de 3 px e acento #8B6A40 no tema claro / #D8BC7C no escuro. A opção A acrescentou keylines neutras branca (#FFFFFF) e preta (#000000), com spreads de 3 px e 1 px dentro da extensão externa do outline. Elas não aumentam o limite externo do indicador.

## Evidência que motivou a proposta

A medição aproximada da foto de Cozinha encontrou medianas do anel de:

- Claro: 3,18–3,92:1 no desktop e 3,31–3,94:1 no mobile; alguns pontos ficaram abaixo de 3:1.
- Escuro: 1,24–1,46:1 no desktop e 1,26–1,46:1 no mobile.

A amostra compara pixels da imagem-base com a cor do traçado; não é captura dos pixels compostos nem auditoria WCAG completa. Ela é válida somente para a cena publicada, renderização, viewports e método descritos em [evidência de contraste](../runtime/pr242-viewer-focus-image-contrast-sample-2026-10-25.md).

## Candidatos considerados

| Opção | Tratamento | Resultado |
|---|---|---|
| A — anel dourado com keylines neutras | Preserva o anel dourado aprovado e acrescenta linhas clara e escura dentro de sua extensão externa. | Escolhida para testar em preview. |
| B — anel neutro duplo | Substitui o acento aprovado por bordas clara e escura. | Não testada; muda a cor homologada. |
| C — suporte opaco atrás do hotspot | Adiciona fundo sólido ao alvo durante o foco. | Não testada; altera o alvo e pode cobrir a cena. |

A primeira versão de A, com keylines por fora do anel, foi rejeitada após o hotspot 07 ficar cortado na borda direita do viewport móvel. A implementação final limitou as linhas neutras a 1 px preta e 3 px branca, dentro da extensão externa do outline. Ver [registro do teste em preview](../runtime/pr242-viewer-hotspot-focus-keylines-preview-2026-10-25.md).

## Resultado do preview

No head `2727c85e933f4f17f539a97a263c7845d31efa0b` da PR #242, todos os sete hotspots receberam `:focus-visible` em claro/escuro nas viewports 390 × 844 e 1280 × 800. A menor folga observada entre o indicador e o limite da cena foi 0,11 CSS px no mobile e 6,29 CSS px no desktop; não houve overflow horizontal. Os checks associados ao commit terminaram com sucesso.

O ensaio cobre somente a cena Cozinha. A inspeção de posicionamento não mede contraste pixel a pixel da composição final das keylines com a foto e não prova conformidade WCAG. A PR continua DRAFT para revisão visual; não houve merge nem deploy de Production.

## Limite da decisão

O usuário autorizou **A — testar keylines no preview**. Isto não torna as keylines canônicas nem autoriza integração ou Production. Cores globais, tokens, `decisions.json`, hover, seleção e cenas não foram alterados.
