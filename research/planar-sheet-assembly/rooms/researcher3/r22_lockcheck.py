# R22-researcher3: independent check of locking (R20 Def 3.1 (L1),(L2)) for Q (r20_locked_only_N80_n3.json)
# and for the other cover R (r21_g80_other_cover.json). Reference only, not evidence.
import json, networkx as nx
def norm(L): return [tuple(sorted(map(int,e))) for e in L]
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
Q=[norm(q) for q in json.load(open('r20_locked_only_N80_n3.json'))['Q']]
R=[norm(r) for r in json.load(open('r21_g80_other_cover.json'))['R']]
EQ=set(e for q in Q for e in q); ER=set(e for r in R for e in r)
print("same G:",EQ==ER,"|E|",len(EQ),"V",len({v for e in EQ for v in e}))
for name,P in (("Q",Q),("R",R)):
    allp=[e for p in P for e in p]
    print(name,"sizes",[len(p) for p in P],"L1 disjoint",len(allp)==len(set(allp)),
          "planar",[planar(p) for p in P],"spanning",[len({v for e in p for v in e}) for p in P])
    bad=[]
    for k,p in enumerate(P):
        s=set(p)
        for e in sorted(EQ-s):
            if planar(p+[e]): bad.append((k,e))
    print(name,"L2 violations (sheet index 0-based, edge):",bad)
print("|R_i cap Q_k|:",[[len(set(r)&set(q)) for q in Q] for r in R])
