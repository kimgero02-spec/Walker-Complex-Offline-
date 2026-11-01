import networkx as nx, itertools, time, random
from n1_zig import zig_le
from n1_hom import hom_map
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
t0=time.time(); seen=set(); res=[]
for n in range(8,14):
    for r in (2,3):
        for ks in itertools.combinations(range(1,n//2+1),r):
            G=circ(n,ks)
            if not nx.is_connected(G): continue
            z=2
            while not zig_le(G,z): z+=1
            if z<4: continue
            if G.number_of_edges()*2**0 > 60: pass
            k=2
            while k<z and not hom_map(G,k)[0]: k+=1
            xi1=k+1 if k<z else z
            res.append((n,ks,z,xi1))
            print(n,ks,'zig',z,'xi+1<=',xi1,round(time.time()-t0,1),flush=True)
            if time.time()-t0>200: raise SystemExit
