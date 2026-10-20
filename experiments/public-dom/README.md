# Auditor P0-R — DOM público e CSS computado (read-only)

Este instrumento **não é uma prova visual automática**; registra observações reproduzíveis do navegador sobre páginas públicas, sem sessão e sem escrita de dados do produto.

## Executar em um clone que tenha Node >= 20

Instale `playwright` em um ambiente isolado e o Chromium compatível (por exemplo `npm install --no-save playwright` e `npx playwright install chromium`). Então:

```sh
M2D_AUDIT_BASE_URL=https://casaemmodulos.casa \
M2D_AUDIT_WIDTHS=390,1366 M2D_AUDIT_THEMES=light,dark \
node experiments/public-dom/audit-public-dom.mjs
```

Produz `artifacts/public-dom-audit.json` ou o caminho indicado por `M2D_AUDIT_OUTPUT`. Também é apropriado para preview autorizado ou localhost. URLs fora de HTTPS e localhost são rejeitadas.

### Padrões de segurança e escopo

- Somente `page.goto` e leitura de DOM/CSS; **não** faz login, cliques ou gravações.
- O navegador executa a própria UI pública, inclusive buscas GET que a página normalmente faz. Bloqueia service workers; não injeta API privada.
- Não recolhe texto de página, valor de inputs, cookies, armazenamento, tokens, payloads, headers ou query strings. Guarda apenas DOM/classe/retângulo/atributos ARIA relevantes, estilos calculados e caminhos de recursos com status >= 400.
- Larguras e temas são amostras iniciais, **não** matriz obrigatória homologada. Evidência de iPad, WebKit, interação real e outras combinações continua independente.
- O Viewer depende de projeção pública válida. Se o endpoint não responder ou gerar erro, o resultado será registrado como indisponível e **não** assumirá equivalência.
- A saída é observação datada, não baseline imutável; snapshots não determinísticos podem ocorrer por fonte, carregamento e viewport.
- Não use este script em rotas com dados pessoais autenticados sem política separada de redação.

### Próximo gate

Depois de executar, classificar divergências por componente e rota, comparar estilos computados *antes/depois* de uma refatoração, e complementar com screenshots aprovadas e teste funcional. Não utilizar esse JSON isoladamente para declarar fidelidade visual ou segurança da aplicação.
