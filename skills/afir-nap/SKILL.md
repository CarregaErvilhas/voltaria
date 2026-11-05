---
name: afir-nap
description: "Explica o conceito de Ponto de Acesso Nacional (NAP) no âmbito do AFIR (Regulamento (UE) 2023/1804): o que é, quem o gere, que dados publica (estáticos e dinâmicos), em que formato (DATEX II), como os OPC se ligam, o que é o CEAP europeu, e como isso se aplica em Portugal (MOBI.E/EADME, DL 93/2025). Usa quando o utilizador pergunta o que é um NAP, como consultar ou publicar dados de postos, o que é o CEAP, ou como funcionam os identificadores IDRO/IDACS."
---

# AFIR NAP — Ponto de Acesso Nacional

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## O que é o AFIR

O **Regulamento (UE) 2023/1804** (AFIR — Alternative Fuels Infrastructure Regulation) substitui a
Diretiva 2014/94/UE e define requisitos mínimos de infraestrutura para combustíveis alternativos na
UE, incluindo a rede de carregamento de veículos elétricos. Aplica-se diretamente em todos os
Estados-membros. Texto oficial: https://eur-lex.europa.eu/eli/reg/2023/1804/oj

## O que é um NAP

Um **Ponto de Acesso Nacional (NAP)** é a plataforma central de cada Estado-membro onde se publicam
os dados sobre infraestruturas de combustíveis alternativos, incluindo os postos de carregamento de
VE. O conceito não nasceu com o AFIR: já existia no âmbito da Diretiva ITS 2010/40/UE e das suas
regulamentações delegadas (MMTIS, RTTI, SRTI, SSTP), para dados de mobilidade em geral. O AFIR
estende-o aos combustíveis alternativos, em particular ao carregamento elétrico (art. 20.º).

- Cada Estado-membro opera o seu próprio NAP. Não há um NAP europeu único.
- O NAP é um **ponto de acesso**, não uma base de dados centralizada: agrega e disponibiliza os
  dados que os OPC (e outras entidades) lhe entregam.
- Serve três propósitos: permitir aos condutores encontrar postos disponíveis; permitir às
  autoridades monitorizar a implantação da rede; e permitir aos eMSP prestar serviços de carregamento
  integrados.

## CEAP — o ponto de acesso europeu

O AFIR prevê um **Ponto de Acesso Comum Europeu (CEAP)**, hospedado no Observatório Europeu dos
Combustíveis Alternativos (EAFO), que funciona como **porta de entrada** para descobrir os dados
publicados em cada NAP nacional. O CEAP não armazena dados: liga o utilizador à informação
disponível nos NAPs. A sua criação está prevista até 31 de dezembro de 2026. Ver:
https://alternative-fuels-observatory.ec.europa.eu

## O que os OPC publicam no NAP (AFIR, art. 20.º)

Os OPC que operam postos públicos ou semipúblicos têm de disponibilizar, através do NAP nacional,
dados **estáticos** e **dinâmicos**, via API, a partir de 14 de abril de 2025 (para os Estados-membros
com os prazos aplicáveis):

- **Dados estáticos**: localização do posto; número de conectores; lugares para pessoas com
  mobilidade reduzida; contactos; horário; código do operador; tipos de conector; tipo de corrente
  (AC/DC); potência máxima do posto e do EVSE; tipos de veículo compatíveis.
- **Dados dinâmicos**: estado operacional (em serviço/avariado); disponibilidade em tempo real;
  preço ad hoc; se a eletricidade é 100 % renovável.

A publicação pode ser feita pelo próprio OPC ou por um intermediário (por exemplo, uma plataforma de
gestão de postos), mas a responsabilidade é do OPC. Em Portugal, a MOBI.E publica o inventário
estático e o estado dinâmico com preços no seu NAP.

## Formato: DATEX II

