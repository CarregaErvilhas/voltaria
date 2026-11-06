---
name: carregar-em-casa
description: "Ajuda um condutor em Portugal a carregar o carro elétrico em casa ou na garagem do prédio, com tomada doméstica ou wallbox, em moradia ou condomínio, ligado ou não à MOBI.E, com ou sem painéis solares. Usa quando o utilizador pergunta como instalar, quem pode fazer a instalação, que papéis pedir, de que quadro ligar o posto, o que o condomínio pode recusar ou quanto custa carregar em casa."
---

# Carregar em casa

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- Não inventes preços, potências de um carro concreto nem prazos que não estejam aqui. Para o carro,
  procura as especificações da versão exata (carregamento AC máximo, fases, ficha). Para o preço de
  um carregamento em casa, usa a ferramenta de custos se a tiveres (no ohmigo:
  `estimate_charging_cost` com `private`).
- Não digas que uma instalação está aprovada ou que é segura. Isso cabe ao técnico certificado que a
  faz e, num prédio, também à administração do condomínio.
- Não dês parecer jurídico. Explica o que a lei diz, cita o artigo e, se houver um conflito com o
  condomínio, sugere apoio jurídico.
- Em casa o utilizador é um DPC, não um OPC: o posto não é acessível ao público. Não o procures no
  NAP nem perguntes onde fica.

## O que perguntar primeiro

Pergunta só o que não souberes, uma coisa de cada vez:

1. **Moradia ou prédio?** Num prédio: o lugar é uma garagem fechada só sua, um lugar na garagem
   comum, ou na rua?
2. **Que carro?** Procura tu as especificações. Não peças ao utilizador.
3. **Quanto conduz por dia**, em média. Define se uma tomada doméstica chega.
4. **Potência contratada** da casa e se o contrato é monofásico ou trifásico, se souber. Se não
   souber, está na fatura da eletricidade.
5. **Tarifa da eletricidade**: simples, bi-horária ou tri-horária.
6. **Painéis solares?** Se sim, tem autoconsumo (UPAC).

## As opções

### Tomada doméstica

- A lei permite carregar numa tomada doméstica em locais não acessíveis ao público, desde que se
  cumpram as regras técnicas e de segurança (DL 93/2025, art. 21.º, n.º 2).
- É a opção mais lenta. Chega quando o carro fica ligado muitas horas e os quilómetros por dia são
  poucos.
- Recomenda que um eletricista verifique o circuito antes do primeiro uso: um carregamento longo
  puxa muita corrente durante horas. Nada de extensões nem fichas múltiplas.
- O cabo que vem com o carro para a tomada doméstica é um carregador ocasional: serve para um
  recurso, não para ser a forma habitual de carregar durante muito tempo. Se a tomada for a solução
  de todos os dias, recomenda uma tomada reforçada e a instalação revista por um eletricista
  certificado [UVE, tomada ou wallbox].
- Numa tomada doméstica comum (Schuko) a corrente de carregamento não deve passar de **10 A**. Só
  uma tomada marcada de fábrica para carregar veículos aguenta mais. Muitos cabos de carregamento
  ocasional deixam escolher a corrente: diz ao utilizador para a pôr em 10 A ou menos numa Schuko
  que não seja própria para carregar. O guia da DGEG recomenda usar tomadas domésticas só em instalações existentes e, numa obra
  na instalação, pôr uma tomada própria para carregar [DGEG, guia técnico, 5.1.2.5.1].
- Regras do guia técnico que o eletricista deve cumprir, para o utilizador saber o que pedir
  [DGEG, guia técnico, 3.1.5, 4.3, 5.1.2.1.1]: um **circuito dedicado** para cada carro, para pelo
  menos 16 A e com cabos de 2,5 mm² ou mais; e um **diferencial próprio** (DR) de 30 mA ou menos,
  no mínimo do tipo A, para cada ponto de ligação.
- Nada de extensões nem de um segundo cabo. Adaptadores só os feitos para carregar veículos,
  marcados para isso e aprovados pelos fabricantes do carro e do equipamento [DGEG, guia técnico,
  2.2.1 e 2.2.2].

### Wallbox

- Carrega mais depressa e com mais segurança do que a tomada doméstica. Permite programar o
  carregamento e, em muitos modelos, limitar a potência à que a casa tem livre (balanceamento
  dinâmico).
