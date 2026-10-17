# R10: odd-wheel hub split. G/e = W_{2k+1}; search for chosen small splittings (not an evidence sweep)
import itertools, networkx as nx, sys
def cols(G,q=3):
    V=list(G.nodes()); out=[]
    def rec(i,c):
        if i==len(V): out.append(dict(c)); return
        x=V[i]
        for a in range(q):
            if all(c.get(y)!=a for y in G[x]):
                c[x]=a; rec(i+1,c); del c[x]
    rec(0,{}); return out
def build(n,Su,Sv):
    G=nx.cycle_graph(n)
    G.add_edge('u','v')
    for i in Su: G.add_edge('u',i)
    for i in Sv: G.add_edge('v',i)
    return G
def analyze(G,verbose=False):
    H=G.copy(); H.remove_edge('u','v')
    CG=cols(G); 
    if not CG: return None
    CH=cols(H)
    danger=all(c['u']!=c['v'] for c in CH)
    eq={x:[p for p in H if all(c[p]==c[x] for c in CH) and p!=x] for x in ('u','v')}
    t4=any(H.has_edge(p,r) for p in eq['u']+['u'] for r in eq['v']+['v'])
    # T5
    Ge=nx.contracted_nodes(G,'u','v',self_loops=False)
    t5=any(all(Ge.has_edge(a,b) for a,b in itertools.combinations(T+('u',),2)) for T in itertools.combinations([x for x in Ge if x!='u'],3))
    kG=nx.node_connectivity(G); kH=nx.node_connectivity(H); luv=nx.node_connectivity(H,'u','v')
    return dict(danger=danger,eq=eq,t4=t4,t5=t5,kG=kG,kH=kH,luv=luv,nCH=len(CH),nCG=len(CG))

if __name__=="__main__":
    n=int(sys.argv[1])
    for r in range(1,n):
      for Su in itertools.combinations(range(n),r):
        if 0 not in Su: continue
        rest=[i for i in range(n) if i not in Su]
        for extra in range(0,len(Su)+1):
          for ov in itertools.combinations(Su,extra):
            Sv=tuple(sorted(rest+list(ov)))
            if len(Sv)<1: continue
            G=build(n,Su,Sv); a=analyze(G)
            if a and a['danger'] and not a['t4'] and not a['t5'] and a['kG']>=3:
                print(Su,Sv,a)
