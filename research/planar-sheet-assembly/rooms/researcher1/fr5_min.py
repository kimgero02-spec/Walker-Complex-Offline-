import itertools, networkx as nx
exec(open('fr5.py').read().split("# 엇갈림")[0])
E1 = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 4), (2, 5), (3, 5)]
E2 = [(0, 4), (1, 2), (1, 3), (3, 4), (4, 5)]
cl = [[(1, 0), (2, 0)], [(1, 3), (2, 2)], [(1, 5), (2, 3)], [(1, 2), (2, 1)], [(1, 4), (2, 4)], [(1, 1), (2, 5)]]
def ok(E1, E2, cl):
    try:
        A = build({1: E1, 2: E2}, cl); recover(A)
    except Exception: return False
    B = add_ww(A)
    return nx.check_planarity(A)[0] and not nx.check_planarity(B)[0]
changed = True
while changed:
    changed = False
    for i in range(len(E1)):
        if ok(E1[:i] + E1[i+1:], E2, cl): E1 = E1[:i] + E1[i+1:]; changed = True; break
    if changed: continue
    for i in range(len(E2)):
        if ok(E1, E2[:i] + E2[i+1:], cl): E2 = E2[:i] + E2[i+1:]; changed = True; break
    if changed: continue
    for i in range(len(cl)):
        if ok(E1, E2, cl[:i] + cl[i+1:]): cl = cl[:i] + cl[i+1:]; changed = True; break
print('E1', E1); print('E2', E2); print('cl', cl)
A = build({1: E1, 2: E2}, cl); B = add_ww(A)
print('ww edges', [e for e in B.edges if e not in A.edges and (e[1], e[0]) not in A.edges])
G = nx.Graph(recover(A)[0]); print('G', sorted(G.edges), 'planar', nx.check_planarity(G)[0])
print('P1 planar', nx.check_planarity(nx.Graph(E1))[0], 'P2 planar', nx.check_planarity(nx.Graph(E2))[0])
ok_, K = nx.check_planarity(B, counterexample=True); print('Kuratowski degs', sorted(d for _, d in K.degree() if d>=3), sorted(map(str,K.nodes)))
