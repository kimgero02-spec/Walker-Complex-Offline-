# R10: decisive example W7 hub split: rim 0..6, u~0,1,3 ; v~2,4,5,6 ; e=uv
import itertools, networkx as nx
from r10_wheel import cols, analyze, build
G=build(7,(0,1,3),(2,4,5,6)); H=G.copy(); H.remove_edge('u','v')
print(analyze(G))
CG=cols(G); print('a G coloring', CG[0])
CH=cols(H)
for x in ('u','v'):
    for p in H:
        if p==x: continue
        w=next(c for c in CH if c[p]!=c[x]); 
print('u-v 3 disjoint paths', [p for p in nx.node_disjoint_paths(H,'u','v')])
print('min u-v cuts size3:', [set(S) for S in nx.all_node_cuts(H) ])
# vertex-deleted: c(u)=c(v) possible?
for i in range(7):
    Hi=H.copy(); Hi.remove_node(i)
    print(i, any(c['u']==c['v'] for c in cols(Hi)))
# explicit witnesses: small set of H-colorings separating u (resp v) from every other vertex
need=[(x,p) for x in ('u','v') for p in H if p!=x]
chosen=[]
while need:
    best=max(CH,key=lambda c:sum(c[p]!=c[x] for x,p in need))
    chosen.append(best); need=[(x,p) for x,p in need if best[p]==best[x]]
for c in chosen: print({k:c[k]+1 for k in ['u','v',0,1,2,3,4,5,6]})
# H8/e vs Moser spindle
H8=nx.Graph([('x','y'),('v','x'),('v','y'),('r','x'),('r','y'),("x'","y'"),('u',"x'"),('u',"y'"),('p',"x'"),('p',"y'"),('r','p'),('u','v')])
M=nx.contracted_nodes(H8,'u','v',self_loops=False)
mos=nx.Graph([(0,1),(0,2),(1,2),(1,3),(2,3),(0,4),(0,5),(4,5),(4,6),(5,6),(3,6)])
print('H8/e ~ Moser', nx.is_isomorphic(M,mos))
