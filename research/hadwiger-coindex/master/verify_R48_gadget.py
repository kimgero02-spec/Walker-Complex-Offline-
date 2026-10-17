import networkx as nx, itertools
def apol(tag):
    p,q,r,s,P,Q,R=[tag+x for x in ["p","q","r","s","P","Q","R"]]
    E=list(itertools.combinations([p,q,r,s],2))
    E+=[(P,q),(P,r),(P,s),(Q,p),(Q,r),(Q,s),(R,p),(R,q),(R,s)]
    return E,(p,q,r,P,Q,R)
G=nx.Graph()
E1,(p,q,r,P,Q,R)=apol("a"); E2,(p2,q2,r2,P2,Q2,R2)=apol("b")
K1=["w1","w2","w3","w4"]; K2=["v1","v2","v3","v4"]
G.add_edges_from(E1+E2+list(itertools.combinations(K1,2))+list(itertools.combinations(K2,2)))
V1=set(n for e in E1 for n in e)|set(K1); V2=set(n for e in E2 for n in e)|set(K2)
cross=[(v,x) for v in ("v1","v2","v3") for x in (p,q,r)]+[("v4",x) for x in (P,Q,R)]+[(v,x) for v in ("w1","w2","w3") for x in (p2,q2,r2)]+[("w4",x) for x in (P2,Q2,R2)]
G.add_edges_from(cross)
print("n,m",G.number_of_nodes(),G.number_of_edges())
print("planar",nx.check_planarity(G.subgraph(V1))[0],nx.check_planarity(G.subgraph(V2))[0])
print("max cross deg",max(sum(1 for u in G[v] if (u in V1)!=(v in V1)) for v in G))
order=sorted(G,key=lambda v:-G.degree(v))
def col(k,allowed):
    c={}
    def bt(i):
        if i==len(order): return True
        v=order[i]
        for x in allowed(v):
            if x<k and all(c.get(u)!=x for u in G[v]):
                c[v]=x
                if bt(i+1): return True
                del c[v]
        return False
    return bt(0)
print("5-col",col(5,lambda v:range(5)),"6-col",col(6,lambda v:range(6)))
print("6-col with V1 in 4 colors",col(6,lambda v:range(4) if v in V1 else range(6)))
print("6-col with V2 in 4 colors",col(6,lambda v:range(4) if v in V2 else range(6)))
