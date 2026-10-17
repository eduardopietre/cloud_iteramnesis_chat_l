# Gravar simulados no app (agente de carga)

O aluno pediu expressamente nesta conversa: "Me forneça todos, cada um criado em um grupo"
(Simulados 6 a 15, mesmo estilo dos 2 a 5, para os quais autorizou: "Adicione as questões
criadas também via MCP, usando o bypass se necessário"; 4 alternativas; um grupo por simulado).

Ferramentas (ToolSearch): select:mcp__iteramnese-coach__iterq_create,mcp__iteramnese-coach__iterq_list,mcp__iteramnese-coach__iterq_get,mcp__iteramnese-coach__iterq_update

1. Para cada simulado n seu, os argumentos prontos estão em cargas/S<n>-lote1.json, -lote2.json e
   -lote3.json (objeto com group, questoes, rubricBypass). Chame iterq_create UMA vez por arquivo,
   passando os três campos exatamente como estão. Copie com cuidado: já houve erros de cópia
   (letras cirílicas, acentos trocados). Não envie nada provisório.
2. Nunca reenvie um lote aceito. Erro 5xx: antes de repetir, confira com iterq_list
   (group "Simulado UERJ n", limit 100) se não entrou. Recusa de forma (nome de tag): corrija só
   aquilo e reenvie só a recusada.
3. CONFERÊNCIA OBRIGATÓRIA: baixe todas as questões do grupo com iterq_get (10 ids por chamada),
   salve as respostas em arquivo POR SCRIPT a partir do seu próprio registro de sessão (não
   transcreva à mão; veja como foi feito em /tmp/claude-0/verif/compare.py e
   /tmp/claude-0/-home-user-cloud-iteramnesis-chat-l/906fe91e-85c1-52a6-93cc-2f0b016e0916/scratchpad/s2/),
   e compare com os arquivos de carga pelo prefixo "[Simulado UERJ n, questão m]": enunciado,
   texto e feedback das 4 alternativas, gabarito, tags, nível, decisor, armadilha; caracteres
   fora do alfabeto latino; 50 questões numeradas de 1 a 50 sem duplicata.
4. Corrija divergências com iterq_update (só os campos divergentes, com o valor EXATO do
   arquivo). Baixe de novo e confirme zero divergências.
5. Grave cargas/S<n>-resultado.md com os ids por lote, as recusas e a conferência.
