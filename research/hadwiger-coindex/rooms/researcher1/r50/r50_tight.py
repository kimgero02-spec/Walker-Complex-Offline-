# R50: 경계 색수 정리의 극값 예 확인 (결정적 예 몇 개만)
import itertools, networkx as nx
from pysat.solvers import Glucose4

def colorable(G, q, restrict=None):
    """restrict: dict v -> allowed color set"""
    nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}
    var=lambda v,c: idx[v]*q+c+1
    s=Glucose4()
    for v in nodes:
        allowed=[c for c in range(q) if restrict is None or v not in restrict or c in restrict[v]]
        if not allowed: return False
        s.add_clause([var(v,c) for c in allowed])
        for c in range(q):
            if c not in allowed: s.add_clause([-var(v,c)])
    for u,v in G.edges():
        for c in range(q): s.add_clause([-var(u,c),-var(v,c)])
    r=s.solve(); s.delete(); return r

def chi(G):
    q=1
    while not colorable(G,q): q+=1
    return q

def s_val(B,W):  # min #colors on W over 4-colorings of B
    for t in range(1,5):
        if colorable(B,4,{w:set(range(t)) for w in W}): return t

def report(name,B1,B2,H):
    G=nx.union(B1,B2); G.add_edges_from(H)
    W1={u for u,v in H}; W2={v for u,v in H}
    p1=nx.check_planarity(B1)[0]; p2=nx.check_planarity(B2)[0]
    a1=chi(B1.subgraph(W1)); a2=chi(B2.subgraph(W2))
    d1=max(sum(1 for e in H if e[0]==x) for x in W1); d2=max(sum(1 for e in H if e[1]==y) for y in W2)
    print(f"{name}: n={G.number_of_nodes()} planar=({p1},{p2}) a=({a1},{a2}) s=({s_val(B1,W1)},{s_val(B2,W2)}) d=({d1},{d2}) chi={chi(G)} bound4+min(a)={4+min(a1,a2)}")
    return G

def K(n,pre): 
    return nx.relabel_nodes(nx.complete_graph(n),{i:f"{pre}{i}" for i in range(n)})

def gamma(a,pre):  # K4 r0..r3, each r_i joined to private K_a
    B=K(4,pre+"r"); W=[]
    for i in range(4):
        T=[f"{pre}t{i}_{j}" for j in range(a)]
        B.add_edges_from(itertools.combinations(T,2)); B.add_edges_from((f"{pre}r{i}",t) for t in T)
        if a==1: B.add_node(T[0])
        W+=T
    return B,W

def gamma2p(pre):  # K4, each K4 edge r_i r_j gets a W-edge u v with u,v ~ r_i,r_j
    B=K(4,pre+"r"); W=[]
    for i,j in itertools.combinations(range(4),2):
        u,v=f"{pre}u{i}{j}",f"{pre}v{i}{j}"
        B.add_edges_from([(u,v),(u,f"{pre}r{i}"),(u,f"{pre}r{j}"),(v,f"{pre}r{i}"),(v,f"{pre}r{j}")]); W+=[u,v]
    return B,W

def gamma1(pre):  # 8-vertex Apollonian, W = {x,y,z,t} rainbow independent
    B=K(4,pre); m=lambda s:f"{pre}{s}"
    for name,face in [("x",(0,1,2)),("y",(0,1,3)),("z",(0,2,3)),("t",(1,2,3))]:
        B.add_edges_from((m(name),m(str(f))) for f in face)
    return B,[m("x"),m("y"),m("z"),m("t")]

def join(B1,W1,B2,W2): return [(u,v) for u in W1 for v in W2]

B1,W1=gamma1("A"); B2=K(1,"k")
report("(1,1) Gamma1+K1",B1,B2,join(B1,W1,B2,list(B2)))
B1,W1=gamma2p("A"); B2=K(2,"k")
report("(2,2) Gamma2'+K2",B1,B2,join(B1,W1,B2,list(B2)))
B1,W1=gamma(2,"A"); B2,W2=gamma(2,"B")
report("(2,2) Gamma2+Gamma2",B1,B2,join(B1,W1,B2,W2))
B1,W1=gamma(2,"A"); B2=K(3,"k")
report("(2,3) Gamma2+K3",B1,B2,join(B1,W1,B2,list(B2)))
B1,W1=gamma(3,"A"); B2=K(3,"k")
G=report("(3,3) Gamma3+K3",B1,B2,join(B1,W1,B2,list(B2)))
report("(4,3) K4+K3=K7",K(4,"A"),K(3,"k"),[(f"A{i}",f"k{j}") for i in range(4) for j in range(3)])
# Gamma2' 의 프로필: W 가 정확히 t 색 (색 0..t-1 로 한정) 일 때 최소 총 색수
B,W=gamma2p("P")
for t in (2,3):
    q=4
    while not colorable(B,q,{w:set(range(t)) for w in W}): q+=1
    print("Gamma2' beta(",t,")<=?: min total colors with W in [t] =",q)
# K7 minor 확인 (Gamma3+K3): 각 T_i 를 r_i 로 축약
H=G.copy()
for i in range(4):
    for j in range(3): H=nx.contracted_nodes(H,f"Ar{i}",f"At{i}_{j}",self_loops=False)
print("contracted graph complete K7?", H.number_of_nodes(), H.number_of_edges())
