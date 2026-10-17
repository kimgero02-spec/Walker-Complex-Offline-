# R04 researcher2: Steiner 정리 2 증명(6-8쪽)의 단계별 구현 점검.
# 보조정리 5 는 "극대 연결 이분 유도부분그래프를 탐욕적으로 뗀다"로 직접 구성(증명은 보고서).
import itertools, sys, random
import networkx as nx

def lemma5(G, order=None):
    R = set(G.nodes()); parts=[]
    nodes = list(order) if order else list(G.nodes())
    while R:
        v0 = next(v for v in nodes if v in R)
        X = {v0}
        side = {v0:0}
        changed=True
        while changed:
            changed=False
            for v in list(R-X):
                nb=[u for u in G[v] if u in X]
                if not nb: continue
                s={side[u] for u in nb}
                if len(s)==1:   # 한쪽 이웃만 -> 반대편에 붙일 수 있음 (극대성 위반)
                    side[v]=1-s.pop(); X.add(v); changed=True
        parts.append((X,{v:side[v] for v in X})); R-=X
    return parts

def check_lemma5(G,parts):
    eta={}
    for i,(X,sd) in enumerate(parts):
        for v in X: eta[v]=i
        H=G.subgraph(X)
        assert nx.is_connected(H) and nx.is_bipartite(H)
        for u,v in H.edges(): assert sd[u]!=sd[v]
    for j,(Xj,_) in enumerate(parts):
        for v in Xj:
            for i in range(j):
                Xi,sdi=parts[i]
                nb=[u for u in G[v] if u in Xi]
                if nb: assert len({sdi[u] for u in nb})==2,(v,i)
    return eta

def best_zigzag(G,c):
    verts=sorted(G.nodes(),key=lambda v:c[v]); best=[]
    def dfs(seq):
        nonlocal best
        if len(seq)>len(best): best=list(seq)
        last=c[seq[-1]] if seq else -1
        for v in verts:
            if c[v]<=last: continue
            ok=True
            for idx,z in enumerate(seq):
                if (len(seq)-idx)%2==1 and not G.has_edge(z,v): ok=False;break
            if ok: dfs(seq+[v])
    dfs([]); return best

