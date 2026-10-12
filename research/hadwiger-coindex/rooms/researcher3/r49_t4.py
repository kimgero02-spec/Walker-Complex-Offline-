from r49_ladder import *
import sys
for (a,b,t) in [(3,3,2),(4,3,2),(4,4,3)]:
    G=nx.complete_graph(a+b); r=search(G,range(a),t)
    print('K%d=K%d+K%d tubes'%(a+b,a,b),t,'->', None if r is None else (r['pairs'],[len(l) for l in r['ladders']],r['info']))
