# Evidência CI autenticada — DS-05A Config e progressão de etapas — 24/10/2026

- Produto: PR [#238](https://github.com/EAKerber/MobiliPresenter2D/pull/238), commit `eb7a64d552ab4b16b70c5615928d8eb10a52d54d`.
- Execução autenticada: [Actions #40120919242](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/40120919242) — SUCCESS.
- Deploy Previews dos projetos principal e isolado: SUCCESS. Supabase Preview: SKIPPED, pois não há branch Supabase associada; o gate usa o banco interno de teste já existente.
- O gate confirmou readiness da superfície Config: contadores coerentes, estimativa monetária e ação seguinte visíveis.
- Dois toggles de módulos foram exercitados individualmente: cada um alterou a contagem e foi restaurado ao estado inicial. A estimativa permaneceu visível após cada alteração e restauração.
- O botão de continuação abriu Acabamentos, Serviços e Resumo, em sequência. Em cada etapa, o painel esperado e a estimativa monetária permaneceram visíveis.
- O relatório da execução contém apenas flags. Nenhum preço, configuração, cookie, token, URI ou segredo foi gravado no artefato.
- O gate também confirmou o resgate do grant temporário, o bootstrap de Config, a negação de Admin e a revogação do grant.

## Limites

Esta evidência cobre a progressão padrão pelas quatro etapas e dois toggles de módulos. Não exercita opções de Acabamentos ou Serviços, combinações de preço, envio de proposta, estados administrativos nem homologação visual abrangente. O grant e a conexão usam a fixture autorizada existente; o papel de fixture não recebeu permissões adicionais.
