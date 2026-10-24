# About — validação do skip link no Preview #239 (24/10/2026)

## Alvo e contexto

- Preview: https://deploy-preview-239--mobilipresenter2d.netlify.app/about/
- Produto PR #239, head observado: `bf82272ba19007b65b1bd23856d182346d2fd634`.
- Production base: `main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`.
- Sessão anônima, viewport 1280×720 CSS px.
- Diff da PR: uma regra em `app/about/about.css` para `.about-skip:focus-visible`; nenhuma transferência de foco ou outra rota alterada.

## Resultado do foco visível

Percorri a navegação por teclado e foquei “Pular para o conteúdo” nos dois temas:

| Tema | Cor computada | Largura | Offset declarado | Offset computado na sessão |
|---|---|---:|---:|---:|
| Claro | `#8B6A40` | 4 px | 3 px | 2,66667 px |
| Escuro | `#D8BC7C` | 4 px | 3 px | 2,66667 px |

Nos dois casos `:focus-visible` ficou ativo. Capturas de observação mostraram o anel visível sem recorte do link. O link aparece sobreposto à marca no cabeçalho enquanto recebe foco; esta observação não julga se esse posicionamento atende ao uso pretendido.

## Comportamento de ativação e limites

Enter atualizou o endereço para `#main`, mas o foco ativo terminou em `body`; `main#main` não recebeu foco e não tem `tabindex`. Portanto, o Preview #239 valida a correção de estilo, mas **não corrige a transferência de foco ao destino** observada em Production. Essa mudança de comportamento está fora do diff atual e não foi implementada.

Esta é uma amostra em um navegador, viewport e rota. Não cobre leitor de tela, outras larguras/rotas nem homologação visual global. Nenhuma alteração foi feita à `main`, ao produto ou à decisão canônica.
