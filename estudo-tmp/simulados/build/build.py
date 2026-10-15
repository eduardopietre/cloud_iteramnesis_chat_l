#!/usr/bin/env python3
"""Monta os Simulados UERJ 2 a 5: valida, ordena, numera e gera o HTML do
caderno e da resolução. O PDF sai de render.js."""
import glob, html, json, os, random, re, sys, collections

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RED = os.environ.get('RED_DIR', os.path.join(BASE, 'redacao'))
OUT = os.environ.get('OUT_DIR', os.path.join(BASE, 'build', 'out'))
os.makedirs(OUT, exist_ok=True)

ARMAS = {
    'Rótulo verdadeiro': ('blue', 'um dado real do paciente puxa para a doença de manual errada'),
    'Negativo no meio': ('blue', 'o discriminante é um dado negativo no meio do caso'),
    'Dado omitido': ('blue', 'o achado mais famoso foi retirado'),
    'Droga a deduzir': ('green', 'a droga em uso não é nomeada'),
    'Grade X / Y': ('purple', 'alternativa composta em que uma metade não basta'),
    'Qualificador': ('purple', 'o comando restringe o que se pede'),
    'Limiar': ('orange', 'um ponto de corte ou janela decide'),
    'Omissão': ('orange', 'a resposta certa é não fazer, ou o degrau mais simples'),
    'Cronologia': ('orange', 'o tempo entre os eventos decide'),
}
ORDEM_ARMAS = list(ARMAS)
BLOCOS = ['REU', 'HEM', 'INF', 'NEU', 'CAR', 'END', 'NEF', 'GAS', 'PNE']
CAMPOS = ['id', 'simulado', 'area', 'titulo', 'arma', 'comando', 'nivel', 'enunciado',
          'alternativas', 'gabarito', 'armadilha', 'dado_decisivo', 'resolucao',
          'comentarios', 'para_levar', 'referencias', 'tags', 'sourceQuestionId', 'alvo']
PROIBIDO = re.compile(r'[—–]|(?<!Hodgkin )\bcl[aá]ssic[oa]s?\b|\bt[ií]pic[oa]s?\b|patognom', re.I)


def carregar(n):
    qs = []
    for f in sorted(glob.glob(os.path.join(RED, f'*-S{n}.json'))):
        for q in json.load(open(f)):
            q['_arquivo'] = os.path.basename(f)
            qs.append(q)
    return qs


def validar(qs):
    erros = []
    for q in qs:
        i = q.get('id', '?')
        for c in CAMPOS:
            if c not in q:
                erros.append(f'{i}: falta {c}')
        alt = q.get('alternativas', {})
        if sorted(alt) != ['A', 'B', 'C', 'D']:
            erros.append(f'{i}: alternativas {sorted(alt)}')
        if sorted(q.get('comentarios', {})) != ['A', 'B', 'C', 'D']:
            erros.append(f'{i}: comentários incompletos')
        if q.get('gabarito') not in 'ABCD' or q.get('armadilha') not in 'ABCD':
            erros.append(f'{i}: gabarito/armadilha inválidos')
        if q.get('gabarito') == q.get('armadilha'):
            erros.append(f'{i}: armadilha igual ao gabarito')
        if q.get('arma') not in ARMAS:
            erros.append(f'{i}: arma "{q.get("arma")}"')
        if q.get('dado_decisivo', '') not in q.get('enunciado', ''):
            erros.append(f'{i}: dado_decisivo fora do enunciado')
        texto = json.dumps({k: q.get(k) for k in CAMPOS if k not in ('tags', 'sourceQuestionId')}, ensure_ascii=False)
        m = PROIBIDO.search(texto)
        if m:
            erros.append(f'{i}: termo proibido "{m.group(0)}"')
    ids = collections.Counter(q.get('id') for q in qs)
    erros += [f'id duplicado {k}' for k, v in ids.items() if v > 1]
    return erros


def ordenar(qs, n):
    rnd = random.Random(1000 + n)
    por_bloco = collections.defaultdict(list)
    for q in qs:
        por_bloco[q['id'].split('-')[1]].append(q)
    chave = []
    for b, lista in por_bloco.items():
        rnd.shuffle(lista)
        k = len(lista)
        off = rnd.random()
        for j, q in enumerate(lista):
            chave.append(((j + off) / k + rnd.random() * 0.02, q))
    chave.sort(key=lambda t: t[0])
    final = [q for _, q in chave]
    # evita duas da mesma área seguidas quando der
    for _ in range(3):
        for i in range(1, len(final)):
            if final[i]['area'] == final[i - 1]['area']:
                for j in range(i + 1, len(final)):
                    if final[j]['area'] != final[i - 1]['area'] and (j + 1 >= len(final) or final[i]['area'] != final[j + 1]['area']):
                        final[i], final[j] = final[j], final[i]
                        break
    for num, q in enumerate(final, 1):
        q['numero'] = num
    return final


