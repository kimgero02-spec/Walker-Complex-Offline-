# 다각형 조각 + 단일 변 arc 를 부호 붙여 접착하는 설명서 조립기 (colimit = union-find)
import networkx as nx
class UF:
    def __init__(s): s.p={}
    def f(s,x):
        s.p.setdefault(x,x)
        while s.p[x]!=x: s.p[x]=s.p[s.p[x]]; x=s.p[x]
        return x
    def u(s,a,b): s.p[s.f(a)]=s.f(b)
def assemble(lengths, glues):
    """lengths[k]=boundary length of polygon piece k (vertices (k,0..L-1), edges (k,i)-(k,i+1)).
    glues: (k,i, j,m, sign): edge i of piece k [(k,i)->(k,i+1)] glued to edge m of piece j.
    sign=+1: orientation-compatible (k,i)~(j,m+1),(k,i+1)~(j,m);  sign=-1: (k,i)~(j,m),(k,i+1)~(j,m+1)."""
    uf=UF()
    for k,L in enumerate(lengths):
        for i in range(L): uf.f((k,i))
    for k,i,j,m,s in glues:
        Lk,Lj=lengths[k],lengths[j]
        a,b=(k,i),(k,(i+1)%Lk); c,d=(j,m),(j,(m+1)%Lj)
        if s==1: uf.u(a,d); uf.u(b,c)
        else: uf.u(a,c); uf.u(b,d)
    G=nx.MultiGraph(); loops=0
    for k,L in enumerate(lengths):
        for i in range(L):
            x,y=uf.f((k,i)),uf.f((k,(i+1)%L))
            if x==y: loops+=1
            G.add_edge(*sorted([x,y],key=str))
    S=nx.Graph(G)  # collapse parallels (glued edges become same edge)
    mult=sum(1 for u,v in S.edges() if G.number_of_edges(u,v)>2)
    return S,loops,mult
if __name__=="__main__":
    # figure-8 interlaced at central octagon P0: arcs at edges 0,2,4,6 in cyclic order a,b,a',b'
    # cycle1: P0(e0) - Q1 - Q2 - P0(e4) ; cycle2: P0(e2) - R1 - R2 - P0(e6); squares, arcs opposite edges 0 and 2
    L=[8,4,4,4,4]
    gl=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,4,1),(0,2,3,0,1),(3,2,4,0,1),(4,2,0,6,1)]
    G,lo,mu=assemble(L,gl)
    print("interlaced torus manual: n",G.number_of_nodes(),"m",G.number_of_edges(),"loops",lo,"planar?",nx.check_planarity(G)[0])
    # non-interlaced (order a,a',b,b') -> planar ribbon (two annuli joined) expected planar
    gl2=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,2,1),(0,4,3,0,1),(3,2,4,0,1),(4,2,0,6,1)]
    G2,lo,mu=assemble(L,gl2)
    print("non-interlaced manual: planar?",nx.check_planarity(G2)[0])
    # prism / mobius n=3,4 squares
    for n in [2,3,4]:
        for tw in [1,-1]:
            gl=[(k,2,(k+1)%n,0,1) for k in range(n-1)]+[(n-1,2,0,0,tw)]
            G,lo,mu=assemble([4]*n,gl)
            print("band n",n,"hol",tw,"V,E",G.number_of_nodes(),G.number_of_edges(),"planar?",nx.check_planarity(G)[0])
