# NAPs europeus (AFIR — carregamento de VE)

Lista dos Pontos de Acesso Nacionais (NAP) relevantes para o carregamento de
veículos elétricos ao abrigo do AFIR (art. 20.º, Regulamento (UE) 2023/1804).
Fonte principal: https://evnapdata.eu/naps (mantido manualmente; pode estar
ligeiramente desatualizado). Complementado com a lista NAPCORE/ITS (transporte em
geral): https://napcore.eu/description-naps/national-access-point/.

Estado: ✅ ligado, ⚠️ parcialmente ligado, 🚫 não ligado (à data da fonte).

| País | NAP | Estado | Formato principal |
|---|---|---|---|
| Áustria | https://mobilitydata.gv.at | ✅ | XLSX (E-Control) |
| Bélgica | https://transportdata.be | ⚠️ | OCPI, DATEX II, AFIR |
| Bulgária | https://sipbg.gov.bg/bgnap | 🚫 | — |
| Croácia | https://promet-info.hr | ⚠️ | GeoJSON |
| Chipre | https://traffic4cyprus.org.cy | ✅ | DATEX II v2 |
| Chéquia | https://registr.dopravniinfo.cz | ✅ | XLSX |
| Dinamarca | https://nap.vd.dk | ⚠️ | DATEX II v3, AFIR |
| Estónia | https://peatus.ee | 🚫 | — |
| Finlândia | https://finap.fi | ✅ | GeoJSON, DATEX II v3.6 |
| França | https://transport.data.gouv.fr | ✅ | CSV (IRVE) |
| Alemanha | https://mobilithek.info | ✅ | CSV (BNetzA) |
| Grécia | https://nap.gov.gr | ✅ | OCPI 2.x |
| Hungria | https://napportal.kozut.hu | ✅ | DATEX II 3.3 |
| Irlanda | https://data.gov.ie | ⚠️ | CSV, GeoJSON |
| Itália | https://cciss.it | 🚫 | — |
| Letónia | https://transportdata.gov.lv | ✅ | DATEX II v3.4 |
| Lituânia | https://ev.vialietuva.lt | ✅ | OCPI 2.3.0 |
| Luxemburgo | https://data.public.lu | ✅ | KML |
| Malta | https://geoservices.transport.gov.mt | ⚠️ | KML |
| Países Baixos | https://ntm.ndw.nu | ✅ | GeoJSON, JSON |
| Noruega (não-UE) | https://transportportal.atlas.vegvesen.no | ✅ | NOBIL JSON |
| Polónia | https://kpd.gddkia.gov.pl | 🚫 | DATEX II v3.5 |
| Portugal | https://nap-portugal.imt-ip.pt | ✅ | DATEX II v3 |
| Roménia | https://pna.cestrin.ro | ⚠️ | XLSX |
| Eslováquia | https://ndsas.sk | 🚫 | — |
| Eslovénia | https://nap.si | 🚫 | DATEX II v3.6 |
| Espanha | https://nap.mitma.es | ✅ | DATEX II v3 |
| Suécia | https://trafficdata.se | ✅ | NOBIL JSON |
| Suíça (não-UE) | https://opentransportdata.swiss | ✅ | OICP JSON |

## Notas

- "Ligado" significa que a fonte acima consegue obter dados desse país; "parcial" significa
  cobertura incompleta da rede nacional; "não ligado" significa que não foi possível obter dados.
- O CEAP (Common European Access Point) europeu, hospedado no EAFO, será a porta de entrada para
  descobrir os dados dos NAPs nacionais; previsão até 31-12-2026:
  https://alternative-fuels-observatory.ec.europa.eu
- Em Portugal, o NAP é gerido pelo IMT-IP e a MOBI.E publica os endpoints
  (evChargingInfra, evActualStatus) em DATEX II 3.3, ao abrigo do DL 93/2025.
- Para a lista completa de NAPs no âmbito da Diretiva ITS (MMTIS/RTTI/SRTI/SSTP), ver
  https://napcore.eu/description-naps/national-access-point/ e
  https://eunapmonitoring.napcore.imet.gr/national_access_points.html.
