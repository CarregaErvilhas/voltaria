# DGEG como fonte

A DGEG – Direção-Geral de Energia e Geologia (https://www.dgeg.gov.pt/) é a entidade que licencia os
OPC e que aprova as regras técnicas das instalações de carregamento. A sua área de mobilidade
elétrica resume o DL 93/2025, as portarias e os despachos, e tem FAQ próprias.

## Como a usamos

- **Escrevemos por palavras nossas.** O site da DGEG não tem uma licença aberta declarada. Usamos
  os factos e as regras, não o texto.
- **A lei manda.** Sempre que a DGEG resume um artigo, a skill cita o artigo. Os pontos que são só
  leitura da DGEG (as FAQ, os quadros de "quem opera o posto") levam a marca `[DGEG, …]`, para o
  agente os apresentar como posição da DGEG e não como texto da lei.
- O que a DGEG resumia foi confirmado no texto consolidado do DL 93/2025 (versão de 2026-07-31) e
  na Portaria n.º 128/2026/1, no Diário da República.
- As listas de OPC e de CEME mudam: as skills dão a ligação, não copiam as entradas.

## O que veio da DGEG

Verificado a 2026-11-04.

| Página da DGEG | Para onde foi |
|---|---|
| [Mobilidade Elétrica](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/) | Índice; nada de novo |
| [Edifícios](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/edificios/) | `carregar-em-casa`: prédios novos (3680 VA, N = 0,8 + 0,2 × n, sistema de controlo de carga) |
| [Acesso privado](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/acesso-privado/) | `carregar-em-casa`: quem pode instalar (arrendatário, ocupante legal), projeto, EI e técnico até 41,4 kVA, declaração de conformidade, de que quadro ligar, quem opera o posto |
| [Acesso público](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/acesso-publico/) | `carregamento-publico`: etiquetas no posto, botão de corte de emergência |
| [Inspeções periódicas](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/instalacao-de-pontos-de-carregamento/inspecoes-periodicas/) | `carregamento-publico`: inspeção de 5 em 5 anos; postos antes de 2019 sem botão de emergência |
| [Registo e comunicação](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/registo-e-comunicacao/) | Não usado: é para quem quer ser OPC (licença de 10 anos, taxa, deferimento tácito) |
| [Obrigações e direitos](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/obrigacoes-e-direitos/) | `carregamento-publico`: acesso universal, preço antes de começar, acidentes; o resto é para OPC |
| [Regime transitório](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/regime-transitorio/) | `regime-2010`: sem novos CEME, lista dos registados |
| [Lista de OPC](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/lista-de-opc/) e [lista de CEME](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/regime-transitorio/ceme-registados/) | `carregamento-publico`, `regime-2010`: só a ligação |
| [Perguntas Frequentes](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/perguntas-frequentes-faq-s/) | `carregamento-publico`: categorias de potência do AFIR (1.2.9); `carregar-em-casa`: 2.1.1, 2.1.5 a 2.1.7, 2.1.12 a 2.1.17; `regime-2010`: 1.1.2; `glossario.md`: ECVE, EIIEL, ENSE, EADME, EI |
| [Legislação e despachos](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/legislacao-aplicavel-e-despachos-dgeg/) | Já estava na skill `afir` |
| [Guia Técnico, 3.ª ed.](https://www.dgeg.gov.pt/media/dzejui0r/guia-ve-ed-3-2023.pdf) (CTE 64, aprovado pela DGEG a 2023-09-18) | `carregar-em-casa`: tomada doméstica a 10 A, circuito dedicado de 16 A e 2,5 mm², diferencial de 30 mA tipo A ou B, sem extensões, percurso dos cabos na garagem |

Do DL 93/2025, confirmado no texto e não só no resumo da DGEG: arts. 13.º (acesso universal, apoio
ao condutor), 14.º (informação no posto, taxa de ocupação, não discriminação de preços, fatura,
livro de reclamações, acidentes), 16.º (inspeções), 20.º, n.º 8 (lugares reservados), 21.º e 23.º.

## Lido e não usado

- **Licenciamento de OPC**, seguro, taxas, prazos de 12 meses, EADME em detalhe: são para quem
  quer ser operador. A skill `afir` já lista as portarias.
- **Regras técnicas dos postos públicos** (QVE, ligação à RND, distâncias a postos de combustível,
  documentos à EIIEL): são para projetistas e OPC.
- **Casos de retroatividade** nas inspeções (projeto, diferencial por ponto, código AG2): só
  usámos o do botão de emergência, porque explica ao condutor porque um posto antigo pode não o ter.

## Por confirmar ou acompanhar

- A Portaria n.º 128/2026/1 (art. 3.º, n.º 4) previa um guia técnico novo da DGEG 60 dias depois
  de entrar em vigor (março de 2026). A 2026-11-04 a DGEG ainda liga à 3.ª edição, de 2023. Quando
  sair a nova, rever `carregar-em-casa`.
- A ligação do guia mudou: a DGEG usa agora `/media/dzejui0r/guia-ve-ed-3-2023.pdf`. A antiga
  (`/media/5adbxzxo/…`) ainda funciona e está na skill `afir`.
- A skill `afir` aponta o Despacho DGEG n.º 22/2024 para uma cópia no site da MOBI.E. A cópia da
  DGEG é https://www.dgeg.gov.pt/media/kx5einio/despacho-22_2024_ecve.pdf.
