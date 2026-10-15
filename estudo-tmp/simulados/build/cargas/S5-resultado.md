# Simulado UERJ 5: carga no Iteramnese via MCP

Data: 2026-10-15. Ferramenta: iterq_create (rubricBypass, pedido expresso do aluno), grupo "Simulado UERJ 5".
Cada lote foi enviado uma única vez; nenhum reenvio, nenhuma duplicata.

| Lote | Arquivo | Lote no servidor | Aceitas | Recusadas | Duplicadas |
|---|---|---|---|---|---|
| 1 (q1 a q20) | S5-lote1.json | 2026-10-15-d1e0d0 | 20 | 0 | 0 |
| 2 (q21 a q40) | S5-lote2.json | 2026-10-15-dab5b3 | 20 | 0 | 0 |
| 3 (q41 a q60) | S5-lote3.json | 2026-10-15-b3ab9e | 20 | 0 | 0 |
| 4 (q61 a q80) | S5-lote4.json | 2026-10-15-14fa39 | 20 | 0 | 0 |

Conferência final: iterq_list(group "Simulado UERJ 5", limit 100) devolveu 80 questões, sem cursor de continuação.
As 80 foram relidas com iterq_get e comparadas ao JSON de origem.

## Pendência (erro de transcrição na carga)

- Questão 58, id dd57a3783ca0c05: o enunciado gravado diz "trombose venosa profunda poplínea direita";
  o arquivo S5-lote3.json diz "poplítea". O restante da questão confere. Não foi corrigido, porque a
  tarefa vetava outras ferramentas de escrita; a correção é um iterq_update só no enunciado
  ("poplínea" para "poplítea").

## IDs criados, na ordem das questões

### Lote 1
0022b6eb739839f 54225d6f5b48cbd 2abdd9691abb0e4 cee3d1fa5e9d6b3 7772f8768828c56 daf20b4e80ae012 57a3dc7e96cc9b2 f73c965c1390630 6be0ee2a3ffe4d1 0c8885ded7b7372 ddbc734a459aa28 7dd6b6066b349d4 4f890791d0e83c6 4f5beb85a754027 e93ba6c71379d6c f9d00b8f3105a0e 222f5bfd3c14043 bee0b2351050f88 c1994ac6052bf3e e6cbd8c1a1107c3
### Lote 2
c5bcd28827f8009 182fdc9aee18226 b51aaacd6bfaade f24bc3caaea092a 5cb34145468acee a8fbb3c6c5f5ae3 85cefa3c821f0f5 f66410b9aec0ac8 df1fb8f4f5c24d7 b001f6335d7b7f4 49f1e9d23f8a16a b46891ab4a693c4 e79efa6fd2bb95d 6681d7ccb5d0968 209b55ed3250cb8 8f5926f83fb2d45 d53fb06bf0cafea 7e4f1598226788f f86c0372bfa325f 536c4c7ef7317ed
### Lote 3
180d213256f18d5 5a6e25a3c6a7851 c37e011a332e203 68459a64ffb71bd c314fa9177c4c75 fd0f672dd6f79e2 f4015c96ea1be4c 6aeb79a14271be0 ef73514a4138427 546b98045a6d0a8 7259416f92f6f43 2c4977552489ff4 b312881e3537ec1 1824b72036160d5 3f7542c54145740 6a7265cb28d93c8 991144b82d7024e dd57a3783ca0c05 b22c3166530e540 ff1752b19ff9705
### Lote 4
188500c9e90c5b3 bcc8da69cb76e1a c1bd549696ff8a4 b6ac064b65eb128 3bf5918c953b2bd 98cc161f11d3ff3 c39c10725427649 1758718c799fa43 90d8b95dd9f1216 31d2646b3c9bc10 9ec731fc146c647 eff648b81457054 e2dd1decbe3584a 247326b0de8ce5f ab715977edb3bb3 f6607ddae28827e eb6e45ea8853653 104d35786a1e25a 8833fa458f4516d 576aab2378b67eb

- 15/10/2026: corrigido pelo coordenador com iterq_update (enunciado restaurado do lote, 'poplítea').
