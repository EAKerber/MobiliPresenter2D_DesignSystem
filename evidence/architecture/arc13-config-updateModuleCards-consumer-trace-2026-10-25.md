# ARC-13 — rastreio de `updateModuleCards`

**Data:** 25/10/2026  
**Fonte:** `EAKerber/MobiliPresenter2D/app/app.js`, `main`, blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; mesmo blob registrado no mapa ARC-13. Consumer: cartões de módulos em `/config/`.

## Consumers e estados

- **Controle bloqueado por evento:** quando há regra ativa para a entidade, o checkbox fica desabilitado e recebe o tooltip `Controlado por um evento da configuração.`; o nome acessível e `aria-describedby` permanecem tratados no renderer/listener do cartão.
- **Status de inclusão:** texto visível é escolhido pelo estado resolvido: `Incluído` quando visível, `Não incluído` quando fora da composição, ou `Requer suporte incluído` quando o motivo é `requirement-hidden` ou `requirement-missing`.
- **Relação acessível:** o status fica em um `<small>` dentro do cartão; quando bloqueado, o checkbox aponta para esse elemento via `aria-describedby`. O botão de abrir detalhes atualiza `aria-expanded` de acordo com a ficha selecionada.

O renderer atualiza classe visual selecionada/bloqueada/incluída e mantém dimensões calculadas para a configuração. O texto de status não substitui as ações nem altera seleção; o toggle continua sincronizado com o estado efetivo, com override de evento aplicado.

## Limites

Rastreio manual do estado resolvido e DOM, sem runtime/AT. A frase de bloqueio reúne dois motivos de dependência; a tradução deve conservar que o módulo exige suporte incluído. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` não foram alterados.
