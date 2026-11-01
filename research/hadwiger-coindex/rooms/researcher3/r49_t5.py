# 정이십면체 쌍 W (교차 i -> 12+(i+s), s in 0,1,5; R48 r48_t7 과 같은 패턴):
# 면-직사각형 덮개수 cov_F(H) (사다리 비교차 조건 무시 → 관 수의 하한)
import networkx as nx, itertools
from pysat.formula import CNF
from pysat.card import CardEnc
from pysat.solvers import Glucose4
from r49_ladder import ccw_rot, face_list
I=nx.icosahedral_graph()
H=[(i,(i+s)%12) for i in range(12) for s in (0,1,5)]
r=ccw_rot(I); F=[tuple(f) for f in face_list(r)]
print('faces',len(F))
rects=[]
for a in F:
    for b in F:
        S=frozenset(k for k,(u,v) in enumerate(H) if u in a and v in b)
        if S: rects.append(S)
rects=list(set(rects))
mx=max(len(S) for S in rects); print('max edges in a face-pair rectangle',mx, 'lower bound tubes >=',-(-36//mx))
# 극대인 것만
rects=[S for S in rects if not any(S< T for T in rects)]
print('maximal rects',len(rects))
for K in range(-(-36//mx),13):
    cnf=CNF(); x=lambda i:i+1
    for e in range(36):
        cnf.append([x(i) for i,S in enumerate(rects) if e in S])
    card=CardEnc.atmost([x(i) for i in range(len(rects))],bound=K,top_id=len(rects))
    cnf.extend(card.clauses)
    with Glucose4(bootstrap_with=cnf.clauses) as s:
        ok=s.solve()
    print('cover with',K,'rects:',ok)
    if ok: break
