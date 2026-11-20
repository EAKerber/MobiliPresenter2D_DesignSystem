# DS-05A — medição pareada do badge de módulo

**Data:** 20/11/2026 (BRT)  
**Alvo:** regra candidata limitada a `.module-number` no tema claro.  
**Tipo de evidência:** captura local pareada de CSSOM; não é o gate integral DS-05A.

## Proveniência e método

O Product canônico durante a medição era `main@dc066f55619824626ea4752ecc0bafc67f9d9110`. O checkout de execução registrou `efc40584c3f3ca940cf6cbca408f8fda31e3e1c9`, portanto a identidade do commit **não** coincide. A árvore `app/` foi comparada separadamente: ambas são `0c4c2aecde1f78023965d503e92c83bf774b1dd3`; o blob de `app/ui-theme.css` é `3114bbfe0a67cbdc53757f5f50a0d035559767a6` em ambas. O runner registrou `appWorkingTree: clean`; seu checkout temporário não ficou disponível para uma segunda leitura independente de `git status`.

O runner `ds05a-runtime-cssom-v2.cjs` (SHA-256 `ab2a1e2dc68ffe19b4689a264214454c0a3dc135715bba2820cfcc5ed86ce359`) carregou HTML/JavaScript reais da árvore `app/` por interceptação CDP, bloqueou solicitações externas e congelou transições. A configuração Buyer V5 veio de defaults versionados locais e é sintética; não houve acesso a banco, autenticação ou deploy.

A regra foi injetada somente em memória, removida após cada par:

```css
html[data-theme="light"] .module-number {
  background: rgb(34 33 31 / 8%);
  color: var(--text);
}
```

Seu SHA-256 é `88a531048d52807c5a0dca73f1887463d22daa4d6d70d4e926bbf118c4ad8407`. O Chrome foi `156.0.8078.82`, via Node `v24.20.0`.

## Resultado

Foram capturados seis pares (três larguras × dois temas), com sete badges em cada estado.

| Largura CSS px | Tema | Contraste baseline | Contraste candidato | Badges alterados |
|---:|---|---:|---:|---:|
| 390 | claro | 1,43:1 | 13,02:1 | 7 |
| 1050 | claro | 1,43:1 | 13,02:1 | 7 |
| 1366 | claro | 1,43:1 | 13,02:1 | 7 |
| 390 | escuro | 8,10:1 | 8,10:1 | 0 |
| 1050 | escuro | 8,10:1 | 8,10:1 | 0 |
| 1366 | escuro | 8,10:1 | 8,10:1 | 0 |

O resultado apoia somente a medição desse consumidor e dessa fixture. A regra está como candidata de escopo limitado na [PR #271](https://github.com/EAKerber/MobiliPresenter2D/pull/271), ainda aberta e não integrada; esse resultado não constitui aprovação final do estilo.

## Recibos e capturas

- JSON original: 520.762 bytes; SHA-256 `94adade504a4188a70b011ec254856f2d300af0dac7daf3e14898a9af98bef95`.
- Recibo gzip anexado: 27.371 bytes; SHA-256 `bf6d54a954e42f9816a360da10aed7f48ad594fdc90f8fb4ed987140cd0b2eaa`.
- Seis PNGs são capturas do tema claro apenas. Seus hashes e tamanhos completos estão dentro do JSON, junto com os resultados CSSOM de tema escuro. Os PNGs permanecem no conjunto local; não foram duplicados na branch documental.

## Limites e leitura

- Não é uma execução do gate DS-05A, não compara estados hospedados nem confirma os required checks.
- Os controles escuros foram medidos via CSSOM/JSON, sem screenshot escuro.
- A configuração sintética não representa comprador, conta, banco ou publicação real.
- A captura não valida Safari/iPad, zoom, nem conformidade WCAG global.
- A medição do badge não resolve o achado independente de `#viewerHint` (1,00:1 no claro e 4,05:1 no escuro no baseline desta fixture).
- A equivalência comprovada é somente da árvore `app/`; não se declara igualdade do repositório completo entre os dois commits.

**Conclusão operacional:** manter a regra como candidata restrita e aguardar a validação/decisão própria da PR #271. Não ampliar o seletor para tokens globais nem encerrar DS-05A com base neste recibo.
