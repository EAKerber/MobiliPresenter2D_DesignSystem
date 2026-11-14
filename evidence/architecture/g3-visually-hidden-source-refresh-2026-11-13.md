# G3 — refresh estático de `.visually-hidden`

**Data:** 2026-11-13 (BRT)
**Produto observado:** `EAKerber/MobiliPresenter2D/main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7`
**Design System:** branch documental `docs/architecture-status-20261109@bb0ad029395ef0c4c2820bebcd5ffe283bc254fd` antes desta atualização.
**Método:** leitura estática das fontes pinadas; sem mudança no Produto, execução de testes ou validação visual/runtime.

## Consumidores e folhas carregadas

| Rota | Consumidor DOM | Ordem declarada de CSS | Fonte pinada |
| --- | --- | --- | --- |
| `/admin` | `<strong class="visually-hidden">Casa em Módulos</strong>` dentro do link da marca | `admin/admin.css` → `ui-theme.css` | `app/admin.html` blob `28e57028e235944dfd581820ed90078866af93bc`; `app/admin/admin.css` blob `1b3b41e166d44dbf70c1096db36255398aff8493`; uso em `:19`, regra em `:157` |
| `/config/` | `<h1 class="visually-hidden">Casa em Módulos</h1>` como título da página | `styles.css` → CSS inline da página → `ui-theme.css` | `app/config/index.html` blob `ba684d31cf3f79c7bf00c7c669d786f734927acb`; `app/styles.css` blob `d43e6fb5e66133d2389b5c39b165b76b13cfa868`; uso em `:49`, regra em `:853` |

As folhas de Admin e Configurador não são co-carregadas. As duas regras `.visually-hidden` são textualmente idênticas: nove declarações, todas `!important`, totalizando 243 bytes UTF-8 sem compressão. A folha `ui-theme.css` é carregada depois em ambas as rotas; não contém uma regra `.visually-hidden` concorrente. A regra não usa tokens, cor, breakpoint, tema, pseudo-elemento ou estado de interação. A busca nos HTML, CSS e JS da aplicação encontrou somente esses dois consumidores estáticos; nenhum componente JavaScript acrescenta a classe.

## Fronteiras semânticas e de estado

- O utilitário tem o mesmo contrato visual nos dois casos: manter texto semanticamente presente e retirá-lo da apresentação visual. A tag difere (`strong` de marca no Admin, `h1` de página no Configurador), sem variação correspondente na regra.
- `.sr-only` permanece separado. Ele é usado para heading de seção gerado e para `#configurationAnnouncement[aria-live="polite"]`; sua regra tem sete propriedades, não usa `!important` e inclui `clip-path`. Não é a mesma superfície de consumidor.
- Não existe regra explícita `.visually-hidden:focus`, `@media print` ou `@supports` nos arquivos carregados. Isso é observação do código pinado; não prova a árvore acessível ou a apresentação impressa em browser/leitor de tela.
- A regra não define `display:none` ou `visibility:hidden`; não se inferiu resultado de leitor de tela sem inspeção runtime.

## Julgamento e decisão

**Classificação G3:** mesma regra utilitária e mesmo propósito entre duas rotas, com consumidores e folhas por rota já identificados. A duplicação não ocorre duas vezes na mesma página. O pin atual confirma a classificação anterior; os arquivos de aplicação observados não mudaram desde `main@221b54b2a41ecc8c338d1bf2cf67280cf165ce95`.

**Decisão G4:** não extrair agora. Remover a cópia de cada folha de rota e colocá-la em `ui-theme.css` levaria a declaração a todas as rotas que carregam tema; criar folha utilitária acrescentaria outra requisição. Não há medição de payload transferido/comprimido, waterfall ou cache de sessão que demonstre benefício material. A redução de texto-fonte por si só não satisfaz o gate de ganho.

G3 fica concluído para esta família no nível de ownership estático. G4 continua HOLD para esta proposta até uma medição demonstrar ganho; não há alteração de Produto nem proposta de promover `.sr-only` junto com ela. G3 geral continua parcial pelas outras famílias e estados ainda não classificados.

## Limites e próximo passo

Não foram inspecionados CSSOM, estilos computados, árvore de acessibilidade com leitor de tela, impressão, navegação autenticada, carregamento real, cache ou bytes transferidos. Essa ausência não impede a classificação estática; impede declarar validação de runtime ou ganho de extração. A próxima família segue sendo marca/logo e ownership de slots entre shells público, Viewer e privado, conforme o inventário G3.

**Validação documental:** identidade do repositório e Product main foram reobservadas; os blobs acima fixam as fontes. Os arquivos de aplicação comparados entre o pin anterior `221b54b2` e `bb3e3a34` não mudaram. Nenhum teste foi executado.
