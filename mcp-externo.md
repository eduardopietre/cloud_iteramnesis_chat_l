# O MCP visto de fora

O `POST /mcp` não existe só para o coach de dentro do Iteramnese. Ele é um
servidor MCP publicado no mesmo Fastify, e qualquer cliente que fale o protocolo
pode se ligar nele: o Claude Code, o Claude Desktop, o inspector do SDK, um
script seu. O que muda em relação ao coach da tela é quem paga e quem manda: o
modelo passa a ser o da assinatura de quem se conectou, e a sua chave da
OpenRouter fica fora do caminho.


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

As doze ferramentas, todas escopadas no dono do token. Sete leem o acervo:

| Ferramenta | O que devolve |
|---|---|
| `get_performance_stats` | `overall`, `byExam`, `byTag`, `byDifficulty` e `weakSpots`. Sem parâmetros. |
| `list_exams` | As provas capturadas, com data e placar. Pagina por `cursor`. |
| `get_exam` | Uma prova e todas as questões dela, em texto limpo. |
| `list_questions` | Filtra por `examId`, `result`, `tag`, `difficulty`, `institution`. |
| `get_question` | A questão inteira: alternativas, comentário de cada uma, gabarito, marcada, `percent`, tags. |
| `get_question_history` | As tentativas da mesma questão, pelo `questionKey`. |
| `search_questions` | Busca full-text, com a sintaxe de um buscador comum. |

E cinco mexem nas memórias: `memory_list`, `memory_read`, `memory_create`,
`memory_update` e `memory_delete`.

Três detalhes que evitam surpresa:

- **As de memória escrevem nas mesmas linhas que o coach usa**, inclusive a
  `main`. Uma sessão externa distraída reescreve o que ele diagnosticou, e não
  há desfazer.
- **`includeHtml` é opt-in por um motivo.** O HTML íntegro carrega as imagens
  remontadas como `data:` URI e chega a megabytes.
- **`list_questions` e `search_questions` paginam.** Elas devolvem `nextCursor`,
  e concluir a partir de meia lista é o erro mais fácil de cometer aqui.

## O que não fica disponível

O ciclo da sessão não passa pelo MCP. O `started` e o `finished` de
`chat_sessions` pertencem às rotas de conversa da interface, e o cliente externo
não os alcança: para ele, encerrar uma sessão é escrever as memórias do fecho, e
mais nada. Os quatro atalhos, os tetos de gasto e o `SEED_LLM.md` também ficam
do lado de dentro, porque são do laço do coach, e o laço não roda aqui.

## O que pode dar errado

| Sintoma | Causa |
|---|---|
| 401 com `WWW-Authenticate: Bearer` | token ausente, errado ou já substituído por uma rotação. |
| 406 | o `Accept` não trouxe `application/json` e `text/event-stream` juntos. |
| 405 com `Allow: POST` | o cliente tentou `GET` ou `DELETE`. Sem sessão não há stream para retomar nem sessão para encerrar. |
| 429 por dez minutos | vinte recusas do mesmo endereço. Adivinhar um token de 32 bytes é impossível, encher o banco de consultas tentando não é. |
| A captura parou de funcionar | a rotação trocou o `itc_` junto. Reconfigure o userscript. |

