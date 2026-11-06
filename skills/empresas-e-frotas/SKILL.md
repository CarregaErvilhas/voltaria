---
name: empresas-e-frotas
description: "Ajuda empresas, trabalhadores independentes e gestores de frota em Portugal com carros elétricos: vantagens fiscais (IVA, depreciações e tributação autónoma até ao limite de custo da portaria, sem IVA, IUC, ISV), o que não é dedutível (carregadores, despesas de utilização), e como carregar a frota nas instalações, na rede pública e em casa de quem conduz, com a empresa como DPC e um sub-CPE em nome da empresa. Usa quando o utilizador pergunta se compensa a empresa ter um elétrico, se pode deduzir o IVA do carro, da wallbox ou da eletricidade, ou como pagar o carregamento em casa do colaborador."
---

# Empresas e frotas

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- **Não dês aconselhamento fiscal.** Explica a regra, cita o artigo ou a informação vinculativa da
  AT, e diz para confirmar com o contabilista certificado antes de decidir. As informações
  vinculativas respondem a um caso concreto: valem como posição da AT, não como lei.
- **Os valores vêm dos factos** (no ohmigo: `get_facts` com `topic: "incentivos"`), com a fonte e a
  data. Não dês taxas nem limites de memória.
- **Pergunta se a empresa tem direito à dedução do IVA.** Uma atividade isenta (por exemplo, boa
  parte da saúde, do ensino e dos seguros) não deduz IVA, e as regras do IVA abaixo não se aplicam.
- Esta skill junta o que está espalhado: os factos fiscais de `incentivos`, as regras de quem tem o
  posto (DPC) de `carregar-em-casa` e o contador próprio de `sub-cpe`. Para o pormenor, remete para
  essas skills.
- O carregamento em casa do colaborador com sub-CPE em nome da empresa (mais abaixo) é uma leitura
  das regras da ERSE e da AT, não uma solução que alguma delas tenha descrito. Apresenta-o assim e
  manda confirmar com o operador de rede e com o contabilista.

## O que perguntar primeiro

Pergunta só o que não souberes, uma coisa de cada vez:

1. **Que entidade**: sociedade, trabalhador independente com contabilidade organizada, IPSS, ou
   autarquia. E se tem direito à dedução do IVA.
2. **Compra, locação financeira ou renting.** Muda quem deduz o quê, e de que fatura.
3. **100 % elétrico ou híbrido plug-in.** Os limites e as regras não são os mesmos.
4. **Onde vai carregar**: nas instalações da empresa, na rede pública, em casa de quem conduz.
5. **Uso pessoal**: se quem conduz leva o carro para casa e o usa fora do trabalho.

## As vantagens fiscais

Os valores estão nos factos; aqui fica o que cada um quer dizer para a empresa.

- **O limite de custo de aquisição**, sem IVA, para os carros ligeiros de passageiros 100 %
  elétricos (Portaria n.º 467/2010, alterada pela Lei n.º 82-D/2014; o valor está no facto
  `limite-custo-viaturas-eletricas-62500`). É o mesmo limite para três coisas:
  - **IVA da compra ou da locação**: dedutível se o custo de aquisição ficar dentro do limite. Acima
    dele, a AT considera que nenhuma parte é dedutível, não só o excesso (facto
    `limite-custo-viaturas-eletricas-62500`).
  - **Depreciações em IRC**: aceites até ao limite; o que passar dele não conta (Código do IRC, art.
    34.º, n.º 1, e)).
  - **Tributação autónoma**: os encargos com um 100 % elétrico dentro do limite não pagam; acima,
    pagam a taxa do facto `irc-tributacao-autonoma-eletricos`.
- **Híbridos plug-in** têm um limite e regras de tributação autónoma próprios. Usa os factos e, se
  não estiverem lá, manda confirmar na portaria e no Código do IRC.
- **IUC**: os 100 % elétricos estão isentos. **ISV**: estão fora do imposto, o que conta ao importar
  um elétrico usado.
