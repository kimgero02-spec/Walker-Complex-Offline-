# (c) τ<=zig 직접 증명의 구현 점검: 사상 F 가 영벡터를 안 내는지, 그래프·진색칠을 바꿔가며
import itertools, random, networkx as nx, numpy as np
def faces_B0(G):
    V=list(G.nodes()); out=[]
    for k in range(1,len(V)+1):
        for A in itertools.combinations(V,k):
            pass
    # A,B 서로소 완전이분 (빈 변 허용): 전수는 작은 그래프에서만
    for assign in itertools.product((0,1,2),repeat=len(V)):  # 0 없음,1 A,2 B
        A=[v for v,a in zip(V,assign) if a==1]; B=[v for v,a in zip(V,assign) if a==2]
        if not A and not B: continue
        if all(G.has_edge(a,b) for a in A for b in B): out.append((A,B))
    return out
def maxzig(G,col):
    V=sorted(G.nodes(), key=lambda v:col[v]); best=0
    # 최대 지그재그: 색 증가 수열 z1<..<zk, 홀수/짝수 번째가 완전 이분. DFS
    def ext(seq):
        nonlocal best
        best=max(best,len(seq))
        for v in V:
            if col[v]>col[seq[-1]]:
                s2=seq+[v]; odd=s2[0::2]; ev=s2[1::2]
                if all(G.has_edge(a,b) for a in odd for b in ev): ext(s2)
    for v in V: ext([v])
    return best
def check(G,col,trials=20,seed=0):
    rnd=random.Random(seed); L=maxzig(G,col); m=max(col.values())
    bad=0; fs=faces_B0(G)
    for (A,B) in fs:
        for _ in range(trials):
            x=np.zeros(m)
            for v in A: x[col[v]-1]+=rnd.random()+1e-3
            for v in B: x[col[v]-1]-=rnd.random()+1e-3
            mom=[sum(x[j]*(j+1)**k for j in range(m)) for k in range(L)]
            if max(abs(t) for t in mom)<1e-9: bad+=1
    return L,len(fs),bad
for name,G,col in [("C5",nx.cycle_graph(5),{0:1,1:2,2:1,3:2,4:3}),
                   ("C5 (다른 색칠)",nx.cycle_graph(5),{0:1,1:3,2:1,3:2,4:4}),
                   ("K4",nx.complete_graph(4),{i:i+1 for i in range(4)}),
                   ("comp(C7)",nx.complement(nx.cycle_graph(7)),{0:1,1:1,2:2,3:2,4:3,5:3,6:4})]:
    print(name, check(G,col))
