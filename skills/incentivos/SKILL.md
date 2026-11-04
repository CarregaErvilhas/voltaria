---
name: incentivos
description: Responde a perguntas sobre apoios e benefícios fiscais para veículos elétricos e postos de carregamento em Portugal (Fundo Ambiental, IUC, IVA, tributação autónoma), para particulares e empresas. Usa quando o utilizador pergunta se há apoio para comprar um carro, mota, bicicleta ou wallbox elétrica, ou que impostos poupa.
---

# Incentivos

Escrito para ti, o assistente. Responde na língua do utilizador. Os termos seguem o `glossario.md`
do Voltaria.

## Regras

- **Nunca dês valores, prazos ou condições de memória.** Os apoios mudam todos os anos e abrem e
  fecham por fases. Usa só os factos do Voltaria (no ohmigo: `get_facts` com `topic: "incentivos"`)
  ou a página oficial.
- **Cita sempre a fonte e a data** de cada facto: "segundo o Fundo Ambiental, verificado a
  <checkedAt>". Dá a ligação oficial para o utilizador confirmar antes de decidir.
- Se um facto vier marcado `stale`, diz que pode estar desatualizado e manda confirmar na fonte.
- Se não houver nenhum apoio aberto nos factos, diz isso e manda para a página do Fundo Ambiental.
  Não digas que "não há apoios": diz que não conheces nenhum aberto à data dos factos.
- Fontes válidas: só oficiais (Fundo Ambiental, Autoridade Tributária, Diário da República). Não
  uses blogues, marcas ou stands como fonte de um valor.
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

### Impostos (Autoridade Tributária)

- **IUC**: os veículos exclusivamente elétricos estão isentos.
- **IVA** (empresas e independentes com direito à dedução): o IVA da compra ou locação de viaturas
  elétricas ou híbridas plug-in é dedutível até um custo de aquisição definido em portaria, e o IVA
  da eletricidade usada nelas também.
- **Tributação autónoma** (IRC): os encargos com viaturas exclusivamente elétricas só pagam
  tributação autónoma se o custo de aquisição passar o limite da portaria.
- Os valores e o limite da portaria vêm dos factos. Não os dês de memória.

### Câmaras municipais

- Algumas câmaras têm benefícios próprios (por exemplo estacionamento). O Voltaria ainda não os
  cobre: manda o utilizador ver o site da câmara.

## Como responder

1. Diz que apoio se aplica ao caso do utilizador, com os valores e as condições dos factos.
2. Diz o estado: aberto, fechado ou esgotado, com as datas.
3. Diz o que é preciso (documentos, abate, prazo) e onde se candidata.
4. Termina com a fonte, a data de verificação e a ligação oficial.

## Fontes

- Fundo Ambiental: https://www.fundoambiental.pt/
- Portal das Finanças, códigos tributários:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/
