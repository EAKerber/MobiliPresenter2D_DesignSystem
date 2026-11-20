# G3 — Slots de marca e logo — auditoria estática — 2026-11-13

## Fonte e alcance

Produto: EAKerber/MobiliPresenter2D main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7. Leitura estática de HTML, seletores, folhas de estilo declaradas e mecanismo de tema. Esta matriz classifica slots e ownership; não determina dimensões computadas em runtime.

## Matriz de slots

| Superfície | Estrutura/consumidor | Contrato compartilhado | Classificação |
|---|---|---|---|
| Cabeçalho público — Home, Sobre, Como funciona | .site-header e .brand; Home app/index.html:16,22, Sobre app/about/index.html:9, Como funciona app/how-it-works/index.html:16. | As páginas usam img[data-brand-variant] para escolher logo claro/escuro; a base geométrica está em app/landing/landing.css:23–26. Cada página mantém folha local; Como funciona tem geometria específica em app/how-it-works/how-it-works.css:181. | Mesmo shell público com variante local de página. Há candidato de ownership compartilhado do shell, sujeito ao gate G1. |
| Splash da Home | Marca própria na abertura em app/index.html:21. | Usa variantes de imagem próprias, em resolução de 1548 px, selecionadas pelo tema. | Slot de abertura independente do cabeçalho público. |
| Arte do hero da Home | Raster ilustrativo referenciado em app/index.html:34, enquadrado por .hero-image-frame em app/landing/landing.css:62. | Não usa data-brand-variant; o lettering integra a própria imagem. | Arte/composição específica. Corrigir o logo inventado na imagem requer substituir/ajustar o ativo do hero. A proposta de vídeo dentro do telefone pertence à mesma composição, não a um componente de logo compartilhado. |
| Comparação em Como funciona | Logo em app/how-it-works/index.html:86, com seu slot editorial próprio. | Pode compartilhar seleção do ativo por tema. | Slot de conteúdo da comparação, não o cabeçalho. |
| Rodapés públicos | Consumidores próprios em Home (app/index.html:55), Sobre (app/about/index.html:26) e Como funciona (app/how-it-works/index.html:251). | O ativo pode ser comum, mas o layout e as medidas pertencem ao rodapé. | Família de rodapé separada do cabeçalho e da comparação. |
| Viewer | .viewer-header e .viewer-brand, com retorno e ações, em app/viewer/index.html:15; regras próprias em app/viewer/viewer.css:1. | Seleção de variante de tema compartilhada. | Cabeçalho do Viewer distinto do shell público. |
| Cabeçalhos privados — Admin, Config e Access | Regras .private-header em app/ui-theme.css:268; estruturas diferentes em Admin app/admin.html:18–19, Config app/config/index.html:44–50, Access app/access/index.html:25–26 e app/access/manage.html:44–45. | Há convenções e seleção de variante em comum; os documentos declaram estilos locais antes de ui-theme.css. | Família privada com variação estrutural. Sem inspeção de CSSOM, a ordem/especificidade não basta para fechar as dimensões visuais por rota. |

## Julgamento e decisão

O que se repete com clareza é a **seleção do ativo de marca por tema** em app/core/ui-theme.js:22,40–44. Isto não é um contrato geral de tamanho, layout ou estrutura do cabeçalho. Home/Sobre/Como funciona partilham o shell público; Viewer e cabeçalhos privados têm contextos próprios; splash, comparação e rodapé são slots distintos.

**G3 estático:** a matriz de ownership está classificada para as superfícies acima. **G4:** nenhuma extração de layout de logo é indicada por esta evidência. Preservar os slots separados até demonstrar equivalência por consumidor e custo/benefício de mudança.

## Atualização após a PR #273 integrada — 14/11/2026

**Base atual do Produto:** `main@46a52e76a0eeae4bed4b567b12da5311ed90b475`. A implementação veio da PR [#273](https://github.com/EAKerber/MobiliPresenter2D/pull/273), head revisado `6799d3177bf931f087f2bf451a6d6dbf5b4d5f6f`, integrada por squash em `46a52e76`.

A revisão visual registrada no Deploy Preview da PR cobriu desktop e celular. O hero mantém a arte do ambiente e do aparelho como imagem estática de fundo; o vídeo preenche a tela do telefone sem o cabeçalho fictício. O telefone e a composição completa aparecem menores, preservando proporção: redução documentada de 12% em desktop, 16% em telas intermediárias e 20% em celular. O player só é ativado após escolha de reprodução; o controle de tela cheia fica sobreposto. A miniatura segue a imagem padrão do YouTube e não garante o primeiro quadro decodificado do vídeo. “Como funciona” conserva seu vídeo e normaliza as imagens dos cards comparativos em molduras comuns.

**Ownership G3 atualizado:** (1) arte raster do ambiente/aparelho, (2) superfície do vídeo e seus controles dentro da tela ilustrada e (3) logos/cabeçalhos pertencem a slots diferentes. O slot da marca do cabeçalho não fornece lettering à arte do hero. A nota de 13/11 de que o lettering incorreto ainda precisava de correção era correta naquele snapshot e está agora **superada** pela integração da #273. A baseline CSSOM de CTAs de 14/11 continua sendo uma coleta local pinada em árvore anterior; ela não passa a representar o estado pós-#273. Esta revisão do preview complementa a baseline, sem convertê-la em medição CSSOM, screenshot arquivado ou evidência de dispositivo físico.

O corpo da PR registrou 11/11 checks, compilação canônica sincronizada e ausência de rolagem horizontal. Esta atualização apenas reconcilia propriedade/proveniência; G3 continua parcial e não aprova extração de CSS compartilhado.

## Follow-up de semântica do grupo de links — PR #275 Draft

A triagem pós-#273 identificou `aria-label` no `div` genérico dos links secundários do hero. A PR [#275](https://github.com/EAKerber/MobiliPresenter2D/pull/275) propõe `role="group"` e sincroniza a fonte, a saída gerada e o manifest. Ainda não foi integrada nem validada com leitor de tela; G3 permanece parcial.

## Limites

Não foi medido CSSOM, tamanho computado em temas/telas, clipping, proporção do ativo, performance de transferência ou comportamento de dispositivo. A matriz não autoriza substituir qualquer imagem; apenas mostra que o hero raster não é o logo do cabeçalho. A revisão visual da arte e do vídeo está registrada no adendo pós-#273; esta auditoria estática não mede CSSOM, clipping ou comportamento em dispositivo físico.
