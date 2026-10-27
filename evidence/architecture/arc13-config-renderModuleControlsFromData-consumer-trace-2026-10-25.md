# ARC-13 — rastreio de `renderModuleControlsFromData`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`. O blob coincide com o registrado no mapa ARC-13; o escopo verificado é `startConfigurator > renderModuleControlsFromData`, em `/config/`.

## Consumers

- **Checkbox do módulo — `Incluir ${product.title}`:** rótulo acessível do controle de seleção. O título é dado dinâmico do catálogo; a visibilidade inicial vem do estado efetivo, após regras de eventos.
- **Tooltip do checkbox — `Controlado por um evento da configuração.`:** só é definido quando há regra ativa `set-enabled` para aquele módulo. Nesse ramo o checkbox fica desabilitado; sem override, o atributo `title` é esvaziado. O texto explica por que a alteração direta não está disponível.
- **Botão de detalhes — `Ver detalhes de ${product.title}`:** nome acessível de botão que seleciona o módulo e controla `#moduleDetail`; o título também aparece visualmente no cartão junto às dimensões. Título e dimensões são dados dinâmicos do catálogo/configuração, não copy estática desta ocorrência.

O renderer só cria cartões para entidades controláveis, módulos configurados que existem no catálogo e produtos encontrados. Assim, os dois rótulos acessíveis compartilham o mesmo parâmetro de título do catálogo, mas representam ações distintas (selecionar e abrir detalhes). Sua eventual chave precisa manter ambos os consumers e o parâmetro; igualdade parcial de template não os funde automaticamente.

## Limites

Rastreio manual de fonte e fluxo de estado, sem teste de runtime ou AST. Nenhuma chave foi proposta; catálogo, código do produto, índice e `decisions.json` permanecem inalterados. O bucket não determina política de tradução dos nomes de produto.
