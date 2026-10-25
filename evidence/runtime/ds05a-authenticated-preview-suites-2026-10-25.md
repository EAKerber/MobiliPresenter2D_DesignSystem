# DS-05A — gate autenticado e suítes funcionais no Deploy Preview

Data: 2026-10-25  
Produto: `EAKerber/MobiliPresenter2D`  
Issue: [#232](https://github.com/EAKerber/MobiliPresenter2D/issues/232)  
PR: [#238](https://github.com/EAKerber/MobiliPresenter2D/pull/238), DRAFT  
Head avaliado: `ecd2c5b07246a59f2ed959376eb311f53cffdf2e`  
Execução autenticada: [Actions #40149640577](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40149640577)

## O que passou

- Os Deploy Previews principal e isolado ficaram READY; os checks estáticos, browser geral, fixture-contract, gate anônimo e current-asset-gates passaram.
- O job autenticado passou por preflight, conexão com o papel restrito, criação/resgate de grant e verificação da fronteira de Admin.
- A chamada autenticada a `/api/buyer-configuration` retornou HTTP 200.
- Um probe no navegador confirmou `publishedConfigurationStatus=validated`, ausência do alerta de configuração inválida e workspace visível; não observou erros de página nessa leitura.
- Os grants foram revogados. O replay do token revogado foi negado com HTTP 400, que é o contrato implementado pela função; a navegação da sessão revogada terminou em `/access/`.

## O que continua falhando

As cinco suítes chegaram à interface autenticada, mas não terminaram:

| Suíte | Falha observada |
|---|---|
| Mobile/PiP | Assert de erros de console em `tests/mobile-pip-main-browser.cjs:144` |
| Keyboard | Timeout de interação em `tests/keyboard-browser.cjs:174` |
| Flow | Timeout ao interagir com a navegação de etapas em `tests/flow-layout-browser.cjs:415` |
| Summary/Pricing | Assert de erros de console em `tests/summary-pricing-browser.cjs:209` |
| Stone | Assert de erros de console em `tests/stone-browser.cjs:269` |

Os diagnósticos sanitizados não registraram status HTTP de erro ou códigos `net::ERR_*`. Isso não determina a causa das falhas funcionais. A autenticação real e o bootstrap V5 passaram; as cinco suítes ainda não estão homologadas no Deploy Preview autenticado.

## Limites

O gate do host estável verifica sessão, bootstrap, negação de Admin e revogação. As suítes funcionais rodam no Deploy Preview #238, onde a fixture V5 existe. O check Supabase Preview foi skipped porque a branch não tem uma Supabase Branch associada; o fluxo usa o banco interno já autorizado. Nenhum valor de variável, URI, cookie, token ou dado de configuração foi registrado nesta evidência.

Issue #232 permanece aberta até as falhas das suítes serem compreendidas e a cobertura funcional passar. PR #238 permanece DRAFT. Sem merge, mudança de runtime em Production ou deploy de Production.
