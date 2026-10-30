# B, C = greedy maximal planar subgraphs inside allowed cross pairs u_i v_j, |i-j|>=2 (mod k).
import random, sys
from r20_prism import planar, prism, norm, frozen, thick2
k=int(sys.argv[1]); T=int(sys.argv[2]); rng=random.Random(int(sys.argv[3]))
A=[norm(e) for e in prism(k)]
allowed=[norm((('u',i),('v',j))) for i in range(k) for j in range(k) if min((i-j)%k,(j-i)%k)>=2]
def greedy(pool):
    S=[]; p=pool[:]; rng.shuffle(p)
    for e in p:
        if planar(S+[e]): S.append(e)
    return S
best=None
for t in range(T):
    B=greedy(allowed)
    if not all(not planar(B+[e]) for e in A): continue
    rest=[e for e in allowed if e not in set(B)]
    for t2 in range(20):
        C=greedy(rest)
        cl=[A,B,C]
        if frozen(cl):
            E=A+B+C
            print("frozen found t=",t,"|A|,|B|,|C|=",len(A),len(B),len(C),"N=",2*k)
            P=thick2(E,rng,3000)
            if P:
                assert planar(P[0]) and planar(P[1]) and set(P[0])|set(P[1])==set(E) and not planar(E)
                print("THICKNESS-2 CERTIFICATE"); print("A=",A);print("B=",B);print("C=",C);print("T1=",P[0]);print("T2=",P[1]); sys.exit()
            else: print(" greedy found no thickness-2 cover")
print("done")
