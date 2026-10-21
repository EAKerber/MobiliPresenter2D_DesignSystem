# Status efetivo — main do produto, 21/10/2026

**IMPLEMENTADO E PUBLICADO COM AUTORIZAÇÃO PADRÃO OFF:** [MobiliPresenter2D `main@026f04aa`](https://github.com/EAKerber/MobiliPresenter2D/commit/026f04aa88beae41d1242288421b658670d048d4). [Netlify produção `6ad903c1`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad903c1720d8e369a3954d9) `ready` para esse SHA. Não confundir implementação de opção com **ativação/publicação efetiva de preços**: é necessário uma gravação Admin V5 voluntária e confirmada.

- A versão integrada foi portada **da feature para a main diretamente**, sem incorporar NAV-005 ou outras alterações da PR #230 (continua DRAFT/HOLD).
- Em produção, Admin → Preços oferece o checkbox global para valores base; por contrato ausente/legado=OFF. Viewer com DTO 0.2 negociado mostra apenas `basePriceCents` válido/positivo quando ON for publicado. Leitores antigos 0.1 seguem sem preços.
- [Gate isolado #39652058042](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39652058042) PASS e [gate main #39652406203](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39652406203) PASS; build e variant fidelity na main PASS após `test-core.js` ajustar asserções das versões de cache. Gate real de publicar ON/OFF + inspeção anônima continua PENDING; nada foi ativado pelo agente.
- Registro de arquitetura específico da main: [viewer-base-price-publication-main-2026-10-21.md](https://github.com/EAKerber/MobiliPresenter2D/blob/main/docs/architecture/viewer-base-price-publication-main-2026-10-21.md).

O trecho seguinte é o checkpoint **histórico anterior à integração**, preservado para recuperar a pesquisa e a separação da PR #230.

---

# Checkpoint de implementação — publicação opcional de preço base no Viewer

**Data:** 2026-10-21. **Tipo:** registro técnico, não homologação visual e não autorização de release.

## Origem e autoridade

- Produto: [MobiliPresenter2D / issue #228](https://github.com/EAKerber/MobiliPresenter2D/issues/228), autorização do usuário de **um único controle global OFF por padrão**, em Admin → Preços.
- Base visual do Viewer: [NAV-005, profundidade 2](NAVIGATION_DEPTH_AUTHORITY_GATE_2026-10-21.md), sem alterar header aceito.
- Base técnica dependente: PR de integração [#230](https://github.com/EAKerber/MobiliPresenter2D/pull/230) — head `24bbeadba8ec231c8c9f603c4da5116ab8a5ce3e`. Continua DRAFT/HOLD.
- Implementação isolada: branch [`feature/viewer-base-prices-global-off-20261021`](https://github.com/EAKerber/MobiliPresenter2D/tree/feature/viewer-base-prices-global-off-20261021), **head `82e4d09a842d830d80b0b5f19bd5370fe146d57c`** quando este documento foi redigido. A branch **não foi mesclada nem publicada**.

## Implementação (em branch, não em produção)

1. `ConfiguratorAdministration2D 5.0` admite `viewerPricePublication: { enabled: boolean }` com validação estrita. Ausente/legado = OFF. O Admin só torna a autorização efetiva via publicação V5 já existente, com sessão admin, validação, ETag e readback.
2. Admin → Preços ganhou checkbox global “Mostrar preços base no Viewer”, com aviso explícito de que o estado do checkbox é rascunho até **Publicar configuração**. Sem flag individual por módulo.
3. `pricing.roles.itemBase[moduleId]` permanece fonte exclusiva. Regra final em centavos, `type:amount`, positiva e dentro do contrato comercial. Regra zero, ausente, inválida ou módulo oculto = campo de preço omitido; não sintetizar base.
4. `PublicModulePresentation2D 0.1`: HTTP não contém preço. Em publicação habilitada, `0.2` acrescenta apenas `basePriceCents` para módulos elegíveis e visíveis, nunca `priceBook`, margens, custos, regras ou flag administrativa.
5. Compatibilidade: Viewer novo envia `X-Public-Modules-Version: 0.2` e aceita 0.1 ou 0.2. Viewer antigo sem header recebe 0.1 sem preço mesmo que a publicação permita DTO 0.2. O header negocia **formato**, não autorização.
6. Viewer mantém dimensões no canto inferior esquerdo, e usa o campo escalar autorizado para apresentar “Valor base do módulo” com BRL no inferior direito do mesmo footer. A seleção do módulo controla a leitura, sem calcular serviços/opções.
7. Endpoint usa `no-store` e Blob strong; desligar e republicar elimina campo público a partir da próxima leitura. Preview sem documento próprio só reutiliza DTO público da origem, nunca documento administrativo. Revogação antes de republicar não foi implementada.

## Evidência e gates

- [Actions #39646570942](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39646570942): **PASS** testes de projeção ON/OFF, autorização V5, roundtrip ETag, regressões V5 e build bundle.
- [Actions #39646860625](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39646860625): **PASS 16/16 navegador** Chromium/WebKit × 390/1366 × claro/escuro × ON/OFF, dados sintéticos; sem Deploy Preview.
- O novo gate com negociação de versões está [neste workflow](https://github.com/EAKerber/MobiliPresenter2D/actions/workflows/viewer-base-price-contract-gate.yml); resultado do head `82e4d09` deve ser lido após conclusão, não presumido.
- **PENDING:** sessão administrativa real no ambiente de revisão para ligar/desligar e republicar, HTTP público com ON/OFF incluindo cliente legado, inspeção visual humana das capturas, iPad físico/teclado, revogação no redeployment/cache. A PR #230 permanece independente e sem merge.
- **NÃO REALIZADO:** nenhuma publicação de dados reais, merge, criação de nova PR, Deploy Preview adicional ou alteração em produção. A escolha técnica de omitir preço zero é provisória até o gate de release.

## Próxima decisão operacional

A branch parte do head de #230 para preservar seu NAV-005 e evitar conflito mecânico no Viewer. Após fechar o gate de negociação e revisão de fluxo real, decidir se o incremento será integrado **depois** de #230 ou receberá preview próprio, apenas se necessário. Nunca mesclar automaticamente por sucesso de testes isolados.
