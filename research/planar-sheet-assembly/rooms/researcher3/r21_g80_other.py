# R21-researcher3: find a planar 3-cover of G80 whose edge family differs from the locked one (then verified directly).
import json, random, networkx as nx
from r21_verify import planar
d=json.load(open("r20_locked_only_N80_n3.json")); Q=[[tuple(sorted(e)) for e in q] for q in d["Q"]]
E=sorted(set(e for q in Q for e in q)); fam={frozenset(q) for q in Q}
rng=random.Random(0)
for t in range(200):
    order=E[:]; rng.shuffle(order); R=[]; rest=order
    for k in range(3):
        S=[]
        for e in rest:
            if planar(S+[e]): S.append(e)
        R.append(S); rest=[e for e in rest if e not in set(S)]
    if not rest:
        ok=all(planar(s) for s in R) and set(e for s in R for e in s)==set(E)
        print("found 3-cover, sizes",[len(s) for s in R],"verified",ok,"same family as locked:",{frozenset(s) for s in R}==fam)
        json.dump({"R":[[list(e) for e in s] for s in R]},open("r21_g80_other_cover.json","w")); break
    else: print("trial",t,"leftover",len(rest))
