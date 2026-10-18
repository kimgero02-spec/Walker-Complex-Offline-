from lib import *
import sympy as sp
# (1) W5-pendant counterexample to "clique-Hall" prediction: hub+C5, each with pendant triangle (W)
B=nx.wheel_graph(6); W=[]
for v in list(B):
    T=[f'{v}_{i}' for i in range(3)]; W+=T
    B.add_edges_from(itertools.combinations(T,2)); B.add_edges_from((v,u) for u in T)
print("W5-pendant planar",nx.check_planarity(B)[0])
print(" q=6, W in 3 colours:",colorable(B,6,allowed={w:{0,1,2} for w in W}) is not None,
      "| q=6 W in 4 colours:",colorable(B,6,allowed={w:{0,1,2,3} for w in W}) is not None)
# (2) decoupled product: boundary vertices in distinct components
x=None
def cp(G):
    global x; P,x=chrom_poly(G); return P
B1=nx.disjoint_union(nx.cycle_graph(3),nx.cycle_graph(4)); W1=[0,3]   # one vertex per component
B2=nx.disjoint_union(nx.complete_graph(4),nx.path_graph(3)); W2=[0,4]
G=nx.disjoint_union(B1,B2); n1=B1.number_of_nodes()
H=[(0,n1+0),(0,n1+4),(3,n1+0),(3,n1+4)]; G.add_edges_from(H)
Hg=nx.Graph(); Hg.add_nodes_from(['a','b','c','d']); Hg.add_edges_from([('a','c'),('a','d'),('b','c'),('b','d')])
lhs=cp(G); rhs=sp.factor(cp(B1)*cp(B2)*cp(Hg)/x**4)
print("decoupled product identity:",sp.simplify(lhs-rhs)==0)
# (3) two-point correlation on path of length l: Pr[same]-1/x  vs (x-1)/x*(-1/(x-1))^l
for l in range(1,6):
    Pp=nx.path_graph(l+1); Q=nx.contracted_nodes(Pp,0,l,self_loops=False) if l>1 else None
    tot=cp(Pp); same=cp(Q) if l>1 else 0
    corr=sp.simplify(same/tot-1/x); pred=sp.simplify((x-1)/x*(-1/(x-1))**l)
    print(" path l=",l,"corr ok:",sp.simplify(corr-pred)==0)
# (4) connected sheet: leading order of correlation for C6 opposite (dist 3, 2 geodesics), K_{2,3} poles (dist2, 3 geodesics)
for name,Gc,u,w in (("C6",nx.cycle_graph(6),0,3),("K23",nx.complete_bipartite_graph(2,3),0,1),("icosa",nx.icosahedral_graph(),0,[v for v in nx.icosahedral_graph() if nx.shortest_path_length(nx.icosahedral_graph(),0,v)==3][0])):
    tot=cp(Gc); same=cp(nx.contracted_nodes(Gc,u,w,self_loops=False))
    corr=sp.simplify(same/tot-1/x)
    y=sp.Symbol('y'); ser=sp.series(corr.subs(x,1/y),y,0,7).removeO()
    print(" ",name,"dist",nx.shortest_path_length(Gc,u,w),"#geodesics",len(list(nx.all_shortest_paths(Gc,u,w))),"corr series in 1/x:",sp.expand(ser))
# (5) ladder = two paths + matching
for n in (3,4,5):
    L=nx.ladder_graph(n); print(" ladder",n, sp.factor(cp(L)))
