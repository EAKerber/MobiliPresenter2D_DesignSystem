# ARC-13 — rastreio de clicks em `moduleDetail`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Dois listeners, dois resultados

- **Aplicar acabamento local:** o click só prossegue se a configuração ainda estiver habilitada, for de escopo local e incluir o módulo do botão. Atualiza acabamento daquele módulo, sincroniza camadas e anuncia `Acabamento aplicado somente ao módulo selecionado.`.
- **Fechar ficha:** o listener delegado reconhece apenas o botão `data-close-module-detail`, guarda a origem de foco, limpa a entidade selecionada, sincroniza visibilidade, anuncia `Detalhes do módulo fechados.` e restaura foco para a origem.

Clicks nas setas de navegação são tratados no mesmo listener de fechamento, mas retornam antes do ramo close; a navegação não anuncia este texto de encerramento. Ambas as mensagens são feedback no live region polite e representam ações distintas.

## Limites

Rastreio manual dos listeners e guardrails; sem runtime/AT. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` não foram alterados.
