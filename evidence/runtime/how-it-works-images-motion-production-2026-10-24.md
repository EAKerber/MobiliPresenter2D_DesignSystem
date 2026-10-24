# Como funciona — imagens e movimento em Production (24/10/2026)

**Alvo:** Production `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy READY `6adc221479c773577ed45e23`, rota `/how-it-works/`.

Em viewport desktop 1280×720, percorri a rota até o final para disparar as imagens com carregamento lazy. Na leitura final, o documento tinha 28 imagens: 28 completas com largura natural positiva, 0 falhas e 0 sem atributo `alt`. As imagens que estavam fora do viewport permaneceram pendentes até serem trazidas à tela. Esta contagem não cobre imagens definidas em CSS nem os recursos internos do iframe do YouTube.

A consulta `matchMedia("(prefers-reduced-motion: reduce)")` retornou `false` nesta sessão; isso não testa a resposta da página quando a preferência está ativada. A chamada `document.getAnimations()` não estava disponível no escopo de leitura do browser, então não pude medir se animações estavam em execução. A evidência anterior de movimento reduzido cobre somente o menu público, não esta rota inteira.

Não simulei falha de imagem, rede lenta ou erro de carregamento. Não alterei dados, estilos, configuração ou código de produto. Uma rota e um viewport; nenhuma captura foi persistida.
