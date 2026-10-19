# Paleta e conformidade visual

**Estado:** registro de valores contextualizados e plano de fechamento da paleta; registra a paleta-base aprovada, mas ainda não declara conformidade global da interface.  
**Fonte canônica de decisões:** [decisions.json](decisions.json).  
**Produto mapeado:** snapshot `298c11441f82cacfff2f809fd9e5ad6f1fc33c0a`; deploy/runtime observado em 2026-10-18.  
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
| Base neutra aprovada para paleta de interface | Canvas claro/escuro `#E8E3DC` / `#171614`; superfície `#F0EDE8` / `#211F1C`; superfície suave `#DED9D2` / `#2C2924`; textos `#292723` / `#F0EAE1` e `#705C4B` / `#C7BBAA`; bordas `#D6CCC0` / `#4E4942` | Valores de paleta aprovados pelo usuário (VIS-002) | Aplicação por componente e verificação de contraste no DOM pendentes. `#F0EDE8` evita branco puro; `#171614` evita preto puro. |
| Foco da paleta aprovada | Contorno `#8B6A40` / `#D8BC7C`, 4 px com offset 3 px | Tratamento visual aprovado (VIS-002) | Validar teclado e contraste em componentes reais. |
| Informação promocional de produto e campanhas | Base cobre `#A64D13` | Papel e base aprovados (VIS-002) | Não é warning técnico. Variantes light/dark, superfícies, texto e contraste continuam por homologar. |
| Informação de processo/funcionamento | Família azul | Papel aprovado (VIS-002); valores exatos ainda não homologados como tokens | `--info: #245d87` (light) e `#a7d1f0` (dark) existem em `app/admin/admin.css`; são uso atual a conferir no runtime, não valores oficiais. |
| Texto auxiliar claro em três contextos públicos auditados | Par anterior `#675F55` sobre `#F0EDE8`; substituto aprovado na paleta `#705C4B` | Par anterior reaberto após feedback estético; tom da paleta aprovado; aplicação pendente | `.hero-description`, `.how-hero-note`, `.about-scale p:not(.eyebrow)`. Não implementar até nova revisão; ver PR20.
| Rótulo quente claro em Como funciona | `#70522F` sobre `#E8E3DC`, 5,60:1 | Par contextual aprovado (VIS-002) | `.study-band .eyebrow` somente. |
| Legenda da ilustração no tema escuro | `#F0EDE8` sobre `#20211F`, 13,85:1 | Par contextual aprovado (VIS-003 / FIND-004), seleção A | `.study-art figcaption` em `/how-it-works/`, tema escuro. Não global; aplicação no produto pendente. |
| Erro, sucesso e aviso técnico | Sem token homologado neste registro | Semântica reconhecível e harmonizada com marca é direção; valores/candidatos visuais não aprovados | Não reaproveitar cobre promocional como warning automaticamente. |
| Foco, seleção, hover, pressionado, desabilitado e carregamento | Sem paleta completa homologada | Direções de comportamento em VIS-002 e EST-01–06; combinações por componente/tema pendentes | Validar indicação não cromática e estados reais. |

## O que precisa mudar na interface observada

Esta lista aponta trabalhos requeridos pela evidência atual. Não é autorização para alterar o produto; cada correção de código precisa ser executada e revisada no repositório do produto.

| Área | Estado observado | Mudança para conformidade | Registro |
|---|---|---|---|
| `/`, `/how-it-works/`, `/about/` | Texto auxiliar claro medido em 4,47:1 nos seletores indicados | Não aplicar o par reaberto `#675F55`; revisar o candidato marrom `#705C4B` (5,41:1 na superfície `#F0EDE8`) e validar DOM após aprovação | FIND-002, issue produto #216 |
| `/how-it-works/` eyebrow | 3,89:1 no tema claro | Aplicar `#70522F` sobre `#E8E3DC` somente no seletor auditado | FIND-003, issue produto #216 |
| `/how-it-works/` legenda da figura | 1,78:1 no estado auditado do tema escuro | Criar faixa opaca `#20211F` com texto `#F0EDE8`; manter a legenda visualmente integrada; conferir imagem e layout em viewports variados | FIND-004, issue produto #217 |
| Configurador, etapas Serviços/Resumo | Contador reporta 8/8 com módulos desmarcados; iluminação indisponível entra no total | Corrigir primeiro a semântica/contagem (decisão funcional do produto); depois medir contraste no DOM em ambos temas | FIND-006, issue produto #209. Não é correção só de paleta. |
| Configurador, Resumo claro | Rótulo Módulos com legibilidade baixa observada, sem razão runtime nova | Medir par real; selecionar/aplicar um par aprovado e verificar hierarquia | FIND-010, issue produto #208 |
| Administração / editor | Auditoria estática antiga aponta riscos remanescentes em DS04-02–07, 09–10 e 12; inspeção runtime por seletor pendente | Confirmar cada achado em DOM real nos temas/estados; corrigir apenas os confirmados e registrar exceções justificadas | FIND-008, issue produto #208 |
| Administração / sucesso, processo, avisos | Há cores locais; mapeamento runtime incompleto | Distinguir azul funcional, warning técnico, erro e sucesso por papel; medir pares usados antes de criar tokens | VIS-002, EST-06, inventário |
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