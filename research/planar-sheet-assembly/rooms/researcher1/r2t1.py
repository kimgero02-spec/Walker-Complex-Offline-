# R2-T1 researcher1: 접합 그래프 A 와 접합 부풀림 A^(t) 의 결정적 예 확인 (탐색 없음)
import networkx as nx
from math import factorial

def ncolorings(G, q, stop_at_one=False):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    # 연결 순서로 정렬해 가지치기 개선
    order=[]; seen=set()
    for s in nodes:
        if s in seen: continue
        for v in nx.bfs_tree(G, s):
            if v not in seen: seen.add(v); order.append(v)
    col = {}
    def bt(i):
        if i == len(order): return 1
        v = order[i]; tot = 0
        for c in range(q):
            if all(col.get(u) != c for u in G[v]):
                col[v] = c
                tot += bt(i+1)
                del col[v]
                if stop_at_one and tot: return tot
        return tot
    return bt(0)

def colorable(G, q):
    """DSATUR 순서의 정확한 백트래킹 (존재 판정)."""
    adj={v:set(G[v]) for v in G}; col={}
    def pick():
        best=None;key=None
        for v in adj:
            if v in col: continue
            k=(len({col[u] for u in adj[v] if u in col}), len(adj[v]))
            if key is None or k>key: best,key=v,k
        return best
    def bt():
        v=pick()
        if v is None: return True
        used={col[u] for u in adj[v] if u in col}
        mx=max(col.values(),default=-1)
        for c in range(min(q,mx+2)):   # 색 대칭 깨기
            if c in used: continue
            col[v]=c
            if bt(): return True
            del col[v]
        return False
    return bt()

def chi(G, qmax=9, lo=1):
    if G.number_of_edges()==0: return 1
    for q in range(max(lo,1), qmax+1):
        if colorable(G, q): return q
    return None

class Manual:
    """사상 없는 설명서: 조각들(서로소)과 식별 간선 E_J."""
    def __init__(self):
        self.P = nx.Graph(); self.EJ = []
    def piece(self, tag, edges, nodes=()):
        for a,b in edges: self.P.add_edge((tag,a),(tag,b))
        for a in nodes: self.P.add_node((tag,a))
    def ident(self, x, y): self.EJ.append((x,y))
    def classes(self):
        J = nx.Graph(); J.add_nodes_from(self.P.nodes()); J.add_edges_from(self.EJ)
        return [c for c in nx.connected_components(J) if len(c) >= 2]
    def quotient(self):
        rep = {}
        J = nx.Graph(); J.add_nodes_from(self.P.nodes()); J.add_edges_from(self.EJ)
        for i,c in enumerate(nx.connected_components(J)):
            for v in c: rep[v] = i
        G = nx.Graph(); G.add_nodes_from(set(rep.values()))
        loop=False
        for a,b in self.P.edges():
            if rep[a]==rep[b]: loop=True
            G.add_edge(rep[a],rep[b])
        return G, loop
    def A(self, t):
        """접합 부풀림 A^(t): 조각 + 류마다 K_t (류의 모든 포트에 잇는다). t=1 이면 접합 그래프 A."""
        X = self.P.copy()
        for i,c in enumerate(self.classes()):
            K = [('J',i,j) for j in range(t)]
            for a in range(t):
                for b in range(a+1,t): X.add_edge(K[a],K[b])
                for x in c: X.add_edge(K[a], x)
        return X

def report(name, M, tmax=4, poly_q=()):
    G, loop = M.quotient()
    cg = None if loop else chi(G)
    seq = [chi(M.A(t), lo=(t+1 if M.classes() else 1)) for t in range(0, tmax+1)]
    thr = next((t+1 for t,c in enumerate(seq) if c == t+1), None)
    print(f"[{name}] |V(G)|={G.number_of_nodes()} |E(G)|={G.number_of_edges()} 평면={nx.check_planarity(G)[0]} "
          f"chi(G)={cg} | chi(A^(t)), t=0..{tmax}: {seq} | 문턱 1+min t = {thr} | 일치={thr==cg}")
    nJ = len(M.classes())
    for q in poly_q:
        lhs = ncolorings(G, q)
        rhs = ncolorings(M.A(q-1), q)
        print(f"    다항식 항등식 q={q}: P(G,q)={lhs},  P(A^(q-1),q)/((q-1)!)^|J| = {rhs}/{factorial(q-1)**nJ} = {rhs/factorial(q-1)**nJ}")
    return seq

