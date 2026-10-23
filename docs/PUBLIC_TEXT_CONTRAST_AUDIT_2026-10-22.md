# AUDIT-PUBLIC-TEXT-01 — contraste computado nas páginas públicas (22/10/2026)

## Estado e alcance
**PASS técnico de auditoria, sem correções visuais integradas.** Executado no
[Actions #39883740485](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39883740485),
produto [branch audit/public-text-contrast-coverage-20261022@35d9c22](https://github.com/EAKerber/MobiliPresenter2D/tree/audit/public-text-contrast-coverage-20261022),
base exata `main@15e1cfb4866886649adbcd00fef9bef5e5843fda`.

Código: `tests/public-text-contrast-coverage.mjs`, sem tocar `app/`, sem PR,
sem Netlify Preview, sem login/fixture privada. Comando do workflow serve os três HTML
públicos de `app/` por loopback e lê CSS computado em Chromium e WebKit.
O artefato `public-text-contrast/report.json` está no run.

**Matriz:** 3 rotas (`/`, `/about/`, `/how-it-works/`) × 3 larguras
(390, 768, 1366) × 2 temas (light/dark) × 2 navegadores = **36/36 cenários PASS**.
São 456 observações de elementos selecionados, **388 aprovadas por limiar,
36 candidatas abaixo do limiar, 32 não verificadas**.
Os quatro pares contextuais de cor já homologados passaram **36 verificações individuais**.

## Achados abaixo do limiar de 4,5:1

| Rota / seletor | Cor sobre superfície (tema claro) | Contraste mínimo | Amostras abaixo | Priorização |
|---|---|---:|---:|---|
| Landing, `.story-section > p:not(.eyebrow)` | `#706C66` sobre `#E8E3DC` | **4,09:1** | 6 | Primeiro: desvio mais evidente |
| Landing, `.feature-copy > p:not(.eyebrow)` | `#706C66` sobre `#F0EDE8` | **4,47:1** | 6 | Revisar variação/estado da feature |
| Quem somos, `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | `#706C66` sobre `#F0EDE8` | **4,47:1** | 12 | Caso relatado pelo usuário na imagem; dois parágrafos |
| Quem somos, `.about-scale__stat > span` | `#706C66` sobre `#F0EDE8` | **4,47:1** | 6 | Mesmo cartão com outros parágrafos já corrigidos |
| Como funciona, `.finish-copy > p:not(.eyebrow)` | `#706C66` sobre `#F0EDE8` | **4,47:1** | 6 | Mesmo papel visual, ainda não homologado nesse contexto |

**Importante:** 36 são medições/cenários repetidos, **não 36 defeitos independentes**.
Nos casos com fonte suficientemente grande há limiar de 3:1, já considerado pelo código;
estes casos acima ficaram abaixo do limiar aplicável nos cenários testados.

Os **32 não verificados** vieram de `.environment span` (20 observações
não verificadas entre os dois temas) e `.feature-copy` (12 observações
não verificadas). Motivos são registrados individualmente no JSON:
elemento não visível, gradiente/imagem, transparência ou cor não interpretada.
Não inferir falha nem conformidade nesses contextos. **Também não inferir
conformidade de todos os outros elementos fora dos seletores amostrados**.

## Decisão de token e governança
Os pares VIS-002 previamente homologados permanecem restritos aos seus seletores:
`.hero-description`, `.how-hero-note`, `.about-scale p:not(.eyebrow)`,
e par `#70522F/#E8E3DC` para `.study-band .eyebrow`.
**Esta auditoria não amplia a homologação** de `#705C4B` a outro seletor.
É um candidato especialmente promissor onde a superfície é `#F0EDE8` e o texto
tem o mesmo papel; porém ainda requer aprovação contextual e gate de browser após a mudança.

O índice é uma primeira passada orientada a risco sobre texto público, não um
laudo completo de WCAG: não compõe backgrounds alpha/imagens/pseudo-elementos,
não cobre Viewer/Admin/Config, estado de foco e leitura autenticada.
No produto, PR #231 (tokens) e PR #234 (header) seguem independentes e em HOLD
pela fixture de CI da issue #232. A próxima correção deve ser **separada, mínima,
revisável e sem mudança global de `--public-muted`**.

## Proposta de próximo gate
1. Homologar os cinco papéis/superfícies como pares contextuais, dando prioridade
à Landing story (4,09:1) e à seção `.about-closing` mostrada pelo usuário.
2. Implementar somente os seletores aprovados, respeitando tema e variante, sem
introduzir token global nem tocar JS/domínio.
3. Comparar CSS computado, DOM e pixels antes/depois nos dois navegadores e três
larguras, além de inspeção visual humana; registrar rollback.
4. Tratar os 32 não verificados com protocolo de visibilidade/composição apropriado,
não contando como PASS nem FAIL até haver evidência.
