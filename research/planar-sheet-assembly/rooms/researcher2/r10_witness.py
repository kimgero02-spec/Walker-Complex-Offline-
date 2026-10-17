# R10: explicit witness colourings for the two decisive examples (W9-split, Groetzsch-split)
import networkx as nx
from r10_wheel import cols, build, analyze
from r10_grotzsch import M, split
def witnesses(G):
    H=G.copy(); H.remove_edge('u','v'); CH=cols(H)
    need=[(x,p) for x in ('u','v') for p in H if p!=x]; ch=[]
    while need:
        b=max(CH,key=lambda c:sum(c[p]!=c[x] for x,p in need)); ch.append(b)
        need=[(x,p) for x,p in need if b[p]==b[x]]
    gc=cols(G)[0]
    return ch,gc,list(nx.node_disjoint_paths(H,'u','v')),H
print('Groetzsch edges',sorted(M.edges()))
for name,G in [('W9',build(9,(0,1,3,5),(2,4,6,7,8))),('Gr',split(M,10,(5,6,7),(5,8,9)))]:
    ch,gc,paths,H=witnesses(G)
    order=['u','v']+sorted(x for x in H if x not in('u','v'))
    print(name,'G-col',{k:gc[k]+1 for k in order})
    for c in ch: print(name,'H-wit',{k:c[k]+1 for k in order})
    print(name,'paths',paths)
    print(name,'G/e 3-col?',bool(cols(nx.contracted_nodes(G,'u','v',self_loops=False))))
    # vertex-deleted witnesses (minimality)
    print(name,'H-x allows c(u)=c(v):',all(any(c['u']==c['v'] for c in cols(H.subgraph([y for y in H if y!=x]))) for x in H if x not in('u','v')))
