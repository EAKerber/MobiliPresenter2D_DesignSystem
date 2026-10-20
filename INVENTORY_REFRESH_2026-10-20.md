# Reconciliação do inventário visual — 2026-10-20

**Produto:** [EAKerber/MobiliPresenter2D](https://github.com/EAKerber/MobiliPresenter2D), `main` no commit [1878ae1](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463).
**Deploy publicado:** [Netlify 6ad6c3b51b6be05647167f94](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94), estado `ready`, publicado em 2026-10-20 01:28:40 UTC.
**Base anterior do inventário:** `483ef2e6f76a562a3096516ef68d8dfe072ec21f`.

## Delta visual coberto

A comparação de commits entre a base anterior e a atual encontrou mudanças em oito arquivos. Dentro do escopo estático (HTML, CSS e assets), dois HTMLs mudaram; nenhuma folha CSS ou asset visual mudou.

- `app/access/index.html`: recebeu a estrutura `nav[data-private-menu]` com regiões de links e conta. O tamanho da marcação passou de 2.890 para 3295 unidades UTF-16; linhas: 44 para 50. Foram adicionadas as classes estáticas `private-menu`, `private-menu__account`, `private-menu__email` e `private-menu__logout`; os quatro seletores já existem em `app/ui-theme.css`. A contagem global de nomes de classe permanece em 251 porque esses nomes já aparecem em outras páginas.
- `app/admin.html`: mudou apenas os identificadores de versão/cache dos arquivos CSS e JavaScript. A marcação visual e o conjunto de classes permanecem iguais; bytes/unidades e linha agora refletem o HTML servido pelo commit atual.
- Os demais arquivos alterados no commit são módulos JavaScript e testes, fora do escopo desta atualização visual estática.

A mudança no HTML confirma que o menu existe na página de confirmação de acesso. O comportamento de sessão e o menu após autenticação não foram auditados de novo; a validação pós-login de FIND-007 permanece pendente.

## Atualizações nos artefatos

- `visual-inventory.json`: snapshot e metadados das duas páginas HTML sincronizados com o commit atual.
- `VISUAL_INVENTORY.md` e `DECISION_APPLICATION_MAP.md`: fonte estática e estado runtime separados, com a rota `/access/` atualizada.
- `runtime-evidence.json`: registra o deploy mais recente e aponta a validação autenticada pendente.
- Nenhum token foi promovido, nenhuma decisão visual nova foi inferida e nenhuma tela foi tratada como aprovada por esta reconciliação.
