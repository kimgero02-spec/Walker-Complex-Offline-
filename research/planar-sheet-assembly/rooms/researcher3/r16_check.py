# R16: general Z_q-flow expansion of kappa on I(D); K5 +2 examples; T2-candidate attack on trivial decomposition
import networkx as nx, itertools, cmath
from fractions import Fraction as Fr
exec(open('r15_kappa2.py').read().split('Eg=lambda')[0])
Eg=lambda *es: nx.Graph(list(es))
def flow_kappa(pieces,q):
    blocks=[p.subgraph(C).copy() for p in pieces for C in nx.connected_components(p)]
    cnt={}
    for B in blocks:
        for v in B: cnt[v]=cnt.get(v,0)+1
    hubs=sorted(v for v in cnt if cnt[v]>=2)
    inc=[(i,h) for i,B in enumerate(blocks) for h in B if h in hubs]
    w=cmath.exp(2j*cmath.pi/q)
    hat={}
    for i,B in enumerate(blocks):
        H=[h for h in B if h in hubs]
        if not H: continue
        t=tau(B,tuple(H),q)
        def fh(k,t=t,H=H):
            return sum(float(v)*w**(-sum(kk*cc for kk,cc in zip(k,c))) for c,v in t.items())/q**len(H)
        hat[i]=(H,fh)
    tot=0
    for ks in itertools.product(range(q),repeat=len(inc)):
        K=dict(zip(inc,ks))
        if any(sum(K[(i,h)] for (i,hh) in inc if hh==h)%q for h in hubs for i in [0]): continue
        prodw=1
        for i,(H,fh) in hat.items():
            prodw*=fh(tuple(K[(i,h)] for h in H))
            if abs(prodw)<1e-14: break
        tot+=prodw
    return tot
K4=nx.complete_graph(4)
ex=[('K4=(C4,02,13,01) r=3',[Eg((0,1),(1,2),(2,3),(3,0)),Eg((0,2)),Eg((1,3)),Eg((0,1))])]
for name,p in ex:
    for q in (4,5):
        print(name,q,float(kappa(p,q)),flow_kappa(p,q).real)
K113=nx.complete_multipartite_graph(1,1,3)  # nodes 0,1 apexes; 2,3,4
K5m=nx.complete_graph(5); K5m.remove_edges_from([(0,1),(2,3)])
for q in (3,4,5):
    print('K5=(K113,K3) q=',q,kappa([K113,Eg((2,3),(3,4),(2,4))],q),
          ' K5=(K5-2K2,K2,K2) q=',q,kappa([K5m,Eg((0,1)),Eg((2,3))],q))
print('planar K113:',nx.check_planarity(K113)[0],' planar K5-2K2:',nx.check_planarity(K5m)[0])
print('T2-candidate on trivial decomposition (K4): K4 x K2 planar?',nx.check_planarity(nx.cartesian_product(K4,nx.complete_graph(2)))[0])
print('C4 x K2 planar?',nx.check_planarity(nx.cartesian_product(nx.cycle_graph(4),nx.complete_graph(2)))[0])
