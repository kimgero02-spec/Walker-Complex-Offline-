import networkx as nx, random, sys
from networkx.generators.atlas import graph_atlas_g
from b0lib import tau_h
def contract(G,e):
    u,v=e
    H=nx.contracted_nodes(G,u,v,self_loops=False)
    return nx.convert_node_labels_to_integers(nx.Graph(H))
stats={'contr_drop':{}, 'contr_rise':{}, 'edgedel_drop':{}, 'vdel_drop':{}, 'Xe_drop':{}, 'Xe_vs_contr':{}}
viol=[]
def bump(k,x): stats[k][x]=stats[k].get(x,0)+1
def test(G,tag):
    if G.number_of_edges()==0 or G.number_of_nodes()<2: return
    t=tau_h(G)
    for e in list(G.edges()):
        tc=tau_h(contract(G,e)); bump('contr_drop',t-tc); 
        if tc-t>=2: viol.append(('rise',tag,sorted(G.edges()),e,t,tc))
        if t-tc>=2: viol.append(('drop',tag,sorted(G.edges()),e,t,tc))
        H=G.copy();H.remove_edge(*e); bump('edgedel_drop',t-tau_h(H))
        tx=tau_h(G,remove=[e]); bump('Xe_drop',t-tx)
        bump('Xe_vs_contr',(tx-tc))   # lemma: tau(X_e)<=tau(G/e) so expect tx-tc<=0
    for v in list(G.nodes()):
        H=G.copy();H.remove_node(v); bump('vdel_drop',t-tau_h(H) if H.number_of_nodes() else 0)
for i,G in enumerate(graph_atlas_g()):
    if G.number_of_nodes()>=2: test(G,('atlas',i))
print("ATLAS",stats); 
random.seed(1)
for n in (8,9):
    for k in range(60):
        p=random.choice([0.3,0.5,0.7]); G=nx.gnp_random_graph(n,p,seed=random.randint(0,10**9)); test(G,('gnp',n,p))
print("ALL",stats); print("VIOLATIONS",len(viol)); 
for v in viol[:5]: print(v)
