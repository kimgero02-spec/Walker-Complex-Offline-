# R11: second-order white-point obstruction (omega==0 but no functor) on G = {u,1..5} (isolated vertices)
import sys,os,itertools; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from r09_check import *
U=({'u'},set())
def dec(nu,blocks): return [U]*nu+[(set(b),set()) for b in blocks]
obj={'D2':dec(2,['1','2','3','4','5']),'D3':dec(3,['12','3','4','5']),'X':dec(2,['13','2','4','5']),
     'Z':dec(1,['14','2','3','5']),'D1':dec(2,['123','4','5']),'Y':dec(2,['134','2','5'])}
def amap(src,tgt,umap):
    S,T=obj[src],obj[tgt]; nu=sum(1 for P in S if P[0]=={'u'}); mu=sum(1 for P in T if P[0]=={'u'})
    f=list(umap)
    for P in S[nu:]:
        f.append(next(j for j,Q in enumerate(T) if j>=mu and P[0]<=Q[0]))
    return tuple(f)
gens={'tau':('D2','D3',(0,1)),'sig':('D3','D1',(0,0,1)),'p':('D2','X',(0,0)),'q':('X','D1',(0,1)),
      'h':('X','Y',(0,1)),'t':('D2','Z',(0,0)),'s':('Z','Y',(0,))}
mor={k:(a,b,amap(a,b,u)) for k,(a,b,u) in gens.items()}
comp=lambda g,f:(mor[f][0],mor[g][1],tuple(mor[g][2][j] for j in mor[f][2]))
pi1,pi2=comp('sig','tau'),comp('q','p'); k1,k2=comp('h','p'),comp('s','t')
assert pi1==pi2 and k1==k2; mor['pi']=pi1; mor['kap']=k1
Ls={k:L(obj[a],obj[b],f)[2] for k,(a,b,f) in mor.items()}
for k in Ls: print(k,len(Ls[k]),sorted({str(F.get(('w','u'))) for F in Ls[k]}))
def cmp(F,G): return {x:F[G[x]] for x in G}
eq=lambda A,B: all(A[x]==B[x] for x in A)
cnt=0
for ch in itertools.product(*[range(len(Ls[k])) for k in mor]):
    c={k:Ls[k][i] for k,i in zip(mor,ch)}
    if eq(cmp(c['sig'],c['tau']),c['pi']) and eq(cmp(c['q'],c['p']),c['pi']) and \
       eq(cmp(c['h'],c['p']),c['kap']) and eq(cmp(c['s'],c['t']),c['kap']): cnt+=1
print('number of functorial choices:',cnt)
def im(g,f): return {str(cmp(G,F)[('w','u')]) for F in Ls[f] for G in Ls[g]}
print('pi via (sig,tau):',im('sig','tau'),' via (q,p):',im('q','p'))
print('kap via (h,p):',im('h','p'),' via (s,t):',im('s','t'))
