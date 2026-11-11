---
name: tarifas-de-acesso
description: "Explica as tarifas de acesso às redes (TAR) para quem opera ou detém postos de carregamento em Portugal: a TAR da mobilidade elétrica (TAR ME) da rede MOBI.E, só com preços por kWh; as TAR normais em BTN, BTE e MT, com potência contratada pela máxima potência tomada em 15 minutos nos últimos 12 meses e potência em horas de ponta; o que muda para os OPC quando os postos saem da MOBI.E, até 31-12-2027; o impacto nos postos com pouca utilização e as formas de o reduzir; as TAR do sub-CPE. Usa quando um OPC, um DPC ou um gestor de frota pergunta quanto vai pagar de rede, porque um posto rápido com pouco uso vai custar mais depois de 2027, ou como baixar a potência contratada."
---

# Tarifas de acesso às redes

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- **Os preços vêm dos factos** (no ohmigo: `ev_rules_portugal` com `topic: "incentives"` e
  uma `query`, entradas `kind: "mercado"` com `series: "tar"`), com o ano. A ERSE fixa as TAR todos os anos, em dezembro, para o
  ano seguinte. Não dês preços de memória e diz sempre de que ano são.
- **A TAR é só a parte da rede.** O OPC paga ainda a energia e a margem do comercializador, e os
  impostos. Não apresentes a TAR como o custo total da eletricidade do posto.
- **Os documentos da ERSE de 2025 falam de um período transitório até 31-12-2026.** O DL 155/2026
  alargou-o até 31-12-2027. Usa 2027.
- **As contas de impacto são estimativas.** Diz os pressupostos (potência de pico, kWh por mês, parte
  do consumo em horas de ponta) e que o valor real depende do ciclo, da opção tarifária e do
  comercializador. Não dês conselhos de investimento: mostra a conta e o que a faz mudar.
- O condutor não paga a TAR à parte fora da MOBI.E: está dentro do preço do OPC ou do eMSP. Esta
  skill é para quem opera ou detém postos. Para o condutor, usa `carregamento-publico`.

## O que perguntar primeiro

1. **O posto está integrado na MOBI.E ou não**, e se vai sair antes do fim do período transitório.
2. **O nível de tensão da ligação**: BTN (até 41,4 kVA), BTE (BT acima de 41,4 kVA) ou MT (posto de
   transformação próprio).
3. **A potência dos postos** e se há gestão de potência ou bateria (BESS).
4. **Quantos kWh vende por mês**, e a que horas: o consumo em horas de ponta pesa muito.
5. Se o posto tem uma ligação só para ele ou está numa instalação com outros consumos (uma loja, um
   condomínio, uma empresa), eventualmente com sub-CPE.

## O que é a TAR

- A tarifa de acesso às redes paga o uso das redes de transporte e de distribuição e os custos de
  política energética (CIEG). A ERSE fixa-a todos os anos, por nível de tensão (Regulamento
  Tarifário). O ORD fatura-a ao comercializador, que a repercute na fatura do cliente.
- Tem até quatro termos, conforme o nível de tensão (Regulamento Tarifário, arts. 44.º, 45.º, 52.º e
  54.º):

| Termo | BTN | BTE e MT |
|---|---|---|
| Potência contratada (por dia) | Escalão escolhido no contrato | **Máxima potência tomada nos últimos 12 meses**, incluindo o mês da fatura |
| Potência em horas de ponta (por kW e por dia) | Não tem | Energia em horas de ponta ÷ horas de ponta do período |
| Energia ativa (por kWh, por período horário) | Sim | Sim |
| Energia reativa | Não | Sim |

- **Potência tomada**: o maior valor da potência ativa média em qualquer período ininterrupto de 15
  minutos (Regulamento Tarifário, art. 44.º). Um só quarto de hora a plena potência num mês fixa a
  potência contratada para os 12 meses seguintes. Uma sessão curta conta pela média desses 15
  minutos, não pelo pico instantâneo.
- **Horas de ponta**: no ciclo semanal do continente, 5 h por dia útil na hora legal de inverno e 3
  h na de verão, sem ponta aos fins de semana. No ciclo diário, 4 h por dia todos os dias
  (Regulamento Tarifário, Quadro 8). O preço por kW da potência em horas de ponta é muito mais alto
  do que o da potência contratada (ver os factos).
- Em BTE não há escalões: pode contratar-se qualquer potência acima de 41,4 kVA. A potência
  contratada não pode passar a potência requisitada da ligação [E-REDES, manual de ligações].

## A TAR da mobilidade elétrica (modelo MOBI.E)

