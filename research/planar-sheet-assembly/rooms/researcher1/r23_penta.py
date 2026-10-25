# R23: 조밀한 평면 둘레5 그래프 생성기 (면 목록 유지). 후보 탐색 전용.
import networkx as nx, random
def dense_planar_girth5(n,seed,L0=10):
    rng=random.Random(seed)
    G=nx.cycle_graph(L0); faces=[list(range(L0)),list(range(L0))[::-1]]
    nxt=L0
    def dist(a,b):
        try: return nx.shortest_path_length(G,a,b)
        except: return 99
    def try_chords():
        changed=True
        while changed:
            changed=False
            rng.shuffle(faces)
            for fi,F in enumerate(faces):
                L=len(F)
                if L<8: continue
                opts=[(i,j) for i in range(L) for j in range(L) if 4<=(j-i)%L<=L-4]
                rng.shuffle(opts)
                for i,j in opts:
                    a,b=F[i],F[j]
                    if not G.has_edge(a,b) and dist(a,b)>=4:
                        G.add_edge(a,b)
                        k=(j-i)%L
                        F1=[F[(i+t)%L] for t in range(k+1)]
                        F2=[F[(j+t)%L] for t in range(L-k+1)]
                        faces[fi]=F1; faces.append(F2); changed=True; break
                if changed: break
    while nxt<n:
        F=rng.choice([f for f in faces if len(f)>=5])
        fi=faces.index(F); L=len(F)
        # 경로 (새 점 m 개) 를 면 안에 넣는다: 면 거리 d, 길이 m+1
        cands=[]
        for i in range(L):
            for d in range(1,L):
                for m in (1,2,3):
                    if d+m+1>=5 and L-d+m+1>=5:
                        cands.append((i,d,m))
        rng.shuffle(cands)
        done=False
        for i,d,m in cands:
            a,b=F[i],F[(i+d)%L]
            if dist(a,b)+m+1<5: continue
            if m==1 and False: pass
            newv=list(range(nxt,nxt+m)); nxt+=m
            path=[a]+newv+[b]
            nx.add_path(G,path)
            F1=[F[(i+t)%L] for t in range(d+1)]+newv[::-1]
            F2=[F[(i+d+t)%L] for t in range(L-d+1)]+newv
            faces[fi]=F1; faces.append(F2); done=True; break
        if not done: continue
    try_chords()
    assert nx.check_planarity(G)[0] and nx.girth(G)>=5
    return G
if __name__=="__main__":
    for n in (20,40,60):
        G=dense_planar_girth5(n,1); m=G.number_of_edges(); N=G.number_of_nodes()
        print(N,m,round(m/(5/3*(N-2)),3),nx.girth(G))
