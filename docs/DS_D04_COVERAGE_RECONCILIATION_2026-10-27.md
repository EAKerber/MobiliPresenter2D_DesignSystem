# D04 — matriz de cobertura DS-04, riscos e plano G0–G8 (27/10/2026)

**Origem histórica:** [PR #51](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/pull/51) @ `28062602a4ddcd1bee090742fe2587fe3837175d`. Esta extração transporta 4 arquivos pelo Git Blob SHA original, sem modificar texto, código, decisões, workflows ou estado atual de issues.

## Fontes preservadas e uso apropriado

1. [Conciliação do plano G0–G8](../evidence/architecture/master-plan-g0-g8-current-crosswalk-2026-10-25.md) — compara o plano antigo da #39 com o andamento observado em 25–26/10, sem aprovar merge nem resolução da linha inteira de gates. Números de PR, status e heads são **fotografia datada**, não status atual.
2. [Cobertura do inventário visual por rota](../evidence/architecture/runtime-inventory-coverage-2026-10-24.md) — separa 8 rotas, layout, foco, contraste, mídia e lacunas; a leitura de CSS fonte não certifica comportamento do DOM atual.
3. [Famílias de regras CSS por evidência](../evidence/architecture/visual-rule-family-runtime-map-2026-10-24.md) — 1.390 blocos CSS em 8 folhas do snapshot `MobiliPresenter2D@5ccb2a8`; rótulos `parcial`/`não verificado` não significam conformidade. Famílias, rotas e responsividade precisam de inspeção específica.
4. [Issue #208 — DS-04 reauditoria de 16 achados](../evidence/architecture/issue208-ds04-main-source-reconciliation-2026-10-25.md) — contrasta tokens e código com páginas públicas e limita acesso a rotas autenticadas. Exemplo significativo: DS04-02 mostrava par de ~1,62:1 pelo cálculo estático no cabeçalho privado; isso é **risco datado**, não medição nem falha atual do produto.

## Política de interpretação e dependências

Aprovações em `decisions.json@main` continuam canônicas. Não promover valores incidentais a tokens globais, não chamar uma inspeção estática de teste funcional, não deduplicar CSS entre módulos só por classe idêntica e não usar WebKit headless como equivalente a iPad real.

Essas matrizes incluem links para relatórios detalhados ainda em PR #51 HOLD; o contexto e os objetos originais são rastreáveis pela SHA pinada, mas **alguns links relativos no Markdown importado ainda não resolvem na main**. Não declarar revisão de cobertura completa ou certificação de funcionamento por este lote. Retomar cada issue de produto com consulta nova antes de executar uma correção.

### Próximas inspeções prioritárias

- Rechecar DS04-02 (cabeçalho privado), DS04-06 (legibilidade em Configurador), DS04-10/12 (temas/controles), sem inventar estado atual nem abrir sessão sem autorização específica.
- Validar layout 290–320 CSS px e contraste em contexto real, incluindo carregamento de imagens e `prefers-reduced-motion` como dimensão independente.
- Para qualquer mudança compartilhada, escolher **um contrato e um consumidor** por vez, com origem de CSS, estado, tema, breakpoint, foco, captura visual e gate funcional. Nada de migração/deduplicação em lote.

**Gate deste commit:** 4 blobs exatos, provenientes de 4 documentos arquiteturais da #51; exclusivos daquela fonte **197→193** após merge/readback. Mantém 21 na #39 e todos os HOLDs; dois workflows da #39 permanecem fora da main. Não houve teste runtime ou deploy.
