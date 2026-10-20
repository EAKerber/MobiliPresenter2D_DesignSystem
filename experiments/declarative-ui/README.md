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

Em 2026-10-20, os 11 testes foram executados **nativamente em Node 22 por GitHub Actions**, com `node --test experiments/declarative-ui/registry.test.mjs`: **11 PASS, 0 FAIL**. [Execução PR #39502842741](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39502842741) e [execução push #39502842309](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39502842309), ambas SUCCESS. Também houve execução in-memory prévia com shim; essa prova anterior não substitui a nativa. **Ainda não são testes de navegador, captura visual, integração com o produto ou produção.**

Referências: [UI-ADR-001](../../docs/architecture/ui-adr-001-declarative-boundaries-2026-10-20.md) e [plano incremental](../../docs/architecture/declarative-ui-increment-plan-2026-10-20.md).
