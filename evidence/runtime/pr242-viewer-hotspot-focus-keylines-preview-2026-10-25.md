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
