# G2 — recaptura pareada do Configurador (2026-11-11, BRT)

**Resultado deste subgate:** a divergência anterior entre o estado escuro e a linha candidata do `result.json` não se repetiu quando o tema efetivo foi fixado e registrado junto ao hash de cada screenshot. Este resultado substitui a linha escura não pareada; não fecha G2, #208, #216 nem DS-05A.

## Identidade e método

- Produto: `EAKerber/MobiliPresenter2D@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, checkout detached limpo.
- Base: `app/styles.css` Git blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`.
- Candidata: `app/styles.css` exato da PR produto #271, Git blob `eb346a41ad91f6dc53875cb954e9018fdc1dd713`.
- Casca comum: `app/ui-theme.css` Git blob `3114bbfe0a67cbdc53757f5f50a0d035559767a6` e demais arquivos do mesmo SHA de `main`.
- Navegador Microsoft Edge `157.0.4341.46`, DPR 1; viewports 390×900 e 1366×900 CSS px.
- Cada combinação base/candidata × tema claro/escuro × viewport foi aberta num contexto novo. `localStorage[casa-ui-theme-mode-v1]` foi definido antes da navegação. A captura aguardou `data-published-configuration-status=validated` e registrou o valor solicitado, `documentElement.dataset.theme`, `CASA_UI_THEME.getResolved()` e o SHA-256 do screenshot.
- O DOM real de `/config/` foi carregado a partir do checkout; a configuração Buyer V5 foi projetada localmente a partir dos defaults versionados. Playwright roteou as requisições para os arquivos locais; não houve serviço externo, Netlify, banco, autenticação nem escrita no produto.

## Resultados CSSOM

Todos os oito casos registraram tema solicitado = tema do documento = tema resolvido pela API, configuração `validated`, zero exceções de página e um 404 para a bundle privada ausente.

| Viewport | Tema | Braço | `#viewerHint` / footer | `.config-section > h3` | Screenshot | SHA-256 |
|---:|---|---|---|---|---|---|
| 390×900 | light | base | `rgba(255,255,255,.42)` | `rgba(255,255,255,.58)` | [JPEG](g2-configurator-recapture-2026-11-11/baseline-light-390.jpg) | `77b959c3c46883fd1dd97c49efc422b91b26a9891365a0ed06afd4d5b3618b1b` |
| 390×900 | light | candidata | `rgb(112,108,102)` | `rgb(34,33,31)` | [JPEG](g2-configurator-recapture-2026-11-11/candidate-light-390.jpg) | `b4a3af123d3bf3dcc5bc9086a2d8c5a56612aa9ebe1efa93f0b3e81727a3230c` |
| 390×900 | dark | base | `rgba(255,255,255,.42)` | `rgba(255,255,255,.58)` | [JPEG](g2-configurator-recapture-2026-11-11/baseline-dark-390.jpg) | `02f68cde2f79db6145cefd7b980c8d850dc0799c328594a809407d8170c15dab` |
| 390×900 | dark | candidata | `rgba(255,255,255,.48)` | `rgb(244,241,235)` | [JPEG](g2-configurator-recapture-2026-11-11/candidate-dark-390.jpg) | `0089c788271040f0aed098e061279bdbb966630ef0d8363891f223a222e04bbe` |
| 1366×900 | light | base | `rgba(255,255,255,.42)` | `rgba(255,255,255,.58)` | [JPEG](g2-configurator-recapture-2026-11-11/baseline-light-1366.jpg) | `44adaadbcbb4bedd741c52893cb4dbddcd7f807f93d71008bc27a8dec30d0975` |
| 1366×900 | light | candidata | `rgb(112,108,102)` | `rgb(34,33,31)` | [JPEG](g2-configurator-recapture-2026-11-11/candidate-light-1366.jpg) | `aeb862fde0351fffb440a18984fecd251316dae005d0b1bb109c40c149d988e7` |
| 1366×900 | dark | base | `rgba(255,255,255,.42)` | `rgba(255,255,255,.58)` | [JPEG](g2-configurator-recapture-2026-11-11/baseline-dark-1366.jpg) | `d38905c7ae1922e2ea637a2cff1d7578ef1687b3a5707cf951aeb21e03c9d0a9` |
| 1366×900 | dark | candidata | `rgba(255,255,255,.48)` | `rgb(244,241,235)` | [JPEG](g2-configurator-recapture-2026-11-11/candidate-dark-1366.jpg) | `c006b6a3db2e42a1d54cacc269d8ee20b1b541befe41a3fb6f7b9cea138d4c7e` |

## Interpretação e limites

O CSS candidato aplica os tokens existentes: no tema claro, a dica do Viewer e os títulos deixam de herdar cores brancas translúcidas; no tema escuro, permanecem claros sobre as superfícies escuras. O resultado confirma a reprodução e o pareamento dos alvos visíveis, sem introduzir uma paleta nova.

O 404 de `/core/private-navigation.bundle.js` ocorreu em cada contexto porque o bundle não existe no checkout sem build. Não houve exceção JavaScript e a configuração local validou; este subgate não cobre navegação privada nem autenticação. A captura mostra o estado inicial de Módulos, portanto não mede o anel de acabamento selecionado. A página hospedada `/config/` continua sem configuração publicada válida. Os 98 pares `UNCERTAIN`, as demais evidências de #208/#216 e o escopo DS-05A permanecem pendentes; G2 segue em andamento.

O recibo detalhado está em [`result.json`](g2-configurator-recapture-2026-11-11/result.json), com caminhos relativos aos oito screenshots. O registro antigo de 2026-11-11 descreve a divergência original e permanece como histórico; esta recaptura é a evidência posterior associada aos oito hashes acima.

