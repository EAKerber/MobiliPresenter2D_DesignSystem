# P-TOKEN-01 — Paleta executável de referência do Design System

> **Marco posterior de execução:** a PR [#49](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/49) foi **MERGED** no Design System `main@70f0eab`. O consumidor pinado foi preparado em branch própria de produto e validado, sem carregar CSS; ver [P-TOKEN-01B/02A e observações CSSOM](P_TOKEN_01B_02A_PRODUCT_INTEGRATION_AND_COMPUTED_AUDIT_2026-10-22.md). O estado anterior descrito abaixo refere-se ao momento pré-merge.


**Data:** 2026-10-22. **Estado:** infraestrutura de geração implementada e testada em branch; **sem aplicação no runtime do produto**.

**Decisões:** `ARC-02` (Design System como origem executável), `ARC-14` (integração por versão e PR), `ARC-04` (preservação visual), `VIS-002.approvedPalette` (referência visual homologada), `EST-02` (foco).
**Fronteira de autoridade:** `decisions.json` não deve ser alterado por geração; `VIS-002.implementationAuthorized=false`, a aprovação de cor **não autoriza aplicação global nem associações a controles**.

## O que foi implementado

- [Exportador determinístico](../scripts/export-approved-palette.mjs) em Node.js nativo: lê `decisions.json` e deriva 7 papéis de paleta × 2 temas, e medidas de referência para contorno/offset de foco. **Não mantém cópias manuais dos valores**.
- [CSS de referência gerado](../dist/approved-palette-reference.css): **16 propriedades `--ds-reference-*`**, nomeadas para não coincidir com CSS atualmente executável do produto. É **somente um artefato de distribuição**, **não é importado por página alguma**.
- [Manifesto versionado](../dist/approved-palette-reference.manifest.json): `version=0.1.0`, origem, decisão, escopo, indicação de implementação não autorizada, itens, papéis, temas e paths exatos na decisão.
- [Testes Node nativos](../tests/export-approved-palette.test.mjs): check do hash Git de blob de `decisions.json`, presença/status de VIS-002, conjunto e valores homologados, ausência de aliases do produto, serialização determinística, readback byte a byte, recusa a fonte alterada.
- [Workflow de CI isolado](../.github/workflows/p-token-01-reference-export-gate.yml): sintaxe, `--check`, `node --test`, sem checkout de produto, sem Netlify e sem Deploy Preview.

## Proveniência e protocolo de atualização

A fonte executável é `decisions.json` e o campo específico `VIS-002.approvedPalette`. O exportador fixa o **blob SHA Git `63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa`** como barreira de mudança silenciosa. Uma nova homologação mudará o blob: o gate **deve falhar**, exigindo atualização explícita de versão, revisão da decisão e dos testes antes de gerar outra distribuição.

Comando no clone do Design System:

```sh
node scripts/export-approved-palette.mjs
node scripts/export-approved-palette.mjs --check
node --test tests/export-approved-palette.test.mjs
```

Os artefatos em `dist/` são gerados pelo mesmo programa em qualquer máquina Node suportada. Não se usa `gh`, bibliotecas frontend ou conectividade de rede para gerar CSS.

## Política estrita de ativação — NÃO executar por inferência

1. Antes de consumir um token de referência, provar **por componente, tema, superfície e estado** que o par e o papel foram homologados; observar a **cascata efetiva** e preservar o pixel/behavior quando o incremento tiver fidelidade estrita.
2. Não mapear automaticamente `--ds-reference-surface-light` para `--public-surface`: produto usa `#fff` em certos contextos, enquanto a paleta VIS-002 propõe `#F0EDE8`. Essa mudança seria visual e exige gate decisório distinto.
3. Não mapear automaticamente foco aprovado de 4px/offset3 para controles que hoje usam 3px/offset2: isso é uma possível **correção visual**, não um refactor sem alterações.
4. Não gerar, a partir de VIS-002, cores de `hover`, `disabled`, `pressed`, estados semânticos globais de erro/sucesso/aviso/informação nem variantes de cobre que ainda não tenham aplicação autorizada. Pares contextuais aprovados não viram tokens globais indiscriminadamente.
5. Futuras integrações DS→produto devem ser **PRs explícitas** com commit/manifesto da exportação pinado, diff de CSS e rollback. O pacote pode ser armazenado no repo do produto sem ser carregado; carregar e associar aliases só após o gate visual por consumidor.
6. Não fundir o trabalho com `P-COMP-01` (menu), auth, publicação de preços ou fragmentos HTML.

## Gates e limites de evidência

O workflow testa **a geração**, não aparência renderizada nem acessibilidade em dispositivos. **PASS em CI não significa homologação dos componentes nem autorização de distribuir CSS ativo**.

**Condição para próxima fase P-TOKEN-01B:** distribuir uma cópia versionada e íntegra no repo do produto **fora da pasta publicada `app/`**, validando proveniência e não ativação em build; preparar inventário de consumidores onde valores atuais coincidem e onde divergem. Somente depois planejar a primeira substituição de propriedade aprovada e fazer avaliação visual com as rotas reais e rollback.

**Não há mudança de produto, layout, catálogo, tokens globais atuais, autenticação ou Netlify neste incremento DS.**
