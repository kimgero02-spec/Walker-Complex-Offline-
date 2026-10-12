from r49_ladder import *
G=nx.complete_graph(8); r=search(G,range(4),3)
print('K8=K4+K4 3 tubes ->', None if r is None else (r['pairs'],[len(l) for l in r['ladders']],r['info'],r['ladders']))
