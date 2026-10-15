# Síntese: 13 provas capturadas em 15/10/2026

Base: as 350 questões das 13 provas lidas uma a uma (enunciado, alternativas,
comentários, % de escolha), mais o histórico de cada questão no banco. Detalhe por
prova em `provas/`, dados brutos em `agregado.psv` e `historico.psv`.

## 1. Os números que importam

| recorte | placar | média de quem respondeu |
|---|---|---|
| Lote inteiro | 206/350 (58,9%) | cerca de 61% |
| **Só questões inéditas** (nunca vistas antes de 15/10) | **139/247 (56,3%)** | cerca de 62% |
| Questões já vistas antes | 49/62 | |
| Duplicadas dentro do próprio lote | 18/41 | |

- **O lote está cerca de 5 pontos abaixo da média de quem respondeu** nas inéditas.
  O banco inteiro dele roda em 64,5%. A queda é real e não é efeito de prova difícil.
- **Onde ele perde ponto:** nas questões medianas. Quando 70% ou mais acertaram,
  ele faz 86% (igual à média). Na faixa de 50 a 69% faz **49% contra 61%**: são
  12 pontos abaixo, e é aí que está quase toda a diferença. Nas difíceis (menos de
  50% acertaram) faz 21% contra 36%.
- **Erros "fracos"** (questão que 70% ou mais acertaram): 20. São os mais baratos
  de corrigir (lista na seção 8).

### Por banca (inéditas)

| banca | inéditas | média geral | leitura |
|---|---|---|---|
| UERJ | 11/14 (79%) | 63% | acima, mas amostra pequena |
| USP-RP | 26/41 (63%) | 68% | 5 abaixo |
| USP-SP | 53/92 (58%) | 63% | 5 abaixo |
| Einstein 2026 (prova inteira) | 23/44 (52%) | 62% | 10 abaixo |
| SUS-SP | 6/19 (32%) | 50% | 18 abaixo |
| UNIFESP | 4/12 (33%) | 52% | 19 abaixo |

### Por tipo de comando (inéditas)

| comando | ele | média | |
|---|---|---|---|
| diagnóstico | 20/27 (74%) | 74% | na média |
| fato solto (pergunta direta) | 17/22 (77%) | 74% | na média |
| etiologia | 8/14 (57%) | 52% | acima |
| **conduta** | **57/100 (57%)** | **64%** | 7 abaixo |
| **composta** | 17/30 (57%) | 60% | |
| **próximo exame** | **12/28 (43%)** | **61%** | **18 abaixo** |
| **mecanismo/fisiologia** | 3/9 (33%) | 65% | 32 abaixo (amostra pequena) |
| **comando negativo (EXCETO)** | **1/8 (12%)** | 31% | |

## 2. O que muda no diagnóstico registrado

1. **Conduta deixou de ser o ponto forte fora da UERJ.** O "conduta cerca de 87%"
   de 23/09 era UERJ, com diagnóstico dado. Nas bancas paulistas e no Einstein a
   conduta fica em 57%, e o pior comando é **próximo exame (43%)**. O problema se
   deslocou de "identificar a doença" para **"o que fazer agora e em que ordem"**.
2. **Identificar não é mais o gargalo nestas provas** (diagnóstico 74%, fato solto
   77%). O eixo 1 (rótulo) continua existindo, mas aparece sobretudo quando o
   rótulo empurra a CONDUTA (ex.: "febre, então antibiótico"; "TB", "etilista").
3. **O eixo 2 (fato solto) não se confirmou neste lote**: 77%. O que falha é
   fato de **mecanismo e fisiologia** (curva fluxo-volume, pletismografia,
   neuroanatomia, metformina e glicosúria), e não a pergunta direta em geral.
4. **"Comorbidade na primeira linha ele acerta" não vale fora da UERJ.** Neste lote
   há pelo menos 14 erros por antecedente ou droga em uso ignorados.
5. **Gasometria parece corrigida**: Winters e gap osmolar 5/5 (nefro e mista).

## 3. Padrões de erro, do mais forte ao mais fraco

Contagens sobre os 144 erros; um erro pode ter mais de uma causa.

### P1. Porte e ordem da conduta: cerca de 64 erros (o padrão dominante)
Ele quase sempre erra para o lado de **fazer mais** (cerca de 37 erros de
sobretratar ou sobreinvestigar, contra poucos de subtratar):
- **Pede o exame do degrau seguinte, ou um exótico, antes do simples**: biópsia
  antes de ressecar nódulo pulmonar; LBA antes de perguntar a exposição;
  toracoscopia antes de citometria; HFE e elastografia com FIB-4 de 1,1 e IST não
  calculado; cintilografia com TSH normal; aldo/renina sem HAS; painel hipofisário
  completo; investigar a reflexa antes de excluir disfunção de marca-passo;
  urocultura e imagem na pielonefrite ambulatorial.
