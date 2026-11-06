---
name: carregamento-publico
description: "Ajuda um condutor a carregar o carro elétrico na rede pública em Portugal e em viagem pela Europa, com cartão, app ou pagamento ad hoc, na MOBI.E ou fora dela. Usa quando o utilizador pergunta como carregar fora de casa, como pagar, quanto tempo demora, o que fazer quando um posto não funciona, como se comportar numa fila ou como carregar no estrangeiro."
---

# Carregamento público

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- Não dês preços nem tempos de carregamento de memória. Para o preço, usa a ferramenta de preços se
  a tiveres (no ohmigo: `find_cheapest_charging` e `estimate_charging_cost`). Para o tempo, procura
  as especificações da versão exata do carro (potência máxima em AC e DC, curva de carregamento).
- Não prometas que um posto está livre ou a funcionar. Se tiveres estado em tempo real, diz de quando
  é.
- O regime está em transição. Até 31-12-2027 coexistem o modelo antigo, com CEME e a MOBI.E, e o
  novo, do DL 93/2025, com contrato direto com o OPC ou com um eMSP (DL 155/2026). Diz em que modelo
  está o posto de que falas.

## O que perguntar primeiro

Pergunta só o que não souberes, uma coisa de cada vez:

1. **Onde vai carregar**: na cidade, numa viagem (de onde para onde), ou no estrangeiro.
2. **Que carro?** Procura tu as fichas e as potências da versão exata. Não peças ao utilizador.
3. **Como paga hoje**: cartão ou app de um CEME, app de um OPC ou de um eMSP, ou nenhum (ad hoc).
4. **Tem pressa?** O posto mais barato é muitas vezes um posto normal lento.

## Tipos de posto

- **Posto normal**: até 22 kW, em corrente alterna (AC), quase sempre com tomada Tipo 2. Em muitos
  é preciso levar o cabo. A velocidade fica limitada pelo carregador de bordo do carro
  [UVE, formas de carregamento].
- **Posto rápido**: acima de 22 kW, em corrente contínua (DC), com o cabo preso ao posto. A ficha
  habitual é a CCS; alguns carros mais antigos usam CHAdeMO. Há postos que têm as duas e também uma
  tomada AC [UVE, formas de carregamento].
- **Posto ultrarrápido**: um posto rápido acima de 150 kW [UVE, manual].
- A UVE chama-lhes PCN (posto de carregamento normal), PCR (posto de carregamento rápido) e PCUR
  (posto de carregamento ultrarrápido). O utilizador pode usar essas siglas.
- Num posto rápido que também tem tomada Tipo 2, diz para usar a ficha DC (CCS ou CHAdeMO). Pela
  Tipo 2 o carro carrega em AC, limitado pelo carregador de bordo [UVE, manual].
- **Rede Tesla**: muitos Superchargers abriram a carros de outras marcas. Os carros Tesla não têm
  prioridade nesses postos [UVE, carregar com respeito]. Confirma na app da Tesla se um posto
  concreto aceita outras marcas.
- **Nomes oficiais por potência** (AFIR, art. 2.º e anexo, como a DGEG os resume) [DGEG, FAQ
  1.2.9]. Usa-os quando o utilizador ou um documento oficial falar destas categorias. Os limites
  não coincidem com as siglas da UVE: o "ultrarrápido" do AFIR começa nos 150 kW em DC, o "rápido"
  em DC nos 50 kW.

  | Corrente | Nome | Potência máxima |
  |---|---|---|
  | AC | lento, monofásico | menos de 7,4 kW |
  | AC | velocidade média, trifásico | de 7,4 a 22 kW |
  | AC | rápido, trifásico | mais de 22 kW |
  | DC | lento | menos de 50 kW |
  | DC | rápido | de 50 kW a menos de 150 kW |
  | DC | ultrarrápido, nível 1 | de 150 kW a menos de 350 kW |
  | DC | ultrarrápido, nível 2 | 350 kW ou mais |

  No AFIR, até 22 kW é "potência normal" e acima disso "alta potência".

## Fichas e tomadas

### Europa (padrão em Portugal)

