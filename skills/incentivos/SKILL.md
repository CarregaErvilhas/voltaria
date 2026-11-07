---
name: incentivos
description: "Responde a perguntas sobre apoios e benefícios fiscais para veículos elétricos e postos de carregamento em Portugal (Fundo Ambiental, apoios anunciados do Plano Social para o Clima, IUC, ISV, IVA, tributação autónoma, estacionamento municipal), para particulares e empresas. Usa quando o utilizador pergunta se há apoio para comprar um carro, mota, bicicleta ou wallbox elétrica, se há apoio para famílias com poucos rendimentos, que impostos poupa, ou se estaciona de graça na sua cidade."
---

# Incentivos

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- **Nunca dês valores, prazos ou condições de memória.** Os apoios mudam todos os anos e abrem e
  fecham por fases. Usa só os factos do Voltaria (no ohmigo: `ev_rules_portugal` com
  `topic: "incentives"` e uma `query`) ou a página oficial.
- **Cita sempre a fonte e a data** de cada facto: "segundo o Fundo Ambiental, verificado a
  <checkedAt>". Dá a ligação oficial para o utilizador confirmar antes de decidir.
- Se um facto vier marcado `stale`, diz que pode estar desatualizado e manda confirmar na fonte.
- Se não houver nenhum apoio aberto nos factos, diz isso e manda para a página do Fundo Ambiental.
  Não digas que "não há apoios": diz que não conheces nenhum aberto à data dos factos.
- **Um apoio com `validTo` no passado está fechado.** Nunca o apresentes como aberto. Diz sempre a
  edição (`edition`) e as datas.
- **Um apoio com `status: "anunciado"` ainda não existe para candidaturas.** Diz que foi anunciado,
  por quem e quando, e que as regras só valem quando sair o aviso ou o diploma. Não o somes às
  contas do utilizador nem lhe digas para esperar por ele sem dizer que não há data nem valores
  oficiais.

## Histórico

Os apoios do Fundo Ambiental fechados ficam nos factos, um por edição (`series`, `edition`). Usa-os
para:

- comparar anos ("quanto era o apoio em 2022?", "o apoio tem subido ou descido?");
- dizer quando fechou a última edição e quando costuma abrir a seguinte, sem prometer datas;
- ajudar quem já se candidatou a uma edição a perceber as regras que lhe aplicam;
- explicar mudanças de regras, por exemplo quando passou a ser exigido o abate ou mudou o limite de
  preço.

Compara sempre edições pela mesma tipologia (carro para pessoa singular com carro para pessoa
singular) e diz que as regras de cada edição são as do respetivo aviso ou despacho.
- Fontes válidas: só oficiais (Fundo Ambiental, Autoridade Tributária, Diário da República). Não
  uses blogues, marcas ou stands como fonte de um valor. A única exceção são os benefícios
  municipais (`kind: "municipal"`), que vêm da lista da UVE, com a ligação da câmara em `official`.
- Não dês aconselhamento fiscal. Para empresas e trabalhadores independentes, explica a regra e
  sugere confirmar com o contabilista.

## O que perguntar primeiro

Pergunta só o que for preciso para o apoio em causa:

1. **Particular ou empresa** (ou IPSS, autarquia). As regras e os valores mudam.
2. **Que veículo**: carro, mota, bicicleta, trotinete, ou um posto de carregamento.
3. **Novo ou usado.** Os apoios do Fundo Ambiental à compra exigem veículo novo.
4. **Já comprou ou vai comprar**, e em que data. As despesas elegíveis têm uma data a partir da qual
   contam.
5. Para um carro: **preço final com IVA** e se tem um carro a combustão para **abate**. Há limites de
   preço e requisitos de abate.
6. Para um posto: **moradia ou condomínio**. Os factos dizem se o apoio abrange moradias.

## Os tipos de apoio

### Fundo Ambiental: compra de veículos e postos

