---
name: garantias-de-origem
description: "Explica as garantias de origem (GO) da eletricidade em Portugal: o que provam e o que não provam, quem as emite (EEGO/REN), a validade, a rotulagem na fatura, os leilões GO-PT da DGEG com as GO da produção apoiada (como funcionam, quanto custam, para onde vai a receita) e o efeito nas tarifas. Liga isto ao carro elétrico: o que vale um carregamento ou uma tarifa \"100 % renovável\", as GO do autoconsumo, as frotas que reportam emissões, e os títulos de CO2 do DL 93/2025, que ainda não existem. Usa quando o utilizador pergunta o que é uma garantia de origem, se a eletricidade verde é mesmo verde, se compensa pagar mais por ela, como funcionam os leilões ou se o painel solar dá direito a garantias."
---

# Garantias de origem

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- **Os preços e os resultados dos leilões vêm dos factos** (no ohmigo: `get_facts` com `topic:
  "incentivos"`, entradas `kind: "mercado"`), com a data e a fonte. Não dês preços de GO de memória:
  variaram mais de quarenta vezes entre 2022 e 2025.
- **A ENSE tem uma página de 2019 sobre garantias de origem que está desatualizada**: cita o DL
  141/2010 e o DL 23/2010 como base. Desde 2022 a base é o DL 84/2022 (arts. 28.º a 33.º) e o DL
  15/2022 (arts. 174.º a 179.º e 294.º). Não a uses como fonte das regras.
- **Uma GO prova uma compra, não um fluxo físico.** Não digas que o carro "carregou com energia
  solar" por causa de uma GO. Diz que o comercializador ou o OPC cancelou GO renováveis em quantidade
  igual ao consumo, no período que a GO cobre.
- **Os títulos de CO2 do art. 5.º do DL 93/2025 ainda não existem.** Estão na lei, mas a portaria
  que os cria não foi publicada (não está na lista da DGEG, verificada a 2026-11-06). Não os
  confundas com as GO, e não digas a ninguém que já pode vendê-los.
- Não dês aconselhamento de investimento. Explicar o mercado e os números publicados é diferente de
  dizer a alguém para comprar ou vender GO.

## O que é uma garantia de origem

- Um documento eletrónico que prova ao cliente final que 1 MWh foi produzido a partir de fontes
  renováveis (DL 84/2022, art. 29.º, n.º 1). Cada MWh só pode ter uma GO (n.º 2). Também há GO de
  cogeração de elevada eficiência, de gases de origem renovável e de gases de baixo teor de carbono
  (arts. 30.º a 32.º).
- Serve para o comercializador provar a quota de renovável no seu cabaz; **não conta para as metas
  nacionais de renováveis** (art. 28.º, n.º 2).
- Pode ser vendida separada da energia que a originou (art. 28.º, n.º 3). Nesse caso, essa energia
  já não pode ser contada como renovável no cabaz de quem a vende (n.º 4). É isto que evita a dupla
  contagem.
- **Validade**: 12 meses depois da produção do MWh, e tem de ser cancelada até 6 meses depois do fim
  da validade (art. 29.º, n.º 5). Depois de usada para provar a origem, é cancelada (n.º 6).
- Cada GO diz: tipo, fonte, datas de início e fim da produção, instalação (identificação, local,
  tipo, capacidade), se teve apoio ao investimento ou outro apoio, data de entrada em serviço, país e
  entidade emissora, e um número único (art. 29.º, n.º 4).
- As GO emitidas noutros Estados-Membros são reconhecidas em Portugal, salvo suspeita fundada (art.
  29.º, n.º 7). A REN está ligada à AIB (a associação europeia das entidades emissoras), o que permite
  importar e exportar GO.

### Quem faz o quê

| Quem | Papel | Base |
|---|---|---|
| EEGO (REN, no continente; EDA nos Açores, EEM na Madeira) | Regista produtores, emite, transfere e cancela as GO, audita as instalações | DL 15/2022, arts. 176.º e 294.º |
| ERSE | Regula a EEGO, aprova o manual de procedimentos e o orçamento, fixa os preços dos serviços da EEGO, define a rotulagem | DL 15/2022, arts. 174.º, n.º 4, 178.º e 179.º; DL 84/2022, art. 28.º, n.º 11 |
| DGEG | Recebe as GO da produção apoiada e vende-as em leilão | DL 84/2022, art. 28.º, n.os 9 e 10 |
| OMIP | Opera os leilões GO-PT e gere as garantias financeiras dos participantes | Despacho n.º 6560-B/2021 |
| SU Eletricidade (CUR) | Fatura e liquida as receitas dos leilões | Despacho n.º 6560-B/2021, n.º 13 |
| ENSE | Fiscaliza a EEGO | DL 84/2022, art. 33.º, n.º 5 |

- A REN é EEGO a título transitório: a lei prevê um concurso para a licença de EEGO, com um máximo
  de 10 anos (DL 15/2022, arts. 175.º e 294.º). Ainda não houve concurso; se o utilizador perguntar,
  diz isto e não inventes datas.
