# Voltaria: skills de mobilidade elétrica para o ohmigo e o ocarroeletrico.com

> **2026-11-07:** o plano previa duas ferramentas no ohmigo, `get_guide` e `get_facts`. Ficou uma
> só, hoje chamada `ev_rules_portugal` (`topic` devolve a skill; `topic` + `query` os factos). Os
> nomes antigos abaixo ficam como registo do plano.

## Contexto

O Voltaria é um conjunto de **Agent Skills** com conhecimento **atual e fiável** sobre mobilidade
elétrica em Portugal. É a fonte única de conteúdo para dois consumidores, ambos agentes:

- o **MCP do ohmigo**, que serve as skills e os factos aos assistentes (ChatGPT, Claude, ...);
- um **agente construtor** do ocarroeletrico.com, que reconstrói o site a cada release do Voltaria.
  O site vai ser reescrito de raiz (conteúdo e design); o README atual não é fonte.

As skills são sempre escritas para agentes, nunca como páginas para humanos. Cada consumidor decide
como apresentar e em que idioma.

## Decisões

### Repo

- Repo próprio, **`CarregaErvilhas/voltaria`**, com licença, pipelines, contributors e releases
  próprios. O Voltaria não sabe quem o consome.
- **Semver**: atualizar factos é patch, uma skill nova é minor, e mudar o nome de uma skill ou o
  formato dos factos é major (parte o enum de `get_guide` no ohmigo).
- Uma GitHub Action gera em cada release um **zip por skill**, para carregamento manual no
  Claude.ai / ChatGPT.

### Licença (Q11, decidida a 2026-11-04)

- **Conteúdo** (skills, `knowledge/`, `glossario.md`): **CC-BY-4.0**. Uso livre, incluindo
  comercial, com crédito obrigatório: dá visibilidade ao projeto. Cobre também o direito sui generis
  das bases de dados da UE. Não é CC-BY-SA, porque o site é obra derivada e ficaria preso ao SA.
- **Código** (scripts, testes, Actions): **MIT**.
- **Contributos: DCO, sem CLA** (`git commit -s`). Os contributos entram sob a mesma licença com que
  o conteúdo sai, e as duas licenças são irrevogáveis: o projeto nunca depende dos direitos de quem
  contribui. A única coisa que se perde é poder tirar a exigência de crédito (passar a CC0), e isso
  não se quer.
- Atribuição sugerida: "Conteúdo do Voltaria (https://github.com/CarregaErvilhas/voltaria),
  CC-BY-4.0". O ohmigo e o site têm de a mostrar junto do conteúdo servido.

### Conteúdo

- **Uma skill por tema**, `skills/<nome>/SKILL.md` (formato Agent Skills; `name` igual ao nome da
  pasta; minúsculas, números e hífens).
- v1: **`carregar-em-casa`** (wallbox, DPC, condomínio, solar, tomadas e fichas, V2X, o que
  perguntar ao utilizador) e **`incentivos`** (cita sempre fonte + data e encaminha para a página
  oficial). Mais temas a seguir, por exemplo `carregamento-publico`.
- Skills já criadas: `afir` (AFIR e legislação portuguesa), `afir-nap` (Ponto de Acesso Nacional),
  `autonomia`, `baterias`, `carregamento-publico` (o condutor na rede pública), `carregar-em-casa`,
  `empresas-e-frotas` (vantagens fiscais, carregar a frota, sub-CPE em casa do colaborador;
  acrescentada a 2026-11-06), `garantias-de-origem` (GO, leilões GO-PT, rotulagem e o carro
  elétrico; acrescentada a 2026-11-06),
  `incentivos`, `instalacao-eletrica` (o Guia Técnico da DGEG e as RTIEBT, acrescentada a
  2026-11-06), `regime-2010`, `sub-cpe` e `tecnologia-de-carregamento` (roaming e hubs, OCPP/OCPI,
  Plug & Charge e PKI, BESS; separada do `carregamento-publico` a 2026-11-06).
- **`regime-2010`**: o regime revogado (DL 39/2010, na redação do DL 90/2014), como funcionava o
  modelo CEME/OPC/EGME, o período transitório até 31-12-2027 e o que mudou com o DL 93/2025. Serve
  para referências ao modelo anterior e a factos anteriores a 19-08-2025.
- **Tudo em pt-PT**, incluindo o SKILL.md, com os termos que o público usa, mesmo quando são em
  inglês (eMSP, kilowatt em vez de quilowatt). Os agentes traduzem para o idioma do utilizador.
- **`glossario.md`** na raiz: o termo a usar, os sinónimos a evitar e uma definição curta. Um teste
  falha quando uma skill usa um sinónimo proibido.
- Os SKILL.md contêm só como fazer, sem preços nem contagens.

### Factos

- `knowledge/incentives.json` vive no Voltaria. Cada entrada tem id, texto pt + en curto,
  `source{url,name}`, `checkedAt` e `validFrom`/`validTo`; as do Fundo Ambiental têm também
  `series` e `edition`.
