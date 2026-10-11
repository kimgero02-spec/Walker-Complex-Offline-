"""SW 높이: 단체복합체 X(자유 Z2 작용 g)의 정점튜플(단체집합) 모델. 정규화 코체인."""
import sys, time
from boxlib import *

def join_model(G):
    """B(G) * S^0 (극 2개). 정점: 0..2n-1 (B 정점; (v,s)=v+s*n), 2n, 2n+1 극. 반환 (nv, simplex set, g)"""
    n,S=B_simplices(G)
    S=set(S)|{0}
    P1=1<<(2*n); P2=1<<(2*n+1)
    full=set()
    for m in S:
        full.add(m); full.add(m|P1); full.add(m|P2)
    full.discard(0)
    def g(v):
        if v<n: return v+n
        if v<2*n: return v-n
        return 2*n+1 if v==2*n else 2*n
    return 2*n+2, full, g

def direct_B0_model(G):
    n,S=B0_simplices(G)
    def g(v): return v+n if v<n else v-n
    return 2*n, set(S), g

def sw_height_tuples(nv, simps, g, kmax=8, maxtuples=3_000_000, verbose=True):
    eps=[0 if v<g(v) else 1 for v in range(nv)]
    # tuple 열거
    maxdim=max(bin(m).count('1') for m in simps)-1
    kmax=min(kmax,maxdim) if False else kmax
    tuples={0:[(v,) for v in range(nv) if (1<<v) in simps]}
    k=0
    total=len(tuples[0])
    while k<kmax:
        nxt=[]
        for t in tuples[k]:
            m=0
            for v in t: m|=1<<v
            last=t[-1]
            for u in range(nv):
                if u==last: continue
                if (m|(1<<u)) in simps: nxt.append(t+(u,))
        if not nxt: break
        k+=1; tuples[k]=nxt; total+=len(nxt)
        if verbose: print('  k',k,'tuples',len(nxt),flush=True)
        if total>maxtuples: print('  too many'); return None
    def canon(t):
        gt=tuple(g(v) for v in t)
        return min(t,gt)
    orb={kk:sorted({canon(t) for t in L}) for kk,L in tuples.items()}
    idx={kk:{t:i for i,t in enumerate(L)} for kk,L in orb.items()}
    h=0
    for k in range(1,max(orb)+1):
        vec=0
        for i,t in enumerate(orb[k]):
            if all((eps[t[a]]+eps[t[a+1]])%2 for a in range(k)): vec|=1<<i
        rows={}
        for i,t in enumerate(orb[k]):
            for a in range(k+1):
                f=t[:a]+t[a+1:]
                if any(f[b]==f[b+1] for b in range(len(f)-1)): continue
                j=idx[k-1][canon(f)]
                rows[j]=rows.get(j,0)^(1<<i)
        piv={}
        for x in rows.values():
            while x:
                hb=x.bit_length()-1
                if hb in piv: x^=piv[hb]
                else: piv[hb]=x; break
        x=vec
        while x:
            hb=x.bit_length()-1
            if hb in piv: x^=piv[hb]
            else: break
        if verbose: print('  k',k,'w^k',('nonzero' if x else 'zero/coboundary'),flush=True)
        if x==0 and vec!=0 or vec==0:
            if x==0: break
        h=k
    return h, max(orb)

if __name__=='__main__':
    import networkx as nx
    from table import lex
    name=sys.argv[1]
    G={'K3':nx.complete_graph(3),'K4':nx.complete_graph(4),'C5':nx.cycle_graph(5),'Pet':nx.petersen_graph(),
       'C5K2':lex(nx.cycle_graph(5),nx.complete_graph(2)),'coC7':nx.complement(nx.cycle_graph(7))}[name]
    mode=sys.argv[2]
    nv,S,g=(join_model(G) if mode=='join' else direct_B0_model(G))
    print(name,mode,sw_height_tuples(nv,S,g,kmax=int(sys.argv[3])))