def e(s):
    return html.escape(s or '')


def para(s):
    return '<br>'.join(e(x) for x in (s or '').split('\n'))


CSS = open(os.path.join(os.path.dirname(__file__), 'estilo.css')).read()


def pagina(titulo, corpo):
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{e(titulo)}</title><link rel="stylesheet" href="../fonts/fonts.css"><style>{CSS}</style></head>
<body>{corpo}</body></html>'''


def capa(n, tipo, sub, total, data):
    nome = 'Resolução' if tipo.startswith('Resolu') else 'Caderno'
    return f'''<section class="capa">
<div class="kicker">ITERAMNESE · {e(tipo.upper())}</div>
<div class="capa-meio"><div class="barra"></div>
<div class="capa-pre">Estilo UERJ</div>
<h1>Simulado {n}<br>{nome}</h1>
<p class="sub">{sub}</p></div>
<div class="capa-pe"><span>{total} questões</span><span>{e(data)}</span></div>
</section>'''


def badge(arma):
    cor = ARMAS[arma][0]
    return f'<span class="badge {cor}">{e(arma)}</span>'


def tabela_armas(qs):
    por = collections.defaultdict(list)
    for q in qs:
        por[q['arma']].append(q['numero'])
    linhas = ''.join(
        f'<tr><td>{badge(a)}</td><td>{e(ARMAS[a][1])}</td><td class="num">{len(por[a])}</td>'
        f'<td>{", ".join(map(str, sorted(por[a])))}</td></tr>'
        for a in ORDEM_ARMAS if por[a])
    return f'<table class="armas"><thead><tr><th>Arma da banca</th><th>O que faz</th><th class="num">Questões</th><th>Onde estão</th></tr></thead><tbody>{linhas}</tbody></table>'


def resolucao_html(n, qs, data):
    corpo = capa(n, 'Resolução comentada',
                 'Gabarito, a armadilha de cada questão, o dado que decide e o raciocínio completo, alternativa por alternativa.',
                 len(qs), data)
    corpo += f'''<section class="pg"><div class="kicker azul">ANTES DE CORRIGIR</div><h2>Como usar esta resolução</h2>
<p class="lead">Corrija olhando primeiro a coluna da arma. O que interessa não é o total de acertos, é em qual armadilha você caiu.</p>
{tabela_armas(qs)}
<div class="caixa"><h3>O que cada arma treina em você</h3><ul>
<li><b>Rótulo verdadeiro, negativo no meio, dado omitido:</b> a leitura em modo confirmação, a sua maior causa de erro de identificação.</li>
<li><b>Grade X / Y e qualificador:</b> a alternativa aceita pela metade e o comando lido pela metade.</li>
<li><b>Limiar, cronologia e omissão:</b> a regra aplicada sem checar a condição que a habilita, e o exame ou tratamento a mais, o seu padrão dominante em 15/10/2026.</li>
<li><b>Droga a deduzir:</b> a droga em uso que decide e não vem nomeada.</li></ul></div>
<p class="nota">Todas as questões têm uma única alternativa defensável pela diretriz citada. Se discordar de alguma, anote: discutir o gabarito é o melhor treino.</p></section>'''
    cel = ''.join(f'<div class="g"><span class="gn">{q["numero"]}</span><span class="gl">{q["gabarito"]}</span><span class="dot {ARMAS[q["arma"]][0]}"></span></div>' for q in qs)
    cont = collections.Counter(q['gabarito'] for q in qs)
    corpo += f'''<section class="pg"><div class="kicker azul">GABARITO</div><h2>Respostas</h2><div class="grade">{cel}</div>
<p class="nota">A cor ao lado de cada letra é a da arma da banca, como na tabela anterior. Distribuição: A {cont["A"]}, B {cont["B"]}, C {cont["C"]}, D {cont["D"]}.</p></section>'''
    corpo += '<section><div class="kicker azul">RESOLUÇÃO</div><h2>Questão por questão</h2>'
    for q in qs:
        alts = ''
        for L in 'ABCD':
            cls = 'certa' if L == q['gabarito'] else ('trap' if L == q['armadilha'] else '')
            tag = '<span class="tagc">CORRETA</span>' if cls == 'certa' else ('<span class="tagt">ARMADILHA</span>' if cls == 'trap' else '')
            alts += f'<div class="alt {cls}"><div class="at"><b>{L})</b> {e(q["alternativas"][L])} {tag}</div><div class="ac">{e(q["comentarios"][L])}</div></div>'
        corpo += f'''<article class="q">