- A potência útil é a menor de três: a da wallbox, a do carregador de bordo do carro em AC, e a que
  a instalação e a potência contratada deixam livre. Não recomendes uma wallbox trifásica a quem tem
  contrato monofásico sem dizer que é preciso mudar o contrato.
- O carregador de bordo depende do modelo e da versão: vai de 3,7 kW, comum nos híbridos plug-in,
  até 22 kW [UVE, tomada ou wallbox]. Procura o da versão exata do carro antes de recomendar uma
  wallbox: uma wallbox mais potente do que o carregador de bordo não carrega mais depressa.
- Aumentar a potência contratada aumenta o custo fixo da eletricidade. Diz isso, sem inventar
  valores. Se o ramal da casa ou do prédio tiver potência disponível, basta pedir ao comercializador
  de eletricidade. Se não tiver, o reforço do ramal é feito pela E-REDES, com obra e um custo que pode
  ser alto; num prédio, quem o paga é o condómino que o pede, salvo acordo com o condomínio
  [UVE, tomada ou wallbox] [UVE, casa ou condomínio].
- Uma wallbox com tomada ou cabo Tipo 2 precisa também de proteção contra correntes de defeito
  contínuas: um diferencial do tipo B, ou um do tipo A ou F com um detetor de corrente contínua,
  salvo se a própria wallbox já a tiver. Diz ao utilizador para confirmar isto com o instalador
  [DGEG, guia técnico, 5.1.2.1.1].

### Quem instala e que papéis pedir

- A instalação elétrica fica sujeita ao regime das instalações elétricas (DL 96/2017), através do
  DL 93/2025, art. 25.º, n.º 2. O técnico deve seguir o Guia Técnico das Instalações Elétricas para
  a Alimentação de Veículos Elétricos da DGEG, 3.ª edição, de 2023 (ligação nas fontes). A
  Portaria n.º 128/2026/1 (art. 3.º, n.º 4) prevê um guia novo da DGEG; a 2026-11-04 a DGEG ainda
  remete para a 3.ª edição. Se houver uma edição mais recente na página da DGEG, usa essa.
- **Quem pode fazer a instalação**: uma entidade instaladora (EI) ou um técnico responsável pela
  execução, registados na DGEG. Um técnico sozinho pode assumir instalações até 41,4 kVA; acima
  disso é preciso uma EI (Lei n.º 14/2015, art. 4.º, n.º 3; Portaria n.º 128/2026/1, art. 4.º,
  n.º 1) [DGEG, acesso privado]. Sugere ao utilizador pedir o número de registo na DGEG.
- **Se é preciso projeto** depende do tipo de instalação elétrica (DL 96/2017, art. 5.º). Entre
  outros casos, é obrigatório nas instalações do tipo B e nas do tipo C cuja potência total
  alimentada pela rede passe de 10,35 kVA [DGEG, acesso privado]. Quem diz se o caso precisa é o
  técnico; não o afirmes tu.
- **Depois da instalação**, o técnico ou a EI entrega uma declaração de conformidade da execução ou
  um termo de responsabilidade pela execução [DGEG, acesso privado]. Diz ao utilizador para o pedir
  e guardar: serve para o seguro, para o condomínio e para uma venda da casa.
- Quem tem o posto (o DPC) fica responsável por manter as condições técnicas e de segurança e por
  usar materiais e equipamentos conformes às normas (Portaria n.º 128/2026/1, art. 4.º, n.º 2).

### EVSE móvel vs. wallbox

- **EVSE móvel (carregador portátil)**: um cabo com eletrónica de segurança que liga uma tomada
  (doméstica Schuko ou industrial CEE) ao carro. Não é uma tomada "burra": tem proteção contra
  sobrecorrente, deteção de fuga de corrente e controlo do arranque. É o que vem com muitos carros
  (cabo ocasional). Limita-se à potência da tomada (numa Schuko comum até 10 A, cerca de 2,3 kW, ver acima; até 22 kW numa CEE
  vermelha de 32 A). É prático para viagens, casas de férias ou quando não há wallbox, mas não é
  pensado para uso diário prolongado.
- **Wallbox (EVSE fixo)**: unidade fixa à parede, ligada a um circuito dedicado. Dá mais potência
  (até ao limite do carregador de bordo do carro e da instalação), tem balanceamento dinâmico,
  programação de horários, medição e, em muitos modelos, modo solar. É a solução recomendada para
  carregamento habitual em casa.
