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

## Roaming, hubs e plataformas

### O que é o roaming

- **Roaming** é o que permite a um condutor com um cartão ou app de um fornecedor carregar num
  posto de outro operador, sem contrato direto com esse operador. O posto (CPO) e o fornecedor do
  cartão (eMSP) trocam autorização, dados de sessão e faturação entre si.
- **CPO (Charging Point Operator)**: opera os postos físicos e a sua backoffice.
- **eMSP (e-Mobility Service Provider)**: vende o cartão/app ao condutor e fatura-o.
- Um mesmo ator pode ser CPO e eMSP ao mesmo tempo.

### Hubs de roaming

Em vez de cada CPO negociar com cada eMSP (peer-to-peer), muitos usam um **hub** que liga todos
numa só integração técnica e contratual.

- **Hubject (intercharge)**: um dos maiores hubs europeus, com mais de 1 milhão de pontos de
  carregamento e milhares de parceiros em 75+ países. Suporta OICP e OCPI, e é a base do
  Plug & Charge (ISO 15118). Forte presença na Europa e além.
- **Gireve**: hub francês, forte na Europa (especialmente França e sul da Europa). Usa eMIP e
  OCPI. Conhecido pelos serviços de dados (localização, disponibilidade) para parceiros de
  navegação. Líder de intermediação na Europa.
- **e-clearing.net**: hub com raízes na Holanda e Alemanha, usa OCHP e OCPI.
- **OCPI (Open Charge Point Interface)**: protocolo aberto mantido pela EVRoaming Foundation, usado
  tanto peer-to-peer como através de hubs. É o protocolo mais usado em novas integrações de
  roaming e dados.

### Plug & Charge

- O **Plug & Charge** (ISO 15118) permite carregar sem cartão nem app: basta ligar o cabo, e o
  carro e o posto autenticam-se e faturam automaticamente. Depende de certificados e de uma
  infraestrutura de chave pública. O Hubject é uma das entidades que gere a raiz de confiança.
- Ainda em expansão; nem todos os carros e postos o suportam.

### Pan-European eRoaming Initiative

- Em 2014-2015, as plataformas MOBI.E, Hubject, Gireve, e-clearing.net e Enel (entre outras)
  lançaram uma iniciativa para interligar as redes europeias (interroaming), com o objetivo de
  reduzir barreiras e criar uma infraestrutura interoperável na Europa.

### Outras plataformas

- **Virta**: plataforma de roaming gerido que assenta sobre hubs (Hubject, Gireve) e trata de
  contratos, integração, liquidação e disputas por conta do CPO/eMSP.
- **MOBI.E**: a plataforma portuguesa (CEME/OPC) que funciona como hub nacional e liga-se às
  redes europeias.

### Notas práticas

- Para o condutor, o roaming significa que um único cartão/app serve em vários países. Confirma
  sempre com o fornecedor quais as redes e países cobertos e as tarifas de roaming, que podem ser
  mais altas do que as tarifas locais.
- O pagamento ad hoc (cartão bancário no posto) existe independentemente do roaming e é obrigatório
  em muitos postos públicos na UE (AFIR).

## BESS (armazenamento de energia em bateria)

### O que é

- **BESS** (Battery Energy Storage System) é um sistema de armazenamento de energia em bateria
  instalado no local do posto, que pode ser carregado da rede ou de renováveis e descarregado para
  alimentar os carregadores ou para serviços de rede.
- Permite a um posto entregar mais potência do que a ligação à rede suportaria, sem reforço do
  ramal.

### Peak shaving

- Os postos rápidos têm picos de potência muito altos e imprevisíveis (vários carros a carregar ao
  mesmo tempo). A tarifa de potência (demand charge / capacity charge) cobra esses picos.
- O BESS descarrega durante os picos, limitando a potência pedida à rede. Pode reduzir a potência
  de ligação necessária em 50-80 % e as tarifas de demanda em 40-60 %.

### Estabilidade da rede

- Atua como buffer: absorve picos de carga e evita flutuações de tensão/frequência no ponto de
  ligação, ajudando a DSO a gerir o nó.
- Pode prestar serviços de flexibilidade (resposta em frequência FCR/FFR/aFRR, curtailment) e
  participar em mercados de energia (arbitragem de preços, load shifting).
- Em casos de indisponibilidade da rede, pode servir de backup (resiliência).

### Como suplementa um hub

- Num hub de carregamento, o BESS funciona como fonte secundária: quando a procura excede a
  capacidade da ligação, descarrega; em períodos de baixa procura, recarrega (da rede a baixo
  preço ou do solar).
- Permite instalar mais carregadores e de maior potência sem esperar por reforço de rede, que pode
  demorar meses ou anos.

### Quem usa

