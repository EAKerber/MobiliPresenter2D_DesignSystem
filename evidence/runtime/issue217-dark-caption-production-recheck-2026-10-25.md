# Rechecagem de produção — contraste da legenda em Como funciona (#217)

**Data:** 2026-10-25  
**Rota:** https://casaemmodulos.casa/how-it-works/  
**Estado:** verificação read-only; sem alteração no produto, decisões ou publicação.

## Evidência de aprovação e integração

A issue [#217](https://github.com/EAKerber/MobiliPresenter2D/issues/217) recebeu comentário registrando aprovação da alternativa A para `.study-art figcaption` no tema escuro: faixa opaca `#20211F` e texto `#F0EDE8`, com contraste calculado de 13,85:1. A [PR #219](https://github.com/EAKerber/MobiliPresenter2D/pull/219) que aplicou a decisão foi mergeada em 2026-10-19.

A fonte atual em `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, `app/how-it-works/how-it-works.css`, contém a regra contextual:

```css
html[data-theme="dark"] .study-art figcaption {
  background: #20211F;
  color: #F0EDE8;
}
```

## Readback de runtime

No contexto anônimo da Production, com tema `dark` e viewport CSS de 1279 × 663 px:

- A imagem `assets/estudo-espaco.webp` terminou de carregar (1100 × 733 px).
- A imagem ocupou 625,26 × 416,65 px.
- A legenda renderizou com texto `rgb(240, 237, 232)` (`#F0EDE8`) sobre fundo `rgb(32, 33, 31)` (`#20211F`).
- A faixa da legenda começou exatamente no fim da caixa da imagem; não houve sobreposição sobre os pixels claros da ilustração.
- A razão calculada a partir dessas cores é **13,8472:1**, arredondada para **13,85:1**.

## Conclusão e limite

A condição descrita na issue foi corrigida por #219 e a aparência atual foi confirmada no runtime publicado. #217 pode ser encerrada como resolvida. A evidência cobre apenas essa legenda, rota e tema; não certifica contraste de outras imagens, legendas ou estados do produto.

`decisions.json`, o índice ARC-13 e o runtime permaneceram inalterados nesta rechecagem.