- **Eletricidade**: o IVA da eletricidade usada nos elétricos e híbridos plug-in é dedutível, com
  fatura em nome da empresa (Código do IVA, art. 21.º, n.º 2, h)).

### O que não é dedutível

- **O IVA dos carregadores.** Segundo a AT, o IVA da compra e da instalação de uma wallbox para as
  viaturas da empresa não é dedutível, por ser uma despesa de utilização das viaturas (facto
  `iva-carregadores-nao-dedutivel`). Muita gente assume o contrário: diz-lho antes de fazer contas.
- **As despesas de utilização**: reparação, manutenção, portagens e seguros. A exceção do IVA é só
  para a compra e para a eletricidade.
- **O uso pessoal.** Se a viatura for usada fora da atividade, há IVA a liquidar sobre esse uso. Em
  IRS, o uso pessoal de uma viatura da empresa pode contar como rendimento em espécie de quem a
  conduz. Não conhecemos uma regra própria para os elétricos: manda confirmar com o contabilista.

### Apoios à compra

- Os avisos do Fundo Ambiental dizem quem pode candidatar-se em cada edição; nem todas abrangem
  empresas. Usa os factos da edição em causa.
- O Plano Social para o Clima prevê apoio a microempresas dos setores mais expostos ao custo dos
  combustíveis para eletrificar as frotas. Está anunciado, não aberto (facto
  `psc-mobilidade-microempresas`; ver `incentivos`).

## Carregar a frota

### Nas instalações da empresa

- A empresa é a DPC do posto, se o posto não for acessível ao público (DL 93/2025, art. 21.º). Um
  parque só para colaboradores ou clientes continua privado. Se o abrir ao público em geral, passa a
  ser um posto público e a empresa precisa de licença de OPC (ver `afir` e `carregar-em-casa`).
- A eletricidade vem na fatura da empresa: o IVA dela é dedutível. O IVA do posto não é.
- A instalação segue o Guia Técnico da DGEG para zonas de carregamento partilhadas (ver
  `instalacao-eletrica`).

### Na rede pública

- Cartão ou app de um OPC ou de um eMSP em nome da empresa, com faturas em nome da empresa. Até
  31-12-2027, também um cartão de CEME na MOBI.E.
- Pergunta ao contabilista se a fatura de carregamento do OPC ou do eMSP conta como "eletricidade
  utilizada" para o IVA. A AT fala da eletricidade; a fatura do carregamento pode juntar serviços.

### Em casa de quem conduz

O problema é a fatura: o IVA da eletricidade carregada em casa do colaborador só é dedutível se a
fatura estiver em nome da empresa (facto `iva-eletricidade-casa-colaborador`). Há três maneiras de
fazer as coisas:

1. **Reembolso ao colaborador.** O consumo fica no contrato da casa e a empresa paga ao colaborador
   o que o carro gastou, medido pelo contador da wallbox. É o modelo acordado (ver `sub-cpe`). É o
   mais simples, mas a empresa não deduz o IVA, porque a fatura está em nome do colaborador. O
   tratamento do reembolso em IRC e IRS é com o contabilista.
2. **A empresa como DPC, com sub-CPE em nome da empresa.** A empresa compra e instala a wallbox em
   casa do colaborador e fica a ser a DPC desse posto. Como DPC, pode pedir ao operador de rede um
   ponto de entrega interno (sub-CPE), com autorização escrita do titular do contrato da casa
   (GMLDD, art. 11.º-A, n.os 1 e 2), e contratar a eletricidade desse ponto em nome da empresa. A
   fatura do sub-CPE fica em nome da empresa, que é a condição que a AT põe para deduzir o IVA. O
   resto do consumo da casa continua no contrato do colaborador.
3. **Posto integrado na MOBI.E**, com cartão de CEME da empresa, enquanto durar o período
   transitório (até 31-12-2027). A fatura do CEME vem em nome da empresa. Acaba com o fim do regime
   antigo.

