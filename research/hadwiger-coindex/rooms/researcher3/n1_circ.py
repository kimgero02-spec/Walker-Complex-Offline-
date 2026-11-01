import networkx as nx, subprocess, math, sys
from b0lib import tau_h
def Kpq(p,q):
    G=nx.Graph(); G.add_nodes_from(range(p))
    for i in range(p):
        for j in range(i+1,p):
            d=min(j-i,p-(j-i))
            if d>=q: G.add_edge(i,j)
    return G
res=[]
cases=[(5,2),(7,2),(7,3),(8,3),(9,2),(9,4),(10,3),(11,3),(11,4),(11,5),(8,... if False else 8,3)] if False else [(5,2),(7,2),(8,3),(9,2),(10,3),(11,3),(11,4)]
for p,q in cases:
    G=Kpq(p,q)
    chi=math.ceil(p/q)
    th=tau_h(G)
    print(p,q,"omega",max(len(c) for c in nx.find_cliques(G)),"chi=ceil(p/q)",chi,"tau_h",th,flush=True)