- Aviso anual ou por fases, com dotação e número de apoios limitados. As candidaturas são
  ordenadas por data e hora de submissão e fecham na data limite ou quando a dotação esgota, o que
  vier primeiro.
- Depois da aprovação há um prazo para aceitar e pedir o pagamento, com faturas em nome do
  beneficiário. Se o utilizador já tem a candidatura aprovada, lembra-o desse prazo.
- O beneficiário fica obrigado a manter o veículo ou o posto durante um período mínimo e não pode
  exportar o veículo.
- Candidatura só online, no site do Fundo Ambiental. Não aceitam documentos por email.

### Anunciados, ainda não abertos

- **Plano Social para o Clima 2026-2032.** O Governo entregou o plano à Comissão Europeia a
  9-10-2026. Inclui apoio a cerca de 5 000 famílias vulneráveis para eletrificar a mobilidade e a
  cerca de 10 000 microempresas dos setores mais expostos ao custo dos combustíveis para eletrificar
  as frotas, geridos pela Agência para o Clima. Depende da aprovação da Comissão e os primeiros
  avisos estão previstos para o 2.º semestre de 2027. Os factos com `series:
  "plano-social-clima"` têm o que é oficial.
- **O que se lê na imprensa não é regra.** No debate do Orçamento do Estado para 2027
  (28-10-2026), a ministra do Ambiente e Energia falou de uma comparticipação de até 80 % do valor do
  carro, de carros usados até cinco anos e de prioridade a quem tem tarifa social de eletricidade. Os
  jornais acrescentaram pagamento por vale, obrigação de manter o carro e valores máximos que não
  coincidem entre si [imprensa]. Nada disto está num aviso nem num diploma. Se o utilizador citar estes números, diz que
  são declarações e estimativas, não regras, e que podem mudar até ao aviso.
- Não digas a quem precisa de carro agora que espere por este apoio: não há data de abertura nem
  garantia de que o caso dele cabe. Diz o que se sabe e manda acompanhar a Agência para o Clima e o
  Fundo Ambiental.

### Impostos (Autoridade Tributária)

- **IUC**: os veículos exclusivamente elétricos estão isentos.
- **IVA** (empresas e independentes com direito à dedução): o IVA da compra ou locação de viaturas
  elétricas ou híbridas plug-in é dedutível até um custo de aquisição definido em portaria, e o IVA
  da eletricidade usada nelas também.
- **Tributação autónoma** (IRC): os encargos com viaturas exclusivamente elétricas só pagam
  tributação autónoma se o custo de aquisição passar o limite da portaria.
- **ISV**: os veículos exclusivamente elétricos estão fora do imposto sobre veículos. Conta ao
  importar um elétrico usado.
- O limite da portaria para os 100 % elétricos, as regras do IVA dos carregadores e da eletricidade
  carregada em casa do colaborador estão nos factos. Não os dês de memória. Para empresas, frotas e
  o carregamento em casa de quem conduz a viatura da empresa, usa a skill `empresas-e-frotas`.

### Câmaras municipais: estacionamento

- Algumas câmaras isentam os carros elétricos do pagamento de estacionamento, ou dão desconto. Os
  factos com `kind: "municipal"` dizem quais, com as condições: se é preciso dístico municipal e
  quanto custa, se vale só para 100 % elétricos ou só para ligeiros de passageiros, se vale só em
  certos parques.
- Estes factos vêm da lista compilada pela UVE, não da câmara. Diz "segundo a lista da UVE,
  verificada a <checkedAt>", dá a ligação da câmara (`official`) e recomenda confirmar lá antes de
  estacionar sem pagar.
- A lista não é exaustiva. Se o município do utilizador não estiver nos factos, não digas que não
  há benefício: manda ver o site da câmara ou da empresa municipal de estacionamento.
- Algumas cidades têm zonas de acesso condicionado de onde os 100 % elétricos estão isentos
  [UVE, vantagens]. O Voltaria não as cobre: manda ver o site da câmara.

