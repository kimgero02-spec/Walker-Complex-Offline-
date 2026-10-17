import networkx as nx

def col3_all(G):
    nodes = list(G.nodes())
    sols = []
    def bt(i, c):
        if i == len(nodes):
            sols.append(dict(c)); return
        v = nodes[i]
        for k in range(3):
            if all(c.get(w) != k for w in G[v] if w in c):
                c[v] = k; bt(i+1, c); del c[v]
    bt(0, {})
    return sols

def colorable(G, q):
    nodes = list(G.nodes())
    def bt(i, c):
        if i == len(nodes): return True
        v = nodes[i]
        for k in range(q):
            if all(c.get(w) != k for w in G[v] if w in c):
                c[v] = k
                if bt(i+1, c): return True
                del c[v]
        return False
    return bt(0, {})

# H_8: diamonds D1 (x,y ; v,r), D2 (x',y' ; u,p), edge rp; e = uv
H = nx.Graph()
H.add_edges_from([("x","y"),("v","x"),("v","y"),("r","x"),("r","y"),
                  ("xp","yp"),("u","xp"),("u","yp"),("p","xp"),("p","yp"),("r","p")])
G = H.copy(); G.add_edge("u","v")
print("H8: H 3-col", colorable(H,3), " H 2-col", colorable(H,2))
print("H8: G 3-col", colorable(G,3))
Ge = nx.contracted_nodes(G, "u", "v", self_loops=False)
print("H8: G/e 3-col", colorable(Ge,3), " G/e 4-col", colorable(Ge,4))
print("H8: K4 subgraph in G/e:", any(len(c)>=4 for c in nx.enumerate_all_cliques(Ge)))
sols = col3_all(H)
print("H8: #3-colorings of H", len(sols), " all c(u)!=c(v):", all(s['u']!=s['v'] for s in sols))
print("H8: node connectivity of G", nx.node_connectivity(G))

# W4 = wheel with hub 0, rim 1..4
W = nx.wheel_graph(5)
print("W4: 3-col", colorable(W,3), " 2-col", colorable(W,2), " connectivity", nx.node_connectivity(W))
for name,(a,b) in {"spoke 0-1":(0,1),"rim 1-2":(1,2)}.items():
    He = W.copy(); He.remove_edge(a,b)
    We = nx.contracted_nodes(W, a, b, self_loops=False)
    S = col3_all(He)
    print("W4", name, "G/e 3-col", colorable(We,3), " #col of H", len(S),
          " some c(a)=c(b):", any(s[a]==s[b] for s in S), " all c(a)!=c(b):", all(s[a]!=s[b] for s in S))
