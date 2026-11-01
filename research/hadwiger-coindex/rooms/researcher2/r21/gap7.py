import sys, itertools, time
import networkx as nx
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible
def chi(G):
    nodes = list(G.nodes()); n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    adj = [[False]*n for _ in range(n)]
    for u, v in G.edges(): adj[idx[u]][idx[v]] = adj[idx[v]][idx[u]] = True
    for k in range(1, n+1):
        col = [-1]*n
        def bt(i):
            if i == n: return True
            for c in range(k):
                if all(not(adj[i][j] and col[j] == c) for j in range(i)):
                    col[i] = c
                    if bt(i+1): return True
                    col[i] = -1
            return False
        if bt(0): return k
t = time.time()
graphs = [G for G in nx.graph_atlas_g() if G.number_of_nodes() == 7]
print("7-vertex graphs in atlas:", len(graphs))
cands = []
for G in graphs:
    if G.number_of_edges() == 0: continue
    c = chi(G)
    if c < 4: continue
    nodes = list(G.nodes()); idx = {v:i for i,v in enumerate(nodes)}
    adj = [[False]*7 for _ in range(7)]
    for u, v in G.edges(): adj[idx[u]][idx[v]] = adj[idx[v]][idx[u]] = True
    if c == 4:
        z3 = feasible(7, adj, 3)[0]
        if z3:
            cands.append(G)
print("chi>=4 & zig<=3 with chi=4 (tau<chi certified):", len(cands), "time", round(time.time()-t,1), flush=True)
import pickle
pickle.dump([list(G.edges()) for G in cands], open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','wb'))
for G in cands:
    print("edges", G.number_of_edges(), "degseq", sorted(d for _, d in G.degree()), "omega", max(len(c) for c in nx.find_cliques(G)))
