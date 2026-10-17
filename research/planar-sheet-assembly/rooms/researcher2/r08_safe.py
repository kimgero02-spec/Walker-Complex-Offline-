# R08 researcher2: chi-safety of an edge contraction e=uv in G.
# Lemma C: safe <=> exists q-colouring (q=chi(G)) of H=G-e with c(u)=c(v).
# Checks only the specific examples named in the report (no exhaustive search).
import itertools
import networkx as nx

def colourings(H, q):
    nodes = list(H.nodes())
    idx = {x: i for i, x in enumerate(nodes)}
    out = []
    def rec(i, col):
        if i == len(nodes):
            out.append(dict(col)); return
        x = nodes[i]
        for k in range(q):
            if all(col.get(y) != k for y in H.neighbors(x) if y in col):
                col[x] = k
                rec(i + 1, col)
                del col[x]
    rec(0, {})
    return out

def colourable(H, q):
    return len(colourings(H, q)) > 0 if H.number_of_nodes() else True

def chi(G):
    q = 1
    while not colourable(G, q):
        q += 1
    return q

def analyse(name, G, u, v):
    q = chi(G)
    H = G.copy(); H.remove_edge(u, v)
    cols = colourings(H, q)
    safe = any(c[u] == c[v] for c in cols)
    chiH = chi(H)
    Gc = nx.contracted_nodes(G, u, v, self_loops=False)
    chi_contr = chi(nx.Graph(Gc))
    # pinning: p in N_H(v), p != u, every q-colouring of H has c(p)==c(u)
    pinned = [p for p in H.neighbors(v) if p != u and all(c[p] == c[u] for c in cols)]
    cuts = [w for w in H.nodes() if w not in (u, v) and nx.is_connected(H) and
            not nx.is_connected(H.subgraph([x for x in H.nodes() if x != w])) and
            nx.has_path(H.subgraph([x for x in H.nodes() if x != w]), u, u) and False]
    print(f"{name}: chi(G)={q}, chi(G-e)={chiH}, #q-col(H)={len(cols)}, "
          f"safe={safe}, chi(G/e)={chi_contr}, pinned nbrs of v: {pinned}")

# C4, e=14
C4 = nx.cycle_graph([1, 2, 3, 4])
analyse("C4, e=14", C4, 1, 4)
# Prism: a,b,c,x,y,z ; triangles abc, xyz; rungs ax,by,cz
P = nx.Graph([('a','b'),('b','c'),('c','a'),('x','y'),('y','z'),('z','x'),('a','x'),('b','y'),('c','z')])
analyse("Prism, e=ab", P, 'a', 'b')
analyse("Prism, e=ax", P, 'a', 'x')
# Prism/{a,b} then edge m-c
Pab = nx.contracted_nodes(P, 'a', 'b', self_loops=False)
Pab = nx.relabel_nodes(nx.Graph(Pab), {'a': 'm'})
analyse("Prism/ab, e=mc", Pab, 'm', 'c')
# W: triangle xyz, a~x,z, b~y,z, a~b
W = nx.Graph([('x','y'),('y','z'),('z','x'),('a','x'),('a','z'),('b','y'),('b','z'),('a','b')])
analyse("W, e=ab", W, 'a', 'b')
# K4 with edge uw subdivided by v
S = nx.Graph([('x','y'),('u','x'),('u','y'),('w','x'),('w','y'),('w','v'),('v','u')])
analyse("K4 subdivided, e=uv", S, 'u', 'v')
# 8-vertex chain example: gadget1 {x,y,v,r} diamond-with-edge xy, gadget2 {x',y',u,p}, edge rp, e=uv
G8 = nx.Graph([('x','y'),('x','v'),('x','r'),('y','v'),('y','r'),
               ("x'","y'"),("x'",'u'),("x'",'p'),("y'",'u'),("y'",'p'),('r','p'),('u','v')])
analyse("8-vertex chain, e=uv", G8, 'u', 'v')