# 예 1: K4 = (K4 - uv) ∪ K2   (T1 예 1, K2 조각)
M = Manual()
M.piece(1, [('u','a'),('u','b'),('v','a'),('v','b'),('a','b')])
M.piece(2, [('u','v')])
M.ident((1,'u'),(2,'u')); M.ident((1,'v'),(2,'v'))
s1 = report("예1 K4=(K4-uv)+K2", M, poly_q=(3,4))
# 대조: K4-uv 한 조각 (설명서 없음)
M0 = Manual(); M0.piece(1, [('u','a'),('u','b'),('v','a'),('v','b'),('a','b')])
s0 = report("대조 K4-uv 한 조각", M0)
print("    t=1 에서 chi(A) 가 같은가:", s1[1], s0[1])

# 예 2: N4-2 다이아몬드 둘, 골격 K3, 포트 대응만 다름
def diamond_manual(perm):
    M = Manual()
    for tag in 'AB':
        M.piece(tag, [('t0','t1'),('t0','t2'),('t1','t2'),('s','t1'),('s','t2')])
    pA = [('A','t0'),('A','s'),('A','t1')]; pB = [('B','t1'),('B','t0'),('B','s')]
    for i in range(3): M.ident(pA[i], pB[perm[i]])
    return M
M1 = diamond_manual((0,1,2)); M2 = diamond_manual((1,2,0))
report("예2a N4-2 설명서1", M1, poly_q=(3,4))
report("예2b N4-2 설명서2", M2, poly_q=(3,4))
for t in (1,2):
    print(f"    A^({t}) 동형?", nx.is_isomorphic(M1.A(t), M2.A(t)))

# 예 3: 정사각형 3개 띠: 프리즘(곧게) 대 K33 = M6 (꼬아서)
def band(k, twist):
    M = Manual()
    for i in range(k):
        M.piece(i, [('a','b'),('b','c'),('c','d'),('d','a')])  # 가로대 a-b (왼), d-c (오)
    for i in range(k):
        j = (i+1) % k
        if twist and i == k-1:
            M.ident((i,'d'),(j,'b')); M.ident((i,'c'),(j,'a'))
        else:
            M.ident((i,'d'),(j,'a')); M.ident((i,'c'),(j,'b'))
    return M
report("예3a 프리즘 C3xK2", band(3,False), tmax=3, poly_q=(2,3))
report("예3b K33 = 뫼비우스 M6", band(3,True), tmax=3, poly_q=(2,3))
G,_ = band(3,True).quotient(); print("    K33 동형:", nx.is_isomorphic(G, nx.complete_bipartite_graph(3,3)))

# 예 4: K5 = C5 ∪ 오각별 (같은 정점 5개 모두 식별)
M = Manual()
M.piece('C', [(i,(i+1)%5) for i in range(5)])
M.piece('S', [(i,(i+2)%5) for i in range(5)])
for i in range(5): M.ident(('C',i),('S',i))
report("예4 K5 = C5 ∪ C5'", M, tmax=4)

# 예 5: T1 예 2 (굵은 데이터 같고 chi 다름)
def t1ex2(which):
    M = Manual()
    M.piece(1, [('u','a'),('u','b'),('v','a'),('v','b'),('a','b')])
    if which=='A':
        M.piece(2, [('u','a'),('u','b'),('a','b'),('a','w'),('b','w'),('w','v')])
    else:
        M.piece(2, [('u','a'),('u','b'),('a','b'),('a','v'),('b','v'),('v','z')])
    M.ident((1,'u'),(2,'u')); M.ident((1,'v'),(2,'v'))
    return M
report("예5a T1 예2 A", t1ex2('A'))
report("예5b T1 예2 B", t1ex2('B'))

# 예 6: (W) 위반, 고리: 조각 안 인접 두 점이 같은 류
M = Manual(); M.piece(1,[('x','y'),('y','z')]); M.piece(2,[('p','q')])
M.ident((1,'x'),(2,'p')); M.ident((2,'p'),(1,'y'))
G,loop = M.quotient(); print("[예6 고리] loop=",loop," chi(A^(t)) t=0..4:", [chi(M.A(t)) for t in range(4)], "(문턱 없음 = chi 무한 기대)")

# 예 7: 정리 I 의 가제트 Q_pi (q=3, 평면) : Pi_3(Q_pi, J) = {pi}, 두 조각 설명서 Q_pi ∪_J Q_pi' 로 구별
from itertools import product
def gadget(pi):  # pi: 포트 -> 블록 번호 (0..2)
    M_edges=[('z0','z1'),('z1','z2'),('z0','z2')]
    for x,b in pi.items():
        for j in range(3):
            if j!=b: M_edges.append((x,'z%d'%j))
    return M_edges
