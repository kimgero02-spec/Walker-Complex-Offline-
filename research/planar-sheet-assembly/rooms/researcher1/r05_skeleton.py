# 보조정리 K 의 유한 경우 확인: 고정 3-색칠 phi 에서 필요조건 N2 + N3 이 강제하는 골격은 모두 비평면인가?
# T1=a1a2a3, T2=b1b2b3, phi(a_i)=phi(b_i)=i (T1,T2 서로소).
# N3: 색 c 와 s,t != c 에 대해 a_s, b_t 는 색 c 의 공통 이웃을 가진다.  -> 색마다 K_{2,2} 를 이분 클릭(가운데 점)으로 덮는다.
# N2: p⊂T1, q⊂T2 쌍마다 p-q 사이 변.  (a_i b_i 변은 phi 에서 같은 색이라 불가)
import itertools, networkx as nx
def bicliques(c):
    s,t=[i for i in (1,2,3) if i!=c]
    As=[('a%d'%s,),('a%d'%t,),('a%d'%s,'a%d'%t)]; Bs=[('b%d'%s,),('b%d'%t,),('b%d'%s,'b%d'%t)]
    return [(A,B) for A in As for B in Bs], [('a%d'%x,'b%d'%y) for x in (s,t) for y in (s,t)]
def minimal_covers(c):
    bl,need=bicliques(c); out=[]
    for r in range(1,5):
        for S in itertools.combinations(bl,r):
            cov=lambda SS:{(a,b) for A,B in SS for a in A for b in B}
            if cov(S)>=set(need) and all(not cov(S[:i]+S[i+1:])>=set(need) for i in range(r)):
                # 각 클릭을 더 작은 클릭으로 바꿔도 덮이면 극소 아님
                ok=True
                for i,(A,B) in enumerate(S):
                    for A2,B2 in bl:
                        if set(A2)<=set(A) and set(B2)<=set(B) and (A2,B2)!=(A,B):
                            if cov(S[:i]+((A2,B2),)+S[i+1:])>=set(need): ok=False
                if ok: out.append(S)
    return out
cand=[('a%d'%s,'b%d'%t) for s in (1,2,3) for t in (1,2,3) if s!=t]
def N2(B):
    for P in itertools.combinations((1,2,3),2):
        for R in itertools.combinations((1,2,3),2):
            if not any(('a%d'%p,'b%d'%q) in B for p in P for q in R): return False
    return True
Bmin=[]
for r in range(1,7):
    for B in itertools.combinations(cand,r):
        if N2(set(B)) and not any(set(b0)<=set(B) for b0 in Bmin): Bmin.append(B)
print('극소 B:',Bmin)
C={c:minimal_covers(c) for c in (1,2,3)}
print('색별 극소 덮개 수',{c:len(C[c]) for c in C})
nplanar=0; total=0
for B in Bmin:
    for S1 in C[1]:
        for S2 in C[2]:
            for S3 in C[3]:
                G=nx.Graph(list(B))
                for c,S in ((1,S1),(2,S2),(3,S3)):
                    for i,(A,Bb) in enumerate(S):
                        m=('m',c,i)
                        for v in A+Bb: G.add_edge(m,v)
                total+=1
                if nx.check_planarity(G)[0]:
                    nplanar+=1
                    if nplanar<=3: print('평면 골격:',B,S1,S2,S3)
print('골격',total,'평면',nplanar)
