# Checkpoint atual da arquitetura G0–G8 — 2026-11-09

**Escopo:** reconciliação documental do plano de consolidação de Design System, CSS e componentes. Este checkpoint atualiza a fotografia operacional, não aprova mudanças visuais, migrações em lote, merge de código de produto ou publicação.

**Plano de referência:** [Plano diretor G0–G8](../../docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md) · [reconciliação anterior](master-plan-g0-g8-current-crosswalk-2026-10-25.md) · [handover e governança](../../docs/HANDOVER_CURRENT.md).

## Evidência verificada nesta retomada

- Design System: `main@79db735d6f05177b0c406e383d35832f3d72fdef` (último commit observado: 2026-10-27), **1 branch remota** e **0 PRs abertas**.
- O workflow agendado [Branch hygiene #42655241742](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/42655241742) terminou em **success** em 2026-11-09. O endpoint de rulesets ainda lista ativo o ruleset #25953910 para `ds-history/2026-10-27/*`. O último readback documental confirma oito tags históricas protegidas; esta retomada não reenumerou individualmente seus objetos. Nenhuma branch foi removida nesta retomada.
- Produto: `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`, `development@1a69ff76a5f36e3245a288773bb409aa662e4e62`, **2 branches remotas** e **0 PRs abertas**. Foram lidos somente os refs e estados das issues necessários para atualizar o mapa; nenhum arquivo ou serviço do produto foi alterado.
- Issues observadas no repositório do produto: **#208, #216, #218 e #232 abertas**; **#217, #224 e #226 encerradas**. Isso corrige fotografias mais antigas que ainda listavam #217/#224/#226 como pendentes. Fechamento de issue não equivale a auditoria ampla ou aceitação de release.

## Estado operacional das fases

| Fase | Estado nesta retomada | Próximo gate verificável |
|---|---|---|
| **G0 — evidência e documentação** | **CONTÍNUO.** Plano, decisões e evidências históricas estão preservados. Este checkpoint registra HEADs/issues atuais, mas ainda existem mapas datados que precisam ser reconciliados por domínio. | Manter ponteiros atuais e conservar snapshots datados com seus limites; revisar discrepâncias antes de declarar um mapa autoritativo. |
| **G1 — navegação pública** | **PARCIAL.** #224 e #226 estão fechadas; #218 continua aberta. Os testes de branch/preview do crosswalk de 25/10 não são validação do HEAD atual nem de dispositivo real. | Reabrir somente os cenários ainda pendentes em #218 e os contratos de teclado, foco, zoom, touch e dispositivo real; não usar issue fechada como prova universal. |
| **G2 — CSS e acessibilidade** | **EM ANDAMENTO.** #208 e #216 continuam abertas; #217 está fechada. Um subgate CSSOM local recente em `/config/` encontrou zero pares computáveis abaixo do limiar nos seis estados iniciais avaliados, mas manteve **98 candidatos UNCERTAIN** por `backdrop-filter`. | Reconciliar esse resultado com a fonte, pin e recibos; cobrir os estados/rotas ausentes e resolver incertezas. Não inferir conformidade global ou autorização para tokenização. |
| **G3 — ownership CSS/DOM** | **PARCIAL.** Existem mapas estáticos, traces e propostas ARC-13, mas proposta contextual e semelhança lexical não provam ownership nem equivalência. | Fechar ownership por consumidor real, folha carregada, cascata, estado, tema e origem do token antes de qualquer extração. |
| **G4 — foundations, tokens e acessibilidade compartilhável** | **PARCIAL.** A fonte de referência e decisões aprovadas não demonstram integração abrangente no produto. | Continuar por um consumidor autorizado de cada vez, com escopo pinado, rollback e provas por consumidor. |
| **G5 — famílias de componentes CSS** | **SEM CONSOLIDAÇÃO HOMOLOGADA.** Os experimentos antigos continuam evidência de branch datada. | Exigir contrato comum comprovado, consumidores simultâneos e comparação funcional/visual antes de compartilhar regras. |
| **G6 — composição e arquitetura de páginas** | **DIREÇÃO DOCUMENTADA; ADOÇÃO INCREMENTAL.** HTML/CSS/JS Vanilla e ownership por domínio continuam a direção. O protótipo declarativo não vira framework ou schema de produção por inferência. | Selecionar um piloto mínimo, só depois de gates G1–G5 e com autoridade dos dados explícita. |
| **G7 — hardening entre plataformas** | **PENDENTE.** #232 permanece aberta; o crosswalk anterior registra que WebKit headless não substitui Safari/iPad real e que validação autenticada exige fixture autorizada. | Resolver a fixture/CI protegida e completar jornadas críticas sem contornar autenticação. |
| **G8 — aceitação e release** | **NÃO INICIADO COMO RELEASE.** Não há autorização de publicação neste checkpoint. | Somente após revisão humana, integração autorizada, validação na base integrada e readback pós-release. |

## Limites do subgate CSSOM local DS-05A

O material local de 2026-11-09 registra: regressão de oito fixtures PASS; inicialização real do Configurador em seis estados de `/config/` (390/1050/1366 CSS px × light/dark); 70–74 candidatos de texto por estado sem pares computáveis abaixo do limiar; 98 pares no total mantidos como **UNCERTAIN** por `backdrop-filter`. Um ajuste local dos números dos módulos em light está **não commitado** no checkout de auditoria.

A fonte está em `work/MobiliPresenter2D-dev-static-1a69ff7/docs/design-system/DS05A-static-css-provenance-development-1a69ff76.md` no ambiente desta retomada. Esse checkout está sujo e o recibo/runner são locais: o subgate ainda precisa de reconciliação de hashes/artefatos e não constitui evidência reproduzível no repositório Design System. O escopo é somente o DOM inicial montado de `/config/`; não cobre Admin, teclado, foco, hover/seleção/erro/loading/dock, tema `auto`, 320/768 px, screenshot review ou dispositivo real. **DS-05A permanece INCOMPLETO/HOLD.** Não promover o ajuste local para produto nem inferir aprovação visual.

## Higiene de branches e limite de quantidade

Os limites leves informados pelo usuário são até 2 branches no Design System e até 5 no produto. A observação atual encontrou 1 e 2, respectivamente. Logo, nenhuma remoção é necessária para respeitar os limites. O procedimento do produto exige observação completa, plano com hash, reobservação, exclusão somente por SHA/lease quando elegível e readback integral. Nomes, idade, número de diretórios locais ou fechamento de PR não autorizam remoção. Os oito DAGs históricos do Design System estão sob tags protegidas conforme o último recibo; preservar essa retenção.

## Sequência de trabalho

1. Incorporar a fonte e os recibos do subgate DS-05A de modo reproduzível, preservando que o ajuste permanece local.
2. Retomar G1/G2 com #218, #208, #216 e o gate DOM/runtime DS-05A, sem ampliar o escopo visual.
3. Concluir ownership de G3 por rota/estado e selecionar um único piloto autorizado para G4/G5.
4. Reavaliar a arquitetura declarativa G6 após evidência dos componentes e manter G7 como gate para jornadas protegidas/dispositivos.
5. Atualizar este crosswalk com SHAs e resultados quando cada gate tiver evidência; não marcar G8 concluído sem validação integrada e autorização de release.
