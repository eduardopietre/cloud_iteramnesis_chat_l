# Verificação do Simulado UERJ 2 (2026-10-15)

Fonte da verdade: `S2-lote1.json` a `S2-lote4.json` (80 questões, 1 a 80, sem duplicata).

## Método

- `iterq_list` com group "Simulado UERJ 2", limit 100: 80 linhas, 80 ids distintos.
- `iterq_get` das 80, em 8 chamadas de 10. As respostas foram extraídas do
  transcript da sessão para arquivos JSON por script, sem transcrição manual.
- Script Python: casamento pelo prefixo "[Simulado UERJ 2, questão m]" e
  comparação exata (sem normalizar espaços) de enunciado, texto e feedback das 4
  alternativas, letra, gabarito, temas (com ordem), nível, decisor e armadilha;
  varredura de caracteres não ASCII fora do alfabeto latino (cirílico, grego etc.)
  no app e na fonte.

## Resultado da primeira conferência

- 80 de 80 presentes, numeração 1 a 80 completa, sem duplicata, nenhuma de outro grupo.
- Nenhum caractere fora do alfabeto latino, nem no app nem na fonte.
- Gabarito, alternativas, feedbacks, temas, nível e armadilha idênticos nas 80.
- 3 questões divergentes, todas erros de grafia no enunciado:

| Questão | id | Campo | No app | Na fonte |
|---|---|---|---|---|
| 55 | 73979a3ca8a7785 | enunciado (2 ocorrências) e decisor | podáctilo | pododáctilo |
| 62 | c47b035b8eba314 | enunciado | pletóra | pletora |
| 73 | 99a9f9d602c38da | enunciado | enterocútanea | enterocutânea |

## Correções

`iterq_update` nas três, só com os campos divergentes e o valor exato do arquivo
(q55: statement e decider; q62 e q73: statement). As três foram aceitas.

## Conferência final

Novo `iterq_get` das três e nova execução do script sobre as 80: 0 divergências.
Nada foi criado nem apagado.
