# UVE como fonte

A UVE – Associação de Utilizadores de Veículos Elétricos (https://www.uve.pt/) autorizou por escrito o
uso do conteúdo do seu site no Voltaria, com indicação da fonte.

## Autorização

- Recebida por: Fernando Pereira.
- Registada no repo a: 2026-11-04.

## Como a usamos

- **Escrevemos por palavras nossas, não copiamos texto.** A autorização é para usar o conteúdo com
  crédito. Não diz que a UVE aceita que o seu texto saia sob CC-BY-4.0, e é isso que aconteceria se o
  copiássemos para o Voltaria: qualquer pessoa o poderia redistribuir e alterar. Os factos, as regras
  e as listas não têm esse problema quando escritos por nós.
- As skills são para agentes e organizadas por tema. As páginas da UVE são para pessoas e
  organizadas por artigo. Reescrever é também adaptar.
- Cada ponto que vem da UVE leva a marca `[UVE, …]` na skill e a ligação na secção Fontes, com a
  data de verificação. Nos factos, a UVE aparece em `source`.
- A autorização cobre o conteúdo da UVE, não o de terceiros que a UVE republica (por exemplo, artigos
  da VOLT/Exame Informática). Desses só usamos factos gerais, citando o autor original.
- A regra das fontes oficiais para os incentivos mantém-se. A exceção são os benefícios municipais de
  estacionamento: a fonte é a lista da UVE, com a ligação da câmara em `official`.

**Crédito a mostrar** quando um consumidor do Voltaria usar estes pontos: "Fonte: UVE – Associação de
Utilizadores de Veículos Elétricos (uve.pt)", junto da linha de crédito do Voltaria.

## O manual da UVE (CC BY 4.0)

O manual "Parabéns! Comprou um veículo elétrico e agora?" (36 páginas, jul. 2024,
https://www.uve.pt/page/wp-content/uploads/2025/01/2024_manual_me-UVE.pdf) tem uma licença própria,
diferente do resto do site: **Creative Commons Attribution 4.0 International** (pág. 4: "autorizam-se
cópias e a redistribuição deste documento, bem como adaptações desde que o devido crédito seja
atribuído e quaisquer alterações sejam indicadas").

- É a mesma licença do conteúdo do Voltaria, por isso podemos adaptar o texto do manual sem depender
  da autorização acima. Mesmo assim reescrevemos, porque as skills são para agentes e organizadas por
  tema.
- Crédito e alterações: cada ponto leva `[UVE, manual]`, e a secção Fontes da skill diz a licença e
  que o texto foi adaptado.
- Ligamos ao PDF no site da UVE e não o copiamos para o repo: tem 4,9 MB e logótipos (UVE, EDP)
  que a licença não cobre.
- O manual tem o logótipo da EDP e dá destaque à EDP Charge e ao cartão de associado UVE/EDP Charge.
  As skills não herdam essa preferência: as apps aparecem como exemplos, ao lado de outras.
- A skill `autonomia` pode recomendá-lo a quem acabou de comprar um carro, avisando que a parte dos
  pagamentos está ultrapassada.

| Secção do manual | Para onde foi |
|---|---|
| As unidades; capacidade vs tempo; autonomia | `autonomia`: as contas; `carregamento-publico`: as contas; `glossario.md`: autonomia, consumo |
| Tipos de postos; fichas | `carregamento-publico`: PCUR, usar a ficha DC num posto rápido; `glossario.md`: posto ultrarrápido |
| Quanto custa | `carregamento-publico`: taxa de ativação do OPC |
| Quanto tempo demora; curva de carga | `carregamento-publico`: bateria muito baixa, 20 % a 80 %, temperatura, não ir a 100 % em viagem |
| Que postos devo utilizar | `carregamento-publico`: que posto usar |
| Autonomia (WLTP); condução eficiente | `autonomia`: quase tudo; `glossario.md`: WLTP, travagem regenerativa |
| As aplicações móveis | `carregamento-publico`: apps que comparam preço e planeiam; `autonomia`: viagens |
| A bateria | `baterias`: mínimo de 20 a 25 %, garantia comum, temperaturas extremas |

Lido e não usado:

- **Desatualizado:** a parte dos pagamentos é anterior ao DL 93/2025 (diz que é preciso um contrato
  com um CEME e descreve só o modelo antigo); o número de postos é do início de 2022; o exemplo do
  Renault Zoe a 43 kW em AC e "CHAdeMO para marcas japonesas" já não ajudam quem compra hoje.
- **Números sem fonte nem método:** 20 % da energia vem da travagem regenerativa, 95 % de
  reciclagem do lítio, 2000 vs 20 peças móveis, 15 a 20 minutos de rápido para 100 km, baterias de
  15 anos. As skills não os usam.
- **Carregar em casa:** já coberto em `carregar-em-casa` com fontes mais recentes. A frase de que uma
  wallbox DPC dispensa aumentar a potência contratada depende da instalação e do regime dos CEME,
  que acaba a 31-12-2027: não entrou.
- **Manutenção e associação:** promoção do carro elétrico e da UVE, não informação para o condutor.

## O que veio da UVE

Verificado a 2026-11-04.

| Página da UVE | Para onde foi |
|---|---|
| [Como instalar um PCVE em casa ou no condomínio](https://www.uve.pt/page/como-instalar-pcve-casa-ou-condominio/) (7-11-2025) | `carregar-em-casa`: guia técnico da DGEG, quando não é preciso falar com o condomínio, permilagem, dicas antes de enviar, minuta, apoio jurídico |
| [Tomada vs Wallbox](https://www.uve.pt/page/tomada-vs-wallbox/) (10-11-2023) | `carregar-em-casa`: carregador ocasional, carregador de bordo, reforço do ramal, wallbox integrada na MOBI.E |
| [Como carregar um veículo elétrico](https://www.uve.pt/page/como-carregar-um-veiculo-eletrico/) | `carregamento-publico`: tipos de posto, fichas, o que define o tempo; `baterias`: carregamentos rápidos |
| [O Novo Regime Jurídico da Mobilidade Elétrica](https://www.uve.pt/page/blueauto-11_12-2025/) (Blueauto n.º 97) | `carregamento-publico`: como pagar no modelo antigo, no novo e ad hoc; `glossario.md`: TAR |
| [Análise UVE ao novo RJME](https://www.uve.pt/page/analise-uve-nrjme-08-2025/) (26-8-2025) | `carregamento-publico`: cativação, subscrições |
| [Carregar com Respeito](https://www.uve.pt/page/blueauto-07-2026/) (Blueauto n.º 104) | `carregamento-publico`: boas práticas, Tesla sem prioridade, potência a cair perto dos 80 % |
| [Avisos de Cortesia](https://www.uve.pt/page/avisos-de-cortesia-para-utilizadores-de-ve-nova-versao-2018/) | `carregamento-publico`: multa e reboque por ocupar o lugar |
| [Pesquisa de Pontos de Carga](https://www.uve.pt/page/pontos-de-carga/) | `carregamento-publico`: mapas e apps |
| [Alteração do Call-Center da Mobi.E para os OPC](https://www.uve.pt/page/alteracao-do-call-center-da-mobi-e-para-os-opc/) (2020) | `carregamento-publico`: o apoio é do OPC |
| [Furto e vandalismo em PCVE](https://www.uve.pt/page/analise-uve-furto-e-vandalismo-em-pvce_outubro-2025/) (out. 2025) | `carregamento-publico`: avisar o OPC |
| [Carregamento na Europa](https://www.uve.pt/page/carregamento-na-europa/) | `carregamento-publico`: no estrangeiro |
| [Comparativo 100 km](https://www.uve.pt/page/quanto-custa-100-km/) e [Observatório](https://observatorio.uve.pt/) | `carregamento-publico`: encaminhar, sem valores |
| [A química das baterias (LFP ou NMC)](https://www.uve.pt/page/blueauto-08-2026/) (Blueauto n.º 105) | `baterias`: quase tudo; `carregamento-publico`: curva de carregamento |
| [A Vida das Baterias](https://www.uve.pt/page/vida-das-baterias-veiculo-eletrico/) | `baterias`: 80 % e 10 %, rápidos, segunda vida |
| [Veículos elétricos parados](https://www.uve.pt/page/veiculos-eletricos-parados-como-tratar-bem-da-bateria/) (é da VOLT) | `baterias`: carro parado, citando a VOLT |
| [Municípios com isenção/desconto no estacionamento](https://www.uve.pt/page/municipios-com-isencao-desconto-no-pagamento-de-estacionamento-para-veiculos-eletricos/) (2-11-2026) | `knowledge/incentives.json`: 12 entradas `municipal`; `incentivos` |
| [Dístico Identificativo de VE do IMT](https://www.uve.pt/page/distico-identificativo-ve-imt/) | `incentivos`: dístico (a fonte do facto é a Lei n.º 19/2024) |
| [Vantagens de um VE](https://www.uve.pt/page/vantagens-ve/) | `incentivos`: zonas de acesso condicionado |
| [Que tipo de Veículos Elétricos existem?](https://www.uve.pt/page/tipo-de-veiculos-eletricos/) | `glossario.md`: 100 % elétrico, híbrido plug-in, extensor de autonomia |

## Lido e não usado

- **Desatualizado:** "Como carregar" diz que os Superchargers são só para Tesla, que há 7 em Portugal
  e que os cartões de CEME são gratuitos; "Carregamento na Europa" tem a lista de países da IONITY de
  há vários anos; "Carregamento em Portugal" são notícias de 2020. Usámos só o que ainda é verdade.
- **Listas de postos** (rápidos, Tesla, Porsche, concessionados): mudam todas as semanas e o NAP, via
  ohmigo, já as cobre.
- **Números e estatísticas** (vendas mensais, rede de carregamento mensal, custo por 100 km): as
  skills não levam contagens nem preços. Encaminhamos para o Observatório.
- **"Elétrico vs Combustão"**: tradução de um vídeo de terceiros, com valores de manutenção e emissões
  sem data nem método. Não usado.
- **Opinião e propostas** (Carta Elétrica, propostas ao RJME, constrangimentos na instalação,
  transporte pesado, importados usados): posições da UVE, não informação para o condutor.
- **Associação** (órgãos sociais, relatórios e contas, eventos, protocolos e descontos para
  associados): não é para o Voltaria. Só mencionamos que a UVE dá apoio jurídico aos associados nos
  conflitos com o condomínio.
- **Legislação**: a lista da UVE é um índice (ver o plano); cada facto aponta para o texto oficial.
- **Incentivos 2017 e 2018**: a UVE tem cópias dos despachos, mas a regra dos incentivos pede a
  ligação oficial. Continua no TODO do plano.

## Por confirmar antes de entrar

- **ISV**: a UVE diz que os 100 % elétricos não pagam ISV. Falta confirmar no Código do ISV, no
  Portal das Finanças, para entrar em `incentives.json` como `fiscal`.

Resolvido a 2026-11-04: a frase da UVE sobre **construções novas desde julho de 2010** não entrou
como está. O DL 39/2010 (arts. 28.º e 52.º) pedia uma infraestrutura elétrica preparada para um posto
ou uma tomada em cada lugar, não uma ligação entre o lugar e a fração. Hoje vale o DL 93/2025, art.
22.º, que já não tem a regra de cada lugar. `carregar-em-casa` cita o art. 22.º e remete para
`regime-2010`.