- Diferença prática: o EVSE móvel depende da tomada existente e da sua proteção; a wallbox tem
  circuito próprio e proteções dimensionadas. Para uso diário, prefere-se wallbox; para ocasional ou
  em viagem, o EVSE móvel serve.
- Ambos são EVSE (Electric Vehicle Supply Equipment): o que carrega a bateria é o carregador de
  bordo do carro, não a wallbox nem o cabo.

### Carregar com painéis solares

- Com autoconsumo, o carro pode carregar com o excedente solar durante o dia. Há wallboxes com modo
  solar que seguem a produção.
- Só compensa se o carro estiver em casa nas horas de sol. Se só estiver à noite, a tarifa de vazio
  conta mais do que os painéis.

## Tomadas e fichas

### Tomada doméstica

- A tomada doméstica habitual em Portugal é a **Schuko (Tipo F)**, 230 V, 16 A. Para carregar um
  carro, o guia da DGEG limita a corrente a 10 A (cerca de 2,3 kW) numa Schuko comum; os 16 A
  (3,7 kW) só numa tomada marcada de fábrica para carregar veículos, num circuito dedicado
  [DGEG, guia técnico, 5.1.2.5.1].
- Não usar extensões nem fichas múltiplas. Um carregamento longo exige um circuito dedicado
  verificado por eletricista.

### Tomadas CEE industriais (IEC 60309)

Usadas em postos públicos lentos, campings, marinas e instalações particulares. São tomadas
industriais de encaixe rápido, com pinos em arco e anel de borracha. Cores e amperagens:

- **Azul**: monofásica, 230 V, 16 A (3,7 kW) ou 32 A (7,4 kW). Comum em campings e marinas.
- **Vermelha**: trifásica, 400 V, 16 A (11 kW) ou 32 A (22 kW). Usada em postos e instalações
  industriais; dá a potência máxima em AC a carros com carregador trifásico.
- **Amarela**: 110 V (rara em Portugal).

Para carregar num posto com tomada CEE é preciso um cabo próprio, com a ficha CEE de um lado e
Tipo 2 (ou Tipo 1, nos EUA) do outro. Muitos postos não têm cabo preso. O cabo define a potência
máxima: um cabo de 16 A limita a 3,7 kW mesmo numa tomada de 32 A.

### Ficha do carro (AC)

- **Tipo 2 (Mennekes)**: padrão europeu, monofásico ou trifásico, até 43 kW. É a ficha da
  maioria dos carros vendidos na Europa.
- **Tipo 1 (J1772)**: padrão norte-americano, monofásico, até 7,7 kW. Só em carros importados
  dos EUA/Canadá; precisa de adaptador para postos europeus.

### Fichas DC (carregamento rápido)

- **CCS Combo 2** (Europa) e **CCS Combo 1** (EUA): fichas DC dominantes. O carro e o posto têm
  de ter a mesma variante.
- **CHAdeMO**: padrão japonês, em desuso na Europa. Ainda em carros antigos (Nissan Leaf,
  Mitsubishi).
- **NACS (ficha Tesla)**: padrão de facto nos EUA, adotado pelos fabricantes norte-americanos.
- **GB/T**: padrão chinês, incompatível com CCS e Tipo 2.

## V2L, V2H e V2G (carregamento bidirecional)

### Conceitos

- **V2L (Vehicle-to-Load)**: o carro alimenta aparelhos elétricos através de uma tomada no
  próprio carro (ou um adaptador). Não precisa de wallbox nem de instalação especial.
- **V2H (Vehicle-to-Home)**: o carro alimenta a casa. Precisa de wallbox bidirecional e
  instalação elétrica certificada.
- **V2G (Vehicle-to-Grid)**: o carro envia energia para a rede pública, com contrato e
  remuneração. Precisa de carro compatível, wallbox bidirecional, software, contrato de energia,
  aprovação do operador de rede e contador bidirecional.
- **V2B (Vehicle-to-Building)**: variante do V2G para edifícios (sem injeção na rede pública).

### Legislação em Portugal

- **DL 93/2025, art. 2.º**: define "carregamento bidirecional" como uma operação de carregamento
  inteligente em que a direção do fluxo de eletricidade pode ser invertida, permitindo que a
  eletricidade flua da bateria para o ponto de carregamento (veículo-rede).