- **Tipo 2 (Mennekes)**: ficha AC mais comum em carros e postos europeus, até 43 kW (trifásico). A
  maioria dos carros europeus usa Tipo 2; em casa e em postos normais costuma ser a única ficha.
- **CCS (Combined Charging System) Combo 2**: a ficha DC padrão na Europa. Combina as fases AC do
  Tipo 2 com dois pinos DC adicionais. É a ficha dominante nos postos rápidos europeus.
- **CHAdeMO**: ficha DC japonesa, ainda presente em carros antigos (Nissan Leaf, Mitsubishi) e em
  alguns postos. Em desuso na Europa: os novos postos e carros já não a incluem. Diz ao
  utilizador para confirmar se o posto a tem quando o carro for CHAdeMO.
- **Tomadas CEE industriais (IEC 60309)**: tomadas de corrente alternada usadas em postos
  públicos lentos, campings e instalações particulares. Cores e amperagens:
  - **Azul**: monofásica, 230 V, 16 A (3,7 kW) ou 32 A (7,4 kW). Comum em campings e marinas.
  - **Vermelha**: trifásica, 400 V, 16 A (11 kW) ou 32 A (22 kW). Usada em postos e instalações
    industriais; dá a potência máxima em AC para carros com carregador trifásico.
  - **Amarela**: 110 V (rara em Portugal).
  - É preciso cabo próprio com a ficha CEE de um lado e Tipo 2 do outro; muitos postos não têm
    cabo preso.

### América do Norte

- O sistema elétrico é diferente: 120 V / 240 V, 60 Hz, e a ficha doméstica (NEMA 5-15) não dá
  para carregar depressa. Usa-se o **NEMA 14-50** (240 V, 50 A) em casa e em campings.
- **J1772 (Tipo 1)**: a ficha AC padrão nos EUA/Canadá, monofásica, até 7,7 kW. Incompatível
  com o Tipo 2 europeu sem adaptador.
- **CCS1 (Combo 1)**: a ficha DC norte-americana, equivalente ao CCS2 mas com J1772 em vez de
  Tipo 2. Foi o padrão DC nos EUA até recentemente.
- **NACS (ficha Tesla)**: a ficha proprietária da Tesla (North American Charging Standard). A
  Tesla abriu-a e os fabricantes norte-americanos adotaram-na; hoje é o padrão de facto nos EUA
  em vez da CCS1. Os Superchargers norte-americanos usam NACS. Carros com CCS1 precisam de
  adaptador.
- **CHAdeMO** também existiu nos EUA (Nissan Leaf) mas está em desuso.

### China

- **GB/T**: o padrão chinês, com ficha AC e DC próprias (não compatíveis com CCS nem Tipo 2).
  É a ficha predominante na China e em parte da Ásia.

### Japão

- **CHAdeMO** é o padrão histórico japonês para DC. Ainda comum nos carros e postos japoneses.
  No resto do mundo está em desuso.

### Notas práticas

- Ao viajar, confirma sempre a ficha do posto e do carro; as fichas não são todas compatíveis.
  Adaptadores existem mas limitam a potência e nem sempre são seguros.
- Num posto rápido com várias fichas (CCS, CHAdeMO, Tipo 2), usa a DC (CCS ou CHAdeMO) para
  carregamento rápido; a Tipo 2 carrega em AC, limitado pelo carregador de bordo.

## Roaming e Plug & Charge

- **Roaming**: o cartão ou a app de um eMSP funciona em postos de vários OPC, às vezes em vários
  países. Confirma com o eMSP que redes e países cobre e quanto cobra em roaming, que pode ser mais
  do que o preço local.
- **Plug & Charge**: em alguns carros e postos basta ligar o cabo, sem cartão nem app. Só funciona
  se o carro, o posto e o eMSP o suportarem; senão, usa-se o cartão ou a app.
- Para perguntas técnicas (hubs de roaming, OCPP, OCPI, a PKI do Plug & Charge, baterias nos
  postos), usa a skill `tecnologia-de-carregamento`.

## Quanto tempo demora

Não há uma resposta igual para todos. Explica do que depende [UVE, formas de carregamento]:

