# Rotas públicas — teclado e carregamento de imagens em Production (24/10/2026)

**Alvo:** `EAKerber/MobiliPresenter2D@main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, deploy Netlify READY `6adc221479c773577ed45e23`. Viewport temporário 390×844 CSS px, tema escuro; rotas visitadas em contexto público. O override de viewport foi removido e as abas temporárias foram fechadas.

| Rota | Imagens no documento | Falhas | Sem `alt` | Overflow horizontal |
|---|---:|---:|---:|---|
| `/` | 18/18 completas | 0 | 0 | Não |
| `/about/` | 3/3 completas | 0 | 0 | Não |
| `/viewer/` | 22/22 completas | 0 | 0 | Não |

Em `/`, a camada `#introSplash` já estava oculta (`opacity:0`, `pointer-events:none`) na primeira leitura. Um clique no botão do menu abriu `primaryNav` imediatamente; Escape fechou e o foco retornou ao botão. Isso confirma o caminho depois da saída da camada, não o clique durante sua animação ativa.

Em `/about/`, o primeiro Tab focou “Pular para o conteúdo”. Enter alterou a URL para `/about/#main`, mas o foco terminou em `BODY`; `main#main` não recebeu foco, não tem atributo `tabindex` e `scrollY` permaneceu em 0. Esse comportamento permanece uma divergência observada; não fiz correção no produto.

Nas três rotas, `prefers-reduced-motion: reduce` retornou `false`. Não há emulação de mídia disponível nesta sessão do browser; o teste não confirma o comportamento quando a preferência está ativa. A API de animações também não estava disponível no escopo de leitura, então a execução de animações não foi medida. Nenhuma falha de imagem ou rede lenta foi simulada. Uma leitura de cada rota/viewport; capturas não persistidas; sem alteração de código ou dados.


## Rechecagem adicional em Production — 24/10/2026

**Alvo:** Netlify deploy READY `6adc221479c773577ed45e23`, branch `main`, commit `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`; rota `/how-it-works/`, contexto isolado do navegador, viewport de conteúdo 1280×669 CSS px (janela 1280×720), altura documental 9.543 px. Rolei a página em etapas para acionar o carregamento lazy e aguardei a estabilização.

- 28/28 imagens ficaram completas com dimensões naturais válidas; 0 imagens quebradas e 0 ainda pendentes ao final.
- As 28 têm atributo `alt`; oito usam `alt=""`. O ícone do WhatsApp está também marcado `aria-hidden="true"`; as demais ocorrências vazias são a ilustração e o logo redundante do cartão comparativo e cinco ilustrações de etapa, cada uma acompanhada de título e descrição. O sentido decorativo dessas imagens não foi homologado; fica como classificação a revisar, sem concluir ausência de texto alternativo.
- A preferência `prefers-reduced-motion` estava desativada. Esta passagem não mede teclado, estados de foco nem comportamento com movimento reduzido ativo.

Leitura somente de DOM; sem interação com formulários, alterações de dados, CSS ou código do produto. A evidência vale para esta rota, commit, viewport e sessão.


## Inventário DOM de imagens com alt vazio em Como funciona — Production (24/10/2026)

A leitura isolada da rota encontrou oito imagens com `alt=""` entre as 28 completas:

| Elemento | Contexto DOM observado | Leitura preliminar |
|---|---|---|
| Ícone WhatsApp | `aria-hidden="true"`; o link tem nome acessível “Fale conosco pelo WhatsApp”. | Decorativo/redundante para tecnologia assistiva, apoiado pelo nome acessível do link. |
| Ilustração de móveis prontos | Desenho de gabinete; ao lado, a tabela já apresenta em texto os critérios comparados. | Candidato decorativo; não contém dados textuais únicos na leitura DOM. |
| Logo da Casa em Módulos no cartão comparativo | `alt=""`; o cartão tem título visível “Casa em Módulos” e os detalhes aparecem em texto. | Candidato redundante/decorativo; marca já tem rótulo textual no mesmo cartão. |
| Cinco ilustrações das etapas (cozinha, lavanderia, sala, quarto, escritório) | Cada imagem fica numa lista com número, título do ambiente e descrição curta. | Candidatas decorativas por contexto textual, mas cada arquivo ainda precisa de inspeção visual para confirmar que não comunica detalhe essencial ausente do texto. |

A comparação de móveis prontos foi aberta como imagem no navegador: é uma ilustração de gabinete sem rótulos visuais aparentes, enquanto as diferenças estão na tabela textual adjacente. As outras cinco ilustrações foram apenas relacionadas pelo DOM, nomes de arquivo e itens da lista; não foram todas inspecionadas visualmente nesta passagem. Portanto, a classificação das oito imagens segue **candidata**, sem homologação de design/acessibilidade e sem mudança de `alt`, conteúdo ou CSS.
