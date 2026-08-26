# O MCP visto de fora

O `POST /mcp` não existe só para o coach de dentro do Iteramnese. Ele é um
servidor MCP publicado no mesmo Fastify, e qualquer cliente que fale o protocolo
pode se ligar nele: o Claude Code, o Claude Desktop, o inspector do SDK, um
script seu. O que muda em relação ao coach da tela é quem paga e quem manda: o
modelo passa a ser o da assinatura de quem se conectou, e a sua chave da
OpenRouter fica fora do caminho.

Este documento é o passo a passo dessa ligação. Quem quiser o texto que faz o
cliente externo se comportar como o coach encontra em
[Claude_mcp.md](Claude_mcp.md).

## As duas coisas que o cliente precisa

**O endereço.** `POST /mcp`, no mesmo servidor que serve a interface:
`https://<seu-dominio>/mcp` em produção, `http://127.0.0.1:8787/mcp` em
desenvolvimento. O transporte é Streamable HTTP sem sessão, com
`enableJsonResponse`: cada requisição monta o seu par servidor e transporte e o
desfaz no fim, porque nenhuma ferramenta guarda estado entre uma chamada e a
outra.

**O token.** O `itm_`, em `Authorization: Bearer itm_...`. É ele que diz de quem
são as provas: o `createMcpServer` recebe o dono resolvido do token e nasce
preso a ele, e nenhuma ferramenta aceita usuário por parâmetro. Um token errado
não devolve dado de conta nenhuma, e um token certo devolve o acervo inteiro
daquela conta.

O `/mcp` fica fora de `/api/`, então o guarda de sessão e a conferência de
origem não passam por ele. É proposital, e está no [comentário do
mcp-http.ts](../backend/src/mcp-http.ts): a defesa aqui é a credencial, que uma
página de terceiro não tem como apresentar, e não o cookie, que ela conseguiria
fazer o navegador anexar.

## De onde o token sai

Não do `GET /api/export`. O zip leva provas, conversas, memórias, figuras e
configuração, e deixa de fora de propósito a chave da OpenRouter, o hash da
senha e os segredos de máquina: exportar credencial é fabricar uma cópia dela
na pasta de downloads, e o caso em `backend/test/exportacao.test.ts` procura os
três valores literais no arquivo inteiro.

O valor aparece duas vezes, e as duas uma vez só, porque o banco guarda apenas o
sha256 dele:

1. na criação da conta, na tela que mostra os segredos;
2. em Configuração, no botão que troca os segredos
   (`POST /api/config/credentials/mcp/rotate`).

Trocar ali regera **os dois** segredos juntos, o de captura e o do MCP. O
userscript para de enviar até ser reconfigurado com o novo `itc_`, e a tela
avisa isso antes de você confirmar.

## Registrar no Claude Code

```bash
claude mcp add --transport http --scope user iteramnese https://SEU-DOMINIO/mcp --header "Authorization: Bearer itm_SEU_TOKEN"
```

O escopo `user` grava em `~/.claude.json`, fora de qualquer repositório. Evite o
escopo de projeto com o valor cru: um `.mcp.json` na raiz é versionado, e o
token iria junto no commit. Se preferir o arquivo de projeto mesmo assim, deixe
o valor fora dele:

```json
{
  "mcpServers": {
    "iteramnese": {
      "type": "http",
      "url": "https://SEU-DOMINIO/mcp",
      "headers": { "Authorization": "Bearer ${ITERAMNESE_MCP_TOKEN}" }
    }
  }
}
```

Qualquer outro cliente MCP com transporte HTTP serve, desde que deixe você
mandar um cabeçalho próprio. Sem `Authorization` a resposta é 401 com
`WWW-Authenticate: Bearer`.

## Conferir antes de abrir a sessão

Direto no protocolo, sem cliente nenhum no meio:

