# Reconciliação do plano diretor G0–G8 — 2026-10-25

## Propósito e fonte atual

A PR [#39](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/39) preserva o plano diretor de 20/10 e os gates G0–G8. Ela continua DRAFT e o GitHub reporta `mergeable=false`; não deve ser usada como fotografia atual nem consolidada integralmente sobre a branch vigente.

A PR [#51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51), branch `docs/current-handover-20261024`, contém o handover operacional mais recente e atualizações ARC-13 de 25/10. Este crosswalk atualiza a leitura dos gates antigos à luz dessa evidência; não substitui as fontes canônicas, não muda o produto e não homologa decisões visuais.

## Estado dos gates

| Gate | Leitura atual | Evidência e limite |
|---|---|---|
| G0 — base documental e evidências | **CONTÍNUO / fonte atualizada** | PR #51 e o handover em vigor atualizam sequência, estados e evidências. A PR #39 permanece referência histórica; sua base divergiu. |
| G1 — navegação pública | **PARCIAL / preview** | Há implementações e verificações isoladas em PRs de produto. A consolidação About (#239 → #241) passou nos workflows e no Deploy Preview, mas PR #241 segue DRAFT. Isso não encerra todos os testes de teclado, zoom, dispositivos reais ou fluxos da navegação. |
| G2 — conformidade CSS e acessibilidade | **EM ANDAMENTO** | Issues #208, #216 e #218 permanecem abertas. A #217 foi encerrada após confirmação em Production da correção já mergeada na PR #219 (13,85:1 em faixa opaca). Há outros escopos medidos em revisão; não existe aprovação global de tokens. |
| G3 — ownership e contratos CSS/DOM | **PARCIAL** | Há inventários estáticos e runtime e mapas de consumers; a fila ARC-13 avançou com propostas contextualizadas. Propostas não equivalem a ownership aprovado, migração ou prova completa de todos os estados. |
| G4 — foundations, tokens e acessibilidade compartilhável | **PARCIAL / integração pendente** | Decisões e saídas de referência estão documentadas; a aplicação no produto permanece limitada a seletores autorizados e branches de preview. Não há fundamento para extração/globalização em lote. |
| G5 — famílias de componentes CSS | **EM PROVA, sem consolidação** | Os incrementos de navegação, foco, imagens e componentes estão separados por contexto e em PRs DRAFT. Cada família ainda precisa do seu gate visual/funcional e revisão. |
| G6 — composição de páginas e arquitetura | **DIREÇÃO REVISADA; adoção incremental** | A direção vigente mantém HTML/CSS/JS simples e ownership por domínio; o protótipo PageComposition continua experimental, sem autorização para virar framework ou schema de produção. ARC-13 é preparação documental: 318/331 identidades do recorte têm proposta contextual (96,1%), não tradução implantada. |
| G7 — integração e hardening entre plataformas | **PENDENTE EM JORNADAS CRÍTICAS** | PR #238 teve execução autenticada isolada aprovada, mas issue #232 continua aberta até revisão/integração e revalidação. Issue #226 continua aberta: falta teste de zoom real; a tentativa por automação de tecla não alterou o zoom, e duas janelas Chrome com o mesmo título impedem selecionar com segurança a janela alvo. WebKit headless não substitui iPad/Safari real. |
| G8 — aceitação, publicação e pós-release | **NÃO INICIADO COMO RELEASE** | As PRs relevantes seguem DRAFT; não houve merge nem Production. Preview aprovado é evidência de branch, não aceitação do produto. |

## Decisões ARC-13 recém-registradas

- Oito mensagens com plural/lista ficam **adiadas até a etapa de localização**; não escolher formato de pluralização ou extrair esses casos agora.
- Cinco textos de catálogo/editorial ficam **no catálogo** e aguardam revisão do owner do conteúdo. O nome desse owner ainda não está documentado; nenhuma pessoa será presumida ou contatada sem identificação/autorização.
- O recorte de 318/331 mede cobertura de propostas documentais sobre identidades de origem. Não mede cobertura completa de localização, chaves aprovadas, código migrado nem conclusão do plano.
- O índice ARC-13, o runtime e `decisions.json` permanecem intactos.

## Próxima sequência com menor retrabalho

1. Destravar a janela de Chrome correta para completar a verificação de zoom real da issue #226; até isso, manter o gate como PENDING, sem substituir por viewport emulada.
2. Concluir a revisão e revalidação da correção CI da issue #232 na sequência autorizada, usando o estado interno de teste existente; não integrar enquanto PR #238 ainda aguarda revisão.
3. Consolidar apenas incrementos de produto com escopo estável e gates verdes, mantendo-os nas PRs DRAFT para revisão; não carregar a PR #39 inteira para a branch atual.
4. Continuar ARC-13 em propostas contextuais não controversas. Manter os oito casos plurais adiados e os cinco textos de conteúdo pendentes do owner; não alterar catálogo ou índice por inferência.
5. Só avançar G8 após revisão humana, integração autorizada, validação sobre a base integrada e readback do release.

**Estado geral:** trabalho substancial está preparado em branches e evidências, mas a implementação integrada e a aceitação final continuam atrás do avanço documental. Este documento é um crosswalk operacional de 25/10, não uma autorização para merge ou publicação.
