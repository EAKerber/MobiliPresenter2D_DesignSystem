# Revisão manual do preview VIS-002C v0.3 — 25/10/2026

## Alvo e limites

- Produto PR [#241](https://github.com/EAKerber/MobiliPresenter2D/pull/241), head `baef9acd71bc636db66709d93c0d5cf0ab5d0134`.
- Preview: [deploy principal](https://deploy-preview-241--mobilipresenter2d.netlify.app/).
- Teste manual em sessão isolada do preview; nenhum dado de conta foi lido ou enviado.
- Viewport mobile: 390 × 844 CSS px; também houve leitura em 1280 px na landing e em Quem somos.
- Esta revisão cobre os sete seletores candidatos da v0.3; não é auditoria WCAG da página inteira.

## Resultado dos sete seletores mapeados

No tema claro, os sete contextos renderizaram `rgb(41, 39, 35)` (`#292723`) nos seletores definidos pelo mapa: dois na Landing, dois em Quem somos e três em Como funciona. Os fundos observados foram `#E8E3DC` e `#F0EDE8`; os contrastes registrados no mapeamento são 11,68:1 e 12,77:1.

No tema escuro, os sete contextos voltaram a `rgb(196, 188, 178)` (`#C4BCB2`) sobre `rgb(32, 33, 31)` (`#20211F`); a regra clara não vazou para o tema escuro. A leitura incluiu a navegação real do controle de tema.

Em 390 px, `documentElement.scrollWidth` foi 390 px nas três rotas. A captura desktop da Landing mostrou a composição principal; a faixa fixa do Netlify Drawer apareceu na borda inferior do viewport e não encobriu o texto revisado.

## Contextos anteriores preservados

A distribuição v0.3 preserva intencionalmente os três contextos mapeados na v0.2. Na amostra clara, textos longos existentes fora dos sete seletores novos continuam em `#705C4B`: `.hero-description` na Landing, `.about-scale p:not(.eyebrow)` em Quem somos e `.how-hero-note` em Como funciona. Sobre a superfície observada `#F0EDE8`, o par `#705C4B`/fundo tem contraste calculado de 5,41:1, acima do mínimo de 4,5:1 para texto comum. Essa leitura confirma contraste, não a preferência tonal.

Esses contextos foram mantidos fora da alteração restrita aos sete contextos medidos da v0.3. A preferência do usuário por cores próximas de preto/branco para texto corrido pode motivar uma reconciliação posterior do mapeamento v0.2 e da PR de produto #240; esta evidência não amplia a autorização da PR #241 nem declara que os três contextos anteriores devem mudar.

## Estado

Revisão visual pontual concluída para o preview/head indicados. O resultado sustenta o comportamento de tema e os sete contextos aprovados nesta amostra. PRs de Design System #52 e produto #241 continuam DRAFT; sem merge ou deploy de Production.