- Nos postos integrados na rede MOBI.E, a energia dos carregamentos paga uma TAR própria, a TAR da
  mobilidade elétrica, **só com preços por kWh**, em opção bi-horária ou tri-horária. Não tem
  potência contratada nem potência em horas de ponta (Regulamento Tarifário, arts. 57.º e 58.º).
- A ERSE converte os preços de potência da TAR em BTN em preços por kWh, por período horário, com
  base no perfil de consumo da rede de mobilidade elétrica. Justifica-o por a carga (os carros)
  variar no tempo e no espaço. Há quatro variantes, conforme o nível de tensão da ligação do posto
  (BT, MT, AT, MAT): todas partem da TAR em BTN, e as de tensão mais alta tiram o uso das redes que
  não usam [ERSE, estrutura tarifária 2026].
- O ORD fatura a TAR ME ao comercializador que abastece o CEME (Regulamento n.º 7/2026, art. 10.º),
  e o CEME repercute-a na fatura do condutor, à parte da tarifa do OPC.
- **O que isto dá ao OPC**: o custo fixo da rede de um posto MOBI.E é pago pelo condutor, por kWh. Um
  posto rápido que quase não é usado não paga a potência que tem. O custo da rede só existe quando há
  carregamentos.
- A TAR ME só se aplica durante o período transitório e só às entregas dos CEME em postos que
  continuem integrados na MOBI.E [ERSE, estrutura tarifária 2026]. O DL 93/2025 não prevê uma TAR
  própria para os postos fora da MOBI.E. Até 2026-11-06 não encontrámos nenhuma proposta da ERSE
  nesse sentido; se o utilizador falar de uma, pede a fonte.

## Fora da MOBI.E e depois de 2027

- O OPC contrata a eletricidade do posto a um comercializador, como qualquer instalação de consumo
  (DL 93/2025, art. 9.º), e paga a TAR normal do nível de tensão. É o que acontece já hoje a quem
  desintegra o posto da MOBI.E, e a todos a partir de 1-1-2028.
- **Em BTN** (postos AC até 41,4 kVA no total), o termo de potência é o do escalão escolhido. É um
  custo fixo conhecido, que se pode baixar mudando de escalão.
- **Em BTE e MT** (postos DC, parques com muitos postos), entram os dois termos de potência:
  - **potência contratada**: o maior quarto de hora dos últimos 12 meses. Num posto de 150 kW que
    chegue uma vez aos 150 kW em média de 15 minutos, paga-se 150 kW por dia durante um ano, haja
    carregamentos ou não;
  - **potência em horas de ponta**: cada kWh vendido nas horas de ponta pesa muito, porque o preço
    por kW é várias vezes o da potência contratada.
- O custo fixo da rede passa do condutor (por kWh) para o OPC (por kW). O OPC tem de o recuperar no
  preço que cobra, e num posto com poucos carregamentos isso dá muito por kWh.

### Impacto nos postos com pouca utilização

A conta, para um mês de 30 dias em BTE ou MT, com os preços dos factos:

- termo fixo = potência contratada (kW) × preço da potência contratada × 30;
- potência em horas de ponta = (kWh em horas de ponta ÷ horas de ponta do mês) × preço da potência em
  horas de ponta × 30;
- energia = kWh de cada período × preço da energia ativa desse período;
- custo de rede por kWh = soma dos três ÷ kWh vendidos no mês.

Compara com a TAR ME: kWh de cada período × preço da TAR ME desse período.

- O termo fixo não depende dos kWh. **Abaixo de um certo consumo mensal, a TAR normal sai mais cara
  por kWh do que a TAR ME, e quanto menos uso, pior.** Acima desse consumo, a TAR normal pode até
  sair mais barata, porque a energia ativa em BTE e MT é mais barata do que a TAR ME por kWh.
- Os factos têm um exemplo calculado pelo Voltaria (posto de 150 kW em BTE, preços de 2026), com o
  ponto de equilíbrio. Usa-o como ordem de grandeza e refaz a conta com os números do utilizador.
- Quem mais sente a mudança: postos rápidos em locais de passagem rara, postos de redes municipais
  ou de cobertura (instalados para cumprir metas, não pela procura), e parques com muitos postos
  ligados a uma só ligação em BTE ou MT que raramente estão todos ocupados.

### Formas de baixar o custo

Diz o que cada uma faz, sem recomendar uma em concreto:

- **Limitar a potência** com gestão de carga (OCPP, carregamento inteligente): o que conta é a média
  de 15 minutos na ligação, por isso limitar o total do parque baixa a potência contratada para os
  12 meses seguintes. Ver `tecnologia-de-carregamento`.
- **Bateria (BESS) para cortar picos**: a bateria fornece os picos e a rede vê uma potência menor.
  Ver `tecnologia-de-carregamento`.