- **Art. 6.º**: os pontos de carregamento instalados ou renovados devem permitir carregamento ad
  hoc e inteligente nos termos do AFIR; as normas de comunicação que apoiam o carregamento
  bidirecional são as do Regulamento AFIR.
- **Regulamento da Mobilidade Elétrica da ERSE (RME)**: regula a atividade dos OPC e eMSP,
  incluindo medição, leitura e disponibilização de dados de eletricidade. O regime transitório
  vigora até 31-12-2027 (DL 155/2026).
- A utilização de carregamento inteligente ou bidirecional para prestação de serviços à rede não
  carece de regulamentação específica para além da já existente.
- O carregamento bidirecional está previsto no DL 93/2025, mas a sua implementação depende de
  veículos compatíveis e de uma norma europeia ainda não consolidada para AC ou DC.

### Protocolos e standards

- **ISO 15118-20**: standard de comunicação entre veículo e EVSE, base para carregamento
  inteligente e bidirecional. Suporta AC_BPT (bidirecional em AC) e DC_BPT (bidirecional em DC),
  Plug & Charge (autenticação por certificado) e controlo dinâmico.
- **ISO 15118-2**: primeira geração, carregamento unidirecional.
- **OCPP (Open Charge Point Protocol)**: protocolo entre posto e backoffice; versões recentes
  suportam funcionalidades de smart charging.
- **IEC 61851**: standard para sistemas de carregamento condutivo.
- **IEC 62196**: standard para fichas e tomadas (Tipo 1, Tipo 2, CCS).
- **AFIR (Regulamento (UE) 2023/1804)**: impõe carregamento ad hoc e inteligente em postos
  públicos; as normas de comunicação para bidirecional são as previstas no AFIR.
- **Redes de distribuição**: na UE, a interligação e certificação seguem a norma EN 50549 e os
  códigos de rede (RfG, DCC), ainda em consolidação para V2G.

### Estado atual

- Menos de 10 % dos modelos de VE em produção suportavam bidirecional em 2026. A maioria dos
  carros novos ainda é unidirecional.
- A interoperabilidade é o principal obstáculo: não existe ainda uma norma europeia consolidada
  para bidirecional em AC ou DC.
- Em Portugal, o DL 93/2025 abre a porta ao V2H (via autoconsumo), mas o V2G comercial ainda é
  residual.

## Num prédio (condomínio)

**Quando não é preciso falar com o condomínio.** Numa moradia, ou numa garagem ligada diretamente
à instalação elétrica da fração, sem passar por partes comuns, não há nada a comunicar ao
condomínio [UVE, casa ou condomínio].

**Prédios novos.** As construções novas em propriedade horizontal, ou com estacionamento, têm de
incluir uma infraestrutura elétrica adequada para carregar veículos, com uma potência mínima fixada
em portaria. Isto não inclui os postos nem as tomadas (DL 93/2025, art. 22.º). A Portaria n.º
128/2026/1 (art. 2.º) fixa os mínimos [DGEG, edifícios]:

- cada ponto de ligação tem de ter pelo menos 3680 VA;
- num prédio de habitação, só uma parte dos lugares tem de ficar preparada: N = 0,8 + 0,2 × n,
  arredondado para cima, em que n é o número de lugares do parque sem contar os que já são
  alimentados diretamente pelas frações. Num parque de 30 lugares, isso dá 7;
- num prédio de habitação é obrigatório um sistema de controlo de carga, que desliga os
  carregamentos ou reduz a corrente quando a potência não chega;
- o custo é do promotor da obra (art. 4.º, n.º 3).

A regra antiga, para licenciamentos desde 1-7-2010, pedia também que cada lugar ficasse preparado
para um posto ou uma tomada: vê a skill `regime-2010`. Não digas que um prédio novo já tem ligação
em cada lugar sem o utilizador o confirmar com o administrador ou o projeto.

**Quem pode instalar.** Qualquer condómino pode instalar, à sua custa, um posto de carregamento no
seu lugar de estacionamento, desde que o lugar cumpra os requisitos técnicos definidos em portaria
(DL 93/2025, art. 23.º, n.º 1). O mesmo vale para uma tomada. A DGEG diz que o mesmo direito tem o
arrendatário e o ocupante legal [DGEG, acesso privado; DGEG, FAQ 2.1.1]: o n.º 3, a) refere-os, e o
n.º 2 manda comunicar também ao proprietário.

