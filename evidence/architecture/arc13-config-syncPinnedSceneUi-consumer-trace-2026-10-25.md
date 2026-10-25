# ARC-13 — rastreio de `syncPinnedSceneUi`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer em `/config/`, controles do PiP mobile.

## Consumer e estado

Quando o controle de fixação existe, `mobileScenePinEnabled` define seu estado `aria-pressed` e o texto:

- desfixada: `Fixar cena`;
- fixada: `Liberar cena`.

O mesmo texto é usado em `aria-label` e `title` para nome acessível e tooltip. São dois sinks do mesmo comando/estado, não mensagens de “cena já está dockada”: a cena pode estar fixada mesmo antes de entrar no dock automático.

O estado visual/layout do PiP é aplicado separadamente por classes, dimensões e posição. A transparência tem `aria-pressed`, e a saída do dock restaura foco para o botão de fixação ou navegação da etapa. Os anúncios de confirmação ficam no bucket externo de `startConfigurator`.

## Limites

Rastreio manual de fonte, sem runtime/AT. As duas frases de estado podem compor um único contrato com parâmetro booleano na etapa de proposta, se o owner confirmar que o sentido do rótulo permanece “ação disponível”. Nenhuma chave foi proposta; produto, índice e `decisions.json` seguem inalterados.
