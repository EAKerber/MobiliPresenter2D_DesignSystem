# Falha induzida de imagens em rotas públicas — 25/10/2026

**Contexto:** páginas Production em Chromium isolado, sem sessão; viewport CSS emulado de 341 × 768 px. Cada alvo carregou com sucesso antes do ensaio. Para simular falha sem alterar arquivos nem enviar gravações ao servidor, troquei o src do elemento somente no DOM isolado por um data URL inválido. A falha observada é induzida, não um 404 natural.

| Rota | Elemento amostrado | Antes | Depois da falha induzida |
|---|---|---|---|
| Landing | Hero lifestyle; alt “Ambiente planejado com a interface Casa em Módulos” | 1074 × 1465 intrínsecos; caixa 326 × 350 px; object-fit cover | naturalWidth 0; caixa permaneceu 326 × 350 px; alt preservado; sem handler inline |
| Viewer | Imagem-base da composição; alt “Composição da cozinha Casa em Módulos” | 1536 × 1024 intrínsecos; caixa 282,7 × 188,4 px; object-fit contain | naturalWidth 0; caixa permaneceu 282,7 × 188,4 px; alt preservado; sem handler inline |
| Como funciona | Ilustração de planta/estudo de espaço | 1100 × 733 intrínsecos; caixa 288,7 × 192,4 px | naturalWidth 0; caixa caiu para 288,7 × 42,7 px; o pai caiu de 290 × 226,4 para 290 × 76,7 px; alt preservado |
| Quem somos | DOM continha logo, ícone WhatsApp e logo repetido; não havia imagem de conteúdo para escolher nesta rota | 3/3 elementos carregaram | Falha de conteúdo não induzida nesta rota |

As coleções carregadas antes do ensaio estavam completas na Landing (18/18), Quem somos (3/3) e Viewer (22/22); lazy loading foi forçado para eager apenas na página isolada para aguardar as imagens. O ensaio do Viewer mudou só a camada-base no DOM temporário; não foi feita verificação da composição resultante por screenshot.

**Leitura:** a caixa fixa preservou o layout do hero e da imagem-base do Viewer nesta amostra. Na ilustração da página Como funciona, a falha removeu sua altura intrínseca e expôs um colapso visual. Isso não determina o tratamento estético correto: decisions.json não define um componente visual para fallback de imagem. Não houve alteração do produto.

**Limites:** uma imagem por rota com conteúdo visual; Quem somos não tinha imagem de conteúdo em document.images. A amostra não cobre fundos CSS, todas as cenas, leitores de tela, falhas naturais de rede ou outros estados de carregamento. img.onerror não estava definido como propriedade nos alvos; isso, sozinho, não prova ausência de listeners registrados via addEventListener. Não arquivei capturas antes/depois.
## Complemento — varredura de falha das imagens com alt descritivo (25/10/2026)

Em contexto isolado de Production, 341 × 768 CSS px, 28/28 imagens carregaram antes do ensaio. Induzi falha local, um alvo por vez, nos 20 elementos de `/how-it-works/` com `alt` não vazio; em seguida restaurei cada `src`. Ao final, todas as 20 imagens estavam restauradas e carregadas. Os oito elementos com `alt=""` não foram submetidos a este complemento.

| Contexto amostrado | Caixa antes | Caixa durante falha | Resultado |
|---|---:|---:|---|
| Logo do header | 122,9 × 44 px | 122,9 × 44 px | Caixa preservada |
| Hero de abertura | 326 × 320 px | 326 × 320 px | Caixa preservada |
| Comparação planejados | 288,7 × 104 px | 288,7 × 104 px | Caixa preservada |
| Ilustração principal de estudo de espaço | 288,7 × 192,4 px; pai 290 × 226,4 px | 288,7 × 42,7 px; pai 290 × 76,7 px | Colapso de 149,7 px |
| Quatro renders de módulos | 138,7 × 190 px cada | Igual | Caixas preservadas |
| Integração modular | 250 × 125 px | 250 × 125 px | Caixa preservada |
| Seis ilustrações de economia, incluindo o mesmo `estudo-espaco.webp` em cartão compacto | 88 × 90 px nas imagens quadradas; 88 × 90 px no uso compacto do estudo | Igual | Caixas preservadas |
| Imagens de puxadores e hero final | Caixas de 139,2 × 132 px e 326 × 520 px | Iguais | Caixas preservadas |

**Leitura:** 19/20 elementos descritivos mantiveram as dimensões observadas; um único contexto colapsou. O mesmo arquivo `estudo-espaco.webp` manteve a caixa no cartão compacto, então a falha depende da composição/wrapper do contexto, não apenas do arquivo. `alt` permaneceu presente durante todos os ensaios.

**Limites:** falha simulada com data URL inválida no DOM isolado, não resposta 404 ou falha de rede natural. Não arquivei screenshot durante a falha. A amostra não define o fallback visual, semântica de substituição nem comportamento de background CSS. Nenhum arquivo ou dado de Production foi alterado.