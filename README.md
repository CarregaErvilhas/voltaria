# Voltaria

Agent Skills com conhecimento atual e fiável sobre mobilidade elétrica em Portugal, escritas para
agentes (assistentes de IA), em pt-PT.

- `skills/<nome>/SKILL.md`: uma skill por tema.
- `knowledge/`: factos com fonte e data de verificação.
- `glossario.md`: os termos a usar.
- `site/`: o site para pessoas, [voltaria.ocarroeletrico.com](https://voltaria.ocarroeletrico.com), que explica o que é o
  Voltaria e como o usar através do [ohmigo](https://ohmigo.ocarroeletrico.com).

## Plugin para o Claude

Este repo é também um plugin: `.claude-plugin/plugin.json` na raiz. Instalado no Claude (chat,
Cowork ou Claude Code), dá as skills de `skills/` e liga o
[ohmigo](https://ohmigo.ocarroeletrico.com), o servidor MCP com os preços de carregamento em
Portugal. Quem só quer as regras e o saber prático usa as skills, e o Claude só chama o ohmigo
quando a pergunta é um preço.

### Dados

O plugin não corre código, não guarda nada e não tem hooks. As skills são texto que o Claude lê.
O único envio de dados é o das chamadas ao ohmigo (`https://ohmigo.ocarroeletrico.com/mcp`), com o
que o assistente põe em cada pergunta (sítio ou rota, carro, tarifas). O ohmigo não guarda nada
ligado a quem pergunta: ver a [política de privacidade do ohmigo](https://ohmigo.ocarroeletrico.com/privacidade)
e a [do Voltaria](https://voltaria.ocarroeletrico.com/privacidade/).

## Licença

- **Conteúdo** (`skills/`, `knowledge/`, `glossario.md` e o resto do texto): [CC-BY-4.0](LICENSE).
- **Código** (`scripts/`, testes, `.github/`, o HTML, CSS e JavaScript do `site/`): [MIT](LICENSE-CODE).

Podes usar, adaptar e redistribuir, incluindo para fins comerciais, desde que credites:

> Conteúdo do Voltaria (https://github.com/CarregaErvilhas/voltaria), CC-BY-4.0.

Num assistente ou num site, basta uma linha destas junto do conteúdo, no rodapé ou numa página de
créditos. Se alterares o conteúdo, diz que foi alterado.

### O nome e a imagem ficam de fora

As licenças cobrem o conteúdo e o código, não a marca. Não estão licenciados:

- o nome **Voltaria**, a mascote (o livro azul com o raio), o ícone e as imagens feitas com eles, no
  `site/` (os desenhos em `index.html` e `og-card.html`, e os ícones e imagens em `site/static/`);
- a mascote do **ohmigo**, que aparece no site e é do ohmigo.

Podes, e deves, usar o nome para dizer de onde vem o conteúdo, como pede a linha de crédito acima.
Um fork ou uma obra derivada precisa de nome e de imagem próprios.

A fonte Nunito, servida pelo site, tem a sua licença: [SIL OFL 1.1](site/static/fonts/OFL-Nunito.txt).

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md). Sem CLA: basta `git commit -s`.
