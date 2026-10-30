"""Gross–Tucker 식: 순환군 Z_n 위 부케(bouquet) 전압 그래프의 유도 그래프 = Cay(Z_n,S).
모든 정점에 같은 회전(dart 순환순서)을 주는 '유도 매장'의 면 수를 센다."""
import itertools
def faces(n, rot):
    # rot: 순환순서의 생성원 리스트(±s). dart (g,s): g -> g+s. 면 추적: (g,s) 다음 = (g+s, succ_rot(-s))
    succ = {rot[i]: rot[(i+1) % len(rot)] for i in range(len(rot))}
    seen=set(); F=[]
    for g in range(n):
        for s in rot:
            if (g,s) in seen: continue
            L=0; d=(g,s)
            while d not in seen:
                seen.add(d); L+=1; h=(d[0]+d[1])%n; d=(h, succ[(-d[1])%n])
            F.append(L)
    return F
for n,S in ((5,[1,2]),(7,[1,2,3])):
    darts=[s%n for s in S]+[(-s)%n for s in S]
    best=None
    for perm in itertools.permutations(darts[1:]):
        rot=[darts[0]]+list(perm); F=faces(n,rot)
        V,E=n,n*len(S); chi=V-E+len(F)
        if best is None or chi>best[0]: best=(chi,rot,sorted(F))
    print(f"Cay(Z{n},{S}): 최대 χ={best[0]} (방향 종수 {(2-best[0])//2}), 회전 {best[1]}, 면 길이 {best[2]}")