**De onde vem a eletricidade e quem opera o posto.** Pergunta ao utilizador se o lugar é de uso
exclusivo ou partilhado e de que quadro elétrico o posto vai ser alimentado. Muda quem fica
responsável pelo posto (DL 93/2025, art. 21.º, n.º 1, como a DGEG o explica) [DGEG, acesso
privado; DGEG, FAQ 2.1.5, 2.1.6, 2.1.12 a 2.1.16]:

| Lugar | Pode ser alimentado por | Quem opera o posto |
|---|---|---|
| De uso exclusivo (boxe ou marcado no chão), ligado à instalação da fração | O quadro de entrada da fração | O próprio, como DPC |
| De uso exclusivo, ligado a um quadro comum | O quadro de colunas, o dos serviços comuns ou o da garagem | O condomínio, ou um OPC contratado por ele |
| De uso partilhado | O quadro de colunas ou o dos serviços comuns | O condomínio, ou um OPC contratado por ele |

- Ligado à fração, tem de sair do **quadro de entrada** da fração, não de um quadro parcial (por
  exemplo, o do segundo piso de um duplex) [DGEG, FAQ 2.1.15]. Vale também para frações de comércio
  ou serviços no mesmo prédio [DGEG, FAQ 2.1.16].
- Os cabos só podem passar pelas zonas comuns e pelos espaços da própria fração, nunca por dentro
  do lugar de outro condómino [DGEG, guia técnico, 3.1.5]. **Não podem passar pelo poço do
  elevador** nem por condutas ou tubos de outras instalações (RTIEBT, secção 803.4.1) [DGEG, FAQ
  2.1.17]. Se o percurso proposto passar por aí, diz que não é permitido.
- Num lugar marcado no chão, o circuito sai de um quadro próprio do lugar, que só abre com
  ferramenta, com um corte geral junto ao acesso [DGEG, guia técnico, 3.1.5].

**Comunicação prévia.** Se a instalação estiver numa parte comum do prédio, ou passar por ela, mesmo
que seja de uso exclusivo do condómino, é obrigatório comunicar por escrito à administração do
condomínio (e ao proprietário, se for arrendatário) com **pelo menos 30 dias** de antecedência sobre
a data da instalação (art. 23.º, n.º 2).

**Quando o condomínio se pode opor.** Só nestes casos (art. 23.º, n.º 3):

- a) o condomínio instala, **no prazo de 90 dias**, um ou mais postos partilhados que deem os mesmos
  serviços, a mesma tecnologia e cubram as necessidades de todos os potenciais utilizadores;
- b) o prédio já tem um posto ou tomada partilhada nessas condições;
- c) a instalação põe comprovadamente em risco a segurança de pessoas ou bens, com parecer técnico
  entregue à administração. Para saber se há risco, a DGEG manda pedir a avaliação a um engenheiro
  eletrotécnico ou engenheiro técnico registado na DGEG e, se a instalação puder afetar a segurança
  contra incêndio, também a um técnico de SCIE [DGEG, FAQ 2.1.7]. Um receio sem parecer técnico não
  chega;
- d) a instalação dificulta a circulação nas vias comuns de acesso;
- e) deixa de se cumprir, nos espaços comuns, o regime das acessibilidades (DL 163/2006).

**Prazos e forma da decisão** (art. 23.º, n.ºs 4 e 5):

- A decisão é tomada **no prazo máximo de 30 dias** após a comunicação e, se for da administração
  do condomínio, precisa de maioria simples do valor total do prédio. Isto é a maioria da
  permilagem, não a maioria dos votos dos presentes na assembleia [UVE, casa ou condomínio].
- Fica em ata, é comunicada por escrito aos condóminos ausentes **no prazo de 15 dias** e, se for
  negativa, tem de ser fundamentada.
- **Sem oposição fundamentada no prazo, o condómino pode instalar.** O direito de instalar vem do
  n.º 1; a oposição é a exceção e só vale num dos casos do n.º 3, decidida nos 30 dias do n.º 4. Se
  a administração não comunicar no prazo uma razão desses casos, a instalação pode avançar na data
  comunicada.
- Recomenda guardar prova da comunicação e da data em que foi recebida (carta registada com aviso
  de receção ou email com confirmação): é ela que conta os 30 dias. Se o condomínio contestar
  depois, sugere apoio jurídico.

