---
name: carregar-em-casa
description: "Ajuda um condutor em Portugal a carregar o carro elétrico em casa ou na garagem do prédio, com tomada doméstica ou wallbox, em moradia ou condomínio, ligado ou não à MOBI.E, com ou sem painéis solares. Usa quando o utilizador pergunta como instalar, o que precisa, o que o condomínio pode recusar ou quanto custa carregar em casa."
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
- A instalação elétrica fica sujeita ao regime das instalações elétricas (DL 96/2017), através do
  DL 93/2025, art. 25.º, n.º 2: deve ser feita por um técnico certificado. O técnico deve seguir o
  Guia Técnico das Instalações Elétricas para a Alimentação de Veículos Elétricos da DGEG, 3.ª
  edição, de 2023 (ligação nas fontes).

### EVSE móvel vs. wallbox

- **EVSE móvel (carregador portátil)**: um cabo com eletrónica de segurança que liga uma tomada
  (doméstica Schuko ou industrial CEE) ao carro. Não é uma tomada "burra": tem proteção contra
  sobrecorrente, deteção de fuga de corrente e controlo do arranque. É o que vem com muitos carros
  (cabo ocasional). Limita-se à potência da tomada (até 3,7 kW numa Schuko, até 22 kW numa CEE
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

- A tomada doméstica habitual em Portugal é a **Schuko (Tipo F)**, 230 V, 16 A. Com o cabo
  ocasional do carro, dá cerca de 2,3 kW (10 A) a 3,7 kW (16 A), conforme o cabo e o circuito.
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

## Num prédio (condomínio)

**Quando não é preciso falar com o condomínio.** Numa moradia, ou numa garagem ligada diretamente
à instalação elétrica da fração, sem passar por partes comuns, não há nada a comunicar ao
condomínio [UVE, casa ou condomínio].

**Prédios novos.** As construções novas em propriedade horizontal, ou com estacionamento, têm de
incluir uma infraestrutura elétrica adequada para carregar veículos, com uma potência mínima fixada
em portaria. Isto não inclui os postos nem as tomadas (DL 93/2025, art. 22.º). A regra antiga, para
licenciamentos desde 1-7-2010, pedia também que cada lugar ficasse preparado para um posto ou uma
tomada: vê a skill `regime-2010`. Não digas que um prédio novo já tem ligação em cada lugar sem o
utilizador o confirmar com o administrador ou o projeto.

Qualquer condómino pode instalar, à sua custa, um posto de carregamento no seu lugar de
estacionamento, desde que o lugar cumpra os requisitos técnicos definidos em portaria (DL 93/2025,
art. 23.º, n.º 1). O mesmo vale para uma tomada.

**Comunicação prévia.** Se a instalação estiver numa parte comum do prédio, ou passar por ela, mesmo
que seja de uso exclusivo do condómino, é obrigatório comunicar por escrito à administração do
condomínio (e ao proprietário, se for arrendatário) com **pelo menos 30 dias** de antecedência sobre
a data da instalação (art. 23.º, n.º 2).

**Quando o condomínio se pode opor.** Só nestes casos (art. 23.º, n.º 3):

- a) o condomínio instala, **no prazo de 90 dias**, um ou mais postos partilhados que deem os mesmos
  serviços, a mesma tecnologia e cubram as necessidades de todos os potenciais utilizadores;
- b) o prédio já tem um posto ou tomada partilhada nessas condições;
- c) a instalação põe comprovadamente em risco a segurança de pessoas ou bens, com parecer técnico
  entregue à administração;
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

- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica):
  https://diariodarepublica.pt/dr/detalhe/decreto-lei/93-2025-928937303
- Decreto-Lei n.º 155/2026, de 31 de julho (prorroga o período transitório até 31-12-2027):
  https://files.diariodarepublica.pt/1s/2026/07/14700/0003200033.pdf
- DGEG, Guia Técnico das Instalações Elétricas para a Alimentação de Veículos Elétricos, 3.ª edição
  (2023-09-14): https://www.dgeg.gov.pt/media/5adbxzxo/guia-ve-ed-3-2023.pdf
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
