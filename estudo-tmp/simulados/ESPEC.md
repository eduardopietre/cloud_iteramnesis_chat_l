# Especificação dos Simulados UERJ 2, 3, 4 e 5 (80 questões cada)

Pedido do aluno (15/10/2026): "Agora, quero que se inspire nesse modelo E gere mais 4
simulados pareados com resoluções (2 arquivos separados por simulado). Cada um deve
ter 80 questões. Não copie questões desse .pdf. Inspire-se nas que já fizemos."

O modelo é o Simulado UERJ 1 (100 questões, 23/09/2026). O texto da resolução dele
está em `ref/simulado1-resolucao.txt` e os títulos em `ref/simulado1-temas.txt`.
**Nenhuma questão nova pode repetir o caso, o ângulo ou a resposta de uma questão
de lá.** Mesmo tema é permitido só com outro ângulo (outra decisão, outro dado
decisivo, outra resposta). Confira com `grep -i` no txt antes de escrever cada uma.

## Quem é o aluno (resumo; leia também as memórias citadas)

R+ Clínica Médica, alvo UERJ. Leia, só para leitura, pelo MCP `iteramnese-coach`
(`memory_read`): `uerj-banca-perfil`, `uerj-raiz-confirmacao`,
`uerj-temas-recorrentes`, `padrao-degrau-de-conduta`, `lote-15-10-2026-diagnostico`
e a(s) memória(s) da sua área (lista em `memory_list`). E leia
`../sintese.md` (diagnóstico de 15/10/2026) e as análises por prova em
`../provas/*.md` da sua área: são as questões "que já fizemos" e a inspiração.

Pontos que as questões devem atacar (os que importam mais primeiro):
1. **As 7 regras erradas fixadas** (erradas de novo logo depois de ver o gabarito):
   razão glicorraquia/glicemia no líquor da TB; crise provocada (hiponatremia,
   distonia aguda, HSA) tratada com fenitoína sem indicação; Marfan (síndrome para
   lesão valvar); ELA x mielopatia cervical; oftalmoplegia internuclear; DHGNA com
   FIB-4 (menor que 1,3 repete; 1,3 a 2,67 elastografia; maior que 2,67
   hepatologista); hiperferritinemia metabólica (IST abaixo de 45% não é sobrecarga
   de ferro).
2. **Reincidentes UERJ**: SPA2 com cálcio normal, AVC cerebelar no etilista, IM
   crônica (ausculta), Löffler/endomiocardiofibrose, AR com DPI, nódulo pulmonar
   (ressecção x biópsia), DPI (perguntar exposição antes de LBA), osteomalácia
   pós-bariátrica, hiponatremia na IC.
3. **Padrão dominante: porte e ordem da conduta.** Ele faz MAIS do que o caso pede
   (exame do degrau seguinte, exótico antes do simples, tratar o que não precisa) e
   ignora a droga em uso e o antecedente da primeira linha. Próximo exame é o pior
   comando (43%). Muitas questões devem ter a resposta certa como o degrau mais
   simples, a omissão, ou a ordem correta, com a armadilha sendo o exame/tratamento
   a mais.
4. **Exame que decide lido como enfeite** quando um rótulo forte vem antes: o número
   do líquido, a saturação de transferrina, o ECG, a FE, o sódio, o complemento.
5. **Rótulo verdadeiro** que puxa a doença de manual (a arma mais letal da UERJ).
6. Temas UERJ recorrentes que ele erra: lítio, CAD e fluidos, Still, IgG4,
   linfoma por subtipo, HIV oportunista fora da TB, LES como cenário de outra
   doença, amiloidose, policitemia.

## Formato UERJ (obrigatório)

- **4 alternativas (A a D)**, curtas: de uma a seis palavras, no máximo cerca de
  dez. As quatro com a mesma forma (se uma é conduta, as quatro são condutas) e
  comprimento parecido. Cada uma é a resposta certa de um caso vizinho.
- **Enunciado**: caso clínico de 5 a 12 linhas (identificação, tempo de evolução,
  comorbidades e drogas, negativos que importam, exame físico com sinais vitais,
  exames com valores e referências quando preciso) e depois o comando. Varie: cerca
  de 10% podem ser perguntas diretas curtas sem caso (fato solto), porque a UERJ
  usa. Não nomeie o diagnóstico quando a questão é identificá-lo. Nunca escreva
  "clássico", "típico", "patognomônico".
