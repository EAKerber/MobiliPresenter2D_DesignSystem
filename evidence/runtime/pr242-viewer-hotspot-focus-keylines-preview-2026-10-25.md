# VIS-002 — keylines de foco dos hotspots no preview — 25/10/2026

## Escopo e autorização

Teste autorizado pelo usuário para preview na PR de produto [#242](https://github.com/EAKerber/MobiliPresenter2D/pull/242). A regra permanece limitada a `.scene-hotspot:focus-visible`; sem mudança em tokens, hover, seleção, dados da cena, `decisions.json`, merge ou Production.

Preview usado para leitura visual e captura: https://deploy-preview-242--mobilipresenter2d.netlify.app/viewer/
Head da PR: `c2659513c22d886bc4de63074a66ed9228524c0f`.
Deploy Preview confirmado no DOM: `6ade805a7dc745ffae862ccd`.

## Implementação em teste

O anel VIS-002 continua com 4 px, offset CSS declarado de 3 px, `#8B6A40` no claro e `#D8BC7C` no escuro. A regra de foco usa `box-shadow: 0 0 0 2px #000, 0 0 0 3px #fff`: faixa preta ampliada para 2 px e faixa branca na extensão de 3 px. A extensão externa do outline não mudou.

## Verificações atuais

No Deploy Preview do PR, em 390 × 844 e 1280 × 800, nos temas claro e escuro:

- Os sete hotspots aceitaram foco visível; as duas cores das keylines e o outline foram confirmados no CSS computado.
- O indicador permaneceu dentro da cena; folga mínima computada de 0,11 CSS px no mobile e 6,29 px no desktop.
- Não houve overflow horizontal.

Os sete checks associados ao head terminaram com sucesso: App build purity, Current variant fidelity, Summary pricing browser, Stone browser, Mobile browser, Public routing before Clerk e Current asset gates.

## Medição sobre pixels compostos

Amostrei capturas escuras de 390 × 844 comparando o hotspot focado com uma captura-base temporária sem outline/sombra. No hotspot 01, sobre área clara, pixels da faixa escura tiveram contraste de 7,05:1 no mínimo amostrado, 7,56:1 no percentil 10 e 9,16:1 na mediana. No hotspot 02, sobre áreas mais escuras da foto, pixels da faixa preta chegaram a 2,04:1 no mínimo; o percentil 10 ficou em 3,00:1 e a mediana em 7,29:1.

Isso confirma melhora em uma área clara, mas não comprova contraste de 3:1 em cada trecho da fotografia. A rasterização e o fundo variam ao longo do contorno, e a faixa branca não demonstrou uma margem confiável nos pontos amostrados. Não declarar conformidade WCAG com esta amostra.

## Estado do preview isolado

No endereço `https://deploy-preview-242--m2d-auth-ci-isolated.netlify.app/viewer/`, a página carrega, mas `GET /api/public-modules` retorna HTTP 503 com `{"error":"public_modules_unavailable"}`; o Viewer não renderiza hotspots. A função de Netlify `public-modules` foi inspecionada no head testado: ela lê o snapshot publicado em Netlify Blobs (`configurator-settings`) e responde 503 quando a leitura retorna ausência/invalidez ou falha interna. A versão Deploy Preview tenta recorrer à URL primária do mesmo site; a rota primária `https://m2d-auth-ci-isolated.netlify.app/api/public-modules` também retorna o mesmo 503.

Isso aponta, como inferência do código e das respostas, para snapshot publicado ausente/inválido no Netlify Blobs do site isolado ou falha de leitura desse armazenamento. Os logs de borda identificam a função `public-modules`, mas não têm linhas de log da aplicação; não é possível distinguir essas causas. `DATABASE_URL` e `ACCESS_GATE_SECRET` estão configuradas no site isolado com escopos de build, functions e runtime, mas não são lidas por essa função. Não há evidência para adicionar ou trocar essas variáveis como correção do 503.

No Deploy Preview principal, `GET /api/public-modules` retorna HTTP 200 e a cena renderiza. Os checks verdes do commit não cobrem o runtime isolado do Viewer.

## Limites e estado

- A amostra visual contém apenas a cena Cozinha; não generalizar para outras fotografias.
- A folga mobile mínima permanece pequena (0,11 CSS px).
- A medição de pixels é diagnóstica para os hotspots 01 e 02, não uma certificação WCAG global.
- O preview isolado precisa de um snapshot público válido ou de uma leitura funcional do armazenamento para renderizar o Viewer; isso está fora do escopo autorizado do PR #242.
- PR #242 permanece DRAFT. Revisão visual humana pendente; sem integração ou publicação.
- A camada neutra continua experimental e não altera a decisão canônica.

## Referência

A cor e a geometria do anel permanecem conforme VIS-002. As keylines só afetam o foco visível e não alteram a decisão canônica.


## Diagnóstico adicional de escala CSSOM — 25/10/2026

No preview principal da PR #242, 390 × 844, inspecionei um hotspot selecionado e um não selecionado enquanto recebiam `:focus-visible`. A regra da branch declara outline 4 px, offset 3 px e keylines com raio máximo 3 px. O CSSOM reportou a espessura 4 px como 4 px, mas devolveu offset `2.66667px` para os 3 px declarados.

Para separar regra do produto de comportamento de leitura, criei e removi imediatamente elementos `div` de diagnóstico, sem classes nem transforms, com `outline` e `outline-offset` inline de 1 a 8 px. A página reportou: 1→0,66667; 2→2; 3→2,66667; 4→4; 5→4,66667; 6→6; 7→6,66667; 8→8 px — o mesmo padrão de quantização em largura e offset. O viewport era 390 px, `visualViewport.scale=1`, `devicePixelRatio≈1`, zoom CSS do root/body `1`, sem transform nos ancestrais. Isso mostra que a discrepância não é exclusiva do seletor de hotspot. Uma escala interna de renderização é uma hipótese compatível com o padrão, mas a causa continua **não confirmada**.

Também comparei, apenas no DOM da sessão isolada, uma redistribuição de `box-shadow` de raios `2/3` para `1/3` (faixas preta/branca de 2 px/1 px para 1 px/2 px), sem ampliar o limite exterior de 3 px. As capturas de um hotspot sobre a fotografia em claro/escuro pareceram semelhantes; não repeti amostragem de pixels com a variante. A alternativa não foi adotada nem considerada aprovada.

**Consequência:** manter a declaração aprovada 4/3 px; não ajustar a regra para forçar um valor CSSOM específico. A validação de contraste da keyline sobre as sete áreas fotográficas segue inconclusiva e requer revisão/evidência visual adicional. Nenhum arquivo do produto foi alterado nesta leitura.


No seguimento, repeti o mesmo elemento de diagnóstico com viewport constante e `deviceScaleFactor` emulado em 1, 1,25, 1,5 e 2. O padrão CSSOM permaneceu idêntico em todos os quatro valores (1→0,66667; 2→2; 3→2,66667; 4→4; 5→4,66667; 6→6; 7→6,66667; 8→8), enquanto `devicePixelRatio` reportou cada valor solicitado e `visualViewport.scale` permaneceu 1. Isso afasta DPR emulado como causa isolada; não identifica se a origem restante está no Chrome, na medição DevTools ou em outra escala/renderização. Não emulei zoom pelo menu do navegador nem mudei valores do produto.


## Atualização da variante 1 px/2 px — 25/10/2026

Após autorização do usuário para testar keylines em preview, a PR de produto #242 recebeu o commit `55a9c280578d065ba79cbb3565f83ac05964eec8`. O Deploy Preview READY é `6ade958bda108ba3ea541fe2` em https://deploy-preview-242--mobilipresenter2d.netlify.app/viewer/. A sombra foi redistribuída para faixa preta de 1 px e branca de 2 px, mantendo raio total 3 px; o anel VIS-002 permaneceu em 4 px/offset declarado de 3 px, nas cores de tema aprovadas.

A leitura por teclado confirmou `:focus-visible` em 390×844 e 1280×800 nos temas claro e escuro. CSSOM retornou o outline e a sombra esperados; os quatro estados tiveram `scrollWidth <= innerWidth`. Inspecionei screenshots de foco em cada tema/tamanho. Não observei erro de console no preview durante a rechecagem. O Deploy Preview principal retornou HTTP 200 em `/api/public-modules`; o projeto isolado continuou em HTTP 503 com `public_modules_unavailable`, sem mensagem interna nos logs de borda. Essa falha específica permanece sem causa confirmada.

Os sete workflows do head passaram e o deploy do preview ficou READY. Não repeti amostragem de contraste por pixels para esta redistribuição; portanto ela é apenas uma variante visual em teste, sem comprovação de 3:1 em todos os trechos da fotografia e sem declaração de conformidade WCAG. A PR permanece DRAFT, sem merge ou Production.


## Delimitação pelo código do 503 isolado — 25/10/2026

Readback do produto `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`: `netlify/functions/public-modules.mjs` escolhe `getStore({name:"configurator-settings"})` quando `context.deploy.context === "production"`; em Deploy Preview escolhe `getDeployStore`. A função lê a chave `published` via `app/core/published-configuration.js`. Ela só consulta o domínio primário como fallback quando está em Deploy Preview e a leitura do snapshot está ausente. Na URL principal do site isolado, esse fallback não se aplica. A função colapsa ausência, snapshot inválido e exceção de storage em `public_modules_unavailable`; os logs de borda não diferenciam os casos.

A rota não consulta Supabase nem lê `DATABASE_URL` ou `ACCESS_GATE_SECRET`. `netlify/functions/configuration.mjs` usa o mesmo store/chave; seu GET/PUT exige usuário administrador, e o PUT salva a configuração publicada após validação. Isso torna a publicação de um snapshot válido no site isolado um próximo caminho operacional possível, mas a existência/conteúdo do Blob não foi lida nesta auditoria. As ferramentas Netlify conectadas não oferecem leitura de Blobs. Portanto, ausência do snapshot é uma hipótese forte e delimitada, mas não confirmada; não alterei Blob nem configuração.


O readback do projeto Netlify confirma o caminho efetivamente ativo: site `m2d-auth-ci-isolated`, deploy `6adc77b6603e52a336fe045d`, branch `main`, commit `5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, contexto `production`, estado READY. Portanto o endpoint primário lê o store compartilhado do site isolado, não o store de um Deploy Preview. Ainda não foi possível ler o Blob para confirmar ausência/invalidez versus erro de leitura.


## Correção de empilhamento e leitura raster — 25/10/2026

A captura inicial da variante 1/2 px revelou que o frame de seleção `.selection-frame` (`z-index:900`) cobria as sombras da camada `.scene-hotspots` (`z-index:500`). Uma alteração temporária de empilhamento fez as faixas aparecerem. A PR de produto #242 adicionou `.scene-hotspots:has(.scene-hotspot:focus-visible) { z-index:901 }`, que só eleva a camada enquanto há foco visível de teclado; a regra não muda tokens, seleção ou geometria do anel. Head atual `1d5d9dad957800a3dcef72214db67f4d505c47c1`; Deploy Preview READY `6ade99222c5e1eeeae48d7fc`.

Após a correção, os sete hotspots foram focalizados nos quatro estados claro/escuro em 390×844 e 1280×800. Todos computaram `:focus-visible`, o anel temático 4 px, a sombra 1/3 px ficou visível e não houve overflow horizontal. A folga mínima computada ao limite da cena é 0,11 CSS px no mobile e 6,29 px no desktop. Em uma captura escura mobile do hotspot 01, pixels exatos pretos e brancos apareceram nas faixas; essa contagem confirma que foram pintados, mas não calcula contraste contra a foto. Nenhuma nova medição por pixel foi feita e não se declara 3:1 em todo o contorno. Não houve erros de console no preview inspecionado; os sete workflows e os dois status Netlify passaram.

O site isolado continua separado: o endpoint primário retorna 503. A leitura de código anterior delimita a rota ao Blob publicado do próprio site, mas o conteúdo do Blob não pode ser lido pelas ferramentas conectadas. PR #242 permanece DRAFT, sem merge ou Production.


## Amostragem por pixel da variante 1 px preta/2 px branca — 25/10/2026

Medição no Deploy Preview atualizado, cena Cozinha, 390×844, tema escuro e claro, hotspots 01–07. Para cada imagem, comparei pixels da captura com foco com a captura-base do mesmo documento/viewport e mesmo empilhamento (container de hotspots em z901), com outline/sombra de foco, pseudo realçado e rótulo ocultos na base. Usei contraste WCAG entre a cor focada e a cor-base no mesmo pixel, incluindo apenas pixels com diferença máxima de canal >8. O resultado é diagnóstico raster da faixa, não certificação de conformidade.

| Hotspot | Preta: n / min / P10 / mediana / <3:1 | Branca: n / min / P10 / mediana / <3:1 |
| --- | --- | --- |
| 01 | 0 pixels distintos da base | 122 / 1,492 / 1,566 / 1,635 / 113 |
| 02 | 60 / 6,312 / 6,989 / 8,312 / 0 | 128 / 1,352 / 1,354 / 2,068 / 124 |
| 03 | 120 / 5,801 / 14,601 / 14,939 / 0 | 128 / 1,340 / 1,349 / 1,406 / 125 |
| 04 | 197 / 1,050 / 7,205 / 10,801 / 6 | 398 / 1,353 / 1,406 / 1,926 / 333 |
| 05 | 124 / 7,051 / 13,952 / 14,694 / 0 | 132 / 1,316 / 1,328 / 1,437 / 132 |
| 06 | 126 / 1,923 / 4,545 / 13,412 / 4 | 132 / 1,290 / 1,302 / 3,352 / 54 |
| 07 | 86 / 2,243 / 6,126 / 6,265 / 3 | 90 / 1,570 / 1,570 / 1,597 / 88 |

As mesmas medições neutras se repetiram no tema claro, pois a fotografia e as duas keylines são iguais; só o anel dourado muda. A faixa branca fica abaixo de 3:1 na maioria dos pixels amostrados. A preta fica acima de 3:1 na maior parte, mas há pontos abaixo nos hotspots 04, 06 e 07; no hotspot 01, nenhum pixel preto mudou o bastante para ser contado. Portanto esta variante não demonstra contraste consistente sobre toda a foto. Não declarar conformidade WCAG. A PR permanece DRAFT; nenhuma publicação foi feita.


## Amostragem da distribuição 2 px preta / 1 px branca — 26/10/2026

Teste autorizado pelo usuário como nova distribuição em preview. O head da PR de produto #242 é `0ceaac923eccd31db3ec20f8fb044112328d8faf`, Deploy Preview READY `6ade9e2f6a324cc60954c806`. A regra mantém o anel VIS-002 (4 px, offset CSS declarado de 3 px, cores por tema) e distribui as sombras como `0 0 0 2px #000, 0 0 0 3px #fff`; a extensão máxima CSS continua 3 px.

Medi o Viewer da cena Cozinha em 390×844, tema escuro. Os sete hotspots receberam foco por teclado. Para cada um, comparei a captura focada com uma base do mesmo viewport/estado e empilhamento. A amostra ficou limitada ao exterior do retângulo do hotspot, até 4 px, e a pixels cuja diferença máxima de canal excedeu 8. Classifiquei pixels quase pretos (canais ≤20) e quase brancos (canais ≥235) e calculei contraste WCAG sRGB com o pixel-base correspondente. Este é um diagnóstico local, não certificação.

| Hotspot | Preta: n / min / P10 / mediana / <3:1 | Branca: n |
| --- | --- | --- |
| 01 | 309 / 7,349 / 11,129 / 12,106 / 0 | 0 |
| 02 | 308 / 1,587 / 2,972 / 7,990 / 36 | 0 |
| 03 | 408 / 2,305 / 2,699 / 7,354 / 88 | 0 |
| 04 | 485 / 1,056 / 6,420 / 11,771 / 33 | 0 |
| 05 | 388 / 4,797 / 13,015 / 14,231 / 0 | 0 |
| 06 | 525 / 1,923 / 6,184 / 12,888 / 8 | 0 |
| 07 | 321 / 2,144 / 4,128 / 11,763 / 24 | 0 |

Há pixels pretos abaixo de 3:1 nos hotspots 02, 03, 04, 06 e 07; a captura-base não distinguiu pixels brancos na faixa definida em nenhum hotspot. Portanto, esta distribuição tampouco demonstra contraste consistente sobre a foto. A amostra cobre apenas tema escuro e viewport mobile desta cena; não generalizar a outros temas, imagens ou ambientes, nem declarar conformidade WCAG.

Todos os sete workflows do head passaram e os dois status Deploy Preview Netlify ficaram SUCCESS; a navegação por teclado confirmou `:focus-visible` nos sete hotspots, sem overflow horizontal. A medição não é aprovação visual. PR #242 continua DRAFT, sem merge/Production.


## Placa opaca de apoio — head 584c9d3, 26/10/2026

A distribuição 2/1 px foi substituída no Deploy Preview da PR de produto #242 por uma placa opaca de 8 px atrás do foco: branca (`#fff`) no tema claro e quase preta (`#111`) no escuro. O anel VIS-002 permaneceu com 4 px, offset CSS declarado de 3 px e dourado `#8B6A40` / `#D8BC7C`. O limite computado do anel foi 6,67 px; a placa se estende até 8 px.

No head `584c9d3f06896b9c4f44f4437914c9f7b7400d08`, deploy principal READY `6adea3e8c5b47f8e0f4cee0c`, sete workflows passaram e os status Netlify principal/isolado passaram. O foco por Tab alcançou os sete hotspots em 390×844, tema escuro. Também medi todos os sete com `:focus-visible` em 390×844 e 1280×800, claro e escuro; todos permaneceram no viewport, sem overflow horizontal.

O contraste sRGB calculado entre o anel dourado e sua placa uniforme foi 4,96:1 no claro e 10,25:1 no escuro, idêntico nos sete controles por compartilharem as mesmas cores. Capturas mostraram o anel dourado contra a placa nas duas aparências. Isso demonstra contraste do anel em relação à placa neste componente e nesta cena; não é auditoria de acessibilidade global nem prova de contraste da borda externa da placa contra toda a fotografia. A variante continua candidata de preview, sem merge, mudança em `decisions.json` ou Production.
