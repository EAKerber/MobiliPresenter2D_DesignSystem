# G3 — Julgamento dos controles e estados do Admin — 2026-11-13

## Fonte e alcance

Fonte de produto: EAKerber/MobiliPresenter2D em `main@bb3e3a34ee771db1efe6d8dcfe8cbde96c6a40c7`. A revisão ARC-13 atual está no branch local `work/arc13-ui-inventory-20261112@3b97542482ff9c1bdb2ad45aabf777f97991e60f`; os arquivos `app/admin/admin.js` e `app/admin/admin.css` correspondem aos blobs de `origin/main` local; os dois commits mais recentes desse branch alteraram somente inventário/documentação. O inventário associado tem SHA-256 `8765873a096fe95167e4fba74838258e47428fab0e12d16af9b6c92a3e34a51e`.

Revisão estática de geradores DOM, estado/modelo, listeners e regras CSS. As capturas fornecidas pelo usuário servem como observação visual, mas não estabelecem o CSS computado nem intenção de design. Não houve alteração de produto nem validação runtime.

## Julgamento por contrato

| Família | Função e estados observados na fonte | Apresentação e acessibilidade estáticas | Decisão de ownership |
|---|---|---|---|
| Estado inicial no configurador — módulo/objeto | initialState.entities; o Configurador aplica os valores a visibilityByEntity. Gerado em app/admin/admin.js:234–245, consumido em app/app.js:1798. | Módulo: texto “Iniciar visível no configurador”. Objeto: “Iniciar ativo”. Ambos recebem um aria-label terminado em “ativo inicialmente”. Usam .initial-state-option, texto muted de 10 px, sem accent-color declarado. | Um mesmo grupo técnico com variantes de conteúdo por tipo de entidade; não é a disponibilidade da etapa. O nome acessível do módulo diverge do rótulo e do efeito de visibilidade. Confirmar wording do objeto com domínio antes de renomear. |
| Estado inicial no Viewer — módulo | initialState.viewerEntities, independente do estado inicial do Configurador; app/admin/admin.js:246–256. | “Iniciar visível no viewer”; o texto e o nome acessível usam visibilidade. Também usa .initial-state-option. | Manter separado do estado inicial no Configurador, apesar da estrutura visual parecida. |
| Estado inicial de serviço | initialState.services; o listener altera a seleção inicial do serviço, app/admin/admin.js:258–267,1735–1741. | “Iniciar ativo”; o nome acessível acompanha esse sentido. .initial-state-option, 10 px e accent padrão do navegador. | Manter distinto de visibilidade de módulo, visibilidade no Viewer e disponibilidade da etapa. |
| Disponibilidade da etapa | stage.enabled controla a etapa completa; app/admin/admin.js:704–713,1664–1672. Etapas modules, summary e etapas vazias são desabilitadas. | Texto visível Ativa/Inativa; nome acessível imperativo “Ativar etapa …”. .switch usa checkbox nativo, accent-color: var(--accent) e texto de 12 px (app/admin/admin.css:33). | Contrato próprio. Revisar se nome imperativo junto de estado checked comunica a disponibilidade atual com clareza. |
| Disponibilidade para clientes — acabamentos e puxadores | Acabamento usa finish.enabled, com proteção para não desativar o último acabamento global (app/admin/admin.js:853–860,1346–1364). Puxador usa associação a handles-all.materialIds (1000–1007,1393–1402) e suas próprias regras mínimas. | Ambos exibem exatamente “Disponível para clientes” e usam .switch. | Compartilhar a copy/chave de localização é razoável. Manter estado, validação e persistência separados por domínio. |
| Elegibilidade e associação de materiais | Seleciona acabamento por módulo, alvos válidos, materiais por alvo e opção “Sem cor/tinta base”; app/admin/admin.js:879–885,959–982,1026–1056. | Checkboxes nativos em labels e listas; os estados representam associação/propriedade, não um toggle geral de disponibilidade. | Preservar como seleção e associação. Não fundir com os controles de disponibilidade só porque todos são checkboxes. |
| Exibição pública de preços no Viewer | viewerPricePublication muda apenas o rascunho; requer ação explícita de publicar e fica desabilitada quando não há fonte compatível V5 (app/admin/admin.js:1141–1163,1489–1500). | Rótulo “Mostrar preços base no Viewer”; classe .pricing-publication-switch, input de 20 px, texto de 14 px bold e foco de 3 px (app/admin/admin.css:214–217). | Manter contrato próprio, separado de disponibilidade. Confirmar se o foco reforçado é exceção intencional frente ao foco geral de 2 px. |

## Padrões visuais que podem ser comparados

