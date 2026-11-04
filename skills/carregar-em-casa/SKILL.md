---
name: carregar-em-casa
description: Ajuda um condutor em Portugal a carregar o carro elétrico em casa ou na garagem do prédio, com tomada doméstica ou wallbox, em moradia ou condomínio, ligado ou não à MOBI.E, com ou sem painéis solares. Usa quando o utilizador pergunta como instalar, o que precisa, o que o condomínio pode recusar ou quanto custa carregar em casa.
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

### Wallbox

- Carrega mais depressa e com mais segurança do que a tomada doméstica. Permite programar o
  carregamento e, em muitos modelos, limitar a potência à que a casa tem livre (balanceamento
  dinâmico).
- A potência útil é a menor de três: a da wallbox, a do carregador de bordo do carro em AC, e a que
  a instalação e a potência contratada deixam livre. Não recomendes uma wallbox trifásica a quem tem
  contrato monofásico sem dizer que é preciso mudar o contrato.
- Aumentar a potência contratada aumenta o custo fixo da eletricidade. Diz isso, sem inventar
  valores.
- A instalação elétrica fica sujeita ao regime das instalações elétricas (DL 96/2017), através do
  DL 93/2025, art. 25.º, n.º 2: deve ser feita por um técnico certificado.

### Carregar com painéis solares

- Com autoconsumo, o carro pode carregar com o excedente solar durante o dia. Há wallboxes com modo
  solar que seguem a produção.
- Só compensa se o carro estiver em casa nas horas de sol. Se só estiver à noite, a tarifa de vazio
  conta mais do que os painéis.

## Num prédio (condomínio)

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
  do condomínio, precisa de maioria simples do valor total do prédio.
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
instalação da fração ou de um ponto de entrega próprio (CPE autónomo), nos termos que a ERSE
regulamenta (art. 24.º, n.º 3).

**O que levar à administração.** Ajuda o utilizador a escrever a comunicação: identificação do
condómino e do lugar, o equipamento e a potência, o percurso da cablagem pelas partes comuns, quem
instala (técnico certificado) e a data prevista, a pelo menos 30 dias.

## Ligado à MOBI.E ou não

- Até 31-12-2027, a plataforma da MOBI.E continua gerida pela EGME (DL 93/2025, art. 44.º, na
  redação do DL 155/2026). Um posto privado pode estar integrado nela ou não.
- **Sem integração**: o carro carrega com a eletricidade da casa, ao preço do contrato de
  eletricidade.
- **Integrado na MOBI.E**: o carregamento passa pela plataforma, sujeito à tarifa da EGME fixada
  pela ERSE, que deve vir discriminada na fatura se for repercutida (art. 44.º, n.º 4).
- Alguns apoios para postos em condomínio exigem a ligação à MOBI.E. Vê a skill `incentivos`.

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
