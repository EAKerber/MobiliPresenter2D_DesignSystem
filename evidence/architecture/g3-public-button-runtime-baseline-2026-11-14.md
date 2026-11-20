# G3 — baseline CSSOM de CTAs públicos — 2026-11-14

## Objetivo e proveniência

Registro de ownership e comportamento computado dos links de ação em Home, Sobre e Como funciona. A coleta usou o HTML/CSS local efetivo do Produto em um servidor vinculado somente a `127.0.0.1`; o HTML/CSS da árvore `app` coincide com Product `main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7`.

- Commit do Product main: `bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7`.
- Árvore `app`: `fb4cdea0f1c7ea317e9d85fcd01df89144d3b294`.
- Checkout local observado: `work/arc13-ui-inventory-20261112@4c02f5405805d1a1bfc6a8547eaf3c9c228bf053`; árvore `app` igual à main.
- Blobs HTML/CSS estão registrados no [recibo JSON](g3-public-button-runtime-baseline-2026-11-14.json).

## Cobertura e método

Foram observados 3 percursos (`/`, `/about/`, `/how-it-works/`) em 2 larguras (1366×900 e 390×844) e 2 temas, totalizando 12 estados base e 32 elementos. Foram medidos estilos computados, dimensão, nome acessível, destino e ordem/quantidade de regras das folhas CSS carregadas.

Quatro famílias representativas foram avaliadas em hover e foco visível, em tema claro e escuro: CTA do cabeçalho, botão preenchido escuro da Home, link textual da seção de história e botão cobre. São 16 estados de interação. O foco foi ativado com `focus({focusVisible:true})` e conferido via `:focus-visible`; isso verifica o estilo, não a sequência real de Tab. Hover aguardou a transição estabilizar.

O navegador foi Chromium 156 no Windows, com redução de movimento emulada. O atributo `data-theme` foi definido diretamente para selecionar os estilos já existentes; o alternador de tema não foi operado. O recibo JSON contém as observações completas.

## Ownership observado

| Uso | Fonte HTML | Proprietário principal |
|---|---|---|
| CTA do cabeçalho | `app/index.html:22`, `app/about/index.html:13`, `app/how-it-works/index.html:22` | `app/landing/landing.css:32–34` |
| Botão preenchido da Home | `app/index.html:32` | Base `landing.css:57–58`; variante escura `:59–60` |
| Link textual da Home | `app/index.html:49` | `landing.css:128–131` |
| Botões cobre | `app/about/index.html:24`, `app/how-it-works/index.html:31,234` | `landing.css:34,61` |
| Foco visível | compartilhado | `app/public-theme.css:23`; cores de tema em `app/ui-theme.css:105–114` |

A ordem de folhas foi preservada por rota no JSON, junto com a quantidade de regras CSSOM carregadas.

## Resultados

- O mesmo `.header-cta` aparece nas três rotas. Em 1366 px mede 176×42 px. Em 390 px mede 38×38 px, oculta os spans de texto e conserva `aria-label="Fale conosco pelo WhatsApp"`.
- As ações preenchidas compartilham base de tamanho, tipografia, raio e foco, mas há variantes por classe. O botão escuro da Home usa fundo claro-escuro `#22211f` e passa para `#080808` no hover claro; em dark usa `#6e512e` e passa a `#8b6a40`. Os botões cobre partem de `#8b6a40` e passam a `#6e512e` no hover.
- Há uma divergência contextual no efeito hover: em Sobre, `.button-copper` sobe 2 px; na Home, o fundo do `.button-dark` muda, mas o transform computado continua identidade apesar da regra de hover solicitar `translateY(-2px)`. O DevTools mostra a animação `public-reveal` concluída, com `fill: both`, mantendo posse do transform. A regra de hover está ativa, porém a animação ocupa a mesma propriedade.
- O CTA textual da Home tem estilo e hover próprios: fundo transparente, peso 750 e nenhuma mudança de cor observada ao passar o mouse. Mantê-lo separado da família preenchida pode ser intencional; isso não foi inferido como erro.
- A regra-fonte de foco declara contorno e afastamento de 3 px. O CSS computado no Chromium desta sessão resultou em 2,66667 px após estabilização, nas amostras de foco. O JSON conserva valores medidos e fontes declaradas.

## Pendências de decisão

- **P2 — hover do hero:** decidir se o deslocamento de 2 px deve coexistir com a animação de entrada ou se o feedback intencional é somente a troca de cor. A evidência atual identifica a colisão de propriedade, mas não determina a intenção de design.
- **P2 — link textual:** decidir se a aparência separada e a ausência de mudança de cor no hover são uma distinção intencional ou se deve haver um feedback mais evidente. O estado de foco permanece visível.

## Limites

- Baseline local estática, não é captura de produção nem de Deploy Preview.
- Não houve validação em leitor de tela, percurso real por teclado, dispositivo físico, Safari/iPad ou multiplataforma.
- Os alvos são links; estado desabilitado não se aplica.
- A captura PNG pelo Chrome DevTools excedeu o tempo limite; o CSSOM JSON é o artefato verificável desta passagem.
- Sem alteração de arquivos UI do Produto e sem execução de suítes de aplicação.

**Resultado:** subgate G3 de ownership de botões públicos tem baseline CSSOM; G3 permanece parcial. Esta evidência não aprova decisão visual nem extração CSS.
