# ARC-13 — rastreio de `createModuleFocus`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; `app/admin/admin.js` blob `79925345e43096df77bef54fe257e483f922edd8`. O app blob coincide com o mapa ARC-13. Rota `/config/`.

## Consumer

A função cria uma imagem de foco para o módulo na ficha. O arquivo vem de `configuredObjectAssets[entity.id].detailImageAsset`, se configurado; senão usa o asset da entidade de cena. O `alt` é sempre `Recorte isolado de {product.title}`, com o título do produto como dado dinâmico. A camada visual de acabamento fica `aria-hidden`, para não duplicar o nome acessível da imagem.

## Ponto a validar

O Admin chama esse override de “Imagem dos detalhes” e permite escolher um asset da biblioteca. Portanto a fonte não é necessariamente um recorte da imagem da cena; o `alt` fixo pode descrever incorretamente uma imagem alternativa. Confirmar o contrato com o owner: se todo override deve ser crop isolado, preservar a regra e validá-la; se pode ser outra vista, a descrição acessível precisa corresponder ao tipo real da imagem (ou vir de metadado próprio). O fallback para a imagem da cena é um recorte, mas não comprova o uso de todos os overrides.

## Limites

Rastreio manual de renderer e do campo do Admin, sem runtime/AT nem leitura do estado publicado de assets. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` permanecem inalterados.
