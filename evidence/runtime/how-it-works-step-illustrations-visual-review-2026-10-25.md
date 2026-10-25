# Revisão visual das imagens com alt vazio — Como funciona (Production, 25/10/2026)

**Alvo:** `EAKerber/MobiliPresenter2D@main@5ccb2a8dde6dd16e136f03387dc833aab828c5cf`, rota `/how-it-works/`, em contexto público isolado. A inspeção visual ocorreu em tema escuro, viewport 851×397 CSS px, após scroll para acionar o carregamento lazy. Os oito elementos observados mantinham `alt=""`.

| Elemento | Contexto observado | Classificação sustentada pela evidência |
|---|---|---|
| Ícone WhatsApp (`whatsapp.svg`) | `aria-hidden="true"`; o link é nomeado “Fale conosco pelo WhatsApp”. | Decorativo/redundante para tecnologia assistiva; o link fornece o nome acessível. |
| Ilustração de móveis prontos (`comparacao-moveis-prontos-raster-v1.png`) | Desenho de um gabinete, sem texto embutido; título “Móveis prontos” e critérios/detalhes estão em texto no mesmo cartão e na comparação adjacente. | Ilustração representativa de categoria; a inspeção não encontrou dado textual único. |
| Logo no cartão comparativo (`logo-dark-380.png`) | O wordmark visível repete o título “Casa em Módulos” no cartão. | Marca redundante ao nome textual do cartão. |
| `etapa-cozinha.webp` | Gabinete/área de cozinha. | Ambiente já nomeado “Cozinha”; descrição: “Comece pelo ambiente prioritário.” |
| `etapa-lavanderia.webp` | Lavadora e armários. | Ambiente já nomeado “Lavanderia”; descrição: “Acrescente o que fizer sentido.” |
| `etapa-sala-v1.webp` | Sofá e luminária. | Ambiente já nomeado “Sala”; descrição: “Inclua outros ambientes no seu ritmo.” |
| `etapa-quarto.webp` | Cama e mesa lateral. | Ambiente já nomeado “Quarto”; descrição: “Complete em outro momento.” |
| `etapa-escritorio.webp` | Mesa, cadeira e luminária. | Ambiente já nomeado “Escritório”; descrição: “Continue quando quiser.” |

As ilustrações são simples representações visuais das categorias e etapas; não exibem texto nem informação única além dos nomes e descrições adjacentes. A observação sustenta manter `alt=""` nos oito elementos: para as sete imagens em cartões/lista, o contexto textual já identifica a categoria; no ícone, o link tem nome acessível e a própria imagem está oculta da árvore acessível.

**Nenhum `alt`, conteúdo, CSS ou código foi alterado.** Esta é uma revisão técnica do conteúdo publicado, não uma aprovação visual formal nem uma certificação de acessibilidade global. O registro vale para esta rota, commit, tema, viewport e sessão; não cobre outras rotas, larguras, estados, nem teste com tecnologia assistiva.

A leitura foi somente de DOM e pixels. Não houve interação com formulários, autenticação ou escrita de dados, nem simulação de falha de imagem. A evidência anterior permanece como fonte da contagem de carregamento geral (28/28 imagens completas após scroll); esta revisão classifica os oito casos com `alt=""`.