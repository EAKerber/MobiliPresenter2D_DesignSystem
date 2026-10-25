# ARC-13 — rastreio do clique em `restoreButton`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; rota `/config/`.

## Consumer e confirmação

O listener do botão executa `global.confirm` com a pergunta “Recomeçar a configuração? Suas escolhas atuais serão removidas.” Se o usuário cancelar, o handler retorna sem alterar o estado. Se confirmar, recria o estado inicial com `core.createInitialState(scene)`, oculta o alinhamento visual, limpa `detailOrigin` e sincroniza a visibilidade das camadas.

O texto é uma confirmação de ação com efeito destrutivo para as escolhas da sessão atual. Não contém parâmetro dinâmico nem representa o estado de carregamento. O handler não muda `currentStep` explicitamente; confirmar com o owner se “recomeçar” promete também voltar à primeira etapa antes de propor uma chave ou ajustar o texto.

## Limites

Rastreio estático do listener e do efeito imediato; sem runtime, confirmação do escopo de persistência ou revisão de conteúdo pelo owner. Nenhuma chave foi proposta; produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