- **Comando**: quase nunca negativo (no máximo 2 por simulado com EXCETO). A UERJ
  qualifica o comando ("para prevenção", "isoladamente", "inicialmente", "a mais
  adequada neste momento").
- **Grade "X / Y, respectivamente"**: cerca de 15 a 18% das questões, as quatro
  alternativas sendo as combinações de duas decisões.
- **Nível**: difícil ou extremamente difícil em pelo menos 85%; média no resto. Nada
  fácil. Teste do quintanista: se um bom aluno do 5º ano acerta sem pensar, refaça.
  Escreva para você mesmo as duas finalistas e o dado único que as separa.
- **Diretrizes**: preferir as brasileiras (SBC, SBD, SBEM, SBR, SBPT, SBN, MS/PCDT,
  V Consenso H. pylori 2026) e as internacionais vigentes em 2026 (KDIGO, GOLD 2026,
  GINA 2026, AHA/ASA, ESC, SSC, IDSA, ACR/EULAR, Endocrine Society, ADA 2026). Se a
  posição for discutível, não use a questão.
- Português do Brasil. **Sem travessão** (— ou –) em nenhum texto: use dois-pontos,
  vírgula, parênteses.

## As armas da banca (distribuição alvo por simulado de 80)

| arma | alvo por simulado |
|---|---|
| Rótulo verdadeiro | 22 a 26 |
| Grade X / Y | 12 a 15 |
| Negativo no meio | 8 a 10 |
| Limiar | 6 a 8 |
| Omissão (a resposta é não fazer, ou o degrau mais simples) | 6 a 8 |
| Cronologia | 5 a 6 |
| Droga a deduzir | 3 a 4 |
| Dado omitido | 3 a 4 |
| Qualificador | 3 a 5 |

Use exatamente estes nomes no campo `arma`. Como cada redator escreve cerca de 1/9
de cada simulado, mantenha na sua parte de cada simulado proporção parecida.

Comando, alvo por simulado: conduta 30 a 35%, próximo exame 12 a 15%, diagnóstico
ou etiologia 30 a 35%, fato solto curto cerca de 10%, mecanismo/achado esperado o
resto.

## Gabarito

Na sua parte de cada simulado, distribua as corretas igualmente entre A, B, C e D
(diferença máxima de 1). A armadilha (`armadilha`) é a errada que o apressado marca,
nunca a correta.

## Saída: um JSON por redator

Grave UM ARQUIVO POR SIMULADO em `simulados/redacao/<BLOCO>-S<n>.json` (BLOCO dado na sua tarefa; n = 2, 3, 4, 5), cada um com uma lista de
objetos, um por questão, exatamente com estes campos:

```json
{
  "id": "S2-INF-01",
  "simulado": 2,
  "area": "Infectologia",
  "titulo": "Tema curto · com o ângulo (como no modelo: 'Sífilis: critério de resposta sorológica e punção lombar na pessoa com HIV')",
  "arma": "Rótulo verdadeiro",
  "comando": "conduta | próximo exame | diagnóstico | etiologia | fato solto | mecanismo | achado esperado",
  "nivel": "difícil",
  "enunciado": "Caso... Comando:",
  "alternativas": {"A": "...", "B": "...", "C": "...", "D": "..."},
  "gabarito": "C",
  "armadilha": "A",
  "dado_decisivo": "trecho copiado LITERALMENTE do enunciado",
  "resolucao": "Um parágrafo de 4 a 8 frases: por que a armadilha atrai, qual dado decide e o raciocínio completo.",
  "comentarios": {
    "A": "Errada. Em que caso vizinho seria a certa e qual dado deste caso a derruba.",
    "B": "Errada. ...",
    "C": "Correta. O dado do caso que a sustenta.",
    "D": "Errada. ..."
  },
  "para_levar": "Uma ou duas frases com a regra generalizável.",
  "referencias": "Diretriz(es) com ano.",
  "tags": ["nome EXATO de tema do vocabulário do aluno"],
  "sourceQuestionId": "id de 15 hex da questão do banco que inspirou, ou null",
  "alvo": "qual lacuna/padrão do aluno esta questão ataca (uma linha)"
}
```

- `tags`: de 1 a 3 nomes EXATOS do vocabulário do aluno. Confirme cada um com
  `topic_list` (parâmetro `filter`) do MCP. Prefira a tag folha (ex.: "Síndrome
  Nefrótica (CM)"). Tag inexistente é recusada pelo app.
- `sourceQuestionId`: quando a ideia nasceu de uma questão do banco dele (das
  análises em `../provas/`, ou achada com `question_list`/`question_search`/
  `topic_analyze`, de preferência erros e de preferência UERJ), ponha o id; senão
  null. A questão nova NÃO pode ser paráfrase da fonte: outro ângulo.
- `dado_decisivo` tem de ser substring exata de `enunciado`.
- Valide o JSON no fim (`python3 -c "import json;json.load(open(...))"`), confira
  que cada `dado_decisivo` está no enunciado e conte gabaritos e armas por simulado.

## Ferramentas MCP permitidas (só leitura)

memory_list, memory_read, topic_list, topic_analyze, question_list, question_get,
question_search, question_history, performance_stats. Carregue com ToolSearch
("select:mcp__iteramnese-coach__<nome>,..."). **Proibido** escrever no servidor
(memory_create/update/delete, iterq_create, flashcard_*): quem grava é o
coordenador.
