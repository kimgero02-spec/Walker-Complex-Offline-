# R16: W-form (node-weighted nowhere-zero flow expansion) check
from r16_flow import *
from functools import lru_cache
def restrict(p,A):
    return frozenset(frozenset(b&A) for b in p if b&A)
def flowpoly_edges(E):
    # nowhere-zero count via inclusion-exclusion over edge subsets
    E=list(E); tot=0
    for r in range(len(E)+1):
        for T in itertools.combinations(E,r):
            X=nx.MultiGraph(); X.add_edges_from(T)
            b1=X.number_of_edges()-X.number_of_nodes()+nx.number_connected_components(X)
            tot+=(-1)**(len(E)-r)*Q**b1
    return tot
def wform(pieces,q):
    global Q; Q=q
    bl,hubs=blocks_of(pieces)
    data=[]
    for b in bl:
        H=[h for h in b if h in hubs]
        if H: data.append((H,gammas(b,H,q)))
    inc=[(j,i) for j,(H,g) in enumerate(data) for i in range(len(H))]
    tot=Fr(0)
    for r in range(len(inc)+1):
      for S in itertools.combinations(inc,r):
        Sset=set(S)
        # per block: A and choices of rho with parts>=2
        opts=[]
        for j,(H,g) in enumerate(data):
            A=frozenset(i for i in range(len(H)) if (j,i) in Sset)
            Ws={}
            for p,gam in g.items():
                rho=restrict(p,A)
                if all(len(b)>=2 for b in rho): Ws[rho]=Ws.get(rho,0)+gam
            opts.append(list(Ws.items()))
        # hub degree check: each hub must have 0 or >=2 incident edges in S
        hd={}
        for (j,i) in S: hd[data[j][0][i]]=hd.get(data[j][0][i],0)+1
        if any(v==1 for v in hd.values()): continue
        for ch in itertools.product(*opts):
            w=Fr(1)
            for (rho,W) in ch: w*=W
            if w==0: continue
            E=[]
            for j,((H,g),(rho,W)) in enumerate(zip(data,ch)):
                for bi,part in enumerate(sorted(rho,key=sorted)):
                    for i in part: E.append((('p',j,bi),('h',H[i])))
            tot+=w*flowpoly_edges(E)
    return tot
if __name__=='__main__':
    K5=nx.complete_graph(5)
    tests={'K5=(K5-2K2)+2K2':[nx.Graph([e for e in K5.edges() if e not in [(1,2),(3,4)]]),Eg((1,2)),Eg((3,4))],
           'K4=C4+2K2':[nx.cycle_graph([0,2,1,3]),Eg((0,1)),Eg((2,3))],
           'K5=K113+K3':[nx.Graph([(a,b) for a,b in K5.edges() if not (a>=2 and b>=2)]),nx.complete_graph([2,3,4])]}
    for n,p in tests.items():
        for q in (4,5): print(n,q,kappa(p,q),wform(p,q))
