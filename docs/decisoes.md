# Voltaria: decisões

O que está decidido e porquê. O trabalho em aberto está em [plano.md](plano.md).

## Contexto

O Voltaria é um conjunto de **Agent Skills** com conhecimento **atual e fiável** sobre mobilidade elétrica em Portugal. É a fonte única de conteúdo para dois consumidores, ambos agentes:

- o **MCP do ohmigo**, que serve as skills e os factos aos assistentes (ChatGPT, Claude, ...);
- um **agente construtor** do ocarroeletrico.com, que reconstrói o site a cada release do Voltaria.

As skills são sempre escritas para agentes, nunca como páginas para humanos. Cada consumidor decide como apresentar e em que idioma.

## Decisões

### Repo

- Repo próprio, **`CarregaErvilhas/voltaria`**, com licença, pipelines, contributors e releases próprios. O Voltaria não sabe quem o consome.
- **Semver**: atualizar factos é patch, uma skill nova é minor, e mudar o nome de uma skill ou o formato dos factos é major (os nomes das skills são os `topic` de `ev_rules_portugal` no ohmigo).
- Uma GitHub Action gera em cada release um **zip por skill**, para carregamento manual no Claude.ai / ChatGPT.

### Licença

- **Conteúdo** (skills, `knowledge/`, `glossario.md`): **CC-BY-4.0**. Uso livre, incluindo comercial, com crédito obrigatório: dá visibilidade ao projeto. Cobre também o direito sui generis das bases de dados da UE. Não é CC-BY-SA, porque o site é obra derivada e ficaria preso ao SA.
- **Código** (scripts, testes, Actions): **MIT**.
- **Contributos: DCO, sem CLA** (`git commit -s`). Os contributos entram sob a mesma licença com que o conteúdo sai, e as duas licenças são irrevogáveis: o projeto nunca depende dos direitos de quem contribui. A única coisa que se perde é poder tirar a exigência de crédito (passar a CC0), e isso não se quer.
- Atribuição sugerida: "Conteúdo do Voltaria (https://github.com/CarregaErvilhas/voltaria), CC-BY-4.0". O ohmigo e o site têm de a mostrar junto do conteúdo servido.
- **Nome e imagem:** ficam fora das licenças, como no ohmigo. O nome Voltaria, a mascote, o ícone e as imagens feitas com eles não estão licenciados; um fork precisa de nome e imagem próprios. Usar o nome no crédito é o que a atribuição pede.

### Conteúdo

- **Uma skill por tema**, `skills/<nome>/SKILL.md` (formato Agent Skills; `name` igual ao nome da pasta; minúsculas, números e hífens).
- **`incentivos`** cita sempre a fonte e a data e encaminha para a página oficial.
- **`regime-2010`**: o regime revogado (DL 39/2010, na redação do DL 90/2014), como funcionava o modelo CEME/OPC/EGME, o período transitório até 31-12-2027 e o que mudou com o DL 93/2025. Serve para referências ao modelo anterior e a factos anteriores a 19-08-2025.
- **Tudo em pt-PT**, incluindo o SKILL.md, com os termos que o público usa, mesmo quando são em inglês (eMSP, kilowatt em vez de quilowatt). Os agentes traduzem para o idioma do utilizador.
- **`glossario.md`** na raiz: o termo a usar, os sinónimos a evitar e uma definição curta. Um teste falha quando uma skill usa um sinónimo proibido.
- Os SKILL.md contêm só como fazer, sem preços nem contagens.

### Factos