- **Trata o que não precisa**: fenitoína sem indicação em **3 cenários distintos**
  (HSA, distonia aguda, crise provocada por hiponatremia), marcada por menos de 7%
  dos candidatos. Isso não é armadilha da banca: é **reflexo dele**.
  Espironolactona depois de adrenalectomia, intervenção em coleção pancreática
  sem critério de Atlanta, sobretratar OA inicial.
- **Investiga antes de tratar na emergência**: 3 de 3 errados no Einstein
  (estado de mal, hipoglicemia, abstinência), mais as crises da neuro.
- **Aplica a regra sem checar a precondição** (face 4): pólipo e idade no
  rastreio de CCR, ICFEp com FE de 53%, CGM sem hipoglicemia.

### P2. Exame que decide lido como enfeite: cerca de 60 erros
Ele lê o número quando o número é o assunto da questão (gasometria 5/5), e
**ignora o número quando um rótulo clínico forte vem antes**:
- **Líquido pleural**: pseudoexsudato por diurético, ADA baixo com LDH altíssima
  (linfoma), neutrófilos e pH contra ADA alto, Coombs C3d (Mycoplasma).
  Derrame pleural 2 de 5.
- **Endócrino**: IST não calculado (2x), FIB-4 1,1, DST 2,5, PRL acima ou abaixo
  de 100, glicosúria com glicemia normal (iSGLT2), cálcio normal na SPA2 (de novo).
- **Nefro**: albumina normal com proteinúria nefrótica, cadeias leves normais com
  vermelho Congo negativo.
- **Neuro**: razão glicorraquia/glicemia no líquor de TB (2x, mesma letra), sódio
  de 113 (2x, mesma letra), head impulse normal lido como periférico.
- **Cardio**: o "exame" é ECG e eco: FE 53%, espícula de marca-passo sem captura,
  creatinina subindo com IECA.

### P3. Rótulo saliente decide (eixo 1): cerca de 41 erros
LES lido como neurossífilis (92% acertaram); "TVP prévia" puxando TEP na SAHOS;
"etilista" puxando intoxicação no AVC cerebelar (2ª vez, 1,8% marcaram);
"ansiedade" na dor anginosa típica; TB quando não é (3x); Löffler pelo epônimo.

### P4. Comando e forma da alternativa: cerca de 27 erros
- **Comando negativo**: 1 de 8 EXCETO (Einstein 5 de 6). Na UERJ quase não existe,
  mas em toda banca paulista existe.
- **Meia verdade dentro da alternativa** (face 5): 9, quase todos no Einstein.
  Primeira oração verdadeira, a segunda traz absoluto ou premissa errada, e ele
  marca pela primeira.
- **Resposta verdadeira fora do comando**: RAR no lugar de NNT; achado verdadeiro
  quando se pedia outra coisa.
- **Grade "X / Y" conferida pela metade** (UERJ cardio): 2.

### P5. Lacuna de conteúdo pura (mecanismo, semiologia, anatomia): cerca de 34
Semiologia valvar e congênita (Marfan 0 de 3, IM 0 de 2, CIA), fisiologia
pulmonar (3), neuroanatomia (OIN 2x, dermátomo, raiz x nervo), ELA x mielopatia
cervical (0 de 3, nos dois sentidos), miopatias inflamatórias (0 de 3).

### P6. Excesso x deficiência hormonal: 4 (confirmado)
Apoplexia: tratou a massa e não o cortisol baixo. Espironolactona com a adrenal já
fora. Com a memória de 27/08, já é padrão.

## 4. Conhecimento instável (o achado novo mais importante)

- **Dentro do mesmo dia, a mesma questão em duas provas**: 20 enunciados
  repetidos, e **em 14 deles a resposta mudou** de uma cópia para outra.
  - Endócrino: errou as 6 duplicadas na 7b5f e acertou 4 delas na 4bb2. Em todas
    as 4 a errada é **um passo a mais ou um passo pulado**.
  - Neuro: das 16 duplicadas, 7 mudaram de resultado.
  - Dermatomiosite: 3 tentativas, 3 letras diferentes.
- Leitura: ele tem o conteúdo e decide **entre duas finalistas sem regra
  fixada**. Isso não se corrige com teoria, e sim com o **algoritmo escrito**
  (ex.: "FIB-4 < 1,3 repete; 1,3 a 2,67 elastografia; > 2,67 hepatologista";
  "IST ≥ 45% antes de pensar em ferro").
