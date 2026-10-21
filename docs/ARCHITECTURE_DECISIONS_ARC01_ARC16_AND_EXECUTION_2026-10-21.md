# Contrato arquitetural consolidado — ARC-01…ARC-16 e plano de execução

**Data:** 2026-10-21. **Status:** direções arquiteturais aprovadas nas quatro rodadas de questionário; **não** é aprovação de novas escolhas estéticas, implementação, edição de dados de produção, merge automático de PR ou deploy.
**Produto de referência observado:** `EAKerber/MobiliPresenter2D@840a0cda361b3ce215fc934badc26df72dffc6e8` (PR #230 e controle global de preços base). Verificar heads vivos ao retomar.
**Fontes vinculantes:** `decisions.json` do Design System para homologação visual, especialmente NAV-004/005, VIS-002/003 e EST-01…10; este documento para direções **arquiteturais**. Não confundir um contrato técnico com nova homologação de aparência.
**Stack fixa:** HTML, CSS, JavaScript **puros** na interface. Sem React/Vue/Angular/Svelte, CSS-in-JS, bibliotecas de componentes, SSR/hydration ou framework de páginas. Ferramentas Node.js/esbuild já existentes no build/testes não introduzem framework frontend.

## 1. Resultado da rodada final — como interpretar BAAA

O usuário respondeu **13=B, 14=A, 15=A, 16=A**, pedindo compromisso entre A e B em **13 e 16**, com prioridade à opção efetivamente escolhida.

- **ARC-13, B dominante:** o **resultado exigido** é levantamento e extração abrangentes de textos localizáveis públicos, administrativos e de ferramentas para chaves/bundles estruturados versionados, incluindo a fundação de localização. **Compromisso operacional com A:** a substituição no runtime será feita por lotes reversíveis; não haverá migração big-bang, ativação de idiomas adicionais sem pedido nem bloqueio indiscriminado da fundação CSS até toda a migração ser publicada. Escopo/coverage total inventariado no início, execução incremental controlada. Não confundir textos de interface com conteúdo comercial de V5, dados de usuário, códigos operacionais ou mensagens do servidor que não pertençam à interface localizável.
- **ARC-16, A dominante:** um incremento só fecha com contrato e owner definidos, consumidores relevantes migrados, equivalência/fidelidade comprovada, segurança preservada e rollback registrado. **Compromisso com B:** não deixar duplicações efetivamente equivalentes em aberto *por omissão*: identificar e classificar todas as repetições do escopo e resolver as reais, ou justificar/excepcionar/adicionar backlog explícito com owner e gate. Não perseguir remoção máxima de semelhanças textuais se ela piorar responsabilidades ou custo.

## 2. Registro fechado ARC-01…ARC-16

| ID | Resposta | Direção aprovada | Limite vinculante |
|---|---|---|---|
| **ARC-01** | A | Implementação dos componentes compartilhados pertence ao repositório do **produto**; Design System define decisões, contrato e provas | Não estabelecer dependência de biblioteca externa de UI nem replicar duas fontes editáveis da mesma implementação |
| **ARC-02** | A | **Design System** é fonte canônica dos **tokens executáveis homologados**; CSS exportado determinística e versionadamente para o produto | Uso corrente de cor/medida sem homologação não vira token; produto não busca tokens em rede em runtime |
| **ARC-03** | A | **Fragmentos HTML compartilhados no build**; saída HTML estática semanticamente acessível antes do JavaScript | Evitar criar motor universal de template; preservar diferenças NAV-005 por profundidade e auth |
| **ARC-04** | A | **Fidelidade visual e funcional estrita** por padrão durante consolidação | Correções de defeitos e mudanças visuais deliberadas são incrementos próprios, homologados quando necessário |
| **ARC-05** | A | Compartilhar componente pela **mesma responsabilidade semântica/comportamental**, com **variantes explícitas** | Semelhança visual não obriga componente único; separar variantes divergentes, reutilizar primitivas quando cabível |
| **ARC-06** | A | **Controladores JS por componente**, com init/eventos/update/dispose quando pertinente; sem runtime central obrigatório | Evitar duplo listener, efeitos cruzados e acoplamento a DOM/IDs de página não declarados |
| **ARC-07** | A | **Composição híbrida**: HTML essencial materializado no build; JS nativo para interação e regiões genuinamente dinâmicas | Configurador e Viewer preservam renderers, projeções e contratos de dados próprios |
| **ARC-08** | A | **Tokens semânticos + CSS delimitado por família e variantes**, com estado e exceção explícitos | Reuso por nome de classe, cascata global inadvertida e reset amplo sem gate são proibidos |
| **ARC-09** | A + ressalva | Conteúdo editorial **versionado no código**, organizado para mudanças textuais/visuais e tradução futura; Design System fornece fundamentos de estilo de texto | Conteúdo editorial não é token CSS; mensagens e dados comerciais V5 não são fundidos; sem CMS automático |
| **ARC-10** | A | Estrutura e ordem de páginas públicas **explícitas em HTML**, compartilhando fragmentos de build | Manifeste de composição só quando necessidade estrutural for demonstrada; não tornar tudo runtime data-driven |
| **ARC-11** | A | **Core/domínio compartilhados** entre Configurador e Viewer, com apresentação, renderers e interações contextuais | Não duplicar autoridade comercial nem obrigar renderizador visual único |
| **ARC-12** | A | **Domínio/aplicação** controlam validação, autorização, salvamento, conflitos, retries e publicação; **componentes** apresentam estados/feedback | Componentes não inventam permissões, repetem operações críticas ou decidem persistência |
| **ARC-13** | **B + compromisso A** | **Inventariar e extrair integralmente os textos localizáveis** para recursos estruturados e chaves semânticas | Execução em lotes, pt-BR preservado, fixtures/CI e sem obrigação de lançar novas línguas agora |
| **ARC-14** | A | Tokens DS integrados no produto por **versões explícitas e PR de integração**, com CSS gerado e hash/manifesto rastreável | Nada de sincronização contínua automática diretamente em produção ou manipulação manual paralela dos valores |
| **ARC-15** | A | **Matriz de testes representativa baseada em risco**, com aumento por evidência e fluxos críticos | Testes automáticos, inspeção visual e funcional em dispositivo real são evidências diferentes, não substituíveis |
| **ARC-16** | **A + compromisso B** | Concluir incremento só com **contrato, equivalência, benefício, consumidores, owner, gate e rollback** | Auditar duplicações no escopo e eliminar as reais ou registrar exceção/backlog justificados; não otimizar contagem cega de linhas |

**Compatibilidade de ARC-09 e ARC-13:** ARC-09 escolhe *propriedade/forma de publicação* (código versionado e sem CMS), enquanto ARC-13 escolhe *abrangência da extração/localização* (cobertura sistemática, não só textos reutilizados). Não são decisões contraditórias.

## 3. Arquitetura alvo — autoridades e passagem de dados

```text
Design System [decisions.json homologações]
  └── tokens aprovados (fonte executável estruturada)
      └── export determinístico versionado / PR revisada
          └── CSS custom properties consumidas no produto

Produto [fonte executável de componentes HTML/CSS/JS]
  ├── contracts + variants + states + controllers por componente
  ├── fragments HTML -> build time -> páginas HTML estáticas
  ├── conteúdo editorial e mensagens -> bundles pt-BR localizáveis (em código)
  ├── Landing / About / How / Acesso / Admin -> composição por página
  └── Configurador / Viewer e derivados
       └── dados do domínio V5 / catálogo / cena / pricing
            -> projeções seguras por consumidor -> renderers especializados
```

**Distinção importante:** Centralização significa *um owner por responsabilidade* e não *um arquivo universal* ou *tudo em JSON*. Separar conteúdo editorial, localização/UI, tokens de aparência, domínio comercial, sessão/segurança e estado transitório.

## 4. Contratos técnicos mínimos a produzir

### 4.1 Tokens e integração DS→produto

- Fontes canônicas DS separadas em **aprovado executável** e **candidatos/uso observado/pendências**; vincular cada token a decisão/escopo/tema/estado.
- Export CSS custom properties reproduzível por **Node.js puro**, acompanhado de commit do DS, versão semântica interna ou manifesto/hash fixo e lista de consumidores.
- Produto incorpora a exportação por **PR explícita**. CI verifica origem, integridade, duplicação de overrides, tema claro/escuro, contrastes nos pares pertinentes, regressões de cascata e rollback; nunca depender de fetch externo no navegador.
- Arquitetura de distribuição **aprovada**; nomes de arquivos, serialização, semver e implementação do gerador ainda são **decisões técnicas de incremento**.

### 4.2 Componentes HTML/CSS/JS

- Responsabilidade e consumidores declarados, inclusive Landing; variantes p.ex. cabeçalho `public-primary`, `public-secondary` (Viewer), `private` conforme NAV-005.
- HTML inicial essencial incluído no artefato final; parâmetros de fragmento explicitamente permitidos/escapados; sem executabilidade arbitrária em manifestos.
- CSS de escopo próprio com tokens homologados, sem uniformizar homônimos; controladores JS vanilla por componente, inicialização idempotente ou dispose explícito onde dinâmico, sem framework.
- Gates para DOM, ARIA, teclado, foco, touch, tema, motion, compactação, screenshot/estilo computado e ausência de quebra sem JS onde cabível.

### 4.3 Textos e localização (prioridade ARC-13)

**Resultado desejado, abrangente:** um catálogo de **todas as strings localizáveis** do UI nas rotas públicas e privadas, componentes, mensagens e `aria-label`/`alt` textuais; também plurais, parâmetros, datas, moedas e estados de erros apresentados ao usuário. Inventariar textos em HTML, JS dinâmico e templates. Não traduzir identificadores de dados, contratos API ou mensagens técnicas não destinadas ao usuário.

**Caminho reversível:**
1. Extração estática e inventário com `route/file/line/consumer/key/currentText/owner/status`. Classificar texto localizável, comercial autorado no V5, código/ID, texto decorativo e conteúdo sensível; evitar extrair PII/segredos.
2. Convenção simples de keys por domínio (`landing.hero.title`, `ui.menu.open`, `admin.publish.confirm`); catálogo `pt-BR` versionado no **produto**, estrutura pronta para variantes de idiomas posteriores, sem instalar biblioteca i18n nem API dinâmica externa.
3. Substituição de literais por lotes de componente/rota (incluindo HTML build fragments) com diffs de texto/pontuação/ARIA zero; interpolação segura via `textContent`/atributo e `Intl` nativo para formatos quando oportuno; CI contra keys órfãs, valores ausentes e duplicações semânticas.
4. Gate final de **cobertura integral dos textos localizáveis inventariados**, com lista explícita de exceções: valores comerciais oriundos de configuração, autoria de usuário e conteúdo que deve permanecer como data; não exigir idiomas extras antes dessa cobertura.
5. O inventário completo começa **já em V0/V1**, execução acompanha V2/V3/V4 e **não bloqueia** correções de P0/autenticação nem fundação de tokens em componentes já inspecionados.

### 4.4 Configurador/Viewer e móveis reais

- Proteger `ConfiguratorAdministration2D 5.0`, `ConfiguratorPresentation2D 1.1`, catálogo, cena, preços, DTO públicos, permissões e publicação. Não abrir migração schema por padronização visual.
- Garantias centrais existentes (seleção de módulos, etapas, itens admitidos, checkboxes e dependências) são baseline a preservar; pequenas extensões pontuais são preferíveis a abstração universal.
- **Não usar móveis/módulos fictícios como condição de aprovação**. Adições futuras serão testadas com assets/dados concretos no momento em que existir um novo móvel real; consultar coverage de autoria/catalogação então. Por ora, manter testes existentes com fixtures técnicas de regressão do V5 sem construir entidades hipotéticas para provar generalidade.

### 4.5 Compatibilidade, riscos e gate de parada

- O relato iPad antigo foi reclassificado pelo usuário como **provável limitação da versão do dispositivo, resolvido para prioridade atual** após sucesso em dispositivos recentes. **Compatibilidade com aparelhos/OS legados é backlog futuro de baixa prioridade**, sem nova campanha de teste real específica agora. Isto **não** encerra as issues transversais de autenticação `#212`/`#213` nem substitui verificações responsivas essenciais.
- Testes ARC-15: matriz de risco por rota/contrato e dispositivos atuais; incluir falhas conhecidas, navegação, sessão, foco, temas, zoom, movimento reduzido e dado ausente/invalidado. Não tornar todos os pixels/dispositivos combinatórios exigência universal.
- **Saída ARC-16:** cada incremento publica tabela de `component/owner/consumers/duplicates found/duplicated authority? /resolved|exception|backlog/gates/delta/rollback`; cerrar somente com testes aplicáveis e benefício verificável. Duplicação legítima de domínio/semântica não vira débito fictício.

## 5. Roadmap operacional (reordena V0–V6 sem reabrir fases concluídas)

| Gate | Trabalho | Pronto quando | Dependência/risco |
|---|---|---|---|
| **V0 — atualizar autoridades** | Conferir main e deploy; reconciliar PR #39 e #41 sem merge indiscriminado; atualizar inventário pós-#230 e preços; mapear `ARC`/NAV por rota; abrir inventário **integral** de strings localizáveis | mapa de owners e mudanças desde `1878ae1`, gaps/documentos históricos identificados; nenhum runtime alterado | prioridade imediata |
| **V1 — estabilizar e medir** | Auditar DOM estático/dinâmico e CSS por componente; triagem de bugs atuais (#224, #215, #218, #208, #212/#213), CI conhecida; preparar matriz de risco | causas classificadas, baselines reproduzíveis e separação defeito vs refactor | sem exigir iPad legado |
| **V2 — tokens/versionamento** | Selecionar somente tokens aprovados; estabelecer gerador DS→CSS, manifesto pinado e PR de consumo no produto; começar com uma família | CSS, DOM, tema e contraste preservados nos consumidores; atualização rastreável e rollback simples | depende das decisões VIS pendentes nos pares ainda não aprovados |
| **V3 — componentes básicos** | Controlador de tema, menus, headers por profundidade, foco, botões, estados; comportamento encapsulado, CSS delimitado e fragmentos iniciais simples | contrato compartilhado funciona em Landing/Viewer/Config/Admin/Acesso com variantes preservadas; sem regressão | experiências P1–P4 são referência, não pacote a mesclar |
| **V4 — composição e localização** | Expandir fragments build-time e extrair **todos** textos localizáveis em lotes; `pt-BR` fiel, `Intl` onde pertinente, sem editor de layout universal | cobertura/keys/ARIA completos ou exceções motivadas; páginas essenciais não dependem de JS para markup estático | não inferir que EditorialContent exige CMS |
| **V5 — ferramentas derivadas** | Consolidar reuso de tokens/componentes com as projeções do Core; observar extensões concretas de domínio somente quando novo móvel real chegar | schema/projeção e seleção/preço/cena existentes intactos; sem experimento de móvel fictício | extensão de domínio por novo requisito real |
| **V6 — homologação e release** | Testes por risco, inspeção visual e funcional distintas; validar previews necessários, readback, CI/rollback e métricas de duplicações | contratos, fidelidade, consumidores, pendências e exceções rastreáveis; sem regressões P0 | deploy previews apenas quando agregam evidência |

**Execução incremental, sem esperar V4 para criar tokens:** o inventário completo das strings começa agora, e a substituição percorre as famílias conforme passam pelo gate de componentes; mudanças de texto são independentes de alterações de estilo/DOM. Novos idiomas e editor de conteúdo continuam fora do escopo por ora.

## 6. Ajustes em documentos e dívida de decisão

1. **Documento de arquitetura anterior** `ARCHITECTURE_VANILLA_COMPONENTS_AND_DOMAIN_DATA_2026-10-21.md` contém recomendações anteriores às 16 respostas: o presente registro **supersede** as recomendações abertas sobre forma de distribuição de tokens, HTML, i18n e critérios de encerramento, mas preserva a direção Vanilla/domínio.
2. **Roadmap atual** `ROADMAP_AND_CURRENT_STAGE_2026-10-21.md`: o futuro “schema de interface data-driven” não constitui uma obrigação de transformar as páginas; textos/localização agora têm extração abrangente deliberada e imediata em fases, sem CMS.
3. `decisions.json` é autoridade de **homologação visual**, não deve receber estes ARC como se fossem aprovações de cores ou layout. Este arquivo é o registro das decisões arquiteturais.
4. PR #39 draft com divergências e pilotos P2/P3/P4 isolados: portar aprendizados e código individualmente somente após gates com produto main atualizado; não induzir merges automáticos de branches antigas.
5. **Pendências técnicas que podem ser decididas sem perguntar novamente ao usuário**: formato da fonte dos tokens aprovados, gerador Node, formato do catálogo pt-BR, escape e parâmetros, estratégia de fragmentos, convenção de nome de variante, lifecycle dos controladores e relatórios de cobertura/duplication.
6. **Decisões que requerem usuário apenas se surgirem**: novos valores visuais não homologados, aparência intencionalmente diferente, suporte a idioma novo efetivo, edição editorial via Admin, mudanças comerciais/autorização, requisito de móvel que realmente transcenda o V5, ou custo/escopo alto sem valor comprovado.

## 7. Primeiro incremento pronto para planejar (V0-A)

**Escopo exclusivamente documental/read-only de produto:**
- Atualizar ponteiros de HEAD do produto/DS, inventário de rotas/consumidores e matriz ARC/NAV; identificar o delta `1878ae1→840a0cd` incluindo #230, price flag e mudanças de auth, sem editar produção;
- Construir duas matrizes: `route/component/owner/current files/contracts/variants/duplicated authority/risk` e `localized string/key/source route/context/owner/status`, para todas as rotas pertinentes;
- Marcar prioridades de migração de tokens/componentes e conteúdo por **conjunto de consumidores reais**, escolher primeira família pequena que possa ser validada sob ARC-04 e ARC-15;
- Conciliar PR #39 somente em documentos focados: divergências e resultados experimentais não transferem automaticamente autoridade à main.

**Condição de saída:** relação explícita de decisões aprovadas versus tokens candidatos, bugs atuais separados, dependências de CSS/cascade e plano de PRs pequenos com rollback. **Nenhum preview necessário para este gate documental.** Seguir ao piloto técnico V2 apenas com escopo e testes especificados.
