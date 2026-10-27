# /access/: cabeçalho e menu em produção

**Observado em:** 20/10/2026  
**Produto:** `EAKerber/MobiliPresenter2D`, `main`, commit [`1878ae1`](https://github.com/EAKerber/MobiliPresenter2D/commit/1878ae1057ce7c6190e0c8cb08a1f3baadd49463)  
**Deploy:** [`6ad6c3b51b6be05647167f94`](https://app.netlify.com/projects/mobilipresenter2d/deploys/6ad6c3b51b6be05647167f94), produção publicada  
**Contexto:** navegador isolado e sem sessão; nenhum dado de conta alterado ou registrado.

## Capturas

- [Tema claro, menu aberto](../../visualEvidence/private/access-confirmation/access-menu-light-2026-10-20.jpg)
- [Tema escuro, menu aberto](../../visualEvidence/private/access-confirmation/access-menu-dark-2026-10-20.jpg)

Ambas usam viewport CSS de 390 × 844 px, DPR 1, em `/access/`. A página não recebeu token de acesso; mostra a orientação para solicitar um novo link.

## Navegação

O menu abriu no primeiro clique. No estado anônimo, a seção privada contém apenas **Entrar na administração**; a seção pública lista **Ambientes**, **Cozinha**, **Como funciona**, **Quem somos** e **Fale conosco**. Pressionar Escape fechou o menu e devolveu o foco ao botão. A largura do documento permaneceu em 390 px, sem overflow horizontal.

A experiência autenticada e o acesso por link válido não foram testados nesta visita. A observação não confirma o fluxo de convite.

## Superfícies e paleta

As cores computadas no DOM foram:

| Tema | Cabeçalho | Menu | Corpo | Texto |
|---|---|---|---|---|
| Claro | `#FFFFFF` | `#FFFFFF` | `#F7F5F2` | `#22211F` |
| Escuro | `#171816` | `#1B1C1A` | `#111210` | `#F4F1EB` |

A paleta homologada registra superfície clara `#F0EDE8`, canvas escuro `#171614` e superfície escura `#211F1C`. O branco puro do cabeçalho e do menu claro diverge da superfície aprovada; os valores escuros observados também não correspondem exatamente às amostras neutras registradas. Isso é um desvio de aplicação em componente, não uma nova decisão de cor. A escolha do valor por camada deve preservar a hierarquia entre canvas, cabeçalho e popover. O mapeamento fica em **FIND-015**.

O cabeçalho computou `z-index: 60`; o menu, `z-index: 80`. O menu cobre conteúdo da página enquanto aberto. Esta rota não contém a cena do Configurador e, portanto, não fornece evidência para a sobreposição de cena registrada em FIND-009.

## Rede e limites

Os arquivos da rota e o bundle de navegação carregaram com status 200. A chamada sem token a `POST /api/access/session` respondeu 404, observação já rastreada separadamente em FIND-014 e no [issue #222](https://github.com/EAKerber/MobiliPresenter2D/issues/222). Sem um token válido, a resposta não valida nem invalida o caminho de criação/consumo de uma sessão temporária.

Nenhum código do produto foi modificado. Nenhuma credencial, email ou convite foi usado ou copiado.

A tela administrativa anônima foi capturada no mesmo commit e viewport. Sua evidência está em [admin-login-menu-2026-10-20.md](admin-login-menu-2026-10-20.md); nela o cabeçalho claro usa a superfície aprovada, enquanto o menu ainda usa branco puro.
