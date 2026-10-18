# find planar I (dodecahedron, 30 edges) maximal planar in G = I u T, T a triangulation (54 edges) -> augmentation fails.
import random, networkx as nx
from r20_frozen import random_triangulation, planar
rng=random.Random(5)
D=nx.dodecahedral_graph(); N=20
DE=set(frozenset(e) for e in D.edges())
def viol(TE):
    S=set(DE)|TE
    bad=[e for e in TE-DE if planar(list(map(tuple,DE))+[tuple(e)])]
    return bad
T=random_triangulation(N,rng,400)
perm=list(range(N)); rng.shuffle(perm)
def TEof(p): return set(frozenset((p[a],p[b])) for a,b in T.edges())
cur=len(viol(TEof(perm)))
for it in range(6000):
    i,j=rng.sample(range(N),2); perm[i],perm[j]=perm[j],perm[i]
    v=len(viol(TEof(perm)))
    if v<=cur: cur=v
    else: perm[i],perm[j]=perm[j],perm[i]
    if cur==0: break
TE=TEof(perm)
print("violations",cur, "|T|",len(TE), "|D|",len(DE), "overlap",len(TE&DE))
if cur==0:
    G=list(map(tuple,DE|TE))
    I=list(map(tuple,DE)); J=list(map(tuple,TE))
    assert planar(I) and planar(J)
    assert all(not planar(I+[e]) for e in G if frozenset(e) not in DE)
    print("CERTIFIED: I maximal planar in G, |I|=30 < |J|=54; J edges:",sorted(tuple(sorted(e)) for e in J))