Se o utilizador falar em 60 dias, dois terços ou "linha arquitetónica", são regras do regime anterior
(DL 39/2010, art. 29.º). Corrige com as de hoje; a skill `regime-2010` explica as antigas.

**Quem paga.** A instalação é paga pelo condómino (art. 23.º, n.º 1). A energia pode vir da
instalação da fração ou de um ponto de entrega próprio, o sub-CPE, nos termos que a ERSE regulamenta
(art. 24.º, n.º 3). A skill `sub-cpe` explica quando faz sentido e como se pede.

**O que levar à administração.** Ajuda o utilizador a escrever a comunicação: identificação do
condómino e do lugar, o equipamento e a potência, o percurso da cablagem pelas partes comuns, quem
instala (técnico certificado) e a data prevista, a pelo menos 30 dias. A UVE publica uma minuta para
esta comunicação (ligação nas fontes): sugere-a a quem prefira partir de um modelo.

**Antes de enviar** [UVE, casa ou condomínio]:

- Sugere uma visita técnica de um eletricista certificado ou de um instalador de postos antes de
  escolher o equipamento. Uma proposta viável à partida evita uma recusa e ter de recomeçar o
  processo.
- Quanto mais detalhe tiver a comunicação, melhor. Muitos condóminos não conhecem os carros
  elétricos e têm receios que uma instalação bem feita não justifica; uma descrição clara da
  instalação responde a esses receios antes de chegarem à assembleia.
- Se o condomínio recusar e o utilizador quiser contestar, sugere apoio jurídico. A UVE dá apoio
  jurídico aos seus associados nestes casos.

## Ligado à MOBI.E ou não

- Até 31-12-2027, a plataforma da MOBI.E continua gerida pela EGME (DL 93/2025, art. 44.º, na
  redação do DL 155/2026). Um posto privado pode estar integrado nela ou não.
- **Sem integração**: o carro carrega com a eletricidade da casa, ao preço do contrato de
  eletricidade.
- **Integrado na MOBI.E**: o carregamento passa pela plataforma, sujeito à tarifa da EGME fixada
  pela ERSE, que deve vir discriminada na fatura se for repercutida (art. 44.º, n.º 4).
- Alguns apoios para postos em condomínio exigem a ligação à MOBI.E. Vê a skill `incentivos`.

Como funciona uma wallbox integrada na MOBI.E, no período transitório [UVE, tomada ou wallbox]:

- Inicia-se o carregamento com um cartão ou app de um CEME, como num posto público. O dono não paga
  tarifa de OPC, porque o posto é dele: paga a energia ao preço do cartão que usar. Com um cartão de
  frota, a fatura vai para a empresa.
- O consumo da wallbox fica separado do resto da casa ou do prédio: cada um recebe a sua conta. É o
  que torna esta opção útil num lugar ligado ao quadro dos serviços comuns.
- Só carrega com cartão, e pode limitar-se a cartões escolhidos pelo dono. Uma tomada não faz essa
  distinção.
- O período transitório dos CEME acaba a 31-12-2027 (skill `regime-2010`). Não prometas como
  funcionará uma wallbox integrada depois dessa data: a regulamentação do novo regime ainda não o
  diz.

## Quanto custa

- Não dês valores de memória. Usa a ferramenta de custos se a tiveres. Se não, explica do que o
  custo depende: o preço do kWh no contrato da casa, o período horário em que carrega (vazio, fora de
  vazio) e, se estiver integrado na MOBI.E, a tarifa da EGME e o preço do comercializador.
- Na tarifa bi-horária ou tri-horária, recomenda programar o carregamento para as horas de vazio.

## Apoios

Para apoios à compra de um posto (por exemplo em condomínio) ou do carro, usa a skill `incentivos`.

## Fontes

### Legislação

- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica):
  https://data.dre.pt/eli/decreto-lei/93/2025/08/14/p/dre/pt/html
- Decreto-Lei n.º 155/2026, de 31 de julho (prorroga o período transitório até 31-12-2027):
  https://data.dre.pt/eli/decreto-lei/155/2026/07/31/p/dre/pt/html
- Regulamento (UE) 2023/1804 (AFIR): https://eur-lex.europa.eu/eli/reg/2023/1804/oj
- Decreto-Lei n.º 96/2017, de 10 de agosto (instalações elétricas de serviço particular
  alimentadas pela RESP): https://data.dre.pt/eli/decreto-lei/96/2017/08/10/p/dre/pt/html
