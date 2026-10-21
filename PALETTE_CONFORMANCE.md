# Paleta e conformidade visual

**Estado:** registro de valores contextualizados e plano de fechamento da paleta; registra a paleta-base aprovada, mas ainda não declara conformidade global da interface.  
**Fonte canônica de decisões:** [decisions.json](decisions.json).  
**Baseline histórica do documento:** snapshot `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`; veja o adendo de runtime em 2026-10-20 para a publicação atual.  
**Inventário:** [VISUAL_INVENTORY.md](VISUAL_INVENTORY.md), [visual-inventory.json](visual-inventory.json) e [DECISION_APPLICATION_MAP.md](DECISION_APPLICATION_MAP.md).

## O que conformidade quer dizer

Uma tela só está conforme quando, no escopo auditado:

1. Cada cor tem um papel semântico claro: texto principal/secundário, superfície, borda, informação de processo, promoção, erro, aviso, sucesso, seleção, foco ou estado indisponível.
2. O papel e o par de cores usados estão aprovados para aquela superfície, tema e estado. Um valor visto no CSS é apenas uso atual; não se torna token por existir.
3. O DOM renderizado usa o par aprovado, sem transparência/gradiente não medidos que alterem o fundo real.
4. O contraste atende ao alvo documentado: texto comum ≥ 4,5:1; texto grande ≥ 3:1; limites de componentes/indicadores visuais significativos ≥ 3:1 quando aplicável. Compare sem arredondar para alcançar o limiar. Referência: WCAG 2.2 AA, critérios 1.4.3 e 1.4.11.
5. A informação não depende apenas da cor: estado, ação, seleção e feedback também têm indicador textual, estrutural ou iconográfico adequado.
6. Estados pertinentes (normal, hover, foco, pressionado, selecionado, carregando, indisponível e erro/sucesso quando existentes) mantêm legibilidade, distinguibilidade e operação por teclado/toque. Foco é verificado em separado.
7. O resultado é conferido nas rotas, temas, breakpoints e dados/estados dinâmicos cobertos. Cada combinação sem evidência fica marcada não verificada, não presumida conforme.

Contraste é uma condição necessária, mas não prova sozinho a conformidade: semântica errada, estado ausente, texto ilegível na composição real ou interação quebrada ainda são falhas.

## Paleta homologada até agora

| Papel / contexto | Valor ou par | Estado | Limite |
|---|---|---|---|
| Base neutra aprovada para paleta de interface | Canvas claro/escuro `#E8E3DC` / `#171614`; superfície `#F0EDE8` / `#211F1C`; superfície suave `#DED9D2` / `#2C2924`; textos `#292723` / `#F0EAE1` e `#705C4B` / `#C7BBAA`; bordas `#D6CCC0` / `#4E4942` | Valores de paleta aprovados pelo usuário (VIS-002) | A aplicação global por componente e a verificação fora dos contextos medidos continuam pendentes. `#F0EDE8` evita branco puro; `#171614` evita preto puro. |
| Foco da paleta aprovada | Contorno `#8B6A40` / `#D8BC7C`, 4 px com offset 3 px | Tratamento visual aprovado (VIS-002) | Validar teclado e contraste em componentes reais. |
| Informação promocional de produto e campanhas | Base cobre `#A64D13` | Papel e base aprovados (VIS-002) | Não é warning técnico. Variantes light/dark, superfícies, texto e contraste continuam por homologar. |
| Informação de processo/funcionamento | Claro: `#245D87` sobre `#F0EDE8` (6,01:1); escuro: `#A7D1F0` sobre `#211F1C` (10,19:1) | Pares contextuais de texto aprovados pela opção A (VIS-002); aplicação no produto pendente | Na observação de `/admin.html` em 2026-10-19, a mensagem de estado atual sobre configuração carregada foi classificada como informação de processo; o DOM escuro então usava `#C4BCB2` sobre `#111210` (10,00:1), sem aplicar o par azul aprovado. Essa mensagem não foi reavaliada na PR #42. A aprovação não cria tokens globais nem cobre outras superfícies, fundos, bordas ou ícones; ver evidência runtime. |
| Texto auxiliar claro em três contextos públicos auditados | `#705C4B` sobre `#F0EDE8` (5,41:1) | Par aprovado, aplicado e verificado pós-deploy no tema claro nos três seletores listados | `.hero-description`, `.how-hero-note`, `.about-scale p:not(.eyebrow)`. Sem promoção a token global. FIND-002 / issue #216 permanece aberto.
| Rótulo quente claro em Como funciona | `#70522F` sobre `#E8E3DC`, 5,60:1 | Par contextual aprovado e verificado pós-deploy no tema claro | `.study-band .eyebrow` somente. Sem promoção a token global.
| Legenda da ilustração no tema escuro | `#F0EDE8` sobre `#20211F`, 13,85:1 | Par contextual aprovado (VIS-003 / FIND-004), seleção A; DOM verificado em 2026-10-20 e rechecado em 2026-10-21; captura visual da segunda data não persistida | `.study-art figcaption` em `/how-it-works/`, tema escuro. Não global; issue #217 permanece aberto.
| Erro, sucesso e aviso técnico | Pares contextuais de texto/fundo aprovados para cada estado e tema | Seleção do usuário pela maior razão de contraste entre as alternativas; pares aprovados não equivalem a tokens globais nem definem todos os usos | Mapear os componentes reais, preservar distinção semântica e validar superfícies; não reaproveitar cobre promocional como aviso técnico. Ver `decisions.json` e a prancha `VIS-002-semantic-states-selected.svg`. |
| Foco, seleção, hover, pressionado, desabilitado e carregamento | Sem paleta completa homologada | Direções de comportamento em VIS-002 e EST-01–06; combinações por componente/tema pendentes | Validar indicação não cromática e estados reais. |

