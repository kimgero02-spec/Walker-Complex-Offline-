# R2-T2 researcher2: attacks on Theorem A / Theorem I (R2-T1-researcher1)
import networkx as nx, itertools, sys
sys.setrecursionlimit(10000)

def colorable(G, q):
    """exact q-colorability, backtracking with DSATUR-like ordering"""
    nodes = list(G.nodes())
    if q <= 0: return len(nodes) == 0
    adj = {v: set(G[v]) for v in nodes}
    for v in nodes:
        if v in adj[v]: return False
    col = {}
    def pick():
        best=None; bk=None
        for v in nodes:
            if v in col: continue
            sat = len({col[u] for u in adj[v] if u in col})
            key=(sat, len(adj[v]))
            if bk is None or key>bk: bk=key; best=v
        return best
    def rec(used):
        v = pick()
        if v is None: return True
        forb = {col[u] for u in adj[v] if u in col}
        for c in range(min(q, used+1)):
            if c in forb: continue
            col[v]=c
            if rec(max(used, c+1)): return True
            del col[v]
        return False
    return rec(0)

def chi(G, cap=12):
    for q in range(0, cap+1):
        if colorable(G, q): return q
    return None

def count_col(G, q):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    # order by BFS for pruning
    order=[]; seen=set()
    for s in nodes:
        if s in seen: continue
        for v in nx.bfs_tree(G, s): 
            if v not in seen: seen.add(v); order.append(v)
    adj={v:set(G[v]) for v in G}
    col={}
    def rec(i):
        if i==len(order): return 1
        v=order[i]; forb={col[u] for u in adj[v] if u in col}; tot=0
        for c in range(q):
            if c not in forb:
                col[v]=c; tot+=rec(i+1); del col[v]
        return tot
    return rec(0)

def manual_A(pieces, classes, t):
    """pieces: list of graphs with node labels (k,v); classes: list of port lists. returns A^(t)"""
    A = nx.Graph()
    for P in pieces: A.add_nodes_from(P.nodes()); A.add_edges_from(P.edges())
    for i, cl in enumerate(classes):
        K = [('w', i, j) for j in range(t)]
        A.add_nodes_from(K)
        for a, b in itertools.combinations(K, 2): A.add_edge(a, b)
        for k in K:
            for x in cl: A.add_edge(k, x)
    return A

def glue(pieces, classes):
    G = nx.Graph()
    rep = {}
    for P in pieces:
        for v in P: rep[v]=v
    for cl in classes:
        for x in cl: rep[x]=cl[0]
    for P in pieces:
        G.add_nodes_from(rep[v] for v in P)
        for a,b in P.edges(): G.add_edge(rep[a], rep[b])
    return G

def stacked(base_steps):
    """Apollonian network: start K4 colors 0..3, stack into faces given by a rule; return graph, coloring"""
    T = nx.complete_graph(4); col={i:i for i in range(4)}
    faces=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
    return T, col, faces

def stack_into(T, col, faces, f):
    n = max(T.nodes())+1
    a,b,c = f
    T.add_edges_from([(n,a),(n,b),(n,c)])
    col[n] = ({0,1,2,3}-{col[a],col[b],col[c]}).pop()
    faces.remove(f); faces += [(n,b,c),(a,n,c),(a,b,n)]
    return n

print("=== Part 1: d(1)=3 with planar pieces (no (W)) ===")
T,col,faces = stacked(None)
# stack into each of the 4 faces of K4 once -> vertices 4..7 colors opposite
for f in list(faces): stack_into(T,col,faces,f)
assert nx.check_planarity(T)[0]
n4 = count_col(T,4); print("T: n=%d m=%d planar, #4-colorings=%d (24 => unique up to perm)"%(T.number_of_nodes(),T.number_of_edges(),n4))
# rainbow independent 4-set
best=None
for S in itertools.combinations(T.nodes(),4):
    if len({col[v] for v in S})==4 and all(not T.has_edge(a,b) for a,b in itertools.combinations(S,2)):
        best=S; break
print("rainbow independent set:", best, [col[v] for v in best])
P = nx.relabel_nodes(T, {v:(0,v) for v in T})
cls=[[ (0,v) for v in best]]
G = glue([P], cls)
print("G: n=%d chi(G)=%d"%(G.number_of_nodes(), chi(G)))
seq=[chi(manual_A([P],cls,t)) for t in range(0,6)]
print("chi(A^(t)) t=0..5:", seq, " d(t):", [seq[t]-(t+1) for t in range(6)])

