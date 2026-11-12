# G3 — recaptura local do controlador de tema e slots de marca (2026-11-11, BRT)

**Resultado:** os 28 casos alinharam o tema solicitado, o tema resolvido pelo documento e o tema de CASA_UI_THEME. O src de todas as imagens de marca correspondeu à variante esperada, e os dois cliques no controle percorreram as transições esperadas. O logo do cabeçalho carregou em todos os casos. Duas imagens de marca dos cards comparativos em /how-it-works/ a 390 px ainda estavam com complete=false no momento da leitura, embora tivessem currentSrc e naturalWidth=380; isso limita a conclusão de carregamento às marcas do cabeçalho. Não houve exceção de página. G3 segue parcial: os slots, dimensões e folhas continuam diferentes entre shells; isso não justifica extrair ou unificar CSS.

## Identidade e método

- Fonte: EAKerber/MobiliPresenter2D, main em 221b54b2a41ecc8c338d1bf2cf67280cf165ce95, checkout detached limpo. Nenhum arquivo do produto foi alterado.
- Navegador: Microsoft Edge 157.0.4341.46, Playwright, DPR 1; viewports 390×900 e 1366×900 CSS px.
- Rotas: /, /how-it-works/, /about/, /viewer/, /config/, /admin.html e /access/manage.html, cada uma em light e dark nos dois viewports.
- O modo foi definido antes de cada navegação. O recibo registra estado pedido, documentElement.dataset.theme, CASA_UI_THEME, origem/variante/carregamento/retângulo de cada imagem data-brand-variant, slot e retângulo do controle, duas ativações do controle e erros de página, console e HTTP.
- Todo tráfego foi servido localmente. Os endpoints de configuração e navegação sem fixture retornaram 404 intencionalmente, e o endpoint de sessão foi fixado como não autenticado. Nenhum serviço hospedado, banco ou sessão autenticada foi usado.
- Recibo JSON: result.json, SHA-256 DDBDE70729B2FCECDA0D4A5450545705B0D8F1FD585834EDA83777054226C962.
- Runner local: capture-theme-asset-slots.mjs, SHA-256 F8E4E045B29ED29D5914B362CB578E08192CC1E8E535292ACC64A3E4E22B43E9. O runner preserva os caminhos do checkout e browser deste host.

## Cobertura e resultados

| Rota | Slot do controle | Imagens de marca |
|---|---|---:|
| / | cabeçalho público: header-actions | 3 |
| /how-it-works/ | cabeçalho público: header-actions | 3 |
| /about/ | cabeçalho público: header-actions | 2 |
| /viewer/ | viewer-header__actions | 1 |
| /config/ | topbar private-header__actions | 1 |
| /admin.html | admin-topbar__actions private-header__actions | 1 |
| /access/manage.html | admin-topbar__actions private-header__actions | 1 |

Os 28 casos registraram concordância entre preferência inicial, tema raiz e API. Cada src de marca correspondeu ao asset light/dark esperado; nenhuma linha teve divergência de tema ou asset. Os logos de cabeçalho estavam completos em todos os casos. Duas imagens de marca dos cards de comparação abaixo da área inicial em /how-it-works/ a 390 px ainda indicavam complete=false, mas tinham naturalWidth=380. Os botões estavam presentes, com altura de 44 px; larguras variaram com o shell, viewport e texto do modo. Em todos os casos, as duas ativações registraram o modo, tema resolvido e logos resultantes.

Nos 14 casos iniciados em light, o controle foi para dark e depois auto, resolvendo para light segundo o color scheme light. Nos 14 casos iniciados em dark, a primeira ativação foi para auto, resolvendo para dark segundo o color scheme dark, e a seguinte para light. Esse ciclo se repetiu nas sete rotas e nos dois viewports.

## Erros e limites

Foram registrados 28 HTTP 404, distribuídos em: 12 chamadas da private-navigation.bundle.js; 4 da access/manage.bundle.js; 4 da admin/admin.bundle.js; 4 da API buyer-configuration; e 4 da API public-modules. Também houve logs de console em 16 casos: recursos 404 e o aviso de configuração publicada indisponível em /config/. As chamadas privadas/API foram deixadas sem fixture de propósito. Isso impediu verificar menu privado, sessão autenticada, configuração Buyer publicada e conteúdo funcional do Viewer. Não houve exceções JavaScript de página.

A matriz não mediu foco por teclado, hover, navegação privada autenticada, interação do Viewer, Safari/iPad ou resposta tátil. Não foram produzidos screenshots neste subgate; ele mede DOM/CSSOM, slots e estados do controlador, não é revisão visual. O Preview hospedado de /config/ continua sem configuração publicada válida.

## Conclusão e próximo gate

A implementação compartilhada do controlador e da troca dos assets de marca funcionou nesta matriz local, em shells públicos, Viewer e páginas privadas. Os slots e dimensões são contextuais; mantê-los separados segue sustentado pela evidência. Antes de qualquer extração CSS, ainda é necessário revisar estados de foco/hover e validar o shell privado com uma fixture de configuração autorizada; a revisão hospedada e a cobertura cross-platform continuam em aberto. G3 permanece parcial.
