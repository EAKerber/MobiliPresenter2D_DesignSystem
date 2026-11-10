# Checkpoint atual da arquitetura G0–G8 — 2026-11-09

**Escopo:** reconciliação documental do plano de consolidação de Design System, CSS e componentes. Este checkpoint atualiza a fotografia operacional, não aprova mudanças visuais, migrações em lote, merge de código de produto ou publicação.

**Plano de referência:** [Plano diretor G0–G8](../../docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · [reconciliação anterior](master-plan-g0-g8-current-crosswalk-2026-10-25.md) · [handover e governança](../../docs/HANDOVER_CURRENT.md).

## Evidência verificada nesta retomada

- Design System: `main@79db735d6f05177b0c406e383d35832f3d72fdef` (último commit observado: 2026-10-27). Na leitura anterior à criação desta PR havia **1 branch e 0 PRs**; após sua abertura, a observação live é **2 branches e 1 PR aberta (#119)**.
- O workflow agendado [Branch hygiene #42655241742](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/42655241742) terminou em **success** em 2026-11-09. O endpoint de rulesets ainda lista ativo o ruleset #25953910 para `ds-history/2026-10-27/*`. O último readback documental confirma oito tags históricas protegidas; esta retomada não reenumerou individualmente seus objetos. Nenhuma branch foi removida nesta retomada.
- Produto: `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, **2 branches remotas** e **0 PRs abertas**. Foram lidos somente os refs e estados das issues necessários para atualizar o mapa; nenhum arquivo ou serviço do produto foi alterado.
- Issues observadas no repositório do produto: **#208, #216, #218 e #232 abertas**; **#217, #224 e #226 encerradas**. Isso corrige fotografias mais antigas que ainda listavam #217/#224/#226 como pendentes. Fechamento de issue não equivale a auditoria ampla ou aceitação de release.

## Estado operacional das fases

| Fase | Estado nesta retomada | Próximo gate verificável |
|---|---|---|
| **G0 — evidência e documentação** | **PASS como base de rastreabilidade; contínuo.** O handover local de 06/11 registra G0 PASS; esta retomada atualiza HEADs/issues live, mantendo os snapshots datados. | Continuar reconciliando mapas por domínio sem reescrever evidências históricas nem promovê-las automaticamente. |
| **G1 — navegação e foco** | **PARCIAL.** O foco UX-04 passou no gate dedicado em `development@65f2f3e` (#40802466253); o código atual `development@1a69ff76` ainda contém a restauração pelo ID canônico `section:handles`. O run exato do HEAD atual (#42720598449) passou 124 cenários NAV-004/005, mas não é o gate UX-04. #218 continua aberta; #224/#226 estão fechadas. | Revalidar UX-04 no HEAD atual, fechar #218 com evidência específica e completar os cenários de teclado, touch, zoom e dispositivo real que faltam. |
| **G2 — CSS e acessibilidade** | **EM ANDAMENTO.** #208 e #216 continuam abertas; #217 está fechada. Um subgate CSSOM local recente em `/config/` encontrou zero pares computáveis abaixo do limiar nos seis estados iniciais avaliados, mas manteve **98 candidatos UNCERTAIN** por `backdrop-filter`. | Reconciliar esse resultado com a fonte, pin e recibos; cobrir os estados/rotas ausentes e resolver incertezas. Não inferir conformidade global ou autorização para tokenização. |
| **G3 — ownership CSS/DOM** | **PARCIAL.** Existem mapas estáticos, traces e propostas ARC-13, mas proposta contextual e semelhança lexical não provam ownership nem equivalência. | Fechar ownership por consumidor real, folha carregada, cascata, estado, tema e origem do token antes de qualquer extração. |
| **G4 — foundations, tokens e acessibilidade compartilhável** | **HOLD.** Fonte de referência e decisões aprovadas não demonstram integração abrangente; o handover local de 06/11 mantém G4 em HOLD. | Retomar somente após resolver as incertezas visuais/runtime de G2/G3 e definir o consumidor autorizado. |
| **G5 — famílias de componentes CSS** | **PARCIAL na candidata; HOLD na baseline.** O handover local de 06/11 mantém probes/famílias e incertezas sem consolidação homologada. | Fechar associação de probes e incertezas por família e obter comparação funcional/visual antes de compartilhar regras. |
| **G6 — composição e arquitetura de páginas** | **HOLD.** A direção Vanilla e ownership por domínio continua documentada; a composição declarativa segue experimental. Evidência local recente mantém G6 em HOLD enquanto G4/G5 e cobertura de domínio não fecham. | Reavaliar um piloto mínimo depois de G1–G5, com autoridade de dados explícita e sem criar framework genérico. |
| **G7 — hardening entre plataformas** | **PENDENTE.** #232 permanece aberta; o crosswalk anterior registra que WebKit headless não substitui Safari/iPad real e que validação autenticada exige fixture autorizada. | Resolver a fixture/CI protegida e completar jornadas críticas sem contornar autenticação. |
| **G8 — aceitação e release** | **NÃO INICIADO COMO RELEASE.** Não há autorização de publicação neste checkpoint. | Somente após revisão humana, integração autorizada, validação na base integrada e readback pós-release. |

## UX-04 — foco após redesenho do puxador

A varredura dos subdiretórios localizou o relatório de trabalho `docs/work/DEVELOPMENT_UX04_GEOMETRY_FOCUS_2026-10-28.md`. O gate dedicado mais recente verificado no GitHub é [#40802466253](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40802466253), **success** no SHA `65f2f3ec781b7c36e3198159b7a512f1d26c97a4`; ele cobriu geometria nos perfis V5, restauração de foco e a suíte completa de teclado. O HEAD remoto atual de `development` é `1a69ff76a5f36e3245a288773bb409aa662e4e62`; a leitura da fonte confirma a chamada de retorno ao foco com `section:handles`. [O run exato deste HEAD](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/42720598449) passou 124 cenários públicos NAV-004/005, que são outro gate. Não há readback do gate UX-04 nesse SHA, então a correção está presente, mas sua revalidação no HEAD atual permanece pendente.

UX-04 é o foco do Configurador após redraw; a issue #218 é a geometria/contrato NAV-005 do cabeçalho público. São gates distintos e não devem ser tratados como resolvidos um pelo outro.

## Limites do subgate CSSOM local DS-05A

O material local de 2026-11-09 registra: regressão de oito fixtures PASS; inicialização real do Configurador em seis estados de `/config/` (390/1050/1366 CSS px × light/dark); 70–74 candidatos de texto por estado sem pares computáveis abaixo do limiar; 98 pares no total mantidos como **UNCERTAIN** por `backdrop-filter`. Um ajuste local dos números dos módulos em light está **não commitado** no checkout de auditoria.

A fonte está em `work/MobiliPresenter2D-dev-static-1a69ff7/docs/design-system/DS05A-static-css-provenance-development-1a69ff76.md` no ambiente desta retomada. O checkout está sujo. A identidade local foi conferida nesta retomada:

| Artefato local | SHA-256 |
|---|---|
| Relatório de proveniência DS-05A | `7c639f7ac39658f06f931c5baa43222de6e24a8efb6c14056d2c4a1adfab6480` |
| Recibo `runtime_cssom.json` (228.554 bytes) | `aad1f18832d988d13ed635216a91db2eeeb3f5f1cb8fce9bb004131828bb1291` |
| Runner `theme_cssom_runtime_v1.cjs` | `27c923948a20e896c8fc59e013523b4baebacbd4e6450f19a738855fe78b48da` |
| Teste de fixtures `test_cssom_v2.cjs` | `3b05d9a06e562816864ca94f9228d397d650f95d142c07ac4745f6810ef9501e` |
| `app/ui-theme.css` local modificado | `5b11afd500f8545d723a87b22f586c2c8f42e4f9b4fc22f4e953e96da4ae0545` |

Esses hashes identificam os objetos existentes no checkout; não comprovam por si só o método de geração, compatibilidade com o pin remoto ou revisão do patch. O runner, o recibo e a mudança de CSS continuam fora do repositório Design System; por isso o resultado ainda não é evidência reproduzível nele. O escopo é somente o DOM inicial montado de `/config/`; não cobre Admin, teclado, foco, hover/seleção/erro/loading/dock, tema `auto`, 320/768 px, screenshot review ou dispositivo real. **DS-05A permanece INCOMPLETO/HOLD.** Não promover o ajuste local para produto nem inferir aprovação visual.

## Higiene de branches e limite de quantidade

Os limites leves informados pelo usuário são até 2 branches no Design System e até 5 no produto. Após abrir a PR #119, a observação atual encontrou **2 branches e 1 PR aberta** no Design System, e **2 branches e 0 PRs abertas** no produto. Ambos permanecem dentro dos limites; nenhuma remoção é necessária para respeitá-los. O procedimento do produto exige observação completa, plano com hash, reobservação, exclusão somente por SHA/lease quando elegível e readback integral. Nomes, idade, número de diretórios locais ou fechamento de PR não autorizam remoção. Os oito DAGs históricos do Design System estão sob tags protegidas conforme o último recibo; preservar essa retenção.

## Sequência de trabalho

1. Incorporar a fonte e os recibos do subgate DS-05A de modo reproduzível, preservando que o ajuste permanece local.
2. Retomar G1/G2 com #218, #208, #216 e o gate DOM/runtime DS-05A, sem ampliar o escopo visual.
3. Concluir ownership de G3 por rota/estado e selecionar um único piloto autorizado para G4/G5.
4. Reavaliar a arquitetura declarativa G6 após evidência dos componentes e manter G7 como gate para jornadas protegidas/dispositivos.
5. Atualizar este crosswalk com SHAs e resultados quando cada gate tiver evidência; não marcar G8 concluído sem validação integrada e autorização de release.
