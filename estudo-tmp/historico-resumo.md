# Histórico das 350 questões capturadas em 2026-10-15

Levantamento mecânico via `exam_get` + `question_history` (servidor iteramnese-coach). Dados por questão em `historico.psv`.

Corte: tentativa "anterior" = dia anterior a 2026-10-15. Com várias anteriores, a classe usa a mais recente.

Provas: 13. Questões: 350. Divergências entre índice e histórico: 0.

## Contagem por classe (total)

| Classe | Questões | Acertos hoje |
|---|---|---|
| NOVA | 247 | 139/247 |
| DUP_LOTE | 41 | 18/41 |
| REP_CORRIGIU | 18 | 18/18 |
| REP_MANTEVE_ACERTO | 31 | 31/31 |
| REP_REGREDIU | 2 | 0/2 |
| REP_ERROU_DE_NOVO_MESMA | 7 | 0/7 |
| REP_ERROU_DE_NOVO_OUTRA | 4 | 0/4 |
| **Total** | 350 | 206/350 |

## Contagem por classe, por prova

| Prova | Total | Placar | NOVA | DUP | CORR | MANT | REGR | ERR_MESMA | ERR_OUTRA |
|---|---|---|---|---|---|---|---|---|---|
| 057b89e0581a057 | 47 | 29/47 | 18 | 14 | 5 | 9 | 1 | 0 | 0 |
| 63433bb9ae3aae7 | 40 | 25/40 | 34 | 0 | 2 | 4 | 0 | 0 | 0 |
| dec6df94ebc6203 | 30 | 14/30 | 22 | 0 | 2 | 4 | 0 | 2 | 0 |
| c7aeca7cad19860 | 25 | 13/25 | 16 | 1 | 1 | 5 | 0 | 0 | 2 |
| 4bb26343ad0e886 | 19 | 14/19 | 10 | 6 | 0 | 3 | 0 | 0 | 0 |
| b34e2bfc405e4d3 | 30 | 19/30 | 24 | 0 | 2 | 4 | 0 | 0 | 0 |
| 7b5f67f1aa80412 | 30 | 14/30 | 22 | 6 | 1 | 0 | 0 | 1 | 0 |
| aff4e3d49db69d4 | 20 | 10/20 | 4 | 14 | 1 | 0 | 0 | 1 | 0 |
| e0e342921bdebe8 | 14 | 9/14 | 12 | 0 | 1 | 0 | 0 | 0 | 1 |
| c897c7609e2258f | 20 | 17/20 | 19 | 0 | 0 | 1 | 0 | 0 | 0 |
| 065f0e3df14129c | 50 | 26/50 | 45 | 0 | 2 | 1 | 1 | 1 | 0 |
| 13c23806bd1877b | 10 | 5/10 | 6 | 0 | 1 | 0 | 0 | 2 | 1 |
| 1d0d1d1636eb939 | 15 | 11/15 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | 350 | 206/350 | 247 | 41 | 18 | 31 | 2 | 7 | 4 |

Legenda: DUP = DUP_LOTE, CORR = REP_CORRIGIU, MANT = REP_MANTEVE_ACERTO, REGR = REP_REGREDIU, ERR_MESMA / ERR_OUTRA = REP_ERROU_DE_NOVO com a mesma letra / outra letra.

## Placar das questões NOVA (não contaminado)

| Prova | Acertos/NOVA | % |
|---|---|---|
| 057b89e0581a057 | 7/18 | 39% |
| 63433bb9ae3aae7 | 19/34 | 56% |
| dec6df94ebc6203 | 8/22 | 36% |
| c7aeca7cad19860 | 7/16 | 44% |
| 4bb26343ad0e886 | 7/10 | 70% |
| b34e2bfc405e4d3 | 13/24 | 54% |
| 7b5f67f1aa80412 | 13/22 | 59% |
| aff4e3d49db69d4 | 3/4 | 75% |
| e0e342921bdebe8 | 8/12 | 67% |
| c897c7609e2258f | 16/19 | 84% |
| 065f0e3df14129c | 23/45 | 51% |
| 13c23806bd1877b | 4/6 | 67% |
| 1d0d1d1636eb939 | 11/15 | 73% |
| **Total** | 139/247 | 56.3% |

## REP_ERROU_DE_NOVO_MESMA: errou antes e errou hoje com a mesma letra (7)

