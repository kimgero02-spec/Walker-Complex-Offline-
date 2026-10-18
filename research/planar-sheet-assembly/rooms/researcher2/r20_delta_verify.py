# r20_d_*.txt 인증서 독립 검산: 정확 분해, 평면, chi/omega, sigma=N, Delta.
import ast, itertools, sys, networkx as nx
from r19_lib import chi, omega
for fn in sys.argv[1:]:
    L=open(fn).read().splitlines()
    if not L or not L[0].startswith('N '): print(fn,"결과 없음"); continue
    N=int(L[0].split()[1]); P=[nx.Graph(E) for E in ast.literal_eval(L[1])]
    for G in P: G.add_nodes_from(range(N))
    cnt={}
    for G in P:
        for e in G.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    ex=set(cnt)==set(frozenset(e) for e in itertools.combinations(range(N),2)) and all(c==1 for c in cnt.values())
    ch=[chi(G) for G in P]; om=[omega(G) for G in P]
    print(fn,"N=",N,"정확=",ex,"평면=",all(nx.check_planarity(G)[0] for G in P),"chi=",ch,"omega=",om,
          "sigma=",sum(ch),"Delta=",sum(c>w for c,w in zip(ch,om)),"floor(N/3)=",N//3)
