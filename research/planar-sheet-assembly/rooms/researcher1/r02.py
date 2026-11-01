# R02 researcher1: 통합 판정 정리(엇갈림 그래프 I, Z2 행렬 Q=A+diag(w1)) 와 n=2 띠 판정의 단계 확인용.
# 분해 설정: 조각 = (변 목록, 경계 사이클 정점 목록), 정점 이름은 전역.
import networkx as nx, itertools as it, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ribbon import UF

def cyc_edges(c): return [frozenset(e) for e in zip(c, c[1:]+c[:1])]

def rank2(M):
    M=[row[:] for row in M]; r=0; n=len(M[0]) if M else 0
    for c in range(n):
        p=next((i for i in range(r,len(M)) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(len(M)):
            if i!=r and M[i][c]: M[i]=[x^y for x,y in zip(M[i],M[r])]
        r+=1
    return r

def analyze(pieces, name=""):
    """pieces: list of (edges, cycle). returns dict."""
    n=len(pieces); G=nx.Graph(); K=nx.Graph()
    for E,C in pieces: G.add_edges_from(E); K.add_edges_from(zip(C,C[1:]+C[:1]))
    ce=[set(cyc_edges(C)) for _,C in pieces]
    # arcs
    arcs=[]  # (i,j,pathlist,eps)
    for i,j in it.combinations(range(n),2):
        I=nx.Graph(); I.add_edges_from(tuple(x) for x in ce[i]&ce[j])
        for comp in nx.connected_components(I):
            S=I.subgraph(comp); ends=[v for v in S if S.degree(v)==1]
            assert len(ends)==2, "shared part not a path"
            p=nx.shortest_path(S,*ends)
            def dirn(C,a,b):
                k=C.index(a); return 1 if C[(k+1)%len(C)]==b else -1
            Ci,Cj=pieces[i][1],pieces[j][1]
            eps=1 if dirn(Ci,p[0],p[1])!=dirn(Cj,p[0],p[1]) else -1
            arcs.append((i,j,p,eps))
    m=len(arcs)
    # boundary
    cnt={}
    for k in range(n):
        for x in ce[k]: cnt.setdefault(x,[]).append(k)
    assert all(len(v)<=2 for v in cnt.values())
    bd=nx.Graph(); owner={}
    for x,v in cnt.items():
        if len(v)==1: bd.add_edge(*tuple(x)); owner[x]=v[0]
    comps=list(nx.connected_components(bd)); b=len(comps)
    hol_orient=None
    # orientability via 2-coloring of pieces with eps
    T=nx.Graph(); T.add_nodes_from(range(n))
    sign={0:1}; ok=True
    adj={k:[] for k in range(n)}
    for (i,j,p,e) in arcs: adj[i].append((j,e)); adj[j].append((i,e))
    stack=[0]
    while stack:
        u=stack.pop()
        for v,e in adj[u]:
            want=sign[u]*e
            if v not in sign: sign[v]=want; stack.append(v)
            elif sign[v]!=want: ok=False
    res=dict(name=name,n=n,m=m,chi=n-m,b=b,orientable=ok,
             Gplanar=nx.check_planarity(G)[0],Kplanar=nx.check_planarity(K)[0],G=G,K=K,arcs=arcs)
    if b!=1 or not all(d==2 for _,d in bd.degree()):
        return res
    W=[u for u,_ in nx.find_cycle(bd)]; L=len(W)
    # events: for each W-vertex, arcs ending there, ordered by tie-break
    endmap={}
    for a,(i,j,p,e) in enumerate(arcs):
        for v in (p[0],p[-1]): endmap.setdefault(v,[]).append(a)
    tokens=[]  # sequence: ('E',piece) / ('A',arc)
    for t in range(L):
        v=W[t]; inc=owner[frozenset((W[t-1],v))]
        evs=endmap.get(v,[])
        ordered=[]; cur=inc; evs=list(evs)
        while evs:
            nxt=[a for a in evs if cur in arcs[a][:2]]
            assert len(nxt)==1, ("tie-break fail",v)
            a=nxt[0]; ordered.append(a); evs.remove(a)
            cur=arcs[a][1] if arcs[a][0]==cur else arcs[a][0]
        out=owner[frozenset((v,W[(t+1)%L]))]
        assert cur==out, "piece tracking inconsistent"
        tokens+= [('A',a) for a in ordered]+[('E',out)]
    pos={}; before={}; cur=tokens[-1][1]
    for idx,(ty,x) in enumerate(tokens):
        if ty=='A':
            pos.setdefault(x,[]).append(idx); before.setdefault(x,[]).append(cur)
            i,j=arcs[x][:2]; cur=j if cur==i else i
        else: cur=x
    vpos={}  # vertex-level positions for strict interlacement
    for a,(i,j,p,e) in enumerate(arcs): vpos[a]=(W.index(p[0]),W.index(p[-1]))
    def inter(P,Qp):
        p1,p2=sorted(P); return (p1<Qp[0]<p2)!=(p1<Qp[1]<p2)
    I=nx.Graph(); I.add_nodes_from(range(m)); A=[[0]*m for _ in range(m)]
    for a,c in it.combinations(range(m),2):
        if len(set(vpos[a])|set(vpos[c]))==4 and inter(vpos[a],vpos[c]): I.add_edge(a,c)
        if inter(pos[a],pos[c]): A[a][c]=A[c][a]=1
    D=[]
    for a in range(m):
        p1,p2=pos[a]; h=1
        for idx in range(p1+1,p2):
            if tokens[idx][0]=='A': h*=arcs[tokens[idx][1]][3]
        s0=before[a][0]; i,j=arcs[a][:2]; s0=j if s0==i else i
        s1=before[a][1]
        if s0!=s1: h*=arcs[a][3]
        D.append(0 if h==1 else 1)
    Q=[[A[r][c] if r!=c else D[r] for c in range(m)] for r in range(m)]
    res.update(W=W,I=I,A=A,D=D,rankQ=rank2(Q),rankA=rank2(A),Ibip=nx.is_bipartite(I),
               b1=m-n+1, pinch=any(len(v)>1 for v in endmap.values()))
    return res

def show(r):
    s=f"{r['name']}: n={r['n']} m={r['m']} chi={r['chi']} b={r['b']} orient={r['orientable']} Gplanar={r['Gplanar']} Kplanar={r['Kplanar']}"
    if 'I' in r:
        s+=f" | I bip={r['Ibip']} (I edges {r['I'].number_of_edges()}) pinch={r['pinch']} rankQ={r['rankQ']} b1=m-n+1={r['b1']} rankA={r['rankA']} diag={r['D']}"
    print(s)

def from_polygons(lengths, glues):
    """ribbon.py 규약의 다각형 접착을 분해 설정 조각으로."""
    uf=UF()
    for k,Lk in enumerate(lengths):
        for i in range(Lk): uf.f((k,i))
    for k,i,j,mm,s in glues:
        Lk,Lj=lengths[k],lengths[j]; a,b_=(k,i),(k,(i+1)%Lk); c,d=(j,mm),(j,(mm+1)%Lj)
        if s==1: uf.u(a,d); uf.u(b_,c)
        else: uf.u(a,c); uf.u(b_,d)
    names={}
    def nm(x):
        r=uf.f(x); return names.setdefault(r,len(names))
    out=[]
    for k,Lk in enumerate(lengths):
        C=[nm((k,i)) for i in range(Lk)]; out.append((list(zip(C,C[1:]+C[:1])),C))
    return out

def strip(k,tw):  # 정사각형 k 개 띠
    gl=[(t,2,(t+1)%k,0,1) for t in range(k-1)]+[(k-1,2,0,0,tw)]
    return from_polygons([4]*k,gl)

if __name__=="__main__":
    print("=== 정리 U / 정리 R 단계 확인 ===")
    for k in [2,3,4]: show(analyze(strip(k,-1),f"Mobius strip k={k}"))
    # r3 의 K5 = 삼각형 {i,i+1,i+2} 5개 (핀치 띠)
    tri=[[i%5,(i+1)%5,(i+2)%5] for i in range(5)]
    show(analyze([(list(zip(C,C[1:]+C[:1])),C) for C in tri],"K5 triangles (r3)"))
    # 핀치 1개 k=3 띠: 정사각형 2 + 삼각형 1 (삼각형의 두 호가 끝점 공유)
    # 조각: 0=sq,1=sq,2=tri; tri 변 0,1 이 호
    gl=[(0,2,1,0,1),(1,2,2,0,1),(2,1,0,0,-1)]
    show(analyze(from_polygons([4,4,3],gl),"pinched k=3 strip"))
    # 엇갈림 토러스 (R01 §5)
    L=[8,4,4,4,4]
    gl=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,4,1),(0,2,3,0,1),(3,2,4,0,1),(4,2,0,6,1)]
    show(analyze(from_polygons(L,gl),"interlaced torus (R01)"))
    gl2=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,2,1),(0,4,3,0,1),(3,2,4,0,1),(4,2,0,6,1)]
    show(analyze(from_polygons(L,gl2),"non-interlaced (R01)"))
    # 비가향 종수 2: 꼬인 손잡이 두 개 (엇갈림 / 비엇갈림)
    gl3=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,4,-1),(0,2,3,0,1),(3,2,4,0,1),(4,2,0,6,-1)]
    show(analyze(from_polygons(L,gl3),"two twisted, interlaced"))
    gl4=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,2,-1),(0,4,3,0,1),(3,2,4,0,1),(4,2,0,6,-1)]
    show(analyze(from_polygons(L,gl4),"two twisted, not interlaced"))
    # 한 손잡이 꼬임 + 한 손잡이 곧음, 엇갈림
    gl5=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,4,-1),(0,2,3,0,1),(3,2,4,0,1),(4,2,0,6,1)]
    show(analyze(from_polygons(L,gl5),"twisted+straight, interlaced"))
