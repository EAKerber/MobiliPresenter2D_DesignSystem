# DS-HYG-RET — Disposição das branches remanescentes (26/10/2026)

**Autoridade:** delegação do usuário para decidir a política de remoção, sem revogar as decisões D01–D04 nem os gates de higiene.  
**Baseline conferida:** `main@b5363f2fd11b3c6bc3512c01c13e6330e3be17c1`; 10 branches: 1 main, 1 operacional, 8 HOLDs. PRs abertas #39 e #51.

## Decisões de governança assumidas

1. **Uma única branch permanente**: `main`; qualquer branch temporal deve ter propósito e término verificáveis, sem proliferar refs para obter números cosméticos.
2. **Decisões homologadas atuais prevalecem**: `decisions.json@main` e manifests da main mantêm autoridade; textos, experimentos, workflows ou esquemas antigos não serão promovidos automaticamente.
3. **Nenhum descarte silencioso de evidência**: uma ausência de caminhos exclusivos não prova equivalência de conteúdo; mera lista de SHAs sem proteção de alcançabilidade do Git não comprova retenção indefinida. Preservar conteúdo útil com proveniência e distinguir evidência histórica de runtime atual.
4. **D04 seletivo**: para #39, classificar 24 arquivos exclusivos (15 docs, 7 experimentos, 2 workflows), sem ativar os workflows; para #51, classificar 207 caminhos exclusivos após extrações #83 e #85, preservando o material relevante. Fechar PRs apenas após recibo de cobertura.
5. **Somente mecanismo existente de higiene para exclusão**: branch antiga divergida continua HOLD até ser elegível sob as provas de ancestralidade/merge squash exato exigidas pelo executor. O mecanismo alternativo de arquivo histórico que fora bloqueado por segurança não será recriado por outra rota.

## Obstáculo técnico especial: última branch operacional

`maintenance/ds-pr41-runtime-evidence-extract-20261026@544ca50735443bdbe9beffccee39b7542056df57` era ancestral da main, PR #87 estava encerrada/mesclada e nenhum workflow ativo a referenciava. Contudo, um **manifesto SHA-pinned não pode apagar a mesma branch a partir da qual é submetido o PR que contém o manifesto**: ao criar o commit do manifesto, o HEAD da branch muda e invalida o próprio pin, antes do audit/apply.

A preparação local da candidata P13 detectou isso **antes de abrir PR ou de editar a main**. O manifesto P13 não foi aplicado nem submetido. Esta PR substitui o diff candidato por documentação, restaurando o conteúdo do batch P12 consumido exatamente como na main. Não contar exclusões inexistentes.

Usar outra branch temporária para excluir a primeira apenas troca a referência operacional de lugar; **não reduz o conjunto ao estado main-only**. Não criar esse ciclo sem uma saída terminal demonstrável.

## Pendências objetivas, não novas homologações

| Classe | Branches | Gate |
| --- | ---: | --- |
| Operacional | 1 | Encerramento terminal seguro sem violar pin e PR audit; no fluxo atual não pode autoreferenciar a própria exclusão |
| Documentais antigos | 6 | Todos ainda divergem em histórico/valores; comparar cobertura de evidências e comprovar elegibilidade de cada HEAD |
| PR #39 | 1 | 24 arquivos únicos/protótipos, extrair ou classificar com rastreabilidade, fechar a PR |
| PR #51 | 1 | 207 exclusivos, majoritariamente ARC-13/runtime, selecionar e preservar o material necessário, fechar a PR |

**Decisão de parada:** não declarar `SAFE_TO_DELETE` sem gate nem usar merge `ours`/alteração de ancestry artificial para simular integração. Se a limpeza exigir um novo procedimento destrutivo, apresentar explicitamente o trade-off antes da implementação; a autorização de objetivo não substitui o bloqueio de segurança já registrado.

**Próxima tarefa útil e segura:** continuar inventário semântico/seleção das PRs #39 e #51, sem mexer no repositório de produto até autorização explícita do seu nome/URL neste chat.
