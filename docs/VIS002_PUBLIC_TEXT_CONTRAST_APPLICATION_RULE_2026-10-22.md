# VIS-002C — autorização contextual e regra preventiva de contraste textual

**Data:** 22/10/2026 (America/Sao_Paulo). **Decisão expressa do usuário neste turno:** utilizar as cores já homologadas e corrigir/prevenir a escolha de pares inadequados, preferindo regras reproduzíveis a aplicações acidentais.

## Diagnóstico causal

A cor legada `--public-muted: #706C66` do produto é declarada em `app/public-theme.css`. Não há evidência de gerador de Design System que tenha recomendado automaticamente a combinação legada. CSS com `color: var(--public-muted)` foi reutilizado em fundos `#E8E3DC` e `#F0EDE8`, abaixo de 4,5:1 para texto comum, sem um gate por contexto. O problema é **ausência de vínculo verificado entre papel semântico, superfície, tema e estado**, não deficiência de um algoritmo de otimização de cores.

## Decisão delimitada

Aprovar a **extensão contextual** do uso do texto secundário já homologado `VIS-002.approvedPalette.colors.textSecondary.light = #705C4B` aos cinco textos legíveis abaixo, **somente no tema claro**, sem aprovar alteração do token global nem troca irrestrita da paleta:

| Rota | Seletor contextual aprovado | Fundo observado no gate | Razão esperada |
|---|---|---|---:|
| `/` | `.story-section > p:not(.eyebrow)` | `#E8E3DC` | 4,9534 |
| `/` | `.feature-copy > p:not(.eyebrow):not(.feature-availability)` | `#F0EDE8` | 5,4146 |
| `/about/` | `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | `#F0EDE8` | 5,4146 |
| `/about/` | `.about-scale__stat > span` | `#F0EDE8` | 5,4146 |
| `/how-it-works/` | `.finish-copy > p:not(.eyebrow):not(.finish-signature)` | `#F0EDE8` | 5,4146 |

**Exceções obrigatórias:** manter `.feature-availability`, `.finish-signature`, `.about-closing__signature`, tags `.eyebrow`, pares aprovados anteriores e todos os textos no tema escuro. Não alterar domínio, mensagens comerciais, autenticação nem `--public-muted` globalmente.

## Norma preventiva — contrato operacional

1. Um valor da paleta ser homologado **não significa** que qualquer par de cores ou consumidor o seja. A chave de associação é `(papel semântico, rota/componente, estado, tema, fundo efetivo, tamanho/peso)`.
2. Antes de usar novo token ou estender um papel a um consumidor: verificar par texto/fundo em CSS computado, incluindo cascata real, superfície opaca, transparência, imagens e estados pertinentes. Texto normal: contraste `>= 4.5`; texto grande: `>= 3`; componente/indicador significativo: `>= 3` onde aplicável. Nunca arredondar para atingir o limiar.
3. **Fail closed** por seletor/estado homologado: rota ausente, tema errado, par diferente, regra vencedora incerta, razão insuficiente ou mudança na semântica dos estados reprovam o gate. Um caso com fundo/foreground não aferível vira `UNVERIFIED`, nunca PASS.
4. Preferir o valor de token/papel homologado; **não criar um algoritmo gerador de cores** que escolha a alternativa esteticamente por conta própria. Um eventual mecanismo de sugestões pode listar candidatos, contrastes e evidências, mas não pode escrever CSS de produção ou transformar um candidato em aprovado.
5. A mudança aplicada deve ser local, aditiva e reversível; teste de exclusões (estados, assinaturas) e tema escuro precisa ficar junto ao contrato. Comparação de browser não substitui inspeção visual completa nem teste funcional de dispositivos.
6. **Prevenção contínua:** quando o componente mudar cor/fundo/tema/estado, reexecutar os checks de CSS computado e atualizar allowlist homologada ou bloquear a mudança. O gate cobre apenas escopo explicitado; outras páginas continuam `not-evaluated`.

## Evidência de autorização e implementação

