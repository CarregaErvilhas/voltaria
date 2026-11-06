---
name: instalacao-eletrica
description: "Explica as regras técnicas da instalação elétrica para carregar um carro elétrico em Portugal, segundo o Guia Técnico da DGEG (3.ª edição, 2023) e as RTIEBT (secção 722): modos de carga, circuito dedicado, disjuntor e diferencial, tomadas e fichas, de que quadro se alimenta o lugar (quadro de entrada, quadro de colunas, serviços comuns), potência mínima nos parques dos prédios, corte de emergência, proteção à água e ao choque, e ligação à terra. Usa quando o utilizador vai instalar uma tomada ou uma wallbox, quer saber o que pedir ou verificar ao eletricista, que diferencial e que cabo são precisos, ou como se alimenta um lugar na garagem de um prédio."
---

# Instalação elétrica para carregar

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- **O guia é orientador.** O Guia Técnico da DGEG, da comissão CTE 64, interpreta as RTIEBT (Regras
  Técnicas das Instalações Elétricas de Baixa Tensão, Portaria n.º 949-A/2006, com a secção 722
  aditada pela Portaria n.º 252/2015). O que obriga são as RTIEBT e a lei; o guia diz como as
  aplicar. Cita a secção do guia [DGEG, guia técnico, …] e, quando o guia a indica, a das RTIEBT.