```bash
curl -s -X POST https://SEU-DOMINIO/mcp -H "Authorization: Bearer itm_SEU_TOKEN" -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

O `Accept` com os dois tipos não é enfeite: o transporte responde 406 sem ele. É
exatamente o cabeçalho que o `backend/test/isolamento.test.ts` usa para
percorrer as ferramentas com duas contas.

## O que fica disponível

Todas as ferramentas, sempre escopadas no dono do token. Nove leem o acervo:

| Ferramenta | O que devolve |
|---|---|
| `get_performance_stats` | `geral`, `porProva`, `porTema`, `porDificuldade` e `fracas`, com o topo de cada lista. `secao` e `limite` abrem o resto. |
| `analise_de_tema` | Um tema inteiro: aproveitamento, índice dos erros e o que foi errado mais de uma vez. |
| `sugerir_material` | O que ainda não virou material: os temas ordenados pelo que falta escrever, e as questões erradas sem cartão nem questão inédita. |
| `list_exams` | As provas capturadas, com data e placar. Pagina por `cursor`. |
| `get_exam` | O índice de uma prova: uma linha por questão, com o começo do enunciado. |
| `list_questions` | O mesmo índice, filtrando por `examId`, `result`, `tag`, `difficulty`, `institution`. |
| `get_question` | A questão inteira: alternativas, comentário de cada uma, gabarito, marcada, percentual, temas. Aceita `questionIds`, até dez. |
| `get_question_history` | As tentativas da mesma questão, pelo `questionId`. |
| `search_questions` | Busca full-text, com a sintaxe de um buscador comum. |

Seis são dos flashcards (`list_tags`, `flashcard_create`, `flashcard_list`,
`flashcard_update`, `flashcard_delete`, `flashcard_stats`), seis são das questões
inéditas do IterQuestões (`iterq_status`, `iterq_create`, `iterq_list`,
`iterq_get`, `iterq_update`, `iterq_delete`), e cinco mexem nas memórias
(`memory_list`, `memory_read`, `memory_create`, `memory_update`,
`memory_delete`).

Seis detalhes que evitam surpresa:

- **As de memória escrevem nas mesmas linhas que o coach usa**, inclusive a
  `main`. Uma sessão externa distraída reescreve o que ele diagnosticou, e não
  há desfazer.
- **O que sai daqui é índice, e não conteúdo.** As listagens trazem o
  identificador e o começo do enunciado; o texto inteiro e os comentários vêm de
  `get_question`. É o que permite pedir uma prova de cem questões sem encher a
  janela do cliente.
- **Lista homogênea volta tabular**, como `colunas` mais `linhas`, e campo vazio
  não é escrito. Um cliente que espere um objeto por registro precisa remontar.
- **`includeHtml` é opt-in por um motivo.** O HTML íntegro carrega as imagens
  remontadas como `data:` URI e chega a megabytes.
- **`get_exam`, `list_questions` e `search_questions` paginam.** Elas devolvem `nextCursor`,
  e concluir a partir de meia lista é o erro mais fácil de cometer aqui.
- **As do IterQuestões escrevem no que o aluno vai resolver.** A questão gravada
  por `iterq_create` entra na fila da aba Treinar e volta por meses, então
  gabarito errado e feedback preguiçoso duram muito mais que a conversa. O
  servidor confere o que dá para conferir (cinco alternativas, uma correta,
  cinco feedbacks, tema do vocabulário do aluno, nível entre os três que
  existem, e a paráfrase da questão de origem), e recusa questão por questão,
  sem derrubar o lote. Os três níveis são média, difícil e extremamente difícil:
  não há "fácil", e a ausência é a decisão.

## O que não fica disponível

O ciclo da sessão não passa pelo MCP. O `started` e o `finished` de
`chat_sessions` pertencem às rotas de conversa da interface, e o cliente externo
não os alcança: para ele, encerrar uma sessão é escrever as memórias do fecho, e
mais nada. Os cinco atalhos, os tetos de gasto e o `SEED_LLM.md` também ficam do
lado de dentro, porque são do laço do coach, e o laço não roda aqui.

A fila do IterQuestões também não sai daqui. As ferramentas gravam, listam,
reescrevem e apagam questão; quem monta o simulado do dia, corrige a resposta e
guarda o log é a aba Treinar, pelas rotas da interface. É a mesma separação dos
flashcards, e pelo mesmo motivo: quem responde está na tela, e o que a tela
recebe não pode trazer o gabarito junto.

## O que pode dar errado

| Sintoma | Causa |
|---|---|
| 401 com `WWW-Authenticate: Bearer` | token ausente, errado ou já substituído por uma rotação. |
| 406 | o `Accept` não trouxe `application/json` e `text/event-stream` juntos. |
| 405 com `Allow: POST` | o cliente tentou `GET` ou `DELETE`. Sem sessão não há stream para retomar nem sessão para encerrar. |
| 429 por dez minutos | vinte recusas do mesmo endereço. Adivinhar um token de 32 bytes é impossível, encher o banco de consultas tentando não é. |
| A captura parou de funcionar | a rotação trocou o `itc_` junto. Reconfigure o userscript. |

Vale lembrar o preço de guardar o token num arquivo de configuração: ele fica em
texto claro na máquina onde está o cliente. Quem tem esse arquivo lê o acervo
inteiro daquela conta e escreve nas memórias dela. Se ele vazar, a saída é
trocar os segredos na tela de configuração, que mata o anterior na hora.
