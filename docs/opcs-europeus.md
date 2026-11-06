# OPCs europeus ligados aos NAPs

Não existe um registo único europeu de Operadores de Pontos de Carregamento (OPC, CPO).
O AFIR exige que cada Estado-membro nomeie uma **IDRO** (Organização de Registo de
Identificação), que gere os códigos únicos (IDACS) dos OPC e dos eMSP. Os códigos registados
e as listas de OPC são publicados nos NAPs nacionais ou em registos associados.

A lista abaixo indica, por país, onde encontrar os OPC registados. Os OPC que operam postos
públicos/semipúblicos são obrigados (AFIR, art. 20.º) a publicar dados no NAP nacional via API.

| País | Onde estão os OPC registados | Notas |
|---|---|---|
| Áustria | E-Control — registos de Ladestellen (ladestellen.at) | IDRO: Ministério Federal para a Ação Climática |
| Bélgica | Transportdata.be (regional: Flandres/Valónia) | IDRO: autoridades regionais |
| Chipre | NAP traffic4cyprus.org.cy | IDRO: Serviços de Obras Públicas |
| Chéquia | Registo estatutário do MPO (Ministério da Indústria e Comércio) | IDRO: autoridade de tráfego rodoviário |
| Dinamarca | NAP nap.vd.dk (Dataudveksler) | OCPI 2.2.1/2.3.0 |
| Finlândia | Fintraffic Digitraffic — lista de CPOs (JSON aberto) | NAP finap.fi |
| França | QualiCharge / transport.data.gouv.fr | IDRO: Open Data Réseaux Énergies |
| Alemanha | Mobilithek + registo BNetzA (Ladesäulenregister) | IDRO: Bundesnetzagentur |
| Grécia | Registo ΜΥΦΑΗ (electrokinisi.yme.gov.gr) | IDRO: Ministério dos Transportes |
| Hungria | NAP napportal.kozut.hu (subscrições E.ON Drive, Eco-Movement) | — |
| Irlanda | TII Data Exchange Platform (data.gov.ie) | IDRO: Transport Infrastructure Ireland |
| Itália | PUN — Piattaforma Unica Nazionale (cciss.it) | acesso com contrato |
| Letónia | Eco-Movement no NAP transportdata.gov.lv | — |
| Lituânia | Via Lietuva OCPI endpoint | — |
| Luxemburgo | data.public.lu (Chargy) | — |
| Malta | "Charge My Ride" (Google My Maps) | sem NAP formal |
| Países Baixos | NDW open data (ntm.ndw.nu) | OCPI 2.2.1 |
| Noruega (não-UE) | NOBIL (transportportal.atlas.vegvesen.no) | — |
| Polónia | KPD (kpd.gddkia.gov.pl) | DATEX II v3.5 |
| Portugal | DGEG — lista de OPC registados | https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/lista-de-opc/ |
| Roménia | data.gov.ro (estações PNRR por município) | — |
| Eslovénia | NAP nap.si | — |
| Espanha | DGT/MITERD — tabela de eletrolineras (nap.dgt.es) | — |
| Suécia | NOBIL (trafficdata.se) | IDRO: Swedish Energy Agency |
| Suíça (não-UE) | SFOE — opentransportdata.swiss | — |

## Portugal — OPC registados na DGEG

A DGEG mantém a lista oficial de OPC registados em Portugal (tabela HTML:
Nº | Entidade | Validade | Morada | NIF | Site). É a referência autoritativa para o
mercado português. A lista de CEME registados (regime transitório) está também na DGEG.

- OPC: https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/lista-de-opc/
- CEME (regime transitório): https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/regime-transitorio/ceme-registados/

## Croácia — exemplo de registo IDRO publicado

A Croácia publica a lista dos códigos IDRO dos CPO e MSP registados em formato PDF:
"CRO IDRO — Registered CPO/MSP IDs" (NAP pametnamobilnost.hr).

## Como obter a lista completa de um país

1. Identificar a IDRO do país (ver tabela acima e o NAP nacional).
2. Consultar o registo IDRO publicado (PDF/CSV/API) ou o próprio NAP.
3. Os códigos OCPI Party ID (3 caracteres) e os códigos MOBI.E (4 letras, em PT) identificam
   inequivocamente cada OPC.

## Fontes

- GreenFlux — guia completo de reporte ao NAP para OPC:
  https://www.greenflux.com/expertise/blogs/afir-national-access-point-nap-reporting-complete-guide-charge-point-operators/
- Spirii — AFIR art. 20.º para OPC:
  https://spiriipartnerhelp.zendesk.com/hc/en-gb/articles/41027320032913-AFIR-Article-20-What-CPOs-need-to-know-about-it
- Monta — conformidade de reporte AFIR por país:
  https://monta.com/help/monta-hub-reporting-compliance-afir-compliance/charge-point-data-reporting-afir