- São checkboxes HTML nativos; a fonte não aplica role=switch nem aria-checked. O nome da classe .switch não transforma o controle em switch semântico.
- .initial-state-option não define accent-color; a cor do primeiro screenshot pode vir do navegador/sistema. .switch usa o accent da marca. A diferença azul/bege observada é plausível, mas a cor exata depende do browser e do sistema.
- O rótulo inicial tem 10 px; .switch usa 12 px; publicação de preço tem 14 px bold e input de 20 px. Os focos declarados são 2 px no estilo geral e 3 px na publicação de preços.
- Nada nesta varredura comprova que essas diferenças expressem hierarquia visual intencional. Também não comprova CSSOM, contraste computado, aparência de disabled, navegação por teclado ou anúncio por leitor de tela.

## Decisões pendentes para o inventário

O Common Sense Judge fez uma leitura estática complementar em 13/11/2026 no Product ARC-13 HEAD `3b97542482ff9c1bdb2ad45aabf777f97991e60f`. Ela confirma as sete famílias da tabela e refina os itens em aberto:

1. **P1 — nomes acessíveis:** alinhar o nome do módulo à visibilidade real; decidir o rótulo de objeto, já que “Iniciar ativo” representa visibilidade; decidir se “Ativar etapa …” deve descrever disponibilidade atual quando o estado está marcado.
2. **P1 — rascunho versus disponibilidade pública:** acabamentos e puxadores alteram o rascunho e só chegam aos clientes depois de “Publicar configuração”. Decidir se o rótulo/contexto atual comunica essa transição.
3. **P2 — última opção:** confirmar se acabamento e puxador devem usar a mesma defesa/feedback ao tentar retirar a última opção. Hoje acabamento fica bloqueado preventivamente; puxador reverte a tentativa e mostra mensagem.
4. **P2 — hierarquia e accent:** decidir se o estado inicial por item deve manter accent nativo e 10 px ou seguir accent da marca; avaliar a saliência por família. “Sem cor/tinta base” não tem accent explícito.
5. **P2 — foco de preço:** confirmar se o foco de 3 px do controle de publicação é exceção intencional ao contorno geral de 2 px.
6. **Copy compartilhada:** os dois rótulos “Disponível para clientes” podem compartilhar chave de texto; isso não unifica estado, validação ou persistência.
7. **Antes de qualquer ajuste visual:** revisar Admin autenticado em claro/escuro, teclado e focus-visible, checked/unchecked, disabled por motivo, nomes/estados com leitor de tela e contraste CSS computado. Essa matriz ainda não foi executada.

Os dois exemplos do usuário compartilham checkbox nativo, mas não a função. Além disso, “Iniciar ativo” é usado tanto pelo ramo de objeto quanto pelo de serviço (`admin.js:244,266`); sem o item/contexto visível, a captura não distingue esses subtipos. Os sinks candidatos correspondentes são `852e7699499e4703` e `7ef47d84204a2578`; “Ativa” continua ligado ao sink de disponibilidade da etapa `372ab0a32af69fc6`.

Essas são pendências do inventário, não autorização para alterar produto. A revisão permanece estática, sem CSSOM, browser, leitor de tela ou aprovação de copy. As atualizações e os mesmos IDs estão reconciliados no juiz ARC-13 local; o histórico de IDs está na seção seguinte.

## Relação com os candidatos do inventário ARC-13

Os IDs abaixo são sinks candidatos do relatório lexical `docs/architecture/arc13/reviews/2026-11-13/admin-access.json` no checkout local de Product. Eles localizam texto e nomes acessíveis; não tornam as propostas de chave canônicas nem registram aprovação de copy.

| Sink | Papel no controle | Pendência ligada a esta revisão |
|---|---|---|
| 852e7699499e4703 + 3b963de4bff4c87e | Texto visível e aria-label da entidade no Configurador | Alinhar nome acessível do módulo à semântica de visibilidade; confirmar wording de objeto. |
| 709ad1019bfc6a05 + 53fb3aeaa2fdd8db | Texto visível e aria-label da visibilidade inicial no Viewer | Separar do estado inicial no Configurador apesar do texto e estrutura próximos. |
| 7ef47d84204a2578 + e0d9bd67f4de94ba | Texto visível e aria-label do serviço inicialmente ativo | Manter distinto da visibilidade de entidade. |
| 372ab0a32af69fc6 + 0664edc4b387792d | Estado visível da etapa e nome acessível | Revisar se wording e nome descrevem adequadamente o estado enabled/disabled. |
| 0a351b69a83f435b + 955c512b062561d1 | “Disponível para clientes” em acabamento e puxador | Pode compartilhar chave de copy; preservar modelagem e validação distintas. |
| 12a6c7bb28764426 | Publicação de preço base no Viewer | Preservar separado da disponibilidade ao cliente e validar o rótulo contra a publicação explícita. |

A revisão de fontes registra essas ocorrências; a análise G3 acrescenta contexto de função e estado. A classificação de textos e a aprovação lexical continuam sujeitas ao processo ARC-13.
