---
name: autonomia
description: "Ajuda um condutor a perceber e a aumentar a autonomia do carro elétrico: kW e kWh, consumo, autonomia anunciada (WLTP) e real, o que a reduz, climatização e travagem regenerativa. Usa quando o utilizador pergunta quantos quilómetros faz o carro, porque faz menos do que o anunciado, como poupar energia a conduzir ou como fazer as contas de autonomia."
---

# Autonomia e condução

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- Não dês de memória a autonomia, a capacidade útil nem o consumo de um carro. Procura a ficha da
  versão e do ano exatos, de preferência com consumos medidos em estrada (por exemplo, a EV
  Database) e não só o valor WLTP [UVE, manual].
- Não prometas quilómetros. Dá um intervalo e diz de que depende.
- Os números de exemplo desta skill servem para explicar as contas. Não são valores de nenhum carro.
- Para carregar, remete para as skills `carregamento-publico` e `carregar-em-casa`. Para cuidar da
  bateria, para a skill `baterias`.

## O que perguntar primeiro

Pergunta só o que não souberes, uma coisa de cada vez:

1. **Que carro**, versão e ano. Procura tu a capacidade útil e o consumo.
2. **Que percurso**: cidade, estrada ou autoestrada, e a velocidade habitual.
3. **Em que altura do ano**, ou com que temperatura. O frio e o calor pesam muito.
4. **Para que é a pergunta**: o dia a dia ou uma viagem concreta (de onde para onde).

## As contas

Muitos fabricantes e apps falam em quilómetros em vez de kW e kWh. Explica as unidades, que são
simples [UVE, manual]:

- **kW** é potência: a rapidez com que o posto dá energia ou o motor a gasta.
- **kWh** é energia: o que a bateria guarda e o que se paga. Potência vezes horas dá energia.
- **Consumo** é a energia gasta por distância, em kWh/100 km.
- **Autonomia aproximada** = capacidade útil (kWh) ÷ consumo (kWh/100 km) × 100. Por exemplo, 40 kWh
  com um consumo de 20 kWh/100 km dão cerca de 200 km; com 16 kWh/100 km, cerca de 250 km.
- Diz que é uma simplificação. No dia a dia não se anda de 100 % a 0 %: para a autonomia útil, conta
  só a faixa que o condutor usa (por exemplo, de 80 % a 10 %).
- Os "quilómetros por hora de carregamento" dependem do consumo do carro: o mesmo posto dá mais
  quilómetros a um carro mais eficiente. Por isso, para comparar postos, usa kW.

## Autonomia anunciada e real

- A autonomia que o fabricante anuncia vem do WLTP, um ensaio em laboratório: cerca de 23 km em 30
  minutos, a uma média de 46,5 km/h, com máximo de 131 km/h e cerca de 23 °C [UVE, manual].
- Por isso a autonomia real costuma ser menor, sobretudo em autoestrada e com frio. Explica isto sem
  dizer que o fabricante engana: o ensaio serve para comparar carros, não para prever uma viagem.

## Ciclos de homologação: WLTP, EPA e CLTC

### WLTP (Europa e outros mercados)

- **O que é**: Worldwide Harmonised Light Vehicles Test Procedure, o standard europeu (e de muitos
  outros mercados) desde 2019, que substituiu o NEDC.
- **Como funciona**: ensaio em laboratório, num dinamómetro, a 23 °C, sem passageiros nem
  acessórios, sem AC nem aquecimento. O ciclo dura 30 minutos e tem quatro fases de intensidade:
  baixa (até 60 km/h), média (até 80), alta (até 100) e extra-alta (acima de 130). O carro é
  conduzido por computador até a bateria esgotar.
- **Variantes**: o WLTP combina as fases numa única figura combinada; não publica cidade/autoestrada
  separadas como o EPA. A autonomia anunciada é o resultado desse ensaio.
- **Realidade**: costuma ser 10-30 % acima do uso real; com frio e autoestrada pode cair até 40 %.
  Serve para comparar carros, não para prever uma viagem.

### EPA (Estados Unidos)

- **O que é**: o ciclo da Environmental Protection Agency, o mais próximo do uso real.
- **Como funciona**: cinco ensaios — cidade (sem AC), autoestrada (sem AC), mais agressivo/alta
  velocidade (sem AC), quente (95 °F, AC a arrefecer), frio (20 °F, aquecimento/desembaciamento).
  O carro é conduzido até a bateria esgotar em ensaios de ciclo único (cidade e autoestrada) ou
  multi-ciclo (quatro cidade, dois autoestrada, dois velocidade constante).
- **Ajuste**: aplica um fator de 0,7 a todos os parâmetros (incluindo autonomia) para aproximar o
  uso real (condução agressiva, AC, frio).
- **Variantes**: cidade, autoestrada e combinada. A combinada é ponderada 55 % cidade e 45 %
  autoestrada. Apenas a combinada aparece na etiqueta.
- **Realidade**: é a mais realista das três; costuma diferir do uso real apenas alguns pontos
  percentuais.

### CLTC (China)

