import sys,random
sys.path.insert(0,'.')
from r4_blowup import *
def myc(G):
    n=G.number_of_nodes(); H=nx.Graph(G)
    for v in list(G.nodes()):
        H.add_edge(('u',v),'w')
        for x in G[v]: H.add_edge(('u',v),x)
    return nx.convert_node_labels_to_integers(H)
def max_k2t(G):
    # 두 정점의 최대 공통이웃 수
    best=0
    for u in G:
        for v in G:
            if u<v: best=max(best,len(set(G[u])&set(G[v])))
    return best
def search(G,m,iters=2000):
    V,idx,nb,T=types2(G); n=len(V); w=omega(G)
    o=list(range(n)); random.shuffle(o); cur=Dsigma(n,T,o,m)[0]
    for _ in range(iters):
        i,j=random.sample(range(n),2); o2=o[:]; o2[i],o2[j]=o2[j],o2[i]
        v=Dsigma(n,T,o2,m)[0]
        if v<=cur: o,cur=o2,v
    return cur+1,m*w,len(T)
random.seed(3)
gr=myc(nx.cycle_graph(5)); print("Grotzsch 최대 공통이웃",max_k2t(gr),"omega",omega(gr))
for m in (1,2,3): print(" m=",m,"탐색 상계, m*omega, 타입수",search(gr,m,1500))
cl=nx.convert_node_labels_to_integers(nx.from_edgelist([(i,j) for i in range(16) for j in range(i+1,16) if bin(i^j).count('1') in (1,4)]))
print("Clebsch deg",set(dict(cl.degree()).values()),"최대 공통이웃",max_k2t(cl),"omega",omega(cl))
mk=nx.LCF_graph(16,[5,-5],8); print("Mobius-Kantor n=",mk.number_of_nodes(),"공통이웃",max_k2t(mk),"omega",omega(mk))
# 삼각형 없고 K_{2,3} 포함하는 비이분 그래프: C5 의 독립집합 3개 블로업 일부
G=nx.Graph()
for i in range(5):
    for a in range(3):
        for b in range(3): G.add_edge((i,a),((i+1)%5,b))
G=nx.convert_node_labels_to_integers(G); print("C5[3K1] n=",G.number_of_nodes(),"공통이웃",max_k2t(G),"omega",omega(G))
