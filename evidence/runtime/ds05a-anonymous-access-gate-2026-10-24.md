# DS-05A — limite de observação sem sessão autorizada

Data: 2026-10-24  
Produto: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`  
Deploy observado: `6adc221479c773577ed45e23` (Netlify Production, READY)

## Observação anônima

A partir de um contexto isolado, sem cookies de conta:

- Abrir `/config/` terminou em `/access/`. A página informa que o link não contém token válido e orienta solicitar novo acesso. Não havia formulário nem os controles do configurador no DOM.
- Abrir `/admin.html` exibiu o cartão de acesso restrito com campos de e-mail e senha. Os componentes de opções administrativas não estavam montados: não havia `.item-option`, `.hierarchy-name` ou `.hierarchy-tree` no DOM.
- Nenhuma credencial foi inserida, sessão criada ou estado administrativo alterado.

## O que isso significa para DS-05A

A sessão anônima não permite medir em DOM real o contador, a barra de preço/próxima etapa ou as opções do Admin. As evidências existentes dos issues #208/#209 são úteis para orientar os seletores e cenários, mas não demonstram que o detector proposto encontre esses alvos de modo genérico nem substituem uma execução atual no DOM autorizado.

Próximo gate: usar uma sessão administrativa de teste aberta pelo usuário ou a fixture autenticada de CI já prevista para a PR #238, desde que a sessão seja válida para a rota e o detector possa observar a UI sem expor dados de conta. Não copiar credenciais ou tokens para a evidência. Se nenhum dos dois acessos estiver disponível, DS-05A continua pendente.

DS-05B (temas, estados e breakpoints) e DS-05C (ligação ao laboratório v0.3) continuam pendentes conforme `decisions.json`. Esta leitura não altera o status do issue #208, não fecha findings e não autoriza mudanças visuais.
