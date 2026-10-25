# ARC-13 — rastreio de `createLocalFinishControl`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer na ficha do módulo, rota `/config/`.

## Consumers e guardrails

- A legenda `Acabamento deste módulo` nomeia o fieldset local e só aparece se houver ao menos um acabamento publicado, habilitado, de escopo local e associado ao módulo.
- O tooltip usa o nome público do acabamento; o nome acessível do swatch combina a ação `Aplicar`, o acabamento e o título do produto, seguido de `somente em`. Os dois nomes vêm de catálogo/produto, enquanto a gramática descreve aplicação local.
- `aria-pressed` comunica o acabamento selecionado para aquele módulo. O handler valida que o acabamento ainda está habilitado, é local e pertence ao módulo antes de mudar estado; depois anuncia a aplicação local (bucket de evento distinto).

A opção global está fora deste fieldset; não misturar o escopo de aplicação ou seu estado com os swatches globais.

## Limites

Rastreio manual de renderer/handler, sem runtime/AT. Os dados editoriais de acabamento e o título do produto são parâmetros. Nenhuma chave foi proposta; código, catálogo, índice e `decisions.json` não foram alterados.
