# O site do Voltaria

O site para pessoas, em https://voltaria.ocarroeletrico.com: explica o que é o Voltaria e manda
instalar o ohmigo para o usar. São duas páginas, cada uma em português e em inglês: a principal (`/`, `/en/`) e a de privacidade (`/privacidade/`, `/en/privacy/`).

## Como está feito

- `index.html` e `privacy.html` são os modelos; o cabeçalho, o rodapé, o CSS e os scripts, partilhados, estão em `partials/` (`<!--include:nome-->`).
- `index.html` é o modelo da página principal. Um elemento com `data-i="chave"` recebe o texto dessa chave; uma chave entre
  chavetas duplas recebe-o escapado (para atributos e para o `<head>`). As chaves `page.*` vêm do script.
- `strings.json` tem o texto, com as mesmas chaves em `pt` e `en`. O português segue o
  `glossario.md`, como as skills.
- `static/` é copiado tal e qual:
  - a fonte (Nunito, com a licença ao lado);
  - os ícones: `favicon.ico` (16, 32 e 48 px, o que os browsers pedem e o que o Google mostra nos
    resultados), `icon.svg`, `apple-touch-icon.png` e os do `site.webmanifest` (Android);
  - as imagens das pré-visualizações de links, `og-pt.png` e `og-en.png`;
  - `404.html`, que o GitHub Pages mostra para qualquer endereço que não existe, nas duas línguas e
    fora dos motores de busca.
- `og-card.html` é o desenho das imagens de pré-visualização. Não é publicado.

O nome, a mascote e os ícones não estão nas licenças do repo: vê "O nome e a imagem ficam de fora" no
`README.md` da raiz.

`scripts/build-site.py` junta tudo em `_site/`:

- as duas páginas, com o texto já lá dentro e, para os motores de busca, a descrição, o `canonical`,
  as ligações `hreflang` entre as duas línguas, as etiquetas Open Graph e Twitter das
  pré-visualizações e os dados estruturados (schema.org `WebSite`);
- a lista de temas, tirada de `skills/`;
- `robots.txt`, que aponta para o `sitemap.xml` (as duas páginas, com a data do último commit e as
  versões em cada língua);
- `llms.txt`, o resumo para agentes, também gerado a partir das skills.

O check falha se uma página ou o manifest apontarem para um ficheiro que não está no build. O `pages.yml` corre-o e publica o resultado a cada push para `main` que
mexa no site ou nas skills.

## Mudar alguma coisa

```sh
scripts/build-site.py --check   # o mesmo que o CI: chaves iguais nas duas línguas, nenhuma por usar, glossário
scripts/build-site.py           # gera _site/; abre _site/index.html no browser para veres
```

- **Um texto:** muda-o em `strings.json`, nas duas línguas.
- **Um texto novo:** uma chave nova em `pt` e em `en`, e o `data-i` no `index.html`. Uma chave que
  ninguém usa faz falhar o check.
- **A mascote, o ícone ou a frase principal:** atualiza também `og-card.html` ou `static/icon.svg` e
  volta a gerar as imagens com `node scripts/render-site-images.mjs` (precisa do Playwright).

Sem JavaScript, a página lê-se na mesma e o tema segue o do sistema. O script só serve para os botões
do tema e para lembrar a língua escolhida.

## Aparência e acessibilidade

O botão do olho no cabeçalho abre o menu com o tema (claro, automático, escuro) e a visão (normal,
daltonismo, alto contraste). A visão põe `data-vision` no `<html>`; o CSS troca só variáveis
(`:root[data-vision="cb"]` troca o par verde/vermelho por laranja/violeta, e o significado vai também em
texto e riscado). Quem tem `prefers-contrast: more` no sistema recebe o alto contraste sem escolher.
O que se guarda no browser (`voltaria.theme`, `voltaria.vision`, `voltaria.lang`) só é lido de volta se for
um dos valores fixos, e está descrito na página de privacidade: se mudares as chaves, muda-a também.

## Cabeçalhos de segurança

O GitHub Pages não deixa mudar cabeçalhos HTTP. O build põe em cada página uma
`<meta http-equiv="Content-Security-Policy">` (só a própria origem; scripts e estilos inline por hash,
calculado no build, por isso não há `style=""` nem `on*=` no HTML) e `referrer`. Uma `<meta>` não pode
levar `frame-ancestors`, `X-Content-Type-Options`, `Permissions-Policy` nem HSTS: para esses é preciso um proxy
à frente do domínio (ex.: Cloudflare, com regras de cabeçalhos de resposta).
