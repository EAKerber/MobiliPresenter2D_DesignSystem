# Auditoria runtime pública G1 — 2026-10-21

**Produto:** [casaemmodulos.casa](https://casaemmodulos.casa/)  
**Commit de produção:** [`1878ae1057ce7c6190e0c8cb08a1f3baadd49463`](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463)  
**Deploy:** [`6ad6c3b51b6be05647167f94`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94), ready.  
**Escopo:** leitura e interação somente nas páginas públicas; nenhum código, dado de produto ou configuração foi alterado.

## G1-R1 — painel econômico em “Como funciona”

O painel respondeu corretamente nos viewports observados de 390×844, 768×1024 e 1366×768, nos temas claro e escuro. Alternar itens atualizou seleção e conteúdo, manteve um único item expandido, e o painel de detalhe ocupou a linha correta após o grid em cada composição responsiva. Enter abriu um item; clicar novamente no ativo fechou o detalhe. Não foi observado overflow horizontal.

Este resultado cobre os estados e resoluções exercitados; não certifica todos os breakpoints, navegadores ou estados de foco. Não foi necessária uma escolha estética.

## G1-R2 — landing, seleção de ambiente e carrossel

No estado estabilizado da landing, `#introSplash` ficou invisível e sem capturar ponteiros. O CTA da Cozinha navegou para `/viewer/`. Os cinco ambientes atualizaram rótulo e imagem; o CTA permaneceu específico da Cozinha. Isso confirma apenas o estado posterior à animação e os ambientes exercitados, não o comportamento sob movimento reduzido.

### FIND-016 — seleção de Lavanderia diverge da página do carrossel

Em viewport CSS 390×844 e tema escuro, o carrossel foi levado ao grupo 2 e o cartão “Lavanderia” selecionado. Em **4 de 4 repetições**, o ambiente permaneceu selecionado e o painel mostrou “Lavanderia”, mas a paginação mudou para o grupo 1; os cartões da Lavanderia e Escritório deixaram de estar na janela do carrossel. O usuário recebe, portanto, um painel de detalhe cuja opção ativa não está visível na lista.

A [captura persistida](../../visualEvidence/public/landing/g1-lavanderia-selected-group1-390x844-2026-10-21.svg) registra o estado: grupo 1 visível e detalhe da Lavanderia.

**Hipótese técnica, ainda não comprovada como causa exclusiva:** no código publicado em `app/landing/landing.js` do commit `1878ae1`, `revealCard()` reage a qualquer borda fora da janela e escolhe o grupo pela posição da borda esquerda. Uma medição durante a auditoria encontrou o cartão cerca de 0,16 CSS px além da borda direita; arredondamento fracionário pode disparar a condição e, como a borda esquerda ainda está dentro da janela, escolher o grupo 1. O runtime confirma o comportamento; não confirma ainda qual margem/tolerância é a correção adequada.

O issue [#207](https://github.com/EAKerber/MobiliPresenter2D/issues/207) cobre a indicação “Visualização em breve” para ambientes sem viewer e inclui teste de troca rápida, mas não registra esta divergência de paginação. A falha foi registrada no backlog do produto como [issue #224](https://github.com/EAKerber/MobiliPresenter2D/issues/224); o issue #207 continua separado por cobrir apenas a indicação de disponibilidade.

## Limites e continuidade

- `prefers-reduced-motion` não foi emulado; suporte CSS estático não é validação runtime.
- Não se capturou uma animação `wave` ativa; sua presença ou falha continua desconhecida.
- Rede lenta e falha de carregamento de imagem não foram simuladas.
- Nenhuma proposta visual foi introduzida. O próximo passo técnico é isolar a regra de revelar cartão, validar limites fracionários e só então propor correção no repositório do produto.
