# R06 researcher3: Kempe-chain analysis of Q* and of planar Q*-e.
import itertools, networkx as nx
from r06_qstar import qstar, all_colorings, rainbow

T1, T2 = ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3']

def kempe_chain(Q, c, v, al, be):
    S = {u for u in Q if c[u] in (al, be)}
    return nx.node_connected_component(Q.subgraph(S), v)

def swap(c, K, al, be):
    d = dict(c)
    for u in K: d[u] = be if c[u] == al else al
    return d

def key(c): return tuple(sorted(c.items()))

def kempe_moves(Q, c, k=4):
    seen = set()
    for v in Q:
        for be in range(k):
            al = c[v]
            if be == al: continue
            K = frozenset(kempe_chain(Q, c, v, al, be))
            if (K, frozenset((al, be))) in seen: continue
            seen.add((K, frozenset((al, be))))
            yield v, al, be, K, swap(c, K, al, be)

def classes(Q, k=4):
    C = all_colorings(Q, k); idx = {key(c): i for i, c in enumerate(C)}
    H = nx.Graph(); H.add_nodes_from(range(len(C)))
    for i, c in enumerate(C):
        for *_, d in kempe_moves(Q, c, k): H.add_edge(i, idx[key(d)])
    return C, H

def good(c): return not rainbow(c, T1) and not rainbow(c, T2)

if __name__ == '__main__':
    Qs = qstar()
    C, H = classes(Qs)
    print('Q*: 4-colorings', len(C), ' Kempe classes', nx.number_connected_components(H))
    # start: T1 nonrainbow coloring (a1=a2=4 from phi); all single Kempe swaps that make T2 nonrainbow
    phi = {f'{x}{i}': i for x in 'amb' for i in (1, 2, 3)}
    psi0 = dict(phi); psi0['a1'] = 4; psi0['a2'] = 4
    print('psi0 colors:', {k: psi0[k] for k in sorted(psi0)})
    for v, al, be, K, d in kempe_moves(Qs, psi0):
        if not rainbow(d, T2):
            print(f'  swap ({al},{be}) at {v}: chain={sorted(K)} -> T1 rainbow? {rainbow(d, T1)}')
    # planar Q* - (a1,b2): Kempe distance from phi to good set
    for e in [('a1', 'b2'), ('a1', 'm2')]:
        Q = Qs.copy(); Q.remove_edge(*e)
        C, H = classes(Q); idx = {key(c): i for i, c in enumerate(C)}
        dist = nx.single_source_shortest_path_length(H, idx[key(phi)])
        dg = min(dist[i] for i, c in enumerate(C) if good(c) and i in dist)
        print(f'Q*-{e}: colorings {len(C)}, Kempe classes {nx.number_connected_components(H)}, Kempe distance phi->good = {dg}')