- O manual de procedimentos tem de cumprir a norma EN 16325 (DL 15/2022, art. 174.º, n.º 4, na
  redação do DL 130/2026).
- Para se registar e pedir GO: portal da EEGO, na REN.

## Os leilões GO-PT

### De onde vêm as GO

- Um produtor com tarifa garantida, outro apoio direto ao preço, incentivo ao investimento, CAE ou
  acordo de cessação de CAE **tem de entregar as GO à DGEG**. Sem essa entrega não recebe a
  remuneração (DL 84/2022, art. 28.º, n.º 9).
- Os produtores com regime remuneratório bonificado não podem vender as GO à parte (n.º 5). A
  exceção são os vencedores dos leilões de capacidade de injeção, quando o regime deles constitui um
  ganho para o SEN, o que é verificado periodicamente (n.os 6 a 8).
- Ou seja: as GO da eólica, da hídrica, da solar e da térmica renovável que os consumidores já pagam
  através das tarifas são do Sistema Elétrico Nacional, e é a DGEG que as vende.

### Como funcionam

- Leilão eletrónico na plataforma do OMIP, com periodicidade mensal, trimestral ou semestral
  (Despacho n.º 6560-B/2021, n.º 1). Desde 2026 são seis por ano, e em 2027 são cinco. O calendário
  está nos factos.
- A DGEG publica a convocatória pelo menos 20 dias antes, com a data, as quantidades por tecnologia
  e período de produção (os "lotes"), o preço de reserva, os custos de participação e eventuais
  restrições (n.os 4 e 5).
- Só entram pessoas coletivas registadas na EEGO, admitidas como participantes no OMIP e
  qualificadas com garantia financeira até dois dias úteis antes do leilão (regras do OMIP). Um
  particular não compra GO no leilão.
- O resultado sai por lote, com um preço marginal. A EEGO transfere as GO para a conta de quem
  ganhou (Despacho, n.º 14), e o OMIP publica o histórico dos resultados.
- O OMIP e o CUR recebem uma retribuição por MWh adjudicado, com um teto em percentagem da receita
  (Despacho, n.os 11 e 12). O valor está nos factos.

### Para onde vai a receita, e o efeito nas tarifas

- O resultado líquido é **deduzido aos sobrecustos com a aquisição de eletricidade renovável com
  remuneração garantida**, nos termos do Regulamento Tarifário da ERSE (DL 84/2022, art. 28.º, n.º
  10; Despacho, n.º 13). Esses sobrecustos entram nas tarifas de acesso às redes que todos pagam, por
  isso a receita dos leilões baixa, um pouco, a fatura de todos os consumidores.
- A receita depende do preço europeu das GO, não da quantidade, que anda estável por leilão. Foi
  máxima em 2023 e caiu muito em 2024 e 2025, quando o preço das GO caiu na Europa. Os totais por ano
  estão nos factos, e são uma conta do Voltaria sobre o histórico do OMIP (volume vendido × preço
  marginal de cada lote): diz isso ao citá-los.
- Não digas quanto baixa a fatura de uma casa: não há números oficiais publicados por cliente.

## Na fatura: a rotulagem

- O comercializador tem de dizer, na fatura ou na documentação que a acompanha, a contribuição de
  cada fonte para a energia fornecida e as emissões de CO2 associadas (DL 15/2022, art. 136.º, n.º 3,
  e Anexo VII, n.º 3).
- As regras estão na Diretiva n.º 16/2018 da ERSE: o mix trimestral, o dos últimos quatro
  trimestres e o do ano anterior, e as emissões específicas do ano anterior e de cada fatura. A ERSE
  publica o "mix base do sistema", que é o que mostra um comercializador que não prova nada com GO,
  e tem um simulador de rotulagem.
- **Uma oferta "100 % renovável" só o é na rotulagem se o comercializador tiver cancelado GO (ou
  usado contratos bilaterais físicos) para todo esse consumo.** Para verificar, o utilizador vê o
  rótulo da oferta e o mix do comercializador no site da ERSE e na fatura.

## E o carro elétrico?

### "Carregar com 100 % renovável"

- Num posto público, o OPC compra a eletricidade a um comercializador (DL 93/2025, art. 9.º). Se o
  OPC anunciar energia 100 % renovável, isso só pode assentar em GO canceladas por ele ou pelo
  comercializador dele, ou em autoconsumo no local (art. 15.º, f)). Se o utilizador perguntar,
  diz-lhe para pedir ao OPC de onde vêm as GO e de que período são.
- Em casa, a energia do carro é a do contrato da casa (ou do sub-CPE): o rótulo é o do comercializador
  desse contrato.
- **Quanto vale, em dinheiro**: o preço de uma GO, em `€/MWh`, dividido por 10 dá o custo em
  cêntimos por kWh. Com os preços dos factos, cobrir com GO os kWh que um carro carrega num ano custa
  muito pouco. Faz a conta com os kWh do utilizador e o preço do último leilão, e diz que é o preço
  grossista em Portugal: uma tarifa "verde" pode custar mais do que isso, porque o comercializador
  junta a sua margem.

