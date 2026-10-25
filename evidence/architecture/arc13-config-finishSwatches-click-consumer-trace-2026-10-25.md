# ARC-13 — rastreio do clique em `finishSwatches`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; rota `/config/`.

## Consumer

O listener delegado encontra o botão mais próximo com `data-finish-id`; sem esse alvo, não faz nada. Para um swatch encontrado, grava a seleção global de acabamento, sincroniza a visibilidade das camadas e anuncia “Cor das frentes atualizada para o conjunto.” em `#configurationAnnouncement[aria-live="polite"]`.

O texto é confirmação de ação global. O consumer não inclui nome de acabamento nem depende dele; a identidade escolhida fica no estado. O anúncio é incondicional após a chamada, mesmo se a seleção já corresponder ao mesmo id.

## Distinção dos consumers próximos

O acabamento local é tratado por outro listener delegado em `moduleDetail`, que valida escopo e módulo e anuncia aplicação somente ao módulo selecionado. Não compartilhar a frase global com o consumer local: escopo e resultado são diferentes. Labels do swatch também são gerados por `renderFinishControlsFromData`, separados deste anúncio de resultado.

## Limites

Rastreio estático de listener, estado, sincronização e live region; sem runtime/AT, leitura da configuração publicada ou confirmação de repetição do mesmo swatch em produção. Nenhuma chave foi proposta; produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