Para a opção 2, diz também o que custa e o que limita:

- Há o preço regulado do contador, a adaptação da instalação, a certificação e um termo fixo novo
  na fatura do sub-CPE. Compensa mais com muitos quilómetros por mês; para pouco uso, o reembolso
  costuma chegar. Não faças a conta de memória: depende dos preços do caso.
- O sub-CPE não dá mais potência do que a da casa, e um corte no contrato da casa corta o posto.
  O operador de rede tem até dois meses para instalar o contador (ver `sub-cpe`).
- Num prédio, a instalação no lugar de garagem continua a precisar da comunicação prévia ao
  condomínio (DL 93/2025, art. 23.º), e o titular que autoriza o sub-CPE depende do quadro de onde
  sai o posto: o colaborador, se sair da fração; o condomínio, se sair dos serviços comuns (ver
  `carregar-em-casa` e `instalacao-eletrica`).
- Combina, por escrito, de quem é o posto e o que acontece quando o colaborador sai da empresa ou
  muda de casa: retirar o posto, vendê-lo ao colaborador, e terminar o contrato do sub-CPE.
- Num posto integrado na MOBI.E na mesma instalação, criar um sub-CPE obriga a desintegrar todos os
  postos dessa instalação da plataforma da EGME (ver `sub-cpe`).

## Como responder

1. Diz que regra se aplica e de onde vem (artigo, portaria ou informação vinculativa, com a data).
2. Separa o que é dedutível do que não é: carro, eletricidade, posto e despesas de utilização.
3. Para o carregamento em casa, compara as três maneiras pelo que importa à empresa: IVA,
   simplicidade e custo fixo.
4. Termina com a fonte, a data e "confirma com o contabilista".

## Fontes

### Legislação

- Portaria n.º 467/2010, de 7 de julho (limites do custo de aquisição das viaturas):
  https://data.dre.pt/eli/port/467/2010/07/07/p/dre/pt/html
- Lei n.º 82-D/2014, de 31 de dezembro (fiscalidade verde; art. 24.º altera a Portaria n.º
  467/2010): https://data.dre.pt/eli/lei/82-d/2014/12/31/p/dre/pt/html
- Código do IVA, art. 21.º (exclusões do direito à dedução), no Portal das Finanças:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva21.aspx
- Código do IRC, art. 88.º (tributação autónoma), no Portal das Finanças:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx
- Lei n.º 22-A/2007, de 29 de junho (Código do ISV, art. 2.º, e Código do IUC):
  https://data.dre.pt/eli/lei/22-a/2007/06/29/p/dre/pt/html
- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica), arts. 21.º e
  23.º: https://data.dre.pt/eli/dec-lei/93/2025/08/14/p/dre/pt/html
- Regulamento n.º 8/2026, de 6 de janeiro (ERSE; altera o Guia de Medição, Leitura e
  Disponibilização de Dados, onde está o art. 11.º-A sobre o ponto de entrega interno):
  https://diariodarepublica.pt/dr/detalhe/regulamento/8-2026-994000577

### Normas e standards

- IEC 61851-1 (sistema de carregamento condutivo): https://webstore.iec.ch/en/publication/33644
- ISO 15118-2 (Plug & Charge, útil em frotas para identificar o carro sem cartão):
  https://www.iso.org/standard/55366.html

### Outras fontes

Da Autoridade Tributária, informações vinculativas, verificadas a 2026-11-06:

- Processo 28949 (2025-10-31), IVA na compra de uma viatura 100 % elétrica e o limite da portaria,
  sem IVA:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/despesa/civa/Documents/PIV_28949.pdf
- Processo 24830 (2023-10-27), IVA dos carregadores e da eletricidade:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/despesa/civa/Documents/PIV_24830.pdf
- Processo 25928 (2024-04-30), eletricidade gasta em casa dos colaboradores:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/despesa/civa/Documents/PIV_25928.pdf