## O que precisa mudar na interface observada

Esta lista aponta trabalhos requeridos pela evidência atual. Não é autorização para alterar o produto; cada correção de código precisa ser executada e revisada no repositório do produto.

| Área | Estado observado | Mudança para conformidade | Registro |
|---|---|---|---|
| `/`, `/how-it-works/`, `/about/` | Pares anteriores mediram 4,47:1; depois da PR #219, os três seletores aprovados mediram 5,41:1 no DOM publicado em 2026-10-20 | Mantido conforme homologado nos três contextos; sem generalização. Issue #216 permanece aberto | FIND-002 |
| `/how-it-works/` eyebrow | Após a aplicação, `#70522F` sobre `#E8E3DC` mediu 5,60:1 no DOM publicado em 2026-10-20 | Par mantido somente no seletor homologado; issue #216 permanece aberto | FIND-003 |
| `/how-it-works/` legenda da figura | Após a aplicação, `#F0EDE8` sobre faixa opaca `#20211F` mediu 13,85:1 no DOM publicado em 2026-10-20; revisão visual separada em captura de navegador em 2026-10-21 (arquivo não persistido) | Par visual aprovado foi confirmado no viewport observado; responsividade e demais temas não foram verificados. Issue #217 permanece aberto | FIND-004 |
| Configurador, etapas Serviços/Resumo | Contador reporta 8/8 com módulos desmarcados; iluminação indisponível entra no total | Corrigir primeiro a semântica/contagem (decisão funcional do produto); depois medir contraste no DOM em ambos temas | FIND-006, issue produto #209. Não é correção só de paleta. |
| Configurador, Resumo claro | Rótulo Módulos com legibilidade baixa observada, sem razão runtime nova | Medir par real; selecionar/aplicar um par aprovado e verificar hierarquia | FIND-010, issue produto #208 |
| Administração / editor | Auditoria estática antiga aponta riscos remanescentes em DS04-02–07, 09–10 e 12; inspeção runtime por seletor pendente | Confirmar cada achado em DOM real nos temas/estados; corrigir apenas os confirmados e registrar exceções justificadas | FIND-008, issue produto #208 |
| Administração / mensagens de estado | Uma mensagem de estado atual foi classificada como informação de processo; outros estados permanecem sem mapeamento runtime | Usar papel azul para a mensagem mapeada; mapear sucesso, aviso e erro separadamente. Medir cada estado e superfície antes de fixar tokens | VIS-002, evidência runtime `admin-dark-status-message-2026-10-19.md` |
| Login e gerenciamento de acessos | Menus/sessão têm relatos intermitentes, que não são defeito cromático | Resolver confiabilidade funcional separadamente; revisar contraste/foco visual dos estados efetivamente renderizados | FIND-005/007, issues #212/#213 |
| Menu no configurador estreito | Uma imagem da cena cobre link do menu em largura estreita | Corrigir empilhamento/hit-testing e revalidar a interação; não classificar como paleta | FIND-009, issue #214 |
| Labels e controles Ativa / Iniciar ativo | Cor atual é inconsistente entre telas | Aplicar papel informativo aprovado somente após identificar se descreve processo, estado ou configuração; evitar solução baseada em cor sem semântica confirmada | VIS-002 / EST-01, pendente de mapeamento |

## Proposta inicial para revisão

