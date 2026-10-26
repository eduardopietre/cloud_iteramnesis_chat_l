# Simulados de revisão R01 a R04 (50 questões cada), pedido de 26/10/2026

Pedido do aluno: "a partir desses erros elabore mais 200 questões divididas em 4 novos
simulados r01 a r04, com prova e solução. Explore também assuntos pouco explorados na
prova inicial. Mantenha o estilo da UERJ." E, logo depois: "O alvo deve ser
exclusivamente a UERJ e os simulados que te mandei as respostas."

Portanto há DUAS fontes de alvo, e só elas:
1. **Os erros dele nos Simulados 1 a 4** (`ERROS_S1_S4.md`, 139 erros, com o que ele
   marcou, o certo e o dado que decidia). Os textos completos dessas questões estão em
   `ref/simulado1-resolucao.txt` (S1) e em `build/out/simulado2.json` a
   `simulado4.json` (S2 a S4, campo `numero`).
2. **A UERJ**: perfil da banca e temas que ela repete (memórias `uerj-banca-perfil` e
   `uerj-temas-recorrentes`, leia pelo MCP). "Assuntos pouco explorados na prova
   inicial" = temas que a UERJ cobra e que o Simulado 1 (`ref/simulado1-temas.txt`)
   e os Simulados 2 a 4 quase não tocaram na sua área. Nada fora da UERJ: nenhum tema
   que não seja da prova de R+ Clínica Médica da UERJ.

Vale todo o formato de `ESPEC.md` (4 alternativas curtas, campos do JSON, proibições,
tags exatas, MCP só leitura, sem travessão, sem "clássico/típico/patognomônico").
Mudanças estão abaixo.

## Proporção de alvo, na sua parte de cada simulado

- Cerca de 70%: **um erro do dossiê da sua área por questão**, com o mesmo conceito e
  OUTRO caso e ângulo. Não é reescrever a questão errada: é cobrar a regra que ele
  errou num cenário novo (outra doença em que o mesmo dado decide, o mesmo rótulo
  plantado puxando para outro lado, a mesma regra vista pela conduta em vez do
  diagnóstico, a exceção). Registre em `alvo` qual erro: "S3 q16: lítio contra
  resposta à desmopressina". Cubra o maior número possível de erros diferentes da sua
  área nos 4 simulados; erro reincidente (o mesmo tema errado em dois simulados) pode
  voltar uma segunda vez, em simulado diferente.
- Cerca de 30%: **tema UERJ recorrente ou detalhe de especialista que a UERJ cobra**
  (subtipo, epônimo, doença rara, posição de diretriz brasileira) e que os
  Simulados 1 a 4 quase não exploraram na sua área. Confira com grep em
  `ref/simulado1-temas.txt` e nos títulos de `build/out/simulado2.json` a
  `simulado4.json`. Registre em `alvo`: "UERJ pouco explorado: ...".

## Os padrões dele (todos medidos nos Simulados 1 a 4)

- **Rótulo verdadeiro vence o dado que discrimina** (o maior agora): diagnóstico caiu
  de 75% para 38% do S1 ao S4. O antecedente, o parente, a exposição ou a droga é
  verdadeiro e puxa para a doença de manual; o exame no fim do caso derruba.
- **Grade X / Y aceita pela metade**: acerta o diagnóstico e erra a conduta por não
  ler o critério de gravidade (SINS, embolia sob antibiótico, creatinina na malária,
  Child C, crise renal esclerodérmica).
- **Porte da conduta nos dois sentidos**: exagera no estável (biópsia, TC, corticoide,
  imunossupressão, profilaxia sem indicação) e subtrata no grave (alta precoce,
  aguardar diálise, radioterapia isolada com instabilidade).
- **Droga em uso não cruzada**: anticoncepcional falseando dexametasona, colírio
  betabloqueador, sulfato de magnésio na miastenia, metotrexato com SMX-TMP,
  rifampicina com dolutegravir, biotina, zinco, alergia a sulfa, G6PD.