- **O carro**: o carregador de bordo limita a potência em AC; em DC, conta a curva de carregamento.
- **O nível da bateria**: em DC, a potência mais alta costuma estar entre cerca de 20 % e 80 %,
  conforme o modelo. Com a bateria muito baixa, o carro pode demorar a chegar à potência máxima
  [UVE, manual]. Perto do cheio abranda muito: a potência costuma cair bastante a partir de cerca de
  80 % [UVE, carregar com respeito].
- **A potência do posto**: a útil é a menor entre a do posto e a que o carro aceita.
- **A temperatura**: o frio e o calor extremos tornam o carregamento mais lento. A bateria carrega
  melhor entre cerca de 20 e 30 °C; abaixo de 10 °C a potência pode cair [UVE, manual].

Um carro que mantém uma potência alta durante muito tempo pode carregar mais depressa do que outro
que anuncia um pico maior mas o perde em poucos minutos [UVE, química das baterias]. Para viagens,
olha para os minutos de 10 a 80 % publicados para a versão, não para o pico.

### As contas

Se o utilizador quer perceber de onde vem um tempo, explica a conta com os números da versão
exata, nunca de memória [UVE, manual]:

- Potência (kW) vezes horas dá energia (kWh): 7 kW durante 2 horas são cerca de 14 kWh.
- Tempo aproximado = energia a carregar ÷ a menor potência entre a do posto e a que o carro aceita
  (o carregador de bordo em AC, a potência máxima em DC).
- Diz que é uma aproximação. Em DC, a curva de carregamento muda o resultado; em AC, as perdas
  também contam.
- "Quilómetros por hora de carregamento" depende do consumo do carro: o mesmo posto dá mais
  quilómetros a um carro que gasta menos. Prefere falar em kW e kWh. Para autonomia, ver a skill
  `autonomia`.

### Que posto usar

- No dia a dia, carregar num posto normal enquanto o carro está parado de qualquer forma: em casa,
  no trabalho, nas compras [UVE, manual].
- Em viagens longas e quando há pressa, um posto rápido ou ultrarrápido.
- Numa viagem, carregar até 100 % num posto rápido não poupa tempo. Em regra é melhor ir até cerca
  de 80 % e seguir para o posto seguinte [UVE, manual].

## Como pagar

### Modelo antigo (MOBI.E, até 31-12-2027)

A história e as regras do regime anterior estão na skill `regime-2010`. Aqui fica só o que o condutor
precisa para pagar hoje.

- O condutor tem contrato com um CEME, que lhe dá um cartão ou uma app que funciona em todos os
  postos da rede MOBI.E. O preço da energia do CEME é o mesmo em todos os postos
  [UVE, novo regime].
- O OPC cobra a utilização do posto, por kWh, por minuto, um valor fixo por carregamento (taxa de
  ativação) ou uma combinação destes [UVE, manual]. Esses valores têm de estar afixados no posto.
  Quando há cobrança ao minuto, a potência real do carro conta para o preço.
- A fatura do CEME discrimina tudo: energia do CEME, tarifa de acesso às redes da mobilidade
  elétrica (TAR), tarifa do OPC, tarifa da EGME e impostos (IEC e IVA).

### Modelo novo (DL 93/2025)

- O OPC compra a eletricidade e fixa um preço total, por kWh ou por kWh mais minuto. A fatura é
  simplificada, sem parcelas [UVE, novo regime].
- Para carregar na rede de um OPC, o condutor faz contrato com esse OPC e usa o cartão ou a app dele.
- Um eMSP junta postos de vários OPC num só contrato e numa só fatura. A app do eMSP mostra só os
  postos que ele cobre.
- As subscrições podem mudar muito o preço: a UVE encontrou casos em que sem subscrição se paga duas
  a três vezes mais [UVE, análise do novo regime]. Se o utilizador carrega muitas vezes na mesma
  rede, sugere comparar com e sem subscrição.
- O OPC não pode cobrar preços diferentes a quem paga ad hoc e a quem vem por um eMSP, nem entre
  eMSP. Pode dar descontos com critérios objetivos, por exemplo a quem tem subscrição (DL 93/2025,
  art. 14.º, n.º 4). A fatura do OPC tem de mostrar o preço total e as parcelas por tipo de serviço
  (art. 14.º, n.º 5).

### Ad hoc, sem contrato

