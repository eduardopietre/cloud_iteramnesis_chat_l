# Simulados R03 e R04 (50 questões cada), pedido de 26/10/2026

Pedido do aluno: "mais 2 provas de 50, focando em erros e temas que caem bastante na
UERJ. Com questões que você apostaria. Questões extensas, com armadilhas e
distratores."

Vale todo o formato de `ESPEC.md` (seções "Formato UERJ" e "Saída") e de `ESPEC3.md`
(padrões do aluno). O modelo de qualidade é `redacao3/INF-R01.json`. Diferenças:

## O que muda

- **Aposta UERJ.** Cada questão sai de um tema que a UERJ repete (lista da sua área
  abaixo, tirada das provas UERJ 2023 a 2026) cruzado, sempre que possível, com um erro
  do aluno em `ERROS_S1_S4.md`. Pergunte-se: "este tema cai na UERJ do ano que vem?"
  Se não, troque.
- **Questões extensas.** Caso de 8 a 14 linhas: identificação, tempo de evolução,
  comorbidades e drogas em uso, antecedentes, negativos que importam, exame físico com
  sinais vitais e exames com valores e referências. O dado que decide fica NO MEIO do
  caso, cercado de dados verdadeiros que não decidem. Até 10% podem ser curtas (fato
  solto), porque a UERJ usa.
- **Armadilha e distratores.** Toda questão tem um distrator plantado no enunciado (o
  rótulo verdadeiro, a exposição que aponta a vizinha, o laboratório que imita outra
  doença, o exame tranquilizador, o diagnóstico falso já afirmado no texto) e a
  armadilha é a alternativa que esse distrator puxa. As quatro alternativas são
  respostas certas de casos vizinhos.
- **Grade X / Y em cerca de 15%** (pelo menos 1 por área por simulado nas áreas com 5
  ou 6 questões).
- **Não repetir NADA** de `ref/simulado1-resolucao.txt`, `redacao/`, `redacao2/` e
  `redacao3/*-R01.json` e `*-R02.json` (grep rápido de 1 ou 2 termos-chave).
- Arquivos: `redacao3/<AREA>-R03.json` e `redacao3/<AREA>-R04.json`, ids
  `R03-INF-01`..., campo `"simulado": "R03"`. Campo `alvo`: "UERJ 2024 (Burkitt no
  HIV) + S1 q37" ou "UERJ recorrente: ...".
- Gabarito A a D equilibrado por arquivo; armadilha diferente do gabarito; textos de
  resolução e comentários sem citar letras; sem travessão; sem "clássico", "típico",
  "patognomônico". Tags copiadas de `build/out/simulado2.json` a `simulado4.json`,
  `redacao2/` ou `redacao3/`. Não use o MCP.
- Grave cada arquivo assim que ficar pronto (Write, um arquivo por chamada).