- `knowledge/incentives.json` vive no Voltaria. Cada entrada tem id, texto pt + en curto, `source{url,name}`, `checkedAt` e `validFrom`/`validTo`; as do Fundo Ambiental têm também `series` e `edition`.
- **Histórico:** as entradas com `validTo` no passado não são descartadas. Ficam como apoios fechados, para comparar edições e responder a quem já se candidatou, e nunca se apresentam como abertas. `stale` marca só as entradas em vigor cujo `checkedAt` é antigo. O histórico do Fundo Ambiental vem sempre do aviso ou despacho oficial.
- Fontes dos incentivos: só oficiais (Fundo Ambiental, AT, Diário da República).
- **Apoios anunciados:** um apoio anunciado pelo Governo e ainda sem aviso entra com `status: "anunciado"`, só com o que está no anúncio oficial, sem `validFrom` no passado. Não conta como em vigor. Quando sair o aviso, a entrada é substituída por uma normal. Valores ditos em declarações e publicados na imprensa ficam fora dos factos; a skill pode dizer que existem, marcados [imprensa], mas nunca como regra.
- **Benefícios municipais:** entradas `kind: "municipal"` em `incentives.json`, com `municipality`, `benefit` (`isenção` ou `desconto`) e `official{url,name}`, a ligação da câmara. A fonte (`source`) é a lista de estacionamento da UVE, a única exceção à regra das fontes oficiais: nenhuma fonte oficial junta os municípios.
- Índices de terceiros (por exemplo a lista de legislação da UVE) servem para encontrar diplomas, nunca como fonte: cada facto aponta para o texto oficial. A lista da UVE vai até 2020 e boa parte foi revogada pelo DL 93/2025.
- **Factos de carros (`car`) ficam fora da v1**: não há fonte com licença aberta e o modelo já pesquisa bem na web.

### Fontes de terceiros (FAQ da UVE, da MOBI.E, outros guias)

- São **fontes, não texto**. Escrevemos as respostas por palavras nossas, e cada facto tem `source{url,name}` + `checkedAt`.
- Alimentam as **skills por tema**, não há uma skill por FAQ. A origem fica em `source`.
- Para usar texto tal e qual, é preciso autorização escrita do autor, registada no repo.
- **UVE:** autorizou por escrito o uso com crédito; registo e inventário em `docs/fontes/uve.md`. Continuamos a reescrever, porque a autorização não cobre relicenciar o texto em CC-BY-4.0. Cada ponto leva a marca `[UVE, …]`.
- **Manual da UVE (jul. 2024):** está sob CC BY 4.0, a mesma licença do Voltaria, e pode ser adaptado com crédito. A parte dos pagamentos é anterior ao DL 93/2025 e não é usada.
- O conteúdo é redigido pelo Agente a partir das fontes, com ligação em cada facto, e revisto pelos CODEOWNERS num PR.
- **Cron mensal**: propõe as alterações por **PR**, e o merge é sempre manual. O `checkedAt` só muda quando o PR é aprovado. A mecânica está por decidir ([plano.md](plano.md)).

### Site (repo do ocarroeletrico.com)

- O **system prompt do agente construtor vive no repo do site**.
- O agente publica por **PR**, com o site gerado guardado no repo.
- O site é multilingue (PT/EN).

### Site do Voltaria (voltaria.ocarroeletrico.com)

- Uma página para pessoas, em PT (`/`) e EN (`/en/`), que explica em termos simples o que é o Voltaria e manda instalar o ohmigo para o usar. O público é quem percebe pouco de tecnologia; os detalhes de Agent Skills e MCP ficam numa secção que se abre. Não repete o conteúdo das skills, que continuam escritas só para agentes. Não confundir com o ocarroeletrico.com, acima.
- Alojada no **GitHub Pages** deste repo, sem custos: `scripts/build-site.py` gera as páginas a partir de `site/`, e `pages.yml` publica a cada push para `main`.
- Design da família do ohmigo (escolhido entre três mockups): letra arredondada, uma mascote (um livro com um raio), claro e escuro. Sem analytics e sem pedidos a terceiros: a fonte é servida pelo site.
- O texto não fala em IA na escrita do conteúdo; diz que é revisto por pessoas.

### ohmigo (ohmigo.ocarroeletrico.com)

- As regras de apresentação (ordenar opções, promoções, preços de ponta, créditos, estado em tempo real) passam das `INSTRUCTIONS` para as **descrições das ferramentas de preço** (`find_cheapest_charging`, `estimate_charging_cost`). São regras de uso das ferramentas do ohmigo, não do Voltaria, e assim chegam sempre ao modelo.
- O ohmigo recebe o Voltaria por **git submodule**: a versão que serve fica fixada no repo dele e muda por PR.
- Os temas chegam por uma só ferramenta, **`ev_rules_portugal`** (`topic` devolve a skill; `topic` + `query` os factos). As mesmas skills são servidas pela extensão de skills do MCP, a quem a suporta.
