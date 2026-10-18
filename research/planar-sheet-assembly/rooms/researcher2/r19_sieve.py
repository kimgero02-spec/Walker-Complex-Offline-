# arithmetic sieve (fiber lemma): chi-multisets with sum N, parts<=4, some part>=3 marked defective (omega=chi-1),
# condition N <= (chi_k-1)*prod_{j!=k} chi_j for each defective k. Lists surviving (multiset, defective-set) pairs.
import itertools, math
def parts(n,m):
    if n==0: yield (); return
    for p in range(min(n,m),0,-1):
        for r in parts(n-p,p): yield (p,)+r
for N in range(6,10):
    out=[]
    for P in parts(N,4):
        idx=[i for i,p in enumerate(P) if p>=3]
        ok=[i for i in idx if N <= (P[i]-1)*math.prod(P[:i]+P[i+1:])]
        if ok: out.append((P,[P[i] for i in ok]))
    print(N,out)