def construct(G,parts,eta,c,Z):
    t=len(Z)-(len(Z)%2); Z=Z[:t]; k=t//2+1
    Z1=Z[0::2]; Z2=Z[1::2]
    for a in Z1:
        for b in Z2: assert G.has_edge(a,b)
    M=[(Z[i],Z[j]) for i in range(t) for j in range(i+1,t) if eta[Z[i]]==eta[Z[j]]]
    for a,b in M: assert Z.index(b)==Z.index(a)+1
    used=set(); [used.update(e) for e in M]; assert len(used)==2*len(M)
    spanning={i:nx.minimum_spanning_tree(G.subgraph(X)) for i,(X,_) in enumerate(parts)}
    col={}
    for i,(X,sd) in enumerate(parts):
        for v in X: col[v]=sd[v]+1   # 고유 이분 -> 진 2-색칠
    trees=[]  # (vertex set, set of eta indices)
    if len(M)<=k-2:
        # perfect matching extending M in K_{k-1,k-1}
        mm=[(a,b) if a in Z1 else (b,a) for a,b in M]
        rx={x for x,_ in mm}; ry={y for _,y in mm}
        rem1=[x for x in Z1 if x not in rx]; rem2=[y for y in Z2 if y not in ry]
        pm=mm+list(zip(rem1,rem2)); r=len(mm)
        for j,(x,y) in enumerate(pm):
            if j<r: trees.append(({x,y},{eta[x]}))
            elif j<k-2: trees.append(({x,y},{eta[x],eta[y]}))
        x,y=pm[k-2]
        trees.append(({x},{eta[x]})); trees.append(({y},{eta[y]}))
        # 위 마지막 두 트리는 전체 T_eta(x), T_eta(y)
        T=[]
        for vs,es in trees:
            full=set()
            for e in es: full|=parts[e][0]
            T.append((full,es))
        trees=T
        assert len(trees)==k
    else:
        assert len(M)==k-1
        mm=sorted(([(a,b) if a in Z1 else (b,a) for a,b in M]),key=lambda p:eta[p[0]])
        for x,y in mm[:-1]:
            trees.append((set(parts[eta[x]][0]),{eta[x]}))
        x,y=mm[-1]
        trees.append(({x},set())); trees.append(({y},set()))
        col[x]=1; col[y]=1
        assert len(trees)==k
    # 서로소
    allv=set()
    for vs,_ in trees:
        assert not (vs&allv); allv|=vs
    # 각 트리 안에서 색칠이 진(고유 이분 그대로, 병합 트리는 x-y 간선이 진이 되도록 한쪽 반전)
    # Case1 병합 트리(j in [r, k-2)): T_eta(x)+edge xy + T_eta(y): col[x]!=col[y] 되도록 y쪽 반전
    if len(M)<=k-2:
        for j,(vs,es) in enumerate(trees):
            if len(es)==2:
                x,y=pm[j]
                if col[x]==col[y]:
                    for v in parts[eta[y]][0]: col[v]=3-col[v]
    # 검증: 트리가 연결·진색칠 가능하고 모든 쌍에 단색 연결 간선
    for vs,es in trees:
        sub=G.subgraph(vs)
        if len(es)==2:
            x,y=[p for p in pm if p[0] in vs][0]
            S=nx.Graph(); S.add_nodes_from(vs)
            S.add_edges_from(spanning[min(es)].edges()); S.add_edges_from(spanning[max(es)].edges()); S.add_edge(x,y)
            assert nx.is_tree(S)
            for u,v in S.edges(): assert col[u]!=col[v]
        elif len(es)==1:
            S=spanning[list(es)[0]]
            for u,v in S.edges(): assert col[u]!=col[v]
    for a in range(k):
        for b in range(a+1,k):
            ok=any(G.has_edge(u,v) and col[u]==col[v] for u in trees[a][0] for v in trees[b][0])
            assert ok,("no mono edge",a,b)
    return k,len(M),t

def run(name,G,tries=1):
    for tr in range(tries):
        order=list(G.nodes()); random.shuffle(order)
        parts=lemma5(G,order); eta=check_lemma5(G,parts)
        c={}
        for i,(X,sd) in enumerate(parts):
            for v in X: c[v]=2*(i+1)-1+sd[v]
        for u,v in G.edges(): assert c[u]!=c[v]
        Z=best_zigzag(G,c)
        if len(Z)<2: print(name,"zigzag",len(Z)); continue
        k,m,t=construct(G,parts,eta,c,Z)
        print(f"{name}: parts={len(parts)} zigzag={len(Z)} t={t} |M|={m} -> odd K_{k} expansion verified")

if __name__=="__main__":
    random.seed(1)
    run("K4",nx.complete_graph(4),3)
    run("K6",nx.complete_graph(6),5)
    def blow(G,m):
        H=nx.Graph()
        for u in G: 
            for s in range(m): H.add_node((u,s))
        for u in G:
            for s in range(m):
                for t in range(s+1,m): H.add_edge((u,s),(u,t))
        for u,v in G.edges():
            for s in range(m):
                for t in range(m): H.add_edge((u,s),(v,t))
        return H
    run("C5[K2]",blow(nx.cycle_graph(5),2),5)
    run("C5[K3]",blow(nx.cycle_graph(5),3),5)
    run("Petersen",nx.petersen_graph(),5)
    G=nx.complement(nx.cycle_graph(7)); run("co-C7",G,5)
    # Kneser K(6,2)
    sub=list(itertools.combinations(range(6),2)); K=nx.Graph(); K.add_nodes_from(sub)
    for a,b in itertools.combinations(sub,2):
        if not set(a)&set(b): K.add_edge(a,b)
    run("K(6,2)",K,5)
