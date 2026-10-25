# R21-researcher3: GENERATOR. Exchange-chain walk from the locked 3-partition of G80 looking for a different
# planar 3-cover (edge family not a permutation of the locked one). Output re-verified directly below.
import json, random, networkx as nx
from r21_verify import planar
d=json.load(open("r20_locked_only_N80_n3.json")); Q=[[tuple(sorted(e)) for e in q] for q in d["Q"]]
E=sorted(set(e for q in Q for e in q)); fam={frozenset(q) for q in Q}
rng=random.Random(1)
for trial in range(300):
    S=[set(q) for q in Q]
    k0=rng.randrange(3); e=rng.choice(sorted(S[k0])); S[k0].discard(e); fl=e; last=k0
    for step in range(60):
        k=rng.choice([j for j in range(3) if j!=last])
        if planar(list(S[k])+[fl]): S[k].add(fl); fl=None; break
        cand=[f for f in sorted(S[k]) if planar(list(S[k]-{f})+[fl])]
        if not cand: continue
        f=rng.choice(cand); S[k].discard(f); S[k].add(fl); fl=f; last=k
    if fl is None:
        ok=all(planar(list(s)) for s in S) and set().union(*S)==set(E)
        same={frozenset(s) for s in S}==fam
        print("trial",trial,"cover verified",ok,"same family",same,"sizes",[len(s) for s in S])
        if ok and not same:
            json.dump({"R":[[list(x) for x in sorted(s)] for s in S]},open("r21_g80_other_cover.json","w")); break
else: print("none")
