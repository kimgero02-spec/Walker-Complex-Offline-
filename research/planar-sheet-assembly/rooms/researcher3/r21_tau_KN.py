# R21-researcher3: decisive-example search: a triangularly locked 3-partition of K_N (N=8,9) with theta(K_N)=2.
# P1 = a triangulation (then P1+e is non-planar by the Euler bound), P2 subset of the complement R, P3=R\P2 nonempty,
# P2 planar and P2+e non-planar for every e in P3. Every claim is checked by direct planarity tests.
import itertools, random, sys, json, networkx as nx
from r21_pendant import sphere_tri
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
N=int(sys.argv[1]); rng=random.Random(int(sys.argv[2]))
for t in range(3000):
    T=sphere_tri(N,rng); P1=[tuple(sorted(e)) for e in T.edges()]
    R=[e for e in itertools.combinations(range(N),2) if e not in set(P1)]
    if planar(R): continue
    for r in range(len(R)-1,0,-1):
        for P2 in itertools.combinations(R,r):
            P3=[e for e in R if e not in P2]
            if planar(list(P2)) and all(not planar(list(P2)+[e]) for e in P3):
                ok1=all(not planar(P1+[e]) for e in R) and planar(P1)
                print("FOUND N",N,"|P1|",len(P1),"|P2|",len(P2),"|P3|",len(P3),"P1 locked vs rest:",ok1)
                json.dump({"Q":[P1,list(P2),P3]},open(f"r21_tau_K{N}.json","w")); sys.exit()
print("none")