- [Inventário AUDIT-PUBLIC-TEXT-01](PUBLIC_TEXT_CONTRAST_AUDIT_2026-10-22.md): 36/36 cenários; cinco contextos falhando antes da correção.
- [Experimento visual AUDIT-PUBLIC-TEXT-02](PUBLIC_TEXT_CONTRAST_CANDIDATE_2026-10-22.md), [Actions #39888294326](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326): 36/36 browser scenarios, 36 alterações light, 36 equivalências dark, 84 controles negativos e capturas comparativas. **O PASS do experimento não representa sozinho homologação de produção ou validação de todos os dispositivos.**
- Decisão deste turno autoriza o mapeamento contextual acima; o patch do produto fica em branch independente com gate próprio. **Nenhuma instrução de merge ou publicação automática**.

## Compatibilidade com o pipeline canônico

`decisions.json` contém `VIS-002.approvedPalette` como origem dos **valores**, e o exportador P-TOKEN-01 fixa seu Git blob SHA para impedir alterações silenciosas. **Este contrato de mapeamento contextual não altera a paleta nem o blob de decisions.json**: é um adendo de consumidores homologados, versionado por documento, até integração explícita ao schema/pipeline de tokens com atualização de versão, hashes e testes. Evitar desarmar o gate pinado para registrar a nova regra.

## Implementação em branch — 23/10/2026

- Produto: [`fix/vis002c-public-text-contrast-20261022@b0eb52f`](https://github.com/EAKerber/MobiliPresenter2D/tree/fix/vis002c-public-text-contrast-20261022), partindo de `main@15e1cfb`; diffs em três arquivos CSS de páginas e quatro arquivos de testes/CI/documentação, sem alterar o token `--public-muted`.
- [Gate inicial #39890281124 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39890281124): CSS contract e browser checks PASS. 36 cenários Chromium/WebKit, 72 checagens de pares contextualizados, 456 medições (424 satisfatórias, zero abaixo, 32 não verificadas).
- [Gate definitivo #39890589800 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39890589800): mesma matriz PASS após tornar o gate reutilizável em futuras PRs para `main` e push `main` **quando o incremento for integrado**; o contrato deixa CSS adicionais legítimos serem escritos, desde que não se percam os pares/contextos aprovados e as regras vencedoras computadas continuem corretas.
- **Gate conservado no produto:** `.github/workflows/vis002c-public-contrast.yml`, `tests/vis002c-css-contract.test.mjs` e `tests/vis002c-public-contrast.mjs`; nenhum algoritmo gera cores, nenhum requisito `!important`, nenhuma modificação global nem exceção silenciosa.
- **Estado:** implementação verificada em branch; **sem PR, Deploy Preview, merge ou release**. Validar composição de página completa e CI global antes de integrar. Os 32 casos não verificados não são homologados por inferência.


## Gate de integração visual de página inteira — 23/10/2026

- [Run #39891404267 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39891404267), produto `fix/vis002c-public-text-contrast-20261022@007fc8e`. Os dois jobs (`css-contract` e `browser-contrast`) passaram.
- Conformidade contextual no app real: **36/36 cenários**, 72 verificações de pares, 456 medições = **424 com contraste satisfatório**, zero abaixo do limiar e 32 `UNVERIFIED` (não declarar conformidade nos 32).
- Gate novo `tests/vis002c-full-page-visual.mjs`: **12/12 pares full-page** nas três rotas × 390/1366 × Chromium/WebKit (tema claro). O baseline anterior é reconstituído via CSS temporário na mesma página para evitar ruído de DOM/JS; o CSS é removido para o after. **90.315 pixels com diferença real, nenhum pixel modificado fora das caixas dos textos autorizados**; mesmo tamanho e geometria dos screenshots.
- [Artefato auditável (12 pares de imagens e JSON)](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39891404267/artifacts/12475036038), hash SHA-256 `41f1efea780f853b18fab5b2b60ff85c1b5ece7be66f1da2ecd9696d0c1abadb`. Inspeção visual de composições Chromium mobile/desktop e comparação do fechamento da About não revelou mudança de layout ou hierarquia além da cor do texto; o gate não verifica todos os estados e mídias possíveis.
- **HOLD para integração:** [PR #231](https://github.com/EAKerber/MobiliPresenter2D/pull/231) também altera `app/landing/landing.css`, `app/about/about.css` e `app/how-it-works/how-it-works.css`; usa a variável contextual gerada `--ds-vis002-approved-support-text-light` apenas nos três consumidores anteriores, mantendo `#705C4B` em fonte canônica. VIS002C deve ser reconciliado com o consumidor/data mapping de P-TOKEN-02B quando a PR for integrada, sem criar duas autoridades permanentes da mesma cor. Não editar a PR #231 indiscriminadamente e reexecutar os dois gates após a reconciliação.
- [PR #234](https://github.com/EAKerber/MobiliPresenter2D/pull/234) toca HTML/compilador, mas não as três CSS; ainda requer respectivo gate. [Issue #232](https://github.com/EAKerber/MobiliPresenter2D/issues/232) impede afirmar CI global verde: fixtures privadas sem login dão falhas herdadas. Preservar HOLD; não desarmar auth nem gerar previews repetidos.
- **Nenhuma PR nova, nenhum Deploy Preview, merge ou publicação no VIS002C até este checkpoint.** O ganho visual foi testado em branch, mas não está no domínio público.


## Reconciliação concluída com P-TOKEN-02B — v0.2.0 (23/10/2026)

**Estado: gate de integração isolado PASS; merge/publicação não autorizados.**

- **Autoridades separadas e precisas:** `VIS-002.approvedPalette.colors.textSecondary.light` em `decisions.json@63b60f8` fornece exclusivamente o valor `#705C4B`. O arquivo data-driven [`VIS002C_CONTEXTUAL_MAPPING_V0_2_0.json`](VIS002C_CONTEXTUAL_MAPPING_V0_2_0.json) contém exclusivamente as oito associações `route, selector, background, authorization` (três originais e cinco adicionadas). Não duplica o valor da cor. Git blob do mapa: `717b400da8d5590a03118e4ce58f07fcbababc48`.
- **Produto:** branch [`integration/vis002c-p-token-02b-v2-20261023@34a305c`](https://github.com/EAKerber/MobiliPresenter2D/tree/integration/vis002c-p-token-02b-v2-20261023) baseada em [PR #231](https://github.com/EAKerber/MobiliPresenter2D/pull/231) `afb80965` (mantida intocada). Distribuição v0.1 pinada por hash **não modificada**; nova v0.2 pinada por hash entrega uma única definição do mesmo `--ds-vis002-approved-support-text-light` apenas nos oito seletores aprovados; três páginas públicas carregam **somente v0.2**. Os três CSS de componente consomem `color: var(...)` sem cor literal concorrente; `--public-muted` legado, tema escuro, Viewer/Admin/Config/Access, JS e comportamento comercial preservados.
- **Conformidade:** [GitHub Actions #39894163198 — SUCCESS](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39894163198), jobs `pin-and-contract` e `browser` verdes. **48/48** screenshots byte-idênticos (e CSS computado idêntico) nos três consumidores antigos, comparando v0.1 e v0.2 na mesma página; **36/36** cenários de contraste (72 pares homologados, 456 observações: 424 PASS, **0 abaixo**, 32 não verificadas); **12/12** pares de páginas integrais Chromium/WebKit, larguras 390/1366, tema claro, com **90.315 pixels modificados exclusivamente nos cinco textos aprovados, zero fora**.
- **Evidência durável:** [artefato Actions v0.2](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39894163198/artifacts/12476630137), SHA-256 `cdf5263a6bd4075075091cf18391e8ec1195c270205c244b4f03333c8a55b861`. [Checkpoint técnico detalhado no produto](https://github.com/EAKerber/MobiliPresenter2D/blob/integration/vis002c-p-token-02b-v2-20261023/docs/architecture/vis002c-p-token02b-integration-2026-10-23.md).
- **Diagnóstico e preservação de rigor:** teste lexical histórico da P-TOKEN-01B passou a ler os bytes do `sourceCommit` que o próprio inventário registra, evitando tratar uma amostra antiga como estado atual. Comparador de três seletores antigos passou a alternar v0.1/v0.2 **no mesmo DOM** em vez de comparar animações de carregamentos independentes; raster tem exigência de igualdade exata. O gate full-page intercepta apenas o HTML da incorporação `www.youtube-nocookie.com/embed/` com fixture estável no CI, preservando iframe, layout e player real; diferenças fora dos textos continuam falhando o teste.
- **Integração futura em HOLD:** PR #231 continua DRAFT, PR #234 (ARC-03C) DRAFT e a issue [#232](https://github.com/EAKerber/MobiliPresenter2D/issues/232) ainda exige fixture autenticada para os testes privados. Não introduzir preview repetitivo nem fazer merge sob CI global vermelho. A versão v0.2 depende da base da PR #231; planejar ordem de integração e readback de produção antes de qualquer publicação.

A aprovação dos cinco contextos do usuário refere-se ao papel visual e ao patch restrito; **não generaliza `VIS-002.implementationAuthorized` para o produto inteiro** e não autoriza token global.
