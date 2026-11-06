# Evals do Voltaria

Medem se uma skill muda a resposta do modelo, por pergunta, por skill, por categoria e por secção.
O objetivo é cortar o que não muda nada.

- `questions.json`: o banco de perguntas, com a rubrica de cada uma.
- `config.json`: modelos fixados, orçamento, limiares, perguntas do smoke.
- `run.py`: runner, juiz, ablação e relatórios. Só stdlib (o backend `api` precisa do SDK).

## Como correr

Da raiz do repo:

```bash
python3 evals/run.py check                          # valida o banco contra skills/ (sem custo)
python3 evals/run.py run --smoke                    # 10 perguntas, sem e com skill
python3 evals/run.py run --budget 12                # o banco inteiro
python3 evals/run.py ablate --skill sub-cpe --cited-only
python3 evals/run.py sections --skill sub-cpe       # as secções e quantas perguntas citam cada uma
```

Cada comando escreve `evals/runs/<data>-<tipo>/report.md` e `results.json`. `report <dir>` volta a
gerar o relatório. `--dry-run` mostra a estimativa e para. Filtros: `--ids`, `--skill`, `--category
ad`, `--limit`. `--reps 3` repete cada resposta (necessário para medir ruído antes de cortar).

**Autenticação.** O backend por omissão é `cli`: `claude -p` sem ferramentas, sem MCP, sem
settings, sem `CLAUDE.md`, numa pasta vazia. Precisa de `claude auth login` feito no terminal. A
alternativa é `--backend api`, com `pip install anthropic` e `ANTHROPIC_API_KEY` no ambiente.
`--backend mock` não chama modelos: serve para testar o pipeline.

## O que faz

1. **Duas respostas por pergunta.** Sem skill: só um prompt base (pt-PT, a data de hoje, a lista
   das ferramentas do ohmigo, que nesta avaliação não se podem chamar). Com skill: o mesmo prompt,
   mais os `SKILL.md` das skills da pergunta, o `glossario.md` e, para `incentivos` e
   `empresas-e-frotas`, os factos de `knowledge/incentives.json` (o que `get_facts` devolveria).
2. **Juiz.** Um segundo modelo, que não sabe de que braço vem a resposta, marca cada item `must`
   (cumpre ou não) e `must_not` (viola ou não). Os `must_not` com `regex` também são verificados
   por regex: um acerto conta como violação, diga o juiz o que disser. Nota = itens certos ÷ itens.
3. **Δ = com − sem**, agregado por skill e por categoria. O relatório separa as perguntas que
   melhoram (Δ ≥ 0,2), as que não mudam e as que pioram, e lista o que a resposta com skill ainda
   falha.
4. **Ablação.** Tira uma secção `##` de cada vez (`--depth 3` também cada `###`) e volta a
   responder às perguntas da skill. Veredicto por secção:
   - **cortar?**: as perguntas que a citam (`source`) não descem e nenhuma desce mais de 0,34;
   - **manter**: descem;
   - **sem perguntas**: nenhuma pergunta a cita, por isso não se sabe. Escrever perguntas antes de
     cortar.

Respostas e notas ficam em cache (`evals/.cache/`), indexadas pelo modelo, pelo prompt e pela
pergunta. Repetir um comando não custa nada. Mudar uma skill só paga as perguntas dessa skill. A
ablação reaproveita as respostas com a skill inteira de um `run` anterior.

## Custo

Modelos fixados em `config.json`: respostas com `claude-sonnet-5-5`, juiz `claude-opus-5-5`,
ambos com effort `medium`. Estimativas do `--dry-run`, por repetição, sem contar com o prompt
caching (o custo real deve ficar abaixo):

| Execução | Chamadas | Estimativa |
|---|---|---|
| `run --smoke` (10 perguntas) | 20 respostas + 20 notas | ~1 USD |
| `run` (84 perguntas) | 168 + 168 | ~8 USD |
| `ablate --skill X --cited-only` | 9 a 29 de cada | 0,5 a 1,9 USD por skill; ~12 USD as 12 |
| `ablate --skill X` (todas as perguntas por secção) | 100 a 140 de cada | 6 a 9 USD por skill |

Com `--reps 3`, vezes três. O juiz é cerca de metade do custo: passá-lo para Sonnet em
`config.json` corta-o a metade, à custa de notas menos fiáveis. Com `claude -p` numa subscrição, o
custo reportado é o equivalente em API e gasta a quota do plano, não é faturado.

O orçamento por omissão é `budget_usd` (3 USD). Acima dele, o comando recusa arrancar e diz o
`--budget` que é preciso; durante a execução, para quando o gasto real o passa.

## Acrescentar perguntas

Em `questions.json`, uma entrada por pergunta:

```json
{
  "id": "sub-11",
  "skills": ["sub-cpe"],
  "category": "e",
  "persona": "administrador",
  "question": "A pergunta como a faria um condutor, eletricista, administrador ou gestor de frota.",
  "must": ["Um facto ou comportamento por item, verificável sozinho"],
  "must_not": ["Uma resposta errada conhecida", {"text": "Dá preços em euros", "regex": "\\d+\\s?€"}],
  "source": ["sub-cpe#Quanto custa"]
}
```

- `category`: a lei depois do corte do modelo (`a`), factos portugueses raros (`b`), processos e
  decisões locais (`c`), comportamento (`d`), erros comuns a corrigir (`e`).
- `must`: um item por facto. Itens largos ("explica o sub-CPE") passam sempre e não medem nada.
- `must_not`: o erro que o modelo dá sem a skill. Só ponha `regex` quando uma resposta certa nunca
  lhe acertaria (preços, telefones); corrigir um erro ("já não são 60 dias") não pode contar como
  violação.
- `source`: `skill#Título exato da secção`. É o que liga a pergunta à ablação. `check` falha se o
  título não existir.
- Para o smoke, acrescentar o `id` a `smoke_ids` em `config.json`.

Correr `python3 evals/run.py check` antes de fazer commit.

## Limites

- **O juiz é um modelo.** Uma rubrica mal escrita dá Δ errado. Ler as respostas das perguntas que
  mudam muito antes de tirar conclusões (estão em `results.json`).
- **Ruído.** Com uma repetição, um Δ de 0,2 numa pergunta pode ser sorte. Para decidir um corte,
  `--reps 3`, e o relatório mostra o desvio entre repetições.
- **As ferramentas não correm.** O modelo diz que ferramenta chamaria; as perguntas de
  comportamento (`d`) avaliam isso, não o resultado da ferramenta.
- **A ablação mede só o que as perguntas perguntam.** "cortar?" quer dizer que nenhuma pergunta do
  banco precisa da secção. Antes de apagar, confirmar que não há uma pergunta realista que falte.
- O `skill-creator` tem evals de *triggering* (se a descrição faz o modelo ler a skill) e um juiz
  por agente sobre ficheiros produzidos. Não serve aqui, onde a skill vai sempre no prompt e se
  compara texto. Daqui ficou o formato `expectations` (aqui `must`) e a forma de lançar `claude -p`
  aninhado.
