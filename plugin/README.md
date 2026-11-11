# Voltaria

Skills com conhecimento atual e fiável sobre mobilidade elétrica em Portugal, em pt-PT, para o
Claude: carregar em casa e no condomínio, o que o condomínio pode recusar, instalação elétrica,
fichas e tomadas, apoios e benefícios fiscais, carregamento público e MOBI.E, baterias e autonomia,
empresas e frotas, AFIR e o Ponto de Acesso Nacional. Cada skill cita a lei e as normas de onde vem.

O plugin liga também o [ohmigo](https://ohmigo.ocarroeletrico.com), o servidor MCP com os preços de
cada posto público em Portugal: quanto custa um carregamento e onde é mais barato, perto de um sítio
ou numa rota. Quem só quer as regras usa as skills, e o Claude só chama o ohmigo quando a pergunta é
um preço.

## Dados

O plugin não corre código, não guarda nada e não tem hooks. As skills e os factos (`knowledge/`)
são texto que o Claude lê. O único envio de dados é o das chamadas ao ohmigo
(`https://ohmigo.ocarroeletrico.com/mcp`), com o que o assistente põe em cada pergunta (sítio ou
rota, carro, tarifas). O ohmigo não guarda nada ligado a quem pergunta: ver a
[política de privacidade do ohmigo](https://ohmigo.ocarroeletrico.com/privacidade) e a
[do Voltaria](https://voltaria.ocarroeletrico.com/privacidade/).

## Licença e créditos

Conteúdo [CC-BY-4.0](LICENSE). O nome Voltaria e a mascote não estão licenciados.
Fonte, histórico e contributos: https://github.com/CarregaErvilhas/voltaria. Este branch é gerado
em cada release a partir do `main`; não se edita à mão.
