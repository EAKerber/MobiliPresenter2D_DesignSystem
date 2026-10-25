# VIS-002C v0.3 — revisão manual do preview em dez contextos

Data: 25/10/2026

## Identidade e escopo

- Produto: PR #241, branch `a11y/vis002-measured-copy-contrast-20261024`, head `f102c3037e2f64ebb904643bbc076064322f1672`.
- Distribuição: Design System PR #52, head `2f11ecf8948c779706a0ce0795e088d29633fb7e`.
- Preview principal: `https://deploy-preview-241--mobilipresenter2d.netlify.app/`.
- Preview isolado: `https://deploy-preview-241--m2d-auth-ci-isolated.netlify.app/`.
- Escopo: DOM/CSSOM das dez regras autorizadas em Landing, Quem somos e Como funciona; sem alteração de Production, `decisions.json`, tokens globais, Viewer, eyebrows ou assinaturas.

## Resultado visual e de estilo

- Tema claro: os dez seletores resolvem para `#292723` (`rgb(41, 39, 35)`) nas três rotas. Os fundos lidos são `#F0EDE8` e `#E8E3DC`; a distribuição calcula 12,77:1 e 11,68:1, respectivamente.
- Tema escuro: os mesmos seletores mantêm `#C4BCB2` (`rgb(196, 188, 178)`) sobre `#20211F` (`rgb(32, 33, 31)`).
- Landing: 3 grupos de seletores; About: 3; Como funciona: 4. A contagem de nós encontrados foi 3, 6 e 5, respectivamente.
- A captura visual da Landing/Como funciona não mostrou conflito na cópia medida. A faixa do Netlify Drawer aparece na borda inferior do preview e é uma sobreposição do ambiente de revisão.

## Viewports

- Desktop emulado: 1280 × 720 CSS px. `documentElement.clientWidth` e `scrollWidth` foram ambos 1265 px, diferença causada pela scrollbar vertical clássica; não houve overflow horizontal.
- Mobile emulado: 390 × 844 CSS px. Em cada rota, `clientWidth` e `scrollWidth` foram 390 px; overflow horizontal zero.
- Os dez seletores foram verificados no claro e no escuro em desktop; todos os dez foram verificados no claro em mobile. O escuro em mobile não foi repetido nesta passagem.

## Integração e limites

- Oito workflows do produto terminaram SUCCESS na head acima: build purity, product pin, current asset gates, Mobile, Public routing, Summary/Pricing, Stone e current variant fidelity.
- Os status de Deploy Preview principal e isolado estão SUCCESS/READY. O gate de produto confirma os hashes do pacote v0.3 do Design System.
- Esta é uma verificação manual restrita de uma head e das três rotas públicas, apoiada por DOM/CSSOM e uma captura visual. Não é uma homologação global de acessibilidade nem substitui a revisão humana final.
- PRs #241 e #52 continuam DRAFT. PR #240 segue em v0.2 e requer reconciliação antes de qualquer integração conjunta. Sem merge ou deploy de Production.