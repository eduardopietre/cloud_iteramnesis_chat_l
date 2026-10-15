# Revisão dos blocos (revisor independente)

Você revisa um bloco de questões já escritas por outro redator, em
`simulados/redacao/<BLOCO>-S2.json` a `-S5.json`. Leia antes `simulados/ESPEC.md`.
Corrija NOS PRÓPRIOS ARQUIVOS (mesmo formato JSON). Nada de escrever no servidor MCP
(só leitura: topic_list, memory_read, question_get).

Para CADA questão, confira e corrija:

1. **Medicina.** O gabarito é a única alternativa defensável pela diretriz vigente
   em 2026 citada em `referencias`? Os números (doses, cortes, janelas, valores de
   exame) estão certos? Se houver duas defensáveis, mude o enunciado (acrescente o
   dado que separa) ou troque a alternativa errada. Se a posição for controversa e
   não houver como consertar, reescreva a questão inteira com outro ângulo do mesmo
   tema.
2. **Dificuldade honesta.** Teste do quintanista: se dá para acertar lendo só a
   última linha, só as alternativas, ou se o enunciado entrega o diagnóstico,
   endureça (tire a pista óbvia, acrescente um rótulo verdadeiro que puxa para a
   armadilha, ponha o dado decisivo no meio do caso). A armadilha deve ser plausível
   de verdade.
3. **Estilo UERJ.** Quatro alternativas curtas, mesma forma e comprimento parecido
   (a correta não pode ser a mais longa ou a mais específica de forma sistemática).
   Enunciado sem "clássico", "típico", "patognomônico", sem travessão (— ou –).
   `dado_decisivo` copiado literalmente do enunciado.
4. **Arma coerente.** O campo `arma` descreve mesmo a mecânica da questão (ex.:
   "Grade X / Y" só se as alternativas forem combinações "X / Y").
5. **Não repetir o Simulado 1** (`simulados/ref/simulado1-resolucao.txt`): mesmo
   caso, mesmo ângulo ou mesma resposta é proibido. Confira com grep.
6. **Textos de apoio**: `resolucao`, `comentarios` (um por letra, começando por
   "Correta." ou "Errada."), `para_levar`, `referencias` coerentes com o gabarito
   final. Os comentários das erradas dizem em que caso vizinho seriam certas.
7. **Referências reais.** Cite só diretriz cuja existência e ano você tem certeza (ex.: Surviving Sepsis Campaign 2021, GOLD 2025, GINA 2024). Se a referência for uma versão que você não consegue confirmar (ex.: "SSC 2026", "GOLD 2026"), troque pela última versão confirmada, e confira que o gabarito vale por ela.
8. **Tags** existem no vocabulário (`topic_list` com `filter`).

DEPOIS, POR SIMULADO (cada arquivo), **reequilibre as letras**:
- gabaritos distribuídos igualmente entre A, B, C, D (diferença máxima de 1);
- armadilhas também espalhadas (nenhuma letra com mais da metade das armadilhas);
- para mudar a letra, reordene as alternativas DE VERDADE: mova o texto da
  alternativa, o comentário correspondente, atualize `gabarito` e `armadilha`, e
  corrija qualquer menção a letra dentro de `resolucao`, `comentarios` e
  `para_levar` (prefira que esses textos não citem letras: cite o conteúdo).
- Em "Grade X / Y", mantenha uma ordem lógica das combinações.

No fim, valide: JSON abre, 4 alternativas, dado_decisivo no enunciado, sem termos
proibidos, contagem de gabarito e armadilha por letra em cada arquivo.

Resposta final, no máximo 15 linhas: quantas questões você alterou (e quantas
reescreveu inteiras), os problemas médicos mais sérios que achou, e a contagem final
de gabarito e armadilha por letra em cada simulado.
