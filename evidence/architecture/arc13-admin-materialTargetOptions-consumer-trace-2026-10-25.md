# ARC-13 — rastreio de `materialTargetOptions`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`; rota `/admin.html`.

## Consumer

O helper alimenta as escolhas de destino para associar materiais. O mapa indexa duas labels: “Pedra e rodapé”, opção estática do grupo `stone-all`, e o prefixo “Puxador · {label}”, aplicado às opções derivadas dos produtos de puxador. O id de destino permanece dado técnico (`stone-all` ou `handle:{id}`) e não deve ser traduzido.

A label “Frentes” existe no mesmo array, mas não consta neste bucket como ocorrência sem chave. Não inferir que a chave esteja ausente. “Puxador ·” aqui classifica uma opção de destino; apesar de repetir o prefixo de `catalogObjects`, o consumer e o papel diferem, então a equivalência de chave precisa de ownership/consumer review.

## Limites

Rastreio estático de construção das opções; sem leitura das configurações publicadas nem teste runtime do Admin. Nenhuma chave foi proposta; catálogo, produto, índice ARC-13 e `decisions.json` permanecem inalterados.
