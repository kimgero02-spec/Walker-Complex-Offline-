import sys; sys.argv=['x']
exec(open('fr1_junction.py').read().split("K4m = ")[0])
def sq(c): return [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]
def band(k, twist):
    P, cl = {}, []
    for i in range(k): P[i] = sq([('t',i),('t',i+1),('s',i+1),('s',i)])
    for i in range(1, k): cl += [[(i-1,('t',i)),(i,('t',i))], [(i-1,('s',i)),(i,('s',i))]]
    if twist: cl += [[(k-1,('t',k)),(0,('s',0))], [(k-1,('s',k)),(0,('t',0))]]
    else:     cl += [[(k-1,('t',k)),(0,('t',0))], [(k-1,('s',k)),(0,('s',0))]]
    return build(P, cl)
rep_('E6 Moebius k=4 (V8)', band(4, 1), 4, nx.circulant_graph(8, [1, 4]))
