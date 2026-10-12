# R48 gadget: components, essential half G0, and a connected variant (one sheet-internal edge added)
import networkx as nx, itertools
import os; _TOPIC=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # hadwiger-coindex/
exec(open(os.path.join(_TOPIC,'master','verify_R48_gadget.py')).read().split('order=')[0])
print("components:",[len(c) for c in nx.connected_components(G)])
G0=G.subgraph(nx.node_connected_component(G,'v1')).copy()
print("G0 n,m",G0.number_of_nodes(),G0.number_of_edges(),"contains K6 on v1,v2,v3,p,q,r:",
      all(G0.has_edge(x,y) for x,y in itertools.combinations(['v1','v2','v3',p,q,r],2)))
def col(H,k,allowed):
    order=sorted(H,key=lambda v:-H.degree(v)); c={}
    def bt(i):
        if i==len(order): return True
        v=order[i]
        for x in allowed(v):
            if x<k and all(c.get(u)!=x for u in H[v]):
                c[v]=x
                if bt(i+1): return True
                del c[v]
        return False
    return bt(0)
Gc=G.copy(); Gc.add_edge('as','w4')   # sheet-1 internal edge joining A and Q1 (outer faces)
print("connected variant: connected",nx.is_connected(Gc),"sheet1 planar",nx.check_planarity(Gc.subgraph(V1))[0])
print(" 6-col",col(Gc,6,lambda v:range(6)),
      " V1 in 4 cols:",col(Gc,6,lambda v:range(4) if v in V1 else range(6)),
      " V2 in 4 cols:",col(Gc,6,lambda v:range(4) if v in V2 else range(6)))
