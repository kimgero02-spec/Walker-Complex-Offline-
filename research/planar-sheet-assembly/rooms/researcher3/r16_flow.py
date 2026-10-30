# R16: splitting expansion kappa = sum_pi prod gamma_b(pi_b) q^{beta1(I_pi)}  and W-form; checks only
import networkx as nx, itertools
from fractions import Fraction as Fr
exec(open('r15_kappa2.py').read().split('Eg=lambda')[0])
Eg=lambda *es: nx.Graph(list(es))
def setparts(xs):
    xs=list(xs)
    if not xs: yield []; return
    f,rest=xs[0],xs[1:]
    for p in setparts(rest):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
def pattern(c):  # partition of indices by equal values
    d={}
    for i,x in enumerate(c): d.setdefault(x,[]).append(i)
    return frozenset(frozenset(v) for v in d.values())
def finer(p,s): return all(any(b<=B for B in s) for b in p)
def gammas(B,H,q):
    t=tau(B,tuple(H),q); k=len(H)
    pats={}
    for c,v in t.items(): pats[pattern(c)]=v
    P=[frozenset(frozenset(b) for b in p) for p in setparts(range(k))]
    P=[p for p in P if len(p)<=q]
    # solve tau(sigma)=sum_{pi<=sigma} c_pi  by recursion from finest
    P.sort(key=lambda p:-len(p)); cc={}
    for s in P: cc[s]=pats[s]-sum(cc[p] for p in cc if p!=s and finer(p,s))
    return {p:cc[p]*Fr(q)**(len(p)-k) for p in cc}
def blocks_of(pieces):
    bl=[p.subgraph(C).copy() for p in pieces for C in nx.connected_components(p)]
    cnt={}
    for b in bl:
        for v in b: cnt[v]=cnt.get(v,0)+1
    hubs=sorted(v for v in cnt if cnt[v]>=2)
    return bl,hubs
def split_kappa(pieces,q):
    bl,hubs=blocks_of(pieces)
    data=[]
    for b in bl:
        H=[h for h in b if h in hubs]
        if H: data.append((H,gammas(b,H,q)))
    tot=Fr(0)
    for choice in itertools.product(*[list(g.items()) for H,g in data]):
        w=Fr(1); X=nx.Graph(); X.add_nodes_from(('h',h) for h in hubs)
        for j,((H,g),(p,gam)) in enumerate(zip(data,choice)):
            w*=gam
            for bi,part in enumerate(p):
                for i in part: X.add_edge(('p',j,bi),('h',H[i]))
        if w==0: continue
        b1=X.number_of_edges()-X.number_of_nodes()+nx.number_connected_components(X)
        tot+=w*Fr(q)**b1
    return tot
if __name__=='__main__':
    K5=nx.complete_graph(5)
    x=K5.copy(); x.remove_edges_from([(1,2),(2,3),(3,4),(4,1)])
    tests={'K5=(K5-C4,4 edges) r=4':[x]+[Eg(e) for e in [(1,2),(2,3),(3,4),(4,1)]],
           'K5=K113+K3 theta':[nx.Graph([(a,b) for a,b in K5.edges() if not (a>=2 and b>=2)]),nx.complete_graph([2,3,4])],
           'K5=(K5-2K2)+2K2':[nx.Graph([e for e in K5.edges() if e not in [(1,2),(3,4)]]),Eg((1,2)),Eg((3,4))],
           'K4=C4+2K2':[nx.cycle_graph([0,2,1,3]),Eg((0,1)),Eg((2,3))]}
    for name,pcs in tests.items():
        for q in (3,4,5,6):
            k=kappa(pcs,q) if True else None
            try: s=split_kappa(pcs,q)
            except KeyError: s='n/a'
            print(name,q,k,s)
