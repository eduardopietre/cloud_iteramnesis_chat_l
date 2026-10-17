#!/usr/bin/env python3
"""Equilibra gabarito e armadilha por simulado trocando alternativas de lugar
(texto e comentário juntos). Só mexe em questões que não são Grade X / Y, cujas
alternativas não são numéricas e cujos textos não citam letras.
Uso: python3 balancear.py <dir_redacao> <n> [<n> ...]"""
import glob, itertools, json, os, re, sys

d = sys.argv[1]
LET = 'ABCD'
CITA = re.compile(r'\b(alternativas?|letras?|op[cç][aã]o)\s+[A-D]\b|\(\s*[A-D]\s*\)|\b[A-D]\)', re.I)


def movivel(q):
    if q['arma'] == 'Grade X / Y':
        return False
    if all(re.match(r'^\s*[<>≥≤]?\s*\d', v) for v in q['alternativas'].values()):
        return False
    txt = ' '.join([q['resolucao'], q['para_levar']] + list(q['comentarios'].values()))
    return not CITA.search(txt)


def custo(qs):
    g = [sum(q['gabarito'] == L for q in qs) for L in LET]
    t = [sum(q['armadilha'] == L for q in qs) for L in LET]
    m = len(qs) / 4
    return sum((x - m) ** 2 for x in g) + sum((x - m) ** 2 for x in t)


def trocar(q, a, b):
    alt, com = q['alternativas'], q['comentarios']
    alt[a], alt[b] = alt[b], alt[a]
    com[a], com[b] = com[b], com[a]
    for k in ('gabarito', 'armadilha'):
        if q[k] == a:
            q[k] = b
        elif q[k] == b:
            q[k] = a


for n in sys.argv[2:]:
    arqs = sorted(glob.glob(os.path.join(d, f'*-S{n}.json')))
    dados = {f: json.load(open(f)) for f in arqs}
    qs = [q for f in arqs for q in dados[f]]
    movs = [q for q in qs if movivel(q)]
    antes = custo(qs)
    trocas = 0
    while True:
        base = custo(qs)
        melhor = None
        for q in movs:
            for a, b in itertools.combinations(LET, 2):
                trocar(q, a, b)
                c = custo(qs)
                trocar(q, a, b)
                if c < base - 1e-9 and (melhor is None or c < melhor[0]):
                    melhor = (c, q, a, b)
        if not melhor:
            break
        trocar(melhor[1], melhor[2], melhor[3])
        trocas += 1
    for f in arqs:
        json.dump(dados[f], open(f, 'w'), ensure_ascii=False, indent=1)
    g = {L: sum(q['gabarito'] == L for q in qs) for L in LET}
    t = {L: sum(q['armadilha'] == L for q in qs) for L in LET}
    print(f'S{n}: móveis {len(movs)}/{len(qs)}, trocas {trocas}, custo {antes:.1f}->{custo(qs):.1f}, gab {g}, arm {t}')
