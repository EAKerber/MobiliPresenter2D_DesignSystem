# VIS-002C — autorização contextual e regra preventiva de contraste textual

**Data:** 22/10/2026 (America/Sao_Paulo). **Decisão expressa do usuário neste turno:** utilizar as cores já homologadas e corrigir/prevenir a escolha de pares inadequados, preferindo regras reproduzíveis a aplicações acidentais.

## Diagnóstico causal

A cor legada `--public-muted: #706C66` do produto é declarada em `app/public-theme.css`. Não há evidência de gerador de Design System que tenha recomendado automaticamente a combinação legada. CSS com `color: var(--public-muted)` foi reutilizado em fundos `#E8E3DC` e `#F0EDE8`, abaixo de 4,5:1 para texto comum, sem um gate por contexto. O problema é **ausência de vínculo verificado entre papel semântico, superfície, tema e estado**, não deficiência de um algoritmo de otimização de cores.

## Decisão delimitada

Aprovar a **extensão contextual** do uso do texto secundário já homologado `VIS-002.approvedPalette.colors.textSecondary.light = #705C4B` aos cinco textos legíveis abaixo, **somente no tema claro**, sem aprovar alteração do token global nem troca irrestrita da paleta:

| Rota | Seletor contextual aprovado | Fundo observado no gate | Razão esperada |
|---|---|---|---:|
| `/` | `.story-section > p:not(.eyebrow)` | `#E8E3DC` | 4,9534 |
| `/` | `.feature-copy > p:not(.eyebrow):not(.feature-availability)` | `#F0EDE8` | 5,4146 |
| `/about/` | `.about-closing > p:not(.eyebrow):not(.about-closing__signature)` | `#F0EDE8` | 5,4146 |
| `/about/` | `.about-scale__stat > span` | `#F0EDE8` | 5,4146 |
| `/how-it-works/` | `.finish-copy > p:not(.eyebrow):not(.finish-signature)` | `#F0EDE8` | 5,4146 |

**Exceções obrigatórias:** manter `.feature-availability`, `.finish-signature`, `.about-closing__signature`, tags `.eyebrow`, pares aprovados anteriores e todos os textos no tema escuro. Não alterar domínio, mensagens comerciais, autenticação nem `--public-muted` globalmente.

## Norma preventiva — contrato operacional

1. Um valor da paleta ser homologado **não significa** que qualquer par de cores ou consumidor o seja. A chave de associação é `(papel semântico, rota/componente, estado, tema, fundo efetivo, tamanho/peso)`.
2. Antes de usar novo token ou estender um papel a um consumidor: verificar par texto/fundo em CSS computado, incluindo cascata real, superfície opaca, transparência, imagens e estados pertinentes. Texto normal: contraste `>= 4.5`; texto grande: `>= 3`; componente/indicador significativo: `>= 3` onde aplicável. Nunca arredondar para atingir o limiar.
3. **Fail closed** por seletor/estado homologado: rota ausente, tema errado, par diferente, regra vencedora incerta, razão insuficiente ou mudança na semântica dos estados reprovam o gate. Um caso com fundo/foreground não aferível vira `UNVERIFIED`, nunca PASS.
4. Preferir o valor de token/papel homologado; **não criar um algoritmo gerador de cores** que escolha a alternativa esteticamente por conta própria. Um eventual mecanismo de sugestões pode listar candidatos, contrastes e evidências, mas não pode escrever CSS de produção ou transformar um candidato em aprovado.
5. A mudança aplicada deve ser local, aditiva e reversível; teste de exclusões (estados, assinaturas) e tema escuro precisa ficar junto ao contrato. Comparação de browser não substitui inspeção visual completa nem teste funcional de dispositivos.
6. **Prevenção contínua:** quando o componente mudar cor/fundo/tema/estado, reexecutar os checks de CSS computado e atualizar allowlist homologada ou bloquear a mudança. O gate cobre apenas escopo explicitado; outras páginas continuam `not-evaluated`.

## Evidência de autorização e implementação

- [Inventário AUDIT-PUBLIC-TEXT-01](PUBLIC_TEXT_CONTRAST_AUDIT_2026-10-22.md): 36/36 cenários; cinco contextos falhando antes da correção.
- [Experimento visual AUDIT-PUBLIC-TEXT-02](PUBLIC_TEXT_CONTRAST_CANDIDATE_2026-10-22.md), [Actions #39888294326](https://github.com/EAKerber/MobiliPresenter2D/actions/runs/39888294326): 36/36 browser scenarios, 36 alterações light, 36 equivalências dark, 84 controles negativos e capturas comparativas. **O PASS do experimento não representa sozinho homologação de produção ou validação de todos os dispositivos.**
- Decisão deste turno autoriza o mapeamento contextual acima; o patch do produto fica em branch independente com gate próprio. **Nenhuma instrução de merge ou publicação automática**.

## Compatibilidade com o pipeline canônico

`decisions.json` contém `VIS-002.approvedPalette` como origem dos **valores**, e o exportador P-TOKEN-01 fixa seu Git blob SHA para impedir alterações silenciosas. **Este contrato de mapeamento contextual não altera a paleta nem o blob de decisions.json**: é um adendo de consumidores homologados, versionado por documento, até integração explícita ao schema/pipeline de tokens com atualização de versão, hashes e testes. Evitar desarmar o gate pinado para registrar a nova regra.
