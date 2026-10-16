# R02: 추측 10 수정판 공격. 조각 = (그래프 변 목록, 경계 사이클 C), 공유 호는 같은 정점 이름으로.
import networkx as nx
from collections import defaultdict, Counter
def cyc_edges(C): return [(C[i],C[(i+1)%len(C)]) for i in range(len(C))]
def analyze(name, pieces, arcs):
    # pieces: dict k -> (extra_edges, C);  arcs: list of (k,j,pathlist)
    G=nx.MultiGraph(); P={}
    for k,(ex,C) in pieces.items():
        g=nx.Graph(cyc_edges(C)+ex); P[k]=g
    # colimit: 공유 변은 호 위의 변뿐. 나머지 같은 이름 변은 중복(다중변)으로 처리
    shared=set()
    for (k,j,path) in arcs:
        for e in zip(path,path[1:]): shared.add(frozenset(e))
    for k,g in P.items():
        for e in g.edges():
            if frozenset(e) in shared: continue
            G.add_edge(*e,key=(k,frozenset(e)))
    for e in shared: G.add_edge(*tuple(e),key=('sh',e))
    Gs=nx.Graph(G)
    multi = G.number_of_edges()!=Gs.number_of_edges()
    # 정점은 조각 2개 이하
    cnt=Counter(v for g in P.values() for v in g.nodes())
    print(f"== {name}: |V|={Gs.number_of_nodes()} |E|={G.number_of_edges()} 다중변={multi} 최대 조각중복={max(cnt.values())}")
    print("  G 평면:", nx.check_planarity(Gs)[0])
    # 호 서로소 (조각마다)
    for k in P:
        my=[set(p) for (a,b,p) in arcs if k in (a,b)]
        dis=all(not (my[i]&my[j]) for i in range(len(my)) for j in range(i+1,len(my)))
        g=P[k]; C=pieces[k][1]
        ind = all(not g.has_edge(C[i],C[j]) for i in range(len(C)) for j in range(i+2,len(C)) if not (i==0 and j==len(C)-1))
        rest=g.subgraph(set(g)-set(C)); nonsep = rest.number_of_nodes()==0 or nx.is_connected(rest)
        ok,emb=nx.check_planarity(g)
        faces=set()
        for u,v in emb.edges():
            f=emb.traverse_face(u,v); faces.add(frozenset(zip(f,f[1:]+f[:1])))
        # 면별로 '통째로 포함한' 호 개수 (호의 모든 변이 면 경계에 있음)
        fe=[{frozenset(e) for e in f} for f in faces]
        Cset={frozenset(e) for e in cyc_edges(C)}
        whole=[]
        for f in fe:
            if f==Cset: continue
            whole.append(sum(all(frozenset(e) in f for e in zip(p,p[1:])) for (a,b,p) in arcs if k in (a,b)))
        print(f"  조각 {k}: 2연결={nx.is_biconnected(g)} 3연결={nx.node_connectivity(g)>=3} 호서로소={dis} C 유도={ind} C 비분리={nonsep} 면수={len(faces)} C가 면={Cset in fe} 다른 면의 통째 호 수={sorted(whole)}")
    # 조립 곡면 X: 원판 D_k (경계 C_k) 를 호로 붙임. 면 = C_k, 변 = 경계 변(공유는 한 번)
    E2=defaultdict(list)
    for k,(ex,C) in pieces.items():
        for (x,y) in cyc_edges(C): E2[frozenset((x,y))].append((k,(x,y)))
    V2={v for (ex,C) in pieces.values() for v in C}
    chi=len(V2)-len(E2)+len(pieces)
    # 가향성
    adj=defaultdict(list)
    for e,l in E2.items():
        if len(l)==2:
            (k1,d1),(k2,d2)=l; s=-1 if d1==d2 else 1
            adj[k1].append((k2,s)); adj[k2].append((k1,s))
    sign={}; orient=True
    for st in pieces:
        if st in sign: continue
        sign[st]=1; S=[st]
        while S:
            x=S.pop()
            for y,s in adj[x]:
                if y in sign:
                    if sign[y]!=sign[x]*s: orient=False
                else: sign[y]=sign[x]*s; S.append(y)
    bd=nx.MultiGraph([tuple(e) for e,l in E2.items() if len(l)==1])
    b=nx.number_connected_components(bd)
    Hm=Counter(frozenset((a,c)) for (a,c,p) in arcs)
    print(f"  X: χ={chi} 가향={orient} 경계성분 b={b} → 종수식 2-χ-b={2-chi-b} (가향이면 0 ⟺ 평면);  H 다중변={any(v>1 for v in Hm.values())}")
    return Gs

# ---- 반례 Y1: 2-연결, '모든 매장에서 강체' 조각, H 에 이중변 ----
C0=['u1','m1','w1','g1','s1','n1','t1','g2','u2','m2','w2','g3','s2','n2','t2','g4']
P0=([('z',x) for x in ('u1','w1','u2','w2')],C0)
Q=([('y','u1'),('y','w1')],['u1','m1','w1','p','u2','m2','w2','q'])
R=([('yR','s1'),('yR','t1')],['s1','n1','t1','r1','s2','n2','t2','r2'])
arcs=[('P0','Q',['u1','m1','w1']),('P0','Q',['u2','m2','w2']),('P0','R',['s1','n1','t1']),('P0','R',['s2','n2','t2'])]
G=analyze("Y1 (반례 후보)",{'P0':P0,'Q':Q,'R':R},arcs)
# 같은 데이터에서 P0 만 3-연결로(바퀴: z 를 C0 전체에 연결)
P0w=([('z',x) for x in C0],C0)
analyze("Y1 의 P0 를 바퀴 W16 으로",{'P0':P0w,'Q':Q,'R':R},arcs)
# Q,R 도 3-연결로 (중심 추가)
Qw=([('hq',x) for x in Q[1]],Q[1]); Rw=([('hr',x) for x in R[1]],R[1])
analyze("Y1 전부 바퀴",{'P0':P0w,'Q':Qw,'R':Rw},arcs)
# 엇갈리지 않은 순서(평면 리본) 대조: R 이 a 와 a' 사이의 같은 쪽 호 둘을 쓰도록

# ---- 반례 Y2: n=2 꼬인 띠(뫼비우스), 두 조각 모두 2-연결·모든 매장에서 강체 ----
C0=['u1','m1','w1','g1','u2','m2','w2','g2']
P0=([('z','u1'),('z','u2')],C0)                         # 세타: 경로 u1-z-u2
Q=([('y','u1'),('y','w1')],['u1','m1','w1','p','w2','m2','u2','q'])   # a 정방향, a' 역방향 → 꼬임
arcs=[('P0','Q',['u1','m1','w1']),('P0','Q',['u2','m2','w2'])]
analyze("Y2 (뫼비우스 반례 후보)",{'P0':P0,'Q':Q},arcs)
Qw=([('hq',x) for x in Q[1]],Q[1]); P0w=([('z',x) for x in C0],C0)
analyze("Y2 의 두 조각을 바퀴로",{'P0':P0w,'Q':Qw},arcs)
