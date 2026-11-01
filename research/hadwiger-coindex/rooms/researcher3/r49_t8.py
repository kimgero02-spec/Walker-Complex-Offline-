from r49_tube import *
import itertools
p,q,r,s,P,Q_,R=range(7); v1,v2,v3,v4=7,8,9,10
U=nx.Graph()
U.add_edges_from(itertools.combinations([p,q,r,s],2))
U.add_edges_from([(P,q),(P,r),(P,s),(Q_,p),(Q_,r),(Q_,s),(R,p),(R,q),(R,s)])
U.add_edges_from(itertools.combinations([v1,v2,v3,v4],2))
U.add_edges_from([(v1,p),(v2,q),(v3,r),(v4,P),(v4,Q_),(v4,R)])
for sd in range(10):
    g,rot=free_genus_search(U,iters=100000,seed=sd,target=1)
    if g==1:
        print('g(U)=1 found, seed',sd, 'tube_info',tube_info(rot,range(7))); break
else: print('not found')