O usuário aprovou a paleta A: ela retira `#675F55` do papel secundário, substitui o foco discreto `#6E512E` por contornos mais visíveis e troca a superfície branca pura `#FFFFFF` por marfim quente `#F0EDE8`. A regra é para superfícies de interface; não altera imagens, logotipos ou ilustrações. Veja os arquivos abaixo. A decisão está registrada no [quadro da paleta A](visualEvidence/experiments/PALETTE-candidate-A-v2.svg) e em [sua especificação](visualEvidence/experiments/PALETTE-candidate-A.md). Ela reutiliza os neutros e estados mais recorrentes do snapshot, e mantém esses papéis como valores homologados de paleta. A criação de tokens e a aplicação no produto ainda dependem do inventário de componentes, mapeamento e validação runtime. Os contrastes do quadro são pares de amostra; os estados de foco, indisponível, seleção e a promoção no tema escuro seguem para revisão.

## Como fechar a paleta total

A paleta global ainda não está fechada porque os papéis de processo têm família aprovada sem pares exatos, e estados técnicos, superfícies, tema e componentes não têm pares homologados suficientes. O caminho proposto:

1. Extrair do inventário os valores realmente usados e agrupar por papel observado, arquivo, seletor, tema, rota e estado. Manter valores sem contexto em uso atual / papel desconhecido.
2. Confirmar em DOM real o que muda por tema e estado; compor o fundo efetivo de transparências, imagens, gradientes e overlays.
3. Propor poucos pares por papel semântico, não uma lista de hexadecimais sem uso. Preservar cobre promocional e azul de processo como papéis distintos.
4. Medir texto comum, texto grande, bordas/indicadores e ícones funcionais; documentar alvo, par e superfície. Apresentar alternativas visuais quando houver decisão estética não determinada.
5. Homologar cada par em `decisions.json`, incluindo escopo explícito. Só então marcar token como oficial. Cores descobertas no CSS continuam uso atual.
6. Aplicar mudanças no produto por famílias de componentes e por PR. Após cada aplicação, conferir DOM real em light/dark, viewports e estados. Atualizar o mapa e findings.
7. Fechar a paleta somente quando todos os papéis visuais em uso estiverem mapeados, nenhuma ocorrência importante estiver sem papel e cada par usado estiver aprovado ou formalmente justificado como exceção.

## Estados do inventário

- **Homologado — valor exato:** par/cor e seu escopo foram aprovados; não generalizar além dele.
- **Homologado — papel:** semântica foi aprovada, mas faltam valores/pares. Exemplo: azul para informação de processo.
- **Uso atual:** valor existente no produto, sem aprovação automática.
- **Candidato:** alternativa preparada para revisão, ainda sem escolha.
- **Pendente:** falta decidir valor, comportamento ou extensão de escopo.
- **Não verificado:** não há observação suficiente no runtime/estado/tema para afirmar.
- **Exceção justificada:** desvio aprovado com razão, escopo e alternativa documentados.

## Referências

- [WCAG 2.2, critério 1.4.3 — contraste mínimo](https://www.w3.org/TR/WCAG22/#contrast-minimum)
- [WCAG 2.2, critério 1.4.11 — contraste não textual](https://www.w3.org/TR/WCAG22/#non-text-contrast)
- `decisions.json` — fonte canônica de decisões, aprovações e limites.
- `visual-inventory.json` — inventário estático com linha de origem e contexto.
- `FINDINGS_REGISTER.md` — defeitos e pendências observados.

## Adendo runtime — validação pós-deploy de contextos aprovados (2026-10-20)

A publicação de produção `1878ae1057ce7c6190e0c8cb08a1f3baadd49463` / Netlify `6ad6c3b51b6be05647167f94` foi inspecionada em `1280x720` CSS px. O DOM confirmou os três textos auxiliares claros em 5,41:1, o rótulo eyebrow claro em 5,60:1 e a faixa escura da legenda FIND-004 em 13,85:1. Valores, seletores e limitações estão em [evidência detalhada](evidence/runtime/contrast-approved-pairs-2026-10-20.md); uma captura da legenda foi revisada separadamente em 2026-10-21, mas seu arquivo não foi persistido nesta PR.

Esta confirmação substitui apenas o estado “pós-deploy pendente” para os seletores/temas listados. Os issues #216 e #217 continuam abertos até serem atualizados no backlog do produto. Não declara conformidade de toda a paleta, não promove tokens globais e não valida outros papéis, superfícies, interações, foco ou breakpoints. O corpo histórico do documento continua útil para baseline anterior à aplicação.