- **Ordem de resolução (confirmada pelo aluno, igual à de captura, 21h49 a 22h10):**
  1d0d, 13c2, 065f, c897, e0e3, aff4, 7b5f, b34e, 4bb2, c7ae, dec6, 6343, 057b.
  Nas 23 duplicadas do lote: **9 corrigiu, 2 regrediu, 7 errou sempre, 5 acertou
  sempre**. Endócrino: 7b5f veio antes, então as 4 mudanças são correção. Neuro:
  aff4 veio antes da 057b, com 5 correções e 2 regressões (distonia aguda por
  metoclopramida, NMO).
- **Leitura revista**: a correção veio minutos depois de ver o gabarito da
  primeira cópia, então mede memória de curto prazo, não regra fixada. O sinal
  forte são as **7 que ele errou de novo logo depois de ver a resposta**: líquor
  da TB (mesma letra), crise provocada com fenitoína (mesma letra), Marfan (mesma
  letra), ELA x mielopatia, oftalmoplegia internuclear, DHGNA com FIB-4 e
  hiperferritinemia metabólica. Errar de novo com a mesma letra depois de ver o
  gabarito é regra errada fixada, a prioridade máxima. As 2 regressões (acertou
  e depois errou) são as finalistas sem regra.

## 5. Reincidentes: errou de novo questão já vista (as lacunas fixas)

| tema | prova/q | antes | marcação |
|---|---|---|---|
| Marfan, IAo (subluxação do cristalino) | e0e3 q14 + 13c2 q6 | 21/09 | 0 de 3 |
| Insuficiência mitral crônica, ausculta (UERJ) | 13c2 q8 | 21/09 | mesma letra |
| Endomiocardiofibrose/Löffler (UERJ) | 13c2 q1 | 21/09 | mesma letra |
| AVC cerebelar no etilista (UERJ) | aff4 q19 | 21/09 | mesma letra (acertou a cópia 057b) |
| SPA2, cálcio normal (UERJ) | 7b5f q10 | 21/09 | mesma letra |
| AR com DPI (UERJ, gabarito discutível) | c7ae q13 | 21/09 | outra letra |
| Osteomalácia pós-bariátrica | c7ae q8 | 09/09 | outra letra |
| Nódulo pulmonar, biópsia x ressecção | dec6 q16 | 05/08 | mesma letra |
| DPI, LBA antes da anamnese | dec6 q17 | 05/08 | mesma letra |
| Hiponatremia na ICFE (Einstein) | 065f q33 | 19/08 | mesma letra |
| **Regrediu**: ELA x mielopatia cervical (UERJ) | 057b q42 | errou 08/09, acertou 21/09 | errou de novo |
| **Regrediu**: espondiloartrite, EXCETO | 065f q3 | acertou 19/08 | errou |

**Errar de novo com a mesma letra** é a assinatura de regra errada fixada, e não
distração: 7 casos.

## 6. Domínios: onde ele está firme

- **Gastro, DII**: 6 de 7. Diagnóstico com dado na última linha de exame, 4/4.
- **Membranosa** 3/3, **microcristalinas** (gota, CPPD) 3/3, **gasometria** 5/5,
  **sódio** (SIADH x DI) 3/4.
- **Emergência e UTI** (mista USP) 7/7: CAD, sedação, Weil, neutropenia febril,
  SVCS, abstinência. **Paliativos conceituais** 3/3. **Oxigenoterapia** 3/3.
- **Vasculites** 3/4 (PAN, IgA, Behçet). **Diagnóstico reumatológico** por padrão
  clínico completo: 5/6.
- **Cardio**: IC com critério numérico escrito (QRS, FC), dissecção, EAo, FA
  valvar, Takotsubo, DAPT.
- **Endócrino**: GLP-1 e iSGLT2 em indicação, hiperparatireoidismo, hipogonadismo
  (Klinefelter, Turner).
- **Regra geral dos acertos**: acerta quando o corte ou a pista vem escrito e a
  questão é sobre ele; erra quando precisa decidir **qual número do caso manda**.

## 7. Por área

