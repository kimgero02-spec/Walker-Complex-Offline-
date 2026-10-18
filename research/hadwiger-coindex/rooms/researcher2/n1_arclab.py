import itertools, networkx as nx
from pysat.solvers import Cadical153
def arc_label(G,k):
    V=list(G.nodes()); n=len(V); ix={v:i for i,v in enumerate(V)}
    adj=[[False]*n for _ in range(n)]
    for u,v in G.edges(): adj[ix[u]][ix[v]]=adj[ix[v]][ix[u]]=True
    labs=[(i,s) for i in range(k) for s in (1,-1)]
    L={};c=0
    for u in range(n):
        for v in range(n):
            if adj[u][v]:
                for x in labs: c+=1;L[(u,v,x)]=c
    S=Cadical153(); neg=lambda x:(x[0],-x[1])
    for (u,v,x),var in list(L.items()):
        S.add_clause([-var,L[(v,u,neg(x))]])
    for u in range(n):
        for v in range(n):
            if adj[u][v]:
                S.add_clause([L[(u,v,x)] for x in labs])
                for x,y in itertools.combinations(labs,2): S.add_clause([-L[(u,v,x)],-L[(u,v,y)]])
    for a,a2,b,b2 in itertools.product(range(n),repeat=4):
        if not(adj[a][b] and adj[a][b2] and adj[a2][b] and adj[a2][b2]): continue
        if a==a2 and b==b2: continue
        for x in labs: S.add_clause([-L[(a,b,x)],-L[(a2,b2,neg(x))]])
    return S.solve()
if __name__=="__main__":
    from n1_hom import hom_map
    def blow(G,m):
        H=nx.Graph()
        for u,v in G.edges():
            for a in range(m):
                for b in range(m): H.add_edge((u,a),(v,b))
        for u in G.nodes():
            for a in range(m):
                for b in range(a+1,m): H.add_edge((u,a),(u,b))
        return H
    T={'K3':nx.complete_graph(3),'K4':nx.complete_graph(4),'C5':nx.cycle_graph(5),'W5':nx.wheel_graph(6),'coC7':nx.complement(nx.cycle_graph(7)),'C5K2':blow(nx.cycle_graph(5),2)}
    for nme,G in T.items():
        print(nme,[(k,arc_label(G,k),hom_map(G,k)[0]) for k in (1,2,3)],flush=True)