- **Histórico (decidido a 2026-11-04):** as entradas com `validTo` no passado não são descartadas.
  Ficam como apoios fechados, para comparar edições e responder a quem já se candidatou, e nunca se
  apresentam como abertas. `stale` marca só as entradas em vigor cujo `checkedAt` é antigo.
  O histórico do Fundo Ambiental cobre 2019 a 2025/2026, sempre a partir do aviso ou despacho
  oficial.
- Fontes dos incentivos: só oficiais (Fundo Ambiental, AT, Diário da República).
- **Apoios anunciados (decidido a 2026-11-06):** um apoio anunciado pelo Governo e ainda sem aviso
  entra com `status: "anunciado"`, só com o que está no anúncio oficial, sem `validFrom` no passado.
  Não conta como em vigor. Quando sair o aviso, a entrada é substituída por uma normal. Valores
  ditos em declarações e publicados na imprensa ficam fora dos factos; a skill pode dizer que
  existem, marcados [imprensa], mas nunca como regra.
- **Benefícios municipais (decidido a 2026-11-04):** entradas `kind: "municipal"` em
  `incentives.json`, com `municipality`, `benefit` (`isenção` ou `desconto`) e `official{url,name}`,
  a ligação da câmara. A fonte (`source`) é a lista de estacionamento da UVE, a única exceção à regra
  das fontes oficiais: nenhuma fonte oficial junta os municípios.
- Índices de terceiros (por exemplo a lista de legislação da UVE) servem para encontrar diplomas,
  nunca como fonte: cada facto aponta para o texto oficial. A lista da UVE vai até 2020 e boa parte
  foi revogada pelo DL 93/2025.
- **Factos de carros (`car`) ficam fora da v1**: não há fonte com licença aberta e o modelo já
  pesquisa bem na web.

### Fontes de terceiros (FAQ da UVE, da MOBI.E, outros guias)

- São **fontes, não texto**. Escrevemos as respostas por palavras nossas, e cada facto tem
  `source{url,name}` + `checkedAt`.
- Alimentam as **skills por tema**, não há uma skill por FAQ. A origem fica em `source`.
- Para usar texto tal e qual, é preciso autorização escrita do autor, registada no repo.
- **UVE (2026-11-04):** autorizou por escrito o uso com crédito; registo e inventário em
  `docs/fontes/uve.md`. Continuamos a reescrever, porque a autorização não cobre relicenciar o texto
  em CC-BY-4.0. Do site da UVE saíram as skills `carregamento-publico` e `baterias`, pontos novos
  em `carregar-em-casa` e `incentivos`, termos do glossário e os factos `municipal`. Cada ponto leva
  a marca `[UVE, …]`.
- **Manual da UVE (jul. 2024):** está sob CC BY 4.0, a mesma licença do Voltaria, e pode ser
  adaptado com crédito. Deu origem à skill `autonomia` e a pontos em `carregamento-publico`,
  `baterias` e no glossário. A parte dos pagamentos é anterior ao DL 93/2025 e não é usada.
- O conteúdo é redigido pelo Agente a partir das fontes, com ligação em cada facto, e
  revisto pelos CODEOWNERS num PR.
- **Cron mensal**: propõe as alterações por **PR**, e o merge é sempre manual. O `checkedAt` só
  muda quando o PR é aprovado. A mecânica fica em TODO.

### Site (repo do ocarroeletrico.com)

- O **system prompt do agente construtor vive no repo do site**.
- O agente publica por **PR**, com o site gerado guardado no repo.
- O site é multilingue (PT/EN).

### Site do Voltaria (voltaria.ocarroeletrico.com, decidido a 2026-11-07)

- Uma página para pessoas, em PT (`/`) e EN (`/en/`), que explica em termos simples o que é o
  Voltaria e manda instalar o ohmigo para o usar. O público é quem percebe pouco de tecnologia; os
  detalhes de Agent Skills e MCP ficam numa secção que se abre. Não repete o conteúdo das skills, que
  continuam escritas só para agentes. Não confundir com o ocarroeletrico.com, acima.
- Alojada no **GitHub Pages** deste repo, sem custos: `scripts/build-site.py` gera as páginas a partir
  de `site/`, e `pages.yml` publica a cada push para `main`.
- Design da família do ohmigo (escolhido entre três mockups): letra arredondada, uma mascote (um livro
  com um raio), claro e escuro. Sem analytics e sem pedidos a terceiros: a fonte é servida pelo site.
- O texto não fala em IA na escrita do conteúdo; diz que é revisto por pessoas.

### ohmigo (ohmigo.ocarroeletrico.com)

- As regras de apresentação (ordenar opções, promoções, preços de ponta, créditos, estado em tempo
  real) passam das `INSTRUCTIONS` para as **descrições das ferramentas de preço**
  (`find_cheapest_charging`, `estimate_charging_cost`). São regras de uso das ferramentas do ohmigo,
  não do Voltaria, e assim chegam sempre ao modelo.
