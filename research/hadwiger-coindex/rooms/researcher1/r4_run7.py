import sys,random
sys.path.insert(0,'.')
from r4_blowup import *
def cn2(n):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for d in (1,2): G.add_edge(i,(i+d)%n)
    return G
G=cn2(9); V,idx,nb,T=types2(G); n=9
for m in (1,2):
    br=brute(G,m); ex=expand(n,m,T)
    d=3*m-1 if m>1 else 2
    print("C_9^2 m=",m,"brute==types",br==ex,len(br),"natural order exact (maxchg,bad), d=",d,check_moment(n,m,br,list(range(n)),d))
# Grotzsch m=2 (22 정점)
def myc(G):
    H=nx.Graph(G)
    for v in list(G.nodes()):
        H.add_edge(('u',v),'w')
        for x in G[v]: H.add_edge(('u',v),x)
    return nx.convert_node_labels_to_integers(H)
gr=myc(nx.cycle_graph(5)); n=11
V,idx,nb,T=types2(gr)
o=list(range(n)); random.seed(5); random.shuffle(o)
print("Grotzsch random order Dsigma(2)",Dsigma(n,T,o,2)[0])
br=brute(gr,2); ex=expand(n,2,T)
print("Grotzsch[K2] brute==types",br==ex,len(br),"exact (maxchg,bad) d=3:",check_moment(n,2,br,o,3))