print("=== Part 1b: trivial counterexample to 'd(t)<=1 for t>=1': K4 piece + K1 ===")
P1 = nx.relabel_nodes(nx.complete_graph(4), {v:(1,v) for v in range(4)}); P2=nx.Graph(); P2.add_node((2,0))
cls=[[(1,0),(2,0)]]
seq=[chi(manual_A([P1,P2],cls,t)) for t in range(0,6)]
print("chi(A^(t)):", seq, "d:", [seq[t]-(t+1) for t in range(6)], "chi(G)=", chi(glue([P1,P2],cls)))

print("=== Part 1c: (W)-version, 4 copies of uniquely 4-colorable T, 64 classes ===")
# reduction (proved in report): chi(A)<=4 iff exists sigma2..4 in S4 with no rainbow tuple
S=[(0,a2,a3,a4) for a2 in range(4) for a3 in range(4) for a4 in range(4)]
perms=list(itertools.permutations(range(4)))
bad=0
for s2 in perms:
    for s3 in perms:
        for s4 in perms:
            if not any(len({0,s2[a],s3[b],s4[c]})==4 for (_,a,b,c) in S): bad+=1
print("sigma triples with no rainbow class (should be 0):", bad)
# greedy smaller S
alltup=list(itertools.product(range(4),repeat=3))
sig=[(s2,s3,s4) for s2 in perms for s3 in perms for s4 in perms]
unc=set(range(len(sig))); chosen=[]
cover={tp:{i for i,(s2,s3,s4) in enumerate(sig) if len({0,s2[tp[0]],s3[tp[1]],s4[tp[2]]})==4} for tp in alltup}
while unc:
    tp=max(alltup,key=lambda x:len(cover[x]&unc)); chosen.append(tp); unc-=cover[tp]
print("greedy S size:", len(chosen))
# concrete build with greedy S: need per copy enough vertices of each color
need=[{a:0 for a in range(4)} for _ in range(4)]
for tp in chosen:
    need[0][0]+=1
    for k in range(3): need[k+1][tp[k]]+=1
print("vertices needed per color per copy:", need)

print("=== Part 2: Theorem A polynomial identity, class hitting same piece twice ===")
C5=nx.relabel_nodes(nx.cycle_graph(5),{v:(0,v) for v in range(5)})
K2=nx.Graph(); K2.add_edge((1,0),(1,1))
cls=[[(0,0),(0,2),(1,0)]]   # identifies two nonadjacent vertices of C5 and an end of K2
G=glue([C5,K2],cls)
print("G edges:",sorted(G.edges()), "chi(G)=",chi(G))
import math
for q in range(1,5):
    A=manual_A([C5,K2],cls,q-1)
    lhs=count_col(A,q); rhs=math.factorial(q-1)**len(cls)*count_col(G,q)
    print(" q=%d  P(A^(q-1),q)=%d  ((q-1)!)^|J| P(G,q)=%d  %s"%(q,lhs,rhs,lhs==rhs))
print(" chi(A^(t)) t=0..4:", [chi(manual_A([C5,K2],cls,t)) for t in range(5)])

print("=== Part 3: s=3, every family of <=3-block partitions realized by a planar piece ===")
parts3 = {'123':[[0,1,2]], '12|3':[[0,1],[2]], '13|2':[[0,2],[1]], '23|1':[[1,2],[0]], '1|2|3':[[0],[1],[2]]}
def pkey(cs):
    # canonical partition of port colors
    m={}; out=[]
    for c in cs:
        if c not in m: m[c]=len(m)
        out.append(m[c])
    return tuple(out)
pname={ (0,0,0):'123',(0,0,1):'12|3',(0,1,0):'13|2',(0,1,1):'23|1',(0,1,2):'1|2|3'}
def Pi3(H, ports):
    res=set()
    for cs in itertools.product(range(3),repeat=3):
        if cs[0]!=0: continue
        if any(H.has_edge(ports[i],ports[j]) and cs[i]==cs[j] for i in range(3) for j in range(i+1,3)): continue
        H2=H.copy()
        # fix port colors via a triangle gadget
        H2.add_edges_from([('z0','z1'),('z1','z2'),('z0','z2')])
        for i,p in enumerate(ports):
            for j in range(3):
                if j!=cs[i]: H2.add_edge(p,'z%d'%j)
        if colorable(H2,3): res.add(pname[pkey(cs)])
    return frozenset(res)
