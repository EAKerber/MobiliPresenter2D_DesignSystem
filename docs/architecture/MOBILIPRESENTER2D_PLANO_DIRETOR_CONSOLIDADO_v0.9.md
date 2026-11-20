---
title: "MobiliPresenter2D — Plano Diretor de Execução Arquitetural"
subtitle: "Edição consolidada — capítulos I–VIII e anexos operacionais"
author: "Plano técnico de análise e execução"
date: "17 de novembro de 2026"
lang: pt-BR
toc: false
---

# MobiliPresenter2D

**Plano Diretor de Execução Arquitetural**

*Edição consolidada 0.9 — Análise, contratos, backlog, DoD e integração*

**Data-base:** 17/11/2026  
**Material de origem:** oito capítulos completos fornecidos pelo usuário  
**Caráter:** plano de execução, não relatório de implantação

---

# Índice

- [Prefácio](#prefacio)
- [Como utilizar este documento](#como-usar)
- [Visão do plano e seus marcos](#visao-marcos)
- [Capítulo I — Auditoria do método, histórico e proposta de reestruturação](#capitulo-1)
- [Capítulo II — Revisão crítica ARC-01…16 e arquitetura-alvo executável](#capitulo-2)
- [Capítulo III — Backlog técnico de foundations, tokens, CSS e estados](#capitulo-3)
- [Capítulo IV — Componentes, composição de páginas e ciclo de vida dos controladores](#capitulo-4)
- [Capítulo V — Contratos de domínio, integração das ferramentas e localização](#capitulo-5)
- [Capítulo VI — Engenharia de testes, fixtures, CI e evidências de conclusão](#capitulo-6)
- [Capítulo VII — Governança Git, integração incremental, publicação e rollback](#capitulo-7)
- [Capítulo VIII — Backlog mestre, dependências globais, marcos, DoD e acompanhamento](#capitulo-8)
- [Anexo A — Registro canônico de IDs e estados iniciais](#anexo-a)
- [Anexo B — Notas de reconciliação editorial](#anexo-b)
- [Anexo C — Proveniência dos oito anexos](#anexo-c)
- [Anexo D — Política operacional de Netlify via navegador](#anexo-d)

---

<a id="prefacio"></a>
# Prefácio

Este plano foi produzido para tornar a evolução arquitetural do **MobiliPresenter2D** mais fácil de executar, verificar e continuar entre sessões de trabalho. Ele reúne oito capítulos de análise técnica e planejamento: do diagnóstico do método histórico à governança Git, passando por Design System, CSS, componentes, Core V5, localização, testes e publicação.

A conclusão recorrente é que o produto já possui contratos, componentes e mecanismos de proteção importantes. A prioridade é **reconhecer e aproveitar o que existe, consolidar suas autoridades e integrar mudanças pequenas com evidência suficiente**, não iniciar uma reescrita ampla.

A presente edição tem duas camadas complementares: **os capítulos detalhados** preservam procedimentos e justificativas; o **backlog mestre**, os critérios de DoD e os anexos permitem operar essas decisões sem reler todo o histórico. Referências a branches, PRs e SHAs são fotografias da data da análise, não afirmações de status corrente.

Este é um **documento de planejamento**. Os oito capítulos não representam oito etapas implementadas; não foram realizadas alterações em Git, CI ou Netlify como parte desta consolidação. Cada tarefa deve ser reconciliada com a versão atual do repositório antes de receber um estado operacional diferente de `not_started`.

Uma prioridade adicional foi registrada para o Netlify: avaliar a conveniência de desativar Deploy Previews automáticos de PRs. A avaliação e qualquer alteração futura de configuração deverão usar **a interface gráfica no navegador próprio do ChatGPT**, conforme a experiência informada pelo usuário; CLI, automações genéricas e plugin Netlify não são os caminhos previstos para esse controle. Nenhuma configuração é modificada por este documento.

---

<a id="como-usar"></a>
# Como utilizar este documento

**Para compreender a arquitetura:** leia os Capítulos I e II, depois o capítulo técnico da frente desejada (III–VII).

**Para executar trabalho:** consulte o Capítulo VIII, escolha um ID com dependências satisfeitas, leia seu procedimento integral no capítulo de origem e registre um recibo de evidência antes de atualizar o DoD.

**Para decidir se uma entrega está concluída:** exija o contrato, o SHA, o ambiente, os testes apropriados e a integração na branch-alvo; publicação só conta quando fizer parte do escopo da tarefa.

**Para investigar divergências:** consulte o Anexo A (IDs canônicos), o Anexo B (reconciliações editoriais) e o Anexo C (fontes originais e integridade).

**Terminologia:** as referências a `HOLD`, `PASS`, `READY` ou `INTEGRATED` em capítulos históricos podem designar decisões de gate ou etapas de um processo local. No acompanhamento canônico, os seis status são `not_started`, `in_progress`, `blocked`, `in_review`, `done` e `cancelled`. As classificações locais devem ser mantidas como evidência/nota, não como novos estados do backlog.

---

<a id="visao-marcos"></a>
# Visão do plano e seus marcos

| Onda | Resultado esperado | Capítulos mais relacionados |
|---|---|---|
| O0 | Autoridade, método e controle de publicações acidentais | I, VI, VII, VIII |
| O1 | Contratos, owners e DAG de integração | II, IV, V, VII |
| O2 | Cores, tokens, CSS e foundations coerentes | II, III |
| O3 | Componentes públicos e navegação homologados | IV, VI |
| O4 | Core V5 e ferramentas protegidos por contratos | IV, V, VI |
| O5 | Catálogo `pt-BR` e cobertura ARC-13 | II, V, VI |
| O6 | CI otimizada, publicação, DoD e consolidação documental | VI, VII, VIII |

A ordem é preferencial, não uma dependência global. Pacotes independentes podem avançar em paralelo quando não houver conflito de arquivos, dados ou gates.

---

<a id="capitulo-1"></a>
# Capítulo I — Auditoria do método, histórico e proposta de reestruturação

## 1. Tese central

A arquitetura proposta é, em grande parte, coerente com as necessidades do produto. O problema principal não parece estar nas decisões ARC-01…ARC-16, mas na forma como sua execução foi organizada.

O processo demonstra excelente preocupação com rastreabilidade, reversibilidade e prevenção de regressões. Em contrapartida, apresenta sinais de quatro problemas estruturais:

1. **O custo de produzir e reconciliar evidências cresceu muito em relação ao volume de código arquitetural efetivamente integrado.**
2. **Gates de abrangência excessiva criaram dependências que bloqueiam entregas menores e tecnicamente independentes.**
3. **O planejamento passou a ser distribuído entre múltiplos sistemas de classificação, documentos, PRs e snapshots, sem uma visão executável única de conclusão.**
4. **O método privilegia demonstrar segurança de uma alteração isolada, mas ainda não resolve suficientemente bem a passagem dessa alteração até sua integração definitiva.**

A correção proposta não é reduzir indiscriminadamente os testes ou acelerar merges. É **reduzir o trabalho repetido, melhorar a qualidade dos limites de cada incremento e aproximar a validação da integração**.

### Hipótese orientadora

O próximo ganho de produtividade virá menos de novos mecanismos de arquitetura e mais de uma reorganização do fluxo de execução:

**Intenção aprovada → contrato verificável → implementação por conjunto coeso → testes proporcionais ao risco → integração → comprovação no consumidor → encerramento.**

Cada etapa deve produzir o mínimo necessário para tornar a etapa seguinte segura, sem exigir a conclusão de partes não relacionadas do programa.

---

## 2. Reconstrução histórica

A análise distingue o que está documentado, o que foi confirmado nos commits e o que ainda depende de execução em ambiente real.

| Período | Trabalho predominante | Resultado | Efeito metodológico |
|---|---|---|---|
| 20–21/10 | Inventários, decisões visuais e aprovação ARC-01…16 | Arquitetura-alvo definida | Forte direção técnica |
| 21–23/10 | Experimentos de componentes, tokens e compilação de páginas | Diversas provas isoladas | Adoção ainda dependente de reconciliação |
| 22–26/10 | ARC-03C, navegação, VIS-002C e correções públicas | Entregas efetivas e testes de integração | Demonstração de que incrementos pequenos podem chegar ao produto |
| 26–29/10 | Reconciliação histórica e higiene de branches | Grande redução de divergências Git | Alto esforço operacional, diferente do avanço arquitetural |
| 01–09/11 | NAV-005 na `development`, alias de foco e testes | Mudanças pontuais integradas | Avanço arquitetural pequeno, porém comprovável |
| 10–16/11 | G0–G8, DS-05A, ARC-13, ARC-15 e correções da `main` | Grande expansão das evidências, documentação e diagnósticos | Crescente distância entre investigação e implementação |
| 17/11 | PRs de navegação, contraste, localização e testes aguardando integração | Trabalho promissor em diferentes estágios | Necessidade de consolidar a fila e estabelecer sequência executável |

### Fotografia atual confirmada

No repositório principal:

- `main@efc40584`, com alterações até 16/11.
- `development@1a69ff76`, com última alteração em 09/11.
- Oito branches remotas, incluindo seis branches de trabalho.
- Seis PRs abertas: #269, #271, #274, #278, #279 e #280.
- `development` com 434 commits próprios em relação à base comum e `main` com cinco commits próprios.

No Design System:

- `main@79db735`, sem alterações integradas desde 27/10.
- PR #119 aberta em Draft, com extensa atualização de evidências e execução arquitetural.
- A PR #119 reúne atualmente 151 commits e 93 arquivos alterados em relação à `main`.

**Interpretação:** o trabalho arquitetural não parou. Contudo, parte relevante da atividade recente não chegou às branches definitivas. E uma quantidade crescente de decisões operacionais está registrada em uma PR documental ainda não integrada.

Isso não prova, isoladamente, desperdício. Demonstra uma diferença entre **produção de trabalho** e **consumo definitivo desse trabalho pelo produto**.

---

## 3. Avaliação crítica do método existente

### 3.1 O que deve ser preservado

**A. Autoridade explícita por responsabilidade**

A separação entre Design System e Produto está correta:

- Design System: decisões visuais homologadas, contratos, referência dos tokens e evidências.
- Produto: implementações Vanilla, composição, controladores, domínio V5 e consumidores.
- Administração: autoridade comercial, autorização, persistência e publicação.
- Viewer/Configurador: projeções e renderizadores específicos.

Essa distribuição evita duas fontes editáveis da mesma implementação e reduz a chance de uma refatoração visual alterar regras comerciais.

**Decisão proposta:** preservar.

**B. Fidelity-first**

A política de preservar aparência e comportamento por padrão é apropriada para uma migração arquitetural.

Ela evita o erro clássico de misturar modernização de código, redesign e mudança de domínio em uma única PR.

**Decisão proposta:** preservar, mas distinguir equivalência estrita de alterações com diferença visual intencional já aprovada.

**C. Evidência ligada ao código exato**

A exigência de SHA, fixture, browser, viewport, tema, estado e resultado é valiosa. Especialmente em fluxos de publicação, segurança e renderização, ela impede que um teste antigo seja apresentado como prova do código atual.

**Decisão proposta:** preservar a identidade exata, reduzindo a necessidade de produzir relatórios narrativos repetidos.

**D. Consolidação por responsabilidade semântica**

A ARC-05 evita componentes universais baseados apenas em semelhança visual. É um limite importante.

Um controle administrativo e um botão público podem compartilhar primitivas, mas isso não significa que devam compartilhar comportamento ou geometria.

**Decisão proposta:** preservar integralmente.

**E. Reversibilidade e precedência das decisões homologadas**

Os cuidados com rollback, alterações aditivas pequenas, catálogo real e separação da `main` e `development` continuam adequados.

**Decisão proposta:** preservar, com critérios proporcionais ao risco.

### 3.2 Atritos identificados

| ID | Atrito | Evidência ou sintoma | Consequência provável | Gravidade |
|---|---|---|---|---|
| A-01 | Planejamento sobreposto | ARC-01…16, V0–V6 e G0–G8 coexistem | Dificuldade de identificar a próxima entrega concreta | Alta |
| A-02 | Critério de conclusão insuficientemente operacional | Grandes fases continuam “parciais” apesar de subentregas aprovadas | Progresso difícil de medir e comunicar | Alta |
| A-03 | Gate amplo bloqueando mudança estreita | G2/DS-05A ainda depende de `/config/` e 98 pares incertos | Trabalho independente aguarda infraestrutura incompleta | Crítica |
| A-04 | Repetição de evidências | ARC-15 identifica 21 comandos, 21 workflows e invocações compartilhadas | Custo de CI e investigação sem ganho proporcional | Alta |
| A-05 | Problemas de fixture confundidos com problemas de aplicação | Issue #232; teste de vidro abria Home esperando Configurador | Falsos bloqueios e diagnóstico atrasado | Crítica |
| A-06 | Handover excessivamente acumulativo | Snapshots históricos e adendos sucessivos | Alto custo de recuperar o estado vigente | Alta |
| A-07 | Documentação evoluindo antes da integração | DS #119, Product #274 | Autoridade operacional dispersa entre branches | Alta |
| A-08 | Divergência entre branches de referência | `main` e `development` seguem evoluindo separadamente | Revalidação e reconciliação recorrentes | Alta |
| A-09 | Política de uma variável por incremento excessivamente literal | O plano antigo recomenda separar JS, CSS, tema e layout | Divisão artificial de mudanças tecnicamente inseparáveis | Média/alta |
| A-10 | Bloqueios sem alternativas graduais | HOLD em G4/G5/G6, mesmo havendo famílias menores | Lentidão para começar a implementação compartilhada | Alta |
| A-11 | Métricas de conclusão incompatíveis | ~30% no DS e 49% na avaliação anterior | Impossibilidade de usar porcentagens como instrumento confiável | Alta |
| A-12 | Testes exploratórios sem promoção controlada | Alguns replays ficam manuais ou fora da CI | Trabalho de diagnóstico não se transforma em proteção contínua | Média/alta |

As gravidades são avaliações desta auditoria, não classificações já homologadas.

---

## 4. Análise causal dos principais atritos

### 4.1 Excesso de granularidade administrativa versus granularidade funcional

O plano original favorece “uma variável por incremento”. Isso funciona muito bem quando existe uma alteração independente, como substituir dois literais CSS por uma variável já definida.

Entretanto, pode produzir fragmentação artificial quando um comportamento exige mudanças coordenadas.

Exemplo: um componente compartilhado pode precisar de HTML acessível, CSS de variante, controlador JS, contrato e testes. Separá-los em cinco PRs independentes não reduz necessariamente o risco; pode até criar estados intermediários inconsistentes e aumentar o número de reconciliações.

**Revisão proposta:**

A unidade de trabalho passa a ser **um contrato funcional ou visual coerente**, não um tipo de arquivo.

Uma entrega pode modificar HTML, CSS e JS se essas mudanças forem necessárias ao mesmo comportamento e se houver um teste integrado que prove sua consistência.

Continuam proibidos os agrupamentos injustificados: mudança de autenticação junto com refatoração estética, migração de schema junto com reorganização de botões ou alterações de preços para viabilizar um componente visual.

### 4.2 Gates tratados como bloqueios globais

A G2 precisa verificar CSS e contraste reais. Essa exigência é correta.

O problema surge quando a indisponibilidade da configuração publicada em `/config/` impede, na prática, que outras famílias avancem, mesmo quando seus consumidores são públicos, independentes e reproduzíveis.

A solução é decompor o gate por **família, consumidor e risco**.

Por exemplo:

- O teste de contraste do Admin não precisa esperar um defeito do Configurador quando utiliza fixture e DOM administrativos válidos.
- A extração de um token semântico numa rota pública pode avançar se todos os consumidores afetados estiverem identificados e testados.
- A extração de CSS compartilhado entre Viewer e Configurador precisa esperar os dois consumidores relevantes, não todos os 98 pares incertos do produto.
- Uma alteração que depende da configuração publicada não pode declarar conformidade hospedada com base em uma fixture sintética local.

Isso preserva a segurança enquanto substitui um HOLD abrangente por **HOLDs localizados**.

### 4.3 Testes corretos, mas execução possivelmente redundante

A ARC-15 já trouxe um insight importante: dois testes que compartilham assertions não são necessariamente redundantes.

Um teste puro de preço e um teste de browser do resumo podem verificar propriedades diferentes. Eliminá-los porque ambos usam os mesmos valores seria incorreto.

A economia deve ocorrer primeiro na **orquestração**, não na remoção das garantias.

Proposta:

1. Inventariar assertions por contrato e camada.
2. Separar repetição do mesmo comando de repetição semântica.
3. Agrupar testes que compartilham fixture e inicialização.
4. Executar um bundle focalizado por mudança.
5. Reservar a matriz maior para integrações e alterações com efeitos transversais.
6. Preservar logs e resultados individualizados quando forem necessários para auditoria.
7. Repetir uma suíte completa somente quando a nova árvore de integração exigir essa prova.

**Objetivo:** não é reduzir o número de assertions; é reduzir inicializações, downloads, browsers e diagnósticos repetidos sem diminuir cobertura.

### 4.4 Problemas de evidência que deveriam ser detectados antes

A auditoria encontrou casos concretos:

- O inventário ARC-13 anterior continha um marcador literal de truncamento e não era JSON válido; foi necessário reconstruí-lo a partir da árvore de origem.
- O replay de vidro esperava o Configurador, mas abria a Home; a PR #280 está corrigindo essa incompatibilidade.
- Um teste de navegação falhou e posteriormente passou no mesmo SHA; o registro não demonstrou uma regressão funcional determinística.
- Evidências locais de CSSOM foram produzidas em condições que não cobriam todos os estados e, em alguns casos, precisaram de correções metodológicas posteriores.
- A instalação de um workflow de UX-04 na branch padrão tornou-se uma PR separada (#279), necessária para possibilitar o disparo oficial do gate no SHA da `development`.

Cada caso é explicável isoladamente, mas o conjunto aponta para uma lacuna: **falta uma pré-validação padronizada da própria infraestrutura de teste**.

Antes de usar um teste para bloquear uma alteração, deve haver prova mínima de que ele carrega a rota correta, usa uma fixture adequada, encontra os elementos esperados e distingue claramente falta de pré-condição de falha do produto.

### 4.5 Métricas arquiteturais sem denominador comum

O Design System registra aproximadamente 30% de avanço, com faixa de 25–35%, para seu programa G0–G8. Minha estimativa anterior de 49% considerou também infraestrutura pré-existente que satisfaz parte dos contratos ARC.

**Esses percentuais não são comparáveis diretamente.**

O número de 49% não deve ser promovido a KPI canônico. E os 30% também não devem se tornar um KPI operacional sem explicitar o conjunto de entregáveis, pesos e critérios de fechamento.

O método novo precisa medir separadamente:

- **Cobertura de intenção:** requisitos classificados e associados a um contrato implementável.
- **Cobertura de implementação:** consumidores realmente migrados.
- **Cobertura de validação:** consumidores migrados com provas adequadas.
- **Cobertura de integração:** mudanças incorporadas na branch-alvo, sem regressões conhecidas.
- **Cobertura de release:** mudanças disponibilizadas e verificadas quando publicação fizer parte do objetivo.

Isso impede que um grande inventário aumente artificialmente o percentual de localização implementada.

---

## 5. Revisões de método propostas

### RM-01 — Criar uma única unidade executável de planejamento

Manter ARC, V e G como classificações de referência, mas fazer o gerenciamento operacional por **pacotes de entrega**.

Cada pacote terá:

- ID estável.
- Resultado observável.
- Requisitos ARC relacionados.
- Famílias/consumidores afetados.
- Dependências reais.
- Mudanças de código previstas.
- Testes aplicáveis.
- Critérios de GO/HOLD/NO-GO.
- Responsável por decisão, quando necessário.
- Estratégia de rollback.
- Estado e evidência de integração.

A fase V0–V6 informa a natureza do trabalho. O gate G0–G8 informa a disciplina de validação. Nenhum dos dois substitui o pacote executável.

### RM-02 — Substituir documentação narrativa repetida por registros estruturados

Separar três tipos de documentos:

**1. Contratos canônicos:** decisões duráveis, alteradas somente quando uma decisão é realmente revista.

**2. Estado operacional:** uma tabela curta gerada ou atualizada por evento relevante, apontando para o último SHA, entregas abertas e bloqueios.

**3. Evidências históricas:** artefatos imutáveis que preservam a origem da prova e não precisam ser reescritos a cada checkpoint.

Os handovers deixam de ser diários cumulativos e passam a referenciar esses registros.

Uma nova execução de teste deve acrescentar um resultado, não necessariamente um novo documento explicando novamente o mesmo contexto.

### RM-03 — Utilizar bundles de teste por domínio de mudança

Proposta inicial:

| Bundle | Quando executar | Garantias principais |
|---|---|---|
| **BT-00 — Preflight** | Toda mudança | Build, sintaxe, artefatos gerados, integridade e escopo |
| **BT-10 — Tokens/CSS** | Tokens, cores, foco, cascata | Proveniência, CSSOM, contraste contextual, regressão de estados |
| **BT-20 — Componentes/DOM** | HTML, componentes e JS de apresentação | Semântica, lifecycle, teclado, eventos, variantes |
| **BT-30 — Navegação/composição** | Header, menu, rotas e fragmentos | Rotas, foco, ordem, responsive, sem JS onde aplicável |
| **BT-40 — Core/V5** | Configurador, Viewer, Admin e projeções | Domínio, preço, seleção, DTO, invariantes e publicação |
| **BT-50 — Auth e segurança** | Sessão, acesso, gravação e publicação | Negativas 401/403, autenticação, isolamento, persistência segura |
| **BT-60 — Localização** | Extração de textos e bundles | Chaves, cobertura, fidelidade pt-BR, interpolação, ARIA |
| **BT-70 — Integração** | Promoção entre branches ou múltiplas famílias | Regressão cruzada e compatibilidade dos consumidores |
| **BT-80 — Release** | Publicação autorizada | Smoke hospedado, assets, sessão, cache, versão, readback e rollback |

Os bundles serão refinados no turno 6, com comandos existentes, fixtures compartilhadas e matrizes de disparo.

Eles não substituem testes especializados. Um bundle é um conjunto de garantias, não obrigatoriamente um único workflow ou um único processo.

### RM-04 — Separar prova local de prova hospedada

Cada pacote de entrega deve declarar quais níveis são necessários:

| Nível | Prova | Uso |
|---|---|---|
| L0 | Estática/determinística | Arquivos, hashes, schema, lint, diff e build |
| L1 | Execução local controlada | Contrato e comportamento com fixture válida |
| L2 | Browser local | DOM, CSSOM, eventos, foco, layout e renderização |
| L3 | Cross-browser/ambiente hospedado | Integração real, diferenças de motor, sessão controlada |
| L4 | Dispositivo real/revisão humana | Touch, visual, acessibilidade assistiva e particularidades de plataforma |
| L5 | Pós-release | Produção, assets, cache, autorização e readback |

Nenhum pacote precisa executar todos os níveis automaticamente. A escolha é determinada pelo risco e pelos consumidores afetados.

### RM-05 — Tornar a integração uma etapa planejada desde o início

O plano atual tende a concluir uma investigação antes de definir como ela será integrada.

A proposta inverte isso: **todo pacote nasce com seu caminho de integração e sua condição de promoção conhecidos**.

Antes de começar:

1. Definir branch-alvo e baseline.
2. Identificar alterações concorrentes.
3. Confirmar consumidores que precisam ser migrados juntos.
4. Escolher o bundle de testes.
5. Definir quais resultados serão portáveis após reconciliação e quais exigirão rerun.
6. Especificar a menor PR ou sequência de PRs que mantém o sistema consistente.
7. Preparar rollback sem exigir reverter funcionalidades independentes.
8. Reservar Preview somente quando sua evidência for necessária.

---

## 6. Backlog inicial — Reforma do processo

Esta é a primeira camada do backlog. Ela organiza os mecanismos que serão usados nos demais turnos.

### Marco M0 — Estabelecer uma base confiável e uma única fonte de progresso

**Objetivo:** tornar o programa auditável sem depender de interpretação de handovers históricos.

**MD-001 — Congelar o inventário de referência**

1. Ler `main` e `development` do Produto e `main` do Design System.
2. Registrar commits, árvores, PRs e issues ativos.
3. Classificar cada PR como implementação, teste, documentação, experimento ou infraestrutura.
4. Mapear quais contratos ARC cada PR satisfaz ou prepara.
5. Distinguir o que está somente na branch candidata do que está integrado.
6. Registrar divergências de consumidores entre `main` e `development`.
7. Produzir um manifesto de snapshot com links, SHAs, data e limites.
8. Comparar o manifesto com os registros atuais sem reescrever o histórico.

**Saída:** inventário único do programa.

**Teste/validação:** BT-00, consultas Git read-only, comparação de árvores e integridade do manifesto.

**Concluído quando:** todos os itens ativos tiverem identidade, finalidade, branch-alvo e classificação verificáveis.

**MD-002 — Consolidar a cadeia ARC → entrega → consumidor**

1. Percorrer ARC-01…16.
2. Dividir cada contrato em obrigações observáveis.
3. Associar cada obrigação aos consumidores reais.
4. Classificar implementação atual como completa, parcial, candidata, experimental, não iniciada ou não aplicável.
5. Apontar os testes existentes.
6. Identificar obrigações sem teste.
7. Separar obrigações satisfeitas por código legado legítimo das que exigem migração.
8. Eliminar contagens duplicadas de uma mesma obrigação entre fases V e gates G.

**Saída:** matriz de cobertura arquitetural.

**Concluído quando:** nenhuma decisão ARC depender apenas de uma indicação genérica de “parcial”.

**MD-003 — Recalibrar métricas**

1. Definir denominador por contrato e consumidor.
2. Estabelecer pesos de esforço e criticidade de maneira explícita.
3. Separar implementação, validação, integração e release.
4. Tratar evidência ausente como não verificada, não como falha presumida.
5. Publicar percentuais por trilha, com incerteza.
6. Manter estimativas anteriores como histórico, sem misturar séries.
7. Atualizar números somente quando um evento alterar efetivamente a cobertura.

**Saída:** baseline quantitativa reproduzível.

**Concluído quando:** duas auditorias independentes, usando o mesmo manifesto e as mesmas regras, chegarem ao mesmo resultado ou explicarem claramente a divergência.

### Marco M1 — Recuperar previsibilidade dos testes

**MD-004 — Auditar os 21 comandos e 21 workflows do baseline ARC-15**

1. Reconstituir o grafo workflow → comando → fixture → assertion → contrato.
2. Marcar comandos chamados em múltiplos workflows.
3. Identificar inicializações repetidas desnecessárias.
4. Diferenciar testes de camadas distintas com assertions coincidentes.
5. Classificar testes de proteção de fonte literal, execução real, geometria, autenticação e integração.
6. Identificar triggers inconsistentes e testes sem invocação.
7. Propor bundles que reaproveitam fixtures sem esconder resultados.
8. Comparar o tempo, a estabilidade e a cobertura antes de mudar workflows.

**Saída:** proposta técnica da nova matriz de execução.

**Concluído quando:** cada workflow tiver finalidade, trigger e garantia própria explícitos.

**MD-005 — Validar a infraestrutura dos browsers**

1. Confirmar que cada teste abre a rota que realmente pretende verificar.
2. Validar readiness da aplicação antes de testar comportamento.
3. Confirmar que a fixture reproduz o contrato mínimo necessário.
4. Rejeitar fixtures inválidas com erro diagnóstico próprio.
5. Separar falha de autenticação, de bootstrap, de carregamento e de assertion.
6. Registrar browser, versão, sistema e seed/fixture.
7. Adotar encerramento garantido de servidores e browsers.
8. Impedir que sucesso de um ambiente seja apresentado como sucesso de outro.

**Prioridade imediata:** a PR #280 e o replay de vidro.

**Saída:** infraestrutura de execução confiável.

**Concluído quando:** os testes que dependem do Configurador não puderem passar ou falhar silenciosamente sobre a Home, e os erros de pré-condição estiverem diferenciados dos defeitos do produto.

**MD-006 — Resolver a estratégia de fixture autenticada**

1. Enumerar quais jornadas exigem autenticação real.
2. Separar testes de aplicação de testes de fronteira de autorização.
3. Definir fixture local para domínio e navegação sempre que suficiente.
4. Definir ambiente hospedado autorizado para testes que realmente precisam dele.
5. Preservar resultados anônimos 401/403 e comportamento de redirecionamento.
6. Não publicar configuração real ou reduzir restrições de acesso para liberar CI.
7. Validar os fluxos permitidos e negados.
8. Documentar explicitamente os testes que continuam bloqueados por ausência de autorização.

**Saída:** estratégia de autenticação reproduzível e segura.

**Concluído quando:** os testes protegidos tiverem um caminho válido de execução, sem ampliar permissões do produto.

### Marco M2 — Reorganizar o fluxo de integração

**MD-007 — Classificar as PRs atualmente abertas**

Para cada PR:

1. Verificar o objetivo ainda pertinente.
2. Identificar a mudança semântica efetiva.
3. Reconhecer código já absorvido, substituído ou superado.
4. Identificar dependências com outras PRs.
5. Verificar se o bundle de testes é apropriado.
6. Determinar se falta prova, decisão ou implementação.
7. Definir uma saída: integrar, revisar, dividir por responsabilidade ou encerrar como substituída.
8. Registrar a decisão sem movimentar a PR antes dos gates.

**Fila inicial:** Produto #269, #271, #274, #278, #279, #280 e Design System #119.

**Saída:** fila ordenada de integração, não apenas de investigação.

**MD-008 — Estabelecer política de reconciliação `main` ↔ `development`**

1. Inventariar diferenças de runtime, ignorando inicialmente arquivos de evidência e históricos inertes.
2. Separar alterações mais recentes da `main` das implementações arquiteturais próprias da `development`.
3. Identificar conflitos semânticos, não apenas conflitos de linha.
4. Classificar consumidores alterados por ambas.
5. Preservar decisões homologadas e corrigir regressões reais.
6. Criar plano de promoção por famílias independentes.
7. Exigir testes do estado integrado, não apenas dos dois estados de origem.
8. Evitar merge indiscriminado enquanto a divergência não estiver classificada.

**Saída:** plano de integração incremental com proveniência.

**Concluído quando:** cada família de mudança tiver destino, precedência e teste de integração definidos.

### Marco M3 — Abrir caminho para a execução arquitetural

**MD-009 — Decompor G2/DS-05A em bloqueios localizados**

1. Revalidar a lista de pares incertos no CSS atual.
2. Agrupar por causa técnica, consumidor e superfície.
3. Identificar casos em que `backdrop-filter` ou composição exigem medição de pixels.
4. Separar pares realmente afetados por uma extração candidata dos não afetados.
5. Priorizar defeitos de contraste já comprovados.
6. Permitir o avanço de famílias não dependentes desses casos.
7. Preservar HOLD para mudanças cujo consumidor relevante não foi validado.
8. Publicar uma matriz de incertezas com condição explícita de resolução.

**Saída:** G2 dividido em subgates independentes.

**MD-010 — Selecionar o primeiro pacote vertical de componentes/tokens**

1. Escolher uma família pequena com consumidores conhecidos.
2. Verificar o papel semântico e a decisão homologada.
3. Confirmar os CSS/JS realmente carregados.
4. Medir baseline visual e funcional.
5. Identificar duplicação efetiva de autoridade.
6. Projetar a menor implementação compartilhada.
7. Definir BT-10/BT-20 e testes de integração.
8. Executar a mudança somente depois da aprovação operacional do pacote.
9. Comparar antes/depois.
10. Integrar e encerrar a duplicação, ou registrar por que ela é legítima.

**Saída:** primeiro pacote arquitetural fechado do novo método.

**Concluído quando:** a família tiver consumidores migrados, equivalência demonstrada e nenhuma implementação editável paralela injustificada.

---

## 7. Nova política de marcos e encerramento

Os marcos deixam de corresponder apenas a grandes fases e passam a representar capacidades verificáveis.

| Marco | Resultado exigido |
|---|---|
| **M0 — Base confiável** | Backlog, contratos e progresso com fonte única |
| **M1 — Testes previsíveis** | Bundles e fixtures válidos, sem bloqueios falsos conhecidos |
| **M2 — Integração governável** | Fila de PRs e divergência `main`/`development` classificadas |
| **M3 — CSS destravado** | Incertezas localizadas e primeiros pacotes de tokens integrados |
| **M4 — Componentes consistentes** | Famílias compartilhadas com variantes e lifecycle validados |
| **M5 — Localização operacional** | Catálogo `pt-BR` e migração incremental real |
| **M6 — Ferramentas consolidadas** | Reuso coerente entre Configurador, Viewer e Admin, sem violar V5 |
| **M7 — Validação transversal** | Matriz de risco e jornadas críticas validadas |
| **M8 — Encerramento arquitetural** | Critérios ARC-16 atendidos, pendências explícitas e integração concluída |

Um marco pode ter subpacotes concluídos e outros bloqueados. O bloqueio de um subpacote não paralisa automaticamente os demais.

A exceção são dependências reais: não se declara completo um componente compartilhado que ainda quebra um consumidor obrigatório.

---

## 8. Questões abertas que exigem investigação ou decisão

Estas questões serão tratadas como itens do backlog. Não é necessário responder a todas antes de iniciar o trabalho independente.

| ID | Questão | Como resolver |
|---|---|---|
| Q-01 | Qual deve ser a unidade canônica de progresso: contrato, consumidor ou pacote de integração? | Propor modelo híbrido e verificar ausência de dupla contagem |
| Q-02 | Quais HOLDs de G2 realmente impedem G4/G5? | Construir grafo de dependência por consumidor |
| Q-03 | Qual é o custo de CI causado por inicializações repetidas? | Medir execuções e durations por bundle |
| Q-04 | Qual é o conjunto mínimo de testes seguro para cada família? | Derivar dos contratos e de seus riscos |
| Q-05 | Quais decisões ARC ainda precisam de interpretação técnica e quais estão encerradas? | Revisão cruzada de decisões e implementação |
| Q-06 | É possível extrair tokens por equivalência de valores sem homologação visual adicional? | Distinguir aliases de mesmo valor de mudanças de aparência |
| Q-07 | Qual estratégia de fixture permitirá validar `/config/` hospedado com segurança? | Revisão de auth/CI e teste de fronteiras |
| Q-08 | Qual percentual do ARC-13 corresponde a strings realmente localizáveis? | Revisão semântica por coortes e classificação de fontes |
| Q-09 | Quais componentes estão duplicados por responsabilidade, e não apenas por nome? | Matriz de ownership e consumidores |
| Q-10 | Quais PRs candidatas devem ser absorvidas antes da próxima etapa arquitetural? | Triagem de risco, dependência e prontidão |
| Q-11 | Quais métricas realmente demonstram redução de custo de manutenção? | Comparação antes/depois, com dados e não somente linhas de código |
| Q-12 | Quais decisões dependem do proprietário e quais são escolhas técnicas delegáveis? | Matriz de autoridade e limiares de escalonamento |

---

## 9. Avaliação preliminar das prioridades

A priorização não deve começar pela maior categoria de percentual incompleto. Deve começar pelo melhor conjunto de ações para remover bloqueios e permitir integrações posteriores.

**Prioridade crítica:**

- Confiabilidade de fixtures e testes.
- Conversão de HOLDs amplos em dependências localizadas.
- Visibilidade única do backlog e do progresso.
- Reconciliação da fila de PRs.
- Estratégia de integração entre `main` e `development`.

**Prioridade alta:**

- Tokens e CSS por famílias homologadas.
- Controladores/variantes de componentes compartilhados.
- Transformação do inventário ARC-13 em um catálogo operacional.
- Testes integrados por consumidor.

**Prioridade condicionada:**

- Abstrações adicionais de composição.
- Reorganizações amplas de CSS sem duplicação comprovada.
- Criação de renderizadores ou schemas universais.
- Suporte a dispositivos legados fora das prioridades aprovadas.
- Novas ferramentas de auditoria sem problema mensurável que justifique seu custo.

A preferência deve ser por reduzir responsabilidades duplicadas e fechar contratos, não por criar mais infraestrutura.

---

## 10. Critério de qualidade do novo processo

A reforma do método será considerada bem-sucedida quando produzir resultados verificáveis:

1. É possível identificar a próxima ação de implementação sem reler dezenas de handovers.
2. Um desenvolvedor consegue reproduzir o gate de um pacote com comandos e fixtures conhecidos.
3. Uma alteração pequena não depende de testes sem relação com seus consumidores.
4. Uma mudança compartilhada não é aprovada sem validar os consumidores que afeta.
5. Testes flakey ou bloqueados por pré-condições não são confundidos com regressões confirmadas.
6. As PRs deixam de permanecer indefinidamente como depósitos de investigação sem decisão de saída.
7. O progresso passa a crescer por integração comprovada, não por quantidade de documentos, branches, commits ou testes.
8. O custo de CI, previews, produção de evidências e manutenção de ferramentas permanece observável.
9. A arquitetura final preserva a simplicidade de HTML/CSS/JS puros e as autoridades de domínio V5.
10. O encerramento de cada lote inclui seu benefício, evidência, consumidores, exceções e rollback.

---

## 11. Resultado deste primeiro diagnóstico

A hipótese mais importante é que **a segurança técnica e a eficiência de integração não precisam competir**.

O processo atual demonstrou capacidade de produzir provas detalhadas e preservar decisões. O passo seguinte é transformar essa capacidade em uma cadeia de implementação com custo previsível.

O backlog futuro deve ser organizado em dois eixos complementares:

- **Eixo de entrega:** o que muda concretamente no produto, quais consumidores passam a usar o novo mecanismo e quando a duplicação anterior deixa de existir.
- **Eixo de prova:** qual é o conjunto mínimo suficiente de evidências para garantir essa mudança, sem descuidar de autenticação, domínio ou aparência.

A execução arquitetural não deve avançar apenas quando todas as incertezas do produto tiverem desaparecido. Deve avançar quando **todas as incertezas relevantes ao pacote específico** estiverem resolvidas ou explicitamente tratadas.

Esse será o princípio usado para construir os próximos capítulos.

### Referências primárias utilizadas nesta etapa

- [Contrato ARC-01…ARC-16](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md)
- [Plano diretor G0–G8](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/architecture/DESIGN-SYSTEM-CONSOLIDATION-MASTER-PLAN-2026-10-20.md)
- [Crosswalk de execução atualizado — PR #119](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARCHITECTURE_EXECUTION_CROSSWALK_2026-11-15.md)
- [Checkpoint G0–G8 até 16/11](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/evidence/architecture/architecture-g0-g8-current-checkpoint-2026-11-09.md)
- [Inventário ARC-13 após #277](https://github.com/EAKerber/MobiliPresenter2D/blob/docs/arc13-post-273-reconciliation-20261114/docs/architecture/arc13/inventory-reconciliation-post-277-2026-11-16.md)
- [Auditoria ARC-15 de testes](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARC15_VERIFICATION_INVENTORY_2026-11-15.md)
- [PR #280 — correção do replay de vidro](https://github.com/EAKerber/MobiliPresenter2D/pull/280)
- [Issue #232 — pré-condições do Configurador](https://github.com/EAKerber/MobiliPresenter2D/issues/232)

**Limite desta parte:** o diagnóstico é sustentado por contratos, históricos Git, diffs, PRs, issues, código representativo e resultados registrados. Ainda não constitui um perfil quantitativo de duração de CI, custo de engenharia ou taxa de regressões; essas medições são tarefas do plano revisado, não números a serem presumidos.

---

<a id="capitulo-2"></a>
# Capítulo II — Revisão crítica ARC-01…16 e arquitetura-alvo executável

## 1. Premissas e limites da revisão

A presente revisão parte de cinco premissas:

1. **Decisões arquiteturais homologadas continuam vigentes.** O propósito não é substituí-las sem nova autorização, mas identificar interpretações e procedimentos que não decorrem necessariamente dessas decisões.
2. **O código existente tem valor próprio.** Uma funcionalidade que já satisfaz um contrato arquitetural não precisa ser reimplementada apenas para receber um novo nome ou localização.
3. **Compartilhamento não é um objetivo isolado.** Seu valor está em eliminar autoridade duplicada, reduzir inconsistência e facilitar alterações futuras sem aumentar acoplamento.
4. **Provas de equivalência precisam ser proporcionais ao alcance.** Nenhuma prova local autoriza inferir conformidade global, mas uma incerteza global tampouco deve bloquear um componente independente.
5. **A simplicidade é um critério de arquitetura.** Uma camada adicional deve justificar sua existência por uma redução demonstrável de complexidade, risco ou esforço de manutenção.

### Método de avaliação

Cada ARC foi avaliada por seis critérios:

| Critério | Pergunta |
|---|---|
| Necessidade | Existe um problema real que a decisão resolve? |
| Autoridade | Qual camada é dona da regra ou da implementação? |
| Abrangência | Quais consumidores efetivamente precisam compartilhar o contrato? |
| Economia | O mecanismo reduz mais complexidade do que acrescenta? |
| Compatibilidade | A mudança preserva contratos existentes e decisões homologadas? |
| Verificabilidade | Como demonstrar conclusão sem depender de interpretação subjetiva? |

Esses critérios também serão usados para rejeitar extrações que, embora tecnicamente viáveis, não tragam benefício material.

---

## 2. Revisão das 16 decisões ARC

### 2.1 Matriz executiva

| ARC | Decisão original | Avaliação | Revisão operacional proposta |
|---|---|---|---|
| **01** | Componentes implementados no produto | Manter | Definir um dono por contrato executável, não obrigatoriamente um arquivo por componente |
| **02** | Tokens aprovados originados no DS | Manter | Diferenciar tokens aprovados, aliases locais e propriedades ainda não homologadas |
| **03** | Fragmentos HTML no build | Manter com escopo | Gerar somente fragmentos realmente compartilhados entre páginas compatíveis |
| **04** | Fidelidade visual/funcional estrita | Manter | Formalizar dois tipos de mudança: refatoração equivalente e correção intencional |
| **05** | Componentes por responsabilidade semântica | Manter | Permitir primitivas comuns sem forçar a unificação de componentes de domínio |
| **06** | Controladores por componente | Manter com proporcionalidade | `dispose` obrigatório somente onde há remontagem ou ciclo de vida dinâmico |
| **07** | HTML estático + JS onde dinâmico | Manter | Não transformar o Configurador/Viewer em HTML de build por uniformidade |
| **08** | Tokens semânticos + CSS delimitado | Manter | Delimitação pela propriedade do comportamento e consumidores, sem obrigação de nova folha |
| **09** | Conteúdo editorial versionado | Manter | Separar claramente editorial, mensagens UI, metadados e domínio V5 |
| **10** | Estrutura pública explícita | Manter | Não expandir o manifesto de composição sem duplicação concreta |
| **11** | Core comum, apresentações específicas | Manter integralmente | Proteger os contratos existentes antes de propor extrações adicionais |
| **12** | Domínio controla validação, auth e persistência | Manter integralmente | UI pode apresentar estados e disparar intenções, nunca assumir autoridade de negócio |
| **13** | Extração abrangente de textos localizáveis | Manter com método novo | Inventariar amplamente, classificar semanticamente e migrar por contratos/consumidores |
| **14** | Distribuição versionada DS → produto | Manter | Um manifesto verificável e um caminho de atualização explícito, sem infraestrutura extra desnecessária |
| **15** | Testes proporcionais ao risco | Manter e fortalecer | Seleção de bundles por contrato afetado, com infraestrutura de teste pré-validada |
| **16** | Encerramento com provas, duplicações e rollback | Manter | Critério de saída por pacote integrado; exceções rastreadas sem bloquear o programa inteiro |

**Parecer:** nenhuma das 16 decisões exige revogação com base nas evidências atuais. Há, porém, ajustes substanciais a fazer em como se transformam essas decisões em trabalho.

---

## 3. Grupo A — Autoridade, governança e distribuição

**Contratos:** ARC-01, ARC-02, ARC-14, ARC-16.

### 3.1 ARC-01 — Autoridade de componentes

A direção está correta: a implementação dos componentes pertence ao Produto. O Design System fornece contratos, decisões e provas.

O principal risco é transformar “um owner” em “uma localização física obrigatória”.

Uma implementação pode possuir:

- HTML incluído na fonte de uma página ou fragmento compartilhado.
- CSS mantido na folha da família.
- Controlador JS carregado uma vez.
- Contrato semântico documentado.
- Testes em arquivos separados.

Isso ainda pode ser uma implementação única em termos de responsabilidade.

**Refinamento:** o owner é definido pelo *contrato de manutenção*, não pelo número de arquivos.

#### Protocolo ARC-01 revisado

1. Identificar a funcionalidade observável.
2. Listar seus consumidores reais.
3. Localizar a implementação que produz o comportamento.
4. Localizar configurações, estilos e adaptadores de cada consumidor.
5. Distinguir fonte executável de artefato gerado.
6. Identificar se existem duas fontes editáveis para a mesma regra.
7. Se houver duplicação real, escolher uma fonte responsável.
8. Se houver contratos distintos, preservar a separação.
9. Registrar dependências entre componentes, sem criar um registro central de runtime.
10. Validar a alteração no conjunto de consumidores afetados.

**Saída exigida:** uma matriz componente → owner → consumidores → variantes → fontes editáveis.

**Rejeitar:** mover todas as implementações para uma pasta universal de componentes sem evidência de necessidade.

### 3.2 ARC-02 — Fonte dos tokens

A exportação determinística já existe no Design System, mas a distribuição de paleta aprovada de referência não foi autorizada como integração global.

Essa distinção é correta e deve ser preservada.

O ponto a melhorar é a taxonomia dos valores CSS.

Propõe-se classificá-los em quatro grupos:

| Tipo | Característica | Política |
|---|---|---|
| **T1 — Token homologado** | Papel e valores aprovados para consumidor/tema/estado | Exportação DS → produto |
| **T2 — Alias técnico equivalente** | Nomeia valor já usado sem alterar resultado | Pode avançar com prova de equivalência |
| **T3 — Valor contextual próprio** | Pertence a uma variante, arte ou consumidor particular | Permanece local |
| **T4 — Candidato não homologado** | Valor proposto ou conflito de aparência não decidido | Não ativar como token de design |

Essa classificação evita dois erros opostos:

- Globalizar cores que deveriam continuar contextuais.
- Exigir aprovação visual adicional para cada alias puramente técnico de mesmo valor, mesmo quando sua equivalência pode ser comprovada.

O P-TOKEN-02A1 da `development` é exemplo de T2: substitui dois literais pelo token de foco existente, preservando os valores finais.

#### Protocolo de promoção de um token

1. Identificar sua origem e classe T1–T4.
2. Registrar o contexto aprovado.
3. Localizar consumidores efetivos.
4. Medir os valores computados atuais.
5. Examinar herança, especificidade, ordem de folhas e temas.
6. Definir o menor patch de consumo.
7. Confirmar que fallback e estados conservam a aparência.
8. Aplicar testes do bundle BT-10.
9. Integrar o patch e testar a árvore resultante.
10. Registrar ganho concreto: eliminação de autoridade duplicada, inconsistência resolvida ou facilidade real de manutenção.

**Não promover** automaticamente todos os literais de cor identificados por scanners.

### 3.3 ARC-14 — Distribuição DS → produto

A arquitetura atual prevê exportações determinísticas, versões, hashes, manifesto e PR de integração.

Tudo isso faz sentido.

A insuficiência metodológica está na falta de um contrato operacional único para percorrer o caminho completo.

**Cadeia-alvo:**

1. Decisão homologada no Design System.
2. Geração determinística do artefato.
3. Manifesto de origem, versão, escopo e hash.
4. Atualização explícita no Produto.
5. Verificação de integridade.
6. Verificação de consumidores.
7. Testes da mudança.
8. Integração e registro do resultado.

Não há necessidade, por enquanto, de criar um serviço de sincronização, pacote npm próprio ou processo de publicação de biblioteca.

A distribuição pode continuar sendo realizada com arquivos versionados e scripts Node puros.

#### Contrato mínimo de manifesto

Deverá conter:

- Identificador e versão do artefato.
- Commit/hash da fonte no Design System.
- Decisão homologada correspondente.
- Escopo aprovado de consumo.
- Hash do arquivo gerado.
- Versão/esquema do gerador.
- Lista de consumidores esperados ou referência à matriz.
- Indicação de ativação ou estágio apenas de referência.

Não incluir lógica executável nem comandos de deploy no manifesto.

### 3.4 ARC-16 — Critério de encerramento

A ARC-16 está correta, mas o critério deve ser aplicado ao **escopo da entrega**, não a toda a arquitetura em cada incremento.

Para um pacote específico:

- Todos os consumidores afetados devem estar identificados.
- Todas as duplicações relevantes ao contrato devem estar classificadas.
- Duplicações reais dentro do escopo devem ser eliminadas ou justificadas.
- Testes necessários devem ter resultados válidos.
- O resultado deve estar integrado na branch definida.
- Exceções devem ter owner e condição de revisão.

Não é necessário resolver todas as duplicações do produto antes de encerrar uma alteração de menu ou um token isolado.

**Alteração de método recomendada:** transformar ARC-16 em um critério de aceite mecânico de cada pacote.

---

## 4. Grupo B — Componentes, controladores, composição e CSS

**Contratos:** ARC-03, ARC-05, ARC-06, ARC-07, ARC-08, ARC-10.

### 4.1 ARC-03 e ARC-10 — Composição estática

#### Evidência existente

O arquivo `scripts/compile-primary-pages.mjs` já estabelece:

- Fonte autoral em `architecture/pages`.
- Fragmento compartilhado do cabeçalho.
- Configuração de rotas restrita.
- Saída HTML em `app/`.
- Manifesto com hashes.
- Verificação que falha diante de divergência.
- Lista explícita de rotas excluídas.

**Avaliação:** esse é um bom exemplo de implementação proporcional ao problema.

O compilador resolve duplicação de HTML estático sem introduzir uma linguagem geral de templates.

#### Ajuste recomendado

A expansão deve ser condicionada a duplicação estrutural real.

Não considero adequado estabelecer como meta que cada página privada, cada renderer ou cada conjunto de cards dinâmicos seja convertido em artefato HTML gerado.

O Viewer e o Configurador têm necessidades diferentes: a estrutura estática pode existir antes do JS, mas cena, seleção, opções e composição dependem dos dados e da projeção do domínio.

A geração no build não deve competir com o renderer dinâmico.

#### Método de decisão para novo fragmento

1. Comparar as fontes autorais das páginas.
2. Identificar um trecho com responsabilidade verdadeiramente igual.
3. Examinar diferenças de conteúdo, ordem e semântica.
4. Separar parâmetros de rota de parâmetros de comportamento.
5. Verificar que o fragmento pode ser emitido sem lógica arbitrária.
6. Medir o custo atual de manutenção duplicada.
7. Propor a menor extração.
8. Executar teste de geração e drift.
9. Executar testes do DOM final e navegação.
10. Rejeitar a extração se a parametrização ficar mais complexa que a duplicação original.

**Critério de parada:** o fragmento compartilhado deve ser mais simples de manter que as versões duplicadas, sem exigir adaptações ocultas de CSS/JS.

### 4.2 ARC-05 — Compartilhar por semântica

A norma precisa ser aplicada em três níveis distintos.

**Nível 1 — Primitiva:** regra técnica reutilizável, como indicador de foco, utilitário para texto visualmente oculto ou tratamento de estado.

**Nível 2 — Componente:** estrutura e comportamento equivalentes, como um menu público consumido por várias páginas.

**Nível 3 — Adaptador contextual:** apresenta ou conecta o componente ao domínio específico, como o Admin ou o Viewer.

Não se deve transformar toda primitiva em componente, nem obrigar cada adaptador a usar a mesma estrutura de DOM.

#### Exemplos concretos

| Família | Compartilhamento plausível | Separação obrigatória |
|---|---|---|
| Tema | Preferência, resolução claro/escuro, nomes e sinalização de estado | Geometria/posicionamento por shell |
| Menu | Primitivas de abertura/fechamento e foco, quando iguais | Menu privado com sessão e permissões |
| Cabeçalho | Marca, alguns controles e contratos de acessibilidade | Profundidade pública/Viewer/privada homologada |
| Botões | Papel semântico, foco e estados básicos | Tamanhos, hierarquia, CTA e comportamento de domínio |
| Swatches | Primitivas visuais de foco/seleção | Seleção global de acabamento versus seleção local ao módulo |
| Hotspots | Geometria de cena e indicativo selecionado | Intenção de interação de Configurador versus Viewer |
| Mensagens | Renderização de aviso, erro e sucesso | Fonte da mensagem, retry e autorização controlados pelo domínio |

O caso `.swatch` é especialmente importante: uma semelhança de CSS não autoriza concluir que a seleção global e a seleção por módulo pertencem ao mesmo estado.

### 4.3 ARC-06 — Controladores e ciclo de vida

#### Evidência existente

O controlador público `app/landing/header-menu.js` é uma IIFE que identifica o menu, registra listeners e inicializa o comportamento.

Ele não possui interface externa de `dispose()`.

Esse desenho é aceitável para uma página tradicional em que o documento é carregado uma única vez e destruído ao navegar.

Já `scene-component.js` registra um listener de teclado no documento por meio de `bindKeyboard()`. Se esse método for executado repetidamente para a mesma cena sem mecanismo de limpeza, poderá registrar listeners adicionais.

Isso indica a necessidade de classificar controladores segundo seu ciclo de vida.

#### Classes de lifecycle propostas

| Classe | Ciclo de vida | Exigência |
|---|---|---|
| **L1 — Estático único** | Inicializa uma vez por documento | Guard de instalação ou carregamento único; `dispose` opcional |
| **L2 — Atualizável** | Estado muda, elemento permanece | `update` estável; evitar registrar listeners novamente |
| **L3 — Remontável** | Elemento pode ser removido e recriado | `dispose` obrigatório ou equivalente |
| **L4 — Assíncrono** | Sessões, requests, observers e callbacks | Guard de obsolescência/cancelamento e limpeza apropriada |

Não recomendo impor uma interface universal `init/update/dispose` a todos os controladores.

#### Método por controlador

1. Identificar quem o inicializa.
2. Contar quantas vezes pode inicializar por documento.
3. Listar os listeners, observers, timers e assinaturas.
4. Determinar se o DOM controlado pode ser substituído.
5. Identificar callbacks assíncronos que podem chegar após uma atualização.
6. Verificar se existe estado compartilhado ou global.
7. Classificar L1–L4.
8. Aplicar somente os mecanismos de ciclo de vida necessários.
9. Testar instalação repetida, re-render e encerramento quando aplicáveis.
10. Registrar que o comportamento permaneceu equivalente.

**Prioridade:** examinar controladores de cena, formulários e interfaces que fazem re-render, antes de refatorar controladores estáticos já estáveis.

### 4.4 ARC-07 — Composição híbrida

A separação entre HTML de build e DOM dinâmico é sólida.

A revisão propõe utilizar quatro categorias:

- **Estrutura estática:** headers, navegação, seções essenciais e conteúdo fixo da página.
- **Composição editorial versionada:** dados de apresentação carregados de código, quando reduzirem duplicação sem esconder a estrutura.
- **Composição dinâmica de UI:** opções, estados e listas montadas segundo interação e projeções.
- **Renderização de domínio:** cena, módulos, materiais, seleção, desenhos técnicos e estimativas.

As duas primeiras não devem controlar contratos da quarta. A terceira apresenta estado, mas não deve assumir persistência ou preço.

#### Critério para adotar mais composição declarativa

Exigir evidência de pelo menos uma destas condições:

1. A mesma estrutura precisa ser mantida em diversos consumidores reais.
2. A duplicação produz inconsistências comprovadas.
3. A forma declarativa reduz custo de manutenção medido ou demonstrável.
4. A estrutura representa dados editoriais com variação legítima, não uma tentativa de substituir HTML por JSON.

Rejeitar motores que só tornam o código mais abstrato sem diminuir decisões ou trabalho.

### 4.5 ARC-08 — Delimitação CSS e tokens semânticos

Esta decisão é a mais sensível aos atritos metodológicos atuais.

A extração ampla está bloqueada por evidências incompletas de CSSOM, contrastes e consumidores privados. Porém, esse bloqueio não exige paralisar todas as extrações.

#### Unidade de análise revisada

Cada regra CSS candidata deve ser descrita por:

- Propriedade que controla.
- Papel semântico.
- Elementos que realmente a recebem.
- Arquivos co-carregados.
- Seletores concorrentes.
- Tema e estado.
- Variante de layout.
- Dependência de ancestral.
- Dependência de `@media`, `@supports` ou variável herdada.
- Efeito de composição/transparência.
- Prova visual/funcional necessária.

#### Classificação de extração

| Classificação | Tratamento |
|---|---|
| Equivalência demonstrada | Candidata à extração |
| Valores iguais, papéis diferentes | Manter separados |
| Mesmo papel, variantes legítimas | Primitiva comum + variantes locais, se simplificar |
| Aparência diferente não homologada | Não extrair como correção |
| Consumidor não observável | HOLD somente na família dependente |
| Ganho nulo ou negativo | Não extrair |

Não recomendo criar uma nova folha para cada componente. Escopo pode ser obtido com seletores suficientemente delimitados, tokens por papel e ownership claro.

A preocupação principal é a autoridade da regra, não a topologia idealizada dos arquivos.

---

## 5. Grupo C — Conteúdo editorial e localização

**Contratos:** ARC-09 e ARC-13.

### 5.1 A obrigação de cobertura integral precisa ser tecnicamente delimitada

A ARC-13 determina levantamento e extração abrangentes de textos localizáveis. Essa decisão continua válida.

Entretanto, “todos os textos localizáveis” não pode ser operacionalizado como “todas as strings encontradas no JavaScript” ou “todos os sinks do scanner”.

O inventário atual da PR #274 possui 1.026 ocorrências de pontos de uso e 360 registros de fontes JavaScript. Ele já distingue algumas mensagens diagnósticas de mensagens exibidas ao usuário.

A implementação ainda exige julgamento semântico.

### 5.2 Taxonomia de strings proposta

| Categoria | Exemplo | Destino |
|---|---|---|
| Texto fixo de UI | “Abrir menu”, “Salvar” | Catálogo pt-BR |
| Texto acessível | `aria-label`, `title`, alt informativo | Catálogo pt-BR ou conteúdo editorial contextual |
| Texto editorial | Título da Landing, descrição institucional | Conteúdo versionado, com chave de localização conforme necessidade |
| Mensagem de estado | “Publicação concluída” | Catálogo do componente/domínio |
| Mensagem técnica interna | Erro capturado e nunca exibido | Diagnóstico, fora do catálogo UI |
| Dado comercial | Preço, material, nome de módulo | Autoridade V5; não migrar para catálogo de interface |
| Texto de usuário | Nomes e informações autoradas | Dados, não tradução automática |
| Identificador operacional | IDs, códigos de erro, chaves API | Contrato técnico; não traduzir |
| Valor formatado | Moeda, número, data | Dados + `Intl` e mensagens de interface quando apropriado |
| Símbolo decorativo | Seta ou separador visual | Markup/semântica, não necessariamente tradução |

### 5.3 Estratégia de execução

A localização deve seguir duas trilhas paralelas.

**Trilha de cobertura:**

1. Inventariar fontes e sinks.
2. Medir omissões conhecidas do scanner.
3. Classificar as ocorrências.
4. Resolver ambiguidades de origem.
5. Associar owner e domínio.
6. Diferenciar duplicação textual de chave compartilhável.
7. Identificar conteúdo acessível.
8. Construir relatório de cobertura por rota e família.

**Trilha de migração:**

1. Escolher uma família pequena com conteúdo estável.
2. Criar catálogo pt-BR versionado.
3. Extrair strings mantendo texto e pontuação.
4. Integrar em HTML de build ou JS conforme o consumidor.
5. Validar interpolação e atributos acessíveis.
6. Testar ausência de chaves e fallback.
7. Verificar que não houve mudança de domínio.
8. Integrar e registrar a cobertura.
9. Repetir por família, sem reabrir o inventário inteiro a cada alteração.

As duas trilhas não devem permanecer bloqueadas uma pela outra até o fim do programa.

### 5.4 Estrutura técnica mínima

A solução deve usar arquivos versionados simples, JavaScript nativo e `Intl` onde necessário.

Não há razão atual para acrescentar biblioteca de i18n, serviço remoto de tradução ou CMS.

O formato do catálogo deve privilegiar:

- Chaves estáveis por domínio semântico.
- Valores explícitos pt-BR.
- Fallback previsível.
- Detecção de chave ausente.
- Interpolação segura.
- Suporte a plurais, formatos e estados quando necessário.
- Ausência de tradução de nomes comerciais por inferência.
- Compatibilidade com geração de HTML estático.

A localização precisa coexistir com ARC-03C, mas não deve exigir que todas as páginas passem pelo compilador atual.

### 5.5 Caso de aplicação inicial

O menu público e o controle de tema são candidatos interessantes porque já possuem textos identificáveis, consumidores conhecidos e contratos acessíveis.

Porém, antes de extraí-los:

1. Confirmar o texto homologado atual.
2. Identificar os locais em que esse texto é gerado.
3. Verificar as versões com tema e menu aberto/fechado.
4. Decidir se o mesmo conceito semântico realmente usa a mesma chave.
5. Manter a correspondência exata entre valor exibido e nome acessível.
6. Garantir que o cabeçalho estático continua funcional sem JS quando aplicável.

O primeiro pacote de localização não deve conter também uma alteração geométrica do header.

---

## 6. Grupo D — Core, domínio e ferramentas

**Contratos:** ARC-11 e ARC-12.

### 6.1 Situação técnica

O código já contém responsabilidades bem delimitadas:

- `presentation-contract.js` para o contrato de apresentação.
- `public-module-projection.js` para a projeção pública.
- Módulos específicos de precificação.
- Administração e publicação V5.
- Modelos de fluxo.
- Cena, geometria e máscaras.
- Renderizadores de Configurador e Viewer.

A projeção pública utiliza allowlist e não libera todos os dados da configuração administrativa. A publicação de preço-base depende da autorização declarada no documento.

Essas responsabilidades têm alta criticidade e não devem ser alteradas durante uma consolidação de estilo.

### 6.2 Revisão proposta

A arquitetura visual deve consumir capacidades existentes do domínio, não criar uma segunda camada que interprete regras comerciais.

| Responsabilidade | Camada proprietária |
|---|---|
| Selecionar módulo | Estado e contrato do produto |
| Determinar preço | Domínio de preço |
| Validar configuração | Domínio e aplicação |
| Publicar configuração | Administração/backend autorizado |
| Projetar dados ao comprador | Projeção segura |
| Renderizar valor ou estado | UI |
| Exibir erro e instrução | UI, a partir do resultado tipado do domínio |
| Executar retry | Camada de aplicação conforme regra autorizada |
| Determinar variante visual | Componente/UI, respeitando contexto |
| Escolher asset/cena | Catálogo e renderer de domínio |

A UI pode decidir como apresentar um erro; não pode decidir que o erro é ignorável ou que uma operação de persistência deve ser repetida.

### 6.3 Política de mudança

Qualquer pacote que envolva simultaneamente componente visual e domínio deve responder:

1. Qual comportamento funcional exige alterar o domínio?
2. O contrato V5 existente não atende ao caso?
3. É possível adaptar apenas a projeção/apresentação?
4. A mudança aumenta superfície de autorização ou publicação?
5. É necessária migração de schema ou banco?
6. Quais consumidores externos ou internos podem observar a mudança?
7. Como manter retrocompatibilidade e rollback?

Se a mudança visual funciona sem modificar o domínio, a alteração de domínio deve ser excluída do pacote.

### 6.4 Sobre extensibilidade para novos móveis

A arquitetura existente já permite variações importantes, mas isso não comprova suporte a qualquer nova família de móvel apenas por dados.

Uma nova família pode exigir mudanças de assets, geometria, máscara, cena, opções, composição e publicação.

**Recomendação:** não construir um modelo universal preventivo. Usar um novo requisito real, quando surgir, para identificar quais extensões são necessárias.

Até lá, preservar contratos e testes das famílias atuais é suficiente.

---

## 7. Grupo E — Fidelidade e validação

**Contratos:** ARC-04 e ARC-15.

### 7.1 Dois tipos formais de alteração

A política atual de fidelidade estrita precisa distinguir:

**Tipo E — Refatoração equivalente**

Não pretende alterar aparência, interação, dados ou semântica acessível.

Exige comparação antes/depois apropriada ao escopo. Qualquer diferença observada precisa ser explicada ou revertida.

**Tipo I — Alteração intencional**

Corrige bug comprovado ou implementa mudança já homologada.

Exige verificar simultaneamente:

- Que a diferença pretendida ocorreu.
- Que o comportamento não relacionado foi preservado.
- Que o resultado não introduziu regressões.

Um teste raster que exige zero diferença fora de regiões permitidas faz sentido para muitos patches Tipo E, mas não deve ser aplicado indiscriminadamente a uma mudança Tipo I cuja diferença visual é justamente o objetivo.

### 7.2 As provas precisam seguir a natureza do risco

| Risco | Prova principal | Complemento |
|---|---|---|
| Token idêntico | CSSOM e contrato de valor | Visual focal quando apropriado |
| Mudança de contraste | Fundo efetivo e composição | Captura/inspeção do contexto |
| Menu | Estado, ARIA, foco e navegação | Responsivo e touch |
| HTML estático | Build e fonte/saída | DOM real e sem JS quando pertinente |
| Controller remontável | Lifecycle e listeners | Browser/re-render |
| Projeção pública | Schema e allowlist | Endpoint e autorização |
| Preço/publicação | Regra de domínio e save/readback | Browser e HTTP quando necessário |
| Localização | Chave, cobertura e fidelidade textual | ARIA, fallback e browser |
| Cena | Geometria e estado funcional | Pixels, foco, interação e assets |

### 7.3 O que não deve acontecer

- Transformar todos os testes de browser em gate obrigatório de toda PR.
- Remover testes de domínio por terem assertions semelhantes às de browser.
- Considerar uma captura de screenshot como prova suficiente de autenticação.
- Considerar WebKit headless equivalente a um iPad real.
- Considerar build bem-sucedido como prova de comportamento.
- Considerar um teste bloqueado por fixture inválida como regressão do produto.
- Aceitar diferenças visuais não explicadas apenas porque são pequenas.

O objetivo é **selecionar provas adequadas**, não provar menos.

---

## 8. Arquitetura-alvo revisada

A arquitetura pretendida pode ser representada por seis fronteiras.

### 8.1 Fronteiras de autoridade

```text
DESIGN SYSTEM
  Homologações visuais
  Contratos ARC / VIS / EST / NAV / CMP
  Tokens aprovados e escopos
  Evidências de conformidade
             |
             | Exportação determinística,
             | hash e integração explícita
             v
PRODUTO — BUILD
  Templates e fragmentos estáticos necessários
  Compilação ARC-03C
  Geração de bundles/artefatos
  Verificação de integridade e drift
             |
             v
PRODUTO — UI VANILLA
  Componentes e variantes
  Controladores por ciclo de vida
  Estilos por responsabilidade
  Mensagens e conteúdo localizável
             |
             | Consome dados projetados,
             | publica intenções de usuário
             v
PRODUTO — DOMÍNIO/APLICAÇÃO
  Configuração, fluxo e seleção
  Preço, cena e catálogo
  Validação e publicação
  Sessão e autorização
  Projeções buyer/public
             |
             v
CONSUMIDORES
  Landing / About / How
  Viewer
  Configurador
  Administração / Acesso
             |
             v
EVIDÊNCIA E INTEGRAÇÃO
  Contratos por consumidor
  Bundles de teste
  Gate do pacote
  Branch-alvo / readback
  Release quando autorizado
```

Essa representação não implica necessariamente criar pastas novas. Ela delimita responsabilidades.

### 8.2 Regra de evolução

Uma mudança deve tentar primeiro a alternativa mais simples que respeite todas as fronteiras.

Ordem preferencial:

1. Preservar código existente que já atende ao contrato.
2. Corrigir um defeito localizado.
3. Reutilizar primitiva já disponível.
4. Extrair responsabilidade duplicada comprovada.
5. Criar componente compartilhado pequeno.
6. Criar novo adaptador por consumidor.
7. Introduzir abstração mais abrangente apenas diante de benefício mensurável.

A ordem não significa que sempre se deva passar por todos os níveis. A melhor implementação pode continuar sendo a primeira.

### 8.3 Requisitos de um contrato de componente

Cada componente que participar da consolidação deverá ter um registro enxuto:

| Campo | Conteúdo esperado |
|---|---|
| ID | Identidade estável |
| Propósito | Responsabilidade observável |
| Owner | Fonte editável responsável |
| Consumidores | Rotas ou módulos reais |
| Variantes | Somente diferenças necessárias |
| Estados | Normal, selecionado, desabilitado, erro etc., quando aplicáveis |
| Dependências | Tokens, controlador, projeção ou dados |
| Lifecycle | L1, L2, L3 ou L4 |
| Garantias | DOM, comportamento, acessibilidade e aparência |
| Gates | Bundles e evidências necessárias |
| Duplicações | Encontradas e disposições |
| Rollback | Menor reversão possível |

Esse contrato poderá ser representado em JSON ou Markdown. O formato será escolhido pela necessidade de automação, não por estética documental.

### 8.4 Exemplo: cabeçalho público

**Responsabilidade:** apresentar marca, navegação e ações globais autorizadas ao contexto público.

**Consumidores:** Home, Quem somos e Como funciona, conforme ARC-03C.

**Variante contextual:** Viewer possui cabeçalho de segunda ordem com contrato próprio; não é mais um consumidor automático do fragmento público primário.

**Controladores:** menu público e preferência de tema podem compartilhar lógica de estado, mas não precisam ter o mesmo posicionamento de elementos.

**Gates:**

- Estrutura inicial no HTML.
- Atributos e nomes acessíveis.
- Foco e teclado.
- Menu compacto.
- Tema.
- Navegação e marcador ativo.
- Mídia responsiva.
- Ausência de alterações não homologadas na geometria.

**Não pertence a esse componente:** sessão privada, decisão de publicação de preço e apresentação de opções de móveis.

---

## 9. Onde simplificar explicitamente o plano

A revisão recomenda remover as seguintes obrigações **do método de execução**, sem revogar contratos homologados:

### S-01 — Não criar um componente para cada repetição visual

Dois elementos parecidos podem ter implementações simples distintas se seu estado, evolução ou semântica divergirem.

### S-02 — Não exigir migração de todas as rotas para o compilador HTML

ARC-03C já resolve um caso concreto. Extensões são decisões pontuais.

### S-03 — Não exigir `dispose()` universal

Somente controladores remontáveis/assíncronos ou com instalação repetida precisam de desmontagem explícita. Os demais precisam impedir dupla inicialização e efeitos indevidos.

### S-04 — Não criar uma camada de tokens para cada valor observado

Tokens devem representar papéis aprovados e aliases tecnicamente justificados. Valores contextuais legítimos podem continuar locais.

### S-05 — Não usar o G2 inteiro como pré-requisito de toda extração

A dependência deverá recair sobre os consumidores e propriedades efetivamente afetados.

### S-06 — Não criar um catálogo de localização a partir de todas as strings automaticamente

A classificação é parte essencial da correção. O catálogo final contém textos localizáveis, não todo texto encontrado no código.

### S-07 — Não criar um motor universal de componentes de móveis

O domínio atual será preservado e estendido a partir de requisitos reais.

### S-08 — Não criar documentação operacional nova sem consumidor

Cada novo documento, ferramenta ou relatório deverá demonstrar o que substitui, quem o lê e como alimenta a próxima ação.

### S-09 — Não exigir zero duplicação textual

O objetivo é evitar duas autoridades editáveis para a mesma responsabilidade. Duplicação de texto, classe ou assertion pode ser legítima.

### S-10 — Não transformar todos os HOLDs em interrupções do programa

HOLD é estado de uma obrigação específica, não uma ordem implícita para paralisar trabalho independente.

---

## 10. Backlog detalhado da revisão arquitetural

Esta seção cria os pacotes arquiteturais que orientarão os próximos capítulos.

### AR2-01 — Matriz definitiva de responsabilidades

**Objetivo:** eliminar dúvidas sobre ownership antes da extração de componentes.

**Passos:**

1. Ler as fontes efetivamente carregadas em cada rota.
2. Classificar cada família de UI por papel semântico.
3. Identificar consumidores com a mesma responsabilidade.
4. Separar variantes intencionais.
5. Identificar componentes já implementados de modo compartilhado.
6. Determinar quais fontes são editáveis e quais são geradas.
7. Apontar duplicação de regra, estado ou comportamento.
8. Criar uma tabela de owners com escopo exato.
9. Revisar conflitos com ARC/NAV/EST/CMP.
10. Registrar exceções deliberadas.

**Dependências:** MD-001 e MD-002, da Parte I.

**Testes:** inspeção estática/DOM por consumidor; BT-00 inicialmente.

**Saída:** matriz de owners, sem alteração de runtime.

**Concluído quando:** cada família no escopo tiver um owner inequívoco e consumidores identificados.

### AR2-02 — Classificação da arquitetura CSS existente

**Objetivo:** diferenciar duplicação corrigível de variação legítima.

**Passos:**

1. Inventariar folhas CSS carregadas por rota.
2. Levantar ordem efetiva de carregamento.
3. Encontrar seletores repetidos em folhas co-carregadas.
4. Identificar classes homônimas com significados diferentes.
5. Identificar propriedades que vencem na cascata.
6. Examinar variáveis herdadas e estados por tema.
7. Registrar efeitos de transparência e composição.
8. Classificar regras em equivalentes, variantes, distintas ou incertas.
9. Calcular o alcance real de cada extração candidata.
10. Priorizar somente extrações com benefício reconhecível.

**Dependências:** AR2-01; DS-05A apenas para consumidores relevantes.

**Testes:** BT-10, CSSOM e capturas focalizadas.

**Saída:** backlog de extrações CSS, com risco e benefício.

**Concluído quando:** cada candidata prioritária tiver hipótese de simplificação e prova necessária definidas.

### AR2-03 — Contrato de tokens por papel

**Objetivo:** fechar a política prática de aplicação da ARC-02/14.

**Passos:**

1. Ler decisões homologadas do DS.
2. Identificar tokens executáveis aprovados.
3. Conferir exportadores e manifestos existentes.
4. Associar tokens aos consumidores permitidos.
5. Separar aliases técnicos e valores não homologados.
6. Verificar duplicações entre CSS local e artefato exportado.
7. Definir atualização mínima por família.
8. Definir regra para descontinuação de um token.
9. Preparar testes determinísticos e de CSSOM.
10. Validar rollback e hash da fonte.

**Dependências:** AR2-02.

**Testes:** BT-00, BT-10.

**Saída:** contrato de consumo DS → Produto sem sincronização remota automática.

**Concluído quando:** um token puder ser atualizado ou rejeitado com critérios objetivos, sem inventar homologação visual.

### AR2-04 — Catálogo de componentes e variantes

**Objetivo:** tornar ARC-05 operacional.

**Passos:**

1. Criar índice das famílias reais.
2. Distinguir primitivas, componentes e adaptadores.
3. Registrar contratos públicos/privados por variante.
4. Mapear estados necessários de cada família.
5. Localizar CSS e controladores atuais.
6. Classificar reuso já existente.
7. Identificar primeiro candidato com baixo risco.
8. Propor patch por responsabilidade, não por tipo de arquivo.
9. Associar testes de DOM, tema e interação.
10. Determinar condição de encerramento da duplicação.

**Dependências:** AR2-01, AR2-02.

**Testes:** BT-20 e BT-30 onde aplicável.

**Saída:** catálogo pequeno e executável, sem biblioteca UI nova.

### AR2-05 — Auditoria de lifecycle dos controladores

**Objetivo:** prevenir listeners duplicados e comportamentos obsoletos sem refatoração desnecessária.

**Passos:**

1. Localizar inicializações de cada controlador.
2. Rastrear eventos e observers registrados.
3. Identificar elementos substituídos por re-render.
4. Classificar lifecycle L1–L4.
5. Procurar eventos registrados em cada render.
6. Verificar callbacks assíncronos e stale state.
7. Definir guard de inicialização ou cleanup.
8. Escrever testes de montagem repetida onde fizer sentido.
9. Confirmar que a correção não muda semântica.
10. Encerrar somente os casos reais, sem padronização geral compulsória.

**Dependências:** AR2-04.

**Testes:** BT-20 e BT-40 para controladores ligados ao domínio.

**Saída:** lista de problemas reais e correções focalizadas.

### AR2-06 — Fechamento da política de composição

**Objetivo:** impedir expansão injustificada de ARC-03C.

**Passos:**

1. Inventariar estruturas estáticas compartilhadas.
2. Confirmar a fonte autoral das três páginas atuais.
3. Verificar se há duplicação semelhante em outras páginas.
4. Distinguir fragmentos de cabeçalho de composição editorial.
5. Identificar consumidores dinâmicos que não precisam de build-time HTML.
6. Avaliar custo de manutenção da duplicação observada.
7. Priorizar apenas novos fragmentos de benefício positivo.
8. Preservar o mecanismo existente quando suficiente.
9. Definir critérios de drift e de HTML inicial.
10. Documentar explicitamente os casos rejeitados.

**Dependências:** AR2-01 e AR2-04.

**Testes:** BT-00 e BT-30.

**Saída:** lista limitada de extensões ARC-03C, se necessárias.

### AR2-07 — Fronteira editorial/localização/domínio

**Objetivo:** tornar ARC-09/13 executáveis sem mistura de autoridades.

**Passos:**

1. Classificar todas as categorias de texto.
2. Identificar origem editorial, UI ou V5.
3. Revisar conteúdo acessível e mensagens dinâmicas.
4. Localizar fontes técnicas que não devem aparecer no catálogo.
5. Definir convenção de chaves.
6. Identificar grupos legítimos de compartilhamento.
7. Especificar interpolação segura.
8. Definir fallback pt-BR.
9. Definir relatório de cobertura.
10. Selecionar o primeiro pacote de migração.

**Dependências:** inventário ARC-13 da PR #274, após validação e integração apropriadas.

**Testes:** BT-60, verificação de texto/ARIA.

**Saída:** política técnica de localização e primeiro backlog de consumidores.

### AR2-08 — Proteção dos contratos V5

**Objetivo:** criar barreira objetiva contra mudanças indevidas durante consolidação visual.

**Passos:**

1. Mapear contratos de configuração, apresentação e projeção.
2. Identificar regras de seleção, preço e publicação.
3. Identificar consumidores de cada projeção.
4. Registrar o que é público e o que é administrativo.
5. Mapear fluxos de autenticação e persistência.
6. Selecionar os testes que já demonstram os invariantes.
7. Identificar alterações arquiteturais que podem tocá-los.
8. Exigir justificativa específica para mudança de domínio.
9. Bloquear introdução inadvertida de segunda autoridade de preços ou publicação.
10. Preservar rollback por adaptador/consumidor.

**Dependências:** MD-001 e matriz de contratos.

**Testes:** BT-40 e BT-50 conforme a alteração.

**Saída:** matriz de invariantes e limites de migração.

### AR2-09 — Política de equivalência e diferenças intencionais

**Objetivo:** operacionalizar ARC-04 sem falsos bloqueios.

**Passos:**

1. Classificar alterações como Tipo E ou Tipo I.
2. Registrar baseline de comportamento e aparência pertinente.
3. Definir diferenças esperadas.
4. Identificar quais elementos devem permanecer iguais.
5. Selecionar comparações estruturais, CSSOM e raster.
6. Definir tolerância somente quando tecnicamente justificada.
7. Preservar evidência do baseline e do candidato.
8. Investigar diferenças não explicadas.
9. Confirmar aprovação para mudanças Tipo I.
10. Registrar resultado no pacote.

**Dependências:** AR2-01 e BTs definidos na Parte VI.

**Saída:** protocolo de fidelidade por tipo de mudança.

### AR2-10 — Contrato de encerramento por pacote

**Objetivo:** transformar ARC-16 em uma condição executável.

**Passos:**

1. Definir pacote e escopo.
2. Registrar requisitos.
3. Listar consumidores e owners.
4. Identificar duplicações envolvidas.
5. Definir provas aplicáveis.
6. Definir branch-alvo e estratégia de integração.
7. Executar validação na base escolhida.
8. Integrar com autorização apropriada.
9. Revalidar o estado resultante.
10. Registrar benefício, exceções, rollback e encerramento.

**Dependências:** MD-002, MD-003 e AR2-09.

**Saída:** checklist único de conclusão.

### AR2-11 — Reexaminar abstrações experimentais

**Objetivo:** aproveitar inovações úteis sem promover infraestrutura pelo investimento histórico.

**Passos:**

1. Identificar protótipos anteriores de composição e componentes.
2. Conferir requisitos que motivaram cada um.
3. Identificar se o problema ainda existe.
4. Comparar com código já integrado.
5. Calcular custos adicionais de build/runtime.
6. Determinar consumidores reais.
7. Avaliar benefício de extrair somente partes.
8. Rejeitar abstrações não justificadas.
9. Preservar provas úteis e histórico.
10. Registrar o resultado como adoção, extração parcial ou encerramento.

**Dependências:** AR2-01 a AR2-06.

**Saída:** mapa de reaproveitamento e descarte de experimentos.

### AR2-12 — Revisar dependências arquiteturais

**Objetivo:** evitar que um grande gate impeça toda a execução.

**Passos:**

1. Identificar o contrato afetado por cada pendência.
2. Localizar consumidores diretamente impactados.
3. Distinguir dependência de implementação, dependência de teste e dependência de homologação.
4. Marcar dependências realmente bloqueantes.
5. Identificar trabalhos independentes.
6. Criar gates por família.
7. Manter gates transversais somente para integração transversal.
8. Definir o caminho crítico.
9. Registrar possibilidades de execução paralela.
10. Revisar dependências sempre que uma PR mudar o alcance de um componente.

**Dependências:** matriz de contratos e estado operacional.

**Saída:** grafo de dependências dos pacotes, sem bloqueios globais artificiais.

---

## 11. Marcos de aceitação da revisão

| Marco | Condições verificáveis |
|---|---|
| **AR-M1 — Autoridades claras** | ARC-01/02/11/12/14 têm responsáveis e fronteiras objetivas |
| **AR-M2 — Reuso delimitado** | ARC-03/05/06/07/08/10 possuem regras de promoção/rejeição por consumidor |
| **AR-M3 — Localização executável** | ARC-09/13 têm política de inventário, classificação, chaves e migração |
| **AR-M4 — Fidelidade proporcional** | ARC-04/15 têm método de seleção de provas por risco |
| **AR-M5 — Critério de conclusão único** | ARC-16 pode ser avaliada por pacote sem interpretação ad hoc |
| **AR-M6 — Arquitetura revisada aprovada** | Sem novas obrigações implícitas; ambiguidades relevantes registradas |

Esses marcos dizem respeito à maturidade do plano. Eles não serão contabilizados como implementação de componentes até que mudanças correspondentes estejam integradas.

---

## 12. Pontos de interrogação relevantes

**Q-AR-01 — Controlador de tema.** Vale separar a lógica de preferência da criação/posicionamento do controle por shell? A fonte atual acumula ambas. A hipótese é que separar responsabilidades pode diminuir acoplamento, mas é necessário demonstrar benefício e evitar novas inicializações.

**Q-AR-02 — `scene-component.js`.** O registro de teclado possui risco real de listeners duplicados em remontagens? Depende dos caminhos de chamada. É necessária auditoria de lifecycle, não reescrita preventiva.

**Q-AR-03 — Fragmentos privados.** Existem estruturas suficientemente iguais entre telas privadas para justificar composição compartilhada no build? A investigação deve responder pela duplicação observada, não pela aparência de seus cabeçalhos.

**Q-AR-04 — Tokens de estado.** Quais tokens EST estão aprovados por papel e quais representam somente orientações ou referências visuais? Não promover valores sem essa distinção.

**Q-AR-05 — `pt-BR`.** A primeira implementação deve materializar HTML localizado durante o build, oferecer funções de localização runtime ou combinar ambos? A resposta deverá minimizar transformação de DOM e preservar conteúdo estático.

**Q-AR-06 — CSS de cena.** Há regras comuns que realmente possam ser centralizadas sem alterar geometria, máscara ou ordem de camadas? Depende de testes completos por consumidor.

**Q-AR-07 — Ownership dos controles Admin.** Quais componentes podem compartilhar estados visuais com as páginas públicas sem compartilhar semântica administrativa? A matriz G3 ainda precisa fechar esses casos.

**Q-AR-08 — Escopo de encerramento ARC-16.** Qual é o nível mínimo de evidência para aceitar uma exceção de duplicação? A proposta é registrar motivo, owner, consumidor e condição de revisão, não exigir justificativas narrativas extensas.

**Q-AR-09 — Versões de tokens.** Qual granularidade de versionamento é suficiente: artefato inteiro, família ou pacote de integração? Não criar versionamento por token se isso aumentar o custo sem oferecer rollback adicional útil.

**Q-AR-10 — Critério de utilidade de uma abstração.** Como demonstrar economia de manutenção antes de existir histórico de mudanças suficientes? Usar uma combinação de consumidores reais, duplicação comprovada, complexidade introduzida e avaliação de impacto, marcando estimativas como hipóteses.

---

## 13. Parecer final da revisão

A arquitetura original já continha boa parte dos limites necessários para evitar uma modernização excessiva. O que precisa melhorar é a disciplina de execução desses limites.

A implementação deve preservar:

- HTML/CSS/JS puros.
- Tokens homologados pelo Design System.
- Componentes por responsabilidade semântica.
- Variantes explícitas.
- HTML estático para conteúdo essencial.
- Renderizadores específicos de domínio.
- Projeções seguras entre Administração, Configurador e Viewer.
- Extração abrangente e gradual dos textos localizáveis.
- Testes proporcionais ao risco.
- Critérios explícitos de conclusão e rollback.

O que deve mudar:

- Não transformar fases em bloqueios globais.
- Não promover abstrações antes de demonstrar consumidores.
- Não equiparar duplicação de sintaxe a duplicação de responsabilidade.
- Não exigir interfaces universais para controladores com ciclos de vida diferentes.
- Não misturar inventário de strings com catálogo já aprovado.
- Não tratar a criação de infraestrutura de teste como encerramento de um contrato funcional.
- Não considerar implementação concluída enquanto faltar consumo efetivo e integração na branch-alvo.

**Resultado da Parte II:** recomenda-se manter as 16 ARC como autoridade normativa, adotar os 12 pacotes AR2 para revisão operacional e usar os critérios de rejeição acima para impedir que o plano acrescente complexidade sem benefício.

### Referências verificadas

- [Contrato arquitetural ARC-01…16](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md)
- [Arquitetura Vanilla e fronteiras de domínio](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/ARCHITECTURE_VANILLA_COMPONENTS_AND_DOMAIN_DATA_2026-10-21.md)
- [Compilador ARC-03C](https://github.com/EAKerber/MobiliPresenter2D/blob/development/scripts/compile-primary-pages.mjs)
- [Controlador do menu público](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/landing/header-menu.js)
- [Controlador de tema](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/ui-theme.js)
- [Componente de cena](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/scene-component.js)
- [Projeção pública segura](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/public-module-projection.js)
- [Revisão operacional ARC/V/G](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARCHITECTURE_EXECUTION_CROSSWALK_2026-11-15.md)

**Estado:** Parte II concluída como proposta de revisão. Nenhum contrato homologado foi alterado e nenhum arquivo foi modificado.

---

<a id="capitulo-3"></a>
# Capítulo III — Backlog técnico de foundations, tokens, CSS e estados

## 1. Objetivo do programa CSS

Transformar o sistema visual existente em uma arquitetura de manutenção previsível, preservando as decisões homologadas e as diferenças legítimas entre interfaces.

O resultado esperado não é necessariamente ter menos arquivos CSS, nem substituir todas as cores por variáveis.

O resultado esperado é:

1. Uma autoridade clara para cada papel visual compartilhado.
2. Tokens de referência consumidos somente nos contextos autorizados.
3. Ausência de regras concorrentes desnecessárias para a mesma responsabilidade.
4. Estados claros/escuros e interativos previsíveis.
5. Correções de acessibilidade separadas de refatorações equivalentes.
6. Consumidores capazes de evoluir sem regressões indiretas.
7. Testes selecionados pela superfície realmente afetada.
8. Integração incremental em branches estáveis, com rollback verificável.

### 1.1 Critérios de sucesso

O programa terá cinco resultados mensuráveis:

| Dimensão | Medida |
|---|---|
| Responsabilidade | Proporção de famílias compartilháveis com owner e consumidores identificados |
| Conformidade | Casos relevantes de cor/estado verificados versus casos pendentes |
| Integração | Famílias efetivamente migradas e integradas |
| Manutenibilidade | Autoridades duplicadas reais eliminadas ou justificadas |
| Eficiência | Tempo/custo de validação por pacote, taxa de retrabalho e reabertura de gates |

A redução de linhas CSS será uma métrica secundária. Uma implementação pode ser melhor mesmo contendo mais linhas, caso reduza acoplamento e regressões.

---

## 2. Estado técnico que condiciona o backlog

### 2.1 Há duas distribuições de tokens distintas

**Distribuição A — Paleta VIS-002 de referência**

O Design System possui:

- `scripts/export-approved-palette.mjs`
- `dist/approved-palette-reference.css`
- `dist/approved-palette-reference.manifest.json`

O Produto possui:

- `design-system/pins/vis-002/v0.1.0/PIN.json`
- `scripts/verify-design-system-reference-pin.mjs`

O manifesto declara que os valores da paleta estão aprovados como referência, mas a integração global não está autorizada. O pin do produto tem `activated: false` e `cssImportAllowed: false`.

**Conclusão:** não utilizar essa paleta como folha CSS global, nem reinterpretar sua aprovação visual como autorização de migração geral.

**Distribuição B — VIS-002C contextual**

O Produto possui um artefato restrito:

`app/design-system/vis002c-long-copy-light-v0.3.0.css`

O mapeamento contém dez contextos de texto distribuídos entre Home, Quem somos e Como funciona, exclusivamente no tema claro. O arquivo é importado pela folha da Landing, e os consumidores específicos utilizam a variável contextual.

O pin dessa distribuição ainda descreve o estágio como `SCOPED_INTEGRATION_CANDIDATE_NOT_RELEASED`, apesar de o código da `development` conter a importação e os consumidores.

**Conclusão:** verificar separadamente presença no código, integração na branch e estado de publicação. A redação do manifesto não deve ser usada isoladamente para inferir o que o navegador já consome.

### 2.2 Alias de foco não equivale à aplicação da paleta homologada

Na `development`, `app/ui-theme.css` declara:

| Tema | Token de foco atual |
|---|---|
| Claro | `--ui-theme-focus: #6e512e` |
| Escuro | `--ui-theme-focus: #d8bc7c` |

O P-TOKEN-02A1 substituiu dois valores literais por referências a esse token.

Isso preservou as cores atuais.

Entretanto, a paleta de referência VIS-002 descreve o foco claro como `#8B6A40` e o tratamento de referência como contorno de 4 px e offset de 3 px. Há, portanto, uma diferença entre o alias técnico atual e o tratamento visual de referência.

**A equivalência do alias não comprova conformidade global com VIS-002.**

O novo processo deverá registrar esses fatos como duas obrigações independentes.

### 2.3 Correções DS-04 em andamento

A PR [#271](https://github.com/EAKerber/MobiliPresenter2D/pull/271) contém mudanças restritas a quatro arquivos:

- `app/access/manage.html`
- `app/admin/admin.css`
- `app/styles.css`
- `app/viewer/viewer.css`

O escopo inclui contraste, seleção visual e indicadores.

Seus nove workflows passaram no head `8a67d10f`, mas a revisão autenticada do Configurador não foi repetida nesse head. O Configurador hospedado ainda apresenta problema na validação da configuração publicada.

**Conclusão:** há subgates aprovados, mas ainda não existe comprovação integral da PR em todos os consumidores relevantes.

### 2.4 Existem problemas independentes na mesma folha

A evidência DS-05A aponta duas questões em `app/styles.css`:

**Caso `.module-number`:** teste local de uma regra candidata elevou o contraste medido dos badges claros de aproximadamente 1,43:1 para 13,02:1, mantendo o controle escuro em 8,10:1. A regra foi injetada em memória; não foi integrada.

**Caso `#viewerHint`:** comparações locais encontraram resultados diferentes entre `main` e `development`. No conjunto examinado, o texto em `main` apresentou 1,00:1 no claro e 4,05:1 no escuro; na `development`, 5,22:1 e 4,88:1. A diferença está associada a `.viewer-card__footer`.

Os problemas pertencem à mesma folha, mas não precisam ser corrigidos no mesmo pacote.

### 2.5 As 98 incertezas não são 98 defeitos confirmados

O DS-05A mantém 98 pares classificados como incertos, especialmente devido à composição com transparência e `backdrop-filter`.

Não se deve concluir que todos falham nos critérios de contraste. Também não se deve declará-los conformes.

A tarefa correta é **classificar a natureza da incerteza, identificar o consumidor afetado e determinar a prova faltante**.

---

## 3. Revisão do método de execução

### 3.1 Unidade de entrega

A unidade de trabalho será o **pacote CSS tecnicamente coeso**.

Um pacote deve corresponder a um único resultado observável e conter tudo que é necessário para produzi-lo.

Pode incluir alterações em mais de um arquivo quando isso for indispensável para preservar o mesmo contrato.

Exemplos:

- Corrigir um par de cores homologado e os seletores que realmente o consomem.
- Aplicar um alias equivalente em uma família.
- Extrair um utilitário compartilhado e ajustar seus consumidores.
- Alterar uma variante de tema com testes para ambos os estados.

Não são pacotes coesos:

- “Melhorar todo o CSS.”
- “Aplicar todos os tokens VIS-002.”
- “Resolver todos os alertas de contraste.”
- “Juntar todas as classes com o mesmo nome.”
- “Refatorar tema, navegação, layout e preço em uma PR.”

### 3.2 Limites máximos de responsabilidade

Cada pacote deve declarar:

**Inclusões:** arquivos e consumidores que podem mudar.

**Exclusões:** domínio, rotas, comportamentos ou valores que não podem mudar.

**Controle negativo:** pelo menos um consumidor/estado que deve permanecer inalterado.

**Critério de retirada:** condição para abandonar a extração caso o benefício não se confirme.

Isso evita que uma mudança inicialmente pequena se transforme em uma modernização geral durante a implementação.

### 3.3 Estados padronizados

Cada pacote poderá estar em:

| Estado | Significado |
|---|---|
| `DISCOVERY` | Ainda não existe contrato completo de consumidor |
| `READY` | Escopo, baseline e testes definidos |
| `IMPLEMENTING` | Alteração em curso |
| `VALIDATING` | Testes e comparação em execução |
| `HOLD` | Bloqueio específico identificado |
| `READY_TO_INTEGRATE` | Evidências necessárias reunidas no head candidato |
| `INTEGRATED` | Mudança incorporada à branch-alvo |
| `VERIFIED` | Resultado integrado revalidado |
| `CLOSED` | Critérios ARC-16 e documentação encerrados |
| `REJECTED` | Extração abandonada por risco ou custo |
| `SUPERSEDED` | Substituída por implementação posterior |

O estado `HOLD` exige motivo, consumidor afetado e condição de desbloqueio. Não é aceito como descrição genérica de uma fase inteira.

---

## 4. Cadeia de dependências proposta

```text
CSS-00 — Baseline e escopo
   |
   +---- CSS-01 — Classificação dos 98 pares incertos
   |         |
   |         +---- CSS-03 — .module-number
   |         +---- CSS-04 — #viewerHint
   |         +---- CSS-05 — demais correções DS-04
   |
   +---- CSS-02 — Fechamento da PR #271
   |
   +---- TOK-00 — Integridade DS→Produto
   |         |
   |         +---- TOK-01 — VIS-002C contextual
   |         +---- TOK-02 — Alias de foco
   |         +---- TOK-03 — Primeiro token compartilhado novo
   |
   +---- FND-01 — Utilitários neutros
   |         |
   |         +---- FND-02 — Estados e variantes
   |                    |
   |                    +---- FND-03 — Famílias CSS compartilhadas
   |
   +---- TST-01 — Bundles de teste e instrumentação
             |
             +---- INT-01 — Integração e readback
```

**Interpretação:** as linhas representam dependências de informação e validação, não necessariamente uma sequência de commits.

A correção da PR #271 não precisa esperar o catálogo de localização.

O alias de foco não precisa esperar a classificação de todos os 98 pares.

Uma extração de `.visually-hidden` não precisa aguardar a validação hospedada dos materiais do Configurador, desde que seu próprio contrato seja comprovado.

---

# 5. Backlog detalhado de execução

## Marco CSS-M0 — Base confiável e incertezas localizadas

### CSS-00 — Reconstruir a baseline CSS atual

**Prioridade:** P0  
**Tipo:** auditoria pré-implementação  
**Dependências:** MD-001 e MD-008 da Parte I

#### Objetivo

Produzir uma fotografia confiável do CSS efetivamente carregado em `main` e `development`, evitando usar evidências antigas como se fossem válidas automaticamente para novos commits.

#### Passo a passo

1. Fixar os SHAs atuais de `main`, `development` e Design System.
2. Listar arquivos CSS em `app/` e classificá-los por rota.
3. Separar folhas runtime de fixtures, snapshots, referências não carregadas e arquivos históricos.
4. Identificar `<link>`, `@import`, CSS injetado por JS e folhas produzidas pelo build.
5. Registrar a ordem de carregamento de cada rota.
6. Identificar arquivos gerados e suas fontes autorais.
7. Comparar blobs CSS entre `main` e `development`.
8. Identificar alterações que já chegaram à `main` por PRs recentes.
9. Distinguir alterações de aparência de mudanças apenas documentais.
10. Construir tabela seletor → folha → rota → estado/tema → consumidor.
11. Marcar caminhos cuja aplicação depende de DOM gerado dinamicamente.
12. Marcar consumidores inacessíveis por falta de fixture ou sessão autorizada.
13. Gerar relatório estruturado com hash dos arquivos analisados.
14. Criar resumo curto das diferenças relevantes para os próximos pacotes.

#### Arquivos iniciais

`app/public-theme.css`, `app/ui-theme.css`, `app/landing/landing.css`, `app/about/about.css`, `app/how-it-works/how-it-works.css`, `app/viewer/viewer.css`, `app/styles.css` e `app/admin/admin.css`.

O levantamento deverá acrescentar qualquer folha realmente utilizada que não esteja nessa lista inicial.

#### Saídas

- Inventário de folhas ativas.
- Matriz por rota e tema.
- Diff semântico `main` ↔ `development`.
- Lista dos snapshots antigos que não podem mais fundamentar conclusões atuais.

#### Testes

BT-00, verificação estática de imports e conferência de hashes.

Não há necessidade de Preview.

#### Critério de conclusão

Nenhum pacote de CSS utiliza uma baseline sem SHA ou desconhece as folhas co-carregadas por seus consumidores.

---

### CSS-01 — Classificar os 98 pares incertos

**Prioridade:** P0  
**Tipo:** investigação estruturada  
**Dependências:** CSS-00  
**Gate associado:** DS-05A

#### Objetivo

Transformar uma quantidade agregada de incertezas em um backlog resolúvel, eliminando bloqueios artificiais.

#### Classificação proposta

| Classe | Causa | Prova adequada |
|---|---|---|
| U1 | Fundo opaco, mas ancestral incorreto identificado | CSSOM e rastreio da cascata |
| U2 | Transparência simples com camadas conhecidas | Composição das camadas |
| U3 | `backdrop-filter` e composição espacial | Captura de pixels e análise da região |
| U4 | Fundo com imagem/gradiente | Amostragem de regiões relevantes |
| U5 | Estado dinâmico ausente na fixture | Renderer real e estado reproduzido |
| U6 | Elemento inacessível por autenticação/configuração | Fixture válida ou ambiente autorizado |
| U7 | Elemento não visível ou fora do escopo naquele estado | Prova de não aplicabilidade |
| U8 | Defeito confirmado | Ticket e pacote corretivo |

#### Passo a passo

1. Recuperar a lista original, preservando IDs e referências.
2. Conferir que cada ocorrência pertence ao código ainda vigente.
3. Agrupar por rota e família de componente.
4. Identificar seletores e estados que correspondem à mesma causa.
5. Classificar a incerteza em U1–U8.
6. Registrar o método de captura necessário.
7. Remover apenas duplicidades de evidência, sem apagar ocorrências semanticamente distintas.
8. Verificar se o par afeta algum pacote de extração planejado.
9. Identificar quais casos podem ser resolvidos com CSSOM.
10. Reservar captura raster somente para os casos de composição que realmente exigirem pixels.
11. Registrar estados que dependem de sessão ou configuração publicada.
12. Separar defeitos confirmados de observações ainda incertas.
13. Criar um pacote corretivo para cada causa técnica compartilhada.
14. Marcar como independentes os grupos sem consumidores comuns.
15. Definir critério de encerramento por grupo, não por redução arbitrária da contagem.
16. Atualizar o mapa de dependências de G2/G3/G4.

#### Estrutura mínima de registro

Cada caso deve incluir:

`id`, `route`, `component`, `selector`, `theme`, `state`, `backgroundModel`, `sourceSha`, `uncertaintyClass`, `affectedPackages`, `requiredProof`, `status`, `owner`.

#### Política de execução

A auditoria não precisa terminar em 98 verificações manuais individuais. Casos que compartilham a mesma causa e a mesma cadeia de pintura podem ser agrupados, preservando a rastreabilidade de cada consumidor.

#### Critério de conclusão

Cada par possui classe de incerteza, prova necessária e relação explícita com os pacotes que efetivamente bloqueia.

**A classificação de todos os pares é o objetivo deste pacote; a correção de todos eles não é pré-requisito para começar os demais.**

---

## Marco CSS-M1 — Corrigir problemas comprovados sem ampliar o escopo

### CSS-02 — Reconciliar e concluir a PR #271

**Prioridade:** P0  
**Tipo:** correção intencional Tipo I  
**Dependências:** CSS-00; fixture pertinente para o Configurador  
**Branch candidata:** `codex/ds04-208-preview-batch-20261111`

#### Objetivo

Aproveitar as correções de contraste já implementadas sem repetir investigações concluídas nem considerar resultados antigos como validação do novo head.

#### Subconjuntos técnicos

**CSS-02A — Admin:** rótulos `.initial-state-option` no tema claro.

**CSS-02B — Acesso:** texto do CTA dourado em modo escuro.

**CSS-02C — Configurador:** headings, `#viewerHint` e anel de seleção.

**CSS-02D — Viewer:** indicadores móveis inativos.

A PR atual reúne os quatro subconjuntos em um patch pequeno. **Não é necessário dividi-la apenas porque existem quatro superfícies**, desde que o conjunto seja revisável, os testes estejam claros e o bloqueio de uma superfície não oculte as outras.

#### Passo a passo

1. Fixar a árvore da PR e a base atual.
2. Confirmar o diff de quatro arquivos e verificar se alguma alteração da `main` já substituiu parte da proposta.
3. Mapear cada regra alterada ao respectivo problema DS-04.
4. Conferir se os valores propostos são homologados ou correções técnicas já autorizadas.
5. Revisar os resultados de Actions do head exato.
6. Separar as evidências antigas por SHA.
7. Reutilizar resultados anteriores somente como comparação e proveniência, não como execução do head atual.
8. Confirmar os casos Admin e Acesso sem necessidade de escrita em configuração.
9. Para Configurador, usar fixture Buyer V5 válida para provas locais.
10. Revalidar no hospedado somente o que exige ambiente hospedado e sessão autorizada.
11. Conferir que a seleção de acabamento preserva estado e semântica.
12. Verificar que os indicadores móveis mantêm o estado ativo/inativo.
13. Revisar a relação com a issue #208.
14. Decidir se existe bloqueio real de integração ou apenas critério futuro de hardening.
15. Se necessária divisão, fazê-la por consumidor e comportamento, preservando a proveniência dos commits.
16. Integrar somente após os critérios apropriados terem sido satisfeitos.
17. Executar readback na árvore integrada.
18. Atualizar os subitens da issue; não fechar #208 enquanto seus demais critérios permanecerem pendentes.

#### Testes obrigatórios

- BT-00.
- BT-10 nos quatro consumidores alterados.
- Captura de contraste Admin claro/escuro.
- Contraste e interação de Acesso.
- Configurador com fixture V5.
- Seleção de acabamentos em estados relevantes.
- Viewer mobile nos dois temas.
- Testes de regressão acionados pelo alcance do diff.

#### Controle negativo

Não mudar preço, opções de móveis, seleção, máscaras, cadastro administrativo, autenticação ou publicação.

#### Critério de conclusão

Correções integradas, consumidores relevantes validados e nenhuma alteração de domínio introduzida.

---

### CSS-03 — Resolver `.module-number`

**Prioridade:** P1  
**Tipo:** correção intencional Tipo I  
**Dependências:** CSS-00, CSS-01 para a família correspondente  
**Estado atual:** candidata local, sem integração comprovada

#### Objetivo

Resolver o contraste dos números de módulo sem alterar todos os badges ou criar uma cor global que alcance superfícies diferentes.

#### Passo a passo

1. Identificar todos os consumidores de `.module-number`.
2. Conferir se possuem o mesmo fundo e papel.
3. Examinar a regra atual em `app/styles.css`.
4. Confirmar o defeito nos temas e estados pertinentes.
5. Reproduzir o baseline com fixture válida.
6. Examinar a regra candidata registrada em DS-05A.
7. Verificar se o novo fundo e a nova cor pertencem ao contexto autorizado.
8. Medir CSSOM e composição do fundo.
9. Capturar baseline e candidata nos mesmos estados.
10. Verificar legibilidade, posição, geometria e contraste.
11. Conferir que o tema escuro mantém o tratamento esperado.
12. Verificar que a regra não alcança outro componente homônimo.
13. Implementar a alteração somente no seletor/família necessários.
14. Executar testes focais.
15. Integrar e repetir a leitura do CSS efetivo.
16. Registrar a resolução da incerteza correspondente.

#### Testes

BT-10; mínimo inicial de 390, 1050 e 1366 px, claro e escuro, ajustado conforme os breakpoints reais observados.

#### Critério de conclusão

Contraste adequado no consumidor real, sem alteração de domínio ou regressão de geometria.

**Observação:** o valor de 13,02:1 é evidência da candidata local, não resultado garantido de qualquer versão hospedada.

---

### CSS-04 — Resolver `#viewerHint` separadamente

**Prioridade:** P1  
**Tipo:** correção intencional Tipo I  
**Dependências:** CSS-00 e fixture de Configurador válida

#### Objetivo

Resolver a diferença de contraste observada entre `main` e `development` sem transferir automaticamente código de uma branch para outra.

#### Passo a passo

1. Confirmar a regra de `.viewer-card__footer` em ambas as branches.
2. Identificar todos os filhos que herdam a cor.
3. Determinar se `#viewerHint` possui outro override.
4. Confirmar a aparência do card nos estados relevantes.
5. Comparar `rgba(255,255,255,.42)` com `var(--muted)` no contexto real.
6. Verificar se o token é apropriado para toda a região ou somente para o hint.
7. Medir contraste com fundo composto.
8. Examinar interações e estados de erro/seleção.
9. Selecionar a menor correção possível.
10. Testar em claro/escuro e larguras relevantes.
11. Conferir que o rodapé mantém o contrato responsivo.
12. Integrar, com prioridade à intenção homologada mais recente.
13. Repetir CSSOM no head integrado.
14. Registrar explicitamente o resultado e seus limites.

#### Controle negativo

Não alterar fluxo V5, publicação, painéis, IDs, ordem dos elementos ou informações comerciais.

#### Critério de conclusão

Cor e contraste corretos para o hint e para os demais consumidores realmente afetados; diferença entre branches reconciliada sem conflito semântico.

---

### CSS-05 — Fechar o restante do DS-04 por causa técnica

**Prioridade:** P1/P2 conforme impacto  
**Dependências:** CSS-01

A issue #208 contém um inventário histórico de problemas de contraste, estados e exceções. Parte foi corrigida em commits posteriores; outra parte permanece aberta.

#### Procedimento

1. Ler cada subitem original DS04-01…16.
2. Mapear para a regra e consumidor atuais.
3. Verificar se o defeito ainda existe.
4. Registrar correções que já chegaram à `main`.
5. Identificar casos que já possuem uma PR candidata.
6. Criar pacotes somente para defeitos atuais ainda não tratados.
7. Preservar explicitamente as exceções editoriais, materiais e de cena.
8. Não corrigir por heurística lexical.
9. Ordenar por severidade funcional e alcance.
10. Executar correções agrupadas quando tiverem a mesma causa técnica.
11. Validar estados claro/escuro e interações afetadas.
12. Atualizar a issue com evidência por subitem.
13. Encerrar apenas os critérios comprovados.
14. Não reabrir a issue #217, já encerrada com readback, sem regressão nova demonstrada.

#### Critério de conclusão

Nenhum subitem permanece com estado ambíguo: todos estão corrigidos, pendentes com prova necessária, excecionados ou não aplicáveis ao código atual.

---

## Marco CSS-M2 — Consolidar a distribuição de tokens sem alterar indevidamente a aparência

### TOK-00 — Endurecer o contrato DS → Produto

**Prioridade:** P0  
**Tipo:** infraestrutura de proveniência  
**Dependências:** CSS-00

#### Objetivo

Garantir que uma exportação homologada seja reproduzível e que a aplicação de uma exportação não amplie sua autorização.

#### Passo a passo

1. Identificar o registro de decisão DS.
2. Ler versão e hash da fonte.
3. Conferir que o gerador reconhece apenas os papéis previstos.
4. Executar o gerador no modo de verificação.
5. Comparar o CSS produzido com o artefato versionado.
6. Conferir o manifesto.
7. Conferir que o Produto possui a cópia do artefato esperado.
8. Verificar hash dos arquivos distribuídos.
9. Confirmar se o artefato é referência ou está autorizado para runtime.
10. Identificar os consumidores explicitamente autorizados.
11. Rejeitar imports de artefatos de referência sem integração aprovada.
12. Rejeitar valores alterados manualmente em cópias geradas.
13. Documentar procedimento de atualização e rollback.
14. Registrar custo e complexidade do mecanismo.
15. Evitar criar empacotamento externo se os arquivos versionados forem suficientes.

#### Testes

BT-00 e teste de integridade do pin.

#### Saída

Contrato único de proveniência e ativação, aproveitando scripts existentes.

#### Critério de conclusão

O sistema consegue distinguir mecanicamente referência, candidata e integração autorizada, sem depender de interpretação do nome do arquivo.

---

### TOK-01 — Reconciliar VIS-002C v0.3

**Prioridade:** P1  
**Tipo:** integração contextual  
**Dependências:** TOK-00 e CSS-00

#### Objetivo

Confirmar o estado real do artefato contextual e eliminar ambiguidade entre “candidata”, “importada”, “integrada” e “publicada”.

#### Passo a passo

1. Conferir mapeamento DS de dez contextos.
2. Verificar os três conjuntos de rotas.
3. Conferir hash do artefato CSS.
4. Verificar o import pela folha Landing.
5. Verificar consumo da variável pelos dez seletores.
6. Confirmar ordem da cascata.
7. Conferir a ausência do token no tema escuro, quando essa for a condição aprovada.
8. Medir cor final e fundo em Chromium e WebKit.
9. Diferenciar mudanças intencionais de texto de diferenças introduzidas por animações e imagens.
10. Revisar o teste raster atual: ele compara duas regras sobre o mesmo DOM e não substitui comparação histórica de um site real.
11. Verificar se o teste de containment continua adequado à finalidade.
12. Atualizar mensagens de workflow que ainda descrevem sete contextos, caso permaneçam desatualizadas.
13. Confirmar se a distribuição existe na `main` e qual é seu estado efetivo de publicação.
14. Atualizar status do manifesto somente para refletir a realidade comprovada.
15. Fechar divergências entre documentação, pin e código.
16. Manter a paleta global de referência desativada.

#### Testes

- `node scripts/verify-vis002c-product-pin-v03.mjs`
- Testes de pin e provenance VIS-002.
- Browser contextual.
- Raster restrito, conforme risco.
- `npm run pages:check` para páginas geradas.
- Verificação do tema escuro como controle negativo.

#### Critério de conclusão

Todos os dez contextos possuem estado rastreável, os consumidores ativos correspondem ao mapeamento e a documentação não declara uma condição de publicação incompatível com o código observado.

---

### TOK-02 — Fechar P-TOKEN-02A1 e distinguir o alias da conformidade visual

**Prioridade:** P1  
**Tipo:** refatoração equivalente Tipo E  
**Dependências:** CSS-00 e TOK-00

#### Objetivo

Preservar o ganho de manutenção do alias de foco sem confundi-lo com a eventual aplicação do tratamento de foco VIS-002.

#### Passo a passo

1. Fixar o commit integrado na `development`.
2. Confirmar que o token é definido para ambos os temas.
3. Confirmar que os consumidores globais utilizam a variável.
4. Verificar ausência de redefinições conflitantes.
5. Executar o contrato específico.
6. Medir cor, largura e offset nos consumidores afetados.
7. Conferir foco visível por teclado.
8. Identificar se existe divergência com os valores de referência DS.
9. Registrar essa divergência como obrigação visual separada.
10. Não alterar cor ou espessura apenas para “completar” o alias.
11. Testar a futura integração na base escolhida.
12. Encerrar a refatoração equivalente independentemente de uma eventual correção visual posterior.

#### Testes

`node tests/ui-theme-focus-token-contract.cjs`, BT-10 e teste focal de teclado.

#### Controle negativo

Os valores computados de foco permanecem iguais ao baseline da alteração equivalente.

#### Critério de conclusão

Alias validado e integrado, com conformidade VIS-002 tratada separadamente.

---

### TOK-03 — Selecionar o primeiro novo token compartilhado

**Prioridade:** P2  
**Tipo:** extração equivalente ou mudança contextual homologada  
**Dependências:** AR2-03, CSS-01, TOK-00

#### Critério de seleção

O candidato deve:

- Ter pelo menos dois consumidores reais do mesmo papel.
- Possuir decisão homologada ou equivalência técnica demonstrada.
- Ter escopo de cascata previsível.
- Evitar DOM inacessível que seja indispensável à prova.
- Oferecer ganho de manutenção superior ao overhead de distribuição.
- Possuir rollback pequeno.

#### Passo a passo

1. Listar candidatos por papel semântico.
2. Eliminar candidatos cuja semelhança é apenas numérica.
3. Verificar consumidores reais.
4. Identificar proprietários das regras atuais.
5. Escolher um token com baixo risco de cascata.
6. Registrar baseline por consumidor/tema/estado.
7. Medir valores computados e fundos.
8. Criar ou selecionar o artefato DS autorizado.
9. Atualizar pin do Produto.
10. Aplicar o token a um conjunto completo de consumidores equivalentes.
11. Remover as antigas autoridades duplicadas no mesmo pacote, quando seguro.
12. Verificar que nenhuma variante legítima foi eliminada.
13. Executar BT-10 e regressões dos consumidores.
14. Medir payload/cache se a estrutura de import mudou.
15. Integrar a alteração.
16. Repetir os testes necessários na árvore integrada.
17. Registrar o benefício real e encerrar o pacote.

#### Critério de retirada

Se o token exigir mais exceções, overrides e configuração do que as regras que substitui, rejeitar a extração e registrar a justificativa.

---

## Marco CSS-M3 — Foundations e estados compartilháveis

### FND-01 — Extrair a primeira primitiva neutra

**Prioridade:** P2  
**Dependências:** CSS-00, AR2-01 e AR2-02

**Candidata inicial:** `.visually-hidden`, se a auditoria confirmar equivalência.

#### Objetivo

Demonstrar que uma primitiva comum pode ser mantida com autoridade única sem alteração visual ou funcional.

#### Passo a passo

1. Localizar todas as definições da utilidade.
2. Listar arquivos co-carregados.
3. Verificar diferenças de `position`, `overflow`, `clip`, dimensões e foco.
4. Verificar pseudoestados e exceções.
5. Identificar os consumidores, incluindo conteúdo acessível.
6. Confirmar se regras aparentemente iguais são realmente equivalentes.
7. Definir um owner compartilhado.
8. Mover somente a responsabilidade equivalente.
9. Manter exceções locais quando justificadas.
10. Comparar estilos computados.
11. Testar Tab e foco em controles associados.
12. Conferir que conteúdo visualmente oculto permanece acessível.
13. Verificar que nenhum texto passa a ficar visível por engano.
14. Repetir em páginas com folhas diferentes.
15. Integrar.
16. Remover a definição redundante ou registrar exceção.
17. Medir se a extração trouxe benefício de manutenção.

#### Testes

BT-00, BT-10 e testes de acessibilidade focais.

#### Critério de conclusão

Uma única responsabilidade compartilhada, consumidores preservados e nenhuma regressão de semântica ou foco.

---

### FND-02 — Contratos de estados visuais

**Prioridade:** P2  
**Dependências:** FND-01, AR2-04 e classificação EST

#### Objetivo

Transformar estados homologados em contratos consistentes sem criar uma folha global que reestilize indiscriminadamente todos os controles.

#### Famílias de estado

- Foco.
- Seleção.
- Hover.
- Disabled.
- Read-only.
- Loading.
- Success.
- Error.
- Warning.
- Retry.
- Estado desconhecido.
- Estado bloqueado por dependência.

#### Passo a passo

1. Recuperar decisões EST e identificar os estados efetivamente homologados.
2. Mapear cada estado aos consumidores reais.
3. Distinguir sinalização visual de regra de negócio.
4. Identificar estados que já são renderizados corretamente.
5. Localizar os casos de duplicação.
6. Separar cores de papel, geometria, interação e texto.
7. Definir quais primitivas podem ser compartilhadas.
8. Preservar variantes por contexto.
9. Evitar que uma classe de estado altere permissões ou seleções.
10. Construir testes visuais e semânticos por família.
11. Aplicar mudanças em lotes pequenos.
12. Validar tecnologias assistivas nos casos pertinentes.
13. Integrar cada família depois de seus consumidores.
14. Registrar exceções intencionais.
15. Encerrar a obrigação sem criar um sistema de estados paralelo ao domínio.

#### Gate

Nenhum estado deve ser considerado implementado apenas porque existe um token com nome correspondente.

---

### FND-03 — Famílias CSS compartilhadas de risco crescente

**Prioridade:** P2/P3  
**Dependências:** FND-01/02 e matriz G3

A implementação deverá seguir a ordem que maximize segurança e ganho.

| Ordem inicial | Família | Risco principal | Condição de entrada |
|---|---|---|---|
| 1 | Utilitários semânticos neutros | Cascata e acessibilidade | Consumidores identificados |
| 2 | Foco/controles simples | Conflito de estado | Baseline de teclado |
| 3 | Tipografia e textos de papel comum | Contraste por fundo | Mapeamento de contexto |
| 4 | Botões públicos com função equivalente | Hover, foco e geometria | Contratos de variantes |
| 5 | Marca e slots de header | Responsivo e profundidade NAV | G1 relevante validado |
| 6 | Controles de seleção | Diferenças de domínio | Global/local separados |
| 7 | Hotspots e cena | Geometria, máscaras e ordem | Prova dos dois renderizadores |
| 8 | Feedback Admin/Config | Estado e autorização | Fronteiras V5 e auth comprovadas |

#### Protocolo repetível por família

1. Identificar problema de manutenção.
2. Demonstrar consumidores com a mesma responsabilidade.
3. Localizar regras atuais e sua ordem.
4. Identificar variantes legítimas.
5. Medir baseline por tema/estado.
6. Formular hipótese de extração.
7. Criar patch mínimo.
8. Executar testes estáticos.
9. Executar testes browser dos consumidores.
10. Comparar CSSOM e capturas pertinentes.
11. Investigar diferenças não aprovadas.
12. Medir benefício.
13. Integrar.
14. Revalidar árvore integrada.
15. Encerrar duplicações ou exceções.
16. Decidir se a família seguinte continua justificável.

Uma família poderá terminar como `REJECTED` sem representar fracasso do programa. A rejeição é correta quando demonstra que manter duas implementações simples é superior a criar uma abstração compartilhada.

---

# 6. Engenharia dos testes — bundles específicos deste capítulo

## 6.1 BT-CSS-0 — Integridade e preflight

**Executar em todo pacote de CSS.**

Garantias:

1. SHA e branch-base registrados.
2. Diff restrito ao pacote.
3. Arquivos esperados presentes.
4. Sintaxe e parsing válidos.
5. Artefatos gerados sincronizados.
6. Pins íntegros.
7. Build reproduzível quando o pacote altera build/imports.
8. Nenhuma mudança inesperada de schema, backend ou assets.
9. Nenhum import proibido da paleta de referência.
10. Resultado com identificador da árvore testada.

Comandos existentes a reutilizar conforme o escopo:

- `npm run pages:check`
- `npm run build`
- Scripts específicos de pin e validação DS.

Não executar todo o build de assets por reflexo se o pacote não altera seus contratos e já existir uma prova suficiente de integridade; o planejamento de CI deverá definir essa fronteira explicitamente.

## 6.2 BT-CSS-1 — Equivalência de tokens e cascata

**Aplicar a aliases e extrações Tipo E.**

Garantias:

1. Mesmos consumidores antes/depois.
2. Mesmos valores computados quando equivalência estrita é exigida.
3. Mesma especificidade efetiva ou efeito equivalente demonstrado.
4. Ordem correta das folhas.
5. Ausência de override inesperado.
6. Variáveis resolvidas, sem fallback acidental.
7. Tema claro/escuro preservado.
8. Foco/hover preservados onde aplicáveis.
9. Nenhum consumidor não autorizado afetado.
10. Controle negativo sem alteração.

Um teste de string CSS pode complementar a prova, mas não substitui CSSOM quando o risco está na cascata.

## 6.3 BT-CSS-2 — Correções de contraste

**Aplicar a mudanças Tipo I.**

Garantias:

1. Defeito original reproduzido.
2. Elemento visível e estado válido.
3. Cor do texto computada.
4. Cadeia de fundos identificada.
5. Transparência e composição consideradas.
6. Critério de contraste adequado ao elemento.
7. Correção aplicada somente no contexto autorizado.
8. Resultado visual inspecionado quando necessário.
9. Tema e estados não alterados verificados.
10. Evidência do head candidato.
11. Evidência da integração quando a árvore mudar.

Para fundos complexos, não aceitar uma razão calculada de duas propriedades CSS isoladas como prova definitiva.

## 6.4 BT-CSS-3 — Raster e geometria

**Aplicar quando houver risco de mudança espacial ou composição.**

Garantias:

1. Baseline e candidata usam o mesmo viewport.
2. DPR, zoom, fonte e preferência de movimento controlados.
3. Estado de aplicação e dados equivalentes.
4. Imagens carregadas ou falhas tratadas explicitamente.
5. Transições estabilizadas.
6. Diferenças restritas às áreas intencionais.
7. Regiões não relacionadas preservadas.
8. Evidência de referência humana quando a decisão for visual.
9. Tolerâncias justificadas.
10. Arquivos e hashes dos resultados preservados.

Testes sintéticos que aplicam duas regras ao mesmo DOM são úteis para containment, mas devem ser identificados como tal. Não equivalem automaticamente a um diff de duas versões publicadas da aplicação.

## 6.5 BT-CSS-4 — Seleção, foco e estados dinâmicos

**Aplicar a controles de seleção, swatches, tema e componentes interativos.**

Garantias:

1. Estado inicial correto.
2. Interação efetiva altera o estado esperado.
3. Estilo selecionado corresponde ao estado.
4. ARIA consistente.
5. Teclado e foco preservados.
6. Hover não destrói indicação de seleção.
7. Tema muda sem perder estado.
8. Re-render não remove feedback necessário.
9. Controle global não interfere no controle local.
10. Dados V5 permanecem inalterados quando a alteração é visual.

## 6.6 BT-CSS-5 — Integração por consumidor

**Aplicar antes de declarar pacote `VERIFIED`.**

Garantias:

1. O patch final corresponde à mudança revisada.
2. Todos os consumidores obrigatórios foram exercitados.
3. Nenhum teste antigo foi promovido para outro SHA sem justificativa.
4. A árvore integrada passa nos testes selecionados.
5. Outros contratos co-carregados permanecem válidos.
6. A ordem final das folhas corresponde ao previsto.
7. Cache, imports e assets continuam resolvidos.
8. Exceções são registradas.
9. O resultado não depende de alteração local não commitada.
10. O rollback continua disponível.

---

# 7. Política de ambientes e cobertura

## 7.1 Matriz mínima sugerida

As dimensões abaixo são ponto de partida, não exigência universal.

| Mudança | Engines | Viewports iniciais | Estados |
|---|---|---|---|
| Alias técnico simples | Chromium | 390 e 1366 | Light/dark, foco quando pertinente |
| Token contextual público | Chromium + WebKit | 390, 768, 1366 | Light/dark, conteúdo carregado |
| Contraste Admin | Chromium + browser hospedado quando necessário | Contexto responsivo do defeito | Light/dark, controle ativo |
| Swatch selecionado | Chromium | 390 e 1366 | Light/dark, hover/foco, duas amostras |
| Header e controles públicos | Chromium + WebKit | Breakpoints críticos NAV | Menu/foco/tema/contato |
| Cena/hotspot | Conforme a família | Layouts reais de Config/Viewer | Seleção, teclado, tema, geometria |

A matriz deverá ser expandida quando o comportamento real, o histórico de bugs ou a homologação exigirem.

## 7.2 Reutilização de infraestrutura

Os workflows existentes já utilizam Playwright e servidores HTTP locais, mas nem todos possuem exatamente a mesma versão do browser client.

Por exemplo, há workflows com Playwright 1.62.1 e o gate raster VIS-002C usa imagem/browser client 1.56.0.

Essa diferença não comprova defeito. Entretanto, precisa ser intencional e documentada se os resultados forem combinados como uma mesma prova.

### Melhorias propostas

1. Catalogar cada workflow, versão de browser e fixture.
2. Identificar onde vários jobs fazem instalação idêntica.
3. Reutilizar fixtures locais por job quando seus contratos são compatíveis.
4. Evitar criar servidor/browser novo para cada assertion.
5. Preservar isolamento de testes que modificam estado global.
6. Usar matriz única quando consumidores e dependências forem iguais.
7. Manter relatórios por contrato mesmo em processos compartilhados.
8. Não fundir resultados de SHAs diferentes.
9. Distinguir falha de infraestrutura de falha funcional.
10. Medir duração e estabilidade antes/depois de reorganizar workflows.

A arquitetura de testes não deve crescer mais do que a economia obtida.

---

# 8. Política de integração de mudanças CSS

## 8.1 Preparação da branch

Cada pacote deve:

1. Escolher branch-alvo.
2. Conferir merge-base e diferenças recentes.
3. Identificar arquivos já modificados por outra PR.
4. Selecionar trabalho independente quando houver disputa de arquivos.
5. Evitar misturar correção existente com nova extração.
6. Fixar baseline e testes.
7. Implementar em branch isolada.
8. Executar o gate focal.
9. Registrar o diff efetivo.
10. Reconciliar com a base atual antes de integrar.

## 8.2 Agrupamento de commits e PRs

**Agrupar no mesmo pacote quando:**

- As mudanças implementam um único contrato.
- Os consumidores estão identificados.
- O rollback pode acontecer em conjunto.
- Os testes precisam validar o mesmo comportamento.

**Separar quando:**

- Uma alteração é correção de bug e outra é refatoração equivalente.
- Existem autorizações diferentes.
- Os consumidores são independentes e os bloqueios distintos.
- Uma alteração envolve domínio/autorização e outra apenas CSS.
- Uma mudança tem risco muito superior à outra.
- Uma parte pode ser integrada enquanto a outra precisa permanecer em HOLD.

Não dividir um pacote apenas para manter “uma linguagem ou arquivo por PR”.

## 8.3 Preview e publicação

O fluxo preferencial será:

1. Testes estáticos e determinísticos.
2. Testes unitários/contratos.
3. Browser local com fixture.
4. Revisão do diff e artefatos.
5. Preview deliberado somente se for necessário.
6. Integração autorizada.
7. Readback no ambiente relevante.
8. Encerramento da entrega.

Previews não devem ser utilizados como substitutos de build local ou como ferramenta primária para descobrir erro simples.

Também não se deve evitar um Preview necessário ao ponto de declarar uma validação hospedada sem tê-la realizado.

---

# 9. Marcos claros de conclusão

| Marco | Resultado concreto | Dependências |
|---|---|---|
| **CSS-M0** | Baseline CSS confiável e 98 incertezas classificadas | CSS-00/01 |
| **CSS-M1** | Correções DS-04 priorizadas, integradas ou bloqueadas por motivo específico | CSS-02…05 |
| **CSS-M2** | Contrato DS→Produto operacional; tokens de referência e contextuais sem ambiguidade | TOK-00/01/02 |
| **CSS-M3** | Primeiro token compartilhado novo integrado com consumidores reais | TOK-03 |
| **CSS-M4** | Primeira foundation neutra consolidada | FND-01 |
| **CSS-M5** | Estados e primeiras famílias compartilháveis migrados | FND-02/03 |
| **CSS-M6** | Bundles de teste CSS estabilizados | BT-CSS-0…5 |
| **CSS-M7** | Integração comprovada na branch-alvo e duplicações encerradas por escopo | INT-01 |

### Critério do marco CSS-M7

O marco somente será fechado quando as mudanças planejadas para sua versão de escopo estiverem integradas e os consumidores relevantes testados.

Ele **não exige** o desaparecimento de toda exceção CSS ou de toda diferença contextual legítima entre interfaces.

---

# 10. Plano operacional sugerido

## Primeira janela — Destravar correções e obter a baseline

Executar CSS-00 e iniciar CSS-01.

Em paralelo, revisar a PR #271 quanto à sua prontidão e seus bloqueios reais.

**Resultados esperados:**

- Fotografias confiáveis das duas branches.
- Classificação inicial dos pares incertos.
- Lista de subgates realmente pendentes da #271.
- Separação dos casos `.module-number` e `#viewerHint`.

## Segunda janela — Consolidar tokens existentes

Executar TOK-00, TOK-01 e concluir o fechamento técnico de TOK-02.

**Resultados esperados:**

- Estado de distribuição de VIS-002 corretamente definido.
- VIS-002C contextual reconciliado com o consumo real.
- P-TOKEN-02A1 encerrado como refatoração equivalente, sem reivindicar homologação visual adicional.

## Terceira janela — Primeiras integrações novas

Selecionar TOK-03 e FND-01 a partir da matriz de ownership.

**Resultados esperados:**

- Um token compartilhado com valor demonstrável.
- Uma primitiva compartilhada de baixo risco.
- Duplicações reais eliminadas.
- Testes executados e integração comprovada.

## Quarta janela — Famílias e estados

Iniciar FND-02 e FND-03.

**Resultados esperados:**

- Estados com papéis claramente definidos.
- Componentes selecionados por equivalência semântica.
- Menor dependência de ajustes manuais repetidos.
- Ausência de globalização indevida.

## Quinta janela — Consolidar a engenharia de testes

Concluir BT-CSS e INT-01.

**Resultados esperados:**

- Conjuntos de testes mais reutilizáveis.
- Falhas de fixture identificadas antes de bloquear mudanças.
- Menor repetição de execução.
- Evidências diretamente ligadas ao pacote integrado.

Essas janelas representam conjuntos de dependências, não estimativas de calendário.

---

# 11. Pontos de interrogação

| ID | Pergunta | Método de resolução |
|---|---|---|
| CSS-Q01 | Quantos dos 98 pares são realmente distintos por causa técnica? | Classificação U1–U8 e agrupamento por cadeia de pintura |
| CSS-Q02 | Quais incertezas bloqueiam a primeira extração de foundation? | Interseção entre consumidores e propriedades alteradas |
| CSS-Q03 | A PR #271 deve integrar como unidade ou dividir-se por consumidor? | Avaliar dependências, evidência e rollback |
| CSS-Q04 | O CSS atual do Configurador pode ser validado com fixture hospedada sem alterar publicação real? | Contrato de fixture/auth e avaliação de segurança |
| CSS-Q05 | O alias de foco atual deve futuramente consumir a referência visual VIS-002? | Comparar contrato homologado, escopo e aparência atual |
| CSS-Q06 | A diferença `#viewerHint` entre branches é correção de bug ou divergência de intenção? | Inspecionar histórico, intenção homologada e CSSOM atual |
| CSS-Q07 | A `.module-number` pode utilizar token existente ou precisa de correção contextual? | Provar equivalência do papel e contraste por estado |
| CSS-Q08 | Há benefício real de extrair `.visually-hidden`? | Matriz de consumidores, especificidade e custo de manutenção |
| CSS-Q09 | Qual é a primeira família de botões cujo compartilhamento reduz duplicação sem alterar variantes? | G3, contratos semânticos e baseline visual |
| CSS-Q10 | Quais workflows repetem infraestrutura sem adicionar garantias próprias? | ARC-15: workflow → fixture → comando → assertion |
| CSS-Q11 | Quanto custam os gates atuais em duração e instabilidade? | Medição histórica de CI e comparação após reorganização |
| CSS-Q12 | O pin VIS-002C reflete corretamente sua condição de publicação atual? | Comparação entre manifesto, branch, build e deploy |
| CSS-Q13 | Quais exceções editoriais precisam permanecer fora dos tokens? | Revisão de decisões VIS e consumidores de conteúdo |
| CSS-Q14 | Quais estados exigem validação por dispositivo real? | Matriz de risco ARC-15, não enumeração universal |

---

# 12. Critérios de interrupção e rollback

Um pacote deve entrar em HOLD se:

- O consumidor necessário não pode ser observado de modo confiável.
- Há diferença de cascata não explicada.
- A fixture não satisfaz o contrato mínimo do renderer.
- Uma mudança Tipo E altera pixels ou comportamento fora do esperado.
- O valor pretendido depende de homologação ainda não concedida.
- A alteração afeta outras rotas e esses consumidores não estão identificados.
- O resultado depende de arquivo local não integrado ou de sessão não autorizada.

Deve ser rejeitado se:

- A extração cria mais overrides do que elimina responsabilidades duplicadas.
- A solução exige mudar V5 sem requisito de domínio real.
- O CSS compartilhado compromete uma variante homologada.
- É necessário aumentar a complexidade de build/runtime para resolver duplicação trivial.
- O benefício alegado é apenas reduzir a quantidade de arquivos ou linhas.
- O mecanismo introduz uma segunda fonte editável da mesma regra.

O rollback deverá preservar:

1. A decisão homologada.
2. O estado de domínio.
3. O histórico de evidências.
4. A possibilidade de reexecutar a validação.
5. Os consumidores não afetados.

---

# 13. Medição do progresso desta frente

Sugiro abandonar um percentual único de “CSS concluído” enquanto os contratos não estiverem mapeados.

Acompanharemos quatro medidas separadas:

**Cobertura de classificação:** famílias e pares com causa, consumidor e estado conhecidos.

**Cobertura de implementação:** responsabilidades efetivamente consolidadas.

**Cobertura de validação:** alterações com provas adequadas ao risco.

**Cobertura de integração:** consumidores migrados e revalidados na branch-alvo.

O percentual de integração não crescerá com um novo relatório CSSOM, a menos que esse relatório permita efetivamente encerrar uma obrigação do pacote.

Também não crescerá porque um teste passou numa branch candidata sem integração correspondente.

### Métricas de eficiência a coletar

- Tempo médio desde `READY` até `INTEGRATED`.
- Tempo gasto em reconciliação de bases.
- Número de execuções de browser por pacote.
- Percentual de falhas causadas por fixture/precondição.
- Número de revalidações do mesmo contrato.
- Tempo de CI por bundle.
- Número de PRs que permanecem abertas sem bloqueio explícito.
- Quantidade de duplicações efetivas resolvidas.
- Quantidade de exceções legítimas preservadas.
- Frequência de regressões após integração.

Essas métricas serão definidas precisamente na Parte VI, sem inventar metas numéricas antes de medir o baseline.

---

# 14. Parecer final — Parte III

A fundação CSS não está tão distante quanto uma leitura literal dos HOLDs globais sugere.

Já existem:

- Exportação determinística de paleta.
- Pins e verificações de proveniência.
- Tokens contextuais restritos.
- Um alias técnico de foco.
- Testes de CSS computado.
- Testes rasterizados.
- Matrizes de contraste.
- Instrumentação de tema, viewport e estado.
- Correções candidatas relativamente pequenas.

O obstáculo principal é a falta de uma passagem suficientemente curta entre essas capacidades e a integração efetiva.

**A reforma recomendada é dividir a frente em três movimentos:**

1. **Concluir correções comprovadas**, sem acoplá-las à extração arquitetural.
2. **Consolidar responsabilidades já equivalentes**, com provas locais e consumidores conhecidos.
3. **Expandir foundations e componentes gradualmente**, apenas quando houver ganho concreto e testes apropriados.

A existência de 98 pares incertos justifica uma investigação organizada, não um embargo geral.

Da mesma forma, a paleta VIS-002 aprovada justifica uma fonte canônica, não sua aplicação automática a todas as páginas.

A melhor arquitetura continuará sendo aquela com menos autoridades independentes para a mesma responsabilidade, não necessariamente aquela com maior quantidade de tokens ou componentes compartilhados.

---

## Referências técnicas principais

- [Exportador de paleta VIS-002 no Design System](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/scripts/export-approved-palette.mjs)
- [Manifesto de referência VIS-002](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/dist/approved-palette-reference.manifest.json)
- [Pin de referência do Produto](https://github.com/EAKerber/MobiliPresenter2D/blob/development/design-system/pins/vis-002/v0.1.0/PIN.json)
- [Mapeamento VIS-002C v0.3](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/VIS002C_CONTEXTUAL_MAPPING_V0_3_0.json)
- [Pin contextual do Produto](https://github.com/EAKerber/MobiliPresenter2D/blob/development/design-system/pins/vis-002/context-v0.3.0/PIN.json)
- [Workflow de contraste público](https://github.com/EAKerber/MobiliPresenter2D/blob/development/.github/workflows/development-public-contrast-semantic.yml)
- [Teste raster VIS-002C](https://github.com/EAKerber/MobiliPresenter2D/blob/development/tests/vis002c-v03-scoped-raster.mjs)
- [DS-05A — comparação de CSS e incertezas](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/evidence/architecture/ds05a-current-product-css-provenance-2026-11-15.md)
- [PR #271 — correções DS-04](https://github.com/EAKerber/MobiliPresenter2D/pull/271)
- [Issue #208 — cobertura de temas e contrastes](https://github.com/EAKerber/MobiliPresenter2D/issues/208)
- [Issue #216 — pares contextuais públicos](https://github.com/EAKerber/MobiliPresenter2D/issues/216)

**Limite da auditoria:** foram examinadas fontes CSS, scripts, manifestos, workflows, issues, PRs e evidências registradas. Não foram executadas novas medições CSSOM ou browsers neste turno. Os valores medidos aqui citados pertencem aos recibos existentes e devem ser revalidados nos novos heads quando cada pacote avançar.

---

<a id="capitulo-4"></a>
# Capítulo IV — Componentes, composição de páginas e ciclo de vida dos controladores

## 1. Objetivo arquitetural

Consolidar a apresentação do MobiliPresenter2D em componentes com responsabilidades claras, reutilização efetiva e ciclo de vida previsível.

A arquitetura-alvo deve permitir modificar uma única implementação de um componente compartilhado e propagar o resultado aos seus consumidores, sem exigir edições repetidas.

Essa centralização deve ocorrer em três níveis distintos:

1. **Valores e papéis visuais:** definidos pelo Design System e distribuídos por tokens e contratos autorizados.
2. **Estrutura e comportamento de interface:** concentrados em componentes, fragmentos e controladores compartilhados.
3. **Dados e regras de negócio:** preservados nas respectivas fontes de domínio, com apresentação desacoplada.

O primeiro e o segundo níveis devem ser reutilizados sempre que os consumidores possuírem o mesmo contrato. O terceiro não deve ser remodelado apenas para facilitar a reutilização visual.

### 1.1 Resultados exigidos

Ao concluir esta frente:

- Cada componente compartilhável terá uma fonte de implementação identificável.
- Cada página terá um contrato explícito de composição.
- Menus públicos e privados terão responsabilidades separadas e consistentes.
- Tema e marca terão um mecanismo compartilhado, com slots por contexto.
- Os controladores não registrarão listeners duplicados quando sujeitos a reinicialização.
- As páginas estáticas preservarão seu HTML essencial sem JavaScript.
- Os componentes dinâmicos manterão seus contratos de domínio.
- Testes serão aplicados ao componente e aos consumidores que realmente dependem dele.
- Cada pacote terá DoD próprio, integração rastreável e rollback delimitado.

### 1.2 Objetivos que deliberadamente não perseguiremos

Esta frente não tem como objetivo:

- Adotar React, Vue ou outro framework de interface.
- Transformar todas as páginas em uma SPA.
- Construir um page builder universal.
- Converter todo HTML em JSON.
- Reescrever o schema de administração para padronizar a apresentação.
- Tornar o Viewer e o Configurador idênticos visualmente.
- Substituir controles nativos por componentes personalizados sem necessidade.
- Eliminar qualquer diferença entre páginas que compartilham o mesmo componente base.

O objetivo é centralização de responsabilidades reais, não uniformidade artificial.

---

## 2. Diagnóstico atualizado da composição existente

### 2.1 Páginas públicas: existe composição compartilhada em build-time

O Produto já possui o compilador:

`scripts/compile-primary-pages.mjs`

Ele utiliza:

- `architecture/pages/root.page.html`
- `architecture/pages/about.page.html`
- `architecture/pages/how-it-works.page.html`
- `architecture/fragments/primary-header.fragment.html`
- `architecture/fragments/primary-header.routes.json`

Os artefatos gerados são:

- `app/index.html`
- `app/about/index.html`
- `app/how-it-works/index.html`

O script registra hashes de fonte e saída no manifesto e verifica desvio entre o HTML autoral e os artefatos gerados.

Isso constitui uma implementação real da direção ARC-03C: uma fonte de composição para três páginas públicas.

**Consequência para o plano:** a próxima etapa não é criar outro mecanismo de templates, mas consolidar e utilizar corretamente o mecanismo já existente.

### 2.2 O Viewer possui um header secundário distinto

A rota `/viewer/` não participa do compilador das três páginas.

O código atual da `development` possui:

- `.viewer-header`
- `.viewer-header__context`
- `.viewer-header__actions`
- `.back-link`
- `#menuToggle`
- `#primaryNav`
- O controle de tema injetado pelo mecanismo compartilhado

O teste `tests/viewer-secondary-header-browser-gate.mjs` especifica a ordem:

**Marca à esquerda; Ambientes, tema e menu à direita.**

Também verifica que o Viewer não deve marcar “Ambientes” como a página corrente da navegação principal.

Essa distinção não é uma exceção temporária: é um contrato homologado para uma página de segunda profundidade.

### 2.3 O menu público já possui um controlador comum

O Produto utiliza:

`app/landing/header-menu.js`

Ele implementa:

- Abertura e fechamento.
- Atualização de `aria-expanded`.
- Fechamento por Escape.
- Fechamento por interação fora do menu.
- Fechamento ao selecionar um link.
- Posicionamento responsivo do CTA de contato.
- Comportamentos de foco em transições de layout.

A auditoria histórica UI-ADR-005 já demonstrou a viabilidade de reutilizar esse controlador nas três páginas públicas sem converter o header para um renderer JavaScript.

A próxima tarefa é verificar sua autoridade e seus consumidores atuais, não refazer o piloto.

### 2.4 O controlador de tema já é transversal

O arquivo:

`app/core/ui-theme.js`

é utilizado em páginas públicas, Viewer e áreas privadas.

Ele administra:

- Preferência `auto`, `light` e `dark`.
- Resolução a partir da preferência do sistema.
- Persistência local.
- Atualização de atributos no documento.
- Controle visual de tema.
- Alternância dos assets da marca.
- Inserção do controle em diferentes posições do DOM.

Há, portanto, centralização real de comportamento.

O principal débito arquitetural é que os slots são determinados parcialmente por consultas estruturais ao documento. Isso funciona, mas cria dependência implícita entre controlador e markup.

A extração de slots explícitos é candidata, não prioridade incondicional.

### 2.5 O menu privado não equivale ao público

O arquivo:

`app/core/private-navigation.js`

depende de identidade, sessão e papéis de acesso.

Ele constrói links segundo a condição do usuário, apresenta informações de conta e incorpora logout.

Também possui mecanismo de revisão para impedir que respostas assíncronas antigas substituam o estado de sessão mais recente.

**Não deve ser substituído pelo controlador público.**

O compartilhamento possível fica restrito a primitivas visuais ou contratos de acessibilidade demonstravelmente equivalentes.

### 2.6 Viewer e Configurador já compartilham um componente de cena

O arquivo:

`app/core/scene-component.js`

expõe `CasaModulesSceneComponent`.

Entre suas responsabilidades:

- Renderização de layers.
- Renderização e atualização de hotspots.
- Frame de seleção.
- Estilos de acabamento.
- Navegação por teclado.

O Viewer consome esse componente por intermédio de `app/viewer/scene-adapters.js`.

O Configurador o utiliza diretamente em `app/app.js`.

Isso é reutilização real e de valor elevado.

A oportunidade de melhoria está em delimitar lifecycle e variantes de apresentação, não em criar um segundo renderer compartilhado.

### 2.7 O Configurador já possui um contrato de componentes

O arquivo:

`app/core/presentation-contract.js`

define o schema `ConfiguratorPresentation2D 1.1`.

Entre os componentes permitidos:

- `choice-swatches`
- `choice-grid`
- `choice-cards`
- `selection-list`
- `toggle-list`
- `action-list`

Existem ainda contratos para `detail-panel`, relações e projeções por layout.

O ganho arquitetural aqui está em completar o alinhamento entre contrato, renderer, estado e estilos, não em reescrever as seções em um novo formato genérico.

---

## 3. Arquitetura-alvo

### 3.1 Quatro categorias de componentes

#### Categoria A — Foundations e primitivas

Responsabilidades pequenas e comprovadamente transversais.

Exemplos:

- Tokens semânticos.
- Utilitário de texto visualmente oculto.
- Foco básico.
- Tratamento de mídia comum.
- Comportamentos genéricos mínimos de controle nativo.

São as partes com maior possibilidade de compartilhamento amplo.

#### Categoria B — Componentes de apresentação

Possuem significado visual/semântico consistente, mas podem apresentar variantes.

Exemplos:

- Botão de ação pública.
- Rótulo editorial.
- Header público.
- Logo em seu slot.
- Controle de tema.
- Mensagem de feedback.

Um componente pode ter diferentes variantes sem exigir código completamente distinto.

#### Categoria C — Adaptadores de domínio

Transformam um contrato de domínio em apresentação.

Exemplos:

- Hotspot de cena.
- Controle de acabamento.
- Cartão selecionável de módulo.
- Linha de preço.
- Painel de detalhes de módulo.
- Controle de disponibilidade administrativa.

Esses componentes recebem dados e estado de domínio, mas não se tornam donos da política comercial.

#### Categoria D — Composições de página

Organizam componentes e conteúdo em uma rota específica.

Exemplos:

- Seções editoriais da Landing.
- Blocos da página Como funciona.
- Shell do Viewer.
- Workspace do Configurador.
- Editor administrativo.

Composição de página não precisa ser uma entidade JavaScript. Pode ser HTML autoral compilado com fragmentos.

### 3.2 Estrutura lógica proposta

A seguinte representação descreve responsabilidades. Não é uma exigência para criar todas essas pastas:

```text
Design System
  ├── Decisões homologadas
  ├── Valores e tokens canônicos
  └── Contratos de componente
           │
           ▼
Produto
  ├── Foundations
  │    ├── Tokens distribuídos
  │    └── Utilitários compartilhados
  │
  ├── Componentes de apresentação
  │    ├── Header público
  │    ├── Controle de tema
  │    ├── Marca
  │    └── Botões e estados
  │
  ├── Composição estática
  │    ├── Home
  │    ├── Quem somos
  │    └── Como funciona
  │
  ├── Adaptadores de domínio
  │    ├── Cena/hotspots
  │    ├── Opções de apresentação V5
  │    └── Visualização de módulos
  │
  └── Aplicações específicas
       ├── Viewer
       ├── Configurador
       ├── Admin
       └── Access
```

### 3.3 Regra de compartilhamento

Dois consumidores devem compartilhar uma implementação quando possuem:

1. A mesma responsabilidade semântica.
2. Contrato de entrada compatível.
3. Estados equivalentes.
4. Comportamento de interação compatível.
5. Critérios de acessibilidade compatíveis.
6. Ciclo de vida compatível.
7. Um ganho concreto de manutenção.

A coincidência de classes CSS não satisfaz esses critérios.

Em contrapartida, **diferenças de posição ou aparência não são motivo suficiente para impedir compartilhamento**, quando representam variantes de um mesmo componente.

Essa última condição é importante para evitar a fragmentação excessiva que também existe no projeto.

---

## 4. Sequência de execução

### Marco CMP-M0 — Ownership de DOM, comportamento e estado

#### CMP-001 — Criar o inventário operacional dos componentes

**Prioridade:** P0  
**Tipo:** auditoria de arquitetura  
**Dependências:** baseline CSS da Parte III  
**Contrato:** ARC-05, ARC-07

##### Objetivo

Transformar o inventário histórico de DOM/JS em um mapa de componentes utilizável para execução.

##### Procedimento

1. Fixar os commits analisados.
2. Listar os shells de todas as rotas.
3. Identificar o HTML autoral de cada uma.
4. Identificar o compilador ou renderer responsável pela materialização.
5. Identificar os controladores JavaScript que operam sobre o DOM.
6. Identificar os arquivos CSS carregados no mesmo contexto.
7. Registrar o domínio responsável pelos dados.
8. Detectar classes e IDs introduzidos dinamicamente.
9. Registrar eventos e listeners relevantes.
10. Identificar a origem dos textos visíveis.
11. Separar classes homônimas de componentes efetivamente equivalentes.
12. Identificar componentes que já possuem implementação compartilhada.
13. Registrar variantes legítimas por rota.
14. Mapear quais componentes dependem de autenticação.
15. Mapear quais dependem de projeção pública V5.
16. Criar relações componente → consumidores → testes.
17. Classificar os candidatos de extração.
18. Registrar exceções e lacunas de runtime.
19. Definir uma ordem de migração que minimize conflitos entre arquivos.
20. Publicar o resultado como referência para os demais pacotes.

##### Classificação obrigatória

Cada candidato receberá uma das seguintes classificações:

- `shared-existing`: compartilhamento já implementado.
- `shared-candidate`: bom candidato a compartilhamento.
- `variant-of-shared`: variante de componente comum.
- `domain-specific`: pertence a um domínio.
- `editorial-specific`: pertence à composição editorial.
- `homonym`: nome semelhante, contrato diferente.
- `unresolved`: requer prova adicional.

##### Bundle

BT-CMP-00 — inventário de source/DOM/CSS.

##### DoD específico

Todo componente priorizado possui owner, consumidores, fonte de estado, variantes, risco e testes relacionados.

---

### Marco CMP-M1 — Composição pública determinística

#### CMP-002 — Consolidar ARC-03C como autoridade das três páginas

**Prioridade:** P0  
**Tipo:** fechamento de implementação existente  
**Dependências:** CMP-001  
**Contrato:** ARC-03, ARC-04, ARC-10

##### Objetivo

Garantir que a composição compartilhada de Home, Quem somos e Como funciona seja aplicada como mecanismo permanente, não apenas como piloto.

##### Procedimento

1. Confirmar o compilador vigente e seus três consumidores.
2. Validar os hashes das fontes autorais.
3. Validar o fragmento compartilhado do header.
4. Conferir o manifesto de rotas.
5. Identificar todos os campos específicos de cada rota.
6. Conferir que cada página possui exatamente um ponto de inserção do header.
7. Verificar que a marca permanece acessível sem JavaScript.
8. Verificar que os links possuem destinos corretos.
9. Conferir a indicação `aria-current` da página apropriada.
10. Verificar que as diferenças autorizadas de markup são preservadas.
11. Executar o compilador com `--check`.
12. Executar os testes negativos de entrada inválida.
13. Confirmar que uma edição de fonte sem atualização do artefato produzido gera falha.
14. Validar os três HTMLs publicados.
15. Conferir que o build utilizado pelo deploy executa a verificação esperada.
16. Verificar se arquivos gerados são alterados manualmente em outras PRs.
17. Definir a correção desse procedimento nas instruções de contribuição.
18. Confirmar que o mecanismo não alcança o Viewer ou as páginas privadas.
19. Encerrar apenas as obrigações cobertas por esse conjunto.
20. Preservar histórico e rollback dos artefatos.

##### Comandos existentes

- `npm run pages:check`
- `npm run pages:sync`
- `npm run build`

O comando `pages:sync` é uma operação de escrita nos arquivos gerados. Deve ser executado apenas quando houver alteração intencional da fonte autoral, e seu diff precisa ser revisado.

##### Testes

- `tests/arc03c-source-authority.test.mjs`
- `tests/arc03c-historical-prototype-guards.test.mjs`
- `tests/arc03c-published-pages-browser-differential.mjs`
- Gate de header público aplicável.

##### Controle negativo

As páginas `/viewer/`, `/config/`, `/admin.html`, `/access/` e `/access/manage.html` não podem ser modificadas pela compilação.

##### DoD específico

Existe uma única fonte autoral por página e por fragmento compartilhado; os artefatos publicados coincidem com ela; os testes de drift e isolamento passam.

---

#### CMP-003 — Consolidar o controlador único do menu público

**Prioridade:** P0  
**Tipo:** consolidação de implementação existente  
**Dependências:** CMP-002  
**Contrato:** ARC-05, ARC-06, NAV-004

##### Objetivo

Eliminar possíveis autoridades concorrentes do menu nas páginas públicas e assegurar comportamento idêntico quando o contrato é o mesmo.

##### Procedimento

1. Identificar todos os scripts carregados nas três páginas.
2. Confirmar que somente `header-menu.js` controla o menu público.
3. Procurar handlers duplicados nos JS editoriais.
4. Conferir inicialização única.
5. Verificar referências a `#menuToggle` e `#primaryNav`.
6. Testar o estado inicial fechado.
7. Testar abertura e atualização de `aria-expanded`.
8. Testar abertura por teclado.
9. Verificar posicionamento inicial do foco.
10. Testar Escape e retorno de foco.
11. Testar fechamento por clique fora.
12. Testar fechamento ao selecionar um link.
13. Testar mudanças de largura enquanto o menu está aberto.
14. Verificar reposicionamento responsivo do CTA.
15. Garantir que o CTA não perde foco ao mudar de região.
16. Confirmar que o contato continua disponível nos breakpoints homologados.
17. Verificar coexistência com o controle de tema.
18. Confirmar ausência de listeners duplos.
19. Verificar que a Landing preserva o comportamento próprio do carrossel.
20. Integrar somente diferenças efetivamente necessárias.

##### Consideração de lifecycle

O controlador atual é executado por uma IIFE sobre uma página estática.

Não existe necessidade automática de introduzir uma API `destroy()` nesse caso.

O contrato mínimo deve ser:

- Uma inicialização por documento.
- Nenhum segundo controlador sobre o mesmo header.
- Listeners compatíveis com a vida da página.
- Nenhum listener órfão em caso de reutilização futura.

Se a aplicação passar a remontar o header sem recarregar a página, a exigência de limpeza será reavaliada.

##### Testes

- `tests/public-header-controller-gate.mjs`
- Contratos públicos de navegação.
- Chromium/WebKit nos cenários relevantes.

##### Controle negativo

Não alterar as funções de carrossel, dados de ambientes, CTA comercial ou conteúdo editorial.

##### DoD específico

Os três consumidores utilizam um único controlador, com comportamento e semântica consistentes, sem regressões nas interações próprias das páginas.

---

#### CMP-004 — Fechar NAV-005 para o header público primário

**Prioridade:** P0  
**Tipo:** correção contextual e integração  
**Dependências:** CMP-002/003  
**Candidata existente:** PR #269

##### Objetivo

Concluir a padronização do header nas páginas públicas de primeira profundidade.

##### Contexto real

A PR #269 permanece Draft.

Seu escopo inclui:

- Escala do logo.
- CTA de contato no menu compacto.
- Semântica e foco.
- Responsividade em larguras muito estreitas.
- Contrato NAV-005.

Os workflows reportados no head atual da PR passaram, mas o histórico de validação visual não substitui automaticamente uma revisão do último SHA.

##### Procedimento

1. Fixar o head da PR e sua base.
2. Reconciliar a PR com o estado atual da `main`.
3. Revisar os 18 caminhos modificados.
4. Identificar arquivos gerados pelo compilador.
5. Conferir o fragmento do header.
6. Conferir o manifesto de rotas.
7. Confirmar que o diff não contém trabalho de UX-04.
8. Comparar o comportamento de menu antes/depois.
9. Verificar o CTA em 290/291 px e nos breakpoints intermediários relevantes.
10. Validar largura da marca sem deformar o asset.
11. Confirmar ausência de overflow horizontal.
12. Verificar foco do menu e do CTA.
13. Testar claro/escuro.
14. Testar zoom e aumento de fonte quando relevante.
15. Conferir que nenhum componente da Landing ficou coberto pelo header.
16. Conferir que a página Como funciona preserva suas interações.
17. Verificar o HTML gerado e seu manifesto.
18. Revisar os resultados de CI do head exato.
19. Identificar critérios pendentes para integração.
20. Revalidar somente as matrizes afetadas após ajustes.
21. Integrar com rollback isolado.
22. Executar readback nas rotas.
23. Atualizar a issue relacionada.
24. Encerrar os subgates comprovados.

##### Testes

BT-CMP-10 — header público: visual, teclado, responsividade e geração de páginas.

##### Controle negativo

Nenhuma mudança funcional em Viewer, Configurador ou headers privados.

##### DoD específico

Header primário homologado, gerado de fonte única, funcional nas três rotas e integrado sem alterações não relacionadas.

---

### Marco CMP-M2 — Variantes de navegação sem duplicação indevida

#### CMP-005 — Consolidar o header secundário do Viewer

**Prioridade:** P0  
**Tipo:** consolidação de contrato homologado  
**Dependências:** CMP-003 para comportamento comum; não depende da conclusão visual integral de CMP-004

##### Objetivo

Preservar a identidade de componente compartilhado sem perder o contexto próprio do Viewer.

##### Contrato obrigatório

No desktop e no mobile:

**Logo à esquerda. À direita: Ambientes → tema → menu.**

O menu deve continuar contendo as rotas públicas.

“Ambientes” é uma ação contextual de retorno, e não uma indicação de que o Viewer está na página ativa de Ambientes.

##### Procedimento

1. Inspecionar o header do Viewer na `main` e na `development`.
2. Confirmar a existência do link de retorno.
3. Confirmar sua posição em `.viewer-header__actions`.
4. Verificar a posição do controle de tema após a inicialização JS.
5. Confirmar a posição do toggle de menu.
6. Confirmar a presença de uma única marca.
7. Confirmar que não existe segundo header renderizado.
8. Conferir os destinos da navegação.
9. Confirmar ausência de `aria-current="page"` no menu do Viewer.
10. Testar abertura e fechamento do menu.
11. Testar Escape e interação fora.
12. Testar mudança de tema.
13. Validar a ordem visual e DOM dos controles.
14. Verificar ausência de colisões.
15. Validar largura mínima do logo.
16. Verificar que a linha do header não quebra indevidamente.
17. Testar larguras pequenas, intermediárias e desktop.
18. Inspecionar temas claro/escuro.
19. Conferir se scripts de menu ou tema foram carregados mais de uma vez.
20. Comparar o header integrado à versão homologada.
21. Registrar eventuais diferenças na PR correspondente.
22. Integrar somente se o contrato ainda não estiver presente na branch-alvo.
23. Revalidar o head resultante.

##### Testes existentes

`tests/viewer-secondary-header-browser-gate.mjs`

A matriz desse teste contempla Chromium e WebKit em 320, 390, 486, 768 e 1366 px, nos dois temas.

Trata-se de um excelente candidato a gate permanente do componente.

##### Controle negativo

Não modificar seleção de módulo, projeção pública, preço, medidas, cena ou links de autenticação.

##### DoD específico

O Viewer conserva a variante NAV-005 de segunda profundidade, com ordem espacial e semântica comprovadas na branch-alvo.

---

#### CMP-006 — Formalizar a fronteira do header privado

**Prioridade:** P1  
**Tipo:** contrato de componente e segurança  
**Dependências:** CMP-001  
**Contrato:** NAV-005 privado, ARC-06 e ARC-12

##### Objetivo

Centralizar o comportamento de menu privado que pode ser compartilhado, preservando regras de sessão e autorização.

##### Procedimento

1. Mapear o DOM em `/config/`.
2. Mapear o DOM em `/admin.html`.
3. Mapear o DOM em `/access/manage.html`.
4. Identificar elementos com `data-private-header`.
5. Conferir que todos usam a mesma autoridade de menu.
6. Mapear links estáticos, condicionais e dependentes de papéis.
7. Identificar estados anônimo, carregando, autenticado, sessão temporária e acesso negado.
8. Verificar os caminhos de login e logout.
9. Inspecionar a função de reconciliação de sessão.
10. Confirmar o uso do contador de revisão para respostas assíncronas.
11. Simular respostas de autenticação fora de ordem.
12. Confirmar que uma resposta antiga não restaura links privados indevidamente.
13. Verificar renderização de links para cada papel autorizado.
14. Verificar que links ausentes da interface não são confundidos com autorização backend.
15. Testar abertura/fechamento.
16. Testar Escape, clique fora e foco.
17. Confirmar que a troca de tema não altera sessão ou permissões.
18. Verificar fallback seguro de erro de serviço.
19. Comparar variantes visuais de Config, Admin e Access.
20. Extrair apenas as primitivas comprovadamente compartilháveis.
21. Manter renderização de links condicionais como responsabilidade privada.
22. Executar testes de sessão e regressão.
23. Integrar com rollback próprio.

##### Risco específico

Não simplificar a lógica de sessão apenas porque ela parece mais complexa do que o controlador público.

A complexidade adicional tem uma finalidade diferente: evitar estado de navegação inconsistente durante autenticação assíncrona.

##### Testes

BT-CMP-20 — navegação privada e sessão.

##### DoD específico

Os três consumidores apresentam o conjunto correto de ações por estado, sem regressão de autenticação e sem dependência do controlador público.

---

#### CMP-007 — Consolidar o mecanismo de tema e os slots de inserção

**Prioridade:** P1  
**Tipo:** simplificação de contrato  
**Dependências:** CMP-001 e CMP-005/006 para análise de slots

##### Objetivo

Manter uma única autoridade para a preferência de tema e eliminar dependências estruturais desnecessárias quando houver ganho claro.

##### Diagnóstico

O controlador atual já identifica vários tipos de posição:

- Ações do header público.
- Ações do Viewer.
- Ações privadas.
- Região de introdução do Viewer.
- Fallback para headers isolados.

Essa flexibilidade possibilitou reutilização sem exigir alteração prévia de todas as páginas.

Por outro lado, cada nova estrutura pode requerer mais uma condição estrutural dentro do controlador.

##### Procedimento

1. Enumerar todos os consumidores de `ui-theme.js`.
2. Identificar a posição atual do controle em cada rota.
3. Registrar se o controle é inserido por JS ou já existe no HTML.
4. Inspecionar como o controlador escolhe o slot.
5. Listar consultas estruturais que dependem de classes circunstanciais.
6. Identificar slots que já possuem marcadores estáveis.
7. Medir se uma anotação explícita simplificaria o algoritmo.
8. Construir proposta mínima de atributo para os consumidores pertinentes.
9. Evitar alterar todas as páginas se uma única regra atual já for estável.
10. Comparar o DOM antes/depois da inicialização.
11. Testar inicialização única.
12. Verificar alternância `auto → light → dark`.
13. Verificar preferência do sistema.
14. Verificar persistência e evento `storage`.
15. Confirmar aplicação antecipada do tema, evitando flash desnecessário.
16. Verificar a marca correta em cada tema.
17. Testar controle de teclado.
18. Verificar alinhamento responsivo do slot.
19. Confirmar que o Viewer mantém a ordem NAV-005.
20. Confirmar que o menu privado não é deslocado inadequadamente.
21. Avaliar custo da mudança contra a implementação atual.
22. Se o custo for maior que o benefício, preservar a estrutura atual e registrar o contrato.
23. Integrar somente uma simplificação comprovadamente útil.

##### Regra de decisão

Não criar uma API de mount universal do tema se os slots atuais forem suficientemente explícitos e estáveis.

##### Testes

- `tests/ui-theme-contract.cjs`
- `tests/ui-theme-focus-token-contract.cjs`
- Matriz de slots G3.
- Gates de header público, Viewer e menu privado quando afetados.

##### DoD específico

Tema centralizado, consumidores corretamente identificados e nenhuma divergência introduzida em marca, preferência ou navegação.

---

### Marco CMP-M3 — Identidade visual e controles de apresentação

#### CMP-008 — Consolidar a identidade da marca

**Prioridade:** P1  
**Tipo:** componente visual  
**Dependências:** CMP-001, CMP-007 e tokens da Parte III

##### Objetivo

Permitir que mudanças em assets homologados, tratamento de marca e variantes sejam propagadas por uma autoridade comum, sem impor uma geometria única a todos os slots.

##### Distinção necessária

Compartilhar:

- Fonte dos assets de marca.
- Regras de alternância claro/escuro.
- Nome e descrição acessíveis.
- Tratamento comum da imagem.
- Contrato de versões e fallback.

Preservar por variante:

- Dimensões do header público.
- Slot do header privado.
- Geometria do Viewer.
- Composição do hero.
- Logos comparativos em conteúdo editorial.

##### Procedimento

1. Identificar todas as imagens `data-brand-variant`.
2. Localizar o catálogo real dos assets homologados.
3. Verificar dimensões intrínsecas.
4. Confirmar qual variante cada tema utiliza.
5. Mapear as regras CSS por contexto.
6. Identificar dimensões redundantes versus necessárias.
7. Conferir textos alternativos e nomes acessíveis.
8. Verificar que o asset não é redimensionado com deformação.
9. Confirmar que o hero não está sendo tratado como logo de header.
10. Comparar marca antes/depois nos consumidores.
11. Validar fallback e carregamento.
12. Testar mudanças de tema.
13. Verificar breakpoints extremos.
14. Propor extração de uma primitiva somente quando houver valor real.
15. Preservar estilos próprios de posicionamento e tamanho.
16. Integrar a distribuição da marca sem alterar a composição editorial.
17. Revalidar os consumers.

##### DoD específico

Uma autoridade reconhecível para os assets e seu comportamento compartilhado; variantes dimensionais preservadas.

---

#### CMP-009 — Definir famílias de botões por contrato, não por classe

**Prioridade:** P2  
**Tipo:** consolidação de apresentação  
**Dependências:** CMP-001 e FND-02

##### Objetivo

Reduzir duplicação em botões e CTAs onde há semântica equivalente, sem fundir controles com responsabilidades distintas.

##### Famílias iniciais

| Família | Exemplos | Escopo |
|---|---|---|
| Botões públicos | CTA de navegação e contato | Shell público |
| Botões de edição | Salvar, adicionar, remover | Admin |
| Botões de configuração | Navegar, selecionar, aplicar | Configurador |
| Controles auxiliares | Tema, menu, paginação | Contratos próprios |
| Botões de cena | Hotspots | Renderer compartilhado |

##### Procedimento

1. Inventariar todas as classes `.button` e variantes.
2. Identificar elementos reais que usam essas classes.
3. Registrar se cada um representa ação ou navegação.
4. Conferir semântica de `<button>` versus `<a>`.
5. Identificar estados normal, hover, foco, disabled e loading.
6. Registrar cor, tamanho, padding, raio e tipografia computados.
7. Identificar diferenças autorizadas.
8. Agrupar somente controles com o mesmo papel.
9. Definir a parte verdadeiramente comum.
10. Definir variantes específicas.
11. Identificar responsabilidades de tema já cobertas por tokens.
12. Criar patch restrito à primeira família.
13. Confirmar a ausência de mudança fora do escopo.
14. Testar teclado e ativação.
15. Testar claro/escuro e responsividade.
16. Comparar capturas e CSSOM.
17. Medir simplificação conseguida.
18. Decidir se outra família pode consumir a mesma primitiva.
19. Rejeitar a generalização quando só houver homonímia.
20. Integrar de forma incremental.

##### DoD específico

Pelo menos uma família consolidada com consumidores reais, variantes explícitas e redução de responsabilidade duplicada demonstrada.

---

#### CMP-010 — Consolidar feedback de interface respeitando sua finalidade

**Prioridade:** P2  
**Tipo:** componentes de estado  
**Dependências:** CMP-001 e FND-02

##### Objetivo

Centralizar a apresentação de mensagens equivalentes, preservando a diferença entre avisos informativos, erro impeditivo e status operacional.

##### Contratos distintos

**Status informativo:** não exige interromper a interação.

**Erro recuperável:** comunica falha e oferece recuperação.

**Erro impeditivo:** impede que a operação continue com dados inválidos.

**Mensagem de sucesso:** confirma uma operação concluída.

**Estado de carregamento:** comunica espera ou processo em andamento.

Esses contratos não se tornam equivalentes apenas porque usam o mesmo elemento `<p>` ou as mesmas cores.

##### Procedimento

1. Inventariar regiões de feedback no Produto.
2. Identificar texto, prioridade e papel de cada região.
3. Mapear `role="alert"` e regiões `aria-live`.
4. Identificar quais mensagens são persistentes ou transitórias.
5. Distinguir mensagens geradas por falha real e por estado de interface.
6. Conferir os métodos de atualização dos textos.
7. Identificar o owner da ação que produz o feedback.
8. Separar o aspecto visual da decisão de negócio.
9. Propor uma primitiva comum quando apropriado.
10. Preservar diferenças de anúncio acessível.
11. Testar sucesso, erro, loading e retry.
12. Testar alternância de tema.
13. Confirmar a ordem de foco.
14. Confirmar que operações bloqueadas não parecem concluídas.
15. Validar casos protegidos com fixture adequada.
16. Integrar apenas os consumidores equivalentes.

##### Controle negativo

Não modificar autorização, validação, persistência ou política de erro.

##### DoD específico

Estados comuns possuem apresentação consistente; os significados operacionais e os anúncios acessíveis permanecem corretos.

---

### Marco CMP-M4 — Composição editorial e controladores locais

#### CMP-011 — Revisar o piloto declarativo da Landing

**Prioridade:** P2  
**Tipo:** decisão de arquitetura  
**Dependências:** CMP-001

##### Contexto

O experimento histórico de benefícios da Landing mostrou que a extração declarativa funcionava em Node, Chromium e WebKit.

Entretanto, o protótipo `PageCompositionExperimental 0.1` adicionava mais de dez mil caracteres de infraestrutura nos arquivos comparados para abstrair um conjunto pequeno de benefícios.

O parecer UI-ADR-004 foi não promover esse mecanismo a registro universal.

##### Objetivo

Preservar os ganhos reais do experimento sem incorporar um custo arquitetural desproporcional.

##### Procedimento

1. Revisar o código atual de benefícios da Landing.
2. Identificar os conjuntos compactos e completos.
3. Verificar se os dados têm uma fonte realmente compartilhável.
4. Examinar as diferenças de renderização e estilo.
5. Comparar o código atual com o experimento.
6. Separar benefício de contrato e custo de infraestrutura.
7. Identificar duplicação de conteúdo editável.
8. Verificar se os dois grupos possuem a mesma fonte de verdade ou apenas conteúdo parecido.
9. Considerar uma função ou estrutura local simples.
10. Evitar importar o registro universal do experimento.
11. Testar número, texto e ordem dos benefícios.
12. Testar responsividade e ícones.
13. Verificar manutenção dos links e assets.
14. Medir custo e ganho de qualquer alteração.
15. Decidir integrar uma simplificação local ou manter a implementação atual.
16. Registrar decisão e disposição da branch experimental.
17. Não reabrir a discussão de framework sem novo requisito concreto.

##### Critério de retirada

Se não existir duplicação operacional relevante, encerrar o pacote como decisão de manutenção sem refatoração.

##### DoD específico

A intenção declarativa foi avaliada, a duplicação real foi tratada ou justificada, e o protótipo não fica indefinidamente como proposta concorrente.

---

#### CMP-012 — Consolidar o carrossel e a seleção de ambientes

**Prioridade:** P2  
**Tipo:** componente local da Landing  
**Dependências:** CMP-001 e CMP-011 para avaliação de dados

##### Objetivo

Garantir que a Landing possua um único fluxo coerente para seleção, imagem, descrição, disponibilidade e ação comercial.

##### Contexto técnico

O controlador atual já utiliza um contador de versão para evitar que a conclusão atrasada de um carregamento de imagem substitua uma seleção mais recente.

Esse mecanismo é apropriado e deve ser preservado.

##### Procedimento

1. Identificar a fonte de ambientes.
2. Confirmar que a renderização usa os dados previstos.
3. Registrar o estado de seleção.
4. Verificar que apenas os ambientes com destino válido apresentam CTA funcional.
5. Confirmar ordem e número dos cards.
6. Verificar mudança de ambiente por clique.
7. Verificar atualização de seleção e ARIA.
8. Testar carregamento e decodificação de imagens.
9. Simular imagens carregando fora de ordem.
10. Confirmar descarte de respostas antigas.
11. Testar falha de imagem.
12. Confirmar fallback sem ação indevida.
13. Testar alterações rápidas de seleção.
14. Verificar navegação de paginação.
15. Verificar estado responsivo.
16. Testar redução de movimento.
17. Testar o comportamento de dica/animação.
18. Confirmar que o menu compartilhado não interfere no carrossel.
19. Revisar event listeners e timers.
20. Fazer alterações somente para problemas comprovados.
21. Integrar e validar em navegador.

##### DoD específico

Seleção atômica e consistente, imagens e CTAs sincronizados, comportamento responsivo preservado e ausência de duplicação de controlador.

---

#### CMP-013 — Consolidar o painel expansível de Como funciona

**Prioridade:** P1  
**Tipo:** validação e eventual correção de componente editorial  
**Dependências:** CMP-001 e CMP-002

##### Objetivo

Garantir que abrir uma explicação não produza a aparência de que todos os cards foram expandidos simultaneamente.

##### Contexto

A implementação atual usa um painel único `#economyDetail`, reposicionado após a linha do card ativo de acordo com a quantidade de colunas CSS.

Isso constitui uma alternativa válida a criar uma expansão independente em todos os cards.

O importante é comprovar o comportamento no navegador.

##### Procedimento

1. Fixar a implementação atual e a versão homologada.
2. Identificar o grid de cards.
3. Identificar o painel de detalhes.
4. Confirmar que existe uma única instância do painel.
5. Verificar estado inicial fechado.
6. Selecionar o primeiro card.
7. Confirmar que somente ele informa `aria-expanded=true`.
8. Verificar o conteúdo apresentado.
9. Verificar o posicionamento do painel em relação à linha.
10. Selecionar outro card na mesma linha.
11. Selecionar outro card em linha diferente.
12. Confirmar que o painel não foi duplicado.
13. Fechar o card ativo.
14. Confirmar que o painel desaparece.
15. Redimensionar durante uma expansão.
16. Confirmar reposicionamento correto.
17. Testar mobile e desktop.
18. Testar foco e ativação por teclado.
19. Verificar estabilidade visual sem salto excessivo.
20. Comparar captura anterior/posterior se houver mudança de layout.
21. Corrigir somente o mecanismo responsável pelo defeito comprovado.
22. Executar o teste browser existente.
23. Integrar e repetir o cenário de regressão.

##### Teste existente

`tests/how-accordion-grid-browser-gate.mjs`

##### Controle negativo

Não modificar o texto comercial ou converter toda a página para um novo renderer.

##### DoD específico

Um único painel expansível, estado acessível coerente e layout estável nas larguras relevantes.

---

### Marco CMP-M5 — Componentes dinâmicos e fronteiras de domínio

#### CMP-014 — Formalizar o contrato compartilhado de cena e hotspots

**Prioridade:** P1  
**Tipo:** consolidação de componente de alto risco  
**Dependências:** CMP-001, baseline CSS, fixture de cena  
**Contrato:** ARC-05, ARC-06, ARC-11

##### Objetivo

Consolidar o componente compartilhado que já existe, separando claramente renderização, skin, seleção e ciclo de vida.

##### Responsabilidades compartilháveis

- Construir a estrutura básica de layers.
- Construir hotspots com atributos semânticos.
- Atualizar visibilidade e seleção.
- Calcular posições com a geometria existente.
- Produzir o frame de seleção.
- Aplicar aparência de materiais conforme contratos existentes.

##### Responsabilidades que permanecem especializadas

- Política de visibilidade do Configurador.
- Projeção pública permitida ao Viewer.
- Escolha e disponibilidade de materiais.
- Seleção e persistência de opções comerciais.
- Composição de layout do Viewer.
- Estado de edição ou configuração.

##### Procedimento

1. Identificar consumidores de `CasaModulesSceneComponent`.
2. Mapear o mount no Configurador.
3. Mapear o mount no adaptador do Viewer.
4. Identificar os elementos exigidos pelo renderer.
5. Confirmar ordem de layers.
6. Confirmar mapeamento de IDs e aliases.
7. Verificar o cálculo de posicionamento.
8. Confirmar ordem e prioridade de hotspots.
9. Verificar a construção de botões nativos.
10. Confirmar nomes acessíveis.
11. Confirmar `aria-pressed`.
12. Confirmar ocultação e desabilitação coerentes.
13. Verificar que o foco não alcança hotspots invisíveis.
14. Inspecionar z-index e sobreposição.
15. Testar seleção por ponteiro.
16. Testar seleção por teclado.
17. Confirmar que a seleção altera apenas o estado autorizado.
18. Testar alteração de acabamento.
19. Verificar máscara e frame de seleção.
20. Comparar skin do Viewer e skin do Configurador.
21. Identificar apenas as propriedades realmente compartilháveis.
22. Preservar as variantes visuais legítimas.
23. Conferir comportamento de cena sem assets completos.
24. Testar fallback de imagem e estados de erro.
25. Investigar como o listener de teclado é registrado.
26. Executar testes focais em ambos os consumidores.
27. Integrar alterações sem reescrever `Scene2D`.
28. Registrar riscos não encerrados.

##### Questão específica de lifecycle

A função `bindKeyboard()` registra um listener em `document`.

O código consultado não expõe uma função de remoção desse listener.

Isso não demonstra um bug por si só: se cada página chama o binding uma única vez, o listener poderá permanecer corretamente durante toda a vida do documento.

O risco surge se uma cena for remontada ou se a função for chamada repetidamente.

A ação correta será:

1. Identificar a quantidade de chamadas por ciclo real.
2. Testar remount quando ele é suportado pelo consumidor.
3. Se houver duplicação, implementar idempotência ou mecanismo de limpeza localizado.
4. Não introduzir uma arquitetura global de disposables apenas para resolver um binding.

##### Testes

BT-CMP-30 — cena/hotspots, ambos os consumidores.

##### DoD específico

Contrato compartilhado preservado, skins contextuais verificadas, seleção e foco corretos, ciclo de vida comprovado no uso real.

---

#### CMP-015 — Consolidar componentes de apresentação do Configurador

**Prioridade:** P1  
**Tipo:** integração entre contrato e renderer  
**Dependências:** CMP-001, CMP-014 e fixture Buyer V5  
**Contrato:** `ConfiguratorPresentation2D 1.1`

##### Objetivo

Garantir que os componentes permitidos pelo contrato de apresentação sejam renderizados e atualizados de maneira consistente, sem criar outro schema.

##### Procedimento

1. Recuperar os componentes aceitos pelo contrato.
2. Identificar as seções e comportamentos associados.
3. Localizar o renderer de cada componente.
4. Identificar regras de compatibilidade com apresentações legadas.
5. Confirmar validação de tipo de componente.
6. Confirmar validação de comportamento.
7. Identificar as relações e projeções por perfil.
8. Confirmar quais componentes podem ser exibidos simultaneamente.
9. Mapear os elementos DOM gerados.
10. Mapear classes e estados.
11. Identificar controle global versus controle local.
12. Confirmar que `choice-swatches` global e local não são confundidos.
13. Verificar `aria-pressed`, checked e disabled onde aplicável.
14. Testar escolha de acabamento.
15. Testar mudança de módulo.
16. Testar sincronização de seleção.
17. Testar projeções responsivas.
18. Confirmar que layout profiles mantêm as dependências atuais.
19. Confirmar que uma alteração visual não muda persistência.
20. Confirmar que a alteração visual não altera o preço calculado.
21. Verificar tratamento de configuração inválida.
22. Comparar DOM e CSSOM da baseline.
23. Extrair estilos comuns quando houver prova de equivalência.
24. Manter diferenças por componente e comportamento.
25. Validar em fixture local V5.
26. Fazer revisão hospedada apenas quando ela for necessária.
27. Integrar e repetir os testes adequados ao escopo.

##### Bloqueio específico

O Configurador hospedado ainda possui histórico de indisponibilidade da configuração publicada em determinados previews.

A ausência de um fixture válido **bloqueia alegações sobre o runtime hospedado**, não necessariamente toda correção estática ou toda extração isolada.

##### DoD específico

Componentes de apresentação possuem correspondência rastreável entre contrato, DOM, estado e CSS; nenhuma regra de negócio foi transferida para a camada visual.

---

#### CMP-016 — Preservar a especialização do Viewer e consolidar seus componentes

**Prioridade:** P1  
**Tipo:** organização de renderers  
**Dependências:** CMP-014 e projeção pública válida

##### Objetivo

Organizar as responsabilidades de apresentação do Viewer sem transformá-lo em um segundo Configurador.

##### Componentes atuais relevantes

- Overview.
- Cena.
- Vistas técnicas.
- Detalhes do módulo.
- Paginação mobile.
- Seleção de módulo.
- Informações de dimensões.
- Preço base público condicionado à autorização.

##### Procedimento

1. Identificar o fluxo que recebe a projeção pública.
2. Confirmar o contrato da projeção.
3. Identificar o adapter de cena.
4. Identificar o registro local de renderers.
5. Mapear inputs de cada renderer.
6. Verificar a seleção inicial por dados.
7. Verificar deep link de módulo, quando válido.
8. Confirmar fallback para ausência de módulos visíveis.
9. Confirmar comportamento de erro de projeção publicada.
10. Verificar que dados inválidos não são substituídos silenciosamente por mocks.
11. Confirmar renderização do overview.
12. Confirmar renderização da cena.
13. Confirmar renderização das vistas técnicas.
14. Confirmar renderização dos detalhes.
15. Testar seleção de outro módulo.
16. Confirmar atualização de todos os blocos dependentes.
17. Testar paginação mobile.
18. Testar foco e teclado.
19. Confirmar o tratamento de `prefers-reduced-motion`.
20. Verificar dimensões.
21. Confirmar que preço base só aparece quando permitido e disponível.
22. Confirmar que não há vazamento de dados privados.
23. Medir DOM e CSSOM.
24. Identificar componentes realmente reutilizáveis.
25. Evitar converter o registro local em um catálogo universal sem necessidade.
26. Integrar as simplificações comprovadas.
27. Revalidar a composição resultante.

##### DoD específico

Viewer estável, renderers com responsabilidades separadas, projeção pública preservada e interfaces compartilhadas sem dependência indevida do Admin.

---

#### CMP-017 — Consolidar controles do Admin por significado

**Prioridade:** P1/P2  
**Tipo:** organização de apresentação de domínio  
**Dependências:** CMP-001 e fixture de administração

##### Objetivo

Reduzir duplicações reais de controles administrativos sem confundir estados que representam políticas diferentes.

##### Distinções obrigatórias

**Estado inicial no Configurador:** visibilidade ou ativação inicial conforme a entidade.

**Estado inicial no Viewer:** visibilidade pública inicial.

**Estado inicial de serviço:** serviço previamente selecionado.

**Disponibilidade de etapa:** inclusão da etapa no fluxo.

**Disponibilidade de acabamento:** elegibilidade para escolha pelo cliente.

**Publicação de preço base:** permissão explícita para exposição pública no Viewer.

Essas ações podem compartilhar marcação ou estilos, mas não têm o mesmo comportamento de domínio.

##### Procedimento

1. Identificar controles por área administrativa.
2. Mapear texto visível e nome acessível.
3. Mapear estado real associado ao controle.
4. Mapear quem valida a alteração.
5. Mapear quem persiste a alteração.
6. Verificar se o controle representa preferência, disponibilidade ou visibilidade.
7. Distinguir checkboxes de associação de checkboxes de habilitação.
8. Confirmar estados disabled e motivos.
9. Confirmar feedback de erro.
10. Mapear estilos compartilháveis.
11. Separar o contrato visual do contrato de persistência.
12. Propor uma primitiva quando houver correspondência de comportamento.
13. Preservar as validações específicas.
14. Testar renderização com dados V5.
15. Testar ativação e desativação.
16. Confirmar que o editor não salva mudanças sem ação explícita.
17. Confirmar que um estado visual não altera política de publicação.
18. Verificar persistência após salvar, quando o pacote envolver esse fluxo.
19. Confirmar que controles desabilitados comunicam o motivo pertinente.
20. Testar teclado e labels acessíveis.
21. Integrar por família técnica.
22. Registrar exceções.

##### DoD específico

Componentes visuais reaproveitados onde há equivalência; autorizações, validações e persistência mantidas nos respectivos contratos.

---

## 5. Programa de ciclo de vida dos controladores

### CMP-018 — Auditar inicialização, atualização e descarte

**Prioridade:** P1  
**Tipo:** melhoria de confiabilidade  
**Dependências:** CMP-001  
**Contrato:** ARC-06

#### 5.1 Problema

Existem diferentes padrões de controlador:

- IIFE executada uma vez em página estática.
- Controlador que manipula DOM após carregamento.
- Controlador que reage a dados e renderiza novamente.
- Adaptador de cena que pode montar elementos.
- Controlador assíncrono vinculado à sessão.

Não devemos obrigar todos a implementar a mesma interface.

#### 5.2 Classes de lifecycle

| Classe | Exemplo | Obrigação |
|---|---|---|
| L1 | Menu público estático | Inicializar uma vez; não duplicar listeners |
| L2 | Controle de tema | Atualizar estado corretamente; preservar instância |
| L3 | Carrossel e painel editorial | Gerenciar timers/listeners próprios |
| L4 | Cena/renderer remontável | Evitar bindings duplicados; descarte se necessário |
| L5 | Sessão/autenticação | Descartar respostas obsoletas; manter autoridade do estado |

#### 5.3 Procedimento

1. Identificar todos os controladores prioritários.
2. Definir sua classe de lifecycle.
3. Identificar o evento ou condição de inicialização.
4. Identificar os elementos DOM necessários.
5. Registrar listeners globais.
6. Registrar listeners locais.
7. Registrar timers e observers.
8. Registrar callbacks assíncronos.
9. Identificar se o consumidor pode remontar o DOM.
10. Identificar se a função pode ser chamada novamente.
11. Identificar mecanismos existentes de idempotência.
12. Testar inicialização repetida apenas onde tecnicamente plausível.
13. Medir eventos processados por interação.
14. Detectar duplas ativações.
15. Detectar referências a elementos removidos.
16. Detectar timers sem encerramento.
17. Detectar respostas assíncronas obsoletas.
18. Corrigir problemas na menor unidade possível.
19. Usar `AbortController` ou função de cleanup onde isso for vantajoso.
20. Evitar gerenciador global de ciclo de vida sem evidência de necessidade.
21. Testar as transições de estado.
22. Integrar e verificar regressões.

#### DoD específico

Cada controlador prioritário possui classe de lifecycle declarada e testes coerentes com seu comportamento real.

---

## 6. Composição híbrida sem motor universal

### CMP-019 — Formalizar o limite entre build-time e runtime

**Prioridade:** P1  
**Tipo:** contrato arquitetural  
**Dependências:** CMP-002, CMP-015 e CMP-016  
**Contrato:** ARC-03, ARC-07 e ARC-10

#### 6.1 Regra geral

Usar o mecanismo mais simples que preserve os requisitos de cada superfície.

| Superfície | Estratégia preferida |
|---|---|
| Header primário | Fragmento HTML em build-time |
| Conteúdo editorial estático | HTML autoral |
| Benefícios com dados simples | JS local ou markup, conforme ganho real |
| Menu público | Controlador compartilhado |
| Menu privado | Controlador de sessão especializado |
| Tema | Controlador transversal |
| Viewer | Renderers especializados sobre projeção pública |
| Configurador | Componentes associados ao contrato V5 |
| Admin | Editor de domínio especializado |

#### 6.2 Procedimento

1. Registrar o modo de composição de cada rota.
2. Identificar o conteúdo essencial que deve existir sem JS.
3. Identificar conteúdo dependente de dados dinâmicos.
4. Identificar conteúdo dependente de autenticação.
5. Identificar fragmentos realmente compartilhados.
6. Conferir ownership de autoria.
7. Identificar páginas geradas e páginas autorais.
8. Confirmar que o compilador não sobrescreve rotas excluídas.
9. Garantir que a implementação não possui duas fontes do mesmo markup.
10. Evitar sincronização manual de fragmentos compartilhados.
11. Avaliar novos fragmentos somente quando houver consumidores reais.
12. Testar output gerado.
13. Testar comportamento sem JS onde aplicável.
14. Testar comportamento com JS e dados válidos.
15. Verificar acessibilidade da estrutura resultante.
16. Identificar limites de rollback.
17. Documentar apenas contratos permanentes.
18. Encerrar protótipos substituídos.

#### Critério para criar novo fragmento

Um fragmento em build-time deve ser criado quando:

- Existem consumidores com a mesma estrutura autoral.
- A duplicação gera manutenção repetida real.
- As variantes podem ser expressas com configuração simples.
- O output continua sendo HTML válido e acessível.
- O mecanismo existente consegue atendê-lo.

Não criar um fragmento para cada seção editorial.

#### DoD específico

Cada rota possui uma estratégia de composição declarada, sem autoridades concorrentes e sem dependência desnecessária de JS.

---

## 7. Bundles de testes de componentes

### BT-CMP-00 — Inventário e integridade

Executado em toda extração.

Verifica:

- Fonte e consumer.
- Presença do componente.
- Ordem de scripts.
- Carregamento de CSS.
- Ausência de definição duplicada.
- Contratos de dados.
- Build e geração, quando aplicáveis.
- Versão/hash do artefato.
- Ausência de mudanças fora do escopo.

### BT-CMP-10 — Header público

Cobertura:

1. Três páginas primárias.
2. Variante secundária do Viewer como contrato próprio.
3. Claro e escuro.
4. Breakpoints críticos.
5. Marca.
6. CTA.
7. Ordem dos controles.
8. Menu fechado/aberto.
9. ARIA.
10. Teclado.
11. Escape.
12. Clique fora.
13. Responsividade.
14. Mudança de tema.
15. Foco ao mudar de layout.
16. Ausência de listeners duplicados.
17. HTML gerado sincronizado.
18. Nenhuma alteração no comportamento editorial.

Não é obrigatório executar todos os cenários de uma vez para cada patch. O subconjunto deve refletir os consumers alterados, e um gate transversal completo deve ser executado nos marcos de integração pertinentes.

### BT-CMP-20 — Header privado e tema

Cobertura:

1. Estado anônimo.
2. Estado carregando.
3. Admin autenticado.
4. Staff autorizado.
5. Sessão temporária.
6. Acesso negado.
7. Respostas assíncronas fora de ordem.
8. Menu aberto/fechado.
9. Logout.
10. Foco e teclado.
11. Tema automático.
12. Tema claro/escuro.
13. Marca correta.
14. Slots corretos.
15. Falha de serviço segura.

As fixtures devem permanecer locais ou utilizar sessões autorizadas. Nenhuma credencial, token ou convite deve ser incluído em artefatos de teste.

### BT-CMP-30 — Cena e controles de domínio

Cobertura:

1. Cena carregada.
2. Cena com falha de asset.
3. Visibilidade de entidades.
4. Seleção de módulo.
5. Hotspot selecionado.
6. Hotspot oculto.
7. Hotspot desabilitado.
8. Foco e teclado.
9. Layering e z-index.
10. Frame de seleção.
11. Acabamento.
12. Controle global/local.
13. Dados públicos permitidos.
14. Projeção responsiva.
15. Ausência de efeito em preços.
16. Ausência de efeito em publicação/autorização.
17. Mount/remount quando aplicável.
18. Cleanup ou idempotência quando necessário.

### BT-CMP-40 — Composição editorial

Cobertura:

1. HTML essencial.
2. Header compartilhado.
3. Dados e cards.
4. Carrossel.
5. Alteração rápida de seleção.
6. Imagem/fallback.
7. Accordion.
8. Resize.
9. Foco.
10. Reduced motion.
11. Conteúdo preservado.
12. Sem duplicação de DOM.
13. Ausência de dependência de um motor universal.

### BT-CMP-50 — Regressão e integração

Executado antes do encerramento do pacote.

Verifica:

1. Patch final e SHA.
2. Diferenças esperadas.
3. Consumer principal.
4. Consumers secundários afetados.
5. Controle negativo.
6. Contrato visual.
7. Contrato funcional.
8. Contrato de acessibilidade.
9. Browser adequado ao risco.
10. Build/fixture corretos.
11. Ausência de regressão de domínio.
12. Resultados registrados.
13. Integração na branch-alvo.
14. Revalidação pertinente após integração.
15. Rollback claro.

---

## 8. Estratégia de execução e integração

### 8.1 Ordem preferencial inicial

1. **CMP-001:** inventário atual de ownership.
2. **CMP-002:** fechar a fonte autoral ARC-03C.
3. **CMP-003:** confirmar a autoridade do menu público.
4. **CMP-004:** integrar NAV-005 primário.
5. **CMP-005:** consolidar NAV-005 secundário no Viewer.
6. **CMP-007:** consolidar contratos de tema/slots.
7. **CMP-008:** consolidar identidade da marca.
8. **CMP-013:** validar/corrigir o painel expansível.
9. **CMP-012:** revisar carrossel da Landing.
10. **CMP-011:** encerrar decisão do protótipo declarativo.
11. **CMP-006:** formalizar a navegação privada.
12. **CMP-018:** fechar contratos de lifecycle prioritários.
13. **CMP-009:** primeira família de botões.
14. **CMP-010:** primeira família de feedback.
15. **CMP-014:** consolidar cena/hotspots.
16. **CMP-015:** consolidar apresentação do Configurador.
17. **CMP-016:** consolidar renderers do Viewer.
18. **CMP-017:** consolidar controles visuais do Admin.
19. **CMP-019:** formalizar a arquitetura híbrida final.

Essa ordem é uma preferência operacional, não uma dependência rígida entre todos os itens.

Trabalho sobre componentes públicos pode avançar enquanto uma fixture privada está bloqueada, desde que não exista conflito de arquivos ou contratos.

### 8.2 Pacotes de integração sugeridos

#### INT-CMP-A — Fonte pública e menu

Inclui CMP-002/003 e dependências necessárias.

Não inclui redesign de header, tema privado ou mudança de domínio.

#### INT-CMP-B — NAV-005 primário

Inclui CMP-004 e correções estritamente relacionadas.

Mantém UX-04 separado.

#### INT-CMP-C — Viewer NAV-005

Inclui CMP-005, quando houver diferença pendente na branch-alvo.

Não altera renderers de módulos.

#### INT-CMP-D — Marca e tema

Inclui CMP-007/008 se os contratos forem compatíveis.

Não introduz aplicação global não autorizada da paleta VIS-002.

#### INT-CMP-E — Editorial e controladores locais

Inclui CMP-011/012/013 somente se houver alterações tecnicamente próximas. Caso contrário, integrar separadamente.

#### INT-CMP-F — Domínio visual

Inclui CMP-014…017 por conjuntos de consumidores, sem necessidade de um merge único.

#### INT-CMP-G — Lifecycle e arquitetura final

Inclui CMP-018/019 e encerramento das duplicações documentais ou técnicas verificadas.

---

## 9. Regras de DoD específicas desta etapa

O anexo operacional final registrará o estado de cada ID.

Nesta etapa, o DoD será definido em duas camadas.

### 9.1 DoD universal

Um pacote de componente somente estará concluído se:

1. O resultado definido foi entregue.
2. A fonte de implementação está identificada.
3. Todos os consumidores obrigatórios estão identificados.
4. As variantes legítimas foram preservadas.
5. Os testes aplicáveis passaram.
6. As decisões homologadas foram respeitadas.
7. O contrato de domínio não foi alterado indevidamente.
8. As diferenças de comportamento e aparência estão autorizadas.
9. A implementação foi integrada quando o pacote for de código.
10. O head integrado possui evidência suficiente.
11. O rollback está delimitado.
12. O estado operacional foi atualizado.

### 9.2 DoD por natureza de mudança

| Natureza | Condição adicional |
|---|---|
| Refatoração equivalente | Nenhuma mudança funcional ou visual não autorizada |
| Correção de bug | Defeito original reproduzido e correção comprovada |
| Componente compartilhado | Todos os consumidores afetados passam |
| Componente de domínio | Contrato de dados e política de negócio preservados |
| Composição build-time | Fonte, output e manifesto sincronizados |
| Controlador interativo | Eventos, foco, ARIA e lifecycle corretos |
| Mudança visual intencional | Homologação correspondente e evidência visual |
| Auditoria | Inventário persistido e decisões operacionais derivadas |
| Experimento rejeitado | Motivo, custo/benefício e disposição da branch registrados |

### 9.3 Reporting

O agente deverá, ao iniciar a execução de qualquer pacote:

- Declarar os IDs escolhidos.
- Confirmar as dependências.
- Registrar o estado inicial.
- Indicar a branch-alvo.
- Informar os testes relevantes.

Ao terminar, deverá registrar:

- Estado final de cada ID.
- Evidência correspondente.
- Mudanças integradas.
- Critérios ainda pendentes.
- Bloqueios específicos.
- Próximos IDs recomendados.

A definição detalhada fica no plano. A lista de estados e a timeline ficam no anexo DoD, sem reproduzir narrativamente o trabalho.

---

## 10. Pontos de interrogação

| ID | Questão | Como resolver |
|---|---|---|
| CMP-Q01 | Existem outros controladores públicos concorrendo com `header-menu.js`? | Inventário de scripts e eventos por rota |
| CMP-Q02 | A PR #269 pode ser integrada como está? | Revisar head, diff, homologação e gates |
| CMP-Q03 | O Viewer da branch-alvo já contém integralmente a variante NAV-005 aprovada? | Comparação `main`/`development` e browser |
| CMP-Q04 | Há benefício em trocar consultas estruturais por slots explícitos no tema? | Comparar complexidade, invariantes e consumidores |
| CMP-Q05 | Quais estilos de marca são realmente compartilháveis? | Comparação de slots/retângulos e variantes |
| CMP-Q06 | A Landing tem duplicação de dados de benefícios ou apenas conteúdo semelhante? | Análise de ownership editorial |
| CMP-Q07 | O bug histórico do accordion ainda se reproduz? | Teste browser do estado atual |
| CMP-Q08 | `bindKeyboard()` pode registrar listeners múltiplos no uso real? | Auditoria de chamadas e remount |
| CMP-Q09 | Quais propriedades de hotspot podem ser compartilhadas entre Viewer e Config? | Cena real, CSSOM e regressão de seleção |
| CMP-Q10 | As famílias de botões comportam uma base comum sem overrides excessivos? | Teste por família/estado |
| CMP-Q11 | Existe uma primitiva de feedback que preserve diferenças de anúncio e prioridade? | Matriz por fluxo |
| CMP-Q12 | Quais telas protegidas podem ser validadas com fixture local suficiente? | Contrato de sessão e publicação |
| CMP-Q13 | Alguma parte da composição dinâmica precisa funcionar sem JavaScript? | Requisito real por superfície |
| CMP-Q14 | Há um segundo consumidor real que justificaria um registro de composição de páginas? | Análise de demanda e custo |
| CMP-Q15 | Quais tarefas já estão efetivamente integradas e apenas aguardam encerramento documental? | Reconciliação por commits e evidências |

---

## 11. Política de interrupção e rollback

Interromper o pacote quando:

- Uma abstração passa a controlar estado de domínio que não lhe pertence.
- O compartilhamento exige alterar consumidores semanticamente distintos.
- O componente deixa de ter comportamento previsível sem JS quando isso é requisito.
- Aparecem listeners duplicados ou eventos conflitantes.
- Uma mudança de tema desloca controles fora do contrato NAV.
- Uma extração de CSS modifica a apresentação de outro shell.
- A fixture não reproduz o componente que pretende validar.
- A prova de equivalência depende de teste executado em SHA antigo.
- Uma alteração em renderização pública expõe dados não permitidos.
- A implementação depende de um sistema universal que não possui necessidade demonstrada.

O rollback deve restaurar o componente e seus consumidores, sem exigir reverter alterações independentes.

---

## 12. Critérios de conclusão do programa de componentes

A frente estará suficientemente consolidada quando:

- Header público possui fonte única de estrutura e controlador.
- Viewer preserva seu header contextual NAV-005.
- Navegação privada conserva regras próprias de sessão.
- Tema e marca possuem autoridade compartilhada consistente.
- Componentes editoriais não duplicam controladores.
- O renderer de cena mantém um único contrato compartilhado.
- Configurador e Viewer continuam usando projeções próprias.
- Admin preserva autoria e persistência de domínio.
- As famílias de CSS são compartilhadas por semântica e não por homonímia.
- Controladores prioritários possuem lifecycle comprovado.
- Compilação, componentes, consumidores e evidências estão rastreados.
- Não permanecem implementações experimentais concorrentes sem disposição.
- Os pacotes concluídos atendem ao DoD e estão integrados.

**Não é necessário transformar todos os elementos da interface em componentes formalizados para considerar essa frente concluída.**

É necessário formalizar aqueles cuja responsabilidade compartilhada reduz custo, regressão ou duplicação real.

---

## 13. Parecer de arquitetura — Parte IV

A principal conclusão é que a consolidação deve ser predominantemente **subtrativa e integradora**, não uma reconstrução.

O projeto já possui:

- Fragmentos autorais de páginas.
- Compilador determinístico.
- Controlador de menu público.
- Controlador transversal de tema.
- Navegação privada especializada.
- Renderer compartilhado de cena.
- Contratos de apresentação no Configurador.
- Renderers organizados no Viewer.
- Múltiplos testes específicos de componentes e estados.

Faltam principalmente:

1. Fechar os gates pendentes e integrar as mudanças relevantes.
2. Determinar ownership por consumidor.
3. Substituir duplicações comprovadas por autoridades únicas.
4. Evitar que alterações de CSS prejudiquem componentes de outras rotas.
5. Verificar lifecycle nos casos realmente remontáveis.
6. Consolidar a composição híbrida já existente.
7. Tornar a execução rastreável por ID e DoD.

O pior caminho seria criar uma camada universal de componentes para substituir estruturas que já funcionam e possuem contratos especializados.

O melhor caminho é **promover implementações existentes a autoridades efetivas**, mantendo variantes e fronteiras de domínio.

---

### Referências técnicas principais

- [Compilador ARC-03C](https://github.com/EAKerber/MobiliPresenter2D/blob/development/scripts/compile-primary-pages.mjs)
- [Fragmento autoral do header](https://github.com/EAKerber/MobiliPresenter2D/blob/development/architecture/fragments/primary-header.fragment.html)
- [Controlador do menu público](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/landing/header-menu.js)
- [Controlador de tema](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/ui-theme.js)
- [Navegação privada](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/private-navigation.js)
- [Componente de cena compartilhado](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/scene-component.js)
- [Contrato de apresentação do Configurador](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/presentation-contract.js)
- [PR #269 — NAV-005](https://github.com/EAKerber/MobiliPresenter2D/pull/269)
- [Teste do header secundário Viewer](https://github.com/EAKerber/MobiliPresenter2D/blob/development/tests/viewer-secondary-header-browser-gate.mjs)
- [Gate do controlador público](https://github.com/EAKerber/MobiliPresenter2D/blob/development/tests/public-header-controller-gate.mjs)
- [Teste de accordion](https://github.com/EAKerber/MobiliPresenter2D/blob/development/tests/how-accordion-grid-browser-gate.mjs)
- [G3 — matriz de componentes e estados](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/evidence/architecture/g3-control-families-static-matrix-2026-11-13.md)
- [UI-ADR-004 — limites de reutilização](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ui-adr-004-cross-page-reuse-gate-2026-10-20.md)
- [Inventário de ownership DOM/JS](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/dom-js-component-ownership-2026-10-20.md)

**Limite desta etapa:** a análise verifica código e evidências existentes. Os testes citados não foram reexecutados aqui. Seus resultados históricos são referências para planejar a validação dos heads atuais, não certificações novas de runtime.

---

<a id="capitulo-5"></a>
# Capítulo V — Contratos de domínio, integração das ferramentas e localização

## 1. Objetivo da frente

Consolidar a integração entre o Core, a administração, o configurador e o visualizador público sem introduzir autoridades concorrentes para dados ou decisões comerciais.

A intenção não é reescrever o V5.

É estabelecer uma cadeia de responsabilidades tão clara que possamos:

1. Modificar a apresentação de um componente sem mudar o significado dos dados.
2. Modificar uma regra comercial no Core e observar a atualização correta dos consumidores.
3. Alterar dados no Admin e publicá-los com validação e controle de concorrência.
4. Produzir a configuração do comprador a partir da fonte publicada, sem criar outro modelo autoral.
5. Produzir uma projeção pública mínima para o Viewer.
6. Preservar a autorização explícita para qualquer exposição de preços.
7. Centralizar textos localizáveis sem deslocar a propriedade do conteúdo comercial.
8. Identificar precisamente quais testes comprovam cada contrato.
9. Integrar as mudanças em conjuntos suficientemente pequenos para serem revisados e revertidos.
10. Reduzir a necessidade de handovers interpretativos e verificações repetidas.

A regra central é:

**Uma responsabilidade possui uma autoridade. Um mesmo dado pode ter múltiplas projeções, mas não múltiplas fontes concorrentes de verdade.**

---

## 2. Diagnóstico técnico atual

### 2.1 O V5 já é a autoridade administrativa

O Produto declara:

`ConfiguratorAdministration2D 5.0`

em:

`app/core/administration-v5.js`

O contrato incorpora hierarquia, apresentação, preços, estado inicial, materiais, dimensões e outros elementos necessários à administração.

Ele também mantém mecanismos de validação, normalização, atualização de schemas anteriores e assinatura semântica da publicação.

Isso significa que a arquitetura não precisa de um novo documento de administração para resolver questões de UI.

O trabalho deve se concentrar em garantir que os consumidores respeitem o V5 existente.

### 2.2 O Configurador recebe um contrato de transporte próprio

O arquivo:

`app/core/published-buyer-projection.js`

declara:

`BuyerConfiguratorPayload 1.0`

Esse DTO é produzido a partir da configuração publicada e inclui dados necessários para que o Configurador funcione.

Entre suas regiões:

- `displaySettings`
- `flow`
- `pricingRules`
- `presentationPolicy`

Há allowlists explícitas para os campos de apresentação e configuração.

A revisão administrativa é excluída do transporte, e o documento autoral completo não é enviado como fonte bruta.

**Distinção fundamental:** o DTO do comprador pode transportar regras necessárias ao cálculo da configuração autorizada. Ele não é a mesma projeção do Viewer público.

Não devemos adotar a regra simplista de que “todo preço é sempre privado” nem a regra oposta de que “todo preço usado pelo comprador pode ser enviado publicamente”.

### 2.3 O Viewer possui uma projeção pública diferente

O arquivo:

`app/core/public-module-projection.js`

declara:

- `PublicModulePresentation2D 0.1`
- `PublicModulePresentation2D 0.2`

A versão 0.2 acrescenta a possibilidade de `basePriceCents`, condicionada à permissão publicada.

Essa projeção contém somente informações aprovadas para visualização pública.

Não inclui o documento administrativo, regras de cálculo completas, revisão, margens ou dados internos desnecessários.

O Viewer solicita a versão 0.2 do endpoint, mas a negociação de versão **não constitui autorização para publicar preços**.

### 2.4 O processo de publicação V5 possui verificações relevantes

O arquivo:

`app/core/v5-normal-save.js`

implementa um fluxo que inclui:

1. Leitura da fonte armazenada.
2. Confirmação de schema V5.
3. Validação da revisão enviada.
4. Validação do candidato.
5. Normalização.
6. Incremento da revisão.
7. Escrita condicional pelo ETag anterior.
8. Leitura posterior à escrita.
9. Comparação de ETag.
10. Comparação de digest.
11. Validação semântica da publicação lida.

Essa estrutura já protege contra diversas falhas de concorrência e falsos sucessos.

A arquitetura não deve substituí-la por uma operação de gravação mais simples.

A simplificação desejada deve ocorrer na organização e verificação das responsabilidades, não na retirada das garantias transacionais.

### 2.5 O backend separa três superfícies

| Superfície | Finalidade | Autoridade |
|---|---|---|
| `/api/configuration` | Leitura e edição administrativa | Identidade administrativa + V5 |
| `/api/buyer-configuration` | Entrega da configuração ao comprador autorizado | Política de acesso + DTO Buyer |
| `/api/public-modules` | Conteúdo permitido ao Viewer anônimo | Projeção pública allowlisted |

Essas três superfícies não devem ser unificadas em um endpoint que retorna campos diferentes com base apenas em um parâmetro de interface.

A separação atual reduz a possibilidade de uma mudança visual revelar conteúdo administrativo.

### 2.6 Existem mecanismos de compatibilidade deliberados

A implementação mantém caminhos de leitura e recuperação de configurações V3.

A migração remota V3→V5 já foi aposentada.

Quando a fonte armazenada é V5, o caminho normal de escrita não pode fazer downgrade silencioso.

A presença de código legado não significa automaticamente redundância removível.

Antes de eliminá-lo, é necessário determinar se ele ainda protege uma capacidade de recuperação.

### 2.7 O ARC-13 possui um inventário extenso, mas ainda não um catálogo de localização

A PR [#274](https://github.com/EAKerber/MobiliPresenter2D/pull/274), ainda Draft, apresenta um inventário atualizado contendo:

- 1.026 ocorrências candidatas de texto.
- 360 registros de fontes JavaScript.
- 420 ocorrências HTML mapeadas às fontes autorais.
- Nenhuma ocorrência sem rota/owner no levantamento atual.

Essas quantidades não equivalem a 1.026 textos que precisam ser migrados.

O inventário contém textos localizáveis, nomes acessíveis, conteúdo editorial, textos condicionais e candidatos que ainda exigem classificação semântica.

A criação do catálogo `pt-BR` e a substituição dos consumidores em runtime permanecem pendentes.

---

## 3. Arquitetura-alvo dos dados

### 3.1 Fluxo conceitual

```text
                   ADMIN
              Autoria e edição
                     │
                     ▼
       ConfiguratorAdministration2D 5.0
                     │
               Validação V5
                     │
           Publicação autenticada
          Revision + ETag + readback
                     │
                     ▼
            Fonte V5 publicada
                     │
       ┌─────────────┴─────────────┐
       │                           │
       ▼                           ▼
Projeção Buyer                 Projeção pública
allowlisted                    allowlisted
       │                           │
       ▼                           ▼
BuyerConfigurator              PublicModulePresentation
Payload 1.0                    0.1 / 0.2
       │                           │
       ▼                           ▼
CONFIGURADOR                    VIEWER
Fluxo, seleção,                 Conteúdo permitido,
cálculo e apresentação          cena e preço autorizado
```

A representação é lógica: o acesso à fonte e as políticas de segurança pertencem ao backend. Não pressupõe que o navegador possa abrir diretamente o armazenamento publicado.

### 3.2 Matriz de autoridade

| Responsabilidade | Fonte autoritativa | Consumidor |
|---|---|---|
| Estrutura administrativa | V5 publicado | Admin, projeções |
| Hierarquia do fluxo | V5 → `NormalizedConfiguratorFlow` | Configurador |
| Componente de apresentação | `ConfiguratorPresentation2D` | Renderers do Configurador |
| Catálogo físico | Catálogo/Scene2D | Core e adaptadores |
| Seleção atual | Estado do Configurador ou Viewer | UI correspondente |
| Regras de preço | `CommercialPricingRules` | Core de pricing |
| Permissão de preço público | `viewerPricePublication` publicado | Projeção pública |
| Conteúdo público do módulo | Objetos V5 filtrados pela projeção | Viewer |
| Permissões de acesso | Backend/identidade/sessão | APIs protegidas |
| Cores e papéis visuais | Design System e distribuição autorizada | CSS dos consumidores |
| Textos de UI | Catálogo versionado `pt-BR`, após classificação | HTML/JS |
| Textos comerciais editáveis | Dados V5 e conteúdo editorial autorizado | Interfaces correspondentes |

Essa matriz deverá ser vinculada aos IDs do backlog e aos testes.

---

## 4. Marco DOM-M0 — Contratos e fontes de verdade estabilizados

### DOM-001 — Inventário executável dos contratos V5

**Prioridade:** P0  
**Tipo:** auditoria de autoridade  
**Dependências:** baseline do repositório e CMP-001  
**Contratos:** ARC-11, ARC-12, ARC-16

#### Objetivo

Construir o mapa definitivo de contratos, transformações e consumidores.

#### Procedimento

1. Fixar os SHAs das branches analisadas.
2. Registrar os schemas efetivamente declarados no código.
3. Localizar os validadores de cada schema.
4. Localizar os normalizadores.
5. Identificar as fontes de defaults.
6. Identificar o documento publicado.
7. Identificar os DTOs usados em transporte.
8. Identificar todos os consumidores de cada DTO.
9. Distinguir dados autorais de dados derivados.
10. Mapear propriedades que são transformadas ao projetar.
11. Mapear propriedades omitidas deliberadamente.
12. Identificar defaults de apresentação.
13. Identificar defaults de domínio.
14. Identificar validações que falham fechado.
15. Identificar caminhos de compatibilidade V3/V4.
16. Mapear endpoints e políticas de autorização.
17. Identificar onde cada valor de preço é calculado.
18. Identificar onde cada valor de preço é apenas formatado.
19. Registrar as regras de publicação pública.
20. Associar testes existentes aos contratos.
21. Identificar caminhos sem prova runtime suficiente.
22. Registrar dependências para os pacotes subsequentes.

#### Entregáveis

- Mapa schema → projeção → consumer.
- Mapa API → autorização → DTO.
- Mapa de propriedades comerciais.
- Inventário de testes por contrato.
- Lista de divergências e exceções legítimas.

#### Bundle

BT-DOM-00 — fonte, schema e proveniência.

#### DoD específico

Cada contrato prioritário possui uma autoridade identificada, consumidores conhecidos e pelo menos um método definido de verificação.

---

### DOM-002 — Distinguir autoria, projeção e estado transitório

**Prioridade:** P0  
**Tipo:** delimitação arquitetural  
**Dependências:** DOM-001

#### Objetivo

Evitar que os próximos componentes acabem criando modelos concorrentes de configuração.

#### Procedimento

1. Identificar valores editáveis no Admin.
2. Identificar valores publicados.
3. Identificar valores normalizados pelo Core.
4. Identificar estado inicial definido no documento.
5. Identificar estado transitório criado pelo Configurador.
6. Identificar estado transitório criado pelo Viewer.
7. Confirmar quais alterações são persistidas.
8. Confirmar quais alterações só existem durante a sessão de uso.
9. Distinguir dados calculados de dados armazenados.
10. Identificar renderers que ainda dependem de estruturas legadas.
11. Confirmar que essas estruturas são projeções derivadas.
12. Impedir que uma projeção derivada seja usada para regravar a fonte autoral.
13. Registrar compatibilidades necessárias.
14. Identificar duplicações verdadeiras de estado.
15. Formular correções pontuais, caso existam.
16. Testar as fronteiras dos consumidores.
17. Persistir a matriz de propriedade.

#### Regra de implementação

Uma cópia de dados usada para renderização não constitui necessariamente uma segunda autoridade.

Ela passa a ser problemática quando:

- É editável independentemente da origem.
- Decide regras que pertencem ao Core.
- Pode ser persistida como fonte concorrente.
- Não possui derivação ou atualização determinística.
- Pode divergir silenciosamente do contrato publicado.

#### DoD específico

Nenhuma nova implementação de apresentação precisa conhecer ou modificar a estrutura administrativa completa quando uma projeção adequada já existe.

---

## 5. Marco DOM-M1 — Publicação segura e compatibilidade controlada

### DOM-003 — Consolidar a leitura da configuração publicada

**Prioridade:** P0  
**Tipo:** contrato de persistência  
**Dependências:** DOM-001

#### Contexto

`app/core/published-configuration.js` separa a leitura bruta da inspeção/validação.

O endpoint administrativo possui compatibilidade histórica específica para fontes V3, mas não deve transformar um V5 inválido em uma configuração padrão aparentemente válida.

#### Objetivo

Garantir que cada situação de armazenamento possua uma resposta explícita e segura.

#### Procedimento

1. Identificar o store de produção e de Deploy Preview.
2. Identificar a política de leitura forte.
3. Confirmar a leitura de metadados.
4. Confirmar a presença e o uso do ETag.
5. Identificar os estados `missing`, `stored`, `valid` e `invalid`.
6. Criar uma matriz de schemas aceitos.
7. Testar documento V3 válido.
8. Testar documento V5 válido.
9. Testar documento ausente.
10. Testar JSON inválido.
11. Testar schema desconhecido.
12. Testar V3 inválido.
13. Testar V5 inválido.
14. Confirmar que cada caso produz o comportamento esperado da API correspondente.
15. Verificar que um V5 inválido não cai em defaults.
16. Verificar que a API administrativa não envia ETag de armazenamento como dado público.
17. Verificar ausência de informações internas nos erros expostos.
18. Conferir comportamento em Preview.
19. Confirmar que nenhum fallback introduz uma fonte não publicada.
20. Executar os testes adequados de leitura e endpoint.
21. Registrar limitações dos mocks.
22. Encerrar com evidência por caso.

#### Controle negativo

Não modificar automaticamente uma configuração real para testar recuperação.

#### DoD específico

Fontes válidas, ausentes e inválidas são distinguíveis; não existe substituição silenciosa de V5 inválido por defaults.

---

### DOM-004 — Consolidar publicação V5, revisão e ETag

**Prioridade:** P0  
**Tipo:** contrato transacional  
**Dependências:** DOM-003

#### Objetivo

Preservar e verificar as garantias do save normal V5.

#### Procedimento

1. Identificar o handler administrativo vigente.
2. Confirmar a autenticação antes do acesso ao store.
3. Confirmar a autorização para edição.
4. Conferir o limite de tamanho do payload.
5. Confirmar que o schema enviado é V5.
6. Confirmar que a fonte armazenada também é V5.
7. Verificar a revisão enviada.
8. Comparar revisão enviada e revisão armazenada.
9. Executar validação do documento candidato.
10. Normalizar o candidato.
11. Confirmar incremento de revisão.
12. Capturar o ETag da fonte lida.
13. Confirmar escrita condicional com esse ETag.
14. Simular conflito de ETag.
15. Verificar que não ocorre retry silencioso.
16. Simular resposta de escrita sem confirmação válida.
17. Confirmar leitura posterior.
18. Confirmar correspondência do ETag de readback.
19. Comparar digests.
20. Comparar assinatura semântica de publicação.
21. Simular readback ausente ou divergente.
22. Confirmar que o cliente só apresenta sucesso quando a operação foi verificada.
23. Testar duas edições concorrentes.
24. Confirmar que o perdedor não substitui silenciosamente a edição vencedora.
25. Verificar que operações antigas não conseguem efetuar downgrade.
26. Executar testes puros e de endpoint.
27. Registrar limitações da simulação do provider.
28. Preservar rollback e recuperação.

#### Observação metodológica

O teste puro do serviço simula uma operação condicional do armazenamento.

Isso comprova a lógica esperada do serviço, mas não certifica sozinho o comportamento transacional de um provider real sob concorrência.

O gate deve distinguir:

- Contrato de código.
- Simulação do provider.
- Teste HTTP do handler.
- Eventual validação em ambiente autorizado.

#### Testes existentes

- `app/tools/test-v5-normal-save.js`
- `app/tools/test-v5-endpoint-safety.js`
- Testes de publicação e inspeção V5.

#### DoD específico

Save V5 preserva CAS, revisão e readback; conflitos e respostas não verificadas não são tratados como sucesso.

---

### DOM-005 — Encerrar o alcance dos caminhos históricos V3/V4

**Prioridade:** P1  
**Tipo:** redução de ambiguidade e manutenção  
**Dependências:** DOM-003/004

#### Objetivo

Manter apenas a compatibilidade histórica que possui finalidade comprovada, sem reativar mecanismos de migração aposentados.

#### Procedimento

1. Inventariar os caminhos atuais V3/V4.
2. Identificar quais são leitores.
3. Identificar quais são writers.
4. Identificar quais existem apenas em ferramentas offline.
5. Identificar quais são executáveis pelo endpoint atual.
6. Confirmar que a migração remota V3→V5 está aposentada.
7. Testar tentativa de reativação da operação antiga.
8. Testar tentativa de downgrade de V5.
9. Confirmar resposta não bem-sucedida.
10. Confirmar zero gravações adicionais.
11. Verificar manutenção da capacidade de recuperação V3.
12. Identificar eventuais códigos mortos sem utilidade comprovada.
13. Separar código histórico necessário de implementação removível.
14. Medir a complexidade efetivamente economizada por qualquer remoção.
15. Evitar refatoração ampla se o benefício não compensar o risco.
16. Preservar testes de recuperação.
17. Documentar a política de compatibilidade suportada.
18. Encerrar o pacote sem reabrir o processo de migração.

#### DoD específico

V5 permanece a autoridade atual; caminhos históricos não podem assumir controle sobre uma fonte V5, e a recuperação necessária continua possível.

---

## 6. Marco DOM-M2 — Fluxo e apresentação do Configurador

### DOM-006 — Consolidar `NormalizedConfiguratorFlow`

**Prioridade:** P1  
**Tipo:** contrato de fluxo  
**Dependências:** DOM-001/002

#### Objetivo

Garantir que o fluxo do Configurador seja derivado deterministicamente da configuração autorizada.

#### Procedimento

1. Identificar a fonte das etapas.
2. Identificar as regras de ativação de etapas.
3. Identificar a estrutura de grupos.
4. Identificar a estrutura de seções.
5. Identificar os itens pertencentes a cada seção.
6. Verificar a ordem declarada.
7. Confirmar ausência de IDs duplicados.
8. Confirmar ausência de ownership concorrente do mesmo item.
9. Verificar classificação de comportamento: seleção, toggle ou ação.
10. Testar rejeição de mistura incompatível de comportamentos.
11. Confirmar derivação das etapas legadas ainda aceitas.
12. Validar etapas personalizadas.
13. Confirmar `enabled` na navegação derivada.
14. Confirmar que etapas desabilitadas não aparecem como etapas disponíveis.
15. Verificar controles gerados para cada seção.
16. Confirmar que uma alteração de ordem não muda dados de domínio.
17. Testar remoção e adição de itens em fixture válida.
18. Testar dependências entre módulos e serviços.
19. Confirmar que a apresentação visual não redefine a regra de disponibilidade.
20. Testar resumo e seleção após alteração de fluxo.
21. Comparar os resultados antes/depois.
22. Integrar apenas correções comprovadas.

#### Regra de simplificação

A tabela de etapas e seus itens é uma boa fonte de composição, mas não deve tornar-se um motor universal que determine toda a interface pública.

#### Bundle

BT-DOM-20 — fluxo, comportamento e renderização.

#### DoD específico

O Configurador deriva uma única estrutura normalizada; componentes não inventam etapas nem reinterpretam dependências.

---

### DOM-007 — Consolidar projeções responsivas e componentes de seção

**Prioridade:** P1  
**Tipo:** integração Core/apresentação  
**Dependências:** DOM-006, CMP-015

#### Objetivo

Permitir que a mesma configuração funcione em diferentes layouts sem alterar seu significado.

#### Procedimento

1. Recuperar o contrato `ConfiguratorPresentation2D 1.1`.
2. Identificar todos os componentes permitidos.
3. Identificar os comportamentos associados.
4. Identificar perfis de layout suportados.
5. Identificar as projeções `inline`, `side-panel` e `replace`.
6. Mapear relações entre views.
7. Confirmar a ausência de relações cíclicas.
8. Validar referências às seções de origem.
9. Validar bindings dos renderers.
10. Verificar componentes exigidos em cada perfil.
11. Confirmar a estrutura DOM de cada projeção.
12. Testar mudança de largura.
13. Testar preservação da seleção.
14. Testar restauração de scroll quando aplicável.
15. Verificar comportamento de mini-cena/PiP.
16. Verificar dock e slots de ação.
17. Confirmar que nenhuma projeção altera preços.
18. Confirmar que nenhuma projeção altera elegibilidade de itens.
19. Verificar foco após reorganização.
20. Verificar ausência de conteúdo inacessível.
21. Executar testes responsivos existentes.
22. Integrar e repetir cenários de regressão.

#### DoD específico

Layout altera a forma de apresentar, não o significado ou a validade das escolhas.

---

### DOM-008 — Consolidar o contrato de precificação tipada

**Prioridade:** P0/P1  
**Tipo:** proteção comercial  
**Dependências:** DOM-001, DOM-004

#### Contexto

`CommercialPricingRules 1.0` distingue valores monetários e regras percentuais.

O Core calcula preços em centavos e separa diferentes papéis comerciais.

#### Objetivo

Evitar que a evolução dos componentes visuais crie uma segunda lógica de preço.

#### Procedimento

1. Inventariar os papéis de preço.
2. Confirmar quais aceitam valor monetário.
3. Confirmar quais aceitam percentuais.
4. Identificar limites de valores.
5. Confirmar normalização.
6. Confirmar rejeição de tipos incompatíveis.
7. Confirmar a fonte das bases por módulo.
8. Identificar ajustes de acabamento.
9. Identificar ajustes de puxador.
10. Identificar ajustes locais.
11. Identificar ajustes globais.
12. Confirmar a regra de alocação de puxadores.
13. Confirmar a regra de cálculo sobre módulos visíveis.
14. Confirmar tratamento de preços ausentes.
15. Confirmar resultado indisponível quando o orçamento não pode ser calculado validamente.
16. Testar valores monetários positivos.
17. Testar valores zerados e inválidos.
18. Testar percentuais nos limites do contrato.
19. Confirmar ausência de divergência causada por arredondamento de centavos.
20. Confirmar que a UI recebe valores calculados, não recria fórmulas.
21. Verificar formatação brasileira por `Intl`.
22. Confirmar que o Viewer não utiliza o total do orçamento como preço base.
23. Executar testes de cálculo e publicação.
24. Integrar apenas alterações cuja necessidade foi demonstrada.

#### DoD específico

Uma única autoridade de cálculo permanece ativa; valores exibidos correspondem ao contrato de preço correto.

---

## 7. Marco DOM-M3 — Administração e publicação comercial

### DOM-009 — Consolidar a autoria de dados no Admin

**Prioridade:** P1  
**Tipo:** organização de editor  
**Dependências:** DOM-004, DOM-006, CMP-017

#### Objetivo

Garantir que a UI administrativa seja uma interface para o V5 e não uma autoridade paralela.

#### Procedimento

1. Inventariar abas e áreas do Admin.
2. Identificar os campos editáveis em cada área.
3. Mapear campos ao V5.
4. Identificar valores derivados.
5. Identificar estados apenas visuais.
6. Conferir validação de campos.
7. Conferir tratamento de novos materiais.
8. Conferir associação de materiais.
9. Conferir disponibilidade de acabamentos.
10. Conferir regras de módulos.
11. Conferir edição de grupos e seções.
12. Conferir regras de dependência.
13. Conferir preços e tipos de ajuste.
14. Confirmar que ações de edição alteram somente o rascunho.
15. Confirmar que publicação exige ação explícita.
16. Verificar estados de erro e sucesso.
17. Verificar preservação de dados ao trocar abas.
18. Verificar serialização do documento candidato.
19. Confirmar que o candidato corresponde ao schema.
20. Testar publicação bem-sucedida com armazenamento simulado.
21. Testar conflito de revisão.
22. Testar erro de validação.
23. Confirmar que nenhum erro é silenciado por um rerender visual.
24. Validar os estados de acesso.
25. Integrar mudanças por família funcional.

#### Controle negativo

Não alterar a semântica dos dados para fazer com que controles visualmente semelhantes compartilhem o mesmo estado.

#### DoD específico

Campos administrativos continuam editando o documento V5; nenhuma regra comercial foi deslocada para um componente visual.

---

### DOM-010 — Consolidar a autorização de preços base no Viewer

**Prioridade:** P0  
**Tipo:** segurança de publicação e apresentação  
**Dependências:** DOM-004, DOM-008  
**Estado:** implementação já existente; requer reconciliação e validação.

#### Objetivo

Preservar a autorização global OFF por padrão e a relação correta entre Admin, configuração publicada, API pública e Viewer.

#### Contrato atual

O campo:

`viewerPricePublication: { enabled: boolean }`

é opcional.

Quando ausente, a publicação de preços permanece desativada.

O Admin permite alterar esse campo no rascunho, mas sua efetivação depende de uma publicação autenticada.

#### Procedimento

1. Confirmar o campo no schema V5.
2. Confirmar que o campo ausente equivale a OFF.
3. Confirmar rejeição de formatos inválidos.
4. Confirmar que o controle aparece na aba Preços.
5. Confirmar que o controle está indisponível quando a fonte publicada não satisfaz o requisito V5.
6. Confirmar que a alteração do checkbox modifica somente o rascunho.
7. Confirmar mensagem explicativa apropriada.
8. Confirmar que o backend não reconhece parâmetro público como autorização.
9. Publicar ON somente em fixture controlada.
10. Confirmar persistência e readback.
11. Solicitar projeção pública 0.2.
12. Confirmar schema 0.2 quando autorizado.
13. Confirmar exposição somente de `basePriceCents` dos módulos elegíveis.
14. Confirmar ausência de preço para módulo oculto.
15. Confirmar ausência de preço para regra inválida.
16. Confirmar ausência de preço para valor zero.
17. Confirmar ausência de fallback do priceBook.
18. Confirmar ausência de margens e regras administrativas.
19. Solicitar projeção 0.1 legada.
20. Confirmar que ela não contém preços.
21. Desativar a permissão na fixture.
22. Publicar novamente.
23. Confirmar revogação dos preços.
24. Confirmar política de cache `no-store`.
25. Verificar que o Viewer remove o bloco visual de preço.
26. Confirmar que dimensões permanecem exibidas.
27. Confirmar que o valor é identificado como preço base, não orçamento total.
28. Testar responsividade e atualização por seleção.
29. Executar testes de DTO, endpoint e browser.
30. Registrar a diferença entre garantia local e validação real de publicação.

#### Observação relevante sobre Deploy Preview

O endpoint público permite, sob condições restritas, que um Deploy Preview sem snapshot próprio utilize uma projeção já pública da origem principal.

Esse fallback aceita somente o contrato público 0.1.

Portanto, ele não deve ser utilizado como prova de que a publicação de preços 0.2 funciona integralmente em Preview.

Para validar ON/OFF, utilizar o backend simulado com fonte V5 válida e, quando autorizado e necessário, um ambiente que possua publicação própria adequada.

#### Testes existentes

- `tests/viewer-base-price-publication.test.cjs`
- `tests/viewer-base-price-browser-gate.mjs`
- Testes de endpoint e V5 normal save.
- Gate de publicação de preços do Viewer.

#### DoD específico

OFF por ausência ou publicação, ON exclusivamente mediante autorização persistida, projeção restrita e apresentação correta no Viewer.

---

## 8. Marco DOM-M4 — Contratos de consumo e segurança

### DOM-011 — Fortalecer o endpoint Buyer e a fixture autorizada

**Prioridade:** P0  
**Tipo:** segurança e confiabilidade operacional  
**Dependências:** DOM-003, DOM-006, DOM-007

#### Objetivo

Permitir validações reproduzíveis do Configurador sem desativar autenticação nem depender de dados inválidos hospedados.

#### Contexto

O endpoint `/api/buyer-configuration` verifica o acesso antes de ler a fonte publicada.

Ele permite os atores autorizados pela política específica, incluindo situações de sessão temporária válida.

Se a publicação estiver ausente ou inválida, o endpoint não inventa uma configuração utilizável a partir de defaults.

Essa proteção precisa continuar.

#### Procedimento

1. Identificar a política de acesso do endpoint.
2. Identificar a fonte de identidade.
3. Identificar o mecanismo de sessão temporária.
4. Confirmar a ordem de autorização e leitura.
5. Testar usuário anônimo sem sessão.
6. Testar usuário sem papel autorizado.
7. Testar usuário autorizado.
8. Testar sessão temporária válida.
9. Testar sessão temporária expirada/inválida.
10. Testar falha do serviço de identidade.
11. Testar falha do armazenamento de sessões.
12. Confirmar códigos de erro corretos.
13. Confirmar ausência de leitura de configuração antes da autorização.
14. Criar fixture local a partir dos defaults validados e do catálogo existente.
15. Gerar um documento V5 válido em memória.
16. Produzir o Buyer DTO pelo projetor real.
17. Servir o DTO somente em origem de teste.
18. Confirmar que a fixture não depende de credenciais.
19. Confirmar que a fixture não altera produção ou Preview.
20. Confirmar que o Configurador reconhece o payload.
21. Aguardar estado V5 validado.
22. Testar DOM e componentes necessários.
23. Comparar a fixture com o contrato do endpoint real.
24. Documentar suas diferenças.
25. Executar regressões funcionais.
26. Registrar que a fixture local não comprova autenticação hospedada.
27. Usar ambiente autenticado somente para gates que exigem essa prova.

#### Critério de segurança

A fixture poderá fornecer respostas sintéticas em ambiente local explicitamente controlado.

Ela não poderá introduzir um bypass de autenticação acessível em produção.

#### DoD específico

Configurador pode ser reproduzido localmente com V5 válido; backend continua falhando fechado para ausência de publicação ou autorização.

---

### DOM-012 — Consolidar o Viewer como consumidor público restrito

**Prioridade:** P1  
**Tipo:** fronteira de apresentação  
**Dependências:** DOM-010, CMP-016

#### Objetivo

Garantir que mudanças editoriais e visuais do Viewer não alterem o contrato de exposição pública.

#### Procedimento

1. Identificar a versão do DTO solicitada pelo Viewer.
2. Confirmar validação do payload recebido.
3. Confirmar validação de membros do catálogo.
4. Confirmar validação de visibilidade.
5. Confirmar validação de acabamentos.
6. Confirmar validação de dimensões.
7. Confirmar validação de preço quando presente.
8. Testar payload 0.1.
9. Testar payload 0.2.
10. Testar payload de schema desconhecido.
11. Testar módulo inexistente.
12. Testar finish inválido.
13. Testar dimensões inválidas.
14. Testar preço incompatível com 0.1.
15. Testar erro HTTP.
16. Confirmar ausência de fallback silencioso para dados privados.
17. Confirmar seleção inicial baseada no payload.
18. Confirmar seleção de outro módulo.
19. Confirmar atualização de overview.
20. Confirmar atualização da cena.
21. Confirmar atualização de vistas técnicas.
22. Confirmar atualização de dimensões e preço autorizado.
23. Verificar deep links válidos e inválidos.
24. Confirmar que um módulo oculto não é exibido indevidamente.
25. Testar claro/escuro e responsividade.
26. Confirmar que a interface de erro é adequada.
27. Integrar mudanças de apresentação com contrato público preservado.

#### DoD específico

Viewer renderiza exclusivamente dados do DTO público válido e não amplia a superfície de exposição.

---

### DOM-013 — Consolidar políticas de acesso por superfície

**Prioridade:** P0  
**Tipo:** segurança transversal  
**Dependências:** DOM-001, DOM-011

#### Objetivo

Garantir que as permissões sejam determinadas pelo backend e que os menus apenas representem essas permissões.

#### Procedimento

1. Inventariar políticas `canManageAdministration`, `canUseConfigurator` e equivalentes.
2. Identificar os endpoints que as aplicam.
3. Identificar seus estados anônimo, admin, staff, comprador e sessão temporária.
4. Confirmar os campos de identidade utilizados.
5. Verificar roles em metadados.
6. Confirmar comportamento para sessão temporária.
7. Testar tentativa de acesso indevido à configuração administrativa.
8. Testar tentativa de acesso indevido ao Buyer DTO.
9. Verificar acesso público ao Viewer.
10. Confirmar proteção das rotas privadas quando aplicável.
11. Confirmar que ocultar um link não é considerado autorização.
12. Confirmar que renderizar um link não concede autorização.
13. Verificar logout e expiração.
14. Simular respostas assíncronas atrasadas.
15. Confirmar revisão de estado da navegação privada.
16. Testar falhas de Identity.
17. Testar falhas de banco de sessões.
18. Confirmar que erros não expõem dados.
19. Verificar ausência de dados de usuário em capturas e relatórios.
20. Executar testes de política e endpoint.
21. Registrar os limites dos mocks.
22. Integrar qualquer correção como pacote de segurança específico.

#### DoD específico

Nenhuma autorização depende apenas do DOM; endpoints protegidos rejeitam operações não autorizadas e a interface representa corretamente o estado conhecido.

---

### DOM-014 — Consolidar as fronteiras Core / apresentação

**Prioridade:** P1  
**Tipo:** redução de acoplamento  
**Dependências:** DOM-006…013

#### Objetivo

Permitir que os componentes extraídos na Parte IV utilizem contratos explícitos, sem importar toda a aplicação.

#### Procedimento

1. Identificar componentes de apresentação do Configurador.
2. Identificar componentes de apresentação do Viewer.
3. Localizar chamadas ao Core.
4. Identificar quais chamadas são necessárias para renderização.
5. Identificar quais chamadas pertencem ao controle de estado.
6. Identificar possíveis decisões de domínio duplicadas no renderer.
7. Confirmar que a normalização é feita pela fonte adequada.
8. Confirmar que o renderer recebe os dados já preparados.
9. Identificar cálculos repetidos.
10. Separar formatação de cálculo.
11. Identificar políticas de visibilidade duplicadas.
12. Identificar cópias de dados que podem divergir.
13. Propor adaptadores mínimos quando houver acoplamento excessivo.
14. Evitar APIs genéricas para casos que possuem um único consumidor.
15. Implementar um conjunto por vez.
16. Testar resultados calculados antes/depois.
17. Testar DOM e interações.
18. Verificar que o bundle não cresceu desproporcionalmente.
19. Integrar sem alterar os schemas.
20. Registrar as duplicações eliminadas.
21. Encerrar com benefício demonstrado.

#### DoD específico

Componentes recebem os dados de que precisam e não assumem responsabilidade de validação, preço, persistência ou autorização.

---

## 9. Marco LOC-M0 — Classificação completa dos textos localizáveis

### LOC-001 — Consolidar o inventário ARC-13

**Prioridade:** P0  
**Tipo:** inventário de cobertura  
**Dependências:** CMP-002, DOM-001  
**Estado atual:** candidata #274, sem catálogo implementado

#### Objetivo

Transformar as 1.026 ocorrências candidatas em um inventário confiável de responsabilidades textuais.

#### Procedimento

1. Fixar a baseline atual.
2. Recuperar o inventário da PR #274.
3. Conferir validade sintática do JSON.
4. Confirmar hashes da fonte analisada.
5. Confirmar a versão do scanner.
6. Confirmar a origem autoral dos HTMLs gerados.
7. Verificar o mapeamento das 420 ocorrências HTML.
8. Revisar fontes JavaScript identificadas.
9. Identificar textos condicionais não capturados diretamente.
10. Identificar interpolação de strings.
11. Identificar textos provenientes de objetos de dados.
12. Identificar textos de templates.
13. Identificar atributos acessíveis.
14. Identificar placeholders e títulos.
15. Identificar textos de erro exibidos.
16. Identificar textos de diagnóstico não exibidos.
17. Identificar strings de identificador técnico.
18. Identificar campos de dados comerciais.
19. Identificar conteúdo editorial autoral.
20. Confirmar que cada ocorrência possui owner/rota.
21. Registrar os limites do scanner.
22. Conferir alterações de código desde o snapshot.
23. Reconciliar IDs alterados apenas por posição.
24. Preservar a continuidade semântica entre versões.
25. Gerar a lista de ocorrências ainda não classificadas.
26. Integrar o inventário revisado quando estiver pronto.

#### Regra de escopo

A cobertura deve ser ampla.

A extração, porém, deve incidir apenas sobre textos classificados como localizáveis.

#### DoD específico

Inventário atualizado, válido, com proveniência e classificação pendente explicitamente identificada.

---

### LOC-002 — Classificar textos por autoridade e função

**Prioridade:** P0  
**Tipo:** decisão semântica  
**Dependências:** LOC-001

#### Classes propostas

| Classe | Exemplo | Tratamento |
|---|---|---|
| `ui-static` | “Abrir menu” | Catálogo de UI |
| `ui-dynamic` | “Mostrar vista 2” | Chave com parâmetro |
| `accessibility` | Nome acessível de botão | Catálogo com contexto semântico |
| `feedback` | Erro apresentado ao usuário | Catálogo de mensagens |
| `editorial` | Texto institucional | Fonte editorial versionada |
| `domain-authored` | Nome de módulo definido no Admin | Preservar no V5 |
| `domain-derived` | Valor calculado ou descrição derivada | Preservar fonte e formatação |
| `diagnostic` | Erro interno capturado e descartado | Fora do catálogo UI |
| `identifier` | Schema, ID e chave técnica | Fora do catálogo |
| `decorative` | Ícone ou símbolo não verbal | Revisar semântica, não traduzir automaticamente |
| `uncertain` | Origem ou consumidor desconhecido | Revisão necessária |

#### Procedimento

1. Separar ocorrências por classe provável.
2. Identificar quem edita cada texto.
3. Identificar onde ele aparece.
4. Verificar se o texto é estático.
5. Verificar se é resultado de cálculo.
6. Verificar se pode variar por dados publicados.
7. Verificar se contém dados do usuário.
8. Verificar se contém plural ou número.
9. Verificar se contém unidade monetária.
10. Verificar se é um nome acessível.
11. Confirmar a semântica do elemento que recebe o texto.
12. Conferir textos visualmente iguais usados em funções diferentes.
13. Conferir textos diferentes que representam a mesma função.
14. Identificar cópias que deveriam compartilhar uma chave.
15. Identificar cópias que precisam permanecer independentes.
16. Registrar dúvidas de conteúdo para o owner.
17. Registrar problemas técnicos de acessibilidade separadamente.
18. Evitar transformar uma aprovação visual em aprovação textual.
19. Definir a destinação de cada ocorrência.
20. Gerar o backlog de extração a partir das classificações.

#### Casos concretos do inventário

**“Saiba mais”** e destino `/about/` possuem decisão de conteúdo registrada. Isso não determina automaticamente a chave de catálogo.

**“Casa em Módulos, início”** teve a pontuação confirmada. Isso não implica uma única chave para todos os contextos em que a frase aparece.

**“Abrir vídeo em tela cheia”** e **“Sair da tela cheia”** são textos de controle associados a estados diferentes da mesma interação.

**“Não foi possível carregar o player do YouTube.”** é diagnóstico interno descartado pelo fluxo de fallback, não necessariamente uma mensagem visível.

O texto alternativo de uma nova arte deve ser reavaliado quando o conteúdo da imagem muda.

#### DoD específico

Toda ocorrência possui classificação, owner e destino; nenhuma classe `uncertain` é silenciosamente tratada como texto de UI.

---

## 10. Marco LOC-M1 — Catálogo de localização em código

### LOC-003 — Definir o catálogo canônico `pt-BR`

**Prioridade:** P1  
**Tipo:** fundação de localização  
**Dependências:** LOC-002  
**Contrato:** ARC-09 e ARC-13

#### Objetivo

Criar uma fonte canônica para os textos de interface localizáveis, sem CMS, sem dependência externa e sem ativar novos idiomas.

#### Princípios

1. Chaves semânticas, não baseadas no texto literal.
2. Texto versionado no repositório do Produto.
3. Categorias reconhecíveis.
4. Suporte a parâmetros.
5. Comportamento explícito para chave ausente.
6. Validação no build/testes.
7. Compatibilidade com HTML autoral e JS existente.
8. Sem duplicação editável de mensagens.

#### Exemplo de estrutura lógica

```json
{
  "ui": {
    "menu": {
      "open": "Abrir menu",
      "close": "Fechar menu"
    },
    "theme": {
      "light": "Claro",
      "dark": "Escuro",
      "auto": "Automático"
    }
  },
  "viewer": {
    "basePrice": "Valor base do módulo",
    "showView": "Mostrar vista {index}"
  }
}
```

O exemplo demonstra a forma proposta, não representa um catálogo aprovado ou existente.

#### Procedimento

1. Selecionar uma organização de arquivos compatível com o build.
2. Definir esquema de chaves.
3. Definir regras de nomeação por domínio.
4. Definir campos obrigatórios.
5. Definir tratamento de interpolação.
6. Definir escape e segurança.
7. Definir política de chaves ausentes.
8. Definir política de textos aprovados e pendentes.
9. Definir regra para variantes de acessibilidade.
10. Definir regra para plurais, se necessário.
11. Confirmar compatibilidade com `Intl`.
12. Definir como HTML compilado recebe textos.
13. Definir como JS clássico consome textos.
14. Evitar dependência de carregamento assíncrono de tradução para páginas públicas.
15. Criar um conjunto inicial pequeno de chaves.
16. Provar consumo em um componente real.
17. Testar que a tradução portuguesa não muda.
18. Testar ausência de HTML arbitrário em interpolação.
19. Medir custo da implementação.
20. Ajustar a estrutura se o primeiro consumidor revelar complexidade desnecessária.
21. Integrar a fundação.
22. Registrar convenções de manutenção.

#### DoD específico

Uma fonte `pt-BR` versionada existe e possui consumidores reais, com validação e sem dependência de biblioteca pesada ou serviço externo.

---

### LOC-004 — Extrair textos dos fragmentos e páginas estáticas

**Prioridade:** P1  
**Tipo:** migração incremental  
**Dependências:** LOC-003, CMP-002

#### Objetivo

Centralizar textos localizáveis de páginas públicas preservando HTML completo e acessível no build.

#### Procedimento

1. Escolher a primeira família textual.
2. Fixar baseline de texto e atributos.
3. Identificar fonte autoral do HTML.
4. Identificar se a região pertence a fragmento compartilhado.
5. Definir chaves.
6. Confirmar propriedade das mensagens.
7. Modificar a fonte autoral.
8. Resolver textos durante a compilação, se isso for a abordagem mínima escolhida.
9. Gerar o HTML final.
10. Confirmar que não há placeholders de catálogo sem resolução.
11. Verificar textos visíveis.
12. Verificar pontuação.
13. Verificar `aria-label`.
14. Verificar `alt`.
15. Verificar `title`.
16. Verificar `placeholder`.
17. Confirmar links e destinos.
18. Confirmar que a página continua legível sem JS.
19. Executar `pages:check`.
20. Comparar DOM antes/depois.
21. Verificar que mudanças de texto são somente as autorizadas.
22. Executar teste visual quando o comprimento afetar layout.
23. Integrar a família.
24. Registrar chaves migradas e exceções.

#### Regra de implementação

Não substituir o conteúdo estático por texto injetado exclusivamente em runtime se o mesmo resultado puder ser produzido de modo simples no build.

#### DoD específico

HTML final contém os textos corretos, a fonte autoral é única e a migração não prejudica disponibilidade sem JavaScript.

---

### LOC-005 — Extrair textos de controladores e componentes JS

**Prioridade:** P1  
**Tipo:** migração incremental  
**Dependências:** LOC-003, CMP-018

#### Objetivo

Centralizar textos de interface gerados dinamicamente sem alterar o comportamento dos controladores.

#### Procedimento

1. Escolher um componente completo.
2. Identificar todos os textos localizáveis que ele produz.
3. Identificar textos de estados.
4. Identificar atributos acessíveis.
5. Identificar interpolações.
6. Definir chaves semânticas.
7. Preservar os textos existentes como referência.
8. Substituir literais no componente.
9. Usar inserção textual segura.
10. Evitar interpolar HTML não confiável.
11. Confirmar que nomes acessíveis continuam corretos.
12. Confirmar que a troca de estado atualiza texto e ARIA.
13. Testar parâmetros numéricos.
14. Testar plural quando aplicável.
15. Testar formatação de valores.
16. Confirmar que callbacks e listeners não foram alterados.
17. Confirmar que a ordem de renderização permanece.
18. Confirmar que a aplicação não depende de catálogo remoto.
19. Comparar resultados visíveis.
20. Executar testes de contrato.
21. Testar browser se o conteúdo for dinâmico.
22. Integrar.
23. Registrar cobertura migrada.

#### Candidatos iniciais

- Controle de tema.
- Menu público.
- Nomes de botões de vídeo.
- Mensagens simples do Viewer.

Esses componentes têm contratos relativamente bem delimitados.

#### DoD específico

Textos dinâmicos têm fonte canônica, permanecem semanticamente corretos e não alteram o funcionamento da interface.

---

### LOC-006 — Extrair textos do Admin e Configurador sem migrar conteúdo comercial

**Prioridade:** P1/P2  
**Tipo:** migração por domínio de UI  
**Dependências:** LOC-005, DOM-009/011

#### Objetivo

Consolidar mensagens administrativas e de configuração sem deslocar conteúdo editável do V5.

#### Procedimento

1. Identificar as mensagens fixas do Admin.
2. Identificar nomes de controles.
3. Identificar validações apresentadas ao usuário.
4. Identificar mensagens de publicação.
5. Identificar mensagens de autenticação.
6. Identificar textos de navegação do Configurador.
7. Identificar mensagens de seleção.
8. Identificar avisos de indisponibilidade.
9. Separar textos fixos de labels definidos no V5.
10. Separar valores comerciais de mensagens explicativas.
11. Separar nomes de materiais de texto de UI.
12. Separar erros técnicos de feedback exibido.
13. Identificar interpolações de IDs e nomes de módulo.
14. Definir chaves por área.
15. Migrar uma família por vez.
16. Testar DOM e texto.
17. Confirmar que nomes de entidades continuam vindo dos dados.
18. Confirmar que erros representam o estado real da operação.
19. Confirmar que mensagens de sucesso aparecem apenas após confirmação adequada.
20. Confirmar que textos de publicação ON/OFF permanecem explícitos.
21. Verificar que nenhuma chave inclui segredo ou dado pessoal.
22. Testar `aria-label` e regiões vivas.
23. Executar suites de domínio afetadas.
24. Integrar.
25. Registrar cobertura e exceções.

#### DoD específico

Textos fixos de UI migrados; nomes, valores e descrições comerciais continuam sob sua autoridade correta.

---

## 11. Marco LOC-M2 — Cobertura e conformidade de localização

### LOC-007 — Automatizar verificação de chaves e consumidores

**Prioridade:** P1  
**Tipo:** engenharia de testes  
**Dependências:** LOC-003…006

#### Objetivo

Evitar regressões de localização e duplicações de fonte após a migração.

#### Procedimento

1. Definir catálogo e schema de chaves.
2. Construir validador estático.
3. Detectar chave inexistente.
4. Detectar chave duplicada.
5. Detectar valor vazio indevido.
6. Detectar parâmetro ausente.
7. Detectar parâmetro inesperado.
8. Detectar referência não utilizada.
9. Identificar textos literais novos em locais migrados.
10. Comparar o inventário com a cobertura.
11. Registrar exceções explícitas.
12. Confirmar que o scanner não confunde diagnóstico com texto UI.
13. Verificar os atributos acessíveis.
14. Verificar texto nos estados de interação.
15. Testar interpolação segura.
16. Executar amostras de browser.
17. Verificar HTML compilado.
18. Confirmar ausência de dependência de rede para o catálogo.
19. Verificar rollback por família.
20. Integrar o gate no CI adequado.
21. Registrar limites de cobertura dinâmica.

#### DoD específico

O CI detecta regressões relevantes de catálogo e os consumidores migrados são rastreáveis até suas chaves.

---

### LOC-008 — Fechar cobertura integral ARC-13 por classificação

**Prioridade:** P1  
**Tipo:** fechamento arquitetural  
**Dependências:** LOC-001…007

#### Objetivo

Concluir a obrigação de abrangência do ARC-13 sem transformar todas as ocorrências candidatas em chaves.

#### Procedimento

1. Regerar inventário no head final.
2. Reconciliar IDs anteriores.
3. Confirmar todas as rotas em escopo.
4. Confirmar fontes HTML.
5. Confirmar fontes JS.
6. Confirmar conteúdos condicionais conhecidos.
7. Confirmar textos acessíveis.
8. Confirmar mensagens de feedback.
9. Confirmar textos de UI classificados.
10. Confirmar textos editoriais classificados.
11. Confirmar dados comerciais excluídos.
12. Confirmar diagnósticos excluídos.
13. Confirmar identificadores técnicos excluídos.
14. Confirmar que cada exceção possui motivo.
15. Confirmar que cada texto localizável possui chave e consumidor.
16. Confirmar que a fonte portuguesa reproduz o texto aprovado.
17. Testar a saída HTML.
18. Testar estados JS dinâmicos.
19. Verificar acessibilidade nos casos relevantes.
20. Confirmar que nenhum idioma adicional foi ativado sem requisito.
21. Registrar lacunas remanescentes quando dependerem de novos consumidores.
22. Atualizar o DoD e timeline.
23. Encerrar ARC-13 somente para o escopo comprovado.

#### DoD específico

Cobertura integral dos textos realmente localizáveis no escopo, exceções classificadas e migração validada; não há lacunas silenciosas.

---

## 12. Matriz de bundles de testes

Esta frente possui contratos de risco mais elevado do que os pacotes predominantemente visuais.

Por isso, os bundles devem considerar tanto **o comportamento correto** quanto **a ausência de comportamentos proibidos**.

| Bundle | Finalidade | Pacotes |
|---|---|---|
| BT-DOM-00 | Schema, fonte, validação e projeção | DOM-001/002 |
| BT-DOM-10 | Persistência V5, CAS, readback e compatibilidade | DOM-003/004/005 |
| BT-DOM-20 | Hierarquia, etapas, componentes e layout | DOM-006/007 |
| BT-DOM-30 | Pricing e regras comerciais | DOM-008/010 |
| BT-DOM-40 | Admin e publicação | DOM-009/010 |
| BT-DOM-50 | Auth, Buyer DTO e segurança | DOM-011/013 |
| BT-DOM-60 | Viewer e projeção pública | DOM-010/012 |
| BT-DOM-70 | Fronteira Core/apresentação | DOM-014 |
| BT-LOC-10 | Inventário e classificação | LOC-001/002 |
| BT-LOC-20 | Catálogo e HTML autoral | LOC-003/004 |
| BT-LOC-30 | JS, interpolação e acessibilidade | LOC-005/006 |
| BT-LOC-40 | Cobertura, exceções e integração | LOC-007/008 |

### 12.1 BT-DOM-10 — Persistência

Cenários mínimos:

- Fonte V5 válida.
- Fonte ausente.
- Fonte corrompida.
- Schema desconhecido.
- Revisão divergente.
- ETag divergente.
- Resposta de escrita sem confirmação.
- Readback ausente.
- Readback com digest diferente.
- Readback semanticamente diferente.
- Tentativa de downgrade.
- Tentativa de operação de migração aposentada.
- Nenhuma escrita nos casos rejeitados.

A suite deverá deixar claro quais cenários são simulações de provider e quais são testes do handler HTTP.

### 12.2 BT-DOM-30 — Preços

Cenários mínimos:

- Módulo com valor base válido.
- Módulo com valor zero.
- Módulo sem regra.
- Módulo oculto.
- Percentual em papel permitido.
- Percentual em papel incompatível.
- Acabamento com adicional.
- Puxador e alocação.
- Ajustes globais e locais.
- Falta de preço necessário ao orçamento.
- Publicação pública OFF.
- Publicação pública ON.
- Projeção 0.1 sem preços.
- Projeção 0.2 com preços autorizados.
- Revogação posterior.
- Ausência de dados privados.

### 12.3 BT-DOM-50 — Autorização

Cenários mínimos:

- Anônimo.
- Admin.
- Staff.
- Usuário sem papel suficiente.
- Sessão temporária válida.
- Sessão temporária inválida.
- Sessão expirada.
- Falha de Identity.
- Falha da store de sessões.
- Tentativa de acesso a endpoint proibido.
- Tentativa de salvar sem autorização.
- Navegação com atualização assíncrona de sessão.
- Logout.
- Nenhum vazamento de dados protegidos.

### 12.4 BT-LOC-30 — Textos em runtime

Cenários mínimos:

- Texto estático.
- Texto com parâmetro.
- Nome acessível inicial.
- Nome acessível após mudança de estado.
- Tooltip.
- Texto em região viva.
- Erro real.
- Sucesso real.
- Chave ausente.
- Parâmetro ausente.
- Conteúdo contendo caracteres especiais.
- Valores e nomes comerciais preservados.
- Ausência de inserção HTML insegura.
- Diferenças de layout provocadas por texto, quando relevantes.

---

## 13. Sequência de integração proposta

A ordem abaixo separa dependência real de preferência operacional.

### Janela A — Contratos e segurança

Executar:

- DOM-001
- DOM-002
- DOM-003
- DOM-004

Em paralelo, iniciar LOC-001, pois o inventário textual não depende da conclusão da persistência.

**Saída:** autoridade clara, DTOs identificados e publicação protegida por testes vinculados.

### Janela B — Compatibilidade e fluxo

Executar:

- DOM-005
- DOM-006
- DOM-007
- DOM-008

Em paralelo, classificar textos em LOC-002.

**Saída:** fronteiras de compatibilidade encerradas e fluxo/apresentação estabilizados.

### Janela C — Admin e Viewer

Executar:

- DOM-009
- DOM-010
- DOM-011
- DOM-012
- DOM-013

Alguns subpacotes podem avançar independentemente.

Exemplo: testes de projeção pública não precisam aguardar a extração de todos os textos do Admin.

**Saída:** publicação comercial, transporte Buyer e projeção pública verificáveis.

### Janela D — Integração Core/UI

Executar DOM-014 e os pacotes visuais da Parte IV que dependem dele.

**Saída:** componentes utilizam contratos existentes sem criar novas autoridades.

### Janela E — Localização

Executar:

- LOC-003
- LOC-004
- LOC-005
- LOC-006

A extração ocorrerá por famílias completas de consumidores.

**Saída:** primeira fonte canônica `pt-BR` integrada, seguida de migração incremental.

### Janela F — Cobertura e fechamento

Executar:

- LOC-007
- LOC-008
- Readback transversal de DOM-001…014.
- Atualização do DoD por ID.

**Saída:** cobertura de localização e domínio comprovada na branch-alvo.

---

## 14. Caminho crítico

Não considero a migração completa dos textos um pré-requisito para consolidar o Viewer.

Também não considero a revisão de todos os componentes administrativos um pré-requisito para integrar o header público.

O caminho crítico desta frente é mais restrito:

```text
DOM-001 — Contratos existentes
          │
          ▼
DOM-003 — Fonte publicada
          │
          ▼
DOM-004 — Save V5 seguro
          │
          ├──────────────────┐
          ▼                  ▼
DOM-011 — Buyer        DOM-010 — Preços públicos
          │                  │
          ▼                  ▼
DOM-007 — Layout       DOM-012 — Viewer
          │                  │
          └────────┬─────────┘
                   ▼
            DOM-014 — Fronteiras
                   │
                   ▼
       Integração Core / ferramentas
```

A trilha de localização pode avançar em paralelo:

```text
LOC-001 — Inventário
          │
          ▼
LOC-002 — Classificação
          │
          ▼
LOC-003 — Catálogo pt-BR
          │
          ├──────────────┐
          ▼              ▼
LOC-004 — HTML     LOC-005 — JS
          │              │
          └──────┬───────┘
                 ▼
           LOC-006 — Admin/Config
                 │
                 ▼
           LOC-007 — Testes
                 │
                 ▼
           LOC-008 — Cobertura
```

Os dois caminhos se encontram nos consumidores, mas não devem gerar bloqueio global quando não existe interseção real.

---

## 15. Pontos de interrogação

| ID | Questão | Resolução proposta |
|---|---|---|
| DOM-Q01 | Existem campos V5 ainda consumidos diretamente onde um DTO já seria suficiente? | Matriz de dependências por renderer |
| DOM-Q02 | Há alguma segunda autoridade de fluxo no Configurador? | Comparação de normalização, layout e renderers |
| DOM-Q03 | Os caminhos V3 restantes são todos necessários à recuperação? | Inspeção dos cenários e testes históricos |
| DOM-Q04 | Quais operações de publicação têm prova de provider real, além dos mocks? | Inventário ARC-15 e evidência de ambiente |
| DOM-Q05 | Há diferenças entre comportamentos de autorização nas rotas privadas? | Matriz de políticas por endpoint |
| DOM-Q06 | A fixture local Buyer reproduz todos os estados necessários aos testes de CSS/componentes? | Coverage de fixture versus DOM exigido |
| DOM-Q07 | Quais controles do Admin têm apresentação duplicada, mas estado de negócio distinto? | Matriz de controle/semântica |
| DOM-Q08 | Alguma regra de preço está sendo reproduzida dentro dos renderers? | Auditoria de funções e valores calculados |
| DOM-Q09 | A revogação de preços públicos foi verificada em ambiente real após publicação? | Gate autorizado de ON/OFF e leitura HTTP |
| DOM-Q10 | Há algum fallback de dados públicos que pode induzir erro de publicação? | Matriz de ausência/invalidade de snapshot |
| LOC-Q01 | Quais das 1.026 ocorrências são efetivamente localizáveis? | Classificação semântica integral |
| LOC-Q02 | Quais textos acessíveis dependem de revisão factual do conteúdo visual? | Revisão por elemento e mídia |
| LOC-Q03 | Quais strings já possuem autoridade compartilhada? | Mapa de owner e consumidores |
| LOC-Q04 | Qual é a menor interface de catálogo compatível com JS clássico e HTML gerado? | Primeiro piloto controlado |
| LOC-Q05 | Como verificar cobertura dinâmica sem exigir execução exaustiva de todas as combinações? | Instrumentação por origem/estado e amostragem por risco |
| LOC-Q06 | Como evitar que texto comercial editável migre para o catálogo UI? | Classificação e regra de exclusão verificável |
| LOC-Q07 | Existem labels iguais que precisam de chaves distintas por contexto? | Revisão semântica e de acessibilidade |
| LOC-Q08 | Quais strings condicionais não aparecem adequadamente no scanner atual? | Inspeção dos sinks e suplemento runtime |

---

## 16. Critérios de interrupção

Interromper uma mudança quando:

- Ela cria uma segunda autoridade de dados.
- Altera o schema apenas para facilitar componente visual.
- Move validação ou autorização para o navegador.
- Permite fallback silencioso de V5 inválido.
- Remove CAS ou readback sem solução equivalente.
- Introduz publicação automática de preço.
- Confunde DTO Buyer e DTO público.
- Envia preço, margem ou regra administrativa fora da allowlist.
- Considera um teste de mock prova de funcionamento em produção.
- Exige alterar produção para obter uma fixture de desenvolvimento.
- Tradução substitui conteúdo comercial editável por string fixa.
- O catálogo depende de carregamento remoto desnecessário.
- Uma mudança textual altera o contrato acessível sem revisão.
- A reestruturação adiciona mais autoridades do que elimina.
- Um pacote depende de outra tarefa não registrada no backlog.

O pacote entra em `blocked` somente quando a condição impede a sua entrega.

Uma limitação de revisão hospedada deve ser registrada como tal, sem transformar automaticamente outras entregas independentes em bloqueadas.

---

## 17. DoD da frente Core e localização

### 17.1 DoD de domínio

Uma entrega envolvendo Core/V5 somente estará `done` quando:

- A autoridade de dados está identificada.
- Os schemas aceitos são conhecidos.
- Os dados de entrada são validados.
- O resultado é determinístico para as entradas previstas.
- O consumidor usa o contrato correto.
- Permissões e publicação foram preservadas.
- Não foram introduzidos fallbacks inseguros.
- Os cenários negativos relevantes passaram.
- O código foi integrado à branch-alvo prevista.
- O head integrado possui evidência suficiente.
- O rollback não depende de modificar dados de produção.
- O backlog registra o estado e o recibo.

### 17.2 DoD de localização

Uma entrega envolvendo ARC-13 somente estará `done` quando:

- Textos localizáveis em seu escopo foram identificados.
- As classificações foram revisadas.
- Os valores portugueses aprovados foram preservados.
- As chaves possuem owner.
- Os consumidores foram migrados.
- O HTML compilado ou o runtime usa a fonte correta.
- Os atributos acessíveis foram verificados.
- As interpolações são seguras.
- Exceções estão registradas.
- Testes de cobertura passaram.
- A integração está comprovada.
- O relatório de progresso foi atualizado.

### 17.3 Regra de reporting

Cada pacote dessa frente aparecerá no anexo operacional dos oito turnos com:

`ID | entrega | dependências | status | DoD | evidence | notes`

Os estados permanecem:

- `not_started`
- `in_progress`
- `blocked`
- `in_review`
- `done`
- `cancelled`

Nenhum estado descrito neste capítulo constitui alteração real do backlog no Git. A consolidação do estado será feita com a reconciliação de evidências no documento final.

---

## 18. Revisão crítica do método

Existem quatro armadilhas metodológicas especialmente relevantes nesta frente.

### 18.1 Confundir segurança existente com complexidade desnecessária

ETag, revisão, readback e projeções restritas aumentam a quantidade de código, mas protegem contratos concretos.

Removê-los para reduzir complexidade aparente seria uma simplificação ruim.

O objetivo é reduzir repetição de verificações, código de adaptação desnecessário e inconsistências entre consumidores, mantendo essas garantias.

### 18.2 Confundir documentação de uma regra com execução da regra

Há documentação extensa descrevendo o que o Buyer DTO e a projeção pública não podem conter.

Isso é importante.

Mas a proteção mais valiosa é uma asserção executada quando o contrato relevante muda.

O pacote DOM-001 deve ligar cada proibição a uma prova.

O documento continua explicando a intenção; o CI verifica a aplicação.

### 18.3 Recriar funcionalidades que já existem

Os preços base são um exemplo claro.

Se o backlog contiver “Implementar preço no Viewer” sem registrar que a funcionalidade já está implementada, um agente poderá criar uma segunda solução.

O item correto será “Consolidar e validar o contrato existente”, com evidência de código, teste e publicação.

A mesma regra vale para:

- Flow normalizado.
- Projeção Buyer.
- Projeção pública.
- Renderer de cena.
- Componentes de apresentação.
- Autorização.
- Compilador das páginas públicas.

### 18.4 Confundir inventário com migração

Contar strings é uma etapa útil, mas não produz, por si só, um catálogo localizável.

Da mesma forma, criar um catálogo com mil chaves não garante qualidade se seus consumidores e contextos semânticos estiverem incorretos.

A sequência apropriada é:

**inventariar → classificar → definir autoridade/chave → migrar consumidor → testar → integrar → registrar DoD.**

Isso deve ser feito incrementalmente, mas com cobertura global rastreável.

---

## 19. Marcos de conclusão da Parte V

| Marco | Resultado | Pacotes |
|---|---|---|
| **DOM-M0** | Autoridades e contratos identificados | DOM-001/002 |
| **DOM-M1** | Publicação e recuperação com fronteiras comprovadas | DOM-003/004/005 |
| **DOM-M2** | Fluxo, apresentação e preços preservados pelo Core | DOM-006/007/008 |
| **DOM-M3** | Admin e autorização de preço público integrados | DOM-009/010 |
| **DOM-M4** | Buyer, Viewer e acesso com contratos verificáveis | DOM-011/012/013/014 |
| **LOC-M0** | Inventário integral classificado | LOC-001/002 |
| **LOC-M1** | Catálogo `pt-BR` e primeiros consumidores integrados | LOC-003/004/005/006 |
| **LOC-M2** | Cobertura e testes de localização fechados | LOC-007/008 |

Não criaremos uma porcentagem manual para cada marco.

No anexo DoD, sua conclusão será derivada das tarefas verificadas. Quando alguma obrigação for explicitamente excluída, a exclusão precisará de justificativa e não poderá ficar oculta em um percentual agregado.

---

## 20. Parecer final — Parte V

O Core V5 e suas projeções já constituem uma fundação razoavelmente madura.

O que precisa melhorar é sua integração operacional com o desenvolvimento das interfaces.

A recomendação é **não iniciar uma nova arquitetura de dados**.

Em vez disso:

1. Formalizar e testar as fontes existentes.
2. Reaproveitar os contratos já implementados.
3. Fortalecer as fronteiras de publicação e autorização.
4. Reproduzir o Configurador com fixtures válidas e seguras.
5. Confirmar o Viewer como consumidor restrito.
6. Consolidar os renderers sobre as projeções atuais.
7. Criar uma fonte canônica para os textos localizáveis.
8. Migrar consumidores por conjuntos relacionados.
9. Encerrar cada incremento com DoD e integração comprovada.

O objetivo final é que alterações visuais e textuais se tornem mais fáceis, enquanto alterações comerciais continuem obedecendo a regras explícitas e centralizadas.

A boa arquitetura nesse ponto não é a que torna todos os consumidores iguais.

É a que **permite que consumidores diferentes usem as mesmas autoridades sem reproduzir suas regras**.

---

### Referências principais

**Core e publicação**

- [Administração V5](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/administration-v5.js)
- [Projeção Buyer](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/published-buyer-projection.js)
- [Projeção pública do Viewer](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/public-module-projection.js)
- [Leitor da configuração publicada](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/published-configuration.js)
- [Save normal V5](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/v5-normal-save.js)
- [Fluxo normalizado](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/flow-model.js)
- [Layout do fluxo](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/flow-layout.js)
- [Contrato de pricing](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/pricing-contract.js)
- [Cálculo de pricing](https://github.com/EAKerber/MobiliPresenter2D/blob/development/app/core/pricing.js)

**Endpoints**

- [Configuração administrativa](https://github.com/EAKerber/MobiliPresenter2D/blob/development/netlify/functions/configuration.mjs)
- [Buyer Configuration](https://github.com/EAKerber/MobiliPresenter2D/blob/development/netlify/functions/buyer-configuration.mjs)
- [Public Modules](https://github.com/EAKerber/MobiliPresenter2D/blob/development/netlify/functions/public-modules.mjs)

**Contratos e testes**

- [Publicação de preços base](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/architecture/viewer-base-price-publication-main-2026-10-21.md)
- [Teste da autorização de preço](https://github.com/EAKerber/MobiliPresenter2D/blob/development/tests/viewer-base-price-publication.test.cjs)
- [Teste browser de preços](https://github.com/EAKerber/MobiliPresenter2D/blob/development/tests/viewer-base-price-browser-gate.mjs)
- [Contrato arquitetural ARC-01…16](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md)
- [Inventário e reconciliação ARC-13](https://github.com/EAKerber/MobiliPresenter2D/blob/docs/arc13-post-273-reconciliation-20261114/docs/architecture/arc13/inventory-reconciliation-post-277-2026-11-16.md)
- [Matriz ARC-15 de assertions e publicação](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md)

**Limite de evidência:** esta etapa utilizou leitura do código, PRs, contratos, relatórios e testes existentes. Não foram executadas novas chamadas de API, autenticação, publicação, testes browser ou alterações em armazenamento.

---

<a id="capitulo-6"></a>
# Capítulo VI — Engenharia de testes, fixtures, CI e evidências de conclusão

## 1. Objetivo

Construir um sistema de validação que responda a cinco perguntas para cada conjunto de alterações:

1. **O que foi alterado?**
2. **Quais contratos podem ser afetados?**
3. **Quais testes realmente comprovam esses contratos?**
4. **Qual evidência permite considerar o resultado integrado e concluído?**
5. **Quais riscos não foram cobertos pela execução realizada?**

O objetivo não é maximizar a quantidade de testes.

Também não é minimizar sua quantidade.

O objetivo é reduzir o custo de obter evidência suficiente e confiável para continuar desenvolvendo o produto sem introduzir regressões.

### 1.1 Resultado esperado

Ao concluir esta frente, o projeto deverá possuir:

- Uma matriz rastreável entre requisitos, assertions, riscos e consumidores.
- Distinção entre testes de comportamento, testes estáticos, visualização real e verificação hospedada.
- Uma fixture local V5 confiável, independente de contas ou dados reais.
- Gatilhos de CI alinhados aos arquivos e contratos afetados.
- Uma estratégia de testes proporcionais ao risco.
- Falhas com diagnósticos suficientes para investigação.
- Evidências associadas a commit, ambiente e configuração exatos.
- Critérios explícitos de quando executar navegador ou Deploy Preview.
- Uma distinção entre artefato presente, integração em branch e publicação efetiva.
- Um protocolo simples de resultados para alimentar o DoD.
- Menor necessidade de reexecutar suites inteiras por incerteza administrativa.
- Preservação dos testes históricos necessários à proveniência dos assets.

### 1.2 Princípio fundamental

**Não eliminaremos um teste porque outro verifica uma condição semelhante. Eliminaremos ou consolidaremos redundância somente quando ficar comprovado que uma garantia não se perde.**

Dois testes podem usar a mesma fixture, chamar a mesma função ou verificar o mesmo valor e ainda proteger riscos diferentes.

A equivalência precisa ser demonstrada no nível da assertion e de seu contexto, não no nome do arquivo.

---

## 2. Diagnóstico da estrutura atual

### 2.1 Existe cobertura considerável, mas fragmentada

A baseline ARC-15 identificou:

| Dimensão | Observação |
|---|---|
| GitHub Actions | 21 workflows no Produto `main` |
| Suíte `app/npm test` | 21 comandos encadeados |
| Composição da suíte | 19 comandos Node e 2 validadores Python |
| Testes não invocados automaticamente | 8 arquivos identificados no levantamento |
| Discrepâncias entre triggers e execução | 4 casos documentados |
| Required checks | Não confirmados pelo acesso disponível |
| Redundância integral comprovada | Nenhum teste inteiro identificado |

As contagens são uma fotografia da baseline de inventário. Não constituem pontuação de qualidade nem um teto desejável.

Além desses elementos, existem testes no diretório `tests/` executados diretamente pelos workflows e validadores de arte externos à suíte `app`.

Uma leitura que conte somente `npm test` subestimará a cobertura.

Uma leitura que conte somente os 21 workflows poderá superestimar a independência das verificações.

### 2.2 Existem pelo menos quatro formas distintas de repetição

#### Reexecução do mesmo comando

Exemplo: `npm test` executado em diferentes workflows.

Isso pode consumir recursos repetidamente.

Mas cada workflow pode proteger um contexto distinto e produzir um status necessário para outra integração.

#### Repetição de assertions

Exemplo: verificações semelhantes de CAS/ETag/readback em testes de save normal V5 e migração histórica.

As assertions se parecem.

As operações não são equivalentes.

#### Repetição de fixture ou infraestrutura

Exemplo: iniciar o servidor local Buyer V5 em diferentes workflows de navegador.

A infraestrutura poderia ser reutilizada ou padronizada.

Isso não torna redundantes os testes que utilizam essa infraestrutura.

#### Sobreposição entre camadas

Exemplo: um teste puro verifica seleção/visibilidade; um teste de navegador verifica o mesmo estado através de DOM, foco e geometria.

Existe interseção.

Mas o segundo observa resultados que o primeiro não consegue comprovar.

Essas quatro formas precisam de classificações diferentes no relatório de auditoria.

### 2.3 O mecanismo de Browser V5 já possui um ponto comum

Os workflows de:

- Flow layout.
- Keyboard.
- Mobile.
- Summary/Pricing.

compartilham a preparação:

`tests/ci/prepare-local-v5-browser.sh`

Esse script chama:

`tests/ci/local-buyer-config-server.mjs`

O servidor cria um payload Buyer derivado dos defaults e o disponibiliza em loopback.

Essa é uma fundação de testes útil.

A oportunidade está em estabelecer seu contrato, aprimorar readiness e ciclo de vida, não em construir outra infraestrutura paralela.

### 2.4 Um teste visual foi apontado para a página errada

Na `main`, o teste:

`tests/exposed-sides-glass.cjs`

abre `app/index.html` via `file://`.

Entretanto, suas assertions exigem elementos e runtime próprios do Configurador.

Isso significa que a verificação não possui uma precondição válida para o contrato que pretende testar.

A PR [#280](https://github.com/EAKerber/MobiliPresenter2D/pull/280) propõe a correção: servidor local, rota `/config/`, fixture V5, porta efêmera e encerramento dos processos.

A proposta deve ser avaliada como correção de harness, e não como alteração funcional do produto.

### 2.5 O teste de tema possui um acoplamento textual discutível

`tests/ui-theme-contract.cjs` contém uma exigência de que todas as páginas carreguem uma URL de stylesheet com o mesmo sufixo de versão.

Mas a implementação atual utiliza revisões de URL diferentes em alguns shells.

Isso não prova, por si só, divergência funcional do tema.

A assertion deve responder à pergunta correta:

**A versão efetivamente carregada fornece o contrato de tema esperado?**

Se a URL idêntica não for uma exigência homologada, o teste precisa deixar de tratá-la como invariável.

É um exemplo claro de teste potencialmente frágil por verificar detalhes de implementação em vez da garantia arquitetural.

### 2.6 O compilador de páginas possui teste negativo que modifica arquivos autorais gerados

`tests/arc03c-source-authority.test.mjs` verifica corretamente se o build falha diante de drift.

Para isso, altera temporariamente HTML gerado e manifesto, restaurando-os depois.

O objetivo do teste é válido.

Entretanto, uma execução concorrente com build ou outra verificação sobre a mesma árvore pode produzir conflito transitório.

O teste deverá ser avaliado para execução isolada em diretório temporário, preservando a mesma garantia.

### 2.7 Um gate verde pode não ter sido executado no caminho esperado

O workflow de publicação de preços base do Viewer não possui trigger `pull_request` na baseline consultada.

O workflow ARC-03C também possui triggers limitados a branches históricas.

Isso cria uma pergunta operacional importante:

**Quando uma alteração relevante entra em uma PR atual, o teste correspondente é automaticamente executado?**

A existência do arquivo e de um workflow não responde a essa pergunta.

Precisamos verificar a alcançabilidade real da assertion.

---

## 3. Modelo de evidência

O plano precisa de uma classificação simples para indicar o que determinada evidência realmente demonstra.

Essa classificação será independente dos estados de progresso do DoD.

### 3.1 Níveis de evidência

| Nível | Tipo | O que demonstra |
|---|---|---|
| E0 | Inspeção estática | Presença, estrutura, referências e contratos textuais |
| E1 | Teste puro | Comportamento de funções e contratos em memória |
| E2 | Teste de integração local | Relação entre módulos, DTOs e handlers simulados |
| E3 | Browser local | DOM, CSSOM, interação e geometria em fixture controlada |
| E4 | Browser hospedado | Comportamento da aplicação publicada em ambiente específico |
| E5 | Fluxo protegido autorizado | Auth, sessão e publicação verificadas no ambiente pertinente |
| E6 | Readback de produção | Resultado observável da versão publicada, preferencialmente sem escrita |

Os níveis não são uma escada que todo pacote precisa percorrer.

Um refactor de função pura pode ser encerrado com E1/E2 e integração confirmada.

Uma mudança de header pode exigir E3 e eventualmente E4.

Uma alteração de autorização não pode ser considerada integralmente demonstrada apenas por E0.

Uma mudança de publicação de preços pode exigir E1, E2, E3 e E5 para a afirmação de validação operacional completa.

### 3.2 Regra de equivalência de evidência

Uma evidência somente substitui outra quando cobre:

1. O mesmo contrato.
2. O mesmo estado relevante.
3. O mesmo consumidor.
4. O mesmo risco.
5. Uma versão de código adequada.
6. O mesmo nível de fidelidade necessário.

Exemplo:

Um screenshot em Chromium pode demonstrar geometria específica.

Ele não substitui um teste de permissão de API.

Um mock de Blob pode demonstrar a lógica esperada de `onlyIfMatch`.

Ele não comprova sozinho as garantias do provider em produção.

### 3.3 Três eixos adicionais de estado

Para cada funcionalidade importante, registrar separadamente:

**Código:** a implementação está presente na árvore observada?

**Integração:** a implementação está efetivamente integrada na branch-alvo?

**Publicação:** a versão publicada incorpora e carrega a implementação?

Exemplo de recibo:

```text
Contrato: NAV-005
Código: presente em PR candidata
Integração: não integrado à main
Publicação: não publicada em produção
Browser local: PASS no head indicado
Browser hospedado: revisão parcial
DoD: in_review
```

A presença de um arquivo no código não comprova a aplicação no navegador.

A presença de um import CSS também não comprova que aquela declaração vence a cascata.

Da mesma forma, a redação de um manifesto não deve substituir a inspeção da integração e do recurso realmente carregado.

---

## 4. Marco TST-M0 — Auditoria de cobertura e seleção de testes

### TST-001 — Fixar baseline e mapa de execução

**Prioridade:** P0  
**Tipo:** inventário operacional  
**Dependências:** nenhuma além da confirmação das branches  
**Bundle:** BT-TST-00

#### Objetivo

Criar uma visão reproduzível dos workflows e comandos realmente disponíveis.

#### Procedimento

1. Fixar o SHA do Produto `main`.
2. Fixar o SHA de `development`.
3. Identificar as PRs candidatas que alteram testes.
4. Enumerar workflows da `main`.
5. Enumerar workflows exclusivos de `development`.
6. Enumerar workflows presentes apenas em PRs Draft.
7. Registrar eventos de cada workflow.
8. Registrar filtros de branch.
9. Registrar filtros de paths.
10. Registrar jobs e suas condições.
11. Registrar os comandos efetivamente executados.
12. Registrar dependências de Node, Python e navegador.
13. Identificar execuções de build.
14. Identificar dependências de fixture.
15. Identificar dependências de serviços externos.
16. Identificar uploads de artefatos.
17. Identificar quais jobs podem modificar dados ou branches.
18. Separar workflows de validação de workflows operacionais.
19. Registrar os arquivos de teste não invocados.
20. Publicar matriz workflow → gatilho → job → comando → resultado.

#### DoD

O inventário reproduz a CI atual e distingue workflows existentes, candidatos e históricos.

---

### TST-002 — Construir matriz assertion → contrato → risco

**Prioridade:** P0  
**Tipo:** auditoria analítica  
**Dependências:** TST-001  
**Bundle:** BT-TST-00

#### Objetivo

Transformar os testes existentes em cobertura inspecionável.

#### Estrutura mínima

| Campo | Significado |
|---|---|
| Assertion ID | Identidade estável da garantia |
| Source | Arquivo e função |
| Contract | Requisito protegido |
| Risk | Regressão que deve detectar |
| Consumer | Rota ou módulo afetado |
| State | Estado exercitado |
| Fixture | Precondição |
| Evidence | E0–E6 |
| Trigger | Como é executada |
| Negative | Se inclui comportamento proibido |
| Owner | Quem mantém o contrato |

#### Procedimento

1. Começar pelos testes de maior impacto.
2. Separar cada arquivo em grupos de assertions.
3. Identificar o contrato protegido.
4. Identificar o risco concreto.
5. Identificar estado inicial exigido.
6. Identificar dados utilizados.
7. Identificar se o teste observa resultado ou apenas texto-fonte.
8. Identificar se a assertion é positiva ou negativa.
9. Identificar o consumer real.
10. Identificar o ambiente.
11. Verificar o caminho de execução até a assertion.
12. Registrar testes cuja execução é apenas manual.
13. Registrar assertions que não poderiam passar na precondição atual.
14. Identificar assertions dependentes de implementação incidental.
15. Agrupar por contrato, não por arquivo.
16. Registrar lacunas sem inventar novas garantias.
17. Priorizar lacunas por impacto.
18. Reconciliar com os contratos das Partes III–V.

#### Ordem sugerida

Primeiro:

- V5/publicação.
- Auth.
- DTOs Buyer e público.
- Pricing.
- Header/navigation.
- Flow e teclado.
- CSS/tema.
- Assets.
- Localização.

#### DoD

Os contratos críticos possuem assertions identificadas e nenhuma garantia é considerada coberta somente pela presença do nome de um teste.

---

### TST-003 — Classificar redundâncias sem eliminar garantias

**Prioridade:** P1  
**Tipo:** otimização segura  
**Dependências:** TST-002

#### Objetivo

Distinguir custo duplicado de cobertura duplicada.

#### Procedimento

1. Listar comandos executados em mais de um workflow.
2. Identificar a frequência de reexecução.
3. Comparar suas entradas.
4. Comparar seus resultados.
5. Comparar seus ambientes.
6. Identificar diferenças de versão.
7. Comparar as assertions.
8. Classificar repetição exata de invocação.
9. Classificar repetição de precondição.
10. Classificar infraestrutura compartilhada.
11. Classificar overlap parcial.
12. Classificar assertions equivalentes.
13. Identificar garantia exclusiva.
14. Medir o custo real do conjunto.
15. Identificar possibilidade de compartilhamento de helper.
16. Identificar possibilidade de workflow reutilizável.
17. Verificar se status separados ainda são necessários.
18. Propor simplificação sem remover a prova.
19. Executar versão anterior e candidata no mesmo SHA.
20. Comparar conjuntos de assertions alcançáveis.
21. Integrar apenas quando houver preservação demonstrada.
22. Registrar a redução de custo observada, quando houver.

#### Exemplos de cautela

Não remover `test-v5-normal-save.js` porque outro teste de migração também verifica ETag.

Não remover `summary-pricing-browser.cjs` porque `test-core.js` verifica totais.

Não remover um teste visual de máscara porque um validador de metadados já passou.

#### DoD

Toda eliminação ou consolidação possui equivalência demonstrada e nenhuma assertion exclusiva desaparece silenciosamente.

---

### TST-004 — Auditar alcançabilidade dos workflows

**Prioridade:** P0  
**Tipo:** correção de CI  
**Dependências:** TST-001/002

#### Objetivo

Garantir que mudanças relevantes acionem as verificações necessárias.

#### Procedimento

1. Criar uma lista de arquivos por contrato.
2. Identificar os workflows que deveriam reagir a mudanças nesses arquivos.
3. Comparar filtros `pull_request`.
4. Comparar filtros `push`.
5. Comparar filtros `workflow_dispatch`.
6. Identificar branches históricas nos filtros.
7. Identificar filtros que não contemplam arquivos implementadores.
8. Identificar filtros que observam testes não executados.
9. Identificar comandos sem filtros relevantes.
10. Identificar casos de `paths-ignore`.
11. Construir cenários sintéticos de diff.
12. Simular seleção de workflow para cada cenário.
13. Confirmar que o job correspondente seria executado.
14. Confirmar que o comando correspondente contém a assertion.
15. Confirmar que condições internas não fazem skip indevido.
16. Registrar custo dos gatilhos amplos.
17. Propor filtros por família técnica.
18. Evitar criar status obrigatórios que ficam ausentes por filtros.
19. Testar a versão candidata do workflow.
20. Documentar a política de seleção.

#### Quatro discrepâncias prioritárias

1. `candidate-assets.yml`: filtros amplos de `tests/**`, mas checks específicos de stone/masks não são todos invocados.
2. `arc03c-static-page-build-gate.yml`: vinculado a branches históricas e observando arquivos que não correspondem integralmente aos comandos executados.
3. `public-routing-before-clerk.yml`: observa o arquivo `public-pages-integrated.cjs` pela expressão de paths, mas não o executa.
4. `viewer-base-price-contract-gate.yml`: sem trigger de PR na baseline consultada.

#### DoD

Cada contrato crítico possui pelo menos um caminho de execução real na integração relevante, com filtros e comandos coerentes.

---

### TST-005 — Determinar required checks e política de status

**Prioridade:** P0  
**Tipo:** governança de CI  
**Dependências:** TST-001/004

#### Objetivo

Eliminar a incerteza sobre quais checks são efetivamente obrigatórios para integrar.

#### Procedimento

1. Consultar regras aplicáveis à branch-alvo.
2. Verificar disponibilidade das regras via integração atual.
3. Não inferir ausência de regra a partir de HTTP 403.
4. Identificar workflows que publicam checks.
5. Identificar nomes de jobs relevantes.
6. Identificar jobs condicionais.
7. Identificar status que podem permanecer pendentes por `paths`.
8. Identificar jobs que só rodam em branches antigas.
9. Registrar regras confirmadas.
10. Registrar regras inacessíveis como `UNKNOWN`.
11. Propor uma política estável de required checks.
12. Garantir que todo check obrigatório tenha caminho de conclusão.
13. Evitar dependência de jobs que nunca rodam em determinadas PRs.
14. Validar essa política com permissão adequada quando disponível.
15. Não alterar proteção da branch sem autorização específica.
16. Registrar o resultado no anexo operacional.

#### DoD

O conjunto obrigatório é conhecido ou permanece explicitamente `UNKNOWN` com razão e ação de resolução. Nunca será presumido.

---

## 5. Marco TST-M1 — Fixtures, infraestrutura e isolamento

### TST-006 — Consolidar o servidor local Buyer V5

**Prioridade:** P0  
**Tipo:** infraestrutura comum  
**Dependências:** DOM-011, TST-001  
**Bundle:** BT-TST-10

#### Objetivo

Disponibilizar uma fixture local válida, previsível e reutilizável entre suites de navegador.

#### Estado atual

`tests/ci/local-buyer-config-server.mjs` já:

- Produz dados a partir dos defaults existentes.
- Usa o Core e a projeção Buyer.
- Serve uma resposta local.
- Responde como sessão anônima no endpoint simulado.
- Mantém o tráfego no loopback.
- Não grava Netlify Blobs nem banco real.

#### Procedimento

1. Identificar todos os workflows consumidores.
2. Definir o contrato de readiness.
3. Validar o payload antes de iniciar o browser.
4. Confirmar o schema Buyer esperado.
5. Confirmar a integridade do fluxo.
6. Confirmar os assets servidos.
7. Confirmar que a sessão reportada é sintética/anônima.
8. Confirmar ausência de cookies de autenticação reais.
9. Tornar a porta configurável.
10. Preferir porta efêmera em execuções independentes.
11. Manter compatibilidade com workflows que dependem da porta atual até migração.
12. Confirmar início e parada controlados.
13. Garantir encerramento após falha do teste.
14. Garantir encerramento após sucesso.
15. Verificar ausência de processos órfãos.
16. Verificar ausência de conflito entre duas execuções.
17. Identificar mensagens de log suficientes para diagnóstico.
18. Garantir que a fixture não faça chamadas a serviços privados.
19. Validar uma execução completa de navegador.
20. Migrar consumidores sem misturar mudanças funcionais.
21. Documentar seus limites de fidelidade.

#### Importante

O servidor é uma fixture de interface.

Ele não representa autenticação real nem publicação real de dados.

Aumentar sua fidelidade de renderização não deve implicar simular permissões inexistentes.

#### DoD

Todos os consumidores previstos utilizam uma fixture V5 validada, com readiness explícito e ciclo de vida controlado.

---

### TST-007 — Corrigir e integrar o browser de vidro/oclusão

**Prioridade:** P1  
**Tipo:** correção de teste  
**Dependências:** TST-006  
**Candidata:** PR #280  
**Bundle:** BT-TST-11

#### Objetivo

Transformar o teste atual em uma prova executável do Configurador.

#### Procedimento

1. Fixar o head da PR #280.
2. Conferir seus três arquivos alterados.
3. Confirmar que nenhum runtime foi modificado.
4. Confirmar a rota `/config/`.
5. Confirmar protocolo HTTP local.
6. Confirmar readiness do payload V5.
7. Confirmar readiness do DOM do Configurador.
8. Confirmar existência dos sete módulos esperados pelo teste.
9. Confirmar execução das 256 combinações previstas.
10. Confirmar seleção independente do vidro.
11. Confirmar o estado visual do serviço.
12. Confirmar a estrutura de layers.
13. Confirmar `z-index` do vidro versus foreground.
14. Confirmar o estado acessível esperado.
15. Confirmar quatro capturas.
16. Confirmar gravação de relatório.
17. Confirmar encerramento de navegador e servidor.
18. Executar em CI no SHA candidato.
19. Inspecionar artefatos e logs.
20. Investigar eventual falha como falha do teste ou do produto, conforme evidência.
21. Decidir se a execução será automática por paths ou manual.
22. Integrar a correção quando o bundle estiver satisfatório.
23. Revalidar na branch-alvo.
24. Atualizar a matriz ARC-15.

#### Limite

As 256 combinações verificam um conjunto definido de estados.

Não representam automaticamente prova de oclusão correta em toda geometria futura.

#### DoD

O teste realmente abre o Configurador, executa suas assertions e fornece relatório confiável no commit integrado.

---

### TST-008 — Isolar testes que alteram arquivos durante a execução

**Prioridade:** P1  
**Tipo:** higiene de testes  
**Dependências:** TST-001

#### Objetivo

Evitar concorrência entre testes e builds que trabalham na mesma árvore.

#### Procedimento

1. Inventariar testes que modificam arquivos.
2. Identificar se são arquivos versionados.
3. Identificar se modificam dados de fixture.
4. Identificar se modificam assets.
5. Identificar se dependem de diretórios temporários.
6. Identificar se possuem restauração em `finally`.
7. Identificar riscos de interrupção abrupta.
8. Identificar execuções paralelas possíveis.
9. Priorizar testes que alteram HTML ou manifesto.
10. Criar um ambiente temporário isolado para esses cenários.
11. Copiar somente os inputs necessários.
12. Executar o comando real nesse ambiente.
13. Confirmar resultado negativo esperado.
14. Confirmar ausência de modificação da árvore original.
15. Confirmar ausência de leftovers.
16. Medir custo da cópia.
17. Preservar o teste original como referência até equivalência.
18. Migrar somente após validação.
19. Integrar com rollback simples.

#### Candidato prioritário

`tests/arc03c-source-authority.test.mjs`

#### DoD

As provas negativas de drift continuam funcionando, sem exigir alteração temporária do checkout ativo.

---

## 6. Marco TST-M2 — Contratos críticos de domínio e segurança

### TST-009 — Fechar a cobertura de publicação V5

**Prioridade:** P0  
**Dependências:** DOM-003/004, TST-002  
**Bundle:** BT-TST-20

#### Objetivo

Conectar assertions de persistência e concorrência a riscos específicos.

#### Procedimento

1. Mapear leitura da configuração publicada.
2. Mapear validação V5.
3. Mapear revisão.
4. Mapear ETag.
5. Mapear CAS.
6. Mapear readback.
7. Mapear assinatura semântica.
8. Mapear códigos de erro.
9. Identificar testes puros.
10. Identificar testes de handler.
11. Identificar assertions apenas estáticas.
12. Confirmar cenários de sucesso.
13. Confirmar cenários de rejeição.
14. Confirmar ausência de gravação quando inválido.
15. Confirmar proteção contra downgrade.
16. Confirmar que migração aposentada retorna erro.
17. Comparar mocks utilizados.
18. Verificar se algum mock aceita sucesso que o provider real rejeitaria.
19. Registrar limite das simulações.
20. Corrigir gaps com assertions comportamentais.
21. Não remover testes históricos exclusivos.
22. Verificar alcançabilidade em PRs de endpoint.
23. Integrar o pacote de testes.
24. Registrar status por contrato.

#### Lacuna específica

Uma modificação isolada em `netlify/functions/configuration.mjs` não é abrangida pelo filtro de PR do workflow `app-build-purity.yml`.

A cobertura de endpoint não deve depender de uma alteração acidental em `app/**` para disparar.

#### DoD

Mudanças relevantes na publicação acionam testes de sucesso e falha, com proof de não escrita nos casos proibidos.

---

### TST-010 — Fechar cobertura de autorização e sessão

**Prioridade:** P0  
**Dependências:** DOM-013  
**Bundle:** BT-TST-21

#### Objetivo

Verificar a cadeia completa de autorização sem confundir UI e backend.

#### Procedimento

1. Identificar as políticas de acesso.
2. Identificar endpoints protegidos.
3. Mapear cada papel previsto.
4. Mapear sessão temporária.
5. Testar usuário anônimo.
6. Testar usuário autorizado.
7. Testar usuário não autorizado.
8. Testar sessão expirada.
9. Testar falha de Identity.
10. Testar falha do armazenamento de sessões.
11. Verificar acesso à configuração administrativa.
12. Verificar acesso ao Buyer DTO.
13. Confirmar que endpoints não consultam dados protegidos antes da autorização.
14. Verificar respostas 401/403 quando pertinentes.
15. Verificar que o menu privado representa o estado retornado.
16. Simular resposta atrasada de sessão.
17. Testar logout.
18. Verificar ausência de dados protegidos em logs.
19. Verificar ausência de tokens em screenshots.
20. Separar mocks de sessão real.
21. Registrar casos que exigem ambiente hospedado autorizado.
22. Integrar testes e correções.
23. Atualizar evidências.

#### DoD

Política de acesso protegida por assertions comportamentais e fronteiras entre fixture local e sessão real documentadas.

---

### TST-011 — Fechar cobertura da projeção pública e preços

**Prioridade:** P0  
**Dependências:** DOM-010/012  
**Bundle:** BT-TST-22

#### Objetivo

Provar a autorização de preço público em todas as camadas necessárias.

#### Procedimento

1. Identificar projeção 0.1.
2. Identificar projeção 0.2.
3. Confirmar campo OFF por ausência.
4. Confirmar OFF explícito.
5. Confirmar ON persistido.
6. Confirmar que versão solicitada não concede permissão.
7. Testar valor base positivo válido.
8. Testar preço zero.
9. Testar preço ausente.
10. Testar preço de tipo inválido.
11. Testar módulo oculto.
12. Testar módulo fora da composição publicada.
13. Confirmar ausência de regras completas.
14. Confirmar ausência de margens e dados administrativos.
15. Testar down-projection para 0.1.
16. Testar falha do endpoint.
17. Verificar resposta e cabeçalhos.
18. Testar Viewer com OFF.
19. Testar Viewer com ON.
20. Verificar alinhamento com dimensões.
21. Verificar atualização ao selecionar módulo.
22. Testar revogação.
23. Confirmar que o Preview não está mascarando resultados com DTO 0.1 da origem principal.
24. Registrar o que é prova local e o que necessita publicação autorizada.
25. Integrar e revalidar.

#### DoD

Publicação de preços protegida por testes de allowlist, autorização, compatibilidade e apresentação, sem depender de uma única camada de teste.

---

## 7. Marco TST-M3 — Interação, acessibilidade e apresentação

### TST-012 — Consolidar o bundle de navegação pública

**Prioridade:** P1  
**Dependências:** CMP-002…005  
**Bundle:** BT-TST-30

#### Objetivo

Preservar as variantes NAV-005 com provas proporcionais ao contexto.

#### Procedimento

1. Distinguir header primário de secundário.
2. Identificar os três consumidores do fragmento.
3. Identificar o header do Viewer.
4. Identificar o controlador compartilhado.
5. Testar menu fechado/aberto.
6. Testar `aria-expanded`.
7. Testar `aria-current`.
8. Testar Escape.
9. Testar clique fora.
10. Testar ativação por teclado.
11. Testar foco e retorno.
12. Testar reflow.
13. Testar zoom.
14. Testar ordem Ambientes/tema/menu no Viewer.
15. Confirmar marca e CTA.
16. Testar claro/escuro.
17. Testar larguras de risco: inclusive 290/291 px quando afetadas.
18. Testar Chromium e WebKit no conjunto de integração relevante.
19. Comparar baseline e candidata.
20. Confirmar ausência de efeito na navegação privada.
21. Integrar com recibo por rota.

#### DoD

Contratos NAV por profundidade validados e teste de menu acionado quando seus arquivos implementadores mudam.

---

### TST-013 — Consolidar teclado e foco do Configurador

**Prioridade:** P1  
**Dependências:** DOM-006/007, TST-006  
**Bundle:** BT-TST-31

#### Objetivo

Verificar navegação real de teclado no contexto de configuração V5.

#### Procedimento

1. Inicializar fixture Buyer válida.
2. Confirmar carregamento da configuração.
3. Confirmar que os controles esperados existem.
4. Confirmar que o primeiro checkbox está habilitado.
5. Confirmar foco inicial antes da tecla Tab.
6. Executar Tab.
7. Verificar o destino esperado.
8. Executar Shift+Tab.
9. Testar seleção de módulo.
10. Testar atalhos aplicáveis.
11. Testar Escape em painéis.
12. Testar restauração de foco.
13. Testar mudança de etapa.
14. Testar reordenação de elementos quando aplicável.
15. Testar foco após mudança responsiva.
16. Verificar controles desabilitados.
17. Verificar regiões de feedback.
18. Capturar o elemento ativo em falhas.
19. Registrar DOM, viewport e estado inicial em caso de divergência.
20. Reexecutar o mesmo SHA para diagnosticar intermitência sem modificar a assertion.
21. Determinar se a falha é produto, fixture ou teste.
22. Integrar correções específicas.

#### Caso histórico relevante

O gate de teclado associado à PR #269 apresentou uma falha isolada que desapareceu em rerun do mesmo SHA.

A revisão posterior acrescentou diagnóstico de precondição, preservando a expectativa original.

Esse é o caminho correto.

O caminho incorreto seria relaxar a assertion até que ela deixe de detectar a regressão.

#### DoD

A navegação é testada sobre estado inicial válido, com falha reproduzível ou diagnóstico suficiente para classificar intermitência.

---

### TST-014 — Consolidar os testes de layout responsivo e PiP

**Prioridade:** P1  
**Dependências:** CMP-015, DOM-007  
**Bundle:** BT-TST-32

#### Objetivo

Preservar comportamento entre perfis de layout sem executar combinações excessivas.

#### Procedimento

1. Identificar breakpoints declarados.
2. Identificar mudanças de perfil.
3. Identificar componentes deslocados.
4. Identificar dock.
5. Identificar mini-cena/PiP.
6. Definir larguras imediatamente antes/depois de cada breakpoint crítico.
7. Verificar 700/701 px quando afetar navegação dinâmica.
8. Verificar 1050/1051 px quando afetar o perfil.
9. Verificar largura mobile representativa.
10. Verificar largura desktop representativa.
11. Testar mudança de etapa.
12. Testar seleção.
13. Testar pin/unpin.
14. Testar rolagem.
15. Testar resize com componente aberto.
16. Confirmar ausência de controles fora do viewport.
17. Verificar sobreposição indevida.
18. Testar foco após reorganização.
19. Testar reduced motion quando relevante.
20. Comparar geometria com baseline.
21. Registrar diferenças intencionais.
22. Integrar testes e correções.

#### Estratégia de matriz

Não executar todas as combinações de:

`rota × largura × tema × navegador × estado × interação`

em todos os commits.

Executar primeiro os estados alterados e suas fronteiras.

Executar uma matriz transversal maior nos marcos de integração.

#### DoD

Breakpoints relevantes e interações de risco possuem cobertura, sem transformar a matriz combinatória inteira em requisito universal.

---

### TST-015 — Fortalecer os testes do tema

**Prioridade:** P1  
**Dependências:** CMP-007, TOK-002  
**Bundle:** BT-TST-33

#### Objetivo

Transformar `ui-theme-contract.cjs` em um contrato confiável e efetivamente executado.

#### Procedimento

1. Identificar assertions puramente semânticas.
2. Identificar assertions de texto-fonte.
3. Identificar assertions de query string.
4. Confirmar como cada página carrega o script.
5. Confirmar como cada página carrega o CSS.
6. Determinar se as versões de URL precisam ser idênticas.
7. Remover apenas a exigência não normativa, se comprovadamente incidental.
8. Preservar teste de ordem de inicialização.
9. Testar modo automático.
10. Testar modo claro.
11. Testar modo escuro.
12. Testar persistência.
13. Testar alteração da preferência do sistema.
14. Testar troca de logo.
15. Testar foco e controle.
16. Testar ausência de duplicação de controles.
17. Testar posição do controle por shell.
18. Medir tamanho real do alvo de toque no navegador.
19. Identificar assertions de Landing/Viewer que pertencem a outros bundles.
20. Não mover essas assertions sem substituto.
21. Integrar a chamada ao workflow adequado.
22. Executar no head exato.

#### DoD

O teste valida o comportamento do tema e sua integração real, com assertions proporcionais ao contrato e sem dependências textuais injustificadas.

---

### TST-016 — Consolidar contraste e CSSOM por contexto

**Prioridade:** P0/P1  
**Dependências:** Parte III e G2  
**Bundle:** BT-TST-34

#### Objetivo

Eliminar ambiguidade entre contraste calculado, contraste observado e contraste ainda não verificável.

#### Procedimento

1. Definir os pares de texto/fundo.
2. Identificar a propriedade efetiva no navegador.
3. Identificar a folha que venceu a cascata.
4. Identificar o token consumido, quando aplicável.
5. Identificar a cor de fundo composta.
6. Identificar overlays e transparência.
7. Identificar `backdrop-filter`.
8. Classificar o par como mensurável ou incerto.
9. Não converter `UNCERTAIN` em falha confirmada.
10. Executar medição em contexto válido.
11. Separar claro e escuro.
12. Separar estados de hover, foco e seleção relevantes.
13. Confirmar tamanho e peso do texto.
14. Identificar requisito de contraste correspondente.
15. Comparar candidato com baseline.
16. Registrar pares que pioraram.
17. Registrar pares que melhoraram.
18. Confirmar a decisão VIS autorizadora.
19. Verificar se o token está realmente integrado.
20. Verificar qual CSS foi servido e aplicado.
21. Validar no ambiente hospedado quando indispensável.
22. Registrar bloqueios locais sem paralisar CSS independente.
23. Integrar resultados no crosswalk G2/G3.

#### Caso concreto

Os 98 pares classificados como `UNCERTAIN` não representam 98 falhas demonstradas.

A necessidade é obter evidência adicional, especialmente nos contextos com composição de fundo complexa.

#### DoD

Pares do escopo possuem classificação sustentada por CSSOM/runtime ou incerteza explicitamente registrada; alterações aprovadas não causam regressões nos consumidores afetados.

---

## 8. Marco TST-M4 — Assets, geometria e evidência visual

### TST-017 — Separar provas geométricas de provas visuais

**Prioridade:** P1  
**Dependências:** CMP-008, TST-002  
**Bundle:** BT-TST-40

#### Objetivo

Evitar que um teste de posicionamento compare o layout apenas com valores copiados do próprio layout.

#### Caso relevante

O gate de geometria do telefone da Home verificava a correspondência entre DOM e coordenadas declaradas.

A PR [#278](https://github.com/EAKerber/MobiliPresenter2D/pull/278) acrescenta uma medida independente da abertura escura da arte rasterizada.

Isso fortalece o teste porque a referência passa a vir também do asset real.

#### Procedimento

1. Identificar o asset homologado.
2. Identificar seu hash.
3. Identificar seu espaço geométrico.
4. Identificar transformações SVG ou de escala.
5. Identificar coordenadas usadas pelo layout.
6. Identificar o objeto físico representado.
7. Medir pixels independentes da declaração DOM.
8. Comparar a medida com a geometria declarada.
9. Definir tolerância para antialiasing.
10. Testar larguras representativas.
11. Confirmar que o vídeo ocupa a região esperada.
12. Confirmar o recuo do player.
13. Confirmar o poster.
14. Confirmar que o crop permanece correto.
15. Verificar controles sobrepostos.
16. Testar a entrada em fullscreen.
17. Testar a saída pelo controle.
18. Testar Escape.
19. Confirmar `aria-label`, `title` e estado.
20. Separar testes de DOM e vídeo real externo.
21. Evitar que uma falha de rede do YouTube seja tratada automaticamente como erro geométrico.
22. Comparar as duas páginas que possuem controle próprio de fullscreen.
23. Integrar o incremento de teste.
24. Registrar limites de validação externa.

#### DoD

Geometria é ancorada a evidência independente do DOM; interação de fullscreen possui teste próprio ou pendência explicitamente documentada.

---

### TST-018 — Preservar contratos de assets atuais e replays históricos

**Prioridade:** P1  
**Dependências:** TST-003/004  
**Bundle:** BT-TST-41

#### Objetivo

Reduzir custo de validação de assets sem destruir sua proveniência.

#### Distinção necessária

**Validação atual:** comprova que a versão vigente dos assets é válida.

**Replay histórico:** comprova como uma versão específica foi produzida.

Essas verificações não devem compartilhar automaticamente a mesma autoridade.

#### Procedimento

1. Inventariar validadores de assets.
2. Identificar quais pertencem ao produto atual.
3. Identificar quais reproduzem checkpoints históricos.
4. Identificar hashes imutáveis de origem.
5. Identificar manifests de reconstrução.
6. Identificar máscaras e composições atuais.
7. Identificar candidatos ainda não homologados.
8. Identificar status `semanticReview=PENDING`.
9. Identificar status `REVIEW`.
10. Verificar quais testes são leves.
11. Verificar quais reexecutam geração de assets.
12. Classificar testes por paths.
13. Criar proposta de invocação específica para máscaras leves.
14. Criar proposta de invocação específica para pixels.
15. Criar proposta de replay stone técnico.
16. Manter replays históricos explícitos.
17. Não atualizar hashes históricos apenas para tornar CI verde.
18. Não promover status técnico a aprovação visual.
19. Confirmar build atual sem rematerialização antiga.
20. Confirmar ausência de alteração inesperada de bytes.
21. Verificar que o artefato final corresponde à fonte atual.
22. Integrar apenas os gates aprovados.
23. Registrar custo e benefício.

#### Arquivos a classificar

- `tests/test_mask_semantics.py`
- `tests/test_stone_backing.py`
- `tests/test_stone_cleanplate.py`
- `tests/test_stone_surface_masks.py`
- `tests/validate-exposed-side-pixels.py`

#### DoD

Assets atuais continuam protegidos; replays históricos permanecem reproduzíveis e nenhuma aprovação semântica é inferida de checks técnicos.

---

### TST-019 — Estabelecer política de screenshots e referências visuais

**Prioridade:** P1  
**Dependências:** TST-015…018  
**Bundle:** BT-TST-42

#### Objetivo

Fazer com que screenshots sejam evidências úteis, e não apenas arquivos acumulados.

#### Procedimento

1. Definir o contrato que a imagem pretende observar.
2. Fixar rota.
3. Fixar viewport.
4. Fixar tema.
5. Fixar estado da interface.
6. Fixar dados/fixture.
7. Fixar navegador ou engine.
8. Fixar preferência de movimento.
9. Esperar fontes carregadas.
10. Esperar imagens relevantes decodificadas.
11. Esperar conclusão de transições controladas.
12. Impedir overlays não relacionados.
13. Capturar baseline.
14. Capturar candidata.
15. Comparar diferenças.
16. Separar alterações intencionais de regressões.
17. Identificar elementos com diferença geométrica.
18. Identificar elementos com diferença de cor.
19. Identificar diferenças de texto.
20. Confirmar que o screenshot não inclui dados pessoais.
21. Guardar metadados da captura.
22. Definir retenção proporcional ao valor.
23. Não promover screenshot a prova de interação ou autorização.
24. Anexar parecer de homologação quando necessário.

#### Regra para golden images

Uma referência visual aprovada deve permanecer estável até haver uma mudança intencional e homologada.

Atualizar automaticamente a referência no mesmo commit que altera a interface pode mascarar regressões.

#### DoD

Capturas possuem contexto reproduzível, referência apropriada e interpretação vinculada ao contrato avaliado.

---

## 9. Marco TST-M5 — Localização, estados e acessibilidade

### TST-020 — Verificar cobertura de localização por consumidor

**Prioridade:** P1  
**Dependências:** LOC-003…008  
**Bundle:** BT-TST-50

#### Objetivo

Garantir que a migração para o catálogo `pt-BR` não produza texto incorreto nem elimine nomes acessíveis.

#### Procedimento

1. Identificar o conjunto de chaves migradas.
2. Identificar consumidores do conjunto.
3. Verificar presença das chaves.
4. Verificar valores.
5. Verificar parâmetros.
6. Verificar pluralização quando aplicável.
7. Verificar fallback.
8. Verificar atributos acessíveis.
9. Verificar texto em estados alternativos.
10. Verificar regiões vivas.
11. Verificar conteúdo editorial preservado.
12. Verificar dados V5 não extraídos.
13. Verificar textos técnicos excluídos.
14. Comparar HTML gerado.
15. Comparar DOM dinâmico.
16. Identificar chaves órfãs.
17. Identificar texto literal remanescente no escopo migrado.
18. Confirmar correspondência entre inventário ARC-13 e consumidores.
19. Testar caracteres especiais.
20. Confirmar inserção segura em DOM.
21. Testar comprimento de texto onde influencia layout.
22. Integrar o gate com triggers corretos.
23. Registrar cobertura e exceções.

#### DoD

Texto localizável migrado e seus estados ficam cobertos por verificações de catálogo, DOM e acessibilidade.

---

### TST-021 — Cobrir interações acessíveis não verificadas

**Prioridade:** P1/P2  
**Dependências:** TST-012…016 e TST-020  
**Bundle:** BT-TST-51

#### Objetivo

Fechar lacunas onde o DOM parece correto, mas o comportamento assistivo ainda não foi demonstrado.

#### Prioridades iniciais

- Nome acessível de controles de vídeo.
- Fullscreen.
- Expansão de detalhes.
- Hotspots de cena.
- Seleção de módulo.
- Feedback de publicação.
- Mensagens de erro e status.
- Controle de tema.
- Navegação privada.
- Controles desabilitados do Admin.

#### Procedimento

1. Identificar o elemento.
2. Identificar seu papel semântico.
3. Identificar nome acessível.
4. Identificar estado acessível.
5. Identificar contexto de navegação.
6. Verificar se a árvore acessível expõe o nome.
7. Testar ativação por teclado.
8. Testar alteração de estado.
9. Testar sincronização do nome.
10. Testar retorno de foco.
11. Testar anúncio de erro.
12. Testar anúncio de sucesso.
13. Testar comportamento em estado disabled.
14. Identificar casos que exigem revisão assistiva real.
15. Executar a revisão correspondente.
16. Registrar ambiente e resultado.
17. Corrigir sem alterar contratos não relacionados.
18. Integrar a mudança e revalidar.

#### DoD

Os estados acessíveis prioritários estão comprovados; revisão estática não é apresentada como prova assistiva quando esta for necessária.

---

## 10. Marco TST-M6 — Otimização efetiva da CI

### TST-022 — Criar seleção de bundles por impacto

**Prioridade:** P0/P1  
**Dependências:** TST-002/004  
**Bundle:** BT-TST-60

#### Objetivo

Executar o conjunto necessário de testes com o menor custo compatível com o risco.

#### Modelo

```text
Mudança de arquivos
        │
        ▼
Mapeamento de contratos afetados
        │
        ▼
Consumidores e riscos transitivos
        │
        ▼
Bundles obrigatórios do pacote
        │
        ▼
Testes rápidos e determinísticos
        │
        ▼
Testes browser correspondentes
        │
        ▼
Gate ampliado no marco de integração
```

#### Procedimento

1. Classificar paths de origem.
2. Associar paths a contratos.
3. Associar contratos a consumers.
4. Associar consumers a riscos.
5. Associar riscos a assertions.
6. Identificar dependências transitivas.
7. Identificar risco de alteração de build.
8. Identificar risco de alteração de schema.
9. Identificar risco de alteração de auth.
10. Identificar risco de alteração de CSS global.
11. Selecionar bundles rápidos.
12. Selecionar browsers apenas quando necessários.
13. Incluir controles negativos para consumidores transversais.
14. Incluir gates de segurança quando contrato protegido for afetado.
15. Evitar usar somente o nome da branch para selecionar testes.
16. Verificar alterações em arquivos de fixture.
17. Verificar alterações em scripts de build.
18. Verificar alterações em workflows.
19. Validar a seleção contra casos históricos.
20. Confirmar que nenhum contrato crítico fica descoberto.
21. Implementar a regra de forma inspecionável.
22. Manter fallback conservador para mudanças não classificadas.
23. Integrar e medir o comportamento.

#### Exemplo

Mudança em:

`app/landing/header-menu.js`

Selecionar:

- Contrato de menu público.
- ARC-03C, se a fonte/estrutura do header também for alterada.
- Teste de foco e teclado.
- Teste responsivo do header.
- Viewer secundário, como consumidor do controlador.

Não selecionar automaticamente:

- Testes de preço tipado.
- Save V5.
- Replays históricos de pedra.
- Autorização administrativa completa.

Isso pode reduzir trabalho sem reduzir cobertura pertinente.

#### DoD

A seleção de testes é explicável, cobre dependências reais e possui fallback seguro para mudanças desconhecidas.

---

### TST-023 — Consolidar infraestrutura de CI compartilhável

**Prioridade:** P1  
**Dependências:** TST-003, TST-006, TST-022  
**Bundle:** BT-TST-61

#### Objetivo

Reduzir instalações, preparação, duplicação de código e execução repetida sem apagar status ou garantias.

#### Procedimento

1. Medir duração atual dos jobs.
2. Medir tempo de instalação de dependências.
3. Medir duração do build.
4. Medir duração da suíte pura.
5. Medir duração dos browsers.
6. Identificar instalações repetidas.
7. Identificar builds repetidos.
8. Identificar servidores de fixture repetidos.
9. Identificar uso de cache que realmente reduz trabalho.
10. Identificar oportunidades de job reutilizável.
11. Separar definição de job e status de integração.
12. Confirmar que o workflow reutilizável recebe SHA correto.
13. Confirmar que cada PR produz seu próprio status.
14. Preservar checks esperados.
15. Evitar compartilhar diretórios mutáveis entre jobs conflitantes.
16. Evitar paralelizar sobre a mesma árvore de trabalho.
17. Testar execução isolada.
18. Testar execução em PR.
19. Comparar resultados do conjunto anterior e novo.
20. Medir redução real de tempo.
21. Registrar custo adicional de manutenção.
22. Descartar otimizações cujo ganho não compense a complexidade.

#### Exemplos candidatos

- Preparação comum de V5.
- Instalação comum de Playwright.
- Helper de servidor loopback.
- Invocação repetida de `public-cutover-contract.cjs`.
- Parte da execução compartilhada de `npm test`.

#### DoD

Infraestrutura comum reduz custo demonstravelmente, sem perda de assertions ou status necessários.

---

### TST-024 — Diagnosticar e tratar intermitência

**Prioridade:** P1  
**Dependências:** TST-002  
**Bundle:** BT-TST-62

#### Objetivo

Evitar que falhas instáveis consumam sucessivos turnos de investigação e levem a mudanças desnecessárias no produto.

#### Protocolo de triagem

1. Registrar SHA exato.
2. Registrar workflow e run.
3. Registrar job e etapa.
4. Registrar fixture.
5. Registrar navegador.
6. Registrar viewport.
7. Registrar estado inicial.
8. Registrar assertion que falhou.
9. Capturar resultado real.
10. Capturar logs relevantes.
11. Capturar screenshot ou DOM quando pertinente.
12. Verificar mudança de runtime relacionada.
13. Verificar mudança de teste relacionada.
14. Verificar mudança de infraestrutura.
15. Reexecutar o mesmo SHA.
16. Comparar resultados.
17. Identificar corrida assíncrona.
18. Identificar falta de readiness.
19. Identificar foco inicial inadequado.
20. Identificar dependência de tempo fixo.
21. Identificar rede externa instável.
22. Classificar causa provável.
23. Corrigir fixture ou teste quando apropriado.
24. Corrigir produto quando demonstrada regressão.
25. Preservar a assertion de negócio.
26. Registrar resolução e prova.

#### Classificações finais

- `product_regression`
- `test_bug`
- `fixture_failure`
- `environment_failure`
- `external_dependency`
- `intermittent_unresolved`

Essas categorias não são estados de backlog, mas diagnósticos opcionais da falha.

#### DoD

Falhas recorrentes possuem diagnóstico e ação definidos; rerun verde não apaga uma causa ainda desconhecida.

---

## 11. Marco TST-M7 — Publicação, readback e DoD operacional

### TST-025 — Formalizar os gates de integração e publicação

**Prioridade:** P0  
**Dependências:** TST-005, TST-009…024  
**Bundle:** BT-TST-70

#### Objetivo

Distinguir claramente aprovação de PR, integração na branch e verificação da versão publicada.

#### Procedimento

1. Identificar a branch-alvo.
2. Identificar o head candidato.
3. Identificar a base da PR.
4. Identificar o merge commit sintético quando aplicável.
5. Registrar tests executados.
6. Registrar tests não executados.
7. Registrar motivo de skip.
8. Confirmar contratos críticos.
9. Confirmar diferenças intencionais.
10. Confirmar ausência de alterações não relacionadas.
11. Integrar somente após critérios relevantes.
12. Registrar SHA integrado.
13. Revalidar gates de integração afetados.
14. Identificar versão de build.
15. Identificar artefato publicado.
16. Verificar caminho real de publicação.
17. Conferir que os assets esperados são carregados.
18. Conferir que CSS/JS esperados são utilizados.
19. Verificar contratos de rota.
20. Executar smoke read-only quando apropriado.
21. Não usar produção como fixture.
22. Não publicar preço ou alterar banco para validar uma refatoração visual.
23. Registrar resultados e limites.
24. Encerrar apenas os critérios comprovados.

#### Política de Deploy Preview

A preferência é:

1. Validação estática/local.
2. Suíte pura.
3. Browser local.
4. CI do head.
5. Deploy Preview, quando acrescentar evidência necessária.
6. Readback de produção após integração/publicação autorizadas.

O Preview não deve ser um requisito automático para qualquer alteração de texto, CSS ou teste.

Da mesma forma, evitar Preview não deve impedir uma validação hospedada indispensável.

#### DoD

Integração e publicação são registradas como fatos distintos, com SHA, ambiente e evidência próprios.

---

### TST-026 — Implantar recibo mínimo por pacote

**Prioridade:** P0  
**Tipo:** método/DoD  
**Dependências:** TST-001/002/025  
**Bundle:** BT-TST-71

#### Objetivo

Transformar resultados de CI em reporting operacional simples.

#### Estrutura sugerida

```text
Package: CMP-004
Target: main
Candidate: <sha>
Integrated: <sha-or-none>

Contracts:
  - NAV-005 public-primary
  - ARC-03C source authority

Checks:
  - pages:check: PASS
  - keyboard/header: PASS
  - browser differential: PASS
  - hosted visual: PENDING

Negative controls:
  - Viewer unchanged: PASS
  - Private header unchanged: PASS

DoD:
  - result: PARTIAL
  - status: in_review
  - notes: hosted visual pending
```

Esse é um exemplo de formato, não um recibo real.

#### Procedimento

1. Identificar ID do backlog.
2. Registrar estado anterior.
3. Registrar escopo do pacote.
4. Registrar commits.
5. Registrar branch-alvo.
6. Registrar contratos afetados.
7. Registrar tests selecionados.
8. Registrar resultado de cada teste.
9. Registrar evidência visual quando necessária.
10. Registrar controles negativos.
11. Registrar limitações da fixture.
12. Registrar se houve integração.
13. Registrar se houve publicação.
14. Registrar pendências restantes.
15. Calcular DoD a partir dos critérios aplicáveis.
16. Atualizar status.
17. Acrescentar transição à timeline.
18. Comunicar o resumo ao usuário.

#### Regra importante

O recibo não deve exigir copiar todos os logs do CI.

Deve apontar para eles.

A informação indispensável é:

**qual contrato, em qual versão, sob qual condição, com qual resultado.**

#### DoD

Um pacote pode ser compreendido e retomado sem reler toda a narrativa do turno anterior.

---

## 12. Bundles consolidados de execução

Os bundles das Partes III–V descrevem quais testes cada componente deve receber.

Os bundles abaixo organizam a infraestrutura que executará essas verificações.

| Bundle | Escopo | Evidência mínima |
|---|---|---|
| BT-TST-00 | Inventário, assertions e triggers | E0 |
| BT-TST-10 | Fixture Buyer V5 | E1/E2 |
| BT-TST-11 | Vidro/oclusão | E1/E3 |
| BT-TST-20 | Save V5, CAS e readback | E1/E2 |
| BT-TST-21 | Auth e sessão | E1/E2; E5 quando necessário |
| BT-TST-22 | Preço público e Viewer | E1/E2/E3 |
| BT-TST-30 | Menu e navegação pública | E0/E3 |
| BT-TST-31 | Keyboard Configurador | E3 |
| BT-TST-32 | Layout/PiP | E3 |
| BT-TST-33 | Tema e marca | E1/E3 |
| BT-TST-34 | CSSOM e contraste | E3; E4 quando necessário |
| BT-TST-40 | Geometria e fullscreen | E3 |
| BT-TST-41 | Assets e replays | E1/E2 |
| BT-TST-42 | Visual differential | E3/E4 |
| BT-TST-50 | Localização | E0/E1/E3 |
| BT-TST-51 | Acessibilidade | E3 e revisão assistiva conforme risco |
| BT-TST-60 | Seleção por impacto | E0/E2 |
| BT-TST-61 | Infraestrutura compartilhada | E2 |
| BT-TST-62 | Diagnóstico de falhas | Evidência do run |
| BT-TST-70 | Integração/publicação | E2–E6 conforme contrato |
| BT-TST-71 | DoD/reporting | Recibo verificável |

### 12.1 Bundles devem ter composição explícita

Um bundle não é apenas um nome para executar `npm test` sempre.

Ele deverá apontar para comandos existentes ou para uma composição pequena de verificações.

Exemplo:

```text
BT-TST-22 — Preços públicos

1. Projeção pura
2. Teste negativo de allowlist
3. Contrato de save V5
4. Handler público simulado
5. Browser Viewer ON/OFF
6. Readback hospedado se exigido
```

Isso permite ajustar a implementação do bundle sem redefinir o DoD do componente.

---

## 13. Política de execução por tipo de alteração

A escolha dos testes deve ser feita por risco e impacto.

A matriz abaixo representa uma configuração inicial, sujeita a medição e ajuste.

| Alteração | Testes normalmente necessários |
|---|---|
| Token de cor isolado | Validação de fonte/token, CSSOM e consumidores afetados |
| CSS de componente | DOM/CSSOM, foco, estado e screenshot do componente |
| Header público | ARC-03C, menu, teclado e responsividade |
| Header Viewer | NAV-005 secundário, tema e links |
| Controlador de tema | Contrato de tema, marca e slots por shell |
| Fluxo do Configurador | Modelo, layout, Buyer V5, teclado |
| Controle de preço | Pricing, projeção, endpoint, browser |
| Salvar V5 | Validação, CAS, readback, endpoint |
| Auth | Política de acesso, endpoint, sessão e UI privada |
| Asset de máscara | Proveniência, geometria, pixels e consumer |
| Composição editorial | HTML, links, interação local e visual |
| Catálogo de localização | Chaves, interpolação, DOM e acessibilidade |
| Script de build | Determinismo, integridade de saída e teste negativo |
| Workflow de CI | Alcançabilidade, comandos, status e smoke de execução |

### 13.1 Controles negativos

Cada conjunto deve identificar aquilo que **não pode mudar**.

Exemplos:

**Mudança no menu público:** não alterar permissões privadas.

**Mudança no Viewer:** não alterar preço calculado no Configurador.

**Mudança em swatches:** não alterar seleção ou disponibilidade de materiais.

**Mudança no catálogo `pt-BR`:** não alterar IDs nem conteúdo comercial V5.

**Mudança em assets:** não reintroduzir arte histórica no build atual.

**Mudança em CSS global:** não modificar consumidores não homologados.

Esses controles negativos reduzem a necessidade de executar suites amplas apenas por medo de efeitos colaterais desconhecidos.

---

## 14. Precondições obrigatórias dos testes de navegador

Cada teste browser deverá declarar suas precondições de forma verificável.

### 14.1 Precondições de ambiente

- Origem HTTP válida.
- Rota correta.
- Browser instalado.
- Arquivos servidos.
- Versão da aplicação identificável.
- Nenhuma chamada externa desnecessária.
- Readiness confirmada.

### 14.2 Precondições de dados

- Schema válido.
- Entidades esperadas presentes.
- Estado inicial correto.
- Opções exigidas disponíveis.
- Compatibilidade com o consumer.
- Nenhum dado privado usado como fixture.
- Ausência de fallback silencioso.

### 14.3 Precondições visuais

- Viewport definido.
- Tema definido.
- Fontes carregadas.
- Imagens decodificadas quando necessário.
- Animação estabilizada.
- `prefers-reduced-motion` conhecido.
- Elemento alvo presente.
- Nenhum overlay inesperado.

### 14.4 Precondições de interação

- Elemento visível.
- Elemento habilitado.
- Foco inicial conhecido.
- Nenhuma operação anterior incompleta.
- Nenhum listener duplicado.
- Sessão no estado esperado.

Quando uma precondição falhar, a mensagem deve indicar:

**A fixture não atingiu o estado necessário para verificar o contrato.**

Ela não deve relatar automaticamente uma regressão na funcionalidade que ainda nem foi exercitada.

---

## 15. Tratamento das quatro decisões ARC-15

O inventário existente pede quatro disposições específicas.

Minha recomendação é a seguinte.

### 15.1 Teste de tema

**Decisão proposta:** corrigir assertions excessivamente estruturais e integrar o contrato central ao CI com triggers por arquivos de tema, headers e marca.

Não exigir uma query string idêntica em todos os shells sem contrato explícito que justifique isso.

### 15.2 Browser glass

**Decisão proposta:** avançar com a correção da PR #280, executar primeiro com fixture validada e então decidir sua inclusão como gate path-specific.

A prioridade é torná-lo uma prova confiável antes de automatizar sua invocação ampla.

### 15.3 Checks leves de máscara e pixels

**Decisão proposta:** automatizar em jobs/condições de paths específicos, porque fornecem garantias úteis e relativamente diretas.

Não inseri-los indiscriminadamente em todo `candidate-assets.yml` acionado por alterações genéricas em `tests/**`.

### 15.4 Replays históricos de stone

**Decisão proposta:** manter replay manual por padrão, com acionamento automático apenas se uma mudança realmente afetar a cadeia de geração correspondente e a execução for tecnicamente justificável.

Os estados `semanticReview=PENDING` e `status=REVIEW` devem permanecer independentes do sucesso técnico.

Isso não remove nenhum arquivo.

Apenas separa o que protege o produto atual do que preserva evidência histórica.

---

## 16. Métricas de eficiência

A melhoria da CI precisa ser avaliada pelos resultados.

Não definiremos metas numéricas arbitrárias antes de medir o comportamento atual.

### 16.1 Indicadores recomendados

| Indicador | O que mede |
|---|---|
| Tempo até primeiro feedback | Velocidade da primeira falha útil |
| Tempo até gate suficiente | Latência para considerar o pacote revisável |
| Tempo de CI por PR | Custo total de execução |
| Testes selecionados corretamente | Alcançabilidade dos contratos afetados |
| Flakiness por gate | Reexecuções inconsistentes no mesmo SHA |
| Falhas de precondição | Problemas de fixture versus produto |
| Defeitos escapados | Regressões que passaram pelos gates |
| Coverage por contrato | Garantias exercitadas, não linhas de código |
| Testes sem invocação | Código de teste sem caminho operacional |
| Tempo de investigação | Custo de explicar falhas |
| Previews utilizados | Custo de validação hospedada |
| Contratos com DoD auditável | Capacidade de encerrar trabalho sem ambiguidade |

### 16.2 Não otimizar métricas isoladamente

Reduzir tempo de CI sacrificando assertions críticas é um resultado ruim.

Aumentar coverage declarativo adicionando source guards frágeis não representa necessariamente melhoria.

Reduzir o número de workflows pode ser útil, mas não deve eliminar status ou gatilhos necessários.

O resultado de eficiência deve considerar simultaneamente:

**custo de execução, capacidade de detectar regressões e custo de investigar falhas.**

---

## 17. Sequência preferencial de execução

A ordem indicada abaixo privilegia correções que aumentam a confiabilidade dos demais testes.

### Fase A — Saber o que existe

1. TST-001 — Baseline e mapa de execução.
2. TST-002 — Matriz de assertions.
3. TST-004 — Alcançabilidade.
4. TST-005 — Required checks.

TST-003 pode iniciar após o primeiro inventário de assertions.

**Marco:** a infraestrutura existente torna-se compreensível.

### Fase B — Confiar nas fixtures

5. TST-006 — Servidor Buyer V5.
6. TST-007 — Browser glass.
7. TST-008 — Isolamento de testes mutáveis.

**Marco:** os testes executam sobre o produto correto e não corrompem o ambiente de trabalho.

### Fase C — Proteger contratos críticos

8. TST-009 — Persistência V5.
9. TST-010 — Autorização.
10. TST-011 — Projeção pública e preços.

Esses pacotes podem ser trabalhados parcialmente em paralelo após a estabilização de suas fixtures.

**Marco:** segurança e publicação possuem cobertura atribuída e alcançável.

### Fase D — Proteger experiência de uso

11. TST-012 — Navegação.
12. TST-013 — Teclado.
13. TST-014 — Layout/PiP.
14. TST-015 — Tema.
15. TST-016 — Contraste.
16. TST-017 — Geometria.
17. TST-019 — Screenshots.
18. TST-021 — Acessibilidade.

**Marco:** componentes e estados visuais possuem provas adequadas ao risco.

### Fase E — Fechar sistemas específicos

19. TST-018 — Assets e replays.
20. TST-020 — Localização.

**Marco:** assets e textos possuem cobertura rastreável e semântica.

### Fase F — Otimizar e integrar

21. TST-022 — Seleção por impacto.
22. TST-023 — Infraestrutura compartilhada.
23. TST-024 — Diagnóstico de intermitência.
24. TST-025 — Gates de integração.
25. TST-026 — Recibos e DoD.

**Marco:** o CI oferece feedback mais rápido e evidências de conclusão reutilizáveis.

A ordem pode mudar conforme os bloqueios reais.

Por exemplo, corrigir o gate de tema não precisa aguardar a conclusão de testes históricos de pedra.

---

## 18. Pontos de interrogação

| ID | Pergunta | Resolução |
|---|---|---|
| TST-Q01 | Quais workflows são required checks hoje? | Consultar regras com autorização adequada |
| TST-Q02 | Quais checks nunca são acionados por uma PR pertinente? | Matriz path→trigger→job→assertion |
| TST-Q03 | Qual é a duração real dos principais jobs? | Medir runs comparáveis |
| TST-Q04 | Quais assertions são estruturalmente frágeis? | Comparar contrato e implementação testada |
| TST-Q05 | Quais chamadas repetidas podem compartilhar infraestrutura? | Classificar por contrato e SHA |
| TST-Q06 | O browser glass da PR #280 passa no head candidato? | Executar Chromium com fixture |
| TST-Q07 | A fixture Buyer precisa de mais estados para cobrir os componentes? | Mapear gaps DOM/contrato |
| TST-Q08 | Existe risco de concorrência entre teste de drift e build? | Execução isolada/concorrente controlada |
| TST-Q09 | O teste de tema pode ser reduzido à semântica sem perder invariantes? | Revisão assertion por assertion |
| TST-Q10 | O gate de preços roda em toda PR que altera o endpoint relevante? | Simulação de triggers |
| TST-Q11 | Quais contratos realmente exigem Preview autenticado? | Matriz de níveis de evidência |
| TST-Q12 | Quais cenários de WebKit requerem dispositivo real adicional? | Revisão de comportamento e risco |
| TST-Q13 | O fullscreen está coberto automaticamente nas duas páginas? | Gate específico de estado e controle |
| TST-Q14 | Quais replays stone devem continuar manuais? | Proveniência, custo e contrato atual |
| TST-Q15 | Existe algum status de CI dependente de branch histórica removida? | Auditoria de workflows e branches |
| TST-Q16 | Como garantir que o teste relevante sempre acompanha a alteração correspondente? | Mapeamento de impacto e CI |
| TST-Q17 | Onde os testes usam uma fixture que não corresponde ao ambiente declarado? | Auditoria de precondições |
| TST-Q18 | Quais falhas recentes foram de fixture e não do produto? | Histórico de runs e diff de runtime |
| TST-Q19 | Quais testes exigem um golden realmente independente? | Revisão de oráculos e assets |
| TST-Q20 | Como medir ganho de eficiência sem incentivar perda de cobertura? | Métricas combinadas de custo e eficácia |

---

## 19. Critérios para interromper alterações na CI

Uma mudança de CI deve ser interrompida quando:

1. Um contrato perde seu único caminho de execução.
2. Um required check fica impossibilitado de concluir.
3. Um workflow reutilizável altera o SHA efetivamente testado.
4. Uma fixture passa a fornecer permissões inexistentes no ambiente real.
5. Uma alteração remove um teste negativo sem substituto.
6. Um source guard frágil é trocado por ausência de verificação.
7. Um rerun verde é usado para descartar uma falha sem diagnóstico.
8. Um teste visual passa a atualizar automaticamente o golden.
9. Um replay histórico modifica assets atuais.
10. Uma validação precisa escrever em produção sem autorização.
11. Uma alteração de paths faz um gate relevante deixar de rodar.
12. O ganho de velocidade só existe porque uma etapa foi ignorada.
13. O pacote combina manutenção de CI com mudança funcional sem necessidade.
14. A integração torna impossível rastrear quais assertions passaram no head.
15. Os resultados não identificam a versão e a fixture utilizadas.

O rollback deverá restaurar o comportamento de CI anterior e preservar o histórico dos runs.

---

## 20. DoD global de engenharia de testes

Um pacote TST somente poderá receber `done` quando:

- O contrato que ele protege está definido.
- O risco correspondente está registrado.
- Os consumidores estão identificados.
- A fixture é válida para o teste.
- A assertion realmente foi executada.
- O ambiente e a versão são conhecidos.
- Os casos negativos pertinentes foram preservados.
- O caminho de CI é alcançável quando necessário.
- As evidências estão associadas ao SHA correto.
- Não houve perda de cobertura relevante.
- A alteração foi integrada à branch-alvo.
- O resultado foi verificado após integração quando aplicável.
- O rollback está definido.
- O estado e o recibo foram adicionados ao acompanhamento operacional.

### 20.1 Estado dos pacotes planejados

Por padrão, novos itens TST entram no anexo como `not_started`.

Itens já implementados ou parcialmente demonstrados deverão ser reconciliados com o código e as evidências.

Isso evita dois erros:

- Marcar como não iniciado algo já concluído.
- Marcar como concluído algo que existe apenas em uma PR Draft.

### 20.2 Protocolo de execução

Antes do trabalho, o agente declara:

```text
IDs assumidos:
TST-006, TST-007

Branch-alvo:
main

Dependências:
DOM-011 — contrato conhecido
Fixture local — existente

Bundles:
BT-TST-10
BT-TST-11

Controle negativo:
Nenhuma alteração em runtime ou auth
```

Ao finalizar:

```text
TST-006
  anterior: in_progress
  novo: in_review
  evidência: teste de fixture no SHA X
  pendente: integração

TST-007
  anterior: not_started
  novo: blocked
  motivo: browser não atingiu estado validado
  evidência: log da precondição
  próximo passo: corrigir readiness
```

Os estados acima são exemplos.

O agente não deverá transformar uma tarefa em `done` só porque executou um comando sem erro.

O estado dependerá do DoD definido.

---

## 21. Critérios de conclusão da Parte VI

A frente de testes estará concluída quando:

1. O inventário de workflows e comandos estiver atualizado.
2. A matriz de assertions cobrir os contratos prioritários.
3. Os oito testes sem invocação tiverem destino definido.
4. As quatro discrepâncias de gatilho tiverem disposição explícita.
5. Required checks forem conhecidos ou a limitação de acesso estiver registrada com encaminhamento.
6. A fixture Buyer V5 estiver estabilizada.
7. O browser glass estiver corrigido ou sua limitação permanecer explícita com decisão de escopo.
8. Testes de source drift não criarem risco desnecessário de conflito.
9. Contratos V5 e auth possuírem caminhos de execução confiáveis.
10. Navegação, tema, foco e layout tiverem bundles por consumidor.
11. Testes visuais utilizarem referências independentes quando necessário.
12. Contraste computado for separado de incertezas.
13. Assets históricos não forem confundidos com a baseline atual.
14. Localização possuir testes de catálogo e consumidores.
15. A seleção por impacto estiver documentada e verificável.
16. CI compartilhada não eliminar garantias.
17. Os pacotes possuírem recibos compatíveis com o DoD.
18. O trabalho puder ser retomado a partir dos IDs e evidências, sem reconstruir o raciocínio da auditoria.

---

## 22. Parecer final

A infraestrutura de testes do MobiliPresenter2D não precisa de uma substituição radical.

Ela precisa de uma **camada de organização entre intenção, execução e evidência**.

O projeto já investiu significativamente em contratos de domínio, validações de assets, browsers e gates especializados.

O problema é que parte desse investimento permanece difícil de capitalizar:

- Testes válidos ficam fora dos gatilhos relevantes.
- Testes semelhantes são reexecutados sem compartilhamento claro de infraestrutura.
- Falhas de fixture podem parecer defeitos do produto.
- Alguns testes verificam textos-fonte em vez de comportamento.
- Documentos afirmam cobertura, mas não necessariamente indicam o caminho de execução atual.
- Resultados de CI podem estar vinculados a branches ou commits anteriores.
- A conclusão de uma tarefa depende excessivamente de interpretação narrativa.

A solução proposta é progressiva.

Primeiro, tornar o CI inspecionável.

Depois, estabilizar as fixtures e corrigir testes com precondições inadequadas.

Em seguida, garantir cobertura dos contratos críticos.

Finalmente, otimizar a seleção de testes e integrar os resultados ao DoD operacional.

**A eficiência virá de executar a prova certa, no contexto certo, sobre a versão certa — não simplesmente de executar menos testes.**

---

### Fontes técnicas principais

**Inventários e método**

- [ARC-15 — inventário de verificações](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARC15_VERIFICATION_INVENTORY_2026-11-15.md)
- [ARC-15 — matriz de assertions V5/API](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARC15_ASSERTION_MATRIX_PUBLISHED_CONFIG_2026-11-16.md)
- [Contrato de autoridade de CI](https://github.com/EAKerber/MobiliPresenter2D/blob/main/docs/architecture/ci-authority-contract-2026-10-05.md)
- [Crosswalk arquitetural](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARCHITECTURE_EXECUTION_CROSSWALK_2026-11-15.md)

**Workflows e fixtures**

- [App build purity](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/app-build-purity.yml)
- [Current asset gates](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/candidate-assets.yml)
- [ARC-03C static page gate](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/arc03c-static-page-build-gate.yml)
- [Public menu gate](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/p-comp-01-public-menu-gate.yml)
- [Viewer base-price gate](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/viewer-base-price-contract-gate.yml)
- [Keyboard browser](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/keyboard-browser.yml)
- [Flow layout browser](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/flow-layout-browser.yml)
- [Local Buyer V5 server](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tests/ci/local-buyer-config-server.mjs)
- [Local Buyer V5 preparation](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tests/ci/prepare-local-v5-browser.sh)

**Casos concretos**

- [PR #280 — correção do browser glass](https://github.com/EAKerber/MobiliPresenter2D/pull/280)
- [PR #278 — geometria independente da arte](https://github.com/EAKerber/MobiliPresenter2D/pull/278)
- [PR #279 — dispatch UX-04](https://github.com/EAKerber/MobiliPresenter2D/pull/279)
- [Teste de tema](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tests/ui-theme-contract.cjs)
- [Teste de fonte ARC-03C](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tests/arc03c-source-authority.test.mjs)
- [Browser glass na main](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tests/exposed-sides-glass.cjs)
- [Geometria do hero](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tests/home-hero-phone-geometry-browser.cjs)

**Limite da análise:** as conclusões deste turno derivam de inspeção de código, workflows, PRs e evidências históricas. Nenhuma suíte foi reexecutada, e não foi possível confirmar os required checks aplicados à branch. Uma recomendação de correção ou integração não constitui afirmação de que a correspondente PR já passou por todos os gates.

---

<a id="capitulo-7"></a>
# Capítulo VII — Governança Git, integração incremental, publicação e rollback

## 1. Objetivo

Converter o trabalho arquitetural acumulado em mudanças integradas, verificáveis e sustentáveis, preservando a estabilidade do produto e a rastreabilidade das decisões.

Esta frente deve resolver um problema diferente da simples limpeza de branches.

O problema central é que o projeto possui trabalho distribuído entre:

- A `main`, que representa a referência estável do Produto.
- A `development`, que acumula trabalho técnico e reconciliações ainda não promovidas.
- PRs especializadas abertas.
- O Design System, que concentra decisões homologadas e evidências.
- Documentos históricos com diferentes datas e autoridades.
- Workflows de CI que validam conjuntos e momentos distintos.
- Publicações que nem sempre correspondem à branch em análise.

A integração deve preservar as informações úteis de cada uma dessas fontes, mas produzir **uma autoridade operacional clara para o próximo trabalho**.

### 1.1 Resultados esperados

Ao concluir esta frente:

1. A finalidade de cada branch ativa estará documentada.
2. Cada alteração relevante terá uma origem e um destino explícitos.
3. A `development` terá seu conteúdo classificado por intenção e contrato.
4. Nenhuma implementação antiga será promovida apenas por existir em uma branch.
5. As PRs abertas terão um plano de conclusão individual.
6. Os gates necessários para integração serão conhecidos.
7. A aprovação de uma mudança não dependerá da interpretação de um handover histórico.
8. Merge, deploy e homologação serão eventos distintos.
9. Os mecanismos de limpeza de branches preservarão seus limites de segurança.
10. O Design System continuará sendo a autoridade das decisões visuais.
11. O Produto continuará sendo a autoridade do código executável.
12. O backlog e o DoD fornecerão o estado operacional único.
13. O histórico documental permanecerá acessível sem competir com o plano atual.
14. Reversões poderão ser feitas por pacotes delimitados.
15. O esforço de retomada entre agentes será reduzido.

---

## 2. Fotografia Git atual

A leitura realizada neste turno encontrou o seguinte estado.

### 2.1 Repositório principal

| Indicador | Resultado |
|---|---|
| `main` | `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9` |
| `development` | `1a69ff76a5f36e3245a288773bb409aa662e4e62` |
| Branches remotas | 8 |
| Branches permanentes pretendidas | 2 |
| PRs abertas | 6 |
| PRs Draft | 5 |
| PR aberta não Draft | #271 |
| Relação `main…development` | `development` 434 commits à frente e 5 atrás |
| Merge base | `221b54b2a41ecc8c338d1bf2cf67280cf165ce95` |

A API de branches reporta `protected=false` para `main` e `development`. Isso não substitui uma auditoria completa de rulesets e required checks, cuja autoridade efetiva permanece pendente de confirmação.

#### Oito branches encontradas

| Branch | Papel observado |
|---|---|
| `main` | Referência estável |
| `development` | Integração e investigação |
| `codex/nav005-public-compact-main-20261110` | PR #269 |
| `codex/ds04-208-preview-batch-20261111` | PR #271 |
| `docs/arc13-post-273-reconciliation-20261114` | PR #274 |
| `fix/hero-screen-art-anchor-20261116` | PR #278 |
| `infra/ux04-dispatch-workflow-20261116` | PR #279 |
| `test/glass-browser-replay-20261116` | PR #280 |

**Nenhuma dessas seis branches de PR é automaticamente candidata à exclusão.**

A contagem de oito ultrapassa o soft cap histórico de cinco, mas cinco é um gatilho de revisão, não um limite de segurança que autoriza destruição.

### 2.2 Repositório Design System

| Indicador | Resultado |
|---|---|
| `main` | `79db735d6f05177b0c406e383d35832f3d72fdef` |
| Branches remotas | 2 |
| PRs abertas | 1 |
| PR #119 | Draft |
| Head da #119 | `c4cff5e0b707ed728618f8ce1c60310eeca23fad` |
| Arquivos alterados na #119 | 93 |
| Commits na PR | 151 |

Os 93 arquivos da #119 são predominantemente documentos e evidências; não representam uma implementação executável do Produto.

O Design System já alcançou a meta de possuir somente `main` e uma branch temporária de documentação.

O trabalho restante nesse repositório é principalmente de **integração e consolidação de autoridade documental**, não de redução agressiva de branches.

### 2.3 Interpretação correta da divergência

Os 434 commits exclusivos da `development` não representam 434 funcionalidades pendentes.

A comparação de GitHub inclui uma quantidade expressiva de:

- Workflows de desenvolvimento.
- Ferramentas de auditoria.
- Inventários e evidências.
- Documentos de reconciliação.
- Testes específicos.
- Alterações pontuais de runtime.

Na lista de arquivos retornada pela comparação, que possui limite de 300 entradas, aparecem 53 arquivos de workflows e 217 caminhos de documentação.

Isso indica forte presença de trabalho metodológico e documental, mas **não é um inventário integral de todos os arquivos divergentes**.

Portanto, não devemos estimar esforço restante contando commits ou linhas de diff.

A unidade relevante é a **intenção técnica ainda não absorvida**, vinculada a contrato, consumer e prova.

---

## 3. Decisões homologadas que governam a integração

As decisões D01–D04 continuam formando uma base adequada.

### D01 — Integração incremental após gates

Uma mudança entra no destino quando suas dependências e testes aplicáveis estão satisfeitos.

Não integrar simultaneamente grandes conjuntos apenas porque suas branches foram classificadas.

### D02 — Testes isolados inicialmente aceitáveis

Testes locais podem satisfazer um gate inicial quando comprovam o contrato correspondente.

Isso não equivale a validação hospedada, autenticação real ou publicação.

O plano deve registrar a diferença em vez de bloquear todo trabalho por um único ambiente indisponível.

### D03 — Extração do útil antes do encerramento

PRs antigas e substituídas devem ser reconciliadas por conteúdo e intenção.

Somente depois de verificar o destino do conteúdo relevante será possível encerrá-las com segurança.

### D04 — Consolidação seletiva com proveniência

Evidências, ferramentas e implementações devem ser importadas por necessidade.

Não mesclar integralmente branches documentais históricas apenas para preservar arquivos que podem ser recuperados de forma seletiva.

### 3.1 Hierarquia de autoridade proposta

A hierarquia deve ser determinada pela natureza da informação.

| Informação | Autoridade primária |
|---|---|
| Homologações visuais | Decisões aprovadas do Design System |
| Arquitetura homologada ARC | Contrato arquitetural aprovado |
| Código executável estável | Produto `main` |
| Código experimental | Branch/PR específica, com escopo limitado |
| Mudanças ainda em integração | `development` ou PR candidata |
| Estado de publicação | Deploy efetivamente servido |
| Resultado de teste | Run e SHA correspondentes |
| Aprovação do usuário | Decisão explicitamente registrada |
| Estado operacional dos trabalhos | Anexo DoD do plano diretor |
| Histórico | Commits, PRs, handovers e recibos preservados |

Não existe uma única autoridade universal para todos os assuntos.

Uma homologação visual não prova que o código correspondente foi integrado.

Um commit integrado não prova que o navegador já está carregando o novo asset.

Uma branch mais recente não revoga automaticamente uma decisão homologada.

---

## 4. Revisão crítica do método histórico

### 4.1 O método de auxiliares foi útil para controlar a reconciliação

As branches auxiliares permitiram:

- Trabalhar em conjuntos tecnicamente relacionados.
- Preservar as origens históricas.
- Evitar merges indiscriminados na `main`.
- Testar extrações separadamente.
- Identificar regressões antes da integração.
- Consolidar resultados em `development`.
- Retirar branches antigas com gates explícitos.

Essa estratégia respondeu adequadamente à situação inicial de grande divergência.

Entretanto, a redução de branches não encerra automaticamente o trabalho arquitetural.

As alterações ainda precisam alcançar os consumidores finais e, quando aplicável, a `main`.

### 4.2 A `development` acumulou outra forma de complexidade

O processo transformou múltiplas branches históricas em uma base de integração com extensa documentação e muitos workflows especializados.

Isso é melhor do que dezenas de branches sem classificação.

Mas o próximo gargalo é diferente: **descobrir qual parcela da `development` ainda precisa de integração funcional e qual parcela já cumpriu sua finalidade como evidência histórica**.

Continuar criando auxiliares exclusivamente para mapear auxiliares produziria retornos decrescentes.

A estratégia agora deve passar de reconciliação histórica para fechamento por contrato.

### 4.3 Há autoridade documental concorrente

O Produto e o Design System contêm vários documentos com status e prioridades.

O exemplo mais claro é o `HANDOVER_CURRENT.md` da `main` do Design System, cuja abertura ainda descreve um checkpoint de outubro e orienta priorizar a limpeza do Design System antes de trabalhar no Produto.

Essa orientação foi adequada ao seu contexto histórico.

Mas, como instrução operacional atual, não pode prevalecer sobre as decisões posteriores de trabalhar no Produto e consolidar a arquitetura.

A #119 contém uma atualização mais recente, porém ainda não foi integrada.

**Diagnóstico:** o projeto precisa de uma fonte operacional atualizada que não dependa de decidir, caso a caso, qual handover narrativo é mais recente.

O anexo DoD será essa fonte de estado.

As decisões técnicas e os recibos continuarão nos documentos pertinentes.

### 4.4 Há risco de fechamento prematuro de gates

Algumas PRs possuem workflows verdes, mas ainda carregam ressalvas de:

- Navegador hospedado.
- Configuração publicada inválida.
- Acessibilidade.
- Integração na `main`.
- Publicação.
- Runtime efetivo do último SHA.

O problema não é possuir ressalvas.

É permitir que “PR verde” seja interpretado como “contrato completamente homologado”.

O DoD precisa impedir essa equivalência.

### 4.5 A seleção de branches por quantidade já não oferece grande benefício

Atualmente, todas as branches temporárias do Produto estão associadas a PRs abertas.

Excluí-las apenas para alcançar cinco ou duas branches seria incompatível com a finalidade do trabalho em curso.

A redução deverá ocorrer como consequência de:

1. Integrar uma PR.
2. Encerrar uma PR efetivamente substituída.
3. Comprovar preservação do conteúdo.
4. Autorizar e executar a higiene segura da ref.

A contagem passa a ser um indicador de fricção operacional, não o objetivo principal.

---

## 5. Modelo de branches proposto

### 5.1 `main`

Responsabilidade:

- Código estável.
- Contratos de produção.
- Correções aprovadas.
- CI de integração.
- Fonte para builds e deploys oficiais.

Uma funcionalidade entra na `main` após satisfazer seu pacote de integração.

### 5.2 `development`

Responsabilidade:

- Integração não estável.
- Trabalho ainda em revisão.
- Ferramentas técnicas necessárias à evolução.
- Extrações históricas que ainda não foram promovidas.
- Experimentos delimitados.

Ela não deve ser tratada como branch automaticamente publicável.

Também não deve permanecer indefinidamente como depósito de qualquer documentação gerada por investigação.

### 5.3 Branches auxiliares

Criadas somente quando:

- Existe uma entrega identificada por ID.
- O escopo é tecnicamente coeso.
- Há destino definido.
- Os testes necessários são conhecidos.
- A integração direta em uma PR existente não é adequada.
- O risco de conflito justifica isolamento.

A meta é evitar criar uma branch para toda subtarefa pequena.

Uma branch pode atender vários IDs próximos.

Mas não deverá reunir contratos independentes apenas para economizar um nome de branch.

### 5.4 Branches de documentação

Documentação operacional que afeta o Produto deverá ter o Produto como destino, quando for seu estado de execução.

Documentação de decisão e evidência do Design System deverá permanecer no Design System.

O mesmo estado de progresso não deve ser mantido manualmente em dois repositórios.


### 5.5 Política de estabilização e promoção — emenda operacional v0.9

Esta política complementa a integração incremental de D01–D04 e as regras GIT-005–011. **Não altera a versão do plano nem substitui os contratos homologados.**

#### Produto: `development` como buffer de estabilização

O caminho preferencial para alterações ordinárias passa a ser:

**Branch de trabalho → PR → `development` → estabilização integrada → promoção seletiva → `main`.**

A `development` é o buffer para ajustes finais e incompatibilidades entre pacotes. Não é apenas um depósito de experimentos, não é uma branch automaticamente publicável e não equivale a autorização de release. Mudanças independentes podem avançar sem esperar que todo o roadmap seja concluído.

**Um pacote é candidato estável à `main` quando:**

1. Seu objetivo, escopo e contratos estão identificados e respeitam as homologações pertinentes.
2. As dependências reais estão atendidas e o pacote foi verificado na `development`, quando aplicável.
3. Testes proporcionais ao risco passaram no SHA correspondente, incluindo os consumidores afetados.
4. Não existem regressões críticas nem bloqueios incompatíveis com a promoção; exceções remanescentes têm owner e aceitação explícita.
5. O conjunto promovido está delimitado, possui provenance, preflight e estratégia de rollback.
6. A candidata foi revisada sobre a `main` atual e pode receber readback pós-merge.

Devido à divergência histórica entre `main` e `development`, **não realizar merge indiscriminado da árvore de `development`**. Selecionar os commits pertinentes ou reconstruir o patch a partir da `main` atual, preservando provenance e revalidando o resultado. A passagem por `development` não substitui o teste da candidata final.

Durante a estabilização, correções pertencentes ao mesmo contrato podem compartilhar o pacote. Mudanças independentes não devem ser incorporadas incidentalmente. Alterações relevantes invalidam apenas as evidências que deixam de cobrir o SHA ou o comportamento atualizado.

Uma correção urgente poderá ir diretamente à `main` quando houver justificativa e autorização apropriadas, mantendo testes, readback e posterior reconciliação com `development` para evitar reintrodução do defeito.

Para fins do DoD, código estabilizado em `development` é evidência de maturidade, não `done` de um item cujo destino declarado seja `main`. A conclusão depende da integração e do readback de destino quando aplicáveis.

#### Design System: persistência e promoção documental

O Plano Diretor consolidado **permanece v0.9**, inclusive com esta emenda. Sua persistência deve preferencialmente aproveitar a branch documental e a PR existentes do Design System, sem criar uma branch `development` nesse repositório apenas para espelhar o Produto.

**Recomenda-se integrar o documento à `main` do Design System assim que for viável**, depois de verificar integridade, compatibilidade com as decisões homologadas e ausência de conflito concreto com o fluxo documental existente. Não é necessário concluir as tarefas arquiteturais descritas para integrar o plano: **a estabilidade do documento é independente do progresso da implementação**.

Manter a PR documental aberta apenas pelo período necessário à revisão e resolução desses conflitos, evitando uma estabilização documental indefinida. A integração à `main` dependerá de aprovação, merge e readback; a persistência na branch não representa, por si só, promoção.

#### Limites de publicação

Atualizações em `development` ou na PR documental não autorizam deploy de produção. A política de Deploy Previews é controlada separadamente pelos itens OPS-NET-001/002, com inspeção e eventual mudança na interface gráfica do Netlify por meio do navegador do ChatGPT, e nunca como efeito automático desta emenda.


---

## 6. Marco GIT-M0 — Reconciliação de autoridade e estado

### GIT-001 — Criar snapshot operacional dos repositórios

**Prioridade:** P0  
**Dependências:** nenhuma  
**Bundle:** BT-GIT-00

#### Objetivo

Estabelecer a base exata de qualquer futura operação Git.

#### Procedimento

1. Registrar a identidade dos dois repositórios confirmados.
2. Consultar os SHAs de `main`.
3. Consultar o SHA de `development`.
4. Listar branches remotas.
5. Listar PRs abertas.
6. Listar PRs Draft.
7. Registrar heads e bases.
8. Identificar os arquivos modificados nas PRs relevantes.
9. Consultar a relação entre `main` e `development`.
10. Identificar a merge base.
11. Consultar workflows atuais.
12. Identificar regras de proteção acessíveis.
13. Registrar required checks conhecidos.
14. Registrar required checks não verificáveis.
15. Identificar o último deploy de produção confirmado.
16. Identificar qual commit esse deploy utiliza.
17. Identificar Preview ativo, quando material ao trabalho.
18. Registrar a data e as ferramentas utilizadas.
19. Produzir um recibo conciso.
20. Não executar operações de escrita nesta etapa.

#### DoD

Snapshot reproduzível, com SHAs e limitações explícitas.

---

### GIT-002 — Consolidar a hierarquia documental

**Prioridade:** P0  
**Dependências:** GIT-001  
**Bundle:** BT-GIT-00

#### Objetivo

Eliminar ambiguidade entre decisão, plano, estado e histórico.

#### Procedimento

1. Inventariar documentos atuais de arquitetura.
2. Inventariar handovers.
3. Inventariar matrizes de gates.
4. Inventariar documentos históricos.
5. Identificar decisões homologadas.
6. Identificar propostas ainda não aprovadas.
7. Identificar documentos que fazem afirmações de estado.
8. Identificar instruções operacionais que ficaram obsoletas.
9. Confirmar quais documentos são vinculantes.
10. Definir o plano diretor como referência de método.
11. Definir o anexo DoD como referência do estado de execução.
12. Manter decisões do Design System como autoridade estética.
13. Manter recibos de teste como autoridade das evidências.
14. Evitar apagar documentos históricos.
15. Substituir links de retomada antigos por ponteiros para a fonte atual.
16. Registrar a data de vigência de cada instrução.
17. Remover duplicações de estado quando sua autoridade já foi transferida.
18. Integrar as atualizações documentais pertinentes.

#### DoD

Um agente consegue determinar qual documento consultar para cada tipo de informação sem reconstruir uma sequência de handovers.

---

### GIT-003 — Classificar a divergência `development` versus `main`

**Prioridade:** P0  
**Dependências:** GIT-001/002  
**Bundle:** BT-GIT-01

#### Objetivo

Transformar os 434 commits exclusivos de `development` em uma lista de intenções ainda relevantes, já absorvidas ou históricas.

#### Procedimento

1. Identificar a merge base.
2. Obter a lista integral de commits exclusivos.
3. Obter a lista integral de arquivos diferentes.
4. Não depender do limite de arquivos de uma única resposta de compare.
5. Agrupar mudanças por intenção declarada.
6. Agrupar alterações por contrato afetado.
7. Identificar alterações exclusivamente documentais.
8. Identificar testes e workflows exclusivos.
9. Identificar alterações de código do Produto.
10. Identificar alterações já absorvidas por outro caminho na `main`.
11. Identificar alterações semanticamente equivalentes, mesmo com SHAs diferentes.
12. Identificar alterações antigas substituídas por implementação mais recente.
13. Identificar alterações exclusivas sem sucessor.
14. Identificar mudanças incompatíveis com o contrato homologado.
15. Identificar diferenças causadas somente pela evolução da `main`.
16. Mapear cada diferença funcional a um ID do backlog.
17. Registrar o SHA original.
18. Registrar o arquivo de destino.
19. Registrar o teste que protege a intenção.
20. Classificar a disposição.
21. Resolver itens de maior risco primeiro.
22. Não criar uma branch por diferença encontrada.
23. Publicar a matriz de reconciliação.
24. Atualizar apenas o estado operacional comprovado.

#### Disposições propostas

- `already_integrated`
- `equivalent_in_main`
- `extract_to_main`
- `retain_in_development`
- `documentation_only`
- `historical_evidence`
- `superseded`
- `requires_decision`
- `reject_incompatible`

Essas classificações não substituem os seis estados do DoD.

Elas explicam o destino técnico de uma diferença.

#### DoD

Todas as diferenças materialmente relevantes possuem destino e justificativa; nenhuma alteração é promovida apenas por ser mais recente.

---

### GIT-004 — Inventariar a intenção das PRs abertas

**Prioridade:** P0  
**Dependências:** GIT-001  
**Bundle:** BT-GIT-01

#### Objetivo

Obter um plano concreto de fechamento das PRs atuais.

#### Procedimento

1. Fixar head e base de cada PR.
2. Identificar sua intenção original.
3. Identificar a intenção vigente.
4. Identificar decisões homologadas aplicáveis.
5. Identificar arquivos alterados.
6. Identificar contratos afetados.
7. Identificar alterações fora de escopo.
8. Identificar testes existentes.
9. Identificar testes que não foram executados no último SHA.
10. Identificar validações hospedadas pendentes.
11. Identificar dependências de outras PRs.
12. Identificar conflitos reais de arquivo.
13. Identificar conflitos de semântica.
14. Registrar o rollback.
15. Associar IDs do backlog.
16. Definir sequência de integração.
17. Definir critério de fechamento.
18. Registrar bloqueios específicos.

#### DoD

Cada PR aberta possui uma disposição e um critério verificável para integração, reestruturação, manutenção ou encerramento.

---

## 7. Marco GIT-M1 — Construção do plano de integração

### GIT-005 — Criar o DAG de dependências entre pacotes

**Prioridade:** P0  
**Dependências:** GIT-003/004  
**Bundle:** BT-GIT-02

#### Objetivo

Impedir que a ordem de merge seja decidida apenas pela ordem de criação das PRs.

#### Procedimento

1. Listar pacotes de integração.
2. Associar IDs de execução.
3. Identificar owners de código.
4. Identificar arquivos comuns.
5. Identificar contratos compartilhados.
6. Identificar dependências de build.
7. Identificar dependências de fixture.
8. Identificar dependências de homologação.
9. Identificar bloqueios de autenticação.
10. Identificar dependências de publicação.
11. Criar arestas somente para dependências reais.
12. Identificar ciclos.
13. Resolver ciclos por redução de escopo.
14. Identificar caminhos independentes.
15. Identificar pacotes com conflito de escrita.
16. Definir ordem preferencial.
17. Definir pontos de rebase/reconciliação.
18. Definir gates por pacote.
19. Revisar risco global de integração.
20. Publicar o DAG operacional.

#### Regra

Um gate de contraste hospedado pendente não deve bloquear automaticamente uma extração textual que não depende dele.

Uma alteração de um token global, porém, deve incluir os consumidores realmente afetados.

#### DoD

O caminho crítico é explícito e os pacotes independentes podem avançar sem bloquear uns aos outros.

---

### GIT-006 — Definir unidade mínima de integração

**Prioridade:** P0  
**Dependências:** GIT-005  
**Bundle:** BT-GIT-02

#### Objetivo

Evitar tanto PRs excessivamente pequenas quanto merges grandes demais.

#### Critério de coesão

Um conjunto pode ser integrado em uma PR quando possui:

1. Objetivo técnico comum.
2. Contrato principal comum.
3. Consumidores relacionados.
4. Testes que formam um bundle coerente.
5. Risco de regressão semelhante.
6. Estratégia de rollback comum.

O número de arquivos não é critério suficiente.

#### Procedimento

1. Definir o objetivo do conjunto.
2. Identificar arquivos necessários.
3. Identificar arquivos gerados.
4. Identificar testes relevantes.
5. Identificar atualizações documentais indispensáveis.
6. Confirmar que nenhuma mudança independente foi incorporada.
7. Confirmar que o diff pode ser revisado.
8. Confirmar que o rollback é delimitado.
9. Avaliar se o conjunto deve ser dividido.
10. Avaliar se subetapas podem compartilhar a mesma branch.
11. Escolher a menor estrutura que preserve o objetivo.
12. Registrar os IDs incluídos.

#### DoD

Pacotes possuem fronteiras técnicas claras e não exigem merges de alterações independentes para produzir uma entrega útil.

---

### GIT-007 — Formalizar extração seletiva com proveniência

**Prioridade:** P0  
**Dependências:** GIT-003/006  
**Bundle:** BT-GIT-03

#### Objetivo

Promover o conteúdo necessário da `development` ou de branches históricas sem carregar código substituído e infraestrutura obsoleta.

#### Procedimento

1. Escolher o ID de execução.
2. Identificar a intenção da alteração.
3. Identificar o commit de origem.
4. Identificar o arquivo de origem.
5. Identificar o contrato vigente.
6. Comparar a origem com a implementação da `main`.
7. Verificar se já existe solução equivalente.
8. Identificar diferenças de comportamento.
9. Identificar dependências internas.
10. Identificar dependências obsoletas.
11. Extrair a menor unidade funcional completa.
12. Adaptar à versão atual do contrato.
13. Preservar semântica homologada.
14. Registrar proveniência do código ou do teste.
15. Não copiar workflows históricos desnecessários.
16. Não copiar bypasses ou fixtures inseguras.
17. Executar testes relevantes.
18. Executar controles negativos.
19. Integrar na branch de destino.
20. Confirmar que a intenção foi preservada.
21. Atualizar a classificação da origem.
22. Registrar a evidência.

#### Regra para divergências

Quando duas implementações atendem à mesma função:

- Primeiro, identificar a intenção homologada mais recente.
- Depois, comparar comportamento real.
- Preferir a implementação mais recente quando ela preserva o contrato e demonstra melhor adequação.
- Manter a versão da `main` quando a alternativa não possui prova suficiente.
- Não descartar uma mudança apenas pela data mais antiga.
- Não promover uma mudança apenas pelo timestamp mais recente.

#### DoD

Conteúdo integrado possui origem identificada, contrato preservado e ausência de dependências históricas desnecessárias.

---

### GIT-008 — Definir a política de reconciliação com `main`

**Prioridade:** P0  
**Dependências:** GIT-005/007  
**Bundle:** BT-GIT-03

#### Objetivo

Evitar rebase ou merge global de uma branch muito divergente.

#### Estratégia preferida

Para alterações destinadas à `main`, utilizar a `main` atual como base da PR candidata sempre que isso produzir um diff mais claro.

Extrair seletivamente da `development` o conteúdo pertinente.

Não exigir que toda a `development` seja incorporada antes de integrar um componente já aprovado.

#### Procedimento

1. Fixar a `main` de origem.
2. Identificar o conjunto de alterações desejado.
3. Determinar se a PR já está baseada na `main` atual.
4. Identificar commits de reconciliação existentes.
5. Identificar diferenças de arquivo.
6. Comparar com o contrato em produção.
7. Identificar mudanças da `main` ocorridas depois do início do trabalho.
8. Identificar quais mudanças precisam ser preservadas.
9. Escolher merge/rebase/cherry-pick seletivo conforme proveniência.
10. Evitar reescrever história compartilhada sem necessidade.
11. Confirmar que a reconciliação não altera o escopo.
12. Executar diff após a reconciliação.
13. Confirmar que o teste anterior continua pertinente.
14. Reexecutar gates necessários no head atualizado.
15. Registrar o novo SHA.
16. Não promover status antigos para o novo SHA automaticamente.
17. Integrar com readback posterior.
18. Registrar eventuais diferenças restantes.

#### DoD

A candidata incorpora a autoridade atual da `main` sem absorver incidentalmente o restante da `development`.

---

## 8. Marco GIT-M2 — PRs, gates e fechamento de mudanças

### GIT-009 — Criar contrato operacional para PRs

**Prioridade:** P0  
**Dependências:** GIT-005/006  
**Bundle:** BT-GIT-04

#### Objetivo

Fazer com que uma PR contenha informação suficiente para ser revisada sem procurar decisões em múltiplos handovers.

#### Campos obrigatórios propostos

| Campo | Conteúdo |
|---|---|
| IDs | Tarefas do backlog |
| Objetivo | Resultado esperado |
| Base | Branch e SHA |
| Origem | PRs/commits relevantes |
| Contrato | Decisão ou schema aplicável |
| Alterações | Arquivos e comportamento |
| Não objetivos | O que não deve mudar |
| Bundle | Testes requeridos |
| Evidência | Runs e capturas |
| Pendências | Gaps reais |
| Rollback | Reversão específica |
| Integração | Branch-alvo |
| DoD | Condição de encerramento |

#### Procedimento

1. Associar IDs.
2. Delimitar escopo.
3. Fixar base.
4. Fixar origem.
5. Listar arquivos alterados.
6. Registrar arquivos gerados.
7. Identificar contratos.
8. Listar testes.
9. Declarar controles negativos.
10. Definir rollback.
11. Registrar resultados por SHA.
12. Registrar limitações.
13. Atualizar após cada mudança relevante do head.
14. Impedir que evidência histórica seja apresentada como prova do head atual.
15. Encerrar somente após integração ou disposição explícita.

#### DoD

Toda PR de integração apresenta contrato, evidência e condição de conclusão diretamente verificáveis.

---

### GIT-010 — Formalizar o preflight de merge

**Prioridade:** P0  
**Dependências:** GIT-009, TST-025  
**Bundle:** BT-GIT-04

#### Objetivo

Evitar merges que aparentemente passam, mas deixam riscos relevantes não resolvidos.

#### Preflight

1. Confirmar head e base da PR.
2. Confirmar que a PR está pronta para revisão.
3. Confirmar ausência de conflito de merge.
4. Confirmar que o diff corresponde ao escopo.
5. Confirmar a decisão homologada.
6. Confirmar o owner responsável.
7. Confirmar ausência de mudança incidental.
8. Confirmar testes necessários.
9. Confirmar resultados do head apropriado.
10. Confirmar required checks aplicáveis.
11. Confirmar que testes skipped têm motivo.
12. Confirmar que não há falso PASS de fixture.
13. Confirmar regressões visuais relevantes.
14. Confirmar acessibilidade quando aplicável.
15. Confirmar ausência de vazamento de dados.
16. Confirmar que scripts de build não reescrevem fontes.
17. Confirmar rollback.
18. Confirmar impacto esperado na publicação.
19. Registrar decisão GO/HOLD.
20. Somente então integrar.

#### DoD

Toda integração possui recibo de preflight e não depende apenas do indicador visual de checks verdes.

---

### GIT-011 — Formalizar o readback pós-merge

**Prioridade:** P0  
**Dependências:** GIT-010  
**Bundle:** BT-GIT-04

#### Objetivo

Comprovar que a entrega entrou no destino previsto.

#### Procedimento

1. Registrar método de merge.
2. Registrar commit integrado.
3. Ler a branch-alvo após integração.
4. Confirmar presença dos arquivos pretendidos.
5. Confirmar presença das alterações necessárias.
6. Confirmar ausência de regressão no diff.
7. Confirmar que arquivos gerados continuam sincronizados.
8. Executar os testes de destino aplicáveis.
9. Verificar o resultado de CI.
10. Conferir eventuais conflitos resolvidos durante merge.
11. Confirmar que a implementação antiga foi substituída quando necessário.
12. Confirmar que não restou segunda autoridade concorrente.
13. Registrar eventuais pendências de publicação.
14. Atualizar status dos IDs.
15. Registrar a transição na timeline.
16. Manter PR/branch até a higiene ser elegível e autorizada.

#### DoD

A integração está comprovada no destino, não apenas na branch de origem.

---

## 9. Marco GIT-M3 — Plano específico das PRs atuais

As seis PRs do Produto devem permanecer como frentes identificáveis.

Não recomendo juntá-las automaticamente.

### GIT-012 — Revisar e concluir PR #269 — NAV-005

**Prioridade:** P0  
**Dependências:** CMP-002/003/004, TST-012  
**Bundle:** BT-GIT-10  
**Head observado:** `28b1e2ef4f62b418110ba7694a59dee95969174b`

#### Escopo

Header público primário, composição autoral e comportamento responsivo.

A PR modifica 18 caminhos.

#### Procedimento

1. Confirmar a base atual.
2. Conferir os arquivos autorais.
3. Conferir os HTMLs gerados.
4. Conferir o controlador de menu.
5. Conferir as alterações de CSS.
6. Conferir o workflow novo.
7. Conferir o teste de teclado modificado.
8. Confirmar que UX-04 está fora do diff.
9. Confirmar que o Viewer não recebeu redesign.
10. Confirmar o CTA em menu compacto.
11. Validar 290/291 px.
12. Verificar foco e Escape.
13. Verificar logo e tema.
14. Verificar resultado visual no head atual.
15. Conferir controles negativos.
16. Confirmar gates necessários.
17. Identificar qualquer decisão ainda pendente.
18. Integrar somente após preflight.
19. Reexecutar os gates relevantes no destino.
20. Atualizar NAV-005/DoD.

#### DoD

NAV-005 primário integrado, com HTML de fonte única e sem regressão nos consumidores.

---

### GIT-013 — Revisar e concluir PR #271 — DS-04

**Prioridade:** P0/P1  
**Dependências:** G2 e TOK/CSS pertinentes, TST-016  
**Bundle:** BT-GIT-11  
**Head observado:** `8a67d10fc8911bc146cf28667dd03e445af37f47`

#### Escopo

Quatro arquivos de CSS/HTML ligados a contraste e controles específicos.

#### Procedimento

1. Fixar os quatro arquivos alterados.
2. Confirmar quais seletores são afetados.
3. Confirmar tokens utilizados.
4. Confirmar que os valores seguem a autoridade aprovada.
5. Identificar pares de contraste corrigidos.
6. Identificar pares ainda incertos.
7. Confirmar o resultado dos nove workflows do head.
8. Confirmar o Preview correspondente.
9. Distinguir validações hospedadas históricas da revisão do head atual.
10. Verificar Admin.
11. Verificar Access.
12. Verificar Viewer.
13. Identificar dependência de `/config/` hospedado.
14. Não tratar fixture inválida como aprovação visual.
15. Isolar o que pode ser integrado com evidência suficiente.
16. Manter HOLD para o que exigir prova hospedada ainda inexistente.
17. Verificar `#viewerHint` e headings pelo contrato de contexto.
18. Integrar somente quando o recorte cumprir seu DoD.
19. Executar readback.
20. Não encerrar globalmente G2 por aprovação de quatro arquivos.

#### DoD

O conjunto integrado possui prova de seus consumidores reais; pendências de G2 permanecem individualizadas.

---

### GIT-014 — Revisar e concluir PR #274 — ARC-13

**Prioridade:** P1  
**Dependências:** LOC-001/002, fonte ARC-03C  
**Bundle:** BT-GIT-12  
**Head observado:** `72ae7c8a7e3a8c89645d91d91482d66c1eb4d764`

#### Escopo

Inventário, ferramentas e documentação ARC-13.

A PR modifica 41 arquivos, incluindo um grande relatório gerado.

Ela não implementa o catálogo final de localização.

#### Procedimento

1. Confirmar a baseline.
2. Confirmar o SHA do inventário.
3. Confirmar validade do JSON.
4. Confirmar os 1.026 sinks.
5. Confirmar as 360 fontes JS.
6. Confirmar mapeamentos HTML autorais.
7. Confirmar ausência de ocorrências sem origem no recorte.
8. Confirmar reconciliação do delta da #277.
9. Revisar textos ainda pendentes.
10. Confirmar que nenhum texto foi aprovado implicitamente.
11. Verificar a utilidade dos artefatos grandes.
12. Identificar artefatos canônicos e derivados.
13. Evitar duplicações editáveis do mesmo inventário.
14. Verificar tamanho e custo de manutenção dos arquivos gerados.
15. Regerar se mudanças relevantes de UI tiverem entrado antes.
16. Confirmar que os scripts de inventário são determinísticos.
17. Executar testes e checks de fonte.
18. Integrar a base documental quando satisfizer o escopo.
19. Registrar que a extração `pt-BR` continua em LOC-003…008.
20. Atualizar DoD sem declarar ARC-13 integralmente concluído.

#### DoD

Inventário ARC-13 confiável e integrado, com escopo distinto da implementação do catálogo.

---

### GIT-015 — Revisar e concluir PR #278 — geometria do hero

**Prioridade:** P1  
**Dependências:** TST-017  
**Bundle:** BT-GIT-13  
**Head observado:** `69b98cbd2466338574068898f7755e1f6f68b852`

#### Escopo

Uma alteração em teste, sem mudança de runtime.

#### Procedimento

1. Confirmar que o diff afeta apenas o teste.
2. Confirmar o hash do asset.
3. Confirmar a transformação SVG aplicada.
4. Confirmar a medida independente dos pixels.
5. Confirmar o limiar de luminância.
6. Confirmar a tolerância.
7. Confirmar as quatro larguras responsivas.
8. Confirmar preservação dos contratos anteriores.
9. Revisar os resultados de CI.
10. Confirmar que não há mudança em HTML/CSS/JS do Produto.
11. Integrar se o DoD do teste estiver satisfeito.
12. Reexecutar o gate de destino aplicável.
13. Registrar que fullscreen continua como contrato separado.

#### DoD

Teste de geometria integrado e ancorado no asset real; sem alegar cobertura de fullscreen que ele não possui.

---

### GIT-016 — Revisar e concluir PR #279 — dispatch UX-04

**Prioridade:** P1  
**Dependências:** TST-004/005, contrato UX-04  
**Bundle:** BT-GIT-14  
**Head observado:** `ffa288d181f0c53148e5a6b9ba69d3d8a5631651`

#### Escopo

Um workflow de CI para executar manualmente o gate existente em `development`.

#### Procedimento

1. Confirmar que o workflow corresponde ao blob pretendido.
2. Confirmar que o arquivo existe em `development`.
3. Confirmar que está ausente da `main` atual.
4. Confirmar que o workflow não modifica runtime.
5. Confirmar que usa permissões mínimas.
6. Confirmar que não requer Netlify.
7. Confirmar que o navegador utiliza fixture local.
8. Confirmar `workflow_dispatch`.
9. Confirmar como o ref de execução é selecionado.
10. Confirmar que a execução não aponta inadvertidamente para outro SHA.
11. Revisar o workflow como alteração isolada.
12. Integrar, se aprovado.
13. Confirmar disponibilização do dispatch.
14. Ler novamente o SHA de `development`.
15. Executar o gate no alvo autorizado.
16. Registrar resultado e evidência.
17. Não confundir disponibilização do botão com execução concluída.
18. Atualizar UX-04.

#### DoD

Workflow integrado e gate realmente executado no SHA correto, se o item tiver como entrega a validação UX-04 completa.

---

### GIT-017 — Revisar e concluir PR #280 — browser glass

**Prioridade:** P1  
**Dependências:** TST-006/007  
**Bundle:** BT-GIT-15  
**Head observado:** `ab2d378555afc96557a332cbb33c531c8133922f`

#### Escopo

Workflow mobile, fixture local e teste de oclusão.

#### Procedimento

1. Confirmar os três caminhos alterados.
2. Confirmar que não há mudança no runtime de produção.
3. Confirmar o novo modo de servir `/config/`.
4. Confirmar a porta efêmera.
5. Confirmar o lifecycle do servidor.
6. Confirmar readiness da configuração.
7. Confirmar 256 combinações.
8. Confirmar os quatro screenshots.
9. Confirmar checks de oclusão.
10. Confirmar ausência de vazamento de processos.
11. Executar browser no SHA exato.
12. Investigar falhas.
13. Confirmar que o teste não depende de autenticação hospedada.
14. Verificar o impacto do novo passo no workflow mobile.
15. Definir política de execução por paths.
16. Integrar somente após gate suficiente.
17. Revalidar no destino.

#### Estado de cautela

A API apresenta a PR como potencialmente mesclável, mas com `mergeable_state=unstable` na consulta deste turno.

Isso não estabelece a causa nem confirma uma falha específica.

O preflight deve consultar os checks antes de qualquer decisão.

#### DoD

Teste de oclusão executável e integrado, com fixture correta, teardown e resultado no head pertinente.

---

### GIT-018 — Revisar e concluir DS PR #119

**Prioridade:** P0/P1 documental  
**Dependências:** GIT-002, TST-002/004 na parte documental  
**Bundle:** BT-GIT-16  
**Baseline de entrada do plano (17/11/2026; não é pin vigente):** head observado `c4cff5e0b707ed728618f8ce1c60310eeca23fad`; o diff observado então continha 93 arquivos. O estado atual da PR, a contagem revisada e os resultados GIT-018 estão no [handover operacional de 19/11](../HANDOVER_CURRENT.md).

#### Objetivo

Consolidar na `main` do Design System as evidências e matrizes atuais sem importar afirmações obsoletas como status vigente.

#### Procedimento

1. Fixar base e head.
2. Conferir os caminhos no head corrente da #119; 93 é a contagem da baseline de 17/11, e a lista viva fica no handover.
3. Separar documentos de evidências brutas.
4. Identificar referências ao Produto.
5. Identificar SHAs históricos.
6. Confirmar que os documentos distinguem snapshots e estado atual.
7. Identificar afirmações que envelheceram após novas PRs.
8. Não reescrever evidências históricas só por mudança de data.
9. Atualizar somente o ponteiro operacional vigente.
10. Revisar o crosswalk ARC/G.
11. Revisar a matriz ARC-15.
12. Revisar o inventário ARC-13.
13. Verificar ligações entre documentos.
14. Verificar que decisões homologadas não foram alteradas.
15. Verificar que o pacote não contém código runtime do Produto.
16. Verificar que o status dos gates não foi promovido sem prova.
17. Verificar que o plano diretor não foi duplicado como segundo backlog de estado.
18. Executar checks documentais.
19. Integrar a documentação pertinente.
20. Fazer readback da `main` do Design System.
21. Atualizar seu handover canônico.
22. Encerrar a branch temporária somente após disposição segura.
23. Confirmar que o Design System retorna à meta de apenas `main`, se não houver outros trabalhos ativos.

#### DoD

Documentação atual integrada, evidência preservada e um único ponteiro operacional vigente.

---

## 10. Marco GIT-M4 — Governança de limpeza de branches

### GIT-019 — Auditar o mecanismo de branch hygiene

**Prioridade:** P0  
**Dependências:** GIT-001  
**Bundle:** BT-GIT-20

#### Objetivo

Preservar o mecanismo de segurança já desenvolvido, eliminando ambiguidades de autorização e replay.

#### Implementação existente

O Produto possui:

- `tools/branch_hygiene_observe.py`
- `tools/branch_hygiene_plan.py`
- `tools/branch_hygiene_apply.py`
- `tools/branch_hygiene_merged_pr_cleanup.py`
- `ops/branch-dispositions.json`
- `ops/branch-hygiene-batch.json`
- `.github/workflows/branch-hygiene.yml`
- `.github/workflows/branch-hygiene-bounded.yml`

O planner produz um plano determinístico com hash.

O executor bounded aceita lotes de uma a três refs com SHA exato.

O apply reobserva os refs, confirma proteções e relações com PRs, utiliza `--force-with-lease` e verifica readback.

Essas garantias são úteis e devem ser preservadas.

#### Procedimento

1. Identificar workflows ativos.
2. Identificar triggers de observação.
3. Identificar triggers de escrita.
4. Identificar quem fornece o batch.
5. Identificar quem aprova o batch.
6. Confirmar que o plano é hash-pinned.
7. Confirmar que a observação é atual.
8. Confirmar limites de um a três refs.
9. Confirmar proteções de `main`.
10. Confirmar proteções de `development`.
11. Confirmar proteção de heads de PR.
12. Confirmar proteção de bases de PR.
13. Confirmar evidência de ancestralidade.
14. Confirmar evidência de equivalência por squash.
15. Confirmar validação de tree.
16. Confirmar validação do merge commit.
17. Confirmar referências de workflows vivos.
18. Confirmar lease exato.
19. Confirmar readback.
20. Confirmar que não existe modo `delete all`.
21. Identificar comportamento de lote consumido.
22. Identificar efeitos de PRs fechadas.
23. Identificar divergências entre regra de segurança e autorização do usuário.
24. Registrar alterações propostas sem executar exclusões.

#### DoD

O mecanismo possui modelo de autorização claro, preserva seus gates atuais e não permite exclusão fora de escopo.

---

### GIT-020 — Resolver a política de exclusão automática pós-merge

**Prioridade:** P0  
**Tipo:** decisão de governança  
**Dependências:** GIT-019  
**Bundle:** BT-GIT-20

#### Diagnóstico

O workflow `branch-hygiene-bounded.yml` contém:

`cleanup-merged-pr-head`

Esse job pode executar após o fechamento com merge de PRs abrangidas por seus gatilhos.

O script `branch_hygiene_merged_pr_cleanup.py`:

1. Confirma identidade da PR.
2. Verifica que foi mesclada.
3. Confirma que o merge pertence à `main`.
4. Reobserva o inventário.
5. Confirma o SHA exato da origem.
6. Confirma ausência de proteção.
7. Confirma ausência de PRs abertas usando a ref.
8. Executa exclusão com lease.
9. Confirma readback.

Esses controles protegem contra diversas exclusões incorretas.

Mas o script não exige uma aprovação individual adicional no momento da exclusão.

#### Questão de política

Há duas políticas possíveis.

**Política A — Exclusão por aprovação explícita de lote.**

Nenhuma exclusão acontece sem autorização específica da ref ou do batch.

**Política B — Autorização permanente e delimitada.**

O usuário homologa previamente a exclusão automática de heads de PR após merge, desde que cumpram todos os critérios técnicos.

Ambas podem ser implementadas com segurança.

Entretanto, não devemos assumir que o merge de uma PR constitui autorização geral para apagar sua branch de origem.

#### Recomendação

**Adotar A como comportamento padrão até uma política permanente B ser explicitamente homologada.**

#### Procedimento

1. Identificar todos os triggers que podem chegar ao cleanup.
2. Identificar o efeito real do evento `closed`.
3. Identificar se o job é acionado em PRs comuns ou somente em arquivos de higiene.
4. Identificar se existe autorização específica anterior.
5. Registrar os limites dos mecanismos de segurança.
6. Separar elegibilidade técnica de autorização.
7. Propor execução `audit-only` por padrão.
8. Propor apply somente por lote ou autorização delegada.
9. Confirmar que nenhuma ref ativa seria apagada.
10. Testar eventos sintéticos.
11. Testar PR mesclada corretamente.
12. Testar PR fechada sem merge.
13. Testar ref movida.
14. Testar ref protegida.
15. Testar PR aberta usando a branch.
16. Testar commit merge inválido.
17. Testar tree divergente.
18. Testar autorização ausente.
19. Registrar a escolha homologada.
20. Integrar somente após aprovação.
21. Confirmar comportamento no workflow resultante.

#### DoD

Exclusão técnica e autorização possuem contratos separados, sem reduzir as proteções existentes.

---

### GIT-021 — Reconciliar batches consumidos e pins obsoletos

**Prioridade:** P1  
**Dependências:** GIT-019/020  
**Bundle:** BT-GIT-21

#### Diagnóstico atual

O batch versionado na `main` contém a branch:

`fix/home-hero-group-a11y-20261114`

no SHA:

`3481ade561deddf561de57225cf8a65491b34654`

Essa ref não aparece mais no inventário remoto atual.

O arquivo de disposições também contém histórico da branch antiga da PR #270.

Isso demonstra que nem todo registro no manifesto corresponde a uma branch viva.

Esse fato não é, por si só, uma inconsistência de segurança: o histórico pode ser útil.

O risco surge quando um lote consumido é reaplicado ou reapresentado como nova autorização.

#### Procedimento

1. Ler batch atual.
2. Ler disposições.
3. Observar refs vivas.
4. Separar refs presentes de ausentes.
5. Identificar batches aplicados.
6. Identificar receipts.
7. Confirmar que o apply falha fechado quando o lote não corresponde à observação.
8. Confirmar que batch antigo não é disparado em push não relacionado.
9. Confirmar que reedição do manifesto não reautoriza alvos.
10. Definir representação simples de lote consumido.
11. Evitar apagar evidência necessária.
12. Evitar criar banco de estado paralelo.
13. Testar idempotência e replays negativos.
14. Integrar eventual melhoria isoladamente.
15. Atualizar a documentação operacional.

#### DoD

Batches antigos não podem produzir exclusões novas nem estados enganosos, e sua proveniência continua disponível.

---

### GIT-022 — Consolidar a política de preservação e retirada de refs

**Prioridade:** P1  
**Dependências:** GIT-003/004/019/021  
**Bundle:** BT-GIT-21

#### Objetivo

Encerrar branches somente quando deixam de ter função operacional.

#### Critérios necessários

Uma ref só pode ser considerada elegível quando:

1. Não é `main`.
2. Não é `development` permanente.
3. Não está protegida.
4. Não é head ou base de PR aberta.
5. Seu conteúdo relevante foi incorporado ou recebeu disposição explícita.
6. Sua identidade atual corresponde ao SHA esperado.
7. Não há workflow vivo dependente dela.
8. Não há trabalho local não preservado vinculado à operação.
9. O método de integração está conhecido.
10. A prova de ancestralidade ou tree é válida.
11. Existe autorização aplicável.
12. O executor pode confirmar readback.

#### Procedimento

1. Gerar inventário novo.
2. Identificar candidatas.
3. Classificar conteúdo exclusivo.
4. Confirmar destino do conteúdo.
5. Confirmar PRs relacionadas.
6. Confirmar eventuais commits locais ainda não publicados, quando a operação os envolver.
7. Confirmar dependência de workflow.
8. Confirmar política de autorização.
9. Criar batch limitado.
10. Executar audit-only.
11. Revisar recibo.
12. Solicitar/confirmar autorização apropriada.
13. Executar apply quando permitido.
14. Ler novamente a ref.
15. Confirmar ausência apenas da ref pretendida.
16. Confirmar `main`/`development` intactas.
17. Confirmar PRs restantes.
18. Registrar resultado.
19. Reconciliar o backlog e o histórico.

#### DoD

A limpeza é resultado de conclusão técnica, com autorização e prova de não perda de conteúdo relevante.

---

## 11. Marco GIT-M5 — Publicação, observabilidade e rollback

### GIT-023 — Formalizar o pipeline de publicação Netlify

**Prioridade:** P0/P1  
**Dependências:** GIT-010/011, TST-025  
**Bundle:** BT-GIT-30

#### Contexto atual

O arquivo `netlify.toml` declara:

```toml
[build]
  publish = "app"
  command = "npm run build"
  functions = "netlify/functions"
```

O mesmo arquivo define redirects para APIs e rotas legadas.

Portanto, a autoridade de publicação não é qualquer diretório de build local.

É o resultado de `npm run build` direcionado ao diretório `app`, conforme a configuração do Netlify.

#### Procedimento

1. Identificar site de produção.
2. Identificar branch de produção configurada.
3. Confirmar comando de build.
4. Confirmar diretório publicado.
5. Confirmar funções.
6. Confirmar redirects.
7. Confirmar variáveis necessárias, sem expor segredos.
8. Confirmar políticas de Deploy Preview.
9. Confirmar se o merge dispara publicação automaticamente.
10. Confirmar qual commit será publicado.
11. Executar build local.
12. Confirmar determinismo.
13. Confirmar integridade dos assets.
14. Confirmar páginas geradas.
15. Confirmar funções compiladas.
16. Confirmar ausência de mudanças inesperadas em arquivos versionados.
17. Executar gates pré-publicação.
18. Autorizar publicação quando necessária.
19. Confirmar resultado do deploy.
20. Confirmar commit e artefatos servidos.
21. Verificar rotas.
22. Verificar endpoint público.
23. Verificar CSS/JS efetivamente carregados.
24. Verificar assets de marca e imagem.
25. Executar smoke read-only.
26. Registrar resultado.
27. Não confundir READY do deploy com homologação visual ou funcional completa.

#### Política de previews

A meta é preservar recursos e evitar geração desnecessária de previews.

Isso implica:

- Preferir navegador local quando suficiente.
- Utilizar um Preview existente e alinhado ao head quando apropriado.
- Não criar sites adicionais apenas para contornar banda.
- Evitar pushes de teste que disparem previews sem necessidade.
- Agrupar alterações de um mesmo pacote antes de verificar hospedagem.
- Não eliminar provas necessárias apenas para reduzir previews.

#### DoD

O pipeline possui fonte, build, artefato, commit e ambiente rastreáveis; a publicação é distinguida da integração.

---

### GIT-024 — Formalizar rollback por classe de mudança

**Prioridade:** P0  
**Dependências:** GIT-006/010/023  
**Bundle:** BT-GIT-31

#### Objetivo

Permitir reversão localizada sem supor que todo problema é corrigido revertendo um commit.

#### Classes de rollback

| Classe | Estratégia inicial | Risco especial |
|---|---|---|
| CSS/tokens | Reverter pacote de estilos e recompilar | Cascata e consumidores |
| Header/HTML | Reverter fonte autoral e regenerar | HTML gerado e manifestos |
| Controlador JS | Reverter comportamento e testar listeners | Estado e foco |
| Catálogo `pt-BR` | Reverter chaves e consumidores do lote | Referências quebradas |
| Projeção pública | Reverter implementação, validar API | Compatibilidade de DTO |
| Preços públicos | Desativar publicação quando autorizado, revalidar API | Exposição pública já ocorrida |
| Auth | Restaurar política segura e validar permissões | Segurança de acesso |
| Schema/persistência | Plano específico de compatibilidade e recuperação | Dados já gravados |
| Assets | Restaurar arte aprovada e validar hashes | Referências e cache |
| CI | Restaurar workflow/teste, preservar evidências | Perda de proteção |
| Docs | Restaurar referência anterior | Ambiguidade de autoridade |
| Branch hygiene | Preservar objetos e recuperar ref quando possível | Exclusão de ref é operação destrutiva |

#### Procedimento

1. Definir o pacote.
2. Identificar artefatos alterados.
3. Identificar mudanças persistentes.
4. Identificar dependências externas.
5. Identificar usuários potencialmente afetados.
6. Identificar reversibilidade por commit.
7. Identificar reversibilidade por configuração.
8. Identificar reversibilidade por dados.
9. Definir teste de rollback.
10. Definir quais informações precisam ser preservadas antes da ação.
11. Não usar `reset --hard` ou force push como rollback padrão de branch compartilhada.
12. Não reverter schema persistido sem plano de compatibilidade.
13. Não tratar preço publicado como informação que nunca foi exposta após desligar a flag.
14. Não tratar exclusão de branch como operação recuperável sem verificar retenção dos objetos Git.
15. Executar reversão controlada se necessária e autorizada.
16. Executar readback.
17. Registrar incidente e decisão.
18. Atualizar DoD e histórico.

#### DoD

Cada pacote de integração possui rollback viável e específico, inclusive para efeitos que não podem ser revertidos por Git.

---

### GIT-025 — Consolidar a prontidão de release e handover

**Prioridade:** P0  
**Dependências:** GIT-011/018/023/024  
**Bundle:** BT-GIT-32

#### Objetivo

Permitir concluir um ciclo e retomá-lo sem perda de estado.

#### Procedimento

1. Identificar a versão ou milestone.
2. Listar IDs concluídos.
3. Listar IDs ainda em revisão.
4. Listar IDs bloqueados.
5. Listar mudanças publicadas.
6. Listar mudanças somente integradas.
7. Listar PRs ainda abertas.
8. Listar branches temporárias.
9. Identificar dependências pendentes.
10. Identificar riscos residuais.
11. Confirmar gates de release.
12. Confirmar integração dos contratos afetados.
13. Confirmar readback de publicação quando aplicável.
14. Identificar rollback por pacote.
15. Atualizar o índice operacional.
16. Atualizar a timeline.
17. Reconciliar o Design System.
18. Apontar para documentos históricos pertinentes.
19. Definir os próximos IDs em ordem preferencial.
20. Publicar um handover curto que referencie o plano e o DoD, sem duplicá-los.

#### DoD

O próximo agente consegue retomar o trabalho a partir de IDs, contratos, commits e pendências, sem reconstruir a história inteira.

---

## 12. Sequência de integração recomendada para o estado atual

A ordem a seguir considera as PRs observadas e as dependências de domínio.

### Janela 0 — Corrigir a autoridade operacional

Executar:

- GIT-001.
- GIT-002.
- GIT-003.
- GIT-004.
- GIT-005.

**Objetivo:** tornar claro o que está realmente pendente.

Essa etapa não exige deploy nem alteração de runtime.

### Janela 1 — Concluir pacotes de baixo acoplamento

Candidatos:

- #278 — teste de geometria.
- #279 — workflow manual UX-04.
- #280 — correção da fixture/browser, após validação.
- #119 do Design System — consolidação documental, após reconciliação.

São pacotes com escopo relativamente isolado.

A ordem exata entre eles pode ser ajustada conforme os gates.

Não é necessário esperar que todos sejam integrados para prosseguir em outras frentes.

### Janela 2 — Consolidar a navegação pública

Candidata:

- #269.

A mudança toca fonte autoral, controlador, CSS, HTML gerado e testes.

Deve seguir o contrato NAV-005 de primeira profundidade.

A revisão do head atual é mais importante do que repetir automaticamente a totalidade das matrizes históricas.

### Janela 3 — Consolidar contraste sem bloquear o restante

Candidata:

- #271.

O pacote contém quatro arquivos e uma justificativa técnica definida.

Entretanto, a configuração hospedada do Configurador continua sendo uma limitação real de validação.

O resultado deve ser dividido entre:

- Mudanças comprovadas no recorte.
- Consumidores não validados no ambiente necessário.
- Gates globais ainda pendentes.

Não declarar G2 concluído integralmente a partir da integração de uma correção parcial.

### Janela 4 — Consolidar ARC-13

Candidata:

- #274.

A sequência de integração importa porque mudanças em HTML/JS público podem afetar o inventário.

Se #269 entrar antes, o scanner deverá ser reconciliado com a nova árvore autoral.

Se #274 entrar antes, a etapa de localização precisará tratar o delta posterior.

A ordem mais simples tende a ser:

**estabilizar o markup principal relevante → regerar inventário → integrar a base ARC-13 → extrair textos em lotes.**

Isso evita que o inventário nasça desatualizado.

### Janela 5 — Fechar a integração seletiva de `development`

Após os pacotes atuais estarem classificados:

1. Priorizar diferenças funcionais exclusivas.
2. Extrair o que realmente pertence à `main`.
3. Preservar contratos de domínio.
4. Descartar workflows históricos obsoletos apenas após sua classificação.
5. Manter evidência de origem.
6. Não fazer merge global dos 434 commits.
7. Reconciliar o saldo por intenção.

### Janela 6 — Consolidar publicação e higiene

Somente após integração:

- Validar builds e readback.
- Confirmar estados do DoD.
- Encerrar PRs substituídas.
- Executar higiene das branches elegíveis e autorizadas.
- Atualizar o plano operacional.
- Publicar o handover curto.

---

## 13. Caminho crítico de integração

A estrutura de dependências pode ser resumida assim:

```text
GIT-001 — Snapshot atual
          │
          ▼
GIT-002 — Autoridade documental
          │
          ├───────────────┐
          ▼               ▼
GIT-003 — Dev delta   GIT-004 — PRs
          │               │
          └───────┬───────┘
                  ▼
GIT-005 — DAG de execução
                  │
                  ▼
GIT-006 — Pacotes
                  │
          ┌───────┴────────┐
          ▼                ▼
GIT-007 — Extração   GIT-009 — Contrato PR
          │                │
          ▼                ▼
GIT-008 — Reconciliar  GIT-010 — Preflight
          │                │
          └────────┬───────┘
                   ▼
           Integração seletiva
                   │
                   ▼
          GIT-011 — Readback
                   │
                   ▼
          GIT-023 — Publicação
                   │
                   ▼
          GIT-025 — Fechamento
```

A higiene deve funcionar como trilha paralela e condicionada:

```text
GIT-019 — Auditoria higiene
          │
          ▼
GIT-020 — Política de autorização
          │
          ▼
GIT-021 — Batches/pins
          │
          ▼
GIT-022 — Elegibilidade por ref
          │
          ▼
   Exclusão autorizada
          │
          ▼
  Readback e recibo
```

Uma branch não precisa ser excluída para considerar um componente integrado.

E um componente não precisa esperar a redução completa de branches para ser trabalhado.

---

## 14. Bundles de governança

### BT-GIT-00 — Autoridade e snapshot

Verifica:

- Repositório correto.
- SHAs.
- Branches.
- PRs.
- CI disponível.
- Deploy observado.
- Documentos vinculantes.
- Limitações de acesso.

### BT-GIT-01 — Reconciliação histórica

Verifica:

- Diff integral.
- Origem.
- Intenção.
- Equivalência.
- Contrato vigente.
- Destino.
- Conteúdo exclusivo.
- Testes existentes.
- Disposição.

### BT-GIT-02 — Integração por pacote

Verifica:

- Coesão técnica.
- Dependências.
- Branch-alvo.
- Contratos afetados.
- Escopo negativo.
- Tests.
- Rollback.

### BT-GIT-03 — Extração e atualização de base

Verifica:

- Proveniência.
- Semântica.
- Compatibilidade.
- Ausência de dependência obsoleta.
- Diff final.
- CI do novo SHA.

### BT-GIT-04 — Merge e readback

Verifica:

- Preflight.
- Required checks.
- Aprovações.
- SHA integrado.
- CI pós-merge.
- Conteúdo integrado.
- Status DoD.

### BT-GIT-10…16 — Pacotes específicos de PR

Cada pacote usa os testes da frente técnica correspondente.

Não cria uma suite de navegador independente apenas para governança.

### BT-GIT-20 — Branch hygiene

Verifica:

- Autorização.
- Proteção.
- SHA exato.
- PRs abertas.
- Ancestralidade/tree.
- Workflows vivos.
- Lease.
- Readback.

### BT-GIT-21 — Idempotência e disposição

Verifica:

- Batches consumidos.
- Manifestos históricos.
- Refs ausentes.
- Reexecução negativa.
- Ausência de exclusão por contagem.

### BT-GIT-30 — Publicação

Verifica:

- Build.
- Artefato.
- Commit.
- Redirects.
- Assets.
- APIs.
- Deploy.
- Smoke.

### BT-GIT-31 — Rollback

Verifica:

- Tipo de mudança.
- Reversibilidade.
- Dados persistidos.
- Contrato de recuperação.
- Readback.

### BT-GIT-32 — Encerramento

Verifica:

- IDs e DoD.
- Milestones.
- Histórico.
- PRs.
- Branches.
- Publicação.
- Próxima sequência.

---

## 15. Modelo de decisão GO/HOLD

A decisão deve ser específica por pacote.

| Situação | Decisão |
|---|---|
| Testes suficientes passaram no head correto | GO técnico, sujeito às demais condições |
| Teste relevante não foi executado | HOLD para o critério correspondente |
| Fixture local passou, runtime hospedado exigido não foi validado | GO apenas para escopo que a fixture comprova |
| PR com base desatualizada | Reconciliar e revalidar |
| Alteração fora de escopo | Separar ou justificar |
| Testes verdes, contrato homologado violado | HOLD |
| Alteração segura mas publicação ainda pendente | Integração concluída; publicação pendente |
| Deploy READY, conteúdo não validado | Deploy concluído; contrato funcional ainda pendente |
| Branch integrada mas conteúdo exclusivo não classificado | HOLD para exclusão |
| Branch elegível sem autorização para exclusão | HOLD para operação destrutiva |
| Documento concluído mas status Git não atualizado | Documentação pronta; integração documental pendente |

**GO/HOLD não substitui o status do DoD.**

GO/HOLD é uma decisão em um gate.

O status registra a situação global do item.

---

## 16. Matriz de riscos da governança

| Risco | Severidade | Mitigação |
|---|---|---|
| Merge global de `development` | Alta | Extração por contrato |
| PR verde com teste relevante ausente | Alta | Matriz assertion→risco→trigger |
| Exposição pública de dados privados | Crítica | DTO allowlisted, auth e gates negativos |
| Exclusão de ref ativa | Alta | Batch, SHA, autorização e readback |
| Lote consumido reaplicado | Alta | Fail-closed e idempotência |
| Merge baseado em documento histórico | Média/alta | Snapshot e autoridade atual |
| Duplicação de implementação | Média | Owner único e crosswalk |
| Fragmentos HTML divergentes | Média | ARC-03C e teste de drift |
| Tokens não consumidos pelo browser | Média | CSSOM/build/deploy readback |
| Preview com commit diferente | Alta para validação | Verificação de identidade do deploy |
| Excesso de documentação concorrente | Média | DoD canônico e referências |
| CI longa por invocações repetidas | Média | Seleção por impacto |
| Golden atualizado para mascarar diferença | Alta | Referência aprovada independente |
| Rollback insuficiente após gravação | Alta/crítica | Plano por tipo de alteração |
| Branch removida sem preservar conteúdo | Alta | Disposição/proveniência prévia |

---

## 17. Métricas de governança

A eficiência não deve ser medida apenas pelo número de branches.

### 17.1 Métricas recomendadas

- PRs abertas por tempo e estado.
- Pacotes integrados por período.
- Tempo médio de preflight.
- Tempo entre aprovação e merge.
- Frequência de rebase/reconciliação.
- Falhas pós-merge.
- Tempo de rollback.
- PRs substituídas sem disposição.
- Branches temporárias sem tarefa ativa.
- Contratos com autoridade concorrente.
- Tarefas com evidência insuficiente.
- Tarefas concluídas sem integração.
- Deploys por pacote.
- Previews por pacote.
- Tempo gasto reconstruindo contexto.
- Tempo gasto repetindo testes.
- Bloqueios de fixture.
- Tarefas em `blocked` por dependência real.
- Cobertura do DoD.
- Divergência funcional residual de `development`.

### 17.2 Métrica central recomendada

A métrica mais útil para avaliar esta reestruturação será:

**percentual de entregas do backlog cujo resultado pode ser verificado e retomado sem depender da interpretação de conversas anteriores.**

Ela representa diretamente o problema que o novo método pretende resolver.

Deve ser calculada a partir de IDs com critérios e evidências, não de declarações narrativas de conclusão.

---

## 18. DoD específico da frente Git e integração

Um pacote GIT somente poderá receber `done` quando:

1. O escopo estiver delimitado.
2. A origem estiver identificada.
3. A autoridade da decisão estiver clara.
4. A branch-alvo estiver definida.
5. As dependências estiverem satisfeitas.
6. Os testes aplicáveis tiverem sido executados.
7. Os controles negativos pertinentes tiverem passado.
8. O rollback estiver estabelecido.
9. A integração estiver comprovada, quando envolver alteração de código.
10. A publicação estiver comprovada, quando for parte da entrega.
11. A PR tiver sido encerrada ou sua continuidade estiver explicitamente justificada.
12. O backlog tiver sido atualizado.
13. A timeline tiver recebido a transição.
14. As referências e evidências permitirem retomada independente.

Uma tarefa de auditoria pode ser concluída com documento integrado e validado.

Uma tarefa de código não é concluída apenas porque a PR está pronta.

Uma tarefa de publicação não é concluída apenas porque a `main` contém o commit.

Uma tarefa de higiene não é concluída apenas porque o planner classifica a ref como elegível.

---

## 19. Pontos de interrogação

| ID | Questão | Método de resolução |
|---|---|---|
| GIT-Q01 | Quais mudanças dos 434 commits exclusivos continuam relevantes? | Inventário por contrato e intenção |
| GIT-Q02 | Qual parte da `development` já está semanticamente absorvida na `main`? | Comparação por comportamento e provenance |
| GIT-Q03 | Quais workflows exclusivos da `development` devem ser promovidos? | Matriz ARC-15 e custo/benefício |
| GIT-Q04 | Qual conjunto de required checks protege a `main`? | Consulta de rulesets com acesso apropriado |
| GIT-Q05 | Qual a ordem exata de integração de #269/#271/#274? | DAG e contratos afetados |
| GIT-Q06 | Quais pendências da #271 exigem realmente runtime hospedado? | Matriz por consumer e estado |
| GIT-Q07 | A #280 já passou seu replay completo no head atual? | Verificar run e artefatos |
| GIT-Q08 | O inventário ARC-13 precisa ser regenerado após NAV-005? | Diff de fontes e scanner |
| GIT-Q09 | A #119 está pronta para substituir o handover obsoleto da main DS? | Revisão documental e crosswalk |
| GIT-Q10 | Quais branches históricas ainda são referenciadas por workflows? | Busca e observação Git |
| GIT-Q11 | A exclusão automática pós-merge possui autorização permanente homologada? | Decisão explícita de política |
| GIT-Q12 | Como representar batches consumidos sem sistema de estado adicional? | Recibos e validação de idempotência |
| GIT-Q13 | Qual configuração efetiva do Netlify gera previews automaticamente? | Consulta da configuração do site |
| GIT-Q14 | Quais operações de produção exigem rollback não-Git? | Matriz de persistência |
| GIT-Q15 | Como garantir que uma PR merged não permaneça aberta em status no backlog? | Protocolo de transição e readback |
| GIT-Q16 | Quando uma alteração na `development` deve ser promovida diretamente à `main`? | Contrato, maturidade e gates |
| GIT-Q17 | Quais documentos podem ser substituídos por ponteiros, preservando história? | Inventário de autoridade documental |
| GIT-Q18 | O plano final terá algum gate que dependa exclusivamente de documentação desatualizada? | Auditoria cruzada dos IDs |

---

## 20. Critérios de interrupção

Interromper a integração quando:

- A branch ou o SHA mudou desde o preflight sem nova verificação.
- A alteração inclui conteúdo de contrato não identificado.
- Uma decisão visual homologada foi substituída silenciosamente.
- O merge introduz código histórico de autenticação não validado.
- O diff não corresponde ao escopo declarado.
- O required check relevante não foi executado.
- A fixture não reproduz o consumidor necessário.
- Um teste foi flexibilizado para obter verde sem corrigir a causa.
- A `main` seria substituída por uma árvore de `development` sem reconciliação.
- O build altera assets versionados inesperadamente.
- A publicação usa um commit diferente do aprovado.
- O rollback depende de ação destrutiva não autorizada.
- Uma branch está elegível tecnicamente para exclusão, mas falta autorização.
- A operação tenta reaplicar batch consumido.
- Não existe prova de preservação do conteúdo exclusivo.
- O status do backlog seria atualizado com base apenas em uma narrativa.

Interromper o pacote não implica paralisar todo o programa.

O agente deve registrar o bloqueio no ID correspondente e prosseguir com entregas independentes quando possível.

---

## 21. Parecer final — Parte VII

A fase de consolidação histórica de branches foi produtiva.

Ela transformou um conjunto muito grande de linhas de desenvolvimento em uma estrutura significativamente mais controlável.

Mas sua próxima evolução não deve repetir o mesmo método indefinidamente.

Com oito branches no Produto, seis delas associadas a PRs abertas, e apenas duas branches no Design System, a principal dificuldade deixou de ser quantidade de refs.

Agora é **converter trabalho acumulado em integração efetiva, sem perder proveniência, testes e autoridade**.

Minha recomendação é:

1. Preservar `main` e `development` como branches permanentes.
2. Evitar merge global dos 434 commits exclusivos da `development`.
3. Classificar a divergência por intenção e contrato.
4. Priorizar PRs e pacotes já maduros.
5. Integrar com gates proporcionais ao risco.
6. Registrar readback em cada destino.
7. Atualizar uma única fonte operacional de status.
8. Consolidar o Design System sem criar outra lista concorrente de progresso.
9. Manter o mecanismo de higiene, mas revisar sua política de autorização automática.
10. Reduzir branches como consequência natural do encerramento do trabalho.
11. Evitar publicações ou previews que não acrescentem evidência necessária.
12. Encerrar cada ID somente com DoD satisfeito.

A grande mudança metodológica é simples:

**O Git deve registrar a história. O plano deve orientar a execução. Os testes devem comprovar os contratos. O DoD deve informar o estado.**

Nenhum desses instrumentos precisa substituir os demais.

---

### Fontes técnicas principais

#### Repositórios e decisões

- [Produto](https://github.com/EAKerber/MobiliPresenter2D)
- [Design System](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem)
- [Decisões D01–D04](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/APPROVALS_D01_D04_2026-10-26.md)
- [Handover development](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/handoffs/HANDOVER_DEVELOPMENT_2026-10-27.md)
- [Crosswalk ARC/G](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARCHITECTURE_EXECUTION_CROSSWALK_2026-11-15.md)

#### PRs abertas

- [Produto #269 — NAV-005](https://github.com/EAKerber/MobiliPresenter2D/pull/269)
- [Produto #271 — DS-04](https://github.com/EAKerber/MobiliPresenter2D/pull/271)
- [Produto #274 — ARC-13](https://github.com/EAKerber/MobiliPresenter2D/pull/274)
- [Produto #278 — geometria do hero](https://github.com/EAKerber/MobiliPresenter2D/pull/278)
- [Produto #279 — dispatch UX-04](https://github.com/EAKerber/MobiliPresenter2D/pull/279)
- [Produto #280 — teste glass](https://github.com/EAKerber/MobiliPresenter2D/pull/280)
- [Design System #119 — status arquitetural](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/119)

#### Higiene de branches

- [Observação](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tools/branch_hygiene_observe.py)
- [Plano](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tools/branch_hygiene_plan.py)
- [Apply](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tools/branch_hygiene_apply.py)
- [Cleanup pós-merge](https://github.com/EAKerber/MobiliPresenter2D/blob/main/tools/branch_hygiene_merged_pr_cleanup.py)
- [Workflow bounded](https://github.com/EAKerber/MobiliPresenter2D/blob/main/.github/workflows/branch-hygiene-bounded.yml)
- [Batch versionado](https://github.com/EAKerber/MobiliPresenter2D/blob/main/ops/branch-hygiene-batch.json)
- [Disposições](https://github.com/EAKerber/MobiliPresenter2D/blob/main/ops/branch-dispositions.json)

#### Publicação

- [Configuração Netlify](https://github.com/EAKerber/MobiliPresenter2D/blob/main/netlify.toml)
- [Autoridade de CI/build](https://github.com/EAKerber/MobiliPresenter2D/blob/main/docs/architecture/ci-authority-contract-2026-10-05.md)

**Limite de evidência:** os estados de Git, branches, PRs e diffs foram consultados diretamente nesta etapa. Nenhum merge, push, exclusão, workflow dispatch, alteração de regras ou deploy foi realizado. Configurações efetivas do site Netlify e required checks não foram revalidadas nesta consulta; o plano trata esses pontos como questões abertas.

---

<a id="capitulo-8"></a>
# Capítulo VIII — Backlog mestre, dependências globais, marcos, DoD e acompanhamento

## 1. Sumário executivo

As sete partes anteriores examinaram o mesmo problema sob diferentes perspectivas:

- O método histórico criou evidências valiosas, mas também documentação e checkpoints dispersos.
- A arquitetura homologada já contém decisões adequadas que ainda precisam ser plenamente aplicadas.
- Tokens, CSS e componentes possuem oportunidades reais de centralização.
- Há componentes e mecanismos compartilhados que não precisam ser reconstruídos.
- O Core V5 possui fronteiras importantes de domínio, publicação e autorização que devem ser preservadas.
- A infraestrutura de testes é extensa, mas sua relação com os contratos e o processo de integração ainda pode melhorar.
- O Git está mais organizado que antes, porém há trabalho acumulado que ainda precisa chegar às branches e aos consumidores corretos.

A conclusão integrada é:

**O programa não necessita de uma nova arquitetura fundamental. Necessita de uma estratégia muito mais eficiente para fechar, integrar e verificar a arquitetura já definida.**

A resposta, portanto, não será uma grande refatoração.

Será uma sequência de pacotes com escopo, dependências, contratos e testes bem definidos.

### 1.1 Resultado que consideraremos sucesso

O resultado final não será medido pela quantidade de arquivos apagados, branches reduzidas ou tokens criados.

Será medido pela capacidade de:

1. Identificar uma mudança necessária.
2. Encontrar sua autoridade.
3. Encontrar todos os consumidores relevantes.
4. Alterar o mínimo necessário.
5. Executar os testes corretos.
6. Integrar sem conflito com trabalhos independentes.
7. Verificar o resultado na branch e no ambiente corretos.
8. Registrar sua conclusão.
9. Retomar o trabalho sem depender da memória de um agente anterior.

---

## 2. Decisões consolidadas

### 2.1 A arquitetura homologada é ponto de partida

ARC-01…16, VIS-002, NAV-005 e as decisões D01–D04 não devem ser reabertas sem conflito real ou novo requisito.

Um código divergente deve ser reconciliado com a decisão.

A mera existência de uma implementação divergente não revoga a homologação.

### 2.2 Centralização visual deve produzir uma fonte de verdade

A centralização das cores é um objetivo explícito do programa.

O Design System deve fornecer a autoridade canônica dos valores aprovados.

A distribuição desses valores deve permitir que alterações homologadas sejam propagadas aos consumidores correspondentes.

É necessário distinguir:

- Valor cromático canônico.
- Papel semântico.
- Variante de tema ou estado.
- Consumidor efetivo.

Cores numericamente iguais podem representar papéis diferentes.

A centralização não deve obrigá-las a continuar iguais quando seus significados divergem.

Também não existe objetivo de substituir cada literal CSS por uma variável indiscriminadamente.

O critério é **autoridade única, propagação previsível e exceções justificadas**.

### 2.3 Simplificação não significa redução arbitrária de arquivos

Um conjunto maior de arquivos com ownership claro pode ser melhor do que um arquivo monolítico.

Um conjunto menor também pode ser melhor quando elimina duplicação desnecessária.

A decisão será tomada por:

- Responsabilidade.
- Acoplamento.
- Número de autoridades.
- Facilidade de mudança.
- Risco de regressão.
- Custo real de manutenção.

### 2.4 Código, integração e publicação são estados diferentes

**Nota de governança v0.9:** no Produto, a `development` é buffer de estabilização e a promoção à `main` depende de contrato e DoD por pacote, sem merge global de seu histórico. A política completa consta na seção 5.5 do Capítulo VII; a integração do plano à `main` do Design System é recomendada assim que a revisão documental permitir.


Para mudanças relevantes, os recibos devem distinguir:

1. Presença no código.
2. Integração na branch-alvo.
3. Inclusão no artefato publicado.
4. Consumo efetivo pelo navegador.
5. Validação do comportamento esperado.

A existência de um pin, manifesto, import ou arquivo não substitui essas verificações.

### 2.5 O Core V5 permanece a autoridade de domínio

Não reescrever o schema por razões visuais.

Preservar:

- Publicação autenticada.
- Revisão e ETag.
- Readback.
- Projeção Buyer.
- Projeção pública.
- Allowlist.
- Contratos de preço.
- Autorização.
- Compatibilidade histórica necessária.

As interfaces podem compartilhar componentes sem compartilhar indevidamente as mesmas permissões ou políticas de dados.

### 2.6 O backlog é um complemento do plano

Este documento não substitui as explicações das Partes I–VII.

O backlog transforma essas explicações em uma lista operacional ordenada.

O DoD determina o que significa concluir cada item.

A timeline registra transições de estado e evidência.

O Git continua registrando a história de implementação.

Nenhuma dessas funções precisa duplicar as demais.

---

## 3. Convenções do backlog

### 3.1 Identidade

Cada item possui ID estável.

A ordem preferencial de execução pode mudar.

O ID não muda apenas porque a prioridade mudou.

### 3.2 Estados permitidos

| Estado | Significado |
|---|---|
| `not_started` | Nenhuma execução formal do item foi iniciada |
| `in_progress` | Trabalho ativo de execução |
| `blocked` | Existe impedimento real que inviabiliza avançar ou concluir |
| `in_review` | Resultado produzido, aguardando validação ou integração |
| `done` | DoD aplicável satisfeito e evidenciado |
| `cancelled` | Escopo retirado, substituído ou absorvido com justificativa |

**Estado inicial padrão dos novos registros deste plano: `not_started`.**

Isso não significa que o código subjacente não exista.

Por exemplo, um ticket de consolidar o renderer de cena pode começar como `not_started`, mesmo que o renderer já esteja implementado.

A primeira operação do ticket será reconciliar o que já existe e determinar o trabalho residual.

Não atribuir `done` apenas porque uma função está presente na `main`.

### 3.3 Prioridades

**P0:** contrato de segurança, autoridade, bloqueio importante ou infraestrutura necessária para continuar.

**P1:** integração arquitetural relevante ou correção importante com benefício operacional claro.

**P2:** melhoria incremental, redução de atrito ou consolidação que não impede trabalho essencial.

A prioridade não deve confundir importância de longo prazo com urgência de execução.

### 3.4 Dependências

Toda dependência deve indicar seu tipo:

- `hard`: impossível cumprir o DoD sem ela.
- `test`: necessária para validar determinado critério.
- `integration`: necessária para incorporar ao destino.
- `decision`: exige homologação.
- `soft`: ordem preferida, não bloqueante.

O campo não deve conter apenas uma lista de IDs sem explicar o tipo de relação.

---

## 4. Backlog mestre em ordem preferencial

A lista abaixo reúne **125 IDs**, incluindo tarefas de método, revisão arquitetural, implementação, verificação, integração e consolidação documental.

Esses IDs não representam 137 PRs nem 137 alterações independentes.

Vários pertencem ao mesmo pacote técnico.

**Reconciliação editorial:** os 125 IDs abaixo correspondem a tarefas efetivamente descritas nos capítulos I, III–VIII. Os doze identificadores `AR2-01`…`AR2-12` que apareciam na versão preliminar da Parte VIII foram retirados do backlog porque a Parte II contém análises ARC, não doze tarefas com esses IDs. Suas obrigações permanecem expressas nas decisões ARC-01…16 e nas tarefas correspondentes. Os rótulos `MD` e `RM` foram normalizados e os títulos das tarefas seguem suas fontes originais.

### Onda 0 — Autoridade, método e prevenção de trabalho acidental

**Objetivo:** garantir que os próximos pacotes sejam executados sobre a base correta, com risco controlado e sem disparar publicações desnecessárias.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 001 | GIT-001 | Criar snapshot operacional dos repositórios | P0 |
| 002 | OPS-NET-001 | Avaliar desativação dos Deploy Previews automáticos | P0 |
| 003 | GIT-002 | Consolidar a hierarquia documental | P0 |
| 004 | MD-001 | Congelar o inventário de referência | P0 |
| 005 | MD-002 | Consolidar a cadeia ARC → entrega → consumidor | P0 |
| 006 | MD-003 | Recalibrar métricas | P0 |
| 007 | MD-004 | Auditar os 21 comandos e 21 workflows do baseline ARC-15 | P0 |
| 008 | MD-005 | Validar a infraestrutura dos browsers | P0 |
| 009 | MD-006 | Resolver a estratégia de fixture autenticada | P0 |
| 010 | MD-007 | Classificar as PRs atualmente abertas | P1 |
| 011 | MD-008 | Estabelecer política de reconciliação `main` ↔ `development` | P0 |
| 012 | MD-009 | Decompor G2/DS-05A em bloqueios localizados | P1 |
| 013 | MD-010 | Selecionar o primeiro pacote vertical de componentes/tokens | P0 |
| 014 | RM-01 | Criar uma única unidade executável de planejamento | P0 |
| 015 | RM-02 | Substituir documentação narrativa repetida por registros estruturados | P0 |
| 016 | RM-03 | Utilizar bundles de teste por domínio de mudança | P1 |
| 017 | RM-04 | Separar prova local de prova hospedada | P0 |
| 018 | RM-05 | Tornar a integração uma etapa planejada desde o início | P0 |
| 019 | TST-001 | Fixar baseline e mapa de execução | P0 |
| 020 | TST-002 | Construir matriz assertion → contrato → risco | P0 |
| 021 | TST-004 | Auditar alcançabilidade dos workflows | P0 |
| 022 | TST-005 | Determinar required checks e política de status | P0 |
| 023 | GIT-004 | Inventariar a intenção das PRs abertas | P0 |
| 024 | GIT-019 | Auditar o mecanismo de branch hygiene | P0 |
| 025 | GIT-020 | Resolver a política de exclusão automática pós-merge | P0 |

#### Marco O0 — Execução controlada

Critérios de saída:

- Fontes de autoridade identificadas.
- Política de preview avaliada, ainda que sua implementação dependa de decisão.
- Estado de Git registrado.
- PRs abertas identificadas.
- Required checks conhecidos ou explicitamente `UNKNOWN`.
- Política de exclusão automática revisada.
- Padrão operacional de DoD definido.

**Não é necessário concluir todas as melhorias metodológicas da Onda 0 para iniciar um pacote de baixo risco já suficientemente delimitado.**

Os bloqueios devem ser aplicados somente onde há dependência real.

---

### Onda 1 — Arquitetura, domínio de responsabilidade e integração

**Objetivo:** associar decisões a autoridades e desenhar as integrações com menor risco.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 026 | GIT-003 | Classificar a divergência `development` versus `main` | P0 |
| 027 | GIT-005 | Criar o DAG de dependências entre pacotes | P0 |
| 028 | GIT-006 | Definir unidade mínima de integração | P0 |
| 029 | GIT-007 | Formalizar extração seletiva com proveniência | P0 |
| 030 | GIT-008 | Definir a política de reconciliação com `main` | P0 |
| 031 | GIT-009 | Criar contrato operacional para PRs | P0 |
| 032 | GIT-010 | Formalizar o preflight de merge | P0 |
| 033 | GIT-011 | Formalizar o readback pós-merge | P0 |
| 034 | CMP-001 | Criar o inventário operacional dos componentes | P0 |
| 035 | DOM-001 | Inventário executável dos contratos V5 | P0 |
| 036 | DOM-002 | Distinguir autoria, projeção e estado transitório | P0 |
| 037 | GIT-018 | Revisar e concluir DS PR #119 | P1 |

#### Marco O1 — Contratos executáveis

Critérios de saída:

- Cada família prioritária possui fonte, owner e consumidores.
- Diferenças relevantes de `development` possuem disposição.
- A integração não depende de um merge global.
- PRs recebem IDs, dependências e testes.
- O Design System tem uma via de atualização documental sem status concorrente.

A matriz ARC deve ser considerada uma estrutura de referência, não uma segunda fila de execução.

---

### Onda 2 — Cores, tokens, CSS e foundations

**Objetivo:** centralizar a identidade visual aprovada e provar seu consumo efetivo.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 038 | TOK-00 | Endurecer o contrato DS → Produto | P0 |
| 039 | TOK-01 | Reconciliar VIS-002C v0.3 | P0 |
| 040 | TOK-02 | Fechar P-TOKEN-02A1 e distinguir o alias da conformidade visual | P0 |
| 041 | TOK-03 | Selecionar o primeiro novo token compartilhado | P1 |
| 042 | CSS-00 | Reconstruir a baseline CSS atual | P0 |
| 043 | CSS-01 | Classificar os 98 pares incertos | P1 |
| 044 | CSS-02 | Reconciliar e concluir a PR #271 | P1 |
| 045 | CSS-03 | Resolver `.module-number` | P1 |
| 046 | CSS-04 | Resolver `#viewerHint` separadamente | P1 |
| 047 | CSS-05 | Fechar o restante do DS-04 por causa técnica | P1 |
| 048 | FND-01 | Extrair a primeira primitiva neutra | P1 |
| 049 | FND-02 | Contratos de estados visuais | P1 |
| 050 | FND-03 | Famílias CSS compartilhadas de risco crescente | P1 |
| 051 | TST-016 | Consolidar contraste e CSSOM por contexto | P0/P1 |

#### Marco O2 — Fonte visual coerente

Critérios de saída:

- Fonte de cores aprovada identificada.
- Tokens e papéis semânticos consistentes.
- Propagação demonstrada nos consumidores previstos.
- Exceções explícitas.
- Estados visualmente relevantes verificados.
- Ausência de alterações acidentais em componentes não homologados.

**Não exigir G2 global totalmente encerrado para permitir a integração de uma família que possui evidência suficiente e rollback independente.**

---

### Onda 3 — Composição pública, navegação e componentes

**Objetivo:** consolidar mecanismos compartilhados existentes e corrigir suas variantes.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 052 | CMP-002 | Consolidar ARC-03C como autoridade das três páginas | P0 |
| 053 | CMP-003 | Consolidar o controlador único do menu público | P0 |
| 054 | CMP-004 | Fechar NAV-005 para o header público primário | P0 |
| 055 | GIT-012 | Revisar e concluir PR #269 — NAV-005 | P0 |
| 056 | TST-012 | Consolidar o bundle de navegação pública | P1 |
| 057 | CMP-005 | Consolidar o header secundário do Viewer | P0 |
| 058 | CMP-018 | Auditar inicialização, atualização e descarte | P1 |
| 059 | CMP-007 | Consolidar o mecanismo de tema e os slots de inserção | P1 |
| 060 | TST-015 | Fortalecer os testes do tema | P1 |
| 061 | CMP-008 | Consolidar a identidade da marca | P1 |
| 062 | CMP-009 | Definir famílias de botões por contrato, não por classe | P2 |
| 063 | CMP-010 | Consolidar feedback de interface respeitando sua finalidade | P2 |
| 064 | CMP-011 | Revisar o piloto declarativo da Landing | P2 |
| 065 | CMP-012 | Consolidar o carrossel e a seleção de ambientes | P2 |
| 066 | CMP-013 | Consolidar o painel expansível de Como funciona | P1 |
| 067 | CMP-019 | Formalizar o limite entre build-time e runtime | P1 |
| 068 | TST-017 | Separar provas geométricas de provas visuais | P1 |
| 069 | GIT-015 | Revisar e concluir PR #278 — geometria do hero | P1 |
| 070 | TST-019 | Estabelecer política de screenshots e referências visuais | P1 |
| 071 | TST-021 | Cobrir interações acessíveis não verificadas | P1 |

#### Marco O3 — Componentes públicos consolidados

Critérios de saída:

- Páginas primárias geradas de fonte autoral correta.
- Menu público com controlador único.
- Viewer com variante NAV-005 homologada.
- Marca e tema consistentes.
- Componentes editoriais sem duplicação indevida.
- Testes acessíveis e visuais associados aos consumidores.
- Nenhuma introdução de renderer universal de páginas.

---

### Onda 4 — Core V5, ferramentas e testes de domínio

**Objetivo:** consolidar os contratos comerciais e sua aplicação no Admin, Configurador e Viewer.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 072 | DOM-003 | Consolidar a leitura da configuração publicada | P0 |
| 073 | DOM-004 | Consolidar publicação V5, revisão e ETag | P0 |
| 074 | TST-009 | Fechar a cobertura de publicação V5 | P0 |
| 075 | DOM-005 | Encerrar o alcance dos caminhos históricos V3/V4 | P1 |
| 076 | DOM-006 | Consolidar `NormalizedConfiguratorFlow` | P1 |
| 077 | DOM-007 | Consolidar projeções responsivas e componentes de seção | P1 |
| 078 | DOM-008 | Consolidar o contrato de precificação tipada | P0/P1 |
| 079 | DOM-009 | Consolidar a autoria de dados no Admin | P1 |
| 080 | DOM-010 | Consolidar a autorização de preços base no Viewer | P0 |
| 081 | TST-011 | Fechar cobertura da projeção pública e preços | P0 |
| 082 | DOM-011 | Fortalecer o endpoint Buyer e a fixture autorizada | P0 |
| 083 | TST-006 | Consolidar o servidor local Buyer V5 | P0 |
| 084 | DOM-012 | Consolidar o Viewer como consumidor público restrito | P1 |
| 085 | DOM-013 | Consolidar políticas de acesso por superfície | P0 |
| 086 | TST-010 | Fechar cobertura de autorização e sessão | P0 |
| 087 | CMP-006 | Formalizar a fronteira do header privado | P1 |
| 088 | CMP-014 | Formalizar o contrato compartilhado de cena e hotspots | P1 |
| 089 | CMP-015 | Consolidar componentes de apresentação do Configurador | P1 |
| 090 | CMP-016 | Preservar a especialização do Viewer e consolidar seus componentes | P1 |
| 091 | CMP-017 | Consolidar controles do Admin por significado | P1 |
| 092 | DOM-014 | Consolidar as fronteiras Core / apresentação | P1 |
| 093 | TST-013 | Consolidar teclado e foco do Configurador | P1 |
| 094 | TST-014 | Consolidar os testes de layout responsivo e PiP | P1 |
| 095 | TST-007 | Corrigir e integrar o browser de vidro/oclusão | P1 |
| 096 | TST-008 | Isolar testes que alteram arquivos durante a execução | P1 |
| 097 | GIT-013 | Revisar e concluir PR #271 — DS-04 | P0/P1 |
| 098 | GIT-016 | Revisar e concluir PR #279 — dispatch UX-04 | P1 |
| 099 | GIT-017 | Revisar e concluir PR #280 — browser glass | P1 |

#### Marco O4 — Domínio preservado e interfaces integradas

Critérios de saída:

- Publicação V5 segura.
- Autorização preservada.
- Preços calculados pelo Core.
- Preços públicos sujeitos à permissão persistida.
- Fixture Buyer válida.
- Viewer restrito ao DTO público.
- Renderers e componentes sobre contratos existentes.
- Nenhuma duplicação de autoridade comercial.

Nem todos os itens desta onda dependem uns dos outros.

A disposição em uma mesma fase reflete proximidade técnica, não autorização para reuni-los em uma única PR.

---

### Onda 5 — ARC-13 e localização

**Objetivo:** transformar o inventário de textos em uma fonte canônica consumida pelo Produto.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 100 | LOC-001 | Consolidar o inventário ARC-13 | P0 |
| 101 | LOC-002 | Classificar textos por autoridade e função | P0 |
| 102 | GIT-014 | Revisar e concluir PR #274 — ARC-13 | P1 |
| 103 | LOC-003 | Definir o catálogo canônico `pt-BR` | P1 |
| 104 | LOC-004 | Extrair textos dos fragmentos e páginas estáticas | P1 |
| 105 | LOC-005 | Extrair textos de controladores e componentes JS | P1 |
| 106 | LOC-006 | Extrair textos do Admin e Configurador sem migrar conteúdo comercial | P1/P2 |
| 107 | TST-020 | Verificar cobertura de localização por consumidor | P1 |
| 108 | LOC-007 | Automatizar verificação de chaves e consumidores | P1 |
| 109 | LOC-008 | Fechar cobertura integral ARC-13 por classificação | P1 |

#### Marco O5 — Localização aplicada

Critérios de saída:

- Inventário classificado.
- Conteúdo comercial preservado.
- Chaves canônicas.
- HTML autoral resolvido.
- JS consumindo catálogo.
- Acessibilidade verificada.
- Exceções documentadas.
- Nenhuma obrigação artificial de traduzir todos os 1.026 sinks candidatos.

---

### Onda 6 — Otimização final, publicação e documentação

**Objetivo:** reduzir o custo recorrente de validação e fechar a aplicação do programa.

| Ordem | ID | Entrega operacional | Prioridade |
|---:|---|---|---|
| 110 | TST-003 | Classificar redundâncias sem eliminar garantias | P1 |
| 111 | TST-018 | Preservar contratos de assets atuais e replays históricos | P1 |
| 112 | TST-022 | Criar seleção de bundles por impacto | P0/P1 |
| 113 | TST-023 | Consolidar infraestrutura de CI compartilhável | P1 |
| 114 | TST-024 | Diagnosticar e tratar intermitência | P1 |
| 115 | TST-025 | Formalizar os gates de integração e publicação | P0 |
| 116 | TST-026 | Implantar recibo mínimo por pacote | P0 |
| 117 | GIT-021 | Reconciliar batches consumidos e pins obsoletos | P1 |
| 118 | GIT-022 | Consolidar a política de preservação e retirada de refs | P1 |
| 119 | GIT-023 | Formalizar o pipeline de publicação Netlify | P0/P1 |
| 120 | OPS-NET-002 | Aplicar a política aprovada | Condicional |
| 121 | GIT-024 | Formalizar rollback por classe de mudança | P0 |
| 122 | GIT-025 | Consolidar a prontidão de release e handover | P0 |
| 123 | DOC-001 | Índice e prefácio | P1 |
| 124 | DOC-002 | Documento único integral | P0 |
| 125 | DOC-003 | Validação editorial | P0 |

#### Marco O6 — Programa operável e documento consolidado

Critérios de saída:

- CI selecionada por impacto.
- Evidência rastreável por contrato e SHA.
- Estado operacional canônico.
- Política de Preview definida.
- Publicação e rollback controlados.
- Branches temporárias com destino explícito.
- Documento único consistente.
- Índice navegável.
- Prefácio contextual.
- Anexo DoD atualizado.
- Próximas entregas identificáveis sem reconstruir o histórico.

---

## 5. Avaliação crítica da sequência

A tabela anterior representa uma ordem preferencial, não um cronograma linear obrigatório.

Seria um erro exigir a conclusão das 125 entradas para permitir uma entrega útil.

### 5.1 Caminho crítico real

O caminho crítico do programa pode ser expresso como:

```text
Autoridade e inventário
        │
        ▼
Contratos e dependências
        │
        ▼
Fontes canônicas
        │
        ▼
Consumidores compartilhados
        │
        ▼
Testes por contrato
        │
        ▼
Integração por pacote
        │
        ▼
Readback
        │
        ▼
DoD e atualização operacional
```

O ciclo é repetido por pacote, não somente no final do programa.

### 5.2 Trilhas que podem avançar em paralelo

A partir do contrato de execução comum:

**Trilha visual**

TOK → CSS/FND → CMP → testes visuais → integração.

**Trilha de domínio**

DOM → fixtures → componentes de domínio → testes comerciais → integração.

**Trilha de localização**

LOC-001/002 → catálogo → consumidores → cobertura → integração.

**Trilha de engenharia**

TST → CI → seleção por impacto → reporting.

**Trilha de governança**

GIT → PRs → readback → publicação → higiene.

Elas se cruzam onde há dependências reais.

Não precisam aguardar umas pelas outras para avançar nos trechos independentes.

### 5.3 Limite de trabalho simultâneo

Recomendação inicial:

- Um pacote de integração em execução por conjunto de arquivos conflitantes.
- Um segundo pacote independente pode avançar em paralelo.
- Auditoria/documentação de apoio pode progredir durante CI.
- Evitar múltiplas branches editando o mesmo fragmento/header.
- Evitar rodar testes mutáveis sobre o mesmo checkout.
- Não iniciar integrações novas enquanto o resultado do pacote anterior ainda não foi compreendido.

Isso não é um limite rígido de duas tarefas simultâneas.

É uma regra de evitar contenção e perda de clareza.

---

## 6. Matriz de integrações prioritárias

As PRs atuais fornecem oportunidades de fechamento relativamente imediato.

| PR | Família | Benefício | Condição antes de integrar |
|---|---|---|---|
| #278 | Testes/hero | Oráculo visual independente | Confirmar resultado do teste no head |
| #279 | CI/UX-04 | Disponibilizar gate manual | Validar workflow e execução posterior |
| #280 | Testes/fixture | Corrigir browser glass | Confirmar replay e CI suficientes |
| DS #119 | Governança | Atualizar evidência arquitetural | Reconciliar referências e autoridade |
| #269 | NAV-005 | Consolidar header público | Validar head, foco, layout e HTML gerado |
| #271 | DS-04 | Corrigir contraste contextual | Separar critérios comprovados de G2 pendente |
| #274 | ARC-13 | Integrar inventário de localização | Regerar sobre fonte autoral mais recente |

A ordenação é uma preferência que pode ser modificada por maturidade, dependência e conflito de arquivos.

Uma PR que já tem todas as provas pertinentes pode avançar antes de outra mais antiga.

A meta é fechar trabalho efetivamente útil, não respeitar uma ordem histórica arbitrária.

---

## 7. Detalhamento do novo item Netlify

### OPS-NET-001 — Avaliar desativação dos Deploy Previews automáticos

**Prioridade:** P0, por prevenção de custo operacional  
**Estado inicial:** `not_started`  
**Tipo:** decisão de infraestrutura  
**Dependências:** GIT-001 e TST-005  
**Prazo relativo:** antes da próxima rodada que possa produzir novos previews não intencionais  
**Autoridade:** configuração do projeto Netlify e política de CI  
**Escrita autorizada:** nenhuma; avaliação inicialmente somente leitura.

**Canal de operação homologado pelo usuário:** interface gráfica do Netlify aberta no navegador próprio do ChatGPT (Work/Cloud Browser). Não planejar alteração dessas configurações por CLI, scripts, automações genéricas ou plugin Netlify: esses caminhos foram relatados como inconsistentes ou sem controles suficientes. O acesso via navegador não substitui a aprovação específica para mudar a configuração.

#### 7.1 Problema

O Netlify gera Deploy Previews automaticamente em PRs de repositórios conectados, salvo configuração em contrário.

Isso cria um acoplamento entre:

**abrir/atualizar PR** e **consumir recursos de hospedagem**.

No MobiliPresenter2D esse acoplamento é especialmente inconveniente porque:

- Muitas PRs são exclusivamente documentais.
- Outras modificam somente testes.
- Há investigação frequente por pequenos incrementos.
- Nem todas as alterações exigem navegador hospedado.
- Existem gates capazes de funcionar localmente.
- A conta já apresentou preocupação concreta com banda.
- Previews automáticos não substituem validação de autenticação ou publicação adequada.

#### 7.2 Pergunta central

**Convém desligar os Deploy Previews automáticos do Netlify e passar a criá-los deliberadamente, somente para pacotes que realmente necessitam de validação hospedada?**

Minha hipótese inicial é que sim, mas a decisão depende de verificar a configuração efetiva e o impacto na CI.

#### 7.3 Alternativas

| Alternativa | Vantagem | Desvantagem |
|---|---|---|
| A — Manter automático | Disponibilidade imediata em toda PR | Geração desnecessária de previews |
| B — Desativar previews de PR por padrão | Controle mais forte de custo e intenção | Exige fluxo deliberado para preview necessário |
| C — Manter automático com skips seletivos | Mudança menor de processo | Dependência de disciplina por PR |
| D — Política híbrida por contexto, caso suportada | Menor atrito para PRs relevantes | Configuração e manutenção mais complexas |

#### 7.4 Procedimento de avaliação

1. Abrir a interface Netlify no navegador próprio do ChatGPT e identificar o projeto correto.
2. Confirmar site de produção.
3. Confirmar integração GitHub atual.
4. Consultar a configuração de Deploy Previews.
5. Consultar branch de produção.
6. Consultar Branch Deploys.
7. Consultar política de Agent Runs, se aplicável.
8. Identificar deploys recentes gerados por PRs de docs/testes.
9. Separar custo de build, transferência de deploy e tráfego servido.
10. Medir quais previews receberam acessos relevantes.
11. Identificar os required checks dependentes de status Netlify.
12. Identificar workflows que exigem URL de Preview.
13. Identificar gates que já podem rodar em loopback.
14. Identificar gates que exigem funções hospedadas.
15. Identificar gates que exigem autenticação real.
16. Identificar como criar preview deliberado com commit exato.
17. Confirmar a compatibilidade desse método com a política GitHub.
18. Confirmar se desligar preview por PR preserva publicação automática da `main`.
19. Confirmar que a alternativa não interrompe todos os builds.
20. Simular o processo para uma PR técnica futura.
21. Comparar custo e complexidade operacional.
22. Propor uma política.
23. Registrar decisão.
24. Somente depois, se autorizado, executar OPS-NET-002.

#### 7.5 Distinção importante

**Desabilitar Deploy Previews de PR não equivale a desativar todos os builds Netlify.**

A segunda opção também pode interromper builds de produção e branch deploys.

Portanto, a configuração a avaliar é especificamente a de previews automáticos de novas PRs.

#### 7.6 Política preliminar recomendada

- PR de documentação: sem Preview por padrão.
- PR apenas de testes: sem Preview por padrão.
- PR de CI: sem Preview por padrão, salvo dependência hospedada explícita.
- Mudança visual com boa fixture local: Browser local primeiro.
- Mudança em autenticação/servidor: Preview quando necessário.
- Mudança comercial/publicação: Preview ou ambiente autorizado quando o contrato exigir.
- Release: readback de produção após integração e deploy.

#### 7.7 DoD

OPS-NET-001 poderá ser `done` quando:

- A configuração atual for conhecida.
- O impacto nos required checks for identificado.
- O custo operacional for avaliado.
- O método de preview deliberado for definido.
- A produção permanecer protegida.
- Houver decisão explícita de manter, desativar ou modular a política.
- A decisão estiver registrada no plano.

A alteração de configuração não faz parte desse DoD.

Ela pertence a OPS-NET-002, se necessária.

#### 7.8 Documentação oficial

- https://docs.netlify.com/deploy/deploy-types/deploy-previews/
- https://docs.netlify.com/build/configure-builds/stop-or-activate-builds/
- https://docs.netlify.com/build/git-workflows/overview/

---

### OPS-NET-002 — Aplicar a política aprovada

**Prioridade:** condicional  
**Estado inicial:** `not_started`  
**Dependências:** OPS-NET-001 e aprovação da alteração.

#### Procedimento

1. Registrar a configuração anterior.
2. Registrar os required checks pertinentes.
3. Confirmar a escolha aprovada.
4. Executar a alteração específica pela interface gráfica do Netlify no navegador do ChatGPT; não por CLI ou plugin.
5. Confirmar que produção continua configurada.
6. Confirmar que os builds não foram interrompidos globalmente.
7. Confirmar comportamento de uma PR de teste controlada.
8. Confirmar a política de geração deliberada de Preview.
9. Confirmar que status GitHub não ficam pendentes indevidamente.
10. Executar readback.
11. Registrar rollback.
12. Atualizar o DoD.

Se OPS-NET-001 concluir que a configuração atual é adequada, OPS-NET-002 será `cancelled` com a justificativa correspondente.

Nenhum teste deve criar um preview apenas para comprovar que ele foi desativado, sem avaliar primeiro o custo e a necessidade dessa prova.

---

## 8. Bundles e critérios transversais

### 8.1 Todo pacote possui um bundle principal

O bundle determina quais verificações são indispensáveis para o tipo de mudança.

| Família | Bundle dominante |
|---|---|
| Método/arquitetura | Auditoria de fonte, contratos e consistência |
| Tokens/CSS | BT-CSS e BT-TST-34 |
| Componentes | BT-CMP correspondente |
| Domínio | BT-DOM correspondente |
| Localização | BT-LOC e BT-TST-50 |
| CI | BT-TST correspondente |
| Git/integração | BT-GIT correspondente |
| Netlify | Configuração, status e readback |
| Documento final | Revisão estrutural, editorial e de rastreabilidade |

### 8.2 Bundle mínimo para refatoração equivalente

1. Baseline.
2. Contrato afetado.
3. Alteração.
4. Teste do contrato.
5. Teste dos consumidores.
6. Controle negativo.
7. Diff final.
8. Integração.
9. Readback.
10. DoD.

### 8.3 Bundle para mudança visual intencional

Acrescentar:

- Decisão homologada.
- Evidência visual.
- Estado/tema relevante.
- Viewport relevante.
- Contraste e acessibilidade, conforme risco.
- Aprovação do escopo visual.

### 8.4 Bundle para domínio e segurança

Acrescentar:

- Entradas inválidas.
- Estados não autorizados.
- Compatibilidade de DTO.
- Garantias de publicação.
- Persistência.
- Rejeições esperadas.
- Ausência de vazamento.
- Reversibilidade de efeitos.

### 8.5 Bundle para CI e tooling

Acrescentar:

- Alcançabilidade do comando.
- Precondições.
- Falha negativa.
- Limites de fixture.
- Execução no SHA correto.
- Sem perda de cobertura.
- Sem efeitos colaterais não autorizados.

---

## 9. Definition of Done global

A conclusão precisa ser mais forte do que “implementado”.

Um item somente pode receber `done` quando cumprir todos os critérios aplicáveis.

### 9.1 Checklist universal

- [ ] O resultado está delimitado.
- [ ] A autoridade do contrato está identificada.
- [ ] As dependências relevantes estão satisfeitas.
- [ ] A mudança ou análise está concluída.
- [ ] Os critérios de aceitação foram verificados.
- [ ] Os testes aplicáveis passaram.
- [ ] Os controles negativos pertinentes passaram.
- [ ] As exceções estão documentadas.
- [ ] Os riscos residuais são conhecidos.
- [ ] A integração foi comprovada, quando aplicável.
- [ ] A publicação foi comprovada, quando faz parte da entrega.
- [ ] A evidência possui versão e origem.
- [ ] O rollback está definido quando necessário.
- [ ] O status operacional foi atualizado.
- [ ] A transição foi registrada na timeline.

### 9.2 Exceções por tipo

Um item de documentação não precisa de screenshot do Viewer.

Um item de CSS não precisa comprovar persistência de preço, salvo se alterar a interface de publicação desse preço.

Um item de CI pode ser concluído sem deploy.

Uma mudança de schema/persistência exige evidências mais fortes que uma alteração editorial.

A regra é aplicar os critérios relevantes, sem transformar o DoD em um ritual burocrático.

### 9.3 Proibição de conclusão por inferência

Não marcar `done` com base apenas em:

- PR aberta.
- CI verde em SHA anterior.
- Código presente em `development`.
- Documento afirmando PASS.
- Preview READY.
- Teste em fixture incompatível.
- Screenshot sem estado identificável.
- Merge de branch que não contém o pacote completo.
- Manifesto declarando ativação.
- Commit recente.
- Contagem reduzida de branches.

---

## 10. Anexo operacional — registro de estado

### 10.1 Estrutura proposta

O anexo operacional deverá conter a lista integral dos IDs, mantendo o documento principal como especificação detalhada.

Esquema:

```text
ID
title
status
priority
dependencies
target
contract
test_bundle
evidence
notes
```

O estado é o único campo de progresso.

Metadados adicionais explicam o que foi comprovado.

Não é necessário adicionar campos como:

- `almost_done`
- `done_but_not_integrated`
- `partially_verified`
- `mostly_passed`

Essas condições são representadas por `in_review`, `blocked` ou notas/evidências.

### 10.2 Exemplo de entrada

```text
ID: GIT-012
title: Integrar NAV-005 primário
status: not_started
priority: P0
dependencies:
  - CMP-002
  - CMP-003
  - CMP-004
target: Product/main
contract: NAV-005
test_bundle: BT-GIT-10
evidence: []
notes: PR #269 candidata; reconciliar head
```

O exemplo descreve a estrutura inicial, não altera o estado real da PR.

### 10.3 Protocolo do agente

Antes de agir:

1. Ler o índice.
2. Identificar a próxima tarefa pronta.
3. Conferir o status.
4. Conferir dependências.
5. Conferir a branch.
6. Conferir o SHA.
7. Declarar os IDs que serão executados.
8. Atualizar os IDs para `in_progress`.
9. Executar os bundles aplicáveis.

Depois:

1. Registrar o resultado.
2. Identificar a evidência.
3. Registrar integração e publicação separadamente.
4. Determinar o status correto.
5. Atualizar apenas os IDs trabalhados.
6. Acrescentar a transição à timeline.
7. Apresentar resumo de alterações de estado.
8. Indicar a próxima tarefa pronta.

### 10.4 Regra para tarefas já implementadas

Se a tarefa está `not_started`, mas o código já existe:

1. Identificar a implementação.
2. Verificar o contrato.
3. Verificar a branch-alvo.
4. Verificar a evidência.
5. Determinar se falta integração, testes ou documentação.
6. Atualizar o estado somente após a reconciliação.

O agente não deverá recriar o componente apenas para demonstrar que executou uma tarefa.

---

## 11. Timeline operacional

A timeline deve registrar eventos, não narrar novamente todo o processo.

### 11.1 Estrutura

```text
timestamp
id
from
to
evidence
note
```

### 11.2 Exemplo ilustrativo

```text
2026-11-17T21:00:00-03:00
GIT-012
not_started → in_progress
evidence: PR #269, head confirmado
note: revisão de NAV-005 iniciada

2026-11-17T21:40:00-03:00
GIT-012
in_progress → in_review
evidence: CI e browser do head
note: aguarda integração

2026-11-18T10:00:00-03:00
GIT-012
in_review → done
evidence: merge SHA e readback
note: pacote integrado
```

As entradas são exemplos de formato, não registros de eventos ocorridos.

### 11.3 Regras de manutenção

- Não alterar o passado para ocultar falhas.
- Não duplicar transições sem motivo.
- Não alterar o ID ao reordenar a tarefa.
- Registrar mudança de escopo relevante em nota.
- Preservar o link para o recibo.
- Evitar registrar cada teste como uma transição de estado.
- Registrar somente eventos com efeito operacional.
- Usar data com fuso explícito.
- Reconciliar conflitos de atualização antes de escrever.
- Não atualizar a timeline a partir de suposição.

### 11.4 Fonte canônica

Recomendo manter o índice de execução e a timeline na mesma área documental, com referências às evidências.

Um único arquivo Markdown é suficiente inicialmente.

Uma estrutura de dados ou dashboard só se justifica se o volume de atualizações demonstrar necessidade.

---

## 12. Progresso e indicadores

### 12.1 Não calcular porcentagens sem baseline reconciliada

O histórico demonstra que percentuais manuais podem transmitir precisão indevida.

A criação das 125 entradas não significa que existem 137 unidades equivalentes de trabalho.

Algumas são pequenas decisões.

Outras são validações extensas.

Outras dependem de integração de código já implementado.

Portanto, uma porcentagem simples por número de tarefas concluídas é útil apenas se for identificada como **percentual de IDs encerrados**, e não como percentual de esforço restante.

### 12.2 Indicadores recomendados

| Indicador | Interpretação |
|---|---|
| IDs `done` / total | Conclusão formal de itens |
| IDs `in_review` | Trabalho produzido aguardando gate |
| IDs `blocked` | Impedimentos ativos |
| Dependências críticas abertas | Gargalos reais |
| Pacotes integrados | Entregas efetivamente absorvidas |
| Contratos com evidência válida | Qualidade de verificação |
| PRs abertas sem disposição | Dívida operacional |
| Branches temporárias sem owner | Dívida de governança |
| Previews por pacote | Custo de hospedagem |
| Tempo entre código e integração | Fricção de release |
| Contratos com autoridade única | Qualidade arquitetural |
| Tarefas retomáveis sem contexto narrativo | Eficiência documental |

### 12.3 Progresso por marco

Um marco estará concluído quando todos os seus critérios obrigatórios forem satisfeitos.

A existência de tarefas P2 remanescentes não precisa bloquear uma release funcional, desde que tenham sido classificadas como não obrigatórias para aquele marco.

Uma tarefa `cancelled` não será computada como implementação entregue.

Sua retirada do escopo deve ser explícita.

---

## 13. Política para mudanças de escopo

Durante a execução surgirão descobertas que não estão descritas no backlog.

A regra deve ser simples.

### 13.1 Descoberta pequena e relacionada

Pode ser incorporada ao ID atual se:

- Não alterar o objetivo.
- Não acrescentar contrato independente.
- Não exigir outro rollback.
- Não alterar significativamente os testes.
- Não introduzir nova decisão de produto.

Registrar em nota.

### 13.2 Descoberta independente

Criar novo ID se:

- Exigir novo contrato.
- Exigir nova autorização.
- Exigir novo consumer não previsto.
- Exigir testes de natureza diferente.
- Alterar o risco de integração.
- Merecer rollback independente.

O novo ID entra na ordem preferencial e começa em `not_started`.

### 13.3 Descoberta que invalida o plano

Não corrigir silenciosamente o documento histórico.

Registrar a evidência.

Atualizar a tarefa e as dependências.

Revisar a arquitetura somente no ponto afetado.

Evitar reabrir decisões homologadas sem necessidade.

---

## 14. Gates de controle do programa

### Gate A — Prontidão de execução

Condições:

- ID conhecido.
- Escopo conhecido.
- Dependências identificadas.
- Branch identificada.
- Testes definidos.
- Ausência de decisão bloqueante ignorada.

### Gate B — Prontidão de revisão

Condições:

- Resultado produzido.
- Diff revisável.
- Testes do pacote executados.
- Controles negativos.
- Limitações registradas.
- Evidência do head.

### Gate C — Prontidão de integração

Condições:

- Contrato homologado preservado.
- CI relevante.
- Base atual reconciliada.
- Required checks.
- Rollback.
- GO técnico.

### Gate D — Integração concluída

Condições:

- Commit integrado.
- Conteúdo presente no destino.
- Testes de readback.
- Nenhuma autoridade concorrente.
- DoD de integração.

### Gate E — Publicação verificada

Condições:

- Build correto.
- Commit correto.
- Artefato servido.
- CSS/JS/rotas corretos.
- Smoke pertinente.
- Ausência de alterações não autorizadas.

### Gate F — Encerramento operacional

Condições:

- Status final.
- Evidência.
- Timeline.
- PR/branch com disposição.
- Próximo trabalho identificado.

---

## 15. Questões que ainda exigem decisão

Nem todas as dúvidas dos sete capítulos exigem intervenção do usuário.

A maioria é resolúvel por inspeção técnica ou testes.

As questões abaixo têm potencial de exigir decisão de política.

| Questão | Recomendação inicial |
|---|---|
| NET-01 — Desativar previews automáticos? | Avaliar e preferir geração deliberada se não prejudicar os gates |
| GIT-11 — Autorizar exclusão automática pós-merge? | Exigir aprovação específica por padrão |
| ARC-13 — Chaves e textos ambíguos | Decidir por owner semântico, não pelo scanner |
| G2 — Contraste ainda incerto | Verificar runtime, sem aplicar correção global especulativa |
| G3 — Aprovação de novas variantes | Aplicar homologações vigentes e pedir decisão apenas quando houver conflito real |
| AUTH — Fixture hospedada indisponível | Resolver tecnicamente sem desativar segurança |
| CI — Required checks desconhecidos | Consultar configuração efetiva antes de mudar política |
| PUBLICAÇÃO — Alteração de dados reais | Não executar sem autorização correspondente |
| RELEASE — Exceções de DoD | Aceitar somente quando explicitamente classificadas |

A decisão sobre Preview não deve impedir a redação do documento final.

Ela deverá permanecer como ticket prioritário do programa de execução.

---

## 16. Estrutura prevista do documento único

No Turno IX, este material será incorporado a uma estrutura editorial completa.

### 16.1 Front matter

1. Capa.
2. Controle de versão.
3. Prefácio.
4. Resumo executivo.
5. Como utilizar o documento.
6. Escopo e limites.
7. Convenções de evidência e DoD.
8. Índice navegável.

### 16.2 Corpo principal

**Capítulo I — Histórico e diagnóstico do método**

Fricções, limitações, causas e revisão de processo.

**Capítulo II — Arquitetura homologada e revisão crítica ARC**

Autoridades, invariantes e alterações permitidas.

**Capítulo III — Foundations, cores, tokens, CSS e temas**

Fonte visual única, consumidores e validação.

**Capítulo IV — Componentes, composição e lifecycle**

Reutilização de HTML, JS e renderers.

**Capítulo V — Core V5, Admin, Configurador, Viewer e localização**

Contratos de domínio, dados públicos e textos.

**Capítulo VI — Testes e evidências**

Fixtures, CI, bundles, browser e assertions.

**Capítulo VII — Git, integração, publicação e rollback**

DAG, PRs, merges, Netlify e governança.

**Capítulo VIII — Plano de execução**

Backlog, prioridades, marcos e caminhos críticos.

### 16.3 Anexos

**Anexo A:** DoD global.

**Anexo B:** Lista operacional integral de IDs.

**Anexo C:** Timeline.

**Anexo D:** Bundles de testes.

**Anexo E:** Matriz ARC/G/IDs.

**Anexo F:** Matriz de dependências.

**Anexo G:** Registro de decisões e questões abertas.

**Anexo H:** Referências técnicas.

**Anexo I:** Glossário.

### 16.4 Regra de consolidação editorial

O documento único não deve ser apenas a concatenação dos oito capítulos.

A revisão deverá:

1. Preservar integralmente as análises e os procedimentos relevantes.
2. Eliminar afirmações repetidas sem perder informação.
3. Reconciliar IDs e referências cruzadas.
4. Corrigir nomenclaturas inconsistentes.
5. Distinguir fatos verificados de recomendações.
6. Conservar datas e SHAs como snapshots.
7. Reconciliar disposições de PRs citadas em diferentes capítulos.
8. Confirmar que cada tarefa está presente no backlog.
9. Confirmar que cada bundle aponta para tarefas reais.
10. Confirmar que nenhuma decisão homologada foi alterada por simplificação editorial.
11. Verificar links.
12. Gerar índice navegável.
13. Inserir o prefácio.
14. Conferir a integridade do documento final.
15. Registrar sua própria versão e status.

---

## 17. DoD da consolidação documental

### DOC-001 — Índice e prefácio

Critérios:

- O prefácio explica origem, finalidade e limites.
- O índice reflete a estrutura real.
- Existe orientação para leitura integral e execução operacional.
- A hierarquia documental é clara.
- O texto não confunde plano com trabalho concluído.

### DOC-002 — Documento único integral

Critérios:

- Partes I–VIII incorporadas.
- Conteúdo técnico preservado.
- IDs consistentes.
- Dependências reconciliadas.
- Contradições resolvidas.
- Repetições reduzidas.
- Anexos incorporados.
- Referências completas.

### DOC-003 — Validação editorial

Critérios:

- Índice e títulos correspondem.
- Nenhum ID está ausente ou duplicado indevidamente.
- Nenhum status foi atribuído por suposição.
- Os links funcionam ou estão classificados.
- As afirmações temporais estão datadas.
- Os comandos e paths são compatíveis com os repositórios consultados.
- Os contratos homologados estão preservados.
- As tarefas prioritárias possuem próximos passos acionáveis.
- O documento é legível sem contexto da conversa.
- O anexo operacional pode ser atualizado sem reescrever os capítulos.

---

## 18. Parecer conclusivo dos oito turnos

A arquitetura do MobiliPresenter2D não parece sofrer principalmente de falta de boas decisões.

Ao contrário, há muitas decisões, mecanismos e provas úteis.

O problema recorrente é a distância entre:

**decidir → implementar → integrar → validar → registrar conclusão.**

Essa distância gerou:

- Múltiplos documentos de estado.
- Revisões repetidas de contextos já avaliados.
- Incerteza sobre qual implementação está ativa.
- CI parcialmente desconectada dos gatilhos relevantes.
- PRs com trabalho útil ainda não integrado.
- Branches históricas que exigiram ampla reconciliação.
- Dificuldade para medir progresso.
- Retomadas dependentes da memória do agente.

O plano proposto reduz essa distância com cinco mecanismos principais.

#### Primeiro — Autoridade única por responsabilidade

Cores, componentes, dados comerciais, rotas e decisões devem possuir donos identificáveis.

#### Segundo — Incrementos tecnicamente coesos

Cada conjunto deve ser suficientemente completo para gerar valor, mas suficientemente restrito para ser revisado e revertido.

#### Terceiro — Testes relacionados a contratos

A prova deve acompanhar o risco real da mudança.

Não precisamos executar tudo sempre.

Precisamos executar tudo que é pertinente.

#### Quarto — Integração verificável

Trabalho presente em PR ou `development` não é automaticamente trabalho entregue.

A integração deve ser comprovada no destino.

#### Quinto — DoD e reporting operacional

Uma única lista ordenada deve informar:

- O que fazer.
- O que está acontecendo.
- O que terminou.
- O que está bloqueado.
- O que ainda depende de decisão.
- Qual evidência comprova cada conclusão.

Essa lista será pequena em estrutura, mesmo sendo extensa em entradas.

**A proposta final é uma arquitetura com mais centralização de responsabilidade e menos centralização de burocracia.**

O documento explica as decisões.

O backlog orienta o trabalho.

Os testes produzem evidência.

O Git registra as alterações.

O DoD determina quando uma entrega terminou.

---

### Referências de execução

- [Produto — repositório principal](https://github.com/EAKerber/MobiliPresenter2D)
- [Design System](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem)
- [Decisões D01–D04](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/main/docs/APPROVALS_D01_D04_2026-10-26.md)
- [Crosswalk atual ARC/G](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARCHITECTURE_EXECUTION_CROSSWALK_2026-11-15.md)
- [Handover development](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/handoffs/HANDOVER_DEVELOPMENT_2026-10-27.md)
- [ARC-15 — verificações](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/blob/docs/architecture-status-20261109/docs/architecture/ARC15_VERIFICATION_INVENTORY_2026-11-15.md)
- [Netlify — Deploy Previews](https://docs.netlify.com/deploy/deploy-types/deploy-previews/)
- [Netlify — Stop/activate builds](https://docs.netlify.com/build/configure-builds/stop-or-activate-builds/)

**Limite deste documento:** o backlog foi consolidado como proposta. Seus estados ainda não foram publicados no Git, os testes não foram reexecutados neste turno e nenhuma configuração Netlify foi modificada. A reconciliação dos registros existentes será requisito da primeira aplicação operacional.

**Registro editorial:** as Partes I–VIII foram reunidas nesta edição 0.9. A execução técnica dos tickets permanece pendente de reconciliação de estado nos repositórios.

---

<a id="anexo-a"></a>
# Anexo A — Registro canônico de IDs e estados iniciais

Este registro é **inicial e editorial**: as tarefas ainda não tiveram seus estados operacionais sincronizados com Git ou com o histórico de execução. `not_started` significa que a execução formal do ID neste programa ainda não foi reconciliada; **não** afirma ausência de código ou testes. A prioridade e a ordem são propostas do Capítulo VIII.

| Ordem | ID canônico | Tarefa descrita na fonte | Parte de origem | Prioridade | Estado inicial |
|---:|---|---|:---:|:---:|---|
| 001 | `GIT-001` | Criar snapshot operacional dos repositórios | VII | P0 | `not_started` |
| 002 | `OPS-NET-001` | Avaliar desativação dos Deploy Previews automáticos | VIII | P0 | `not_started` |
| 003 | `GIT-002` | Consolidar a hierarquia documental | VII | P0 | `not_started` |
| 004 | `MD-001` | Congelar o inventário de referência | I | P0 | `not_started` |
| 005 | `MD-002` | Consolidar a cadeia ARC → entrega → consumidor | I | P0 | `not_started` |
| 006 | `MD-003` | Recalibrar métricas | I | P0 | `not_started` |
| 007 | `MD-004` | Auditar os 21 comandos e 21 workflows do baseline ARC-15 | I | P0 | `not_started` |
| 008 | `MD-005` | Validar a infraestrutura dos browsers | I | P0 | `not_started` |
| 009 | `MD-006` | Resolver a estratégia de fixture autenticada | I | P0 | `not_started` |
| 010 | `MD-007` | Classificar as PRs atualmente abertas | I | P1 | `not_started` |
| 011 | `MD-008` | Estabelecer política de reconciliação `main` ↔ `development` | I | P0 | `not_started` |
| 012 | `MD-009` | Decompor G2/DS-05A em bloqueios localizados | I | P1 | `not_started` |
| 013 | `MD-010` | Selecionar o primeiro pacote vertical de componentes/tokens | I | P0 | `not_started` |
| 014 | `RM-01` | Criar uma única unidade executável de planejamento | I | P0 | `not_started` |
| 015 | `RM-02` | Substituir documentação narrativa repetida por registros estruturados | I | P0 | `not_started` |
| 016 | `RM-03` | Utilizar bundles de teste por domínio de mudança | I | P1 | `not_started` |
| 017 | `RM-04` | Separar prova local de prova hospedada | I | P0 | `not_started` |
| 018 | `RM-05` | Tornar a integração uma etapa planejada desde o início | I | P0 | `not_started` |
| 019 | `TST-001` | Fixar baseline e mapa de execução | VI | P0 | `not_started` |
| 020 | `TST-002` | Construir matriz assertion → contrato → risco | VI | P0 | `not_started` |
| 021 | `TST-004` | Auditar alcançabilidade dos workflows | VI | P0 | `not_started` |
| 022 | `TST-005` | Determinar required checks e política de status | VI | P0 | `not_started` |
| 023 | `GIT-004` | Inventariar a intenção das PRs abertas | VII | P0 | `not_started` |
| 024 | `GIT-019` | Auditar o mecanismo de branch hygiene | VII | P0 | `not_started` |
| 025 | `GIT-020` | Resolver a política de exclusão automática pós-merge | VII | P0 | `not_started` |
| 026 | `GIT-003` | Classificar a divergência `development` versus `main` | VII | P0 | `not_started` |
| 027 | `GIT-005` | Criar o DAG de dependências entre pacotes | VII | P0 | `not_started` |
| 028 | `GIT-006` | Definir unidade mínima de integração | VII | P0 | `not_started` |
| 029 | `GIT-007` | Formalizar extração seletiva com proveniência | VII | P0 | `not_started` |
| 030 | `GIT-008` | Definir a política de reconciliação com `main` | VII | P0 | `not_started` |
| 031 | `GIT-009` | Criar contrato operacional para PRs | VII | P0 | `not_started` |
| 032 | `GIT-010` | Formalizar o preflight de merge | VII | P0 | `not_started` |
| 033 | `GIT-011` | Formalizar o readback pós-merge | VII | P0 | `not_started` |
| 034 | `CMP-001` | Criar o inventário operacional dos componentes | IV | P0 | `not_started` |
| 035 | `DOM-001` | Inventário executável dos contratos V5 | V | P0 | `not_started` |
| 036 | `DOM-002` | Distinguir autoria, projeção e estado transitório | V | P0 | `not_started` |
| 037 | `GIT-018` | Revisar e concluir DS PR #119 | VII | P1 | `not_started` |
| 038 | `TOK-00` | Endurecer o contrato DS → Produto | III | P0 | `not_started` |
| 039 | `TOK-01` | Reconciliar VIS-002C v0.3 | III | P0 | `not_started` |
| 040 | `TOK-02` | Fechar P-TOKEN-02A1 e distinguir o alias da conformidade visual | III | P0 | `not_started` |
| 041 | `TOK-03` | Selecionar o primeiro novo token compartilhado | III | P1 | `not_started` |
| 042 | `CSS-00` | Reconstruir a baseline CSS atual | III | P0 | `not_started` |
| 043 | `CSS-01` | Classificar os 98 pares incertos | III | P1 | `not_started` |
| 044 | `CSS-02` | Reconciliar e concluir a PR #271 | III | P1 | `not_started` |
| 045 | `CSS-03` | Resolver `.module-number` | III | P1 | `not_started` |
| 046 | `CSS-04` | Resolver `#viewerHint` separadamente | III | P1 | `not_started` |
| 047 | `CSS-05` | Fechar o restante do DS-04 por causa técnica | III | P1 | `not_started` |
| 048 | `FND-01` | Extrair a primeira primitiva neutra | III | P1 | `not_started` |
| 049 | `FND-02` | Contratos de estados visuais | III | P1 | `not_started` |
| 050 | `FND-03` | Famílias CSS compartilhadas de risco crescente | III | P1 | `not_started` |
| 051 | `TST-016` | Consolidar contraste e CSSOM por contexto | VI | P0/P1 | `not_started` |
| 052 | `CMP-002` | Consolidar ARC-03C como autoridade das três páginas | IV | P0 | `not_started` |
| 053 | `CMP-003` | Consolidar o controlador único do menu público | IV | P0 | `not_started` |
| 054 | `CMP-004` | Fechar NAV-005 para o header público primário | IV | P0 | `not_started` |
| 055 | `GIT-012` | Revisar e concluir PR #269 — NAV-005 | VII | P0 | `not_started` |
| 056 | `TST-012` | Consolidar o bundle de navegação pública | VI | P1 | `not_started` |
| 057 | `CMP-005` | Consolidar o header secundário do Viewer | IV | P0 | `not_started` |
| 058 | `CMP-018` | Auditar inicialização, atualização e descarte | IV | P1 | `not_started` |
| 059 | `CMP-007` | Consolidar o mecanismo de tema e os slots de inserção | IV | P1 | `not_started` |
| 060 | `TST-015` | Fortalecer os testes do tema | VI | P1 | `not_started` |
| 061 | `CMP-008` | Consolidar a identidade da marca | IV | P1 | `not_started` |
| 062 | `CMP-009` | Definir famílias de botões por contrato, não por classe | IV | P2 | `not_started` |
| 063 | `CMP-010` | Consolidar feedback de interface respeitando sua finalidade | IV | P2 | `not_started` |
| 064 | `CMP-011` | Revisar o piloto declarativo da Landing | IV | P2 | `not_started` |
| 065 | `CMP-012` | Consolidar o carrossel e a seleção de ambientes | IV | P2 | `not_started` |
| 066 | `CMP-013` | Consolidar o painel expansível de Como funciona | IV | P1 | `not_started` |
| 067 | `CMP-019` | Formalizar o limite entre build-time e runtime | IV | P1 | `not_started` |
| 068 | `TST-017` | Separar provas geométricas de provas visuais | VI | P1 | `not_started` |
| 069 | `GIT-015` | Revisar e concluir PR #278 — geometria do hero | VII | P1 | `not_started` |
| 070 | `TST-019` | Estabelecer política de screenshots e referências visuais | VI | P1 | `not_started` |
| 071 | `TST-021` | Cobrir interações acessíveis não verificadas | VI | P1 | `not_started` |
| 072 | `DOM-003` | Consolidar a leitura da configuração publicada | V | P0 | `not_started` |
| 073 | `DOM-004` | Consolidar publicação V5, revisão e ETag | V | P0 | `not_started` |
| 074 | `TST-009` | Fechar a cobertura de publicação V5 | VI | P0 | `not_started` |
| 075 | `DOM-005` | Encerrar o alcance dos caminhos históricos V3/V4 | V | P1 | `not_started` |
| 076 | `DOM-006` | Consolidar `NormalizedConfiguratorFlow` | V | P1 | `not_started` |
| 077 | `DOM-007` | Consolidar projeções responsivas e componentes de seção | V | P1 | `not_started` |
| 078 | `DOM-008` | Consolidar o contrato de precificação tipada | V | P0/P1 | `not_started` |
| 079 | `DOM-009` | Consolidar a autoria de dados no Admin | V | P1 | `not_started` |
| 080 | `DOM-010` | Consolidar a autorização de preços base no Viewer | V | P0 | `not_started` |
| 081 | `TST-011` | Fechar cobertura da projeção pública e preços | VI | P0 | `not_started` |
| 082 | `DOM-011` | Fortalecer o endpoint Buyer e a fixture autorizada | V | P0 | `not_started` |
| 083 | `TST-006` | Consolidar o servidor local Buyer V5 | VI | P0 | `not_started` |
| 084 | `DOM-012` | Consolidar o Viewer como consumidor público restrito | V | P1 | `not_started` |
| 085 | `DOM-013` | Consolidar políticas de acesso por superfície | V | P0 | `not_started` |
| 086 | `TST-010` | Fechar cobertura de autorização e sessão | VI | P0 | `not_started` |
| 087 | `CMP-006` | Formalizar a fronteira do header privado | IV | P1 | `not_started` |
| 088 | `CMP-014` | Formalizar o contrato compartilhado de cena e hotspots | IV | P1 | `not_started` |
| 089 | `CMP-015` | Consolidar componentes de apresentação do Configurador | IV | P1 | `not_started` |
| 090 | `CMP-016` | Preservar a especialização do Viewer e consolidar seus componentes | IV | P1 | `not_started` |
| 091 | `CMP-017` | Consolidar controles do Admin por significado | IV | P1 | `not_started` |
| 092 | `DOM-014` | Consolidar as fronteiras Core / apresentação | V | P1 | `not_started` |
| 093 | `TST-013` | Consolidar teclado e foco do Configurador | VI | P1 | `not_started` |
| 094 | `TST-014` | Consolidar os testes de layout responsivo e PiP | VI | P1 | `not_started` |
| 095 | `TST-007` | Corrigir e integrar o browser de vidro/oclusão | VI | P1 | `not_started` |
| 096 | `TST-008` | Isolar testes que alteram arquivos durante a execução | VI | P1 | `not_started` |
| 097 | `GIT-013` | Revisar e concluir PR #271 — DS-04 | VII | P0/P1 | `not_started` |
| 098 | `GIT-016` | Revisar e concluir PR #279 — dispatch UX-04 | VII | P1 | `not_started` |
| 099 | `GIT-017` | Revisar e concluir PR #280 — browser glass | VII | P1 | `not_started` |
| 100 | `LOC-001` | Consolidar o inventário ARC-13 | V | P0 | `not_started` |
| 101 | `LOC-002` | Classificar textos por autoridade e função | V | P0 | `not_started` |
| 102 | `GIT-014` | Revisar e concluir PR #274 — ARC-13 | VII | P1 | `not_started` |
| 103 | `LOC-003` | Definir o catálogo canônico `pt-BR` | V | P1 | `not_started` |
| 104 | `LOC-004` | Extrair textos dos fragmentos e páginas estáticas | V | P1 | `not_started` |
| 105 | `LOC-005` | Extrair textos de controladores e componentes JS | V | P1 | `not_started` |
| 106 | `LOC-006` | Extrair textos do Admin e Configurador sem migrar conteúdo comercial | V | P1/P2 | `not_started` |
| 107 | `TST-020` | Verificar cobertura de localização por consumidor | VI | P1 | `not_started` |
| 108 | `LOC-007` | Automatizar verificação de chaves e consumidores | V | P1 | `not_started` |
| 109 | `LOC-008` | Fechar cobertura integral ARC-13 por classificação | V | P1 | `not_started` |
| 110 | `TST-003` | Classificar redundâncias sem eliminar garantias | VI | P1 | `not_started` |
| 111 | `TST-018` | Preservar contratos de assets atuais e replays históricos | VI | P1 | `not_started` |
| 112 | `TST-022` | Criar seleção de bundles por impacto | VI | P0/P1 | `not_started` |
| 113 | `TST-023` | Consolidar infraestrutura de CI compartilhável | VI | P1 | `not_started` |
| 114 | `TST-024` | Diagnosticar e tratar intermitência | VI | P1 | `not_started` |
| 115 | `TST-025` | Formalizar os gates de integração e publicação | VI | P0 | `not_started` |
| 116 | `TST-026` | Implantar recibo mínimo por pacote | VI | P0 | `not_started` |
| 117 | `GIT-021` | Reconciliar batches consumidos e pins obsoletos | VII | P1 | `not_started` |
| 118 | `GIT-022` | Consolidar a política de preservação e retirada de refs | VII | P1 | `not_started` |
| 119 | `GIT-023` | Formalizar o pipeline de publicação Netlify | VII | P0/P1 | `not_started` |
| 120 | `OPS-NET-002` | Aplicar a política aprovada | VIII | Condicional | `not_started` |
| 121 | `GIT-024` | Formalizar rollback por classe de mudança | VII | P0 | `not_started` |
| 122 | `GIT-025` | Consolidar a prontidão de release e handover | VII | P0 | `not_started` |
| 123 | `DOC-001` | Índice e prefácio | VIII | P1 | `not_started` |
| 124 | `DOC-002` | Documento único integral | VIII | P0 | `not_started` |
| 125 | `DOC-003` | Validação editorial | VIII | P0 | `not_started` |

---

<a id="anexo-b"></a>
# Anexo B — Reconciliações editoriais e alertas de consistência

Esta consolidação conservou os procedimentos e análises dos oito capítulos, normalizando apenas a hierarquia de títulos e a camada do backlog mestre. As observações abaixo resolvem diferenças que poderiam comprometer a execução.

| Tema | Diferença encontrada | Tratamento na edição consolidada |
|---|---|---|
| Contagem do backlog | A Parte VIII preliminar anunciava 137 IDs, mas incluía `AR2-01` a `AR2-12` inexistentes como tarefas na Parte II | Backlog canônico corrigido para **125 IDs**; as decisões ARC permanecem como contratos de referência, sem IDs fictícios |
| IDs de método | `MD001` e `RM01` na tabela final, contra `MD-001` e `RM-01` nas fontes | Normalização para o formato real |
| Títulos CSS/TOK | A Parte VIII resumia títulos e por vezes trocava o significado de `CSS-02/03/04` e `TOK-01/02` | Cada linha do backlog passa a usar o título da tarefa na parte original; detalhes preservados no Capítulo III |
| Estados locais | A Parte III usa estados de execução CSS próprios (`DISCOVERY`, `READY`, `INTEGRATED` etc.) | Os seis estados canônicos do DoD prevalecem; classificações locais são consideradas notas de evidência, não novos status |
| ARC-13 | 1.026 ocorrências candidatas versus textos realmente localizáveis | Mantida a distinção: inventário não equivale a 1.026 migrações obrigatórias |
| VIS-002 | Paleta homologada como referência versus consumo global | Preservado o limite de autorização de distribuição; centralização deve comprovar consumidores reais |
| V5 | Projeção Buyer versus DTO público do Viewer | Mantidos como contratos distintos, especialmente na publicação de preços |
| Evidência e releases | Código/PR versus merge versus deploy | Exigidos como estados verificáveis diferentes |
| Netlify | Política de previews requer controle de UI do site | `OPS-NET-001/002` explicitam uso do navegador próprio do ChatGPT e rejeitam CLI/plugin como canal para essa configuração |
| Fotografia histórica | SHAs e números de PR podem envelhecer | Datados como baseline, não apresentados como estado corrente |

**O que não foi feito:** esta edição não comprova execução de testes, status atuais de PR, adequação dos deploys ou aprovação de novas decisões. Esses passos pertencem à execução dos IDs correspondentes.

---

<a id="anexo-c"></a>
# Anexo C — Proveniência dos oito anexos

Os capítulos foram montados a partir dos oito arquivos recebidos, em ordem lógica I→VIII. Os hashes abaixo identificam os bytes originais. Uma cópia concatenada literal é fornecida como arquivo de preservação, independente desta edição.

| Capítulo | Arquivo original | Linhas | SHA-256 |
|:---:|---|---:|---|
| I | `Texto colado (8).txt` | 604 | `689470862b8e65363c4bcf128109ac178683913c3b288b3d0e04740a6f91ca8e` |
| II | `Texto colado (7).txt` | 1114 | `fe84cfbe87d37ca5d7f786e5a006e9818c0a58c86120a38fc943fc83904b7532` |
| III | `Texto colado (6).txt` | 1264 | `6fa0cb9c3192eb5a36e69ac3c391670eb22702d6ffd5d23cb776dff7ef9fac2d` |
| IV | `Texto colado (5).txt` | 1840 | `80a6d25779ef6fa42c64a3576565595d2e47c4fe8321c9e9ca83e8f97d2a3193` |
| V | `Texto colado (4).txt` | 1853 | `daa22095b56007a5707028209935b7c0625c8cd996e2caead2039ee027e174f9` |
| VI | `Texto colado (3).txt` | 2144 | `6eb5f13d7bd7cf5c57506ecc7e92da1c5913b0ca53383ab9af0081223e63fac9` |
| VII | `Texto colado (2).txt` | 2071 | `ed2000c0b2e45f021d46e08d622cbf3871b6f331410b739516c8d4a91887e001` |
| VIII | `Texto colado(1).txt` | 1438 | `7ae965fe6a8d01a739da273358bc091a0d9c7654dac29d7e3356c4342ec3fa25` |

---

<a id="anexo-d"></a>
# Anexo D — Política operacional Netlify (acesso pela interface)

**Origem:** orientação expressa do usuário durante a consolidação.

A verificação e a eventual alteração da política de Deploy Previews no Netlify devem ocorrer **pela interface gráfica do próprio serviço, usando o navegador do ChatGPT em Work/Cloud Browser**, não por CLI, scripts ou pelo plugin Netlify para esse controle. Segundo a experiência informada pelo usuário, os métodos automatizados são inconsistentes e o plugin não oferece os controles necessários.

**OPS-NET-001** é uma avaliação somente leitura: identificar a configuração efetiva do projeto, os required checks GitHub dependentes dos previews, o custo operacional, a necessidade de validação hospedada e como obter um preview deliberado sem dispará-lo por acidente.

**OPS-NET-002** só existe como ação se a decisão resultante justificar alteração e houver autorização específica. Desligar previews de PR não deve inadvertidamente interromper os builds de produção.

**Estado na data desta edição:** avaliação não executada; configuração não modificada.
