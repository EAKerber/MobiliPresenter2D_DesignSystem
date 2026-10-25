# ARC-13 — rastreio de `updateAccessoryControls`

**Data:** 25/10/2026  
**Fonte:** produto `main`: `app/app.js` blob `805494f5ff90bc6aa80bfc4279a240a70e84f8b6`; `app/data/scene-data.js` blob `6fb6f79bc4d360d0c8d4d1e799fe6a7ae617cefd`; `app/data/catalog-data.js` blob `b457ec513a7e838e52bbf69b7d7ae10b55d7948e`; `app/data/configurator-settings.js` blob `c380ea16e5cec9851ab213d38e1c71bae4b52015`. Mesmo blob de `app.js` registrado no mapa ARC-13. Rota `/config/`.

## Consumer e precedência

O controle de iluminação (`lighting-08`) só é atualizado quando existe resultado resolvido. Fica bloqueado se algum requisito não estiver ativo ou se a resolução indicar dependência ausente/oculta. O estado marcado usa a seleção efetiva. Um evento ativo tem precedência no tooltip `Controlado por um evento da configuração.`; caso contrário, o estado bloqueado mostra `Inclua a lateral da geladeira e o aéreo da pia para habilitar a iluminação.`; sem bloqueio, o título é limpo.

O texto fixo corresponde aos nomes atuais da cena (Módulo 04, “Lateral da geladeira”; Módulo 06, “Aéreo da pia”) e à descrição de requisito do serviço no catálogo. Porém, o bloqueio é calculado também a partir de `dynamicDependencies` carregadas da configuração administrativa. A configuração estática inicial não define essas dependências. Não houve readback do conjunto publicado em runtime.

## Impedimento de domínio antes de proposta

O tooltip pode ficar incorreto se a configuração publicada mudar as dependências de `lighting-08`: o gate é dinâmico, mas a explicação nomeia dois itens fixos. Antes de propor chave ou parametrização, o owner deve confirmar se esses pré-requisitos são invariantes; se forem configuráveis, a mensagem precisa derivar os nomes do mesmo conjunto de requisitos que bloqueia o controle. A evidência atual não autoriza correção especulativa.

## Limites

Rastreio manual de fonte e dados estáticos; sem runtime/AT e sem readback da configuração administrativa publicada. Nenhuma chave foi proposta; produto, catálogo, índice e `decisions.json` permanecem inalterados.