- Os postos instalados ou renovados têm de permitir o carregamento ad hoc, nos termos do AFIR
  (DL 93/2025, art. 6.º, n.º 1). Na prática paga-se com cartão bancário nos postos de 50 kW ou
  mais, ou por QR code nos de menor potência [UVE, novo regime].
- Nos postos públicos de 50 kW ou mais que já estavam instalados e a funcionar a 19-08-2025, as
  obrigações sobre os meios de pagamento, incluindo o ad hoc, só se aplicam a partir de 01-01-2027
  (DL 93/2025, art. 44.º, n.º 6). Até lá, um desses postos pode ainda não aceitar pagamento ad hoc.
- **Cativação**: ao pagar com cartão bancário, o posto pode cativar um valor bem maior do que o
  carregamento, às vezes mais do dobro, e esse dinheiro pode ficar indisponível vários dias
  [UVE, análise do novo regime]. Avisa quem tem pouco saldo disponível.

## Encontrar postos

- Se tiveres uma ferramenta que procura postos (no ohmigo: `find_chargers`, `lookup_charger`), usa-a.
- Senão, há mapas e apps: o mapa da MOBI.E, Electromaps, PlugShare, miio, a app da Tesla e as apps de
  cada OPC [UVE, pesquisa de pontos de carga]. Algumas mostram o estado do posto e comentários de
  outros condutores.
- Há também apps que juntam o carro e os cartões do condutor: comparam o preço, estimam o tempo,
  indicam a ficha a usar e planeiam a viagem com as paragens. A UVE refere, por exemplo, EVIO e miio
  em Portugal e Chargemap e Electromaps na Europa [UVE, manual].
- Antes de ir, confirma a ficha, a potência, o horário (há parques que fecham) e o número de apoio do
  OPC.

## Boas práticas

A rede pública é partilhada. A UVE resume-o na campanha "Carregar com Respeito"
[UVE, carregar com respeito]:

- Carregar só o necessário para chegar com folga ao destino seguinte. Em DC, sair quando a potência
  cai muito, em regra perto dos 80 %. Os últimos pontos percentuais custam muitos minutos ao
  condutor e a quem espera.
- Não ocupar um lugar de carregamento sem carregar, e tirar o carro quando acabar.
- Planear: começar uma viagem longa com a bateria cheia, evitar as horas de ponta e, se houver fila,
  parar uns quilómetros antes ou num posto de outro OPC.
- Numa fila não há senhas: perguntar quem é o último e dizer quanto falta para acabar evita quase
  todos os conflitos.
- Ninguém tem prioridade, exceto veículos de emergência em missão.

Estacionar num lugar de carregamento sem carregar pode dar multa e reboque
[UVE, avisos de cortesia]. Um carro que não é elétrico num lugar reservado a veículos elétricos em
carga é punido pelo Código da Estrada (DL 93/2025, art. 20.º, n.º 8).

**Taxa de ocupação.** O OPC tem de afixar em todos os seus postos a taxa de ocupação, em preço por
minuto, que cobra a quem deixa o carro ligado depois de a bateria estar carregada (DL 93/2025,
art. 14.º, n.º 2). Lembra o utilizador de a ver antes de deixar o carro a carregar e ir embora.

## O que o posto tem de mostrar

Num posto público, antes de começar, o condutor tem direito a ver (DL 93/2025, art. 14.º, n.ºs 1 a
3):

- o tipo de posto, o tipo de corrente e a potência máxima;
- o preço ad hoc com todas as parcelas, por kWh, por minuto ou por sessão, incluindo tarifas e
  impostos;
- a taxa de ocupação;
- as regras de segurança a seguir.

Cada equipamento tem também duas etiquetas: uma com as entidades responsáveis (o OPC, a DGEG, a
ERSE e a ENSE) e outra com as instruções de carregamento [DGEG, acesso público]. Se o utilizador
não souber de quem é um posto, a etiqueta diz-lhe.

Mais regras que protegem o condutor:

- O OPC tem de deixar carregar qualquer condutor, com ou sem contrato. Só pode recusar por
  incompatibilidade técnica com o carro (DL 93/2025, art. 13.º, n.º 1, a), e n.º 2).