def ports_on_face(H, ports):
    H2=H.copy(); H2.add_edges_from(('apex',p) for p in ports); return nx.check_planarity(H2)[0]
# explicit gadgets (found by hand, verified here)
gad={}
# forbid 123 (not-all-equal): triangle abc, x1-a,x2-b,x3-c
H=nx.Graph([('x1','a'),('x2','b'),('x3','c'),('a','b'),('b','c'),('a','c')]); gad['123']=H
# forbid 12|3 : x1,x2 equal & x3 different is forbidden
# search small gadgets for remaining
ports=['x1','x2','x3']
target={k: frozenset(parts3)-{k} for k in parts3}
found={'123':H} if Pi3(H,ports)==target['123'] else {}
def search(k_extra):
    extra=['e%d'%i for i in range(k_extra)]
    V=ports+extra
    pairs=[(a,b) for a,b in itertools.combinations(V,2)]
    for mask in range(1<<len(pairs)):
        E=[pairs[i] for i in range(len(pairs)) if mask>>i&1]
        H=nx.Graph(); H.add_nodes_from(V); H.add_edges_from(E)
        if not nx.check_planarity(H)[0]: continue
        if not ports_on_face(H,ports): continue
        pi=Pi3(H,ports)
        for k,tg in target.items():
            if k not in found and pi==tg: found[k]=H; print("  found gadget forbidding",k,"with",k_extra,"extra:",E)
        if len(found)==5: return
for ke in range(0,5):
    if len(found)==5: break
    search(ke)
print("co-singleton gadgets found:", sorted(found))
# glue: identify ports of several gadgets (ports on common face, s=3 -> planar)
def glue_gadgets(keys):
    H=nx.Graph(); H.add_nodes_from(ports)
    for i,k in enumerate(keys):
        g=found[k]
        H.add_edges_from(((a if a in ports else (i,a)),(b if b in ports else (i,b))) for a,b in g.edges())
    return H
ok=0
for r in range(0,6):
    for forb in itertools.combinations(sorted(parts3),r):
        if r==5:
            H=glue_gadgets(list(forb))
        else:
            H=glue_gadgets(list(forb))
        pi=Pi3(H,ports); exp=frozenset(parts3)-set(forb)
        pl=nx.check_planarity(H)[0] and ports_on_face(H,ports)
        ok+= (pi==exp and pl)
print("NAIVE gluing of several gadgets at the SAME 3 ports (fails for >=3 gadgets: K_{3,3} minor):", ok, "of 32  -> see r2t2_fam.py / r2t2_fam2.py for the correct realization")

print("=== Part 4: white/black label is essential (uncolored A loses chi) ===")
P=nx.relabel_nodes(nx.complete_graph(4),{v:(0,v) for v in range(4)}); P.remove_edge((0,0),(0,1))
E=nx.Graph(); E.add_edge((1,0),(1,1))
cls=[[(0,0),(1,0)],[(0,1),(1,1)]]
A=manual_A([P,E],cls,1); G=glue([P,E],cls)
print("manual 1: chi(G)=",chi(G)," A has n=%d"%A.number_of_nodes())
print("manual 2 = A itself as ONE piece, no classes: chi(G')=",chi(A), " planar(A)=",nx.check_planarity(A)[0])
print("=> same uncolored graph A, chi(G) 4 vs 3")

print("=== Part 5: finite family X cannot read chi: K_n from K_2 pieces ===")
for n in [4,5,6]:
    pcs=[]; ports={v:[] for v in range(n)}
    for i,(a,b) in enumerate(itertools.combinations(range(n),2)):
        g=nx.Graph(); g.add_edge((i,a),(i,b)); pcs.append(g); ports[a].append((i,a)); ports[b].append((i,b))
    cls=[ports[v] for v in range(n)]
    print(" n=%d chi(G)=%d  chi(A^(t)) t=0..2:"%(n,chi(glue(pcs,cls))),[chi(manual_A(pcs,cls,t)) for t in range(3)], "(bound max chi(P)+t = t+2)")