def profile3(edges, ports):
    Gp=nx.Graph(edges); out=set()
    # 3-색칠을 모두 세지 않고, 각 분할마다 실현 여부만 판정: 포트 색을 고정해 colorable 확인
    for cols in product(range(3), repeat=len(ports)):
        H=Gp.copy()
        # 포트 색 고정: 색 노드 3개 삼각형을 추가하고 포트를 다른 두 색 노드에 잇는다
        H.add_edges_from([('C0','C1'),('C1','C2'),('C0','C2')])
        for x,c in zip(ports,cols):
            for j in range(3):
                if j!=c: H.add_edge(x,'C%d'%j)
        if colorable(H,3):
            # 분할 (정규화)
            m={}; key=tuple(m.setdefault(c,len(m)) for c in cols); out.add(key)
    return out
ports=['x1','x2','x3','x4']
pis=[{'x1':0,'x2':0,'x3':1,'x4':2},{'x1':0,'x2':1,'x3':0,'x4':2},{'x1':0,'x2':1,'x3':1,'x4':1}]
for pi in pis:
    E=gadget(pi); print("[예7] pi=",pi," 평면=",nx.check_planarity(nx.Graph(E))[0]," Pi_3=",profile3(E,ports))
def two(pi1,pi2):
    M=Manual(); M.piece('L',gadget(pi1)); M.piece('R',gadget(pi2))
    for x in ports: M.ident(('L',x),('R',x))
    G,_=M.quotient(); return chi(G), nx.check_planarity(G)[0]
print("    Q_pi1 ∪ Q_pi1:",two(pis[0],pis[0]),"  Q_pi1 ∪ Q_pi2:",two(pis[0],pis[1]))

# 예 8: 후보 C 의 분할 합 공식 P(G,q) = sum_sigma (q)_{|sigma|} prod_k P((P_k)_{sigma|J_k},q)/(q)_{|sigma|J_k|}
def set_partitions(items):
    if not items: yield []; return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first]+p[i]] + p[i+1:]
        yield [[first]] + p
def falling(q,n):
    r=1
    for i in range(n): r*=q-i
    return r
def derived(Pk, blocks):
    """(P_k)_pi: 블록마다 한 점으로 합치고, 블록끼리 클릭 간선."""
    rep={}
    for i,b in enumerate(blocks):
        for x in b: rep[x]=('B',i)
    H=nx.Graph(); loop=False
    for v in Pk.nodes(): H.add_node(rep.get(v,v))
    for a,b in Pk.edges():
        ra,rb=rep.get(a,a),rep.get(b,b)
        if ra==rb: loop=True
        H.add_edge(ra,rb)
    for i in range(len(blocks)):
        for j in range(i+1,len(blocks)): H.add_edge(('B',i),('B',j))
    return H, loop
def poly_by_pieces(M, q):
    cls=M.classes(); cid={}
    for i,c in enumerate(cls):
        for x in c: cid[x]=i
    pieces=[M.P.subgraph(c).copy() for c in nx.connected_components(M.P)]
    total=0
    for sigma in set_partitions(list(range(len(cls)))):
        bl={i:j for j,b in enumerate(sigma) for i in b}
        term=falling(q,len(sigma))
        for Pk in pieces:
            ports=[x for x in Pk.nodes() if x in cid]
            blocks={}
            for x in ports: blocks.setdefault(bl[cid[x]],[]).append(x)
            blocks=list(blocks.values())
            H,loop=derived(Pk,blocks)
            if loop or len(blocks)>q: term=0; break
            term*= ncolorings(H,q)/falling(q,len(blocks))
        total+=term
    return total
for name,MM in [("N4-2 설명서1",M1),("N4-2 설명서2",M2),("프리즘",band(3,False)),("K33",band(3,True))]:
    G,_=MM.quotient()
    print("[예8]",name,[(q, ncolorings(G,q), poly_by_pieces(MM,q)) for q in (2,3,4)])

# 예 9: 라운드 1 명제 4b 쌍 (K33-xy + K2 대 프리즘-가로대 + K2) 에서 접합 그래프 A 의 평면성
def t1ex4(which):
    M=Manual()
    if which=='K33':
        E=[(a,b) for a in 'abc' for b in 'def' if (a,b)!=('a','d')]; x,y='a','d'
    else:
        E=[('a','b'),('b','c'),('c','a'),('d','e'),('e','f'),('f','d'),('b','e'),('c','f')]; x,y='a','d'
    M.piece(1,E); M.piece(2,[('x','y')])
    M.ident((1,x),(2,'x')); M.ident((1,y),(2,'y'))
    return M
for w in ('K33','prism'):
    MM=t1ex4(w); G,_=MM.quotient()
    print("[예9]",w,"P1 평면",nx.check_planarity(MM.P.subgraph([v for v in MM.P if v[0]==1]))[0],"G 평면",nx.check_planarity(G)[0],"A 평면",nx.check_planarity(MM.A(1))[0])