O AFIR exige interoperabilidade europeia. O formato de referência é o **DATEX II** (norma CEN), em
particular o perfil de infraestrutura de energia alternativa. Em Portugal, o NAP da MOBI.E usa
**DATEX II 3.3**, com os namespaces `energyInfrastructure`, `facilities`, `locationReferencing`,
`locationExtension`, `commonExtension` e `common`. Cada país pode ainda expor os dados noutros
formatos (OCPI, GeoJSON, CSV), mas o DATEX II é o denominador comum para a interoperabilidade.

As classes de potência do AFIR (Anexo III) são as usadas para reporte, acima dos 22 kW legais
("potência normal" ≤ 22 kW; "potência elevada" > 22 kW).

## IDRO e IDACS — identificação dos operadores

O AFIR exige que cada Estado-membro nomeie uma **Organização de Registo de Identificação (IDRO)**,
que gere códigos únicos de identificação dos OPC e dos eMSP (IDACS). Estes códigos são usados nos
dados publicados no NAP e permitem identificar inequivocamente quem opera cada posto e quem presta
serviços de mobilidade. A lista dos IDRO por país e os códigos registados estão publicados em cada
NAP nacional (ou em registos associados). Em Portugal, esta função enquadra-se na DGEG e na
estrutura da MOBI.E.

## Como funciona em Portugal

- **NAP português**: `https://nap-portugal.imt-ip.pt`, gerido pelo IMT-IP, com os endpoints da MOBI.E:
  - Inventário estático: `https://pgm.mobie.pt/integration/nap/evChargingInfra` (~190 MB, XML
    DATEX II 3.3).
  - Estado dinâmico + preços: `https://pgm.mobie.pt/integration/nap/evActualStatus` (~40 MB).
- **EADME**: a MOBI.E passou a exercer as funções de Entidade de Acesso aos Dados da Mobilidade
  Elétrica (EADME) ao abrigo do DL 93/2025, com regime transitório até 31 de dezembro de 2027.
- **DL 93/2025**: novo modelo de mercado (contrato direto com o OPC ou com um eMSP). **DL 155/2026**:
  prorroga o período transitório até 31-12-2027, mantendo a coexistência com o modelo antigo
  (CEME + MOBI.E).
- A MOBI.E continua a gerir a plataforma da rede até 31-12-2027 e a cobrar a TAR (tarifa de acesso
  às redes da mobilidade elétrica), fixada pela ERSE.

## Acesso e licença

Os endpoints do NAP português são publicados sob licenças de livre acesso (ver as páginas NAP do
IMT-IP). O tarifário OPC do MOBI.E é publicado em CSV no sítio da MOBI.E. A lista atualizada de OPC
registados está na DGEG; a de CEME também (regime transitório).

## DATEX II — o que é e como aparece nos NAPs

O **DATEX II** é a norma europeia (CEN/TS 16157) para a troca de dados de tráfego e de
mobilidade. No contexto do AFIR, é o formato de referência para publicar dados de
infraestrutura de combustíveis alternativos nos NAPs, de forma interoperável entre
Estados-membros.

### Estrutura de dados nos NAPs

Um NAP AFIR publica, para cada posto, dois conjuntos de dados:

- **Inventário estático** (`evChargingInfra`, em PT): locais, pontos de carregamento (EVSE) e
  conectores, com identificadores, coordenadas, operador, potência, tipos de ficha, horário,
  contactos, acessibilidade. Muda raramente.
- **Estado dinâmico + preços** (`evActualStatus`, em PT): estado operacional, disponibilidade em
  tempo real, preço ad hoc, por ponto. Atualizado com frequência.

Em Portugal (MOBI.E), os dois endpoints são XML DATEX II 3.3 com os namespaces:
`energyInfrastructure`, `facilities`, `locationReferencing`, `locationExtension`,
`commonExtension` e `common`. Cada registo usa identificadores estáveis (site, EVSE, conector) e
potência contínua (`max_power_w`, `voltage`/`max_current`), não classes de potência — as classes
do dashboard seguem o Anexo III §2 do AFIR.

### Como se lê um NAP

