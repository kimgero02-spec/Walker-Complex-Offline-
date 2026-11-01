import random
random.seed(3)
def rand_graph(n,m):
    E=[(random.randrange(i),i) for i in range(1,n)]
    while len(E)<m: 
        u,v=random.randrange(n),random.randrange(n)
        if u!=v: E.append((u,v))
    return E
def dicut_moves(n,E,o):   # o[e]=+1: E[e] 방향 그대로 (u->v), -1: 반대
    # 모든 S 에 대해 단방향 절단 찾기 (소형 n)
    moves=[]
    for mask in range(1,2**n-1):
        S={i for i in range(n) if mask>>i&1}
        ins=outs=0
        for k,(u,v) in enumerate(E):
            t,h=(u,v) if o[k]==1 else (v,u)
            if (t in S)!=(h in S):
                if h in S: ins+=1
                else: outs+=1
        if (ins==0)!=(outs==0): moves.append(S)
    return moves
def flip(E,o,S):
    o=o[:]
    for k,(u,v) in enumerate(E):
        if (u in S)!=(v in S): o[k]=-o[k]
    return o
def potential(n,E,o,o2):   # t(e traversed u->v)=w_o-w_o2 = o[k]-o2[k]; h = 누적/2
    h=[None]*n; h[0]=0; ch=True
    while ch:
        ch=False
        for k,(u,v) in enumerate(E):
            t=o[k]-o2[k]
            if h[u] is not None and h[v] is None: h[v]=h[u]+t//2; ch=True
            if h[v] is not None and h[u] is None: h[u]=h[v]-t//2; ch=True
    for k,(u,v) in enumerate(E):
        if h[v]-h[u]!=(o[k]-o2[k])//2: return None
    return h
ok=True
for trial in range(300):
    n=random.randint(3,7); m=random.randint(n-1,n+4)
    E=rand_graph(n,m); o=[random.choice([1,-1]) for _ in E]
    o2=o[:]
    for _ in range(random.randint(0,6)):
        mv=dicut_moves(n,E,o2)
        if mv: o2=flip(E,o2,random.choice(mv))
    cur=o[:]; steps=0
    while True:
        h=potential(n,E,cur,o2)
        if h is None: ok=False;print("잠재함수 없음");break
        if min(h)==max(h): break
        M={i for i in range(n) if h[i]==max(h)}
        cur=flip(E,cur,M); steps+=1
        assert steps<200
    if cur!=o2: ok=False; print("실패")
print("Pretzel 최상위층 절단 알고리즘 일치:",ok)
