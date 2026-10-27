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

---

## Rechecagem após corrigir a rota de sessão — 25/10/2026

Produto PR [#238](https://github.com/EAKerber/MobiliPresenter2D/pull/238), head `75c38601695b08798264b175068155cd17b7334d`; execução autenticada [Actions #40152094552](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40152094552).

- Os Deploy Previews do produto e do host isolado ficaram READY. Checks estáticos, contrato, browser geral, ativos, gate anônimo e regras da Netlify passaram.
- A remoção do rewrite duplicado de `/api/access/session` eliminou o 404: o browser não registrou falhas HTTP ou erros de rede.
- O preflight de variáveis, grant real, papel restrito, bootstrap publicado V5, negação de Admin e revogação passaram. O browser registrou V5 `validated`, sem erro de configuração e com workspace visível.
- Mobile/PiP, Summary/Pricing e Stone passaram. Keyboard e Flow ainda falharam em interação de etapas. Diagnóstico estrutural limitado e sanitizado: os botões da navegação têm caixa 0×0, apesar de estarem no DOM e computarem `display:block`; no Keyboard, Ctrl+→ foi prevenido mas a etapa permaneceu em Módulos. No Flow, o alvo Módulos não era clicável no perfil stacked e o ponto central atingia `MAIN.workspace`. Não há causa de produto confirmada ainda; não mascarar os asserts nem declarar as duas suítes homologadas.
- Nenhum valor de variável, URI de banco, cookie, grant ou token foi guardado. Supabase Preview ficou skipped porque a branch não usa Supabase Branch; segue o banco interno autorizado. Issue #232 continua aberta; PRs #238 e #51 seguem DRAFT, sem merge ou deploy em Production.

Esta evidência complementa e supersede o estado funcional anterior na mesma trilha; os registros históricos permanecem abaixo.
