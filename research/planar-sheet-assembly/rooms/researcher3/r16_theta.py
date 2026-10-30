# R16: Theta*/8* checks: (s,u) condition at q=b+1, and C_{2k+1} v K_2 family
from r16_flow import *
def family(n,kind):
    C=[('c',i) for i in range(n)]; p,pp=('p',0),('p',1)
    G=nx.cycle_graph(C) if False else nx.Graph([(C[i],C[(i+1)%n]) for i in range(n)])
    G.add_edges_from((a,c) for a in (p,pp) for c in C); G.add_edge(p,pp)
    if kind=='T':
        v=C[0]; tri=[(v,p),(v,pp),(p,pp)]
        x=G.copy(); x.remove_edges_from(tri); return [x,nx.Graph(tri)],x,(v,p,pp)
    else:
        e=(C[0],C[1]); x=G.copy(); x.remove_edges_from([e,(p,pp)]); return [x,Eg(e),Eg((p,pp))],x,None
for n in (3,5,7):
    for kind in 'T8':
        pcs,x,H=family(n,kind)
        print(n,kind,'planar x',nx.check_planarity(x)[0],[kappa(pcs,q) for q in (3,4,5)])
        if kind=='T':
            s,u=coef3(x,H,4); print('   q=4: 1-sum s+2u =',1-sum(s.values())+2*u, ' s,u at q=3:',coef3(x,H,3) if n>=3 else '')
