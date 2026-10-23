# AUDIT-PUBLIC-TEXT-02 — proposta de consistência de contraste

> **GATE DIFERENCIAL CONCLUÍDO EM 23/10 — PASS TÉCNICO**:
> [GitHub Actions #39888294326](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326)
> na branch produto `audit/public-text-contrast-coverage-20261022@ace8510`.
> 36/36 cenários Chromium/WebKit, 36 alterações de cor válidas no light,
> 36 controles equivalentes no dark, **84 controles negativos intactos**,
> 10 pares de imagens antes/depois. Contrastes finais **4,9534:1** no canvas
> `#E8E3DC` e **5,4146:1** na superfície `#F0EDE8`. O CSS candidato
> é temporariamente injetado em browser; não integra `app/`, produção ou
> `decisions.json`. **Os novos cinco contextos continuam SEM HOMOLOGAÇÃO VISUAL**.
> [Artefato original de screenshots e JSON](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326/artifacts/12473448802).

**Data:** 22/10/2026. **Estado: experimento isolado, sem homologação de novos contextos.**
Não altera `decisions.json`, não publica CSS e não constitui decisão do usuário.

## Objetivo
Avaliar uma aplicação seletiva da cor `#705C4B` já presente no VIS-002,
evitando o antigo `#706C66` em cinco contextos de texto público onde o
[AUDIT-PUBLIC-TEXT-01](PUBLIC_TEXT_CONTRAST_AUDIT_2026-10-22.md) mediu
contrastes abaixo de 4,5:1. A imagem relatada pelo usuário pertence aos dois
parágrafos em `/about/ .about-closing`.

| Componente | Seletor | Superfície real auditada | Contraste de referência |
|---|---|---|---|
| Landing / história | `.story-section > p:not(.eyebrow)` | `#E8E3DC` | `#705C4B` ~4,95:1 |
| Landing / descrição | `.feature-copy > p:not(.eyebrow):not(.feature-availability)` | `#F0EDE8` | ~5,41:1 |
| Quem somos / fechamento | `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | `#F0EDE8` | ~5,41:1 |
| Quem somos / destaque 200+ | `.about-scale__stat > span` | `#F0EDE8` | ~5,41:1 |
| Como funciona / encerramento | `.finish-copy > p:not(.eyebrow):not(.finish-signature)` | `#F0EDE8` | ~5,41:1 |

A seleção para esses **novos consumidores** precisa de homologação explícita.
Não trocar `--public-muted` globalmente. Em especial, textos de
`.feature-availability`, a assinatura editorial `.finish-signature` com cor própria `!important`, e outros estados funcionais foram excluídos.

## Evidência experimental (não publicação)
Produto: [branch audit/public-text-contrast-coverage-20261022](https://github.com/EAKerber/MobiliPresenter2D/tree/audit/public-text-contrast-coverage-20261022).
O CSS está **somente** em `evidence/visual/public-text-contrast-candidate-v1.css`,
fora de `app/` e da publicação Netlify, sem import. O script
`tests/public-text-contrast-candidate.mjs` injeta-o temporariamente no
navegador, lendo o mesmo checkout antes/depois.

Matriz programada: 3 rotas × 3 larguras × 2 temas × Chromium/WebKit = 36
cenários, com 36 leituras de textos modificáveis por tema,
controles negativos (textos aprovados, estado indisponível, assinatura),
prova de geometria/conteúdo e screenshots antes/depois em light 390/1366.

Primeiros testes do comparador falharam por artefatos de instrumentação:
- [run #39885261277](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39885261277):
  falhou por diferença de posição da hero `public-reveal` durante a animação;
  não foi observada alteração de sua cor/conteúdo. Nenhuma conclusão estética.
- Correção subsequente no [commit 612bac4](https://github.com/EAKerber/MobiliPresenter2D/commit/612bac407665f665d5c7e2818d45c8a2ecc24f22):
  aguarda a saída do splash antes de avaliar a página.
- [run #39885540377](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39885540377):
  **FAIL**: o tempo de splash não estabilizou a animação `public-reveal`; deslocamento visual
  transitório de 14px num controle não editado.
- [run #39886228368](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39886228368):
  **FAIL**, após estabilização e comparação de controles: a regra candidata da história
  não produziu a cor esperada no CSS computado.
- [run #39886604774](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39886604774):
  **FAIL investigativo**. DOM reportou tema `light`, seletor correspondendo,
  CSS candidato encontrado na folha com declaração correta, porém a cor
  computada permaneceu `#706C66`. Não houve hipótese de regressão do produto.
- [run #39886961612](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39886961612):
  **em execução na última leitura**. O script aguarda frames de pintura e coleta
  todas as regras CSS correspondentes, prioridade e estado disabled da folha.

**HOLD técnico do candidato enquanto o último run não encerrar verde**.
A fonte CSS é deliberadamente um experimento isolado; ela não será copiada
a `app/` por inferência nem haverá PR visual prematura.

O [AUDIT-PUBLIC-TEXT-01 #39883740485](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39883740485)
continua PASS independentemente: 456 medições, cinco contextos abaixo do limiar,
36/36 verificações de pares já homologados.

## Saída e governança
1. Classificar o resultado final do gate e corrigir apenas falhas da ferramenta
   de medição, sem afrouxar contraste ou compatibilidade visual do tema escuro.
2. Inspecionar capturas antes/depois, incluindo mobile. Screenshots de navegador
   não substituem testes funcionais e dispositivos reais.
3. Solicitar homologação contextual expressa antes de inserir essas declarações
   nos CSS do produto ou promover token semântico.
4. Caso homologado, integrar em incremento próprio com gate de contraste,
   geometria, tema, regressões e rollback; reconciliar PR #231 separadamente.
5. Preservar Viewer, Config/Admin/Access, navegação, preços e política de CI #232.
Nenhum Deploy Preview foi gerado para AUDIT-PUBLIC-TEXT-02.


## Reconciliação final de falhas e escopo — 23/10/2026

- O run diagnóstico [#39886961612](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39886961612) **não estava mais em execução**: terminou FAIL. Após aguardar dois frames, a aplicação da regra CSS foi comprovada ao passar por Landing e About; o teste parou no baseline de `.finish-signature`, que usa tom próprio `#6E512E` no tema claro. Não era regressão da proposta nem motivo para forçar um `!important`.
- O commit candidato [`ace8510`](https://github.com/EAKerber/MobiliPresenter2D/commit/ace851004713f92b4425e5832c6c892825814f0a) restringiu o seletor `.finish-copy > p:not(.eyebrow):not(.finish-signature)`, protegeu a assinatura como controle negativo e substituiu a instalação repetitiva de browsers no runner por container Playwright versionado `v1.56.0-noble`. Nenhum arquivo publicado foi modificado.
- [Run #39888294326 **SUCCESS**](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326), 36/36 browser/theme/width/page; 36 alterações de cor computadas em elementos light, 36 casos dark sem qualquer alteração, 84 verificações de controles não alvos e zero alteração da propriedade global `--public-muted`. É um **PASS do experimento CSS-injetado**, não um gate de deploy/merge.
- O artefato Actions [`public-text-contrast`](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326/artifacts/12473448802), digest SHA-256 `41273f402f1450caf392a4edaa13716b1d1637b406baf516f4695b8f65487b9d`, contém relatórios JSON, 10 capturas antes e 10 depois para Chromium light em 390 e 1366 px. Os 10 pares mostram alterações de pixels de texto, com geometria computada inalterada; a comparação de dimensões PNG preservou o tamanho do recorte em 9/10, com diferença de arredondamento de 1 px de altura no recorte `390/finish`. Não inferir equivalência de página inteira desse conjunto de recortes nem conformidade universal.
- É recomendável a revisão visual humana das cinco comparações dentro do layout completo, incluindo o mobile; as capturas de um único parágrafo não representam toda a hierarquia editorial.
- **Decisão pendente:** homologar ou rejeitar o uso de `#705C4B` nos cinco novos seletores. Até lá, não introduzir CSS no produto nem abrir PR/preview visual; manter PRs #231 e #234 e a pendência de auth #232 independentes.
