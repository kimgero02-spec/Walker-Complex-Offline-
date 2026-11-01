# R48 22 정점 가젯: 경계, 유효 지지 (x=6), 유효 계수
from lib import *
import networkx as nx, numpy as np, time
def apollo(o):
    p,q,r,s,P,Q,R=[o+i for i in range(7)]
    return [(p,q),(p,r),(p,s),(q,r),(q,s),(r,s),(P,q),(P,r),(P,s),(Q,p),(Q,r),(Q,s),(R,p),(R,q),(R,s)]
def k4(o): return [(o+i,o+j) for i in range(4) for j in range(i+1,4)]
def gadget(A,Q):
    p,q,r,s,P,Qq,R=[A+i for i in range(7)]
    return [(x,Q+i) for i in range(3) for x in (p,q,r)]+[(x,Q+3) for x in (P,Qq,R)]
B1=nx.Graph(apollo(0)+k4(7)); B2=nx.Graph(apollo(11)+k4(18))
H=gadget(0,18)+gadget(11,7)
W1=sorted({u for u,v in H if u<11}|{v for u,v in H if v<11}); W2=sorted({u for u,v in H if u>=11}|{v for u,v in H if v>=11})
print('W1',W1,'W2',W2)
def indep_partitions(B,W,maxb):
    W=list(W); out=[]
    def rec(i,blocks):
        if i==len(W): out.append([list(b) for b in blocks]); return
        v=W[i]
        for b in blocks:
            if all(not B.has_edge(v,w) for w in b):
                b.append(v); rec(i+1,blocks); b.pop()
        if len(blocks)<maxb:
            blocks.append([v]); rec(i+1,blocks); blocks.pop()
    rec(0,[]); return out
x=6
for name,B,W in (('B1',B1,W1),('B2',B2,W2)):
    ip=indep_partitions(B,W,99); ip6=[p for p in ip if len(p)<=6]
    sup=[p for p in ip6 if atilde(B,W,p,6)>0]
    print(name,'|W|',len(W),'Bell',115975,'indep partitions',len(ip),'(<=6 blocks)',len(ip6),'support@6',len(sup),
          'block counts in support',sorted({len(p) for p in sup}))
    if name=='B1': I1,S1=ip,sup
    else: I2,S2=ip,sup
def rank_np(M,p=2147483629):
    A=np.array(M,dtype=object)%p; A=A.astype(np.int64); r=0; n,m=A.shape
    for c in range(m):
        piv=np.nonzero(A[r:,c])[0]
        if len(piv)==0: continue
        k=r+piv[0]; A[[r,k]]=A[[k,r]]
        inv=pow(int(A[r,c]),p-2,p); A[r]=(A[r]*inv)%p
        f=A[:,c].copy(); f[r]=0
        A=(A-(f[:,None]*A[r][None,:])%p)%p
        r+=1
        if r==n: break
    return r
t=time.time()
M6=[[M_entry(pi,rho,H,6) for rho in S2] for pi in S1]
print('effective M@6 size',len(S1),len(S2),'nonzero entries',sum(1 for row in M6 for v in row if v),'rank@6',rank_np(M6),round(time.time()-t,1))
a1=[atilde(B1,W1,p,6) for p in S1]; a2=[atilde(B2,W2,p,6) for p in S2]
P6=sum(a1[i]*M6[i][j]*a2[j] for i in range(len(S1)) for j in range(len(S2)))
print('P_G(6) via bilinear =',P6)
pos=[(len(S1[i]),len(S2[j])) for i in range(len(S1)) for j in range(len(S2)) if M6[i][j]]
import collections; print('block-count pairs (|pi|,|rho|) with M>0:',sorted(collections.Counter(pos).items()))
print('P_G(5) via bilinear =',bilinear(B1,W1,B2,W2,H,5,[p for p in I1 if len(p)<=5],[p for p in I2 if len(p)<=5]))
