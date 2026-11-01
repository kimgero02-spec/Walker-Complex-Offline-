# R03: C_n[K_m] 의 모멘트 곡선 배치 검증. 극대 완전이분쌍을 brute force 로 열거(작은 경우)하고
# (1) 분류 정리와 개수 대조, (2) Gale 부호변화 수 <= 2m-1, (3) 독립 LP(float) 로 분리 확인.
import sys, itertools, numpy as np
from scipy.optimize import linprog
def build(n,m):
    V=[(i,s) for i in range(n) for s in range(m)]
    N=len(V)
    adj=[[ (a!=b) and ((V[a][0]-V[b][0])%n in (0,1,n-1)) for b in range(N)] for a in range(N)]
    return V,adj
def maxpairs(n,m):
    V,adj=build(n,m); N=len(V)
    nb=[frozenset(k for k in range(N) if adj[v][k]) for v in range(N)]
    def common(S):
        r=set(range(N))
        for v in S: r&=nb[v]
        return frozenset(r)
    pairs=set()
    for mask in range(1,1<<N):
        A=frozenset(k for k in range(N) if mask>>k&1)
        B=common(A)
        if not B: continue
        A2=common(B); B2=common(A2)
        pairs.add(frozenset([A2,B2]))
    return V,pairs
def classify(n,m):
    # 분류 정리에 의한 쌍 목록 (무방향)
    idx=lambda i,s:(i%n)*m+s
    blob=lambda i:frozenset(idx(i,s) for s in range(m))
    out=set()
    for i in range(n):
        for r in range(1,m+1):
            for S in itertools.combinations(range(m),r):
                B=frozenset(idx(i,s) for s in S)
                A=(blob(i)-B)|blob(i-1)|blob(i+1)
                out.add(frozenset([A,B]))
        for r in range(1,m):
            for S in itertools.combinations(range(m),r):
                for q in range(1,m):
                    for T in itertools.combinations(range(m),q):
                        A=frozenset([idx(i,s) for s in S]+[idx(i+1,t) for t in T])
                        B=(blob(i)|blob(i+1))-A
                        out.add(frozenset([A,B]))
    return out
def changes(A,B,t):
    seq=sorted([(t[a],0) for a in A]+[(t[b],1) for b in B])
    return sum(1 for x,y in zip(seq,seq[1:]) if x[1]!=y[1])
def lpsep(A,B,Y):
    d=Y.shape[1]
    Aub=[];bub=[]
    for a in A: Aub.append(list(-Y[a])+[1.0]);bub.append(-1.0)
    for b in B: Aub.append(list(Y[b])+[-1.0]);bub.append(-1.0)
    r=linprog(np.zeros(d+1),A_ub=Aub,b_ub=bub,bounds=[(None,None)]*(d+1),method="highs")
    return r.status==0
def run(n,m,brute=True,lp=True):
    d=2*m-1
    t={ (i*m+s):float(i*m+s+1) for i in range(n) for s in range(m)}   # 블롭 연속, t=1..nm
    # 스케일: 모멘트 곡선 좌표 (t/(nm))^k 로 수치 안정화
    T=n*m
    Y=np.array([[ (t[k]/T)**j for j in range(1,d+1)] for k in range(n*m)])
    cl=classify(n,m)
    msg=f"n={n} m={m} d={d} 분류쌍={len(cl)}"
    if brute:
        V,pairs=maxpairs(n,m)
        pairs={p for p in pairs if all(p)}
        msg+=f" brute={len(pairs)} 일치={cl==pairs}"
    mx=max(changes(*list(p) if len(p)==2 else (list(p)[0],list(p)[0]),t) for p in cl)
    msg+=f" 최대부호변화={mx} (허용 {d})"
    if lp:
        bad=0
        for p in cl:
            L=list(p); A,B=L[0],L[1]
            if not lpsep(sorted(A),sorted(B),Y): bad+=1
        msg+=f" LP실패={bad}"
    print(msg,flush=True)
if __name__=="__main__":
    run(5,2); run(5,3); run(7,2,brute=False)
    run(5,4,brute=False); run(5,5,brute=False,lp=False); run(7,3,brute=False,lp=True)
    run(6,2,brute=True)
