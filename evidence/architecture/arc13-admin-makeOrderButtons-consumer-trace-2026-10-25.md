# ARC-13 — rastreio de `makeOrderButtons`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota Admin.

## Consumer

O helper recebe payloads de ordenação, índice, comprimento e rótulo do item. Cria dois botões icon-only (setas para cima/baixo), atribui tipo `button`, `title` e `aria-label` com as mensagens “Mover {label} para cima” e “Mover {label} para baixo”, desabilita a ação no limite da lista e copia o payload de reordenação para `data-*`.

O mesmo helper é consumido por itens, seções, grupos e etapas da hierarquia. O rótulo é o nome dinâmico correspondente ao item reordenado. A direção e a entidade movida são parâmetros semânticos; `title` e `aria-label` recebem o mesmo texto para cada botão.

## Limites

Rastreio estático do helper e dos quatro tipos de chamada encontrados; sem verificação runtime/AT de nomes lidos nem auditoria do handler que aplica cada payload. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
