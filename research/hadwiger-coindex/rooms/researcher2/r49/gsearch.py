# search for a smaller "forbidden-pattern" gadget: triangulation with a face f and non-mono pattern on f not extendable
import networkx as nx, itertools, random
from tri import faces_of
from minhit import all_fb
from t4 import tri_from_flips
rng=random.Random(3); seen=set(); hits={}
for n in range(6,11):
    for trial in range(400 if n<10 else 300):
        G=tri_from_flips(n,rng.randint(5,60),rng)
        h=nx.weisfeiler_lehman_graph_hash(G,iterations=4)
        if h in seen: continue
        seen.add(h)
        fbs=all_fb(G)
        for f in faces_of(G):
            for P in itertools.product('FB',repeat=3):
                if len(set(P))==1: continue
                if not any(all((v in F)==(p=='F') for v,p in zip(f,P)) for F in fbs):
                    hits.setdefault(n,[]).append((h,f,P))
    print(n,'distinct',sum(1 for _ in seen),'gadget hits',len(hits.get(n,[])),flush=True)
