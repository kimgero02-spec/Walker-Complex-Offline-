# CEGAR: 볼록 순서 0..n-1 위 3-페이지 그래프 중 6-색칠 불가능한 것이 있는가 (n 고정, 결정 절차)
import itertools, sys, time
from pysat.solvers import Cadical153, Glucose4
from pysat.card import CardEnc, EncType
n=int(sys.argv[1]); K=int(sys.argv[2]) if len(sys.argv)>2 else 6; P=3
pairs=list(itertools.combinations(range(n),2))
cnt=[0]
def new(): cnt[0]+=1; return cnt[0]
x={e:new() for e in pairs}; y={(e,p):new() for e in pairs for p in range(P)}
S=Cadical153()
def cr(e,f):
    a,b=e;c,d=f; return (a<c<b<d) or (c<a<d<b)
for e in pairs:
    S.add_clause([-x[e]]+[y[e,p] for p in range(P)])
for e,f in itertools.combinations(pairs,2):
    if cr(e,f):
        for p in range(P): S.add_clause([-y[e,p],-y[f,p]])
# 최소 차수 >= K (K+1-임계 부분그래프 조건; 전체 그래프를 그대로 임계로 가정해도 일반성 잃지 않음: 임계 부분그래프도 3-페이지)
for v in range(n):
    lits=[x[e] for e in pairs if v in e]
    enc=CardEnc.atleast(lits,bound=K,top_id=cnt[0],encoding=EncType.seqcounter)
    cnt[0]=max(cnt[0],enc.nv)
    for c in enc.clauses: S.add_clause(c)
def color(E):
    s=Glucose4(); v=lambda a,c:a*K+c+1
    for a in range(n): s.add_clause([v(a,c) for c in range(K)])
    for a,b in E:
        for c in range(K): s.add_clause([-v(a,c),-v(b,c)])
    if not s.solve(): return None
    m=s.get_model(); return [next(c for c in range(K) if m[a*K+c]>0) for a in range(n)]
it=0; t0=time.time()
while True:
    if not S.solve(): print('n',n,'UNSAT: 모든 3-페이지 (이 순서) 그래프가',K,'-색칠 가능 (최소차수 조건하)', 'iters',it, round(time.time()-t0,1),'s'); break
    m=set(l for l in S.get_model() if l>0); E=[e for e in pairs if x[e] in m]
    col=color(E)
    if col is None: print('FOUND chi>%d'%K, n, E); break
    S.add_clause([x[e] for e in pairs if col[e[0]]==col[e[1]]]); it+=1
