# Adendo: Simulados UERJ 6 a 15 (50 questões cada), pedido de 17/10/2026

Pedido do aluno: "Ficaram ótimos esses simulados. Agora quero mais 10 simulados de mesmo
estilo, mas agora cada deve ter 50 questões. Mesmo estilo, prova e resolução como pdf.
Me forneça todos, cada um criado em um grupo, e depois um .json completo."

**Vale tudo de `ESPEC.md`** (formato UERJ, 4 alternativas, campos do JSON, proibições,
MCP só leitura), com estas mudanças:

## Tamanho e áreas (por simulado de 50)

| bloco | questões por simulado |
|---|---|
| INF (infectologia) | 6 |
| HEM (hematologia) | 6 |
| REU (reumatologia e imunologia/alergia) | 6 |
| NEF (nefrologia, hidroeletrolítico, ácido-base) | 5 |
| NEU (neurologia) | 5 |
| CAR (cardiologia) | 5 |
| END (endocrinologia) | 5 |
| GAS (5 gastro e hepato + 2 oncologia e paliativos) | 7 |
| PNE (4 pneumologia + 1 de UTI, emergência, geriatria, MBE ou dermatologia clínica) | 5 |

Simulados numerados de 6 a 15. Saída: `simulados/redacao2/<BLOCO>-S<n>.json`, ids
`S<n>-<BLOCO>-01...`.

## Armas por simulado de 50 (alvo)

Rótulo verdadeiro 14 a 17; Grade X / Y 7 a 9; Negativo no meio 5 a 6; Limiar 4 a 5;
Omissão 4 a 5; Cronologia 3 a 4; Droga a deduzir 2 a 3; Dado omitido 2 a 3;
Qualificador 2 a 3. Na sua parte de cada simulado, proporção parecida.

Comando: conduta no máximo 40%; **próximo exame 15 a 20%** (o pior comando dele);
diagnóstico ou etiologia cerca de 30%; fato solto cerca de 10%.

Gabarito na sua parte de cada simulado: A, B, C, D equilibrados (diferença máxima de 1);
armadilha também espalhada (nunca mais da metade numa letra).

## Não repetir NADA do que já existe

Já existem 420 questões: Simulado 1 (`ref/simulado1-resolucao.txt`) e Simulados 2 a 5
(`redacao/*.json`, índice em `entrega/indice.md`). E, na segunda fase, as questões da
primeira fase deste lote (`redacao2/<SEU BLOCO>-S6..S10.json`). Antes de escrever cada
questão, confira com grep: mesmo caso, mesmo ângulo ou mesma resposta é proibido.
Repetir o TEMA com outra decisão é bom (são as lacunas dele); repetir a QUESTÃO não.
Com 500 questões novas, vá fundo nos subtemas: doenças menos óbvias, exceções,
segundas linhas, complicações, interações, populações especiais (gestante, idoso,
DRC, cirrótico, imunossuprimido, HIV).

## Alvos (além dos de ESPEC.md)

- As 7 regras erradas fixadas e as reincidentes UERJ continuam, mas no máximo uma
  aparição de cada regra a cada dois simulados, sempre com ângulo novo.
- Lacunas novas, vindas das questões inéditas que ele errou no app: doenças
  oportunistas no HIV (0 de 4), hemoterapia (0 de 4), farmacodermias (0 de 3:
  SSJ/NET, DRESS, PEGA, reação a anticonvulsivante e alopurinol), imunologia e
  imunodeficiências (0 de 3), mononucleose e diferenciais (0 de 2), acidentes por
  animais peçonhentos (1 de 4: botrópico, crotálico, laquético, elapídico, escorpião,
  aranhas), estenose aórtica (0 de 2), alergia e anafilaxia.
- Padrão dominante: porte e ordem da conduta (fazer mais do que o caso pede, ignorar a
  droga em uso). Próximo exame é o comando a explorar.
