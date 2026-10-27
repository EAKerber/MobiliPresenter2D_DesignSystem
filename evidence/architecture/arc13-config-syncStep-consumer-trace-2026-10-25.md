# ARC-13 — rastreio de `syncStep`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Rota `/config/`.

## Consumer e estados

A função mostra o painel correspondente à etapa ativa, atualiza `aria-current="step"` nos botões de navegação e atualiza o texto do CTA principal:

- Em resumo: `Editar {primeira etapa}`.
- Nas demais etapas: `Continuar para {próxima etapa} →`.

Os rótulos vêm da configuração habilitada do fluxo, convertidos para minúsculas em `pt-BR`. A lista é circular: o passo seguinte ao último retorna à primeira etapa. O texto visível é também o nome acessível do botão; não existe label ARIA separado neste consumer.

## Limites

Rastreio manual da navegação e do fluxo normalizado, sem runtime. Nome de etapa é dado configurável/parâmetro; pluralização não se aplica. Nenhuma chave foi proposta; produto, configurações, índice e `decisions.json` permanecem inalterados.