- **Qualificador** (3 de 10): "o mais frequente", "isoladamente", VPP x sensibilidade.
- **Achado esperado / semiologia** (0 de 8): síndrome para lesão e ausculta (Marfan,
  Turner, CIA ostium secundum x primum, aortite sifilítica, IM crônica).
- **Regras fixadas que oscilam** (certo num simulado, errado no seguinte): ELA x
  mielopatia, FIB-4 (1,3 e 2,67, enzimas normais não excluem), anticrise na crise
  provocada (fenitoína, levetiracetam na abstinência), razão glicorraquia/glicemia,
  hiperferritinemia metabólica (saturação abaixo de 45%). Lítio 1 de 4. G6PD 0 de 2.
  HIV como cenário 2 de 6 (HTLV-1, LEMP, sífilis maligna, Burkitt, ILTB no contato).

## Áreas por simulado (50) e o seu bloco

| bloco | área | por simulado | arquivos |
|---|---|---|---|
| INF | Infectologia (inclui HIV) | 6 | `redacao3/INF-R01.json` ... `INF-R04.json` |
| HEM | Hematologia e oncohematologia | 5 | `HEM-R0n.json` |
| REU | Reumatologia, imunologia e alergia | 6 | `REU-R0n.json` |
| NEF | Nefrologia, hidroeletrolítico, ácido-base | 5 | `NEF-R0n.json` |
| NEU | Neurologia | 5 | `NEU-R0n.json` |
| CAR | Cardiologia (semiologia pesa) | 6 | `CAR-R0n.json` |
| END | Endocrinologia (pior área dele: 13 de 31) | 6 | `END-R0n.json` |
| GAS | Gastroenterologia e hepatologia | 4 | `GAS-R0n.json` |
| PNE | Pneumologia (3 de 12 nos S2 e S3) | 4 | `PNE-R0n.json` |
| ONC | Oncologia, paliativos, emergência, UTI, MBE (como a UERJ cobra) | 3 | `ONC-R0n.json` |

Ids: `R01-INF-01`, `R01-INF-02`... O campo `simulado` recebe a string `"R01"` (e assim
por diante). Gravar em `simulados/redacao3/`.

## Armas e comandos (proporção na sua parte de cada simulado)

Armas em 50: Rótulo verdadeiro 14 a 16; Grade X / Y 8 a 10; Negativo no meio 5;
Qualificador 4; Limiar 4; Droga a deduzir 4; Omissão 3 a 4; Dado omitido 3;
Cronologia 2. Use exatamente estes nomes.

Comando em 50: diagnóstico ou etiologia cerca de 40% (o que caiu); conduta cerca de
30%; próximo exame cerca de 15%; achado esperado cerca de 6% (concentre em CAR e NEU);
fato solto curto cerca de 8% (a UERJ usa pergunta direta).

Nível: difícil ou extremamente difícil em pelo menos 85%. Teste do quintanista.

Gabarito na sua parte de cada simulado: A, B, C, D equilibrados (diferença máxima de 1);
armadilha espalhada (nunca mais da metade numa letra). Prefira textos de resolução e
comentários que NÃO citem letras (citem o conteúdo), para que as alternativas possam
ser reordenadas depois.

## Não repetir NADA do que já existe

Já existem 920 questões: Simulado 1 (`ref/simulado1-resolucao.txt`), Simulados 2 a 5
(`redacao/*.json`) e 6 a 15 (`redacao2/*.json`). Antes de escrever cada questão,
confira com grep: mesmo caso, mesmo ângulo ou mesma resposta é proibido. O alvo é o
mesmo CONCEITO que ele errou, cobrado por outro caso; a questão nova não pode ser
paráfrase da errada nem de nenhuma outra existente.

## Entrega

Ao terminar: valide o JSON, confira `dado_decisivo` no enunciado, conte gabarito,
armadilha, arma e comando por arquivo. Resposta final em no máximo 12 linhas: quantas
questões, quantos erros do dossiê cobertos (liste os ids S?q?) e quantas de tema UERJ
pouco explorado.
