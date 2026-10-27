# About — validação do skip link no Preview #239 (24/10/2026)

## Alvo e contexto

- Preview: https://deploy-preview-239--mobilipresenter2d.netlify.app/about/
- Produto PR #239, head validado: `e7b02c04308e9fcc7b52f1d09534058a2a0bbc65`.
- Production base: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Sessão anônima, viewport 1280×720 CSS px.
- Diff validado: regra VIS-002 em `app/about/about.css`, controlador do skip link em `app/about/about.js`, `tabindex="-1"` em `main#main`, fonte autoral e HTML ARC-03C sincronizados, além de gate browser dedicado.

## Resultado do foco visível

Percorri a navegação por teclado e foquei “Pular para o conteúdo” nos dois temas:

| Tema | Cor computada | Largura | Offset declarado | Offset computado na sessão |
|---|---|---:|---:|---:|
| Claro | `#8B6A40` | 4 px | 3 px | 2,66667 px |
| Escuro | `#D8BC7C` | 4 px | 3 px | 2,66667 px |

Nos dois casos `:focus-visible` ficou ativo. Capturas de observação mostraram o anel visível sem recorte do link. O link aparece sobreposto à marca no cabeçalho enquanto recebe foco; esta observação não julga se esse posicionamento atende ao uso pretendido.

## Comportamento de ativação e limites

No head atual, ativei o link por teclado real (Tab → Enter) no Deploy Preview isolado. O endereço mudou para `#main` e a leitura posterior retornou `activeTag=MAIN`, `activeId=main`, `tabindex=-1`; o foco chegou ao landmark. Isso confirma a correção do defeito observado em Production. O gate browser dedicado também passou no head atual após corrigir a importação ESM do teste; build ARC-03C, `pages:check`, `current-build`, `variants`, `current-asset-gates` e checks browser passaram. Deploy Previews principal e isolado ficaram READY. Supabase Preview foi skipped por ausência de associação da branch a um Supabase Branch.

Esta é uma amostra em um navegador, viewport e rota. Não cobre leitor de tela, outras larguras/rotas nem homologação visual global. Nenhuma alteração foi feita à `main`, ao produto ou à decisão canônica.