- A extensão de skills do protocolo MCP (`2026-07-28`) fica em TODO até ser GA e estar disponível em
  mais agentes. Até lá usa-se `get_guide`.

## Trabalho

### A. ohmigo: orçamento (feito: CarregaErvilhas/ohmigo-mcp#60, por fazer merge)

As `INSTRUCTIONS` tinham 3794 caracteres no `main`; no #60 ficam com 2033, com a nota de QA incluída. O Claude Code corta as instruções e cada
descrição de ferramenta aos 2048 (`CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` altera isso), e o ChatGPT
dá mais peso aos primeiros 512.

1. `test/budget.test.js`: `INSTRUCTIONS` ≤ 2048, com o essencial nos primeiros 512 (o que o ohmigo
   cobre, idioma, CEME/OPC/DPC); cada descrição de ferramenta ≤ 2048; no máximo N ferramentas.
2. Encurtar as `INSTRUCTIONS`. Ficam as regras centrais (idioma, quem é quem, lookup_charger, o que
   perguntar antes de uma chamada de custo).
3. Mover as regras de apresentação para as descrições das ferramentas de preço.
4. Paridade em `test/i18n.test.js` para as chaves que mudarem.

### B. Voltaria: arranque (em paralelo com A)

1. Criar o repo. Feito localmente em `voltaria/` (LICENSE, LICENSE-CODE, DCO, CONTRIBUTING.md,
   README, CODEOWNERS, `scripts/check-dco.sh` e a Action `dco.yml`). Falta criar
   `CarregaErvilhas/voltaria` no GitHub e fazer push.
2. `glossario.md` e o teste dos sinónimos. Feito: `scripts/check-skills.py` (ignora URLs, `código`
   e a secção `## Fontes`).
3. `skills/carregar-em-casa/`, `skills/incentivos/` e as restantes skills (`afir`, `afir-nap`,
   `autonomia`, `baterias`, `carregamento-publico`, `regime-2010`, `sub-cpe`,
   `tecnologia-de-carregamento`, `instalacao-eletrica`, `empresas-e-frotas`), com rascunho do
   Claude e revisão por PR. A maioria já foi redigida e fundida em `main`.
4. `knowledge/incentives.json` + teste: todas as entradas têm `source.url`, `checkedAt` e texto
   pt+en; lógica de stale e de expiração. Feito: `scripts/check-knowledge.py` (falha em erros de
   estrutura e datas; avisa das entradas em vigor com `checkedAt` mais antigo que 180 dias).
5. Teste das skills: frontmatter válido (descriptions entre aspas), nome igual ao da pasta, nenhum
   valor em €/kWh. O frontmatter de 9 skills foi corrigido (2026-11-05) para evitar erro de parse
   YAML. Feito: `scripts/check-skills.py`, que corre com os outros na Action `checks.yml`.
6. Action de release: tag semver + zip por skill. Feito: `release.yml` (tag `vX.Y.Z`; cada zip leva
   `<skill>/SKILL.md` e a `LICENSE`). Ainda não testada no GitHub.

### C. ohmigo: integração (depois da Q7)

0. Atribuição CC-BY: cada guia servido por `get_guide` leva a linha de crédito do Voltaria.

1. `src/skills.js`: carregar as skills do Voltaria, calcular o manifesto sha256+tamanho a partir dos
   bytes servidos, e registar recursos `skill://<nome>/SKILL.md`.
2. `get_guide({ topic, lang })`: topic é o enum dos nomes das skills; devolve o corpo do SKILL.md;
   `readOnlyHint`.
3. `src/knowledge.js` + `get_facts({ topic, query, lang })` (reutilizar o padrão `isStale` de
   `src/offers.js`).
4. Nas `INSTRUCTIONS`, uma linha por guia: "para X, chama primeiro get_guide('…')".
5. `test/http.test.js`: `get_guide`, `get_facts` e `resources/read skill://…` contra o servidor
   lançado.
6. Docs: `docs/07-guides-and-facts.md`, `docs/01-how-it-works.md`, README e CLAUDE.md.

Verificação: no Claude Code (limite de 2048) e no ChatGPT, perguntar em português sobre uma wallbox
em casa e sobre um incentivo, e confirmar que o assistente chama get_guide/get_facts e cita a fonte e
a data.

## TODO (por discutir)

- **Q7. Como o ohmigo recebe o Voltaria**: git submodule, busca de uma tag fixa no build, ou uma
  Action que abre um PR no ohmigo com a cópia. Ronda 2 do planeamento.
- **Histórico 2017 e 2018**: os despachos n.º 1612-B/2017 e n.º 1607/2018 só foram encontrados em
  cópias da UVE. Falta a ligação oficial no Diário da República para os acrescentar.
- **Q18. Mecânica do cron mensal**: só scripts que comparam hashes das páginas, Claude a redigir a
  proposta, ou os dois em sequência.
