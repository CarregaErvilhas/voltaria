---
name: tecnologia-de-carregamento
description: "Explica a tecnologia por trás da rede pública de carregamento: roaming e hubs de roaming, os protocolos OCPP e OCPI, Plug & Charge (ISO 15118) e a sua PKI, AutoCharge e baterias estacionárias (BESS) nos hubs de carregamento. Usa quando o utilizador pergunta como um cartão funciona em postos de outros operadores, o que é OCPP, OCPI, OICP ou um hub de roaming, como funciona o Plug & Charge, ou para que serve uma bateria num posto rápido."
---

# Tecnologia de carregamento

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- Esta skill é para perguntas técnicas: quem integra, opera ou estuda a rede. Para o condutor que
  só quer carregar e pagar, usa a skill `carregamento-publico`.
- Não dês contagens (postos, parceiros, países), quotas de mercado nem poupanças de memória. Mudam
  depressa e dependem de quem as publica. Se o utilizador as pedir, manda-o à fonte e diz a data.
- Não recomendes fornecedores nem fabricantes. Se o utilizador pedir exemplos, diz que a lista muda
  e que deve confirmar com o operador concreto.
- Diz a versão do protocolo ou da norma de que falas (OCPP 1.6 ou 2.0.1, ISO 15118-2 ou -20). O que
  vale para uma pode não valer para a outra.

## Roaming

- O **roaming** permite a um condutor com o cartão ou a app de um eMSP carregar num posto de um OPC
  com quem não tem contrato. O OPC e o eMSP trocam entre si a autorização, os dados da sessão e a
  faturação.
- O **OPC** opera os postos e o seu backoffice. O **eMSP** vende o cartão ou a app ao condutor e
  fatura-o. A mesma empresa pode ser OPC e eMSP.
- Cada OPC pode ligar-se a cada eMSP diretamente (peer-to-peer) ou através de um **hub de
  roaming**, que junta muitos numa só integração técnica e contratual.
- Hubs e plataformas que o utilizador pode referir:
  - **Hubject** (marca intercharge): hub europeu com o protocolo OICP; também suporta OCPI. Gere
    uma das raízes de confiança do Plug & Charge.
  - **Gireve**: hub francês, com o protocolo eMIP e OCPI.
  - **e-clearing.net**: hub com origem nos Países Baixos e na Alemanha, com OCHP e OCPI.
  - Plataformas de roaming gerido que assentam sobre os hubs e tratam de contratos, integração e
    liquidação por conta de OPC e eMSP.
  - **MOBI.E**: no regime antigo, a plataforma portuguesa liga CEME e OPC e funciona como hub
    nacional (ver a skill `regime-2010`).
- O pagamento ad hoc não depende do roaming: o AFIR obriga os postos públicos novos ou renovados a
  aceitá-lo.

## OCPP e OCPI

### OCPP (Open Charge Point Protocol)

- **O que é**: o protocolo aberto entre o posto e o sistema de gestão central do OPC (CSMS, o
  backoffice). Mantido pela Open Charge Alliance (OCA).
- **Versões**: 1.6, a mais instalada; 2.0.1, publicada também como norma IEC 63584; 2.1, que
  acrescenta a ISO 15118-20 e o carregamento bidirecional.
- **O que faz**: estado do posto, autorização das sessões, valores de medição, transações,
  atualização de firmware, diagnóstico e perfis de carga (carregamento inteligente).
- **Porque importa**: sem um protocolo comum, cada fabricante de postos usaria o seu e o OPC ficava
  preso a um fornecedor de backoffice.

### OCPI (Open Charge Point Interface)

- **O que é**: o protocolo aberto entre backoffices, de OPC para eMSP, diretamente ou através de um
  hub. Mantido pela EVRoaming Foundation, sob licença CC BY-ND 4.0.
- **Versões**: 2.1.1, 2.2.1 e 2.3.0. A 2.3.0 acrescenta o que o AFIR pede para os dados dos postos.
  Confirma na EVRoaming Foundation se já há uma versão mais recente.
- **O que faz**: localizações e disponibilidade em tempo real, tokens de autorização, sessões, CDR
  (registos de carregamento para faturar), tarifas, comandos remotos e carregamento inteligente.

### Como se relacionam

- O OCPP liga o backoffice aos postos; o OCPI liga backoffices entre si. São complementares.
- Um OPC usa o OCPP para gerir os seus postos e o OCPI para se ligar a eMSP e a hubs.
- Exemplo: um eMSP envia um limite de carga por OCPI ao backoffice do OPC, que o passa ao posto por
  OCPP.

## Plug & Charge (ISO 15118) e PKI

### O que é

- O **Plug & Charge** autentica o carro sozinho: o condutor liga o cabo e a sessão começa sem
  cartão, app nem QR code. A autorização e a faturação correm por trás, com certificados digitais.
- Assenta na **ISO 15118**, a comunicação entre o carro e o posto: a ISO 15118-2 é a que está
  instalada; a ISO 15118-20 acrescenta o carregamento bidirecional (V2G) e TLS 1.3.