- **Fugir às horas de ponta**: preços mais altos ou limitação de potência nessas horas baixam a
  potência em horas de ponta.
- **Ficar na MOBI.E até ao fim do período transitório** (31-12-2027), enquanto a TAR ME existir.
- **Juntar o posto a uma instalação com outros consumos** (por exemplo, um supermercado): o termo
  fixo é partilhado, mas o pico do posto soma-se ao da instalação, e a potência tomada é a do total.
- Num posto em BTN, escolher o escalão pelo uso real e não pela potência máxima dos postos.
- Um aviso: mudar para um escalão ou potência mais baixa sem limitar a potência dos postos não
  resolve nada. Em BTE e MT, a potência contratada volta a subir com o primeiro pico.

## Sub-CPE (ponto de entrega interno)

- O ponto de entrega interno paga **todos os termos da TAR**, menos a energia reativa, ao nível de
  tensão da instalação onde está (Regulamento n.º 7/2026, art. 99.º). Em BTE e MT, a potência
  contratada é a máxima potência tomada medida no ponto interno; em BTN, é o escalão contratado com o
  comercializador do sub-CPE, que não pode ser superior ao da instalação principal.
- A instalação principal paga a TAR sobre o consumo por diferença (ponto de medição virtual). Em
  BTN, o escalão da instalação principal fica no escalão igual ou logo acima da máxima potência
  tomada desse ponto virtual nos últimos 12 meses (art. 98.º).
- Ou seja: o sub-CPE não foge ao termo de potência. A proposta da ERSE de 2025 previa que o ponto
  interno pagasse só a energia e a potência em horas de ponta, mas o texto aprovado não ficou assim.
  Se alguém citar a proposta, corrige.
- Para o processo do sub-CPE, usa `sub-cpe`.

## Como responder

1. Diz em que regime está o posto (MOBI.E com TAR ME, ou TAR normal) e o nível de tensão.
2. Explica que termos paga e o que os faz subir (o pico de 15 minutos, os kWh em horas de ponta).
3. Se pedirem o impacto, faz a conta com os preços dos factos e os números do utilizador, mostra os
   pressupostos e o ponto de equilíbrio.
4. Termina com a fonte e o ano dos preços.

## Fontes

### Legislação

- Regulamento n.º 1218/2025, de 7 de novembro (ERSE; Regulamento Tarifário do setor elétrico; arts.
  44.º, 45.º, 52.º, 54.º, 57.º e 58.º, Quadro 8):
  https://diariodarepublica.pt/dr/detalhe/regulamento/1218-2025-944873898
- Regulamento n.º 7/2026, de 6 de janeiro (ERSE; Regulamento da Mobilidade Elétrica; arts. 10.º, 98.º
  e 99.º): https://diariodarepublica.pt/dr/detalhe/regulamento/7-2026-994000576
- Decreto-Lei n.º 93/2025, de 14 de agosto (mobilidade elétrica; arts. 9.º e 44.º):
  https://data.dre.pt/eli/dec-lei/93/2025/08/14/p/dre/pt/html
- Regulamento (UE) 2023/1804 (AFIR): https://eur-lex.europa.eu/eli/reg/2023/1804/oj

### Normas e standards

- IEC 61851-1 (sistema de carregamento condutivo; a gestão de potência do posto):
  https://webstore.iec.ch/en/publication/33644
- OCPP 2.0.1 (carregamento inteligente e limites de potência): https://openchargealliance.org/protocols/open-charge-point-protocol/

### Outras fontes

Verificadas a 2026-11-06:

- [ERSE, estrutura tarifária 2026] ERSE, "Estrutura tarifária do setor elétrico em 2026", secções 2.6
  e 3.4: https://www.erse.pt/media/lipjxgih/estrutura-tarif%C3%A1ria-se-2026.pdf
- ERSE, Diretiva n.º 10/2025 (tarifas e preços da energia elétrica para 2026; TAR no art. 15.º e
  TAR ME no art. 23.º): https://www.erse.pt/media/lamnmp31/diretiva-erse-10-2025-tep-se-2026.pdf
- Texto consolidado do Regulamento Tarifário publicado pela ERSE (janeiro de 2026):
  https://www.erse.pt/media/5ewbseeb/articulado_rt-se_publicado-dr-com-dretif.pdf
- [E-REDES, manual de ligações] E-REDES, Manual de Ligações à Rede Elétrica de Serviço Público (11.ª
  edição): https://www.e-redes.pt/sites/eredes/files/2026-01/Manual%20Ligaco%CC%83es%20a%CC%80%20Rede%20Revisto_11_%20Edica%CC%83o_2025_26Dez.pdf