| área | lote | inéditas | lacuna principal |
|---|---|---|---|
| Neuro (2 provas) | 39/67 | 10/22 | reflexo da fenitoína, crise provocada, líquor de TB, ELA x mielopatia, vertigem central, OIN |
| Pneumo | 14/30 | 8/22 | líquido pleural, fisiologia funcional, DPI 1/4, pneumonia 0/2, puxa TB |
| Reumato | 13/25 | 7/16 | miopatias 0/3, manejo de AR 0/2, OA, osteomalácia |
| Endócrino (2) | 28/49 | 20/32 | DHGNA/ferro (fixa), prolactinoma 0/3, adrenal, excesso x deficiência |
| Nefro | 19/30 | 13/24 | nefrítica, gamopatia renal, diálise na IRA, rabdomiólise/K |
| Gastro | 25/40 | 19/34 | pancreatite 1/4, diarreia por ácido biliar 0/2, imagem hepatobiliar |
| Cardio (3) | 25/39 | 23/33 | semiologia valvar e congênita (fixa), restritiva, ECG/eco como discriminante |
| Einstein 2026 | 26/50 | 23/44 | EXCETO, meia verdade, emergência neuro e tóxica, paliativos dispneia, osteoporose |
| Mista USP | 17/20 | 16/19 | NNT |

## 8. Os 20 erros fracos (os mais baratos)

| prova | q | % acertou | tema | causa |
|---|---|---|---|---|
| reumato | 9 | 92 | LES neuropsiquiátrico | rótulo, exótico no lugar do banal |
| endo2 | 16 | 85 | CGM no DM2 | precondição |
| Einstein | 40 | 86 | tremor essencial | meia verdade, superinvestiga |
| pneumo | 18 | 81 | SAHOS | rótulo TVP prévia |
| Einstein | 39 | 79 | osteoporose | meia verdade |
| Einstein | 46 | 79 | abstinência/delirium | investiga antes de tratar |
| Einstein | 29 | 77 | pré-operatório, corticoide | droga em uso |
| neuro1 | 33 | 76 | distonia aguda | fenitoína |
| neuro1 | 21 | 76 | miastenia, timoma | rótulo |
| pneumo | 22 | 75 | DPOC | absoluto, grade |
| cardio3 | 8 | 74 | disfunção de marca-passo | ECG pelo rótulo |
| nefro | 4 | 74 | nefrítica, complemento | rótulo |
| pneumo | 17 | 72 | DPI | LBA antes da anamnese (reincidente) |
| endo2 | 20 | 72 | hiperaldo pós-adrenalectomia | excesso x deficiência |
| nefro | 20 | 72 | pielonefrite | sobreinvestiga |
| reumato | 16 | 71 | OA de joelho | sobretrata |
| mista | 10 | 71 | NNT | fora do comando |
| endo1 | 15 / endo2 17 | 71 | hemocromatose x DHGNA | IST (2x) |
| gastro | 35 | 70 | diarreia por ácido biliar | antecedente ignorado |

## 9. UERJ (peso especial)

- **55 questões UERJ no lote, 44 certas (80%) contra 63% de média.** Mas **41 das
  55 eram repetidas** das provas de 21/09 e anteriores: 22 mantidas, 11
  corrigidas, 8 erradas de novo. As inéditas UERJ são só 14 (11 certas, 79%).
- **Nenhuma prova UERJ nova chegou**: a cardio 2 (13c2) é UERJ inteira, mas
  repetida. Não dá para medir a evolução na UERJ com este lote.
- **O que a UERJ ainda derruba** (as 8 reincidentes): Marfan e IAo, IM crônica,
  Löffler/restritiva, SPA2 com cálcio normal, AVC cerebelar no etilista,
  ELA x mielopatia, AR com DPI. É o mesmo eixo 1 de 23/09 (rótulo plantado) mais
  **semiologia por evocação**, agora com reincidência documentada.
- **Questões de outras bancas no estilo UERJ** (distrator plantado, dado na última
  linha, droga a deduzir): ele caiu em cerca de 2 de cada 3 (pneumo 5/6,
  endócrino 12/19, reumato+nefro 8/13, Einstein 9/12). **A arma da UERJ funciona
  contra ele quando a questão é nova**; na UERJ ela parece neutralizada porque as
  questões já são conhecidas.
- **Ganho real**: 11 questões UERJ corrigidas desde setembro, entre elas IRA
  pré-renal pela cronologia, Eaton-Lambert, FA com propafenona e o absoluto do
  teste ergométrico.

## 10. Temas ausentes ou sub-representados no lote

O lote é de clínica médica por especialidade, sem **hematologia** (só 4 questões:
anticoagulação, amiloidose, PV), sem **infectologia** (nenhuma de HIV, TB como
resposta, endocardite infecciosa, meningite bacteriana, ITU complicada, antibiótico)
e com **oncologia** mínima. São justamente as lacunas já registradas e o bloco de
cerca de 45 de cada 200 questões da UERJ (infecto 23, hemato 22).

Prioridade para a UERJ e para R+ CM (ausente = zero questões; sub = 1):

