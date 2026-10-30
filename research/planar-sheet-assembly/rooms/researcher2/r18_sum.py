# R18: 조각 색칠수 합 = chi(G) 의 결정적 예 구성 (근거 아님, 구성 확인용)
import itertools, networkx as nx

def chi(G):
    n=G.number_of_nodes()
    if G.number_of_edges()==0: return 1 if n else 0
    nodes=list(G.nodes())
    for k in range(1,n+1):
        col={}
        order=sorted(nodes,key=lambda v:-G.degree(v))
        def bt(i):
            if i==len(order): return True
            v=order[i]
            for c in range(k):
                if all(col.get(u)!=c for u in G[v]):
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
def omega(G): return max(len(c) for c in nx.find_cliques(G)) if G.number_of_edges() else 1

def report(name,G,sheets):
    cov=set()
    for P in sheets: cov|={frozenset(e) for e in P.edges()}
    assert cov=={frozenset(e) for e in G.edges()}, "not a cover"
    assert all(nx.check_planarity(P)[0] for P in sheets)
    cs=[chi(P) for P in sheets]; ws=[omega(P) for P in sheets]
    print(name,"chi(G)=",chi(G),"omega(G)=",omega(G),"sheet chi",cs,"sum",sum(cs),"sheet omega",ws,"sum",sum(ws))

if __name__=="__main__":
    # (c) K6 = Oct u 3K2
    K6=nx.complete_graph(6); M=[(0,3),(1,4),(2,5)]
    Oct=nx.Graph([e for e in K6.edges() if tuple(sorted(e)) not in M]); Mg=nx.Graph(M)
    report("K6=Oct+3K2",K6,[Oct,Mg])
    
    # (a) K7 = C7 u B1 u B2, bipartite planar
    def search_bip_split(G,base_sheets,classes_bits):
        # classes_bits: vertex -> (b1,b2); edges not in base must go to a sheet where bits differ
        rest=[e for e in G.edges() if not any(P.has_edge(*e) for P in base_sheets)]
        forced1=[e for e in rest if classes_bits[e[0]][0]!=classes_bits[e[1]][0] and classes_bits[e[0]][1]==classes_bits[e[1]][1]]
        forced2=[e for e in rest if classes_bits[e[0]][1]!=classes_bits[e[1]][1] and classes_bits[e[0]][0]==classes_bits[e[1]][0]]
        free=[e for e in rest if classes_bits[e[0]][0]!=classes_bits[e[1]][0] and classes_bits[e[0]][1]!=classes_bits[e[1]][1]]
        bad=[e for e in rest if classes_bits[e[0]]==classes_bits[e[1]]]
        if bad: return None
        for mask in range(2**len(free)):
            B1=nx.Graph(forced1+[free[i] for i in range(len(free)) if mask>>i&1])
            B2=nx.Graph(forced2+[free[i] for i in range(len(free)) if not mask>>i&1])
            if nx.check_planarity(B1)[0] and nx.check_planarity(B2)[0]:
                return B1,B2
        return None
    K7=nx.complete_graph(7); C7=nx.cycle_graph(7)
    bits={0:(0,0),1:(0,0),2:(0,1),3:(0,1),4:(1,0),5:(1,0),6:(1,1)}
    r=search_bip_split(K7,[C7],bits)
    if r:
        B1,B2=r; print("B1",sorted(B1.edges())); print("B2",sorted(B2.edges()))
        report("K7=C7+B1+B2",K7,[C7,B1,B2])
    else: print("K7 none for this coloring")
    
    # (b) Groetzsch = B1 u B2
    Gz=nx.mycielski_graph(4)  # Groetzsch, 11 vertices
    print("Gz",Gz.number_of_nodes(),Gz.number_of_edges())
    # find a 4-colouring, try splits
    import random
    def colorings(G,k,limit=200):
        nodes=list(G.nodes()); out=[]; col={}
        def bt(i):
            if len(out)>=limit: return
            if i==len(nodes): out.append(dict(col)); return
            v=nodes[i]
            for c in range(k):
                if all(col.get(u)!=c for u in G[v]):
                    col[v]=c; bt(i+1); del col[v]
        bt(0); return out
    found=False
    for col in colorings(Gz,4,400):
        b={v:(col[v]>>1&1,col[v]&1) for v in Gz}
        r=search_bip_split(Gz,[],b)
        if r:
            B1,B2=r; print("Gz B1",sorted(B1.edges())); print("Gz B2",sorted(B2.edges()))
            report("Groetzsch=B1+B2",Gz,[B1,B2]); found=True; break
    if not found: print("Gz: none in sampled colourings")
