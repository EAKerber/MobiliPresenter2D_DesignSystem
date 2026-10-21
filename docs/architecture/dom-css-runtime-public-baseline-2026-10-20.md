# P0-R — Linha de base de DOM real e CSS computado em páginas públicas

**Data:** 2026-10-20  
**Estado:** PASS na coleta pública representativa em Chromium; **não** homologação visual ou compatibilidade geral.  
**Produto observado:** [`EAKerber/MobiliPresenter2D@1878ae1`](https://github.com/EAKerber/MobiliPresenter2D/tree/1878ae1057ce7c6190e0c8cb08a1f3baadd49463), publicado em `https://casaemmodulos.casa/`.  
**Instrumento:** [audit-public-dom.mjs](../../experiments/public-dom/audit-public-dom.mjs); [README](../../experiments/public-dom/README.md).  
**CI comprovada:** [GitHub Actions #39503394834](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39503394834), `success`; artefato `public-dom-audit` com observações detalhadas retido conforme prazo do workflow.

## Escopo executado

- Rotas: `/`, `/about/`, `/how-it-works/`, `/viewer/`.
- Viewports: larguras **390** e **1366**; altura 900; `colorScheme=light/dark` e preferência de tema explícita via `casa-ui-theme-mode-v1`; `reducedMotion=reduce`.
- Matriz: 4 páginas × 2 larguras × 2 temas = **16 observações**, todas com `GET` status HTTP 200, sem erro HTTP de recursos na mesma origem, sem exceção JavaScript capturada, e `data-theme` resolvido correspondente ao modo pedido.
- Sem login, credenciais, interação que mude estado comercial, `POST`, gravação de configuração, Netlify deploy ou arquivos do produto alterados.
- Fonte: DOM realmente construído no Chromium e `getComputedStyle()`, não somente HTML estático. Payload do JSON é de classes, atributos de acessibilidade e medidas/estilos, sem conteúdos pessoais.

## Resultados observados

| Rota | Elementos DOM por combinação | Alvos de DOM dinâmico | Resultado |
|---|---:|---|---|
| `/` Landing | 146 | 4 nós `.benefit-item` | 4/4 observações carregadas |
| `/about/` | 91 | conteúdo editorial predominantemente em HTML | 4/4 |
| `/how-it-works/` | 486 | HTML editorial, `details` nativo | 4/4 |
| `/viewer/` | 223 | 4 `.viewer-block`; 7 `.scene-hotspot` | 4/4 |

**A contagem é de elementos no DOM de cada página**, não de componentes de arquitetura nem de classes únicas. Pode depender do produto, da publicação e de estado assíncrono. São valores de referência deste snapshot, não invariantes exigidos em todos os futuros designs.

### Exemplos de valores CSS computados (dados da execução)

| Rota / componente | Claro — `color` | Escuro — `color` | Observação |
|---|---|---|---|
| Landing `.site-header` | `rgb(34, 33, 31)` | `rgb(244, 241, 235)` | background claro `rgba(255, 255, 255, .94)`; escuro `rgba(27, 28, 26, .94)` |
| About `.eyebrow` | `rgb(110, 81, 46)` | `rgb(226, 201, 145)` | background transparente |
| How `.eyebrow` | `rgb(139, 106, 64)` | `rgb(216, 188, 124)` | background transparente |
| Viewer `.viewer-heading` | `rgb(34, 33, 31)` | `rgb(244, 241, 235)` | background transparente |

**Conclusão restrita:** os estilos de contexto/tema realmente resolvem valores diferentes no navegador, mas sem comparação de screenshot não se deduz contraste homologado, ausência de colisão visual nem fidelidade após uma refatoração.

## Acordos arquiteturais derivados de P0-R

1. **Registrar estado renderizado** como camada de evidência separada do mapeamento lexical de `visual-inventory.json`.
2. Comparar componente por componente — por exemplo, `#benefits .benefit-item` — usando DOM/atributos e estilos computados como contrato de regressão observável; **não** usar contagem geral de DOM como gate absoluto.
3. Não automatizar reescrita CSS por nome repetido ou estilo semelhante: `.eyebrow` tem cor calculada diferente entre About e Como funciona mesmo usando o mesmo nome de classe.
4. Uma igualdade de `getComputedStyle` em 2 viewports não equivale à inspeção visual nem à ergonomia; gates funcionais/manuais/visuais continuam independentes.
5. Não ligar autenticação de Admin ao auditor de páginas públicas; testes de sessão precisam de autorização e procedimento específicos, sem expor payload.
6. Mantenha `prefers-reduced-motion: reduce` como dimensão explícita observada, não como aprovação do estado com animações normais. O auditor não clica nem percorre interações.
7. A política de mudança é PR pequena, materialização verificada antes/depois e rollback isolado; script de auditoria não publica qualquer dado.

## Limites e próximos gates

- Publicação e assets são externos; o relatório detalhado do workflow é artefato com retenção limitada. Este checkpoint mantém os fatos de maior valor de forma durável.
- Sem Safari/WebKit/iPad, login, teclado, foco, menu aberto, carrossel interagido, múltiplos zooms, contraste perceptual, performance de longo prazo, área protegida, ou comparação visual pixel-a-pixel.
- Os números do Viewer não provam conteúdo editorial, preço ou dados administrativos; o Viewer opera sobre projeção pública limitada.
- O instrumento ainda é de **observação de estado inicial**: para afirmar regressão ou equivalência, exige baseline de comparação *antes/depois* e contratos de alteração específicos.
- **P2 sombra realizado PASS**: [GitHub Actions #39503582819](https://github.com/EAKerber/MobiliPresenter2D_DesignSystem/actions/runs/39503582819) confirmou `P2_SHADOW_EQUALITY` = `domEquivalent:true`, `rows:4` para `landing/benefit-strip@1`. A comparação conferiu `tag`, `className`, ordem dos filhos, `img[src/alt]` e texto dos `span` com o DOM real de `#benefits`; houve **zero mudanças no DOM do produto**. É equivalência de estrutura e conteúdo no estado observado, não equivalência de CSS pós-refatoração ou visual pós-substituição. O mesmo workflow voltou a registrar P0-R `total=16 ok=16`.