| Prova | n | id | Hoje (marcou/gab) | Tentativas anteriores (dia:prova:res:letra) | Mesmo dia em outra prova |
|---|---|---|---|---|---|
| dec6df94ebc6203 | 16 | 3055763ee87b5c7 | E B/A | 2026-08-05:923e49d3c1c516d:E:B | - |
| dec6df94ebc6203 | 17 | fc91823ae26406e | E B/C | 2026-08-05:923e49d3c1c516d:E:B | - |
| 7b5f67f1aa80412 | 10 | fd9bfae8c4a73ba | E C/D | 2026-09-21:5384d41f4368772:E:C | - |
| aff4e3d49db69d4 | 19 | f20cff986f4800d | E C/A | 2026-09-21:ee2783053bb25cb:E:C | 057b89e0581a057:10:C:A |
| 065f0e3df14129c | 33 | 47bfa207b5faa5a | E A/B | 2026-08-19:e48245c7c0ea42e:E:A | - |
| 13c23806bd1877b | 1 | ab2095024550478 | E A/B | 2026-09-21:ee2783053bb25cb:E:A | - |
| 13c23806bd1877b | 8 | b4253d1db43e0d4 | E B/D | 2026-09-21:5384d41f4368772:E:B | - |

## REP_ERROU_DE_NOVO_OUTRA: errou antes e errou hoje com outra letra (4)

| Prova | n | id | Hoje (marcou/gab) | Tentativas anteriores (dia:prova:res:letra) | Mesmo dia em outra prova |
|---|---|---|---|---|---|
| c7aeca7cad19860 | 8 | 792a751ada88f29 | E B/A | 2026-09-09:f2d8c2239b59a98:E:C | - |
| c7aeca7cad19860 | 13 | da2334d180e31e8 | E A/D | 2026-09-21:ee2783053bb25cb:E:B | - |
| e0e342921bdebe8 | 14 | 6901c2efcb79225 | E D/C | 2026-09-21:4fefe014d446a29:E:B | 13c23806bd1877b:6:E:D |
| 13c23806bd1877b | 6 | 6ba1c9e0b171d6b | E D/C | 2026-09-21:4fefe014d446a29:E:B | e0e342921bdebe8:14:E:D |

## REP_REGREDIU: acertou antes e errou hoje (2)

| Prova | n | id | Hoje (marcou/gab) | Tentativas anteriores (dia:prova:res:letra) | Mesmo dia em outra prova |
|---|---|---|---|---|---|
| 057b89e0581a057 | 42 | b38eb90a6dbc0a1 | E C/A | 2026-09-08:5ef5a92042e9665:E:C, 2026-09-21:4fefe014d446a29:C:A | - |
| 065f0e3df14129c | 3 | 245c096fc64750a | E C/D | 2026-08-19:750919e1db48546:C:D | - |

## Nota sobre DUP_LOTE

41 questões em 20 enunciados repetidos entre provas do mesmo dia. Em 14 desses enunciados a resposta não foi a mesma nas cópias:

- 057b89e0581a057 n1 (d898297d29a5ada) C C/C; c7aeca7cad19860 n5 (10c4d9cbc46fa86) E A/C; aff4e3d49db69d4 n5 (158489ba507057e) E D/C
- 057b89e0581a057 n4 (09f9c437f61dbec) C B/B; aff4e3d49db69d4 n9 (c4ca60b57c6eb17) E D/B
- 057b89e0581a057 n14 (aab81606d495b44) C D/D; aff4e3d49db69d4 n2 (f9197028ad4cf4a) E A/D
- 057b89e0581a057 n19 (bf909b9c57da842) E D/A; aff4e3d49db69d4 n8 (95c2418b679833e) E B/A
- 057b89e0581a057 n33 (e4dae55f1710dcb) E B/C; aff4e3d49db69d4 n7 (fb823593207756d) C C/C
- 057b89e0581a057 n34 (f1e108680e9b294) E A/B; aff4e3d49db69d4 n3 (2d9edec5210a0b6) C B/B
- 057b89e0581a057 n36 (658dffe10afa7e3) E C/A; aff4e3d49db69d4 n15 (b8c3291157cc142) E D/A
- 057b89e0581a057 n40 (4b3d3648be166c5) C C/C; aff4e3d49db69d4 n12 (92f1fef60398b4d) E A/C
- 4bb26343ad0e886 n7 (2936a7b10b9a6fb) C D/D; 7b5f67f1aa80412 n28 (8c0add6d5c5248a) E C/D
- 4bb26343ad0e886 n9 (bfea42ca4d9ee98) C B/B; 7b5f67f1aa80412 n4 (5a12d60a6564f29) E D/B
- 4bb26343ad0e886 n11 (bec1ef60a416fb9) C C/C; 7b5f67f1aa80412 n20 (e1a078608a538e1) E A/C
- 4bb26343ad0e886 n12 (fa0d876e5ae8f19) C D/D; 7b5f67f1aa80412 n26 (89d38d1cfbcf2b4) E B/D
- 4bb26343ad0e886 n15 (7cbcbdc82762746) E D/A; 7b5f67f1aa80412 n17 (28f7dffa9e7b076) E C/A
- 4bb26343ad0e886 n16 (e4b5f50c307b82e) E B/A; 7b5f67f1aa80412 n15 (c9df06d07040f83) E D/A
