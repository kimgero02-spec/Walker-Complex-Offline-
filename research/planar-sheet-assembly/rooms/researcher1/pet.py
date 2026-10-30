import networkx as nx, itertools as it
faces=[[0, 4, 3, 2, 1], [0, 5, 8, 6, 1], [0, 5, 7, 9, 4], [1, 6, 9, 7, 2], [2, 7, 5, 8, 3], [3, 8, 6, 9, 4]]
def fe(f): return {frozenset(x) for x in zip(f,f[1:]+f[:1])}
def piece(gs):
    g=nx.Graph()
    for f in gs: g.add_edges_from(zip(f,f[1:]+f[:1]))
    return g
def bd(gs):
    cnt={}
    for f in gs:
        for k in fe(f): cnt[k]=cnt.get(k,0)+1
    return nx.Graph([tuple(k) for k,v in cnt.items() if v==1])
for npieces in [2,3]:
  for drop in [0]:
    rest=[f for i,f in enumerate(faces) if i!=drop]
    for lab in it.product(range(npieces),repeat=5):
        if lab[0]!=0 or len(set(lab))!=npieces: continue
        gs=[[rest[i] for i in range(5) if lab[i]==g] for g in range(npieces)]
        Ps=[piece(g) for g in gs]; B=[bd(g) for g in gs]
        okdisk=all(nx.is_connected(b) and all(d==2 for _,d in b.degree()) and P.number_of_nodes()-P.number_of_edges()+len(g)==1 for b,P,g in zip(B,Ps,gs))
        inter=[]
        for i,j in it.combinations(range(npieces),2):
            V=set(Ps[i])&set(Ps[j]); Ei={frozenset(e) for e in Ps[i].edges()}&{frozenset(e) for e in Ps[j].edges()}
            I=nx.Graph(); I.add_nodes_from(V); I.add_edges_from(tuple(e) for e in Ei)
            inter.append(((i,j),nx.number_connected_components(I),[sorted(c) for c in nx.connected_components(I)],len(Ei)))
        print(npieces,lab,"disk" if okdisk else "notdisk",inter)