### Dístico de veículo elétrico do IMT

- Já não é obrigatório. A Lei n.º 19/2024, de 5 de fevereiro, acabou com essa obrigação e tirou ao
  IMT a competência para emitir o dístico. Não digas ao utilizador para o pedir ao IMT. A história
  do dístico está na skill `regime-2010`.
- Os dísticos já emitidos continuam válidos. Há municípios que ainda o pedem para a isenção de
  estacionamento, e outros que exigem um dístico municipal próprio: os factos dizem qual
  [UVE, dístico IMT].

## Como responder

1. Diz que apoio se aplica ao caso do utilizador, com os valores e as condições dos factos.
2. Diz o estado: aberto, fechado ou esgotado, com as datas.
3. Diz o que é preciso (documentos, abate, prazo) e onde se candidata.
4. Termina com a fonte, a data de verificação e a ligação oficial.

## Fontes

### Legislação

- Código do IUC — Lei n.º 22-A/2007, de 29 de junho:
  https://data.dre.pt/eli/lei/22-a/2007/06/29/p/dre/pt/html
- Código do IVA — Decreto-Lei n.º 394-B/84, de 26 de dezembro:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/codigo-do-iva-indice.aspx
- Código do IRC — Decreto-Lei n.º 442-B/88, de 30 de novembro:
  https://diariodarepublica.pt/dr/detalhe/decreto-lei/442-b-1988-519003
- Lei n.º 19/2024, de 5 de fevereiro (fim da obrigatoriedade do dístico identificativo):
  https://data.dre.pt/eli/lei/19/2024/02/05/p/dre/pt/html

### Normas e standards

- Regulamento (UE) 2017/1151 (homologação WLTP — base das emissões e da autonomia usadas nos
  escalões fiscais): https://eur-lex.europa.eu/eli/reg/2017/1151/oj
- UNECE, Regulamento n.º 101 (consumo de energia e autonomia dos veículos elétricos):
  https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-101-120
- ISO 15118-2 (Plug & Charge — relevante para o apoio à instalação de postos):
  https://www.iso.org/standard/55366.html

### Outras fontes

- Fundo Ambiental: https://www.fundoambiental.pt/
- Governo de Portugal, "Portugal entrega a Bruxelas Plano Social para o Clima de 1,6 mil milhões de
  euros" (9-10-2026), verificado a 2026-11-06:
  https://portugal.gov.pt/pt/gc25/comunicacao/comunicados/portugal-entrega-a-bruxelas-plano-social-para-o-clima-de-16-mil-milhoes-de-euros
- [imprensa] Observador, "Carros usados, 15 mil euros de ajuda e três anos até vender. Como vai
  funcionar o novo apoio à compra de elétricos?" (3-11-2026): só para saber o que foi dito, nunca
  como fonte de um valor:
  https://observador.pt/especiais/carros-usados-15-mil-euros-de-ajuda-e-tres-anos-ate-vender-como-vai-funcionar-o-novo-apoio-a-compra-de-eletricos/
- Portal das Finanças, códigos tributários:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/

Da UVE – Associação de Utilizadores de Veículos Elétricos, verificado a 2026-11-04:

- Lista dos benefícios municipais (fonte dos factos `municipal`): "Municípios com isenção/desconto
  no estacionamento para Veículos Elétricos":
  https://www.uve.pt/page/municipios-com-isencao-desconto-no-pagamento-de-estacionamento-para-veiculos-eletricos/
- [UVE, dístico IMT] "Dístico Identificativo de Veículo Elétrico do IMT":
  https://www.uve.pt/page/distico-identificativo-ve-imt/
- [UVE, vantagens] "Vantagens de um Veículo Elétrico": https://www.uve.pt/page/vantagens-ve/

O que vem da UVE está assinalado com [UVE, …] ou tem a UVE em `source`, e foi reescrito, com
autorização da UVE (ver `docs/fontes/uve.md` no Voltaria). Cita a UVE quando usares esses pontos.
