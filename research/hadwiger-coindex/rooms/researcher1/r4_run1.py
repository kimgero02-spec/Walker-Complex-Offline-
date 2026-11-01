import sys,random
sys.path.insert(0,'.')
from r4_blowup import *
G=nx.petersen_graph(); G=nx.convert_node_labels_to_integers(G)
V,idx,nb,T=types(G); n=len(V)
print("Petersen 타입 수",len(T),"omega",omega(G))
from collections import Counter
print(Counter((len(bits(X,n)),len(bits(Y,n)),len(bits(Z,n))) for X,Y,Z in T))
for m in (1,2):
    ex=expand(n,m,T)
    if m==2:
        br=brute(G,m)
        print("m=",m,"타입 전개",len(ex),"brute",len(br),"일치",ex==br)
    else:
        br=brute(G,m); print("m=1 타입",len(ex),"brute",len(br),ex==br)
    d=m*omega(G)-1
    for trial in range(3):
        order=list(range(n)); random.shuffle(order)
        print(" order",order,"d=",d,"exact check (maxchg,bad)=",check_moment(n,m,br,order,d), "Dsigma",Dsigma(n,T,order,m)[0])