- Os dados são XML (DATEX II) ou, conforme o país, OCPI, GeoJSON, CSV, JSON.
- O acesso pode ser aberto, com chave, ou com contrato formal (ver `docs/nap-europeus.md`).
- A granularidade típica: **site** (local) → **EVSE** (ponto de carregamento) → **conector**.
- Os campos AFIR obrigatórios (art. 20.º) incluem localização, número de conectores, lugares para
  mobilidade reduzida, contactos, horário, código do operador, tipos de conector, AC/DC, potência
  máxima do posto e do EVSE, tipos de veículo compatíveis, estado, disponibilidade, preço ad hoc
  e se a eletricidade é 100 % renovável.

### Onde encontrar o DATEX II

- Schemas (v3) versionados no nap-dashboard: `assets/schemas/` (descarregados de
  http://datex2.eu/schema/3/...).
- Documentação oficial: http://datex2.eu
- Portal DATEX@NAPs: https://datex2.naps.inqms.tamtamresearch.com/naps-browser/nap/index.html

## Como responder

- Distingue sempre o que é obrigação europeia (AFIR) do que é legislação nacional portuguesa (DL
  93/2025, DL 155/2026) e do que é a operação concreta do NAP (MOBI.E, IMT-IP).
- Não cites números (prazos, distâncias, potências mínimas) de memória. Consulta o texto do AFIR e
  os decretos-lei para valores exatos. O AFIR fixa potências mínimas por nó da rede TEN-T e prazos
  de implantação; confirma sempre na versão oficial.
- Quando o utilizador pedir a lista de NAPs europeus, de OPCs ou de eMSPs, remete para os ficheiros
  de referência do Voltaria (`docs/nap-europeus.md`, `docs/opcs-europeus.md`, `docs/emps-europeus.md`)
  e para os registos IDRO nacionais, que são a fonte autoritativa.
- Para preços e estados em tempo real de postos portugueses, usa as ferramentas do ohmigo
  (`find_chargers`, `lookup_charger`), que leem o NAP da MOBI.E.

## Fontes

- Regulamento (UE) 2023/1804 (AFIR): https://eur-lex.europa.eu/eli/reg/2023/1804/oj
  (versão PT: https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32023R1804)
- Diretiva 2010/40/UE (ITS) e regulamentações delegadas (MMTIS, RTTI, SRTI, SSTP).
- DL n.º 93/2025: https://diariodarepublica.pt/dr/detalhe/decreto-lei/93-2025-928937303
- DL n.º 155/2026: https://files.diariodarepublica.pt/1s/2026/07/14700/0003200033.pdf
- NAP português: https://nap-portugal.imt-ip.pt
- MOBI.E endpoints: https://pgm.mobie.pt/integration/nap/evChargingInfra e evActualStatus
- CEAP / EAFO: https://alternative-fuels-observatory.ec.europa.eu
- NAPCORE (coordenação de NAPs): https://napcore.eu
- Lista de NAPs europeus (AFIR, carregamento): https://evnapdata.eu/naps
- NAPCORE — lista de NAPs (ITS): https://napcore.eu/description-naps/national-access-point/
- GreenFlux — guia de reporte ao NAP para OPC: https://www.greenflux.com/expertise/blogs/afir-national-access-point-nap-reporting-complete-guide-charge-point-operators/
- Spirii — AFIR art. 20.º para OPC: https://spiriipartnerhelp.zendesk.com/hc/en-gb/articles/41027320032913-AFIR-Article-20-What-CPOs-need-to-know-about-it
- Monta — conformidade de reporte AFIR por país: https://monta.com/help/monta-hub-reporting-compliance-afir-compliance/charge-point-data-reporting-afir
- nap-dashboard (Voltaria adjacente) — referências de fontes: `references/data-sources.md`
---

Vê também a skill `afir` (infraestrutura AFIR em geral: cobertura TEN-T, ad hoc, transparência) e
`regime-2010` (modelo MOBI.E antigo) e `carregamento-publico`.
