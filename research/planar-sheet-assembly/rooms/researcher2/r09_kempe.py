import networkx as nx
exec(open('r09_check.py').read().split('# H_8')[0])
def kempe_linked(H, c, u, v):
    a, b = c[u], c[v]
    if a == b: return None
    S = [x for x in H.nodes() if c[x] in (a, b)]
    K = H.subgraph(S)
    return nx.has_path(K, u, v)
H = nx.Graph()
H.add_edges_from([("x","y"),("v","x"),("v","y"),("r","x"),("r","y"),
                  ("xp","yp"),("u","xp"),("u","yp"),("p","xp"),("p","yp"),("r","p")])
S = col3_all(H)
print("H8 Kempe-linked in all colorings:", all(kempe_linked(H,s,'u','v') for s in S))
W = nx.wheel_graph(5)
He = W.copy(); He.remove_edge(1,2)
S = col3_all(He)
print("W4 rim: Kempe-linked in all colorings:", all(kempe_linked(He,s,1,2) for s in S))
# W4 spoke: a witness coloring with c(h)!=c(v1) Kempe-separated?
He = W.copy(); He.remove_edge(0,1)
S = col3_all(He)
print("W4 spoke: exists coloring with c(h)!=c(v1) and not Kempe-linked:",
      any(s[0]!=s[1] and not kempe_linked(He,s,0,1) for s in S))