### O que uma GO não prova

- **Que a central é nova.** Uma GO de uma barragem com décadas vale o mesmo que uma de um parque
  solar novo. Comprar GO não financia, por si, nova produção renovável. Se o utilizador quiser
  adicionalidade, a resposta é um contrato com uma central nova (PPA) ou o autoconsumo.
- **Que a hora bate certo.** A GO cobre um período de produção (um mês, por exemplo), não a hora em
  que o carro carregou. Carregar às 3 da manhã com uma GO solar é legal, mas não quer dizer que o sol
  estava a produzir.
- Diz isto sem desvalorizar: as GO são o único instrumento legal para provar a origem na fatura, e
  evitam que a mesma energia renovável seja vendida duas vezes como verde.

### Autoconsumo: painéis em casa

- O autoconsumidor pode pedir GO da eletricidade excedente que injeta na rede (DL 15/2022, art.
  88.º, n.º 1, h)). A energia que consome em casa, incluindo a que vai para o carro, não precisa de
  GO: já é dele.
- Antes de dizer a alguém que vale a pena, compara os preços dos serviços da EEGO (fixados pela
  ERSE) e o custo de registo com o que rendem as GO dos MWh excedentes ao preço dos factos. Para uma
  casa, com poucos MWh por ano, raramente compensa.

### Frotas e relatórios de emissões

- Uma empresa que reporta emissões do consumo de eletricidade pelo método baseado no mercado usa as
  GO canceladas em seu nome para baixar o fator de emissão desse consumo. Num relatório de
  sustentabilidade, isto inclui a eletricidade dos carros da frota que é faturada à empresa.
- Para o resto das empresas e frotas (fiscalidade, carregamento em casa do colaborador), usa
  `empresas-e-frotas`.

### Títulos de CO2 da mobilidade elétrica (ainda não existem)

- O DL 93/2025, art. 5.º, prevê que as emissões de CO2 evitadas com eletricidade renovável na
  mobilidade elétrica possam ser valorizadas: utilizadores e operadores beneficiariam de títulos
  transacionáveis que contam para as metas de incorporação de renováveis nos combustíveis e
  transportes.
- A portaria que os cria ainda não saiu. Até sair, não há quem os emita, nem preço, nem forma de os
  pedir. Não são GO: uma GO prova a origem da eletricidade, e estes títulos serviriam para as metas
  dos transportes.

## Como responder

1. Diz o que a GO prova (a origem de 1 MWh, num período) e o que não prova (o fluxo físico, a hora,
   a adicionalidade).
2. Se a pergunta for sobre preços ou leilões, usa os factos `kind: "mercado"`, com a data do leilão
   e a fonte (OMIP, DGEG).
3. Se for sobre uma oferta ou um posto "verde", manda ver a rotulagem na fatura e no site da ERSE.
4. Termina com a fonte e, para os números, com a data do leilão.

## Fontes

### Legislação

- Decreto-Lei n.º 84/2022, de 9 de dezembro (metas de renováveis; arts. 28.º a 33.º, garantias de
  origem), texto consolidado:
  https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2022-204553396
- Decreto-Lei n.º 15/2022, de 14 de janeiro (Sistema Elétrico Nacional; arts. 88.º, 136.º, 174.º a
  179.º, 294.º e Anexo VII), texto consolidado:
  https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-lei/2022-177634029
- Despacho n.º 6560-B/2021, de 5 de julho (DGEG; regras dos leilões de GO do SEN):
  https://diariodarepublica.pt/dr/detalhe/despacho/6560-b-2021-166488536
- Decreto-Lei n.º 93/2025, de 14 de agosto (mobilidade elétrica; arts. 5.º, 9.º e 15.º):
  https://data.dre.pt/eli/dec-lei/93/2025/08/14/p/dre/pt/html
- Diretiva (UE) 2018/2001 (RED II; art. 19.º, garantias de origem):
  https://eur-lex.europa.eu/eli/dir/2018/2001/oj

### Normas e standards

- EN 16325:2025 (garantias de origem relativas à energia): https://genorma.com/en/standards/en-16325-2025

### Outras fontes

Verificadas a 2026-11-06:

- OMIP, Leilões de Garantias de Origem (regras, convocatórias, histórico dos resultados,
  calendários): https://www.omip.pt/pt/leiloes-go
- ERSE, Garantias de origem: https://www.erse.pt/eletricidade/garantias-de-origem-e-rotulagem/garantias-de-origem/
- ERSE, Rotulagem: https://www.erse.pt/eletricidade/garantias-de-origem-e-rotulagem/rotulagem/
- REN, Emissão de Garantias de Origem em Portugal: https://www.ren.pt/pt-pt/atividade/garantias-de-origem
- DGEG, Mobilidade elétrica, legislação aplicável e despachos (para ver se já saiu a portaria do
  art. 5.º do DL 93/2025):
  https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/legislacao-aplicavel-e-despachos-dgeg/
- ENSE, "Garantias de Origem" (25-06-2019), desatualizada, só para contexto histórico:
  https://www.ense-epe.pt/news/garantias-de-origem/
