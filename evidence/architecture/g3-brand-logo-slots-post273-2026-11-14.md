# G3 — hero e slots de marca após a PR #273 — 2026-11-14

## Fonte e base

- Produto: `EAKerber/MobiliPresenter2D main@46a52e76a0eeae4bed4b567b12da5311ed90b475`.
- PR de origem: [#273](https://github.com/EAKerber/MobiliPresenter2D/pull/273), head visualmente revisado `6799d3177bf931f087f2bf451a6d6dbf5b4d5f6f`, squash integrado em `46a52e76).
- Preview revisado e registrado pela PR: [Deploy Preview #273](https://deploy-preview-273--mobilipresenter2d.netlify.app/).
- Escopo de implementação identificado na PR: `app/index.html`, `app/landing/landing.css`, `app/landing/landing.js`, os arquivos da página Como funciona e os artefatos canônicos correspondentes.

## Propriedade dos slots

1. **Arte do ambiente e do aparelho:** imagem estática que ancora o hero.
2. **Vídeo e controles:** superfície na tela do aparelho; começa com poster e ativa o player após a escolha de reproduzir. O controle de tela cheia fica sobreposto ao vídeo.
3. **Logo/cabeçalho:** pertence ao shell da página. A arte do hero não fornece um logo/header fictício.

A composição completa do hero mantém sua proporção e aparece menor: 12% no desktop, 16% em telas intermediárias e 20% em celular, conforme o resumo de implementação/revisão da PR. A página Como funciona mantém o vídeo incorporado; as imagens comparativas usam molduras normalizadas para centralizar e dimensionar os conteúdos.

O poster usa a miniatura padrão do YouTube. O player de Shorts não permite escolher o primeiro quadro decodificado como poster; portanto, a imagem exibida antes da reprodução pode não ser esse quadro.

## Evidência registrada e limites

A descrição da PR registra compilação canônica sincronizada, 11/11 checks no head indicado, revisão visual do Deploy Preview em desktop e celular e ausência de rolagem horizontal. Esse é o alcance da evidência visual reaproveitada aqui; este recibo não afirma nova inspeção direta do site nem reexecução dos checks.

A revisão substitui somente o diagnóstico estático de 13/11 de que o lettering incorreto do hero ainda precisava ser corrigido. Ela não transforma o hero em componente de logo compartilhado e não aprova extração de CSS.

A baseline CSSOM de CTAs públicos de 14/11 é um recibo local distinto, em árvore anterior à #273. Ela continua útil para seu escopo histórico, mas não demonstra o estado pós-#273 do hero/CTA. Não houve CSSOM pós-merge, screenshot arquivado por esta atualização, leitor de tela ou teste em dispositivo físico/Safari.

## Follow-up de semântica — PR #275 Draft

A análise pós-#273 identificou `aria-label` aplicado ao contêiner genérico dos links secundários do hero. A PR [#275](https://github.com/EAKerber/MobiliPresenter2D/pull/275) propõe `role="group"`, com fonte canônica, HTML gerado e manifest sincronizados. A WAI-ARIA 1.2 define `generic` como um contêiner sem nome e não permite nomeá-lo por `aria-label`; um `group` nomeado é apropriado aos dois links relacionados. A proposta ainda não foi integrada e não tem validação com leitor de tela; G3 permanece parcial.

**Resultado:** propriedade atual do hero reconciliada para G3; G3 permanece parcial. Nenhuma mudança de runtime, design token ou CSS compartilhado é autorizada por este recibo.


## Acompanhamento visual — PR #275, 15/11/2026

A PR [#275](https://github.com/EAKerber/MobiliPresenter2D/pull/275) foi ampliada para remover as faixas de margem na arte do hero. A nova composição expande o ambiente, reduz o celular dentro da moldura e deixa o display limpo para o player real; o alinhamento do overlay foi atualizado. O head atual é `63782416578015b77e531f45d1dcf6a1b5f5a214`; o Deploy Preview está READY em [abrir preview](https://6af92098c6143a04fda931c0--mobilipresenter2d.netlify.app/). A PR continua Draft, sem integração ou publicação. A revisão visual no navegador permanece pendente; não foram executados testes nem leitor de tela.
