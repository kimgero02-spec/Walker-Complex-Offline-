import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'r15_kappa2.py')).read().split('Eg=lambda')[0])
import networkx as nx, itertools
from fractions import Fraction as Fr
Eg=lambda *es: nx.Graph(list(es))
def tau4(B,h,q): return tau(B,h,q)
for q in (3,4):
    C4=Eg((0,1),(1,2),(2,3),(3,0)); t=tau(C4,(0,1,2,3),q)
    s01=E({c:v*psi(c[0],c[1],q) for c,v in t.items()},q,4)/(q-1)
    s23=E({c:v*psi(c[2],c[3],q) for c,v in t.items()},q,4)/(q-1)
    v=E({c:val*psi(c[0],c[1],q)*psi(c[2],c[3],q) for c,val in t.items()},q,4)/(q-1)**2
    T=Fr(-1,q-1)
    f=1+(q-1)*(T*s01+T*s23)+(q-1)**2*T*T*v
    print('fig8 block',q,kappa([C4,Eg((0,1)),Eg((2,3))],q),f,' v vs s01*s23:',v,s01*s23)
    bow=[Eg(e) for e in [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]]
    tri=[Eg(e) for e in [(0,1),(1,2),(2,0)]]
    print('fig8 hub',q,kappa(bow,q),kappa(tri,q)**2)
# substitution / product law on K4: D=(P1,P2), D3=(P1,03,12)
def inter(A,B):
    H=nx.Graph(); H.add_nodes_from(set(A)&set(B)); H.add_edges_from(e for e in A.edges() if B.has_edge(*e)); return H
P1=Eg((0,1),(1,3),(3,2),(2,0)); P2=Eg((0,3),(3,1),(1,2),(2,0))
D=[P1,P2]; D3=[P1,Eg((0,3)),Eg((1,2))]
def prod(D,Dp): return [inter(a,b) for a in D for b in Dp if inter(a,b).number_of_nodes()>0]
def restr(P,Dp): return [inter(P,b) for b in Dp if inter(P,b).number_of_nodes()>0]
for q in (4,5):
    lhs=kappa(prod(D,D3),q); rhs=kappa(D,q)
    for Pk in D: rhs*=kappa(restr(Pk,D3),q)
    rhs2=kappa(D3,q)
    for Pk in D3: rhs2*=kappa(restr(Pk,D),q)
    print('product law q=',q,lhs,rhs,rhs2)
