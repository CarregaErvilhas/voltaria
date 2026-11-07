# O site do Voltaria

O site para pessoas, em https://voltaria.ocarroeletrico.com: explica o que é o Voltaria e manda
instalar o ohmigo para o usar. É uma página só, em português (`/`) e em inglês (`/en/`).

## Como está feito

- `index.html` é o modelo. Um elemento com `data-i="chave"` recebe o texto dessa chave; uma chave entre
  chavetas duplas recebe-o escapado (para atributos e para o `<head>`). As chaves `page.*` vêm do script.
- `strings.json` tem o texto, com as mesmas chaves em `pt` e `en`. O português segue o
  `glossario.md`, como as skills.
- `static/` é copiado tal e qual: a fonte (Nunito, com a licença ao lado), o ícone e as imagens das
  pré-visualizações de links.
- `og-card.html` é o desenho dessas imagens. Não é publicado.

`scripts/build-site.py` junta tudo em `_site/`: as duas páginas com o texto já lá dentro, a lista de
temas tirada de `skills/`, e `robots.txt`, `sitemap.xml` e `llms.txt` (o resumo para agentes, também
gerado a partir das skills). O `pages.yml` corre-o e publica o resultado a cada push para `main` que
mexa no site ou nas skills.

## Mudar alguma coisa

```sh
scripts/build-site.py --check   # o mesmo que o CI: chaves iguais nas duas línguas, nenhuma por usar, glossário
scripts/build-site.py           # gera _site/; abre _site/index.html no browser para veres
```

- **Um texto:** muda-o em `strings.json`, nas duas línguas.
- **Um texto novo:** uma chave nova em `pt` e em `en`, e o `data-i` no `index.html`. Uma chave que
  ninguém usa faz falhar o check.
- **A mascote ou a frase principal:** atualiza também `og-card.html` e volta a gerar as imagens com
  `node scripts/render-site-images.mjs` (precisa do Playwright).

Sem JavaScript, a página lê-se na mesma e o tema segue o do sistema. O script só serve para os botões
do tema e para lembrar a língua escolhida.
