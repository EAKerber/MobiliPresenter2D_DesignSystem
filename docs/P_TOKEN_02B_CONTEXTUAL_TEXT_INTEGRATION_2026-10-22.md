# P-TOKEN-02B — primeiro consumo real DS→produto, escopo VIS-002 contextual

**Data:** 2026-10-22. **Estado:** gerador DS integrado, consumidor em **branch de produto isolada**, sujeito a validação diferencial. **Não publicar automaticamente.**

## Autoridades

- [ARC-02, ARC-04, ARC-05, ARC-14, ARC-15 e ARC-16](ARCHITECTURE_DECISIONS_ARC01_ARC16_AND_EXECUTION_2026-10-21.md).
- `decisions.json > VIS-002.approvedRuntimePairs[0].candidateReplacement`: **#705C4B** em três seletores já aprovados e previamente aplicados/medidos pela PR #219 (tema claro), sobre superfície `#F0EDE8`. Esta homologação é **contextual**, não global.
- `VIS-002.approvedPalette.colors.textSecondary.light=#705C4B` coincide numericamente com a cor acima, mas `VIS-002.implementationAuthorized=false` continua **proibindo mapeamento universal de tokens ou redesign por inferência**.

## Fonte executável no Design System

- [PR #50](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/50) — **MERGED**, `8f22b610cf45d01d49ca998a4cd08f7b1a097de3`. Introduz `scripts/export-approved-contextual-text.mjs`, `dist/approved-contextual-support-text.css`, manifesto, testes e CI.
- O exportador usa diretamente o blob de decisões `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`, valida valor, tema e **exatamente** os seletores `.hero-description`, `.how-hero-note`, `.about-scale p:not(.eyebrow)`. Mudança na origem falha fechada e pede nova revisão.
- Saída única `--ds-vis002-approved-support-text-light: #705C4B` atribuída **somente** a esses seletores sob `html[data-theme="light"]`. O CSS gerado não contém declarações `color`, `:root`, superfícies, estados ou aliases globais.

## Integração candidata no produto

- Branch [`architecture/p-token-02b-contextual-copy-20261022`](https://github.com/EAKerber/MobiliPresenter2D/tree/architecture/p-token-02b-contextual-copy-20261022), derivada de `architecture/p-token-01b-reference-pin-20261022@854cc05`; a base originalmente veio de `main@840a0cd`.
- `app/design-system/approved-contextual-support-text.css` é cópia **byte a byte** do artefato DS. `design-system/pins/vis-002/context-v0.1.0/PIN.json` e manifesto guardam commits e blobs; verificador Node compara integridade e três consumidores.
- Os três HTML públicos recebem o link versionado `/design-system/approved-contextual-support-text.css?v=vis002-ctx-0.1.0`. Os respectivos CSS de página trocam **apenas** `color:#705C4B` por `color:var(--ds-vis002-approved-support-text-light)`, preservando seletores, ordem e especificidade. Não modificar o Viewer, telas privadas ou o `ui-theme.css`.
- Arquivos de CI `tests/vis002-contextual-text-differential.mjs` e workflow `p-token-02b-contextual-text-gate.yml` validam 3 rotas × 4 larguras (320,390,768,1366) × 2 temas × 2 navegadores (Chromium/WebKit) = **48 cenários**, com screenshot da região, CSS e geometria comparados à `main` intocada. Gate de tolerância de rasterização <=0,1% pixels com delta máximo 1/255/canal **somente depois da equivalência exata de CSS computado e geometria**.

## Limites e próximo gate

- **Não autorizar aplicação universal** de VIS-002: `--public-bg`, `--public-surface`, `--public-text` e foco continuam deliberadamente diferentes da paleta de referência. A mudança é técnica e contextual, não uma homologação de nova aparência.
- CI diferencial **precisa estar concluído em SUCCESS no SHA exato** para classificar o recorte como PASS; registrar id, commit, escopo, exceções e rollback no checkpoint posterior. Um teste de fonte por si só não prova aspecto visual.
- **Não abrir PR de produto apenas para gerar Deploy Preview**; nenhum merge em produção sem revisão dos gates aplicáveis. Além do teste de componente, auth/Viewer/V5 e publicação são contratos preservados.
- **Rollback:** remover o link contextual das três páginas e restaurar os três literais `#705C4B`; descartar a distribuição e os pinos correspondentes. Toda a experiência visual original deve permanecer.
- Mesmo após PASS, outros estados EST e variantes ainda exigem mapeamento/revisão; os três seletores não legitimam um token global.