- Vários CPOs e operadores de hubs usam BESS em hubs de carregamento rápido, sobretudo em locais
  com ligação fraca ou cara. Exemplos referidos na indústria: InstaVolt (Reino Unido), HEP
  (Croácia), e operadores que usam plataformas como Flexecharge, Driivz, Voltic ou EMS próprios.
- A lista de adoptantes muda rapidamente; confirma sempre com o operador concreto.

### Principais OEMs / fornecedores de BESS

- Fabricantes de baterias e sistemas: Tesla (Megapack), BYD, CATL, Sungrow, Fluence, Wärtsilä,
  Powin, LG Energy Solution, Samsung SDI, Saft (TotalEnergies).
- Integradores e EMS (energy management): Driivz, Flexecharge, Voltic, Novagrid, JEM Energy,
  Wattstor, Orbit Energy, entre outros.
- A escolha depende do tamanho do hub, da ligação disponível e do regime de serviços de rede local.

### Notas práticas

- O BESS tem de ser dimensionado ao perfil real do hub; um sistema subdimensionado esgota-se cedo e
  perde poupança de demanda.
- A viabilidade económica depende do custo da energia, das tarifas de potência e dos serviços de
  rede disponíveis localmente. ROI típico de 5-7 anos em hubs co-localizados.

## OCPP e OCPI (protocolos)

### OCPP (Open Charge Point Protocol)

- **O que é**: protocolo aberto de comunicação entre o posto de carregamento (hardware) e o
  sistema de gestão central (CSMS/backoffice). É a "língua" entre o carregador e o servidor do
  operador.
- **Quem mantém**: Open Charge Alliance (OCA).
- **Versões**: 1.6 (2015, amplamente usado), 2.0.1 (2020, aprovado como IEC 63584 em 2024),
  2.1 (2025, com suporte a ISO 15118-20 e bidirecional/V2X).
- **O que faz**: estado do posto, autorização de sessão, valores de medição, firmware, diagnóstico,
  smart charging (perfis de carga), transações. Sem OCPP, cada fabricante usaria protocolo
  proprietário e o operador ficaria preso a um fornecedor.
- **Importância**: é o standard global de facto para ligar carregadores ao backoffice; permite
  interoperabilidade de hardware, atualizações remotas e gestão de carga.

### OCPI (Open Charge Point Interface)

- **O que é**: protocolo aberto de comunicação entre backends de diferentes redes (CPO ↔ eMSP,
  ou via hub). É a "língua" entre operadores, não entre posto e servidor.
- **Quem mantém**: EVRoaming Foundation.
- **Versões**: 2.1.1, 2.2.1, 2.3.0 (a versão 2.3.0 é compatível com o NAP/AFIR; a 3.0 está
  em draft).
- **O que faz**: troca de localizações e disponibilidade em tempo real, tokens de autorização,
  sessões, CDR (Charge Detail Records) para faturação, tarifas, comandos remotos, smart charging.
  Permite roaming: um condutor de uma rede usar postos de outra sem novo registo.
- **Importância**: é a base do roaming peer-to-peer e via hubs; a versão 2.3.0 está alinhada com
  o AFIR e o NAP europeu.

### Como se relacionam

- **OCPP** é "south-bound" (backoffice ↔ carregador). **OCPI** é "east-west"
  (backoffice ↔ backoffice). São complementares, não alternativos.
- Um CPO usa OCPP para gerir os seus postos e OCPI para ligar-se a eMSPs e hubs de roaming.
- Fluxo típico: um eMSP envia um limite de carga via OCPI ao backoffice do CPO, que o traduz
  e reencaminha ao carregador via OCPP.

### Fontes

- Open Charge Alliance (openchargealliance.org) — especificações OCPP.
- EVRoaming Foundation (evroaming.org) — especificações OCPI.
- OCPI é publicado sob Creative Commons Attribution-NoDerivatives 4.0.

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
[UVE, avisos de cortesia]. Alguns OPC cobram uma tarifa de ocupação depois de o carregamento
acabar: está nas condições do posto ou da app.

## Quando o posto não funciona

- O apoio é dado pelo OPC do posto, não pela MOBI.E [UVE, rede de carregamento]. O número costuma
  estar no posto e na app.
- Se o cabo estiver cortado ou o posto vandalizado, sugere avisar o OPC. Os furtos de cabos têm
  afetado sobretudo postos rápidos [UVE, furto e vandalismo].

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

- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica):
  https://diariodarepublica.pt/dr/detalhe/decreto-lei/93-2025-928937303
- Decreto-Lei n.º 155/2026, de 31 de julho (prorroga o período transitório até 31-12-2027):
  https://files.diariodarepublica.pt/1s/2026/07/14700/0003200033.pdf
- Regulamento (UE) 2023/1804 (AFIR): https://eur-lex.europa.eu/eli/reg/2023/1804/oj

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
