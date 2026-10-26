# Experimento: alternativas para falha da ilustração

**Data:** 25/10/2026  
**Escopo:** comparação visual em DOM isolado; sem alteração de produto.

## Contexto observado

No ensaio sintético de falha, a imagem principal de estudo do espaço perdeu a altura intrínseca: o figure caiu aproximadamente 150 px. O mesmo arquivo no cartão compacto conservou sua caixa. O ensaio substituiu localmente o `src` da imagem por uma URL inválida; não representa um 404 de rede nem altera a implementação publicada.

## Alternativas de apresentação

- **Estado atual simulado:** a área colapsa e o navegador exibe o texto alternativo dentro do figure.
- **Opção A:** reservar a altura original, manter a superfície e a legenda, e apresentar um símbolo neutro com “Imagem indisponível”. Comunica falha sem afirmar o conteúdo que deixou de ser visto.
- **Opção B:** reservar a altura original, manter a superfície e a legenda, e mostrar a descrição do `alt`. Mantém o contexto visualmente disponível, mas repete parte da legenda e produz um bloco de texto mais longo.

## Capturas

Largura de viewport: 341 CSS px; tema claro; rota `/how-it-works/`.

- [Estado atual simulado](image-failure-fallback-baseline-2026-10-25.webp)
- [Opção A — estado indisponível](image-failure-fallback-option-a-2026-10-25.webp)
- [Opção B — descrição alternativa](image-failure-fallback-option-b-2026-10-25.webp)

## Limites

As opções são protótipos visuais temporários no DOM. Não foram verificadas semântica HTML final, anúncio por leitor de tela, foco/teclado, 404 real, tema escuro ou outras larguras. Este artefato não escolhe nem autoriza um fallback canônico ou mudança de produto.
