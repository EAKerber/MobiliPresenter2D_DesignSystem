# P1 — registro declarativo isolado

**Somente experimento, sem deploy e sem acesso a dados privados.** Estes arquivos não são carregados pelo MobiliPresenter2D e não representam o novo schema comercial ou editorial do site.

## Arquivos

- `registry.mjs`: `createRegistry` com tipos/variantes permitidos, `compilePage` com validação completa e snapshot JSON, `renderCompiled` que devolve descritores sem montar DOM.
- `landing-benefits.mjs`: manifesto/fixture para `landing/benefit-strip@1`, reproduzindo quatro entradas existentes da `CASA_PUBLIC_LANDING.benefits` e o formato `.benefit-item` (div, img alt vazio, span).
- `registry.test.mjs`: 11 testes para sucesso/ordem/estrutura, restrições de tipo e variante, referência ausente/unsafe, ID duplicado, campo CSS não permitido, origem de imagem não autorizada, ausência de render parcial, registro duplicado e snapshot estável.

## Executar em ambiente Node com os arquivos locais

```sh
node --test experiments/declarative-ui/registry.test.mjs
```

Não exige dependências ou browser. A suite usa Node built-ins e ESM; seu resultado nativo precisa ser confirmado na CI/clone antes de marcar P1-E como PASS.

## Limitações intencionais

- Apenas descritores em memória; nenhum `document.createElement`, evento, `mount()`, `update()` ou `destroy()`. Ainda não há equivalência visual ou funcional testada.
- Sem autorizar `PageCompositionExperimental 0.1` como formato público ou persistido; nenhum payload executa código ou define CSS arbitrário.
- `dataRef` aceita caminho simples de chaves minúsculas; `type` exige namespace/versão explícitos, exemplo `landing/benefit-strip@1`. Outros domínios precisarão de contracts específicos e revisão justificada.
- A restrição de `icon` à pasta pública da Landing é **do componente de fixture**, não política global de assets.
- A cópia de JSON é deliberadamente estrita, sem `structuredClone`, para ser testável em runtimes JS simples; rejeita profundidade excessiva, ciclos, getters e chaves perigosas. Não recebe dados sensíveis.
- Um manifesto válido não concede permissão ou acesso a dados: a autorização continua no backend/DTO.
- A renderização presente em `Landing/landing.js` não foi alterada.

## Evidência de validação nesta branch

Em 2026-10-20, 11 testes passaram num executor JS in-memory sobre os conteúdos **recuperados do GitHub após os commits**. O executor removeu `import/export` e simulou as funções mínimas de `node:test` e `assert`. **Isso não foi uma execução Node `--test` nativa.** Houve tentativa de obter o conteúdo via `curl` no container para executar Node, mas o ambiente não resolveu `raw.githubusercontent.com`. Não marcar testes de navegador, captura visual, CI ou produção como PASS.

Referências: [UI-ADR-001](../../docs/architecture/ui-adr-001-declarative-boundaries-2026-10-20.md) e [plano incremental](../../docs/architecture/declarative-ui-increment-plan-2026-10-20.md).
