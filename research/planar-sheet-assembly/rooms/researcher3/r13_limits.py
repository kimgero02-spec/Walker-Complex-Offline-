# R13: (co)product structure maps vs admissibility; oplax comparison; K1-model threshold
import sys,os,itertools; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from r09_check import *
K2=({'u','v'},{('u','v')}); Uu=({'u'},set())
# codiagonal on path a-b-c, D=(ab,bc)
ab=({'a','b'},{('a','b')}); bc=({'b','c'},{('b','c')})
_,_,Ls=L([ab,bc,ab,bc],[ab,bc],(0,1,0,1)); print('codiagonal (ab,bc)+(ab,bc)->(ab,bc): |L| =',len(Ls))
_,_,Ls=L([K2,K2,K2,K2],[K2,K2],(0,1,0,1)); print('codiagonal (K2,K2)+(K2,K2)->(K2,K2): |L| =',len(Ls))
# product projection D' x D -> D with D'=(K2,K2), D=(K2,{u})
P=[K2,Uu,K2,Uu]; _,_,Ls=L(P,[K2,Uu],(0,1,0,1)); print('projection (K2,K2)x(K2,u)->(K2,u): |L| =',len(Ls))
_,_,Ls=L(P,[K2,K2],(0,0,1,1)); print('projection (K2,K2)x(K2,u)->(K2,K2): |L| =',len(Ls))
# K1 model: FinSet_{<=N}; functor exists iff N<=2  (brute force over choices for N=2, nonexistence for N=3 by R09 ex 1.0)
def objs(N): return list(range(1,N+1))
def homs(m,n): return list(itertools.product(range(n),repeat=m))
def eps_allowed(f,m,n):
    if m<2: return [None]
    if len(set(f))>1: return [1]
    return [0,1] if n>=2 else [0]
def search(N):
    mors=[(m,n,f) for m in objs(N) for n in objs(N) for f in homs(m,n)]
    allowed={x:eps_allowed(x[2],x[0],x[1]) for x in mors}
    names=list(mors)
    for ch in itertools.product(*[allowed[x] for x in names]):
        e=dict(zip(names,ch)); ok=True
        for (m,n,f) in names:
            for (n2,p,g) in names:
                if n2!=n: continue
                gf=(m,p,tuple(g[i] for i in f))
                if m<2: continue
                exp=e[(m,n,f)] and (e[(n,p,g)] if n>=2 else 0)
                if e[gf]!=exp: ok=False;break
            if not ok: break
        if ok: return True
    return False
print('K1 model functor exists, N=2:',search(2))
