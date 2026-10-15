# Verificação S3 a S5: banco do Iteramnese contra os JSON de carga, 2026-10-15

Fonte da verdade: `S<n>-lote1..4.json` nesta pasta. Gravado: `iterq_list` (group, limit 100) e
`iterq_get` dos 240 ids, 10 por chamada. As respostas foram extraídas sem transcrição, direto do
registro da sessão, para `/tmp/claude-0/verif/raw/` (list-3/4/5.json, get-*.json), e comparadas por
script (`/tmp/claude-0/verif/compare.py`).

Campos comparados, casando pelo prefixo "[Simulado UERJ n, questão m]": enunciado; texto e feedback
das 4 alternativas na ordem (letras A a D); gabarito; temas (mesma ordem); e também nível, decisor
e armadilha. Normalização: só espaços nas pontas. Varredura de caracteres fora do alfabeto latino
(cirílico, grego etc.) em todos os campos, gravados e de origem.

## Contagem

| Grupo | No grupo | Números | Duplicatas | Conferiram de primeira | Corrigidas |
|---|---|---|---|---|---|
| Simulado UERJ 3 | 80 | 1 a 80, completos | nenhuma | 80 | 0 |
| Simulado UERJ 4 | 80 | 1 a 80, completos | nenhuma | 77 | 3 |
| Simulado UERJ 5 | 80 | 1 a 80, completos | nenhuma | 80 | 0 |

## Correções (iterq_update com o valor exato do JSON; depois iterq_get e novo diff: idênticas)

1. S4 questão 63, `0dfbbc407b49517`: feedback da alternativa B tinha "sideробlástica" (р U+0440,
   о U+043E, б U+0431 cirílicos). Enviadas as 4 alternativas (text + feedback) do S4-lote4.json.
2. S4 questão 55, `f01085a817cdec6`: "meropénem" no lugar de "meropeném" no enunciado e nos
   textos das alternativas B e C. Enviados enunciado e as 4 alternativas do S4-lote3.json.
3. S4 questão 71, `2dceabf95e9218b`: "meropénem" no lugar de "meropeném" no enunciado. Enviado o
   enunciado do S4-lote4.json.

O servidor aceitou as três atualizações sem recusa e manteve a grafia enviada.

## Observações

- S5 questão 23 (`b51aaacd6bfaade`) tem "APOE ε4" com épsilon grego: está igual no JSON de origem,
  não é erro de cópia.
- Nenhuma questão faltando, nenhuma duplicata, nenhuma questão de um grupo gravada em outro.
- Pendência herdada do S4-resultado.md: as questões 61 a 63 do S4 foram criadas com
  rubricBypass.userRequest = "PLACEHOLDER-DO-NOT-SEND". O conteúdo delas agora confere com o JSON;
  o registro do pedido do aluno nesse lote não foi alterado (iterq_update não mexe nele).
