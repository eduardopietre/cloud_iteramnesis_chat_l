#!/usr/bin/env python3
"""Gera os argumentos de iterq_create (lotes de 20) a partir de out/simulado{n}.json,
na ordem final do simulado."""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
PEDIDO = ("Agora, quero que se inspire nesse modelo E gere mais 4 simulados pareados com resoluções "
          "(2 arquivos separados por simulado). Cada um deve ter 80 questões. Não copie questões desse .pdf. "
          "Inspire-se nas que já fizemos. Adicione as questões criadas também via MCP, usando o bypass se "
          "necessário para criar questões livremente. [Escolheu: 4 alternativas, igual à UERJ; um grupo por simulado]")
os.makedirs(os.path.join(BASE, 'cargas'), exist_ok=True)
OUTD = os.environ.get('OUT_DIR', os.path.join(BASE, 'out'))
for n in [int(x) for x in sys.argv[1:]] or [2, 3, 4, 5]:
    qs = json.load(open(os.path.join(OUTD, f'simulado{n}.json')))
    itens = []
    for q in qs:
        alts = []
        for L in 'ABCD':
            fb = q['comentarios'][L]
            if L == q['gabarito']:
                fb += ' Para levar: ' + q['para_levar']
            alts.append({'text': q['alternativas'][L], 'feedback': fb})
        item = {
            'statement': f"[Simulado UERJ {n}, questão {q['numero']}] " + q['enunciado'],
            'alternatives': alts,
            'correct': q['gabarito'],
            'tags': q['tags'][:3],
            'level': q['nivel'],
            'decider': q['dado_decisivo'][:240],
            'trap': q['armadilha'],
        }
        if q.get('sourceQuestionId'):
            item['sourceQuestionId'] = q['sourceQuestionId']
        itens.append(item)
    for k in range(0, len(itens), 20):
        carga = {'group': f'Simulado UERJ {n}', 'questoes': itens[k:k + 20],
                 'rubricBypass': {'userRequested': True, 'userRequest': PEDIDO[:1000]}}
        f = os.path.join(BASE, 'cargas', f'S{n}-lote{k // 20 + 1}.json')
        json.dump(carga, open(f, 'w'), ensure_ascii=False)
        print(f, len(carga['questoes']), os.path.getsize(f))
