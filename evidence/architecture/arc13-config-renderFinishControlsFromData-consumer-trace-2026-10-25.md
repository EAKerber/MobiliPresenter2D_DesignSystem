# ARC-13 — rastreio de `renderFinishControlsFromData`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumers

- **Tooltip do swatch:** `button.title` recebe `finish.publicLabel` diretamente; é dado editorial do acabamento, não copy fixa.
- **Nome acessível do swatch:** `aria-label` combina o comando `Aplicar … ao conjunto` com `finish.publicLabel`. O comando é copy de interface, enquanto o rótulo do acabamento é dado do catálogo. O botão também expõe o estado de seleção por `aria-pressed`.
- **Descrição do acabamento selecionado:** quando existe acabamento correspondente ao id global ativo, o texto combina o prefixo `Selecionada: ` e a descrição pública do acabamento. O prefixo é interface; o nome continua dado de catálogo. Sem correspondência, o texto é vazio.

O renderer inclui somente acabamentos publicados, habilitados e de escopo global. O clique aplica acabamento global e sincroniza a visibilidade da cena; a mensagem anunciada após a ação fica em outro bucket (`event click on finishSwatches`), não nestas três ocorrências.

## Limites

Rastreio manual de fonte e estado, sem runtime/AST. Os dois fragments estáticos de interface são candidatos distintos por consumer/gramática; `finish.publicLabel` permanece parâmetro de conteúdo. Nenhuma chave foi proposta; catálogo, código, índice e `decisions.json` não foram alterados.
