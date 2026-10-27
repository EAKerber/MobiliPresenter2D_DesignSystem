# ARC-13 — rastreio de `renderServiceChecklist`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumer

O renderer usa a seção de fluxo de serviços vinculada à checklist. O estado marcado vem dos serviços globais efetivos; cada item usa título e descrição do catálogo, com adicional de preço global formatado quando o valor é positivo.

A ocorrência do mapa é o tooltip `Controlado por um evento da configuração.`, aplicado somente quando existe evento ativo que controla aquele serviço. Nessa condição o checkbox desabilita. O mesmo texto aparece em outros controles do Configurador com o mesmo sentido (ação gerida por regra); uma futura chave compartilhada exige confirmar que owner/consumer e contrato continuam comuns. Um serviço com status `included` também fica desabilitado, mas este ramo não define tooltip neste renderer.

## Limites

Rastreio manual de fonte e estado do serviço, sem runtime/AT. Não foram propostas chaves nem alterados produto, catálogo, índice ou `decisions.json`.
