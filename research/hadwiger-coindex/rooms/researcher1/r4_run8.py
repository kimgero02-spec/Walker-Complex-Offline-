import sys,random,time
sys.path.insert(0,'.')
from r4_blowup import *
cl=nx.convert_node_labels_to_integers(nx.from_edgelist([(i,j) for i in range(16) for j in range(i+1,16) if bin(i^j).count('1') in (1,4)]))
t=time.time(); V,idx,nb,T=types2(cl); n=16
print("Clebsch 극대 타입",len(T),time.time()-t, "omega",omega(cl))
random.seed(2)
for m in (1,2,3):
    o=list(range(n)); random.shuffle(o)
    D=Dsigma(n,T,o,m)[0]
    ex=expand(n,m,T)
    d=D
    print("m=",m,"Dsigma",D,"=> tau<=",D+1,"; 전개된 쌍",len(ex),"정확 검증(maxchg,bad) with d=2m-1 (m>=2):",check_moment(n,m,ex,o,2*m-1 if m>1 else 2))
