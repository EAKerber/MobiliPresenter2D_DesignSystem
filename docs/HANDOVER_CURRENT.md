# Current handover — Plano Diretor v0.9

**Verificado:** 24 de novembro de 2026 (BRT)  
**Escopo:** fotografia operacional; não declara o plano concluído.

## Autoridades e referências

- Plano canônico: [Plano Diretor v0.9](architecture/MOBILIPRESENTER2D_PLANO_DIRETOR_CONSOLIDADO_v0.9.md), blob `59bb530b14172eb9772b9f89bb62272173f4381c`.
- Registro operacional único dos 125 IDs: [Produto — register v0.9](https://github.com/EAKerber/MobiliPresenter2D/blob/development/docs/architecture/plan-v0.9-execution-register.json). O estado inicial do plano foi preservado; `unknown` e `unreviewed` não significam que o recurso ou código estejam ausentes.
- O Design System mantém decisões e contratos; o Produto mantém a implementação executável.

| Repositório | `main` | `development` |
|---|---|---|
| Produto | `01ded2c100fbfd8b16897e26113dc5068a83e429` | `6fbddd5a522dfe5ecc218132253647980720ba37` |
| Design System | `c6ff6545e9ae2071e695109fd94ac91676e7fb0a` | — |

O Produto está divergente: `development` tem 552 commits exclusivos e `main` 17. Esses números contam commits, não divergência funcional. A promoção continua seletiva; não integrar a árvore inteira.

## Estado de execução

- O PR #413 criou o registro canônico e foi integrado somente em Produto `development`. Ele contém 125 IDs únicos; cinco têm evidência operacional parcial e os demais aguardam reconciliação. Nenhuma alteração de runtime ou de produção decorreu desse PR.
- LOC-004 já tem extrações de copy estática compiladas para HTML em `development`. Os recibos cobrem apenas famílias específicas e não provam a conclusão global da ARC-13 nem a promoção para `main`.
- Produto tem 16 branches remotas; Design System tem 2. A contagem remota total é 18. Referências locais e worktrees são inventários separados e não devem ser somados como branches remotas.

## Higiene e gates

- PRs abertas do Produto: #400 e #407, ambas para `main`. PR aberta do Design System: #137, este handover.
- O PR #400 agora prepara cinco heads integrados em duas ondas (3 + 2), com SHAs e árvores exatos. O gate revalidou proteção, uso por PR, referências de workflow e árvore: run [#45532055112](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/45532055112) passou com cinco provas e `deleted: 0`; a aplicação foi ignorada. A auditoria de desenvolvimento [#45532055351](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/45532055351) passou com `count: 0` e `readback: NOT_APPLIED`.
- Se a PR #400 chegar a Produto `main` e o gate de aplicação passar, o Produto cai de 16 para 11 branches remotas. Nenhuma foi removida até agora. A integração da PR pode acionar o deploy normal do site.
- PR #407 adiciona o gate de preço do Viewer a PRs para `main`; permanece independente da promoção de LOC-004.

## Próxima sequência

1. Reconciliar os IDs prioritários no registro com código, consumidores, DoD e evidência exata.
2. Preparar a promoção seletiva de uma família arquitetural completa, incluindo suas fontes, compilação, saídas e gates proporcionais.
3. Integrar somente pacotes compatíveis e validados; manter `main` estável e usar `development` como buffer temporário.