- Os postos públicos são inspecionados antes de abrir e de 5 em 5 anos por uma entidade
  inspetora (EIIEL). Sem o certificado, a ENSE pode mandar fechar o posto (art. 16.º).
- Para saber se uma empresa é OPC licenciado, a DGEG publica a lista dos OPC e a dos CEME do regime
  antigo (ligações nas fontes). Não copies as listas: mudam.

## Quando o posto não funciona

- O apoio é dado pelo OPC do posto, não pela MOBI.E [UVE, rede de carregamento]. O OPC é obrigado a
  ter apoio ao condutor disponível durante todo o tempo em que o posto está a funcionar (DL 93/2025,
  art. 13.º, n.º 1, k).
- **Dá logo o número de apoio.** Se tiveres uma ferramenta que identifica o posto (no ohmigo:
  `lookup_charger`), o telefone de apoio do OPC vem no resultado (`support.phone`), tal como o OPC o
  publica no Ponto de Acesso Nacional. Usa esse e diz que vem do OPC. Um telefone de outra origem,
  por exemplo do OpenStreetMap, pode ser da loja ou do dono do local, e não do apoio ao posto.
- Sem ferramenta, o número está na etiqueta do posto e na app do OPC. Não o dês de memória: os
  números mudam. As listas da DGEG de OPC e de CEME não têm telefones.
- Se o cabo estiver cortado ou o posto vandalizado, sugere avisar o OPC. Os furtos de cabos têm
  afetado sobretudo postos rápidos [UVE, furto e vandalismo].
- **Perigo** (fumo, cheiro a queimado, cabo descarnado): não tocar no posto nem no cabo, afastar
  as pessoas e ligar o 112 se houver risco. Muitos postos têm um botão de corte de emergência: é
  obrigatório nas instalações acima de 22 kVA, mas os postos instalados antes de 2019 podem não o
  ter [DGEG, acesso público; DGEG, inspeções periódicas]. Depois, avisar o OPC: o OPC tem de
  comunicar qualquer acidente elétrico à DGEG e à ENSE (art. 14.º, n.º 8).
- **Reclamar**: o OPC tem de ter livro de reclamações. Se não houver atendimento no local, tem de
  ter o livro eletrónico no site e um aviso no posto a dizer como reclamar. As reclamações são
  tratadas pela ERSE (DL 93/2025, art. 14.º, n.ºs 6 e 7). Sugere juntar a data, a hora, o
  identificador do posto e fotografias.

## No estrangeiro

- Fora de Portugal não há um meio de pagamento único: conforme o país e a rede, paga-se por app,
  cartão bancário ou cartão da rede [UVE, carregamento na Europa]. O planeamento é do condutor.
- Na UE, o regulamento AFIR obriga os postos públicos a aceitar pagamento ad hoc.
- Redes com app própria que a UVE indica para viagens: IONITY (rápidos, na Europa), Iberdrola e Ibil
  (Espanha), Fastned (Países Baixos e Alemanha). Electromaps cobre a Península Ibérica.
- Confirma na app da rede antes de partir: as redes e os países cobertos mudam.

## Custo face à combustão

Não dês valores de memória. A UVE publica todos os meses um comparativo do custo de percorrer
100 km com carros elétricos e a combustão, e o Observatório da Mobilidade Elétrica mostra o custo
médio de carregamento em Portugal (ligações nas fontes). Encaminha para lá e diz a data do
comparativo.

## Fontes

### Legislação

- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica):
  https://data.dre.pt/eli/dec-lei/93/2025/08/14/p/dre/pt/html
- Decreto-Lei n.º 155/2026, de 31 de julho (prorroga o período transitório até 31-12-2027):
  https://data.dre.pt/eli/dec-lei/155/2026/07/31/p/dre/pt/html
- Regulamento (UE) 2023/1804 (AFIR): https://eur-lex.europa.eu/eli/reg/2023/1804/oj
- Regulamento n.º 7/2026, de 6 de janeiro (ERSE — Regulamento da Mobilidade Elétrica):
  https://diariodarepublica.pt/dr/detalhe/regulamento/7-2026-994000576

### Normas e standards