| área | ausentes | sub-representados |
|---|---|---|
| Hemato | anemias, leucemias, linfomas por subtipo, mieloma, PTI/PTT/HIT, hemoterapia, SMD | PV, amiloidose |
| Infecto | HIV e oportunistas, TB pulmonar e meníngea (manejo), endocardite (Duke 2023), meningite bacteriana, sepse (SSC) | PAC (2, nenhuma de manejo padrão) |
| Neuro | trombólise e trombectomia, estado de mal (sequência), meningite bacteriana, esclerose múltipla, neuro no HIV, delirium, Wernicke, Bell | HSA, compressão medular |
| Cardio | pericardite e tamponamento, IAMCSST completo, choque cardiogênico, BAV e marca-passo, ACLS, febre reumática, Chagas, CMH, amiloidose cardíaca | HAS (2), FA ritmo x frequência, endocardite (1) |
| Pneumo | TEP agudo, HP, TB como resposta, estadiamento de câncer de pulmão, sarcoidose pulmonar, pneumoconioses, VNI/VM, tabagismo | asma (1), PAC |
| Gastro | hepatites B e C, HDA varicosa e não varicosa (manejo), PBE, encefalopatia, CHC, doença biliar, HAI/CBP/Wilson/DILI, esôfago motor, H. pylori (V Consenso 2026) | nódulo hepático, hemocromatose |
| Nefro | ATR, nefrolitíase, GESF e lesão mínima, nefrite lúpica, DRPAD, SHU/PTT, GNRP, DMO e anemia da DRC | potássio, magnésio |
| Reumato | nefrite lúpica, SAF, esclerose sistêmica, Sjögren, ACG e Takayasu, PMR, artrite psoriásica, Still, IgG4 | LES (2) |
| Endócrino | CAD/EHH, hipoglicemia, tireoidites, crise tireotóxica, mixedema, feocromocitoma, MEN, acromegalia, DI, hipoparatireoidismo, osteoporose (como tema), crise adrenal | hipotireoidismo, insulinoterapia, dislipidemia (metas SBC 2025) |
| MBE e preventiva | sensibilidade, VPP/VPN, tipos de estudo, vieses, RR x OR | NNT (1) |

Note que **Still, IgG4, SAF, linfoma por subtipo, HIV oportunista e lítio** são
temas que a UERJ repete e que ele já errou (memória uerj-temas-recorrentes): nenhum
apareceu neste lote.

## 11. Gabaritos suspeitos (não conte como lacuna)

Fortes: pneumo q13 (transplante na DPOC), mista q15 (AIT, duas defensáveis),
nefro q3 (SIADH sintomática pede salina 3%), Einstein q17 (profilaxia de
endocardite em colonoscopia: ele marcou o certo), q28 (estado de mal refratário
sem a resposta), q42 (ácido bempedoico x iPCSK9), q43 (hidroxiureia), gastro q22
(pólipo hiperplásico de 10 mm), gastro q30 (comentário admite anulação).
Desatualizados no comentário: metronidazol no C. difficile (gastro q11), morfina
no EAP (cardio3 q10), iSGLT2 ausente na ICFEp (cardio2 q4), teste da salina no
hiperaldo (endo2 q1, Endocrine Society 2025).

## 12. Plano de ataque, em ordem

1. **Algoritmo escrito para as decisões instáveis**: ele já sabe o conteúdo.
   Fluxogramas de 3 a 5 passos: DHGNA (FIB-4) e ferro (IST); incidentaloma
   adrenal; hiperaldosteronismo; prolactina por faixa; derrame pleural (Light,
   gradiente, ADA, citometria); crise convulsiva (provocada x primeira crise x
   estado de mal: quando NÃO dar anticonvulsivante); nódulo pulmonar.
2. **Protocolo de prova para porte**: antes de marcar exame ou tratamento,
   perguntar "qual é o degrau mais barato que ainda resolve?" e "o que o paciente
   já usa?". Ler a primeira linha de antecedentes duas vezes.
3. **Bancas paulistas e Einstein**: sublinhar EXCETO; ler a segunda metade de cada
   alternativa longa procurando o absoluto.
4. **Semiologia valvar e congênita** em tabela única (Marfan, IM, IAo, EM, CIA,
   desdobramentos, manobras), cobrada com questão inédita: é a lacuna fixa da UERJ.
5. **Capturar o que falta**: provas de hemato e infecto (HIV, TB, endocardite,
   meningite), de preferência UERJ 2022 ou anterior, ou outra banca do Rio,
   porque as UERJ 2023 a 2026 já estão contaminadas.