- Decreto-Lei n.º 163/2006, de 8 de agosto (acessibilidade a edifícios — lugares de garagem e
  tomadas para carregamento): https://data.dre.pt/eli/decreto-lei/163/2006/08/08/p/dre/pt/html
- Portaria n.º 949-A/2006, de 11 de setembro (RTIEBT — regras técnicas das instalações elétricas
  de baixa tensão): https://data.dre.pt/eli/portaria/949-a/2006/09/11/p/dre/pt/html
- Portaria n.º 128/2026/1, de 26 de março (potências mínimas e regras técnicas dos postos):
  https://files.diariodarepublica.pt/1s/2026/03/06000/0000300006.pdf
- Regulamento (UE) 2016/631 (RfG — requisitos de ligação de geradores à rede) e Regulamento
  (UE) 2016/1388 (DCC — requisitos de ligação de instalações de consumo):
  https://eur-lex.europa.eu/eli/reg/2016/631/oj e https://eur-lex.europa.eu/eli/reg/2016/1388/oj

### Normas e standards

- IEC 60364-7-722 (instalações elétricas de baixa tensão — alimentação de veículos elétricos):
  https://webstore.iec.ch/en/publication/29958
- IEC 61851-1 (sistema de carregamento condutivo):
  https://webstore.iec.ch/en/publication/33644
- IEC 62196-1:2025 (fichas, tomadas e conectores — requisitos gerais):
  https://webstore.iec.ch/en/publication/86313
- IEC 62196-2:2025 (fichas e tomadas AC — Tipo 1 e Tipo 2):
  https://webstore.iec.ch/en/publication/86317
- ISO 15118-20 (comunicação veículo-rede — bidirecional, AC_BPT e DC_BPT):
  https://www.iso.org/standard/77845.html
- ISO 15118-2 (comunicação veículo-rede — Plug & Charge):
  https://www.iso.org/standard/55366.html
- OCPP (Open Charge Point Protocol, posto ↔ backoffice; IEC 63584):
  https://openchargealliance.org/protocols/ocpp-protocols/
- EN 50549-1 (requisitos de ligação de instalações geradoras de baixa tensão em paralelo com a
  rede) — referida nos códigos de rede da UE; a norma é paga, ver catálogo:
  https://genorma.com/en/standards/en-50549-1-2019

### Outras fontes

- Lei n.º 14/2015, de 16 de fevereiro (técnicos e entidades instaladoras):
  https://data.dre.pt/eli/lei/14/2015/p/cons/20200922/pt/html

Da DGEG – Direção-Geral de Energia e Geologia, verificado a 2026-11-04:

- [DGEG, guia técnico] Guia Técnico das Instalações Elétricas para a Alimentação de Veículos
  Elétricos, 3.ª edição (2023-09-14), da CTE 64, aprovado pela DGEG:
  https://www.dgeg.gov.pt/media/dzejui0r/guia-ve-ed-3-2023.pdf
- [DGEG, edifícios] https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/edificios/
- [DGEG, acesso privado] https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/acesso-privado/
- [DGEG, FAQ …] Perguntas frequentes, com o número da pergunta:
  https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/perguntas-frequentes-faq-s/

Os pontos da DGEG estão escritos por palavras nossas (ver `docs/fontes/dgeg.md` no Voltaria). As
FAQ da DGEG são uma leitura da lei pela entidade licenciadora: não substituem o texto da lei nem um
parecer jurídico.

Da UVE:

- [UVE, casa ou condomínio] UVE, "Como instalar um Ponto de Carregamento para Veículo Elétrico em
  casa ou no Condomínio" (7-11-2025), verificado a 2026-11-04:
  https://www.uve.pt/page/como-instalar-pcve-casa-ou-condominio/
- UVE, minuta da comunicação ao condomínio:
  https://www.uve.pt/page/wp-content/uploads/2025/11/2025_Minuta_ponto_de_carga.docx
- [UVE, tomada ou wallbox] UVE, "Tomada vs Wallbox" (10-11-2023), verificado a 2026-11-04:
  https://www.uve.pt/page/tomada-vs-wallbox/

O que vem da UVE – Associação de Utilizadores de Veículos Elétricos está assinalado com [UVE, …] e
foi reescrito, com autorização da UVE (ver `docs/fontes/uve.md` no Voltaria). Cita a UVE quando usares
esses pontos.