- **Quem projeta e executa é o técnico.** Explica o que a instalação tem de cumprir, para o
  utilizador saber o que pedir e o que verificar. Não dês instruções para o utilizador fazer
  ligações elétricas, nem confirmes que uma instalação concreta está conforme: isso é do técnico
  responsável ou da entidade instaladora (ver `carregar-em-casa`, "Quem instala e que papéis
  pedir").
- **O guia é de 2023, anterior ao DL 93/2025.** Algumas referências legais estão desatualizadas
  (ver "O que está desatualizado no guia"). As regras técnicas mantêm-se. A Portaria n.º 128/2026/1
  (art. 3.º, n.º 4) prevê um guia novo; se a página da DGEG já tiver uma edição mais recente, usa
  essa e diz que esta skill pode estar desatualizada.
- Para o condomínio, os papéis e quem opera o posto, usa `carregar-em-casa`; para separar o
  consumo com contador próprio, `sub-cpe`.
- Os valores técnicos abaixo (secções, correntes, alturas, códigos IP e IK) são regras do guia, não
  preços nem estimativas: podes dá-los, sempre com a secção.

## O que perguntar primeiro

Pergunta só o que não souberes, uma coisa de cada vez:

1. **Onde fica o lugar**: moradia, garagem fechada (boxe) num prédio, lugar marcado no chão de uma
   garagem comum, ou zona de carregamento partilhada (prédio, empresa, hotel).
2. **Se o lugar faz parte da fração** (vem na descrição da fração ou tem artigo matricial próprio)
   ou é um espaço comum de uso exclusivo. Muda de que quadro pode ser alimentado.
3. **Tomada ou wallbox**, e que carro. Procura tu o carregador de bordo da versão exata.
4. **A potência contratada** e se o contrato é monofásico ou trifásico.

## Modos de carga

O modo diz como o carro se liga à instalação [DGEG, guia técnico, 2.1.8]:

| Modo | Como liga | Notas |
|---|---|---|
| 1 | Tomada normalizada, até 16 A, sem proteção no cabo | Corrente alterna. Só fase, neutro e terra. |
| 2 | Tomada normalizada, até 32 A, com uma caixa de controlo no cabo | Corrente alterna. A caixa tem função piloto e diferencial. É o cabo que vem com muitos carros. |
| 3 | Posto fixo (wallbox), ligado em permanência à instalação | Corrente alterna, tomada ou cabo Tipo 2. A função piloto vai até ao posto. |
| 4 | Carregador externo que dá corrente contínua | Posto DC, sempre com o cabo preso ao posto. |

- Os modos 1 a 3 carregam em corrente alterna, pelo carregador de bordo; o modo 4 em contínua
  [DGEG, guia técnico, 2.1.8].
- O guia chama SAVE (sistema de alimentação de veículos elétricos) ao que muitas normas chamam
  EVSE: o cabo, as fichas, as tomadas e o posto [DGEG, guia técnico, 2.2.22].
- **Sem extensões nem segundo cabo** entre o carro e a tomada ou o posto. Adaptadores só os feitos
  para carregar, marcados para isso e aprovados pelo fabricante do carro e do equipamento, e nunca
  para passar de um modo a outro [DGEG, guia técnico, 2.2.1 e 2.2.2].

## O circuito

- **Um circuito dedicado por carro.** O circuito só alimenta o ponto de ligação e os consumos
  auxiliares dele, e não deve ser afetado pela falha de outros circuitos [DGEG, guia técnico,
  3.1.5].
- **Cabos de 2,5 mm² ou mais**, dimensionados para pelo menos 16 A [DGEG, guia técnico, 3.1.5 e
  4.3].
- **Queda de tensão** até 5 % entre a origem da instalação e o ponto de ligação [DGEG, guia
  técnico, 3.1.5].
- **Disjuntor próprio** em cada circuito final, de curva C ou D, escolhido para o tipo de carga
  [DGEG, guia técnico, 4.3 e 5.1.2.2]. A proteção não pode ter rearme automático [DGEG, guia
  técnico, 4.2].
- **Fator de simultaneidade 1**: cada ponto conta como se estivesse sempre à corrente máxima. Só
  pode ser menor num circuito com vários pontos se houver um sistema de controlo da carga [DGEG,
  guia técnico, 3.1.3].
- **Descarregador de sobretensões** recomendado, perto da origem da instalação [DGEG, guia técnico,
  4.4 e 5.1.2.3].
- Se ainda não se sabe que carro vai carregar, o circuito pode terminar numa caixa de derivação,
  pronta para ligar depois uma tomada ou um posto [DGEG, guia técnico, 3.1.6].
- **Esquema de terra**: em regra TT. Se a rede for TN, o circuito final tem de ser TN-S, sem condutor
  PEN [DGEG, guia técnico, 3.1.4].

### Potência por disjuntor

O guia dá a potência máxima de cada circuito conforme o disjuntor [DGEG, guia técnico, 3.1.2,
quadro 2]:

| Disjuntor | Monofásico, 230 V | Trifásico, 230/400 V |
|---|---|---|
| 10 A | 2,3 kVA | — |
| 16 A | 3,68 kVA | 11,1 kVA |
| 20 A | 4,6 kVA | 13,9 kVA |
| 25 A | 5,75 kVA | 17,3 kVA |
| 32 A | 7,36 kVA | 22,2 kVA |
| 40 A | 9,2 kVA | 27,7 kVA |

- A potência contratada tem de ter folga acima da do circuito. O guia dá um exemplo: para carregar a
  3,68 kVA, mesmo sem mais nada ligado, o escalão mínimo seria 4,6 kVA (20 A em 230 V) [DGEG, guia
  técnico, 3.1.2]. Os escalões e o custo vêm do contrato de eletricidade; não os inventes.

## O diferencial

- **Um diferencial (DR) próprio por ponto de ligação**, no mínimo do tipo A, de 30 mA ou menos, que
  corte todos os condutores ativos, incluindo o neutro [DGEG, guia técnico, 5.1.2.1.1].
- **Num posto com tomada ou cabo Tipo 2 (EN 62196)**, é preciso também proteção contra correntes de
  defeito com componente contínua, salvo se o próprio posto já a tiver. Serve uma de três
  [DGEG, guia técnico, 5.1.2.1.1]:
  - um diferencial do tipo B;
  - um do tipo A com um detetor de corrente contínua (IEC 62955);
  - um do tipo F com um detetor de corrente contínua (IEC 62955).
- Se ainda não se sabe o que vai carregar, pode ficar um tipo A, A ou F com detetor, ou B. Quando se
  instalar o posto, o técnico tem de confirmar que o diferencial serve [DGEG, guia técnico,
  5.1.2.1.1, nota 1].
- Diz ao utilizador para confirmar na ficha técnica da wallbox se a deteção de corrente contínua já
  vem integrada: muda o diferencial que é preciso pôr no quadro.
- O guia é mais exigente do que o texto da secção 722 das RTIEBT, porque a normalização
  internacional mudou depois de 2015 [DGEG, guia técnico, 5.1.2.1.1, nota 2]. Segue o guia.
- Deve haver seletividade entre este diferencial e os que estão a montante, para uma falha no
  carro não cortar a casa toda [DGEG, guia técnico, 5.1.2.1.1].

## Tomadas e fichas

| Tomada ou ficha | Norma | Para que modo | Regra |
|---|---|---|---|
| Tomada doméstica (Schuko) | NP 1260 | 1 ou 2 | Até 10 A de corrente de carga, salvo se marcada de fábrica para carregar veículos. |
| Tomada industrial CEE | EN 60309 | 1 ou 2 | Em local acessível ao público, só com obturadores ou proteção equivalente. |
| Tipo 2 | EN 62196-2 | 3 | Só num posto (wallbox), que controla o carregamento com o carro. |
| CCS (Combo 2) e CHAdeMO | EN 62196-3 | 4 | Cabo preso ao posto DC. |

[DGEG, guia técnico, 5.1.2.5.1 e quadro 3]

- A tomada doméstica é recomendada só em instalações existentes. Numa remodelação, instala-se uma
  tomada própria para carregar [DGEG, guia técnico, 5.1.2.5.1].
- As tomadas ficam fixas a uma parede ou num quadro, nunca soltas, o mais perto possível do lugar,
  com o bordo de baixo entre **0,5 m e 1,5 m** do chão. Cada tomada ou ficha alimenta só um carro
  [DGEG, guia técnico, 5.1.2.5.1].
- Junto da tomada tem de haver um interruptor ou outro dispositivo que corte o circuito à plena
  carga. A ficha não serve para cortar [DGEG, guia técnico, 3.1.6 e 4.5]. Nas soluções com o corte no
  quadro, fica junto da tomada o aviso "Desligar o interruptor antes de retirar a ficha" [DGEG,
  guia técnico, figura 5].
- Uma tomada Tipo 2 solta, sem posto, não se usa: sem posto o carro só carrega em modo 1 ou 2
  [DGEG, guia técnico, figura 5, nota].
- Cada ponto de ligação fica identificado com o lugar a que pertence, e o circuito no quadro tem a
  mesma identificação [DGEG, guia técnico, 3.1.6]. A aparelhagem é marcada, por exemplo com "VE"
  [DGEG, guia técnico, 5.1.1].

## De que quadro se alimenta

O guia tem esquemas-tipo para cada caso, nas figuras 6 a 19 [DGEG, guia técnico, 3.1.1 e quadro 1].

### Moradia

- Da instalação da casa, com ramal próprio, com ou sem garagem fechada [DGEG, guia técnico, figuras
  8 e 9].

### Prédio, lugar de uso exclusivo

| Origem | Garagem fechada (boxe) | Lugar marcado no chão |
|---|---|---|
| Quadro de entrada da fração | figura 10 | figura 10A |
| Quadro de colunas, com quadro de entrada próprio do lugar | figura 11 | figura 11A |
| Quadro dos serviços comuns | figura 12 | figura 13 |

[DGEG, guia técnico, 3.1.1, alínea b2]

- **Lugar que faz parte da fração** (vem na descrição da fração): em regra é alimentado do quadro
  de entrada da habitação (RTIEBT, secção 803.6.4). Num prédio existente, se isso não for possível,
  pode ser alimentado do quadro de colunas ou dos serviços comuns [DGEG, guia técnico, 2.6.3, nota 2,
  e 3.1.1, nota 5].
- **Espaço comum de uso exclusivo** (por exemplo, um lugar da garagem comum atribuído à fração, que
  não faz parte da descrição dela): não pode ser alimentado do quadro de entrada da habitação [DGEG,
  guia técnico, 2.6.4, nota 2]. Fica o quadro de colunas ou o dos serviços comuns.
- **Serviços comuns só em último caso.** O guia recomenda estas soluções só quando as outras não
  forem viáveis técnica ou economicamente, e exige sempre, além do contador dos serviços comuns, a
  contagem individual de cada ponto [DGEG, guia técnico, 3.1.1, nota de rodapé 2, e parte 7, nota
  1]. Num lugar sem boxe e sem autenticação do utilizador, o acesso à tomada ou ao posto tem de ser
  controlado [DGEG, guia técnico, figura 13].
- Num esclarecimento de 2024, a DGEG diz que a alimentação a partir do quadro de colunas responde às
  limitações da alimentação a partir dos serviços comuns [DGEG, esclarecimento 2024]. Quando o
  utilizador hesitar entre as duas, apresenta o quadro de colunas como a solução que a DGEG
  prefere.

### Zona de carregamento partilhada

- Numa zona dedicada de um parque (prédio, empresa, hotel), com acesso só para condóminos ou
  clientes, alimenta-se de uma instalação própria com ramal, do quadro de colunas ou dos serviços
  comuns [DGEG, guia técnico, 3.1.1, alínea c, e figuras 14 a 19].
- Sem autenticação do utilizador, recomenda-se controlar o acesso à tomada ou ao posto, para evitar
  usos indevidos [DGEG, guia técnico, figura 5].

### Por onde passam os cabos

- O circuito de um lugar alimentado da fração só passa pelas zonas comuns e pelos espaços da
  própria fração. Nunca atravessa a boxe ou o lugar de outro condómino [DGEG, guia técnico, 3.1.5].
- Num lugar marcado no chão, o circuito sai de um quadro próprio do lugar, que só abre com chave ou
  ferramenta, e junto ao acesso há um corte geral de todos os circuitos desse lugar [DGEG, guia
  técnico, 3.1.5].
- Os cabos ficam marcados ou etiquetados com a habitação e o lugar que ligam, para se saber de quem
  são numa reparação [DGEG, guia técnico, 3.1.5].

### Corte de emergência

- Num piso com lugares marcados no chão alimentados dos quadros das habitações, tem de haver um
  sistema de segurança positiva, no quadro geral do piso, que corte de uma vez todas essas
  alimentações, identificado como corte de emergência [DGEG, guia técnico, 4.5.1].
- O corte de emergência interrompe todos os condutores ativos, incluindo o neutro. Fichas e
  tomadas nunca servem de corte de emergência [DGEG, guia técnico, 4.5.1].

## Potência no parque de um prédio

- Cada ponto de ligação conta com pelo menos **3680 VA**, ou com a sua potência, se for maior
  [DGEG, guia técnico, 3].
- Número mínimo de lugares a considerar (arredonda para cima) [DGEG, guia técnico, 3]:
  - prédio de habitação: **N = 0,8 + 0,2 × n**, com n os lugares do parque, tirando os que já são
    alimentados das frações;
  - outros parques com zona dedicada: **N = 0,9 + 0,1 × n**; num parque com mais de 400 lugares, N
    pode ficar limitado a 41.
- A instalação não tem de ficar feita para todos os lugares, mas tem de ficar preparada para ligar
  cada lugar "de forma fácil": caminhos de cabos ou cabos à vista com braçadeiras, sem abrir roços
  [DGEG, guia técnico, 3, nota 3].
- Quando os pontos ou a potência passam do que foi dimensionado, é preciso um sistema de controlo
  da carga, que desliga cargas ou, nos modos 3 e 4, baixa a corrente de carregamento [DGEG, guia
  técnico, 3].
- Nos parques que não são de habitação, basta um ponto de ligação logo de início; o guia recomenda
  dedicar ao carregamento metade da potência mínima desde o início [DGEG, guia técnico, 3, nota 4].

## Dentro e fora

| Onde | Água | Poeiras | Choques |
|---|---|---|---|
| Garagem interior de um prédio | IPX1 ou IPX2 | IP4X | IK08 com proteção contra o carro, IK10 sem ela (entre 0,9 e 2 m); IK07 dentro de uma boxe |
| Exterior | IPX4 ou mais, conforme a exposição | IP4X | IK08 com proteção, IK10 sem ela (até 2,5 m) |

[DGEG, guia técnico, 5.2.1 e 5.3.1, quadros 4 e 5]

- No exterior, o equipamento tem de aguentar de –25 °C a +40 °C. Numa moradia, a proteção contra
  choques do equipamento no exterior pode ser menor, mas não abaixo da do interior [DGEG, guia
  técnico, quadro 5].
- Quadros e postos com partes ativas acessíveis fecham com chave ou ferramenta e, de porta aberta,
  mantêm pelo menos IPXXB ou IP2X [DGEG, guia técnico, 4.1].
- Recomenda-se, no interior, um indicador luminoso de tensão em cada circuito de carregamento
  [DGEG, guia técnico, 5.2.2].

## Carro a alimentar a casa (V2H)

- Nos modos 1 e 2 é proibido o carro alimentar a instalação. No modo 3, o posto tem de impedir que
  aconteça sem querer. Em 2023 as regras para o carro alimentar a casa de propósito ainda estavam em
  estudo no CENELEC [DGEG, guia técnico, 5.1.2.6]. Para o estado atual do V2H, ver
  `carregar-em-casa`.

## Postos acessíveis ao público

Para OPC e projetistas; o condutor raramente precisa disto.

- A resistência de terra não pode deixar aparecer tensões de contacto acima de 25 V, em qualquer
  época do ano. Postos alimentados da rede têm elétrodos de terra próprios [DGEG, guia técnico,
  5.3.2].
- Condutores de terra de cobre: nus com 25 mm² ou mais; isolados (0,6/1 kV, verde/amarelo, bainha
  preta) com 16 mm² ou mais [DGEG, guia técnico, 5.3.2].
- Num posto público, a tomada só fica em tensão depois de o utilizador se autenticar (modos 1 e 2)
  ou de o posto detetar o carro (modos 3 e 4) [DGEG, guia técnico, 3.1.6].

## O que pedir ao eletricista

Uma lista para o utilizador levar, sem substituir o projeto:

- circuito dedicado só para o carro, desde o quadro certo para o lugar (ver acima);
- cabo de 2,5 mm² ou mais, para pelo menos 16 A, com queda de tensão até 5 %;
- disjuntor próprio de curva C ou D e diferencial próprio de 30 mA, tipo A no mínimo, e tipo B (ou A
  ou F com detetor de corrente contínua) se a wallbox não trouxer essa deteção;
- interruptor de corte junto da tomada, ou no quadro do lugar;
- tomada ou wallbox fixa, entre 0,5 m e 1,5 m do chão, com o grau IP e IK do local;
- descarregador de sobretensões, recomendado;
- circuito e ponto de ligação identificados com o lugar;
- no fim, a declaração de conformidade ou o termo de responsabilidade (ver `carregar-em-casa`).

## O que está desatualizado no guia

O guia é de setembro de 2023 e cita o regime de 2010. Quando o utilizador citar estas passagens,
corrige com a regra atual:

- Cita o DL 39/2010 e o DL 90/2014, revogados pelo DL 93/2025 a partir de 19-08-2025 (ver
  `regime-2010`).
- Diz que os postos dos OPC são inspecionados de quatro em quatro anos (DL 90/2014). Hoje são de
  cinco em cinco anos, por uma EIIEL (DL 93/2025, art. 16.º).
- Cita as Portarias n.º 220/2016 e 221/2016 e a Diretiva 2014/94/UE. A diretiva foi substituída pelo
  AFIR (Regulamento (UE) 2023/1804), e as portarias do DL 93/2025 estão na skill `afir`.
- Sugere marcar a aparelhagem com o modelo do anexo do DL 39/2010. Basta a sigla "VE" ou equivalente.
- O esclarecimento da DGEG de 2024 cita o art. 29.º do DL 39/2010, sobre a instalação em edifícios
  existentes. Hoje a regra do condomínio está no art. 23.º do DL 93/2025 (ver `carregar-em-casa`).

## Fontes

### Legislação

- Portaria n.º 949-A/2006, de 11 de setembro (RTIEBT — regras técnicas das instalações elétricas
  de baixa tensão): https://data.dre.pt/eli/portaria/949-a/2006/09/11/p/dre/pt/html
- Portaria n.º 252/2015, de 19 de agosto (adita às RTIEBT a secção 722, alimentação de veículos
  elétricos): https://data.dre.pt/eli/portaria/252/2015/08/19/p/dre/pt/html
- Decreto-Lei n.º 93/2025, de 14 de agosto (regime jurídico da mobilidade elétrica), arts. 16.º,
  21.º, 23.º e 25.º: https://data.dre.pt/eli/decreto-lei/93/2025/08/14/p/dre/pt/html

### Normas e standards

- IEC 60364-7-722 (instalações elétricas de baixa tensão — alimentação de veículos elétricos):
  https://webstore.iec.ch/en/publication/29958
- IEC 61851-1 (sistema de carregamento condutivo): https://webstore.iec.ch/en/publication/33644
- IEC 62196-2:2025 (fichas e tomadas AC — Tipo 1 e Tipo 2):
  https://webstore.iec.ch/en/publication/86317
- IEC 62196-3 (fichas e conectores DC — CCS e CHAdeMO): https://webstore.iec.ch/en/publication/59923
- Também citadas pelo guia: NP 1260 (tomadas domésticas), EN 60309 (tomadas industriais), EN 61008,
  EN 61009 e NP EN 62423 (diferenciais), IEC 62955 (detetores de corrente contínua), EN 62305
  (proteção contra descargas atmosféricas).

### Outras fontes

Da DGEG – Direção-Geral de Energia e Geologia, verificado a 2026-11-06:

- [DGEG, guia técnico] Guia Técnico das Instalações Elétricas para a Alimentação de Veículos
  Elétricos, 3.ª edição (2023-09-14), da CTE 64, aprovado pela DGEG a 2023-09-18:
  https://www.dgeg.gov.pt/media/dzejui0r/guia-ve-ed-3-2023.pdf
- [DGEG, esclarecimento 2024] "Esclarecimento | Instalações Elétricas para Alimentação de Veículos
  Elétricos" (2-12-2024):
  https://www.dgeg.gov.pt/pt/destaques/esclarecimento-instalacoes-eletricas-para-alimentacao-de-veiculos-eletricos/

Os pontos da DGEG estão escritos por palavras nossas (ver `docs/fontes/dgeg.md` no Voltaria).
