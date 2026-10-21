# Plano geral e etapa atual do Design System — 2026-10-21

**Estado:** plano de trabalho e checkpoint; não homologa decisões visuais novas nem autoriza implementação no produto.  
**Fonte canônica de decisões:** [`decisions.json`](../decisions.json).  
**Repositório do produto:** [`EAKerber/MobiliPresenter2D`](https://github.com/EAKerber/MobiliPresenter2D).

## Objetivo

Tornar a interface visualmente coerente e verificável, preservando diferenças de domínio entre Landing, Viewer, Configurador, Administração e Acesso. Mapear antes de generalizar; aplicar somente decisões homologadas e rastreáveis ao componente, rota, tema, estado e evidência.

## Etapa atual — evidência runtime e fechamento do inventário visual

O inventário estático inicial está registrado em [`VISUAL_INVENTORY.md`](../VISUAL_INVENTORY.md), [`visual-inventory.json`](../visual-inventory.json) e [`DECISION_APPLICATION_MAP.md`](../DECISION_APPLICATION_MAP.md). Ele cobre as rotas e famílias documentadas, classes/folhas CSS, cores, espaçamentos, tipografia, breakpoints, movimento e assets. É um mapa de código, não uma certificação do DOM dinâmico.

A auditoria pública G1 foi registrada e integrada pela [PR #45](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/45). Em produção, o painel econômico de “Como funciona” passou nos estados amostrados; a Landing reproduziu em 4/4 uma divergência entre ambiente selecionado e página do carrossel no viewport 390×844. O defeito permanece aberto no [issue #224 do produto](https://github.com/EAKerber/MobiliPresenter2D/issues/224); a causa técnica ainda não foi isolada. Movimento reduzido, animação ativa, rede lenta e falha de imagem seguem sem verificação. Ver [`RUNTIME_AUDIT.md`](../RUNTIME_AUDIT.md) e [`runtime-evidence.json`](../runtime-evidence.json).

O registro de foco foi alinhado à paleta já aprovada pela [PR #47](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/47): contorno claro/escuro `#8B6A40` / `#D8BC7C`, 4 px com offset 3 px. Aplicação por componente, visibilidade em teclado, recorte e fundos reais continuam pendentes; não são tokens globais nem autorização de implementação.

### Próximos trabalhos desta etapa

1. Atualizar evidências visuais de cabeçalhos cujo material persistido pertence a versões anteriores; cobrir rotas públicas e a tela de login sem sessão em temas e larguras representativas, sem persistir dados de conta.
2. Completar verificações públicas de teclado, movimento reduzido, animações e estados de carregamento/erro em imagens; separar limitações de ferramenta de falhas do produto.
3. Revalidar no DOM temas, superfícies e estados dinâmicos dos achados visuais. Medir contrastes efetivos com transparência/ancestrais e registrar cada caso como aprovado, falha, exceção ou não verificado.
4. Fazer uma sequência autenticada controlada para FIND-007 / issue #213 somente quando o usuário estiver conectado na sessão de produção: menu após login sem recarga, navegação privada, nova aba e saída. Não registrar email, credenciais, tokens ou dados de convite.
5. Revisar cobertura de todos os itens do inventário e encerrar a etapa quando cada rota/família estiver ligada a evidência atual ou explicitamente marcada como não verificada.

## Critério para homologar conformidade

Um item só fica conforme quando seu papel semântico e par de cores estão aprovados para a superfície/tema/estado, o DOM real corresponde ao par, contraste e indicação não cromática atendem aos critérios registrados, interação e teclado funcionam nos estados pertinentes, e as rotas/breakpoints cobertos têm evidência. Um valor existente no CSS não vira token por isso. Ver [`PALETTE_CONFORMANCE.md`](../PALETTE_CONFORMANCE.md).

## Sequência futura

1. **Concluir inventário visual e evidência runtime.** Registrar classes, cores, breakpoints, animações, microinterações, espaçamentos, assets, estados e rastreabilidade. Tratar defeitos como achados separados; não alterar CSS para mascarar comportamento.
2. **Homologar os valores e padrões que ainda dependem de escolha.** Exibir comparações identificadas como experimentais apenas quando as decisões existentes não definirem uma solução. Persistir aprovações e limites em `decisions.json`.
3. **Fundação visual e aplicação gradual.** Organizar apenas tokens aprovados e aplicar por família de componentes no produto. Confirmar diferenças de comportamento antes de reduzir duplicações; executar DOM, interação e revisão visual por PR. Usar preview quando integração comportamental ou risco de efeito em cadeia justificar.
4. **Schema de interface data-driven (futuro).** Projetar schema próprio para estrutura da interface, separado dos dados do configurador e da configuração de etapas. Não mover HTML, CSS, handlers ou lógica arbitrária para dados de cliente.
5. **Textos e tradução (futuro).** Separar conteúdo textual da estrutura visual depois da fundação de interface. Preservar Português do Brasil; escolher estratégia de idiomas quando essa etapa começar.
6. **Inventário completo de JavaScript (futuro posterior).** Mapear módulos, funções, eventos, fluxos e dependências depois do foco visual; usar o mapa para orientar mudanças data-driven, sem ampliar a etapa atual.

## Organização e governança

- `decisions.json` é canônico para decisões. Mapa de aplicação, inventário, auditoria, evidência e laboratório mantêm responsabilidades separadas.
- Cores ou medidas observadas permanecem “uso atual” até homologação explícita.
- VIS-001 e CMP-001 permanecem pendentes onde o conteúdo ou a decisão não foi recuperado; GOV-001/NAV-001/NAV-002 têm lacuna de origem encerrada como não recuperável, sem reconstruir conteúdo.
- PR #39 permanece draft e não deve ser integrada em bloco: está divergente, tem 25 arquivos e combina atualizações documentais com experimentos/workflows. Se partes forem aproveitadas, criar mudanças focadas sobre a `main` atual e reconciliar seus estados com este checkpoint.
- O checkout local do produto está sujo. Qualquer implementação futura deverá usar um checkout isolado e preservar as alterações locais existentes.
- Nenhuma PR ou preview deve ser tratado como decisão estética ou como autorização de publicar produção.
