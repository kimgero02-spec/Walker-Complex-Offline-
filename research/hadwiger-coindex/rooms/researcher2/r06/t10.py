import sys
sys.path.insert(0,'.')
from graphs import *
from pi1 import *
from homol import neighborhood_complex
def complex_parts(n, adj):
    F = neighborhood_complex(n, adj)
    V = sorted({v for f in F for v in f})
    E = sorted({tuple(sorted(f)) for f in F if len(f) == 2})
    T = sorted({tuple(sorted(f)) for f in F if len(f) == 3})
    return V, E, T
def test(name, n, adj):
    V, E, T = complex_parts(n, adj)
    ng, rels = pi1_presentation(V, E, T)
    alive, left = tietze(ng, rels)
    print(name, 'gens', ng, 'rels', len(rels), 'after: alive gens', len(alive), 'rels left', len(left), flush=True)
    if not alive and not left: print('  => pi1(N) trivial (proved by elimination)', flush=True)
    else: print('  => inconclusive', flush=True)
#test('C5', *cycle(5))
#test('C6', *cycle(6))
#test('C5[K2]', *lex_blowup(5, cycle(5)[1], 2))
#test('Grotzsch', *mycielski(5, cycle(5)[1]))
