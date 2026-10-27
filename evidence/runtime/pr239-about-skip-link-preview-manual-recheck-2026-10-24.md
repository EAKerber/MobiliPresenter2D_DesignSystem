# PR #239 — rechecagem manual do skip link de About

Data: 2026-10-24  
Preview: https://deploy-preview-239--mobilipresenter2d.netlify.app/about/  
Head: `e7b02c04308e9fcc7b52f1d09534058a2a0bbc65`  
Escopo: teclado e foco no Deploy Preview; nenhuma alteração no produto.

## Readback

A sequência real de teclado confirmou o contrato esperado:

1. Tab focou primeiro o link “Pular para o conteúdo”, com `:focus-visible`.
2. Enter navegou para `/about/#main`.
3. O foco terminou em `main#main`, com `tabindex="-1"`; o landmark não foi adicionado à sequência regular de Tab.

A leitura ocorreu em largura de janela de 1280 px; o documento não excedeu a largura de layout. Não foram lidos ou enviados dados de conta.

## Limite

A observação confirma transferência de foco por teclado no preview de About, não a aparência em todos os temas/tamanhos nem a homologação visual global. A PR [#239](https://github.com/EAKerber/MobiliPresenter2D/pull/239) permanece DRAFT, sem merge ou Production. A captura não foi persistida.
