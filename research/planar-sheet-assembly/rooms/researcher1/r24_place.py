# R24 researcher1: counterexample search only. Same pieces (P1, pi(P2)), different union chromatic data.
import itertools, random
from r24_chrompoly import V, P1, P2, ff_coeffs, ff_to_mono, chi_from_ff
def owners(E1, E2):
    out=[]
    for r in range(len(V)+1):
        for V1 in itertools.combinations(V, r):
            S=set(V1)
            if all(len(e & S)>=1 for e in E1) and all(len(e - S)>=1 for e in E2):
                out.append(V1)
    return out
random.seed(1)
seen={}
for t in range(4000):
    p=V[:]; random.shuffle(p); pi=dict(zip(V,p))
    Q2={frozenset(pi[v] for v in e) for e in P2}
    if Q2 & P1: continue
    G=P1|Q2
    a=ff_coeffs(V,[tuple(e) for e in G]); c=chi_from_ff(a)
    key=tuple(a)
    if key in seen: continue
    own=owners(P1,Q2)
    if not own: continue
    seen[key]=(c, sorted(map(sorted,Q2)), own[0])
for k,(c,Q2,o) in sorted(seen.items(), key=lambda kv: kv[1][0]):
    print('chi',c,'ff',list(k),'P2 image',Q2,'V1',o)