- Usa uma **PKI** (infraestrutura de chave pública): cadeias de certificados X.509 que provam a
  identidade do carro e do contrato, assinadas por autoridades de certificação.

### Como funciona

- O carro guarda um **certificado de contrato**, emitido para o eMSP, e um certificado de
  aprovisionamento do fabricante do carro. Ao ligar, apresenta-o ao posto, que valida a cadeia até
  uma raiz V2G (V2G Root CA).
- Participam quatro PKI ligadas entre si: a do OPC, a do serviço de aprovisionamento de
  certificados (CPS), a do eMSP e a do fabricante do carro.
- O certificado de contrato pode ser instalado no posto, na primeira vez, ou pela telemática do
  fabricante.

### O que muda para o condutor

- Basta ligar o cabo. Só funciona se o carro, o posto e o eMSP suportarem Plug & Charge; senão,
  usa-se o cartão ou a app.
- Alguns carros aceitam vários certificados de contrato, de vários eMSP.

### Porque a adoção é lenta

- O fabricante do carro tem de pôr um módulo de segurança no carro, gerir certificados pela
  telemática e atualizar o software à distância para novas versões da ISO 15118.
- Fabricantes, OPC, eMSP e autoridades de certificação têm de se coordenar, e há várias raízes de
  confiança que nem sempre se reconhecem entre si.
- A maioria das sessões ainda usa cartão RFID ou app.

### AutoCharge

- O **AutoCharge** identifica o carro pelo identificador que este envia ao posto (EVCCID, muitas
  vezes o endereço MAC), sem certificados. É mais simples de pôr a funcionar, mas menos seguro:
  qualquer carro que envie o mesmo identificador é aceite.
- Para o condutor parece igual ao Plug & Charge. Só alguns OPC o oferecem, e é preciso ativá-lo na
  app.

### Outras formas de autenticar

- Cartão RFID ou NFC, a mais comum.
- App ou QR code do eMSP ou do OPC.
- Pagamento ad hoc com cartão bancário.

### Normas e regras

- **AFIR** (Regulamento (UE) 2023/1804): exige interoperabilidade e acesso não discriminatório, e
  remete a comunicação entre o carro e o posto para a ISO 15118.
- **DL 93/2025, art. 6.º**: os postos instalados ou renovados têm de permitir o carregamento ad hoc
  e inteligente; as normas de comunicação para o bidirecional são as do AFIR.
- **VDE-AR-E 2802-100-1** (Alemanha): regra de aplicação para gerir os certificados da ISO 15118.
- **CharIN**: associação que promove a interoperabilidade e publica guias sobre a PKI.

## BESS (baterias estacionárias)

### O que é

- Um **BESS** (Battery Energy Storage System) é uma bateria fixa instalada junto do posto. Carrega
  da rede ou de produção renovável local e descarrega para os carregadores ou para serviços de rede.
- Deixa o posto entregar mais potência do que a ligação à rede permite, sem reforçar o ramal.

### Para que serve

- **Cortar picos (peak shaving)**: os postos rápidos têm picos de potência altos e imprevisíveis, e
  a potência contratada paga-se por esses picos. O BESS descarrega nos picos e baixa a potência
  pedida à rede.
- **Ganhar tempo**: permite instalar mais carregadores, ou mais potentes, sem esperar por um
  reforço da rede, que pode levar meses ou anos.
- **Apoiar a rede**: amortece variações no ponto de ligação e pode vender flexibilidade (reserva de
  frequência, deslocação de consumo) ou fazer arbitragem de preços, conforme o mercado.
- **Reserva**: em alguns casos alimenta o posto durante uma falha da rede.

### O que dizer

- A poupança e o retorno dependem do perfil de uso do hub, das tarifas de potência e dos serviços de
  rede disponíveis em cada país. Não dês percentagens nem prazos de retorno de memória.
- Um BESS subdimensionado esgota-se nos picos e deixa de cortar a potência. O dimensionamento é
  estudo de cada caso.
- Para saber se um posto concreto tem BESS, só o OPC confirma.

## Fontes

### Legislação

- Regulamento (UE) 2023/1804 (AFIR): https://eur-lex.europa.eu/eli/reg/2023/1804/oj
- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica), art. 6.º:
  https://data.dre.pt/eli/dec-lei/93/2025/08/14/p/dre/pt/html

### Normas e standards

- OCPP (Open Charge Point Protocol, posto ↔ backoffice; IEC 63584), Open Charge Alliance:
  https://openchargealliance.org/protocols/ocpp-protocols/
- OCPI (Open Charge Point Interface, roaming entre operadores), EVRoaming Foundation:
  https://evroaming.org/ocpi-background/
- ISO 15118-2 (comunicação carro-posto, Plug & Charge): https://www.iso.org/standard/55366.html
- ISO 15118-20 (comunicação carro-posto, bidirecional e V2G): https://www.iso.org/standard/77845.html
- OICP (Open InterCharge Protocol, Hubject): https://www.hubject.com/en/
- eMIP (protocolo de roaming da Gireve): https://www.gireve.com/en/

### Outras fontes

- CharIN: https://www.charin.global/