- IEC 62196-1:2025 (fichas, tomadas e conectores — requisitos gerais):
  https://webstore.iec.ch/en/publication/86313
- IEC 62196-2:2025 (fichas e tomadas AC — Tipo 1 e Tipo 2):
  https://webstore.iec.ch/en/publication/86317
- IEC 62196-3 (fichas e conectores DC — CCS e CHAdeMO):
  https://webstore.iec.ch/en/publication/59923
- IEC 61851-1 (sistema de carregamento condutivo):
  https://webstore.iec.ch/en/publication/33644
- ISO 15118-2 (comunicação veículo-rede — Plug & Charge):
  https://www.iso.org/standard/55366.html
- DATEX II — domínio de carregamento de veículos elétricos:
  https://datex2.eu/user-domains/ev-charging/

### Outras fontes

Da DGEG – Direção-Geral de Energia e Geologia, verificado a 2026-11-04:

- [DGEG, FAQ …] Perguntas frequentes, com o número da pergunta:
  https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/perguntas-frequentes-faq-s/
- [DGEG, acesso público] https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/acesso-publico/
- [DGEG, inspeções periódicas] https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/inspecoes-periodicas/
- Lista de OPC licenciados: https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/lista-de-opc/
- Lista de CEME (regime transitório): https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/regime-transitorio/ceme-registados/

Os pontos da DGEG estão escritos por palavras nossas (ver `docs/fontes/dgeg.md` no Voltaria).

Da UVE – Associação de Utilizadores de Veículos Elétricos, verificado a 2026-11-04:

- [UVE, formas de carregamento] "Como carregar um veículo elétrico":
  https://www.uve.pt/page/como-carregar-um-veiculo-eletrico/
- [UVE, novo regime] "O Novo Regime Jurídico da Mobilidade Elétrica – Saiba o que traz de novo para
  o Utilizador" (Blueauto n.º 97, nov./dez. 2025): https://www.uve.pt/page/blueauto-11_12-2025/
- [UVE, análise do novo regime] "Análise UVE | Novo Regime Jurídico da Mobilidade Elétrica"
  (26-8-2025): https://www.uve.pt/page/analise-uve-nrjme-08-2025/
- [UVE, carregar com respeito] "Carregar com Respeito" (Blueauto n.º 104, jul. 2026):
  https://www.uve.pt/page/blueauto-07-2026/
- [UVE, química das baterias] "A química das baterias (LFP ou NMC)" (Blueauto n.º 105, ago. 2026):
  https://www.uve.pt/page/blueauto-08-2026/
- [UVE, avisos de cortesia] "Avisos de Cortesia para Utilizadores de VE":
  https://www.uve.pt/page/avisos-de-cortesia-para-utilizadores-de-ve-nova-versao-2018/
- [UVE, pesquisa de pontos de carga] https://www.uve.pt/page/pontos-de-carga/
- [UVE, rede de carregamento] "Alteração do Call-Center da MOBI.E para os OPC" (1-10-2020):
  https://www.uve.pt/page/alteracao-do-call-center-da-mobi-e-para-os-opc/
- [UVE, furto e vandalismo] "Análise UVE | Furto e vandalismo em Postos de Carregamento" (out. 2025):
  https://www.uve.pt/page/analise-uve-furto-e-vandalismo-em-pvce_outubro-2025/
- [UVE, carregamento na Europa] https://www.uve.pt/page/carregamento-na-europa/
- [UVE, manual] "Parabéns! Comprou um veículo elétrico e agora?" (manual, jul. 2024), licença
  CC BY 4.0: https://www.uve.pt/page/wp-content/uploads/2025/01/2024_manual_me-UVE.pdf
  A parte sobre pagamentos é anterior ao DL 93/2025: não a uses para o regime atual.
- Comparativo 100 km, elétrico vs. combustão (mensal): https://www.uve.pt/page/quanto-custa-100-km/
- Observatório da Mobilidade Elétrica: https://observatorio.uve.pt/

O que vem da UVE está assinalado com [UVE, …] e foi reescrito, com autorização da UVE (ver
`docs/fontes/uve.md` no Voltaria). O manual da UVE está sob CC BY 4.0 e os pontos que vêm dele foram
adaptados. Cita a UVE quando usares esses pontos.