- **O que é**: China Light-duty Vehicle Test Cycle, o standard chinês.
- **Como funciona**: três fases — baixa velocidade (CLTC-P1), média (CLTC-P2) e alta (CLTC-P3) —,
  com 11 percursos curtos e 12 paragens, velocidade média de 29 km/h, máxima de 114 km/h e 22 %
  do tempo em ralenti.
- **Realidade**: é o mais otimista dos três; foca em trânsito urbano congestionado a baixa
  velocidade. Para uso em autoestrada, subtrai cerca de 30 % à figura CLTC.

### Conversão aproximada

- EPA → WLTP: multiplica por 1,12-1,15 (WLTP ≈ EPA × 1,14).
- CLTC costuma ser ~35 % acima do EPA e alguns pontos acima do NEDC (obsoleto).
- Estas conversões são regras de bolso; a diferença real varia por fabricante e modelo.

### Notas práticas

- A autonomia real depende de velocidade, temperatura, topografia, carga e estilo de condução.
  Alta velocidade aumenta a resistência do ar; o frio reduz a capacidade da bateria e o aquecimento
  consome energia; o calor obriga a arrefecer a bateria.
- A carga rápida abranda acima de ~80 %; para viagens, planeia paragens até 80 %.
- O WLTP, o EPA e o CLTC são ensaios de laboratório: úteis para comparar carros, não para prever
  uma viagem concreta.

## O que reduz a autonomia

Explica os fatores que contam para o caso do utilizador [UVE, manual]:

- **Velocidade**: acima de cerca de 100 km/h o consumo sobe muito. Em cidade, a velocidade baixa e
  a travagem regenerativa ajudam: é normal o carro fazer mais quilómetros em cidade do que em
  autoestrada.
- **Estilo de condução**: acelerações bruscas e travagens fortes gastam mais.
- **Percurso**: as subidas gastam muito; nas descidas o carro recupera parte da energia.
- **Climatização**: aquecer ou arrefecer o habitáculo gasta energia da bateria, mais ainda no frio.
- **Peso**: carga e passageiros aumentam o consumo.

## Como poupar energia

- **Climatizar com o carro ligado ao posto**: aquecer ou arrefecer antes de sair, com a energia da
  rede e não da bateria. Muitos carros deixam programar isto na app [UVE, manual].
- **Bancos e volante aquecidos**, se o carro os tiver, gastam menos do que aquecer o habitáculo todo
  [UVE, manual].
- **Antecipar as travagens**: tirar o pé do acelerador mais cedo deixa a travagem regenerativa
  devolver energia à bateria, e gasta menos os travões e os pneus [UVE, manual].
- **Modos de regeneração**: muitos carros têm um modo B, patilhas no volante ou condução com um só
  pedal, que travam mais com o motor [UVE, manual]. Procura como funcionam no carro do utilizador,
  e o que faz o modo ECO, se o tiver.
- Diz que a condução se adapta com o hábito: ao fim de alguns meses é normal gastar menos
  [UVE, manual].

## Viagens

- Planear com uma app de rotas para carros elétricos: com o carro e a carga à partida, indica onde
  parar, quanto tempo carregar e a carga prevista à chegada, e atualiza durante a viagem
  [UVE, manual].
- Se tiveres uma ferramenta de postos e preços (no ohmigo: `find_chargers`, `find_cheapest_charging`),
  usa-a para as paragens.
- Para a estratégia de carregamento na viagem (até que percentagem, que posto usar), ver a skill
  `carregamento-publico`.

## Para quem acabou de comprar

A UVE tem um manual para novos condutores com estas bases: unidades, autonomia, condução,
carregamento e bateria (ligação nas fontes). Podes recomendá-lo, avisando que é de julho de 2024:
a parte sobre como pagar é anterior ao DL 93/2025 e já não descreve o regime atual.

## Fontes

### Legislação

- Regulamento (UE) 2017/1151 (homologação WLTP — consumo, CO₂ e autonomia elétrica):
  https://eur-lex.europa.eu/eli/reg/2017/1151/oj
- Regulamento (UE) 2023/1804 (AFIR) — requisitos de informação ao utilizador nos postos:
  https://eur-lex.europa.eu/eli/reg/2023/1804/oj

### Normas e standards

- UNECE, Regulamento n.º 101 (consumo de energia e autonomia dos veículos elétricos) — lista das
  regulamentações UNECE: https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-101-120
- UNECE, GTR n.º 15 (WLTP — Worldwide harmonized Light vehicles Test Procedure), índice das
  Regulamentações Técnicas Globais:
  https://unece.org/transport/vehicle-regulations-wp29/standards/united-nations-global-technical-regulations

### Outras fontes

- EV Database — autonomia e consumo reais por modelo e versão: https://www.ev-database.org/

Da UVE – Associação de Utilizadores de Veículos Elétricos, verificado a 2026-11-04:

- [UVE, manual] "Parabéns! Comprou um veículo elétrico e agora?" (manual, jul. 2024), licença
  CC BY 4.0: https://www.uve.pt/page/wp-content/uploads/2025/01/2024_manual_me-UVE.pdf

O que vem da UVE está assinalado com [UVE, …]. O manual está sob CC BY 4.0 e foi adaptado, não
copiado (ver `docs/fontes/uve.md` no Voltaria). Cita a UVE quando usares esses pontos.
