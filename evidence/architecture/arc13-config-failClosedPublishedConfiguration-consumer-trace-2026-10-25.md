# ARC-13 — rastreio de `failClosedPublishedConfiguration`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; rota `/config/`.

## Consumer e falha fechada

A rota busca `/api/buyer-configuration` sem cache e com credenciais same-origin. HTTP 422 é convertido em erro interno de configuração inválida; outras respostas não-OK viram erro de indisponibilidade/não autorizado. Falha de rede, JSON ou aplicação das configurações também chega ao mesmo `catch`.

A função registra diagnóstico no console, marca o status publicado como inválido, cria uma mensagem estática com `role="alert"` e oculta/inertiza o workspace. O texto visível “Não foi possível validar a configuração publicada. O configurador está temporariamente indisponível.” cobre todos esses caminhos sem expor detalhe técnico nem diferenciar conteúdo inválido de indisponibilidade.

## Limites

Rastreio estático; nenhum runtime testou as classes de falha nem a leitura por tecnologia assistiva. A unificação parece intencional para falha fechada, mas precisa manter a distinção entre erro de diagnóstico interno e mensagem pública se extraída. Nenhuma chave foi proposta; produto, catálogo, índice ARC-13 e `decisions.json` permanecem inalterados.