<div class="qh"><span class="qn">{q["numero"]}</span><span class="qt">{e(q["area"])} · {e(q["titulo"])}</span><span class="qr">{badge(q["arma"])}<span class="gab">Gabarito {q["gabarito"]}</span></span></div>
<div class="enun">{para(q["enunciado"])}</div>
<div class="decide"><div class="dk">O DADO QUE DECIDE</div><i>{e(q["dado_decisivo"])}</i></div>
<p class="res"><b>Resolução.</b> {e(q["resolucao"])}</p>
{alts}
<div class="levar"><b>Para levar.</b> {e(q["para_levar"])}<div class="ref">{e(q["referencias"])}</div></div>
</article>'''
    corpo += '</section>'
    return pagina(f'Simulado UERJ {n} · Resolução', corpo)


def caderno_html(n, qs, data):
    corpo = capa(n, 'Caderno de questões',
                 'Prova inédita no formato da UERJ: quatro alternativas, casos longos e a armadilha da banca em cada questão.',
                 len(qs), data)
    corpo += f'''<section class="pg"><div class="kicker azul">ANTES DE COMEÇAR</div><h2>Instruções</h2>
<ul class="instr">
<li>São {len(qs)} questões de Clínica Médica, com quatro alternativas cada (A a D) e uma única correta.</li>
<li>Tempo sugerido: 4 horas, sem consulta, de uma vez só.</li>
<li>Marque as respostas na folha de respostas da última página, e só depois abra a resolução.</li>
<li>Nas questões de identificar, faça o teste do resto: liste os achados e veja se a hipótese explica todos. Antes de pedir exame ou tratamento, pergunte qual é o degrau mais simples que resolve e o que o paciente já usa.</li>
<li>Na correção, anote em qual arma da banca você caiu. É isso que vai para o diagnóstico, não o total.</li>
</ul></section><section>'''
    for q in qs:
        alts = ''.join(f'<div class="calt"><b>{L})</b> {e(q["alternativas"][L])}</div>' for L in 'ABCD')
        corpo += f'<article class="cq"><div class="cqn">{q["numero"]}</div><div class="cqb"><div class="cenun">{para(q["enunciado"])}</div>{alts}</div></article>'
    corpo += '</section>'
    linhas = ''.join(f'<div class="fr"><span class="frn">{q["numero"]}</span>' + ''.join(f'<span class="bol">{L}</span>' for L in 'ABCD') + '</div>' for q in qs)
    corpo += f'<section class="pg folha"><div class="kicker azul">FOLHA DE RESPOSTAS</div><h2>Simulado {n}</h2><p class="nota">Nome: ____________________________ Data: ____/____/______ Início: ____h____ Fim: ____h____</p><div class="folhagrid">{linhas}</div></section>'
    return pagina(f'Simulado UERJ {n} · Caderno', corpo)


def main():
    data = '15 de outubro de 2026'
    todos_ok = True
    for n in (int(x) for x in (sys.argv[1:] or ['2', '3', '4', '5'])):
        qs = carregar(n)
        erros = validar(qs)
        armas = collections.Counter(q.get('arma') for q in qs)
        gab = collections.Counter(q.get('gabarito') for q in qs)
        areas = collections.Counter(q['id'].split('-')[1] for q in qs if 'id' in q)
        print(f'S{n}: {len(qs)} questões | blocos {dict(areas)} | gabarito {dict(sorted(gab.items()))}')
        print('   armas', dict(armas.most_common()))
        if erros:
            todos_ok = False
            print('   ERROS:'); [print('    -', x) for x in erros]
            continue
        final = ordenar(qs, n)
        json.dump(final, open(os.path.join(OUT, f'simulado{n}.json'), 'w'), ensure_ascii=False, indent=1)
        open(os.path.join(OUT, f'Simulado_UERJ_{n}_Caderno.html'), 'w').write(caderno_html(n, final, data))
        open(os.path.join(OUT, f'Simulado_UERJ_{n}_Resolucao.html'), 'w').write(resolucao_html(n, final, data))
    sys.exit(0 if todos_ok else 1)


if __name__ == '__main__':
    main()
