# Contribuir para o Voltaria

Obrigado. Não há papelada: não assinas nenhum acordo nem cedes direitos.

## Assinar os commits (DCO)

Cada commit leva uma linha `Signed-off-by`, que o git acrescenta com `-s`:

```sh
git commit -s -m "incentivos: atualiza o apoio do Fundo Ambiental"
```

Com ela certificas o [Developer Certificate of Origin](DCO): que o contributo é teu, ou que tens o
direito de o enviar, sob a licença do projeto. O nome e o email têm de ser reais e iguais aos do
autor do commit. Esqueceste-te? `git commit --amend -s` no último commit, ou
`git rebase --signoff main` para todos os do branch.

Uma verificação automática recusa PRs com commits sem assinatura.

## Licença dos contributos

O que envias fica com a licença do resto do repo: [CC-BY-4.0](LICENSE) para o conteúdo, [MIT](LICENSE-CODE)
para o código. As duas são irrevogáveis: o projeto e quem o usa podem continuar a usar o teu
contributo, e tu continuas a ser o autor. O crédito fica no histórico do git.

## Conteúdo de terceiros

As FAQ e os guias de outros (UVE, MOBI.E, ...) são **fontes, não texto**. Escreve por palavras tuas e
indica a origem em `source{url,name}` com `checkedAt`. Para copiar texto tal e qual, é preciso
autorização escrita do autor, registada no repo.

As autorizações ficam em `docs/fontes/<autor>.md`, com o que veio de cada página e para onde foi. A
UVE autorizou o uso do seu conteúdo com crédito ([docs/fontes/uve.md](docs/fontes/uve.md)). Mesmo
assim reescrevemos: a autorização não cobre pôr o texto da UVE sob a licença do Voltaria. A exceção
é o manual da UVE para novos condutores, que tem licença CC BY 4.0: pode ser adaptado, com crédito e
indicando que foi alterado. Os pontos que vêm da UVE levam a marca `[UVE, …]` na skill.

Fontes dos incentivos: só oficiais (Fundo Ambiental, AT, Diário da República). Exceção: os benefícios
municipais de estacionamento vêm da lista da UVE, com a ligação da câmara em `official`.

## Revisão

Tudo entra por PR, revisto pelos CODEOWNERS.
