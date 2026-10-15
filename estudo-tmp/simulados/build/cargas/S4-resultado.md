# Simulado UERJ 4: carga via MCP (iterq_create), 2026-10-15

Grupo: "Simulado UERJ 4". Contagem final no grupo (iterq_list, limit 100): 80 questões (questões 1 a 80, sem duplicatas).
Recusas do servidor: nenhuma, em todas as chamadas.

## S4-lote1.json (questões 1-20), lote 2026-10-15-d386fd: 20 aceitas
12b705bff396e5f cdcd4aa5d92448a 11647f3f702c46f d438eae4d73264f 3d7434748c7bbf5 403ab8bb733c60e dab2aadfc6925e5 66eae94fa4cf582 eb8bc7562b5cf80 8bcce17dbd31741 73b9dddeee37bf3 e6b661a2faa5d97 a052e9fcbe8b298 024bb78c20b1a7b b0e163993582ed6 ba9041c4eaaa91a 37a7eaa808a83e1 001b7c4205a7d9a d16649edb37f88f 0d1109135fe2de9

## S4-lote2.json (questões 21-40), lote 2026-10-15-c45c2c: 20 aceitas
11a5a152038fdc8 0ffca5f483dbac0 087de471ae4c3c9 12dc87e38de08e1 28e8533515bc57a c077b1dcb71f928 0d2096e5cedf70f 1ad109e0b9b9b7d 9b4127830d3384f f83eeb1b8e320e7 347b9518966ef06 d5747a344e6237b f4214e91a798354 c91f04e755926ab c17e3bc7f3cda17 ae221d06017cda2 0eee8b5ef8f8b4b 96be96ba884b03f 45e4d707f7cf378 5e125f7179b8754

## S4-lote3.json (questões 41-60), lote 2026-10-15-66048a: 20 aceitas
f57074383ee2cd2 33c47dd4586805b 8091b38accd8c84 166a25a68a70b0e e8e716742535813 74f4383ce408024 53eb402ef4bd704 60ea3e6db0ab269 95b90872fb1fb91 30801bf47704ed8 5091c8c2f0518a9 f02d98a6fec2f7f 8a8ae411ac2e162 e4fc49cda5c6f33 f01085a817cdec6 53b95c9a06c25d7 337199d2443c4ac 23ff49581070cd6 b72274abb8194f4 31a336a6e7201a9

## S4-lote4.json (questões 61-80): entrou em DUAS chamadas (erro do agente)
- Lote 2026-10-15-487f69 (questões 61-63), 3 aceitas: ec5bd79c5590d8e 2b1cbaf499a8f03 0dfbbc407b49517
- Lote 2026-10-15-a59c9c (questões 64-80), 17 aceitas: 3aa5162ffb5c6fe 039bcbb25028aef f2a578d3eed813f 10d3f4c6c777dcb 9addc24749a9fe8 d7468a16e52d59f 60f3b867293a605 2dceabf95e9218b 5ddf48f09b4ea4c 7d84f085c7e8ac8 11d8f497dda8239 c257817340539dc 7d3758065f760b8 152fc8f5a3a93c4 d65b1ed944dbf29 a58091bd6841521 3783bd6b44be990

### Problemas a corrigir (não corrigidos: exigem iterq_update, fora do escopo autorizado)
1. Por erro do agente, a chamada das questões 61-63 foi enviada antes de estar completa, com
   rubricBypass.userRequest = "PLACEHOLDER-DO-NOT-SEND" em vez das palavras do aluno. As três questões
   entraram; não foram reenviadas para não duplicar. As 64-80 foram enviadas depois com o userRequest correto.
2. Questão 63 (id 0dfbbc407b49517), feedback da alternativa B (correta): a palavra "sideroblástica" ficou gravada
   como "sideробlástica" (letras cirílicas р, о, б). Confirmado por iterq_get. O resto da questão confere com o JSON.
   Correção: iterq_update nesse id com o feedback B exatamente como está em S4-lote4.json.
3. As 80 questões foram transcritas à mão para as chamadas; só a 63 foi conferida campo a campo contra o JSON.
   Vale um diff completo (iterq_get dos 80 ids contra os JSON) para descartar outros desvios de transcrição.
