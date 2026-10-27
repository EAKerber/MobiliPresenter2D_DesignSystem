# ARC-13 — rastreio dos anúncios de `startConfigurator`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; `app/config/index.html`, blob `97c284c9831de05607ede0d024e4d919a898b7fa`. Escopo externo do configurador, oito ocorrências em `/config/`.

## Feedback anunciado

Todos os itens abaixo passam por `announce(message)`, que atualiza `#configurationAnnouncement[aria-live="polite"]`:

- **Mini-cena disponível abaixo das etapas:** anunciada quando a cena fixada passa para o dock automático. A mesma frase existe no caminho de refresh e no `IntersectionObserver`; ambos guardam a transição comparando o próximo estado com `mobileSceneIsMini`, de modo que uma transição só seja anunciada uma vez.
- **Transparência:** alternância do controle informa “ativada” ou “opaca” após atualizar a UI.
- **Tamanho do PiP:** o controle cicla entre pequeno, médio e grande e anuncia o tamanho após sincronizar a UI.
- **Puxador global:** a opção de ausência diz que será definida depois; qualquer outra opção anuncia o rótulo dinâmico do catálogo aplicado ao conjunto.

Esses textos são mensagens de estado/ação para leitor de tela, não rótulos visíveis do controle. O anúncio de mini-cena também aparece em um bucket filho, `refreshMobileSceneDock`; identidade textual não basta para compartilhar chave se o contrato de eventos divergir.

## Limites

Rastreio manual de chamadas e do live region; não houve validação com leitor de tela ou teste runtime. Chaves não foram propostas; código, índice, catálogo e `decisions.json` seguem intactos.
