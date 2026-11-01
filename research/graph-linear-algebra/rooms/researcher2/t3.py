from orb import *
import itertools
def det_mod(M,p):
    n=len(M);M=[list(r) for r in M];d=1
    for c in range(n):
        piv=None
        for r in range(c,n):
            if M[r][c]%p: piv=r;break
        if piv is None: return 0
        if piv!=c: M[c],M[piv]=M[piv],M[c];d=-d
        d=d*M[c][c]%p; inv=pow(M[c][c],p-2,p)
        for r in range(c+1,n):
            f=M[r][c]*inv%p
            M[r]=[(M[r][k]-f*M[c][k])%p for k in range(n)]
    return d%p
def comm_units(n,perms,p):
    # orbital basis
    seen={};orb=[]
    for i in range(n):
        for j in range(n):
            if (i,j) in seen: continue
            o={(s[i],s[j]) for s in perms}
            for x in o: seen[x]=len(orb)
            orb.append(o)
    basis=[tuple(tuple(1 if (i,j) in o else 0 for j in range(n)) for i in range(n)) for o in orb]
    units=[]
    for co in itertools.product(range(p),repeat=len(basis)):
        M=tuple(tuple(sum(co[k]*basis[k][i][j] for k in range(len(basis)))%p for j in range(n)) for i in range(n))
        if det_mod(M,p): units.append(M)
    return len(basis),units
def aut_perms(n,adj):
    return [s for s in itertools.permutations(range(n)) if all(adj[i][j]==adj[s[i]][s[j]] for i in range(n) for j in range(n))]
C4=[[1 if (i-j)%4 in (1,3) else 0 for j in range(4)] for i in range(4)]
P3=[[1 if abs(i-j)==1 else 0 for j in range(3)] for i in range(3)]
K3=[[1 if i!=j else 0 for j in range(3)] for i in range(3)]
for name,adj,n in [("P3",P3,3),("K3",K3,3),("C4",C4,4)]:
  ps=aut_perms(n,adj)
  for q in (3,5):
    if n==4 and q==5: 
        pass
    d,U=comm_units(n,ps,q)
    for m in (1,2):
        if q**(n*m)>2*10**6: continue
        print(name,"|Aut|",len(ps),"dim comm",d,"q",q,"#units",len(U),"m",m,"orbits",orbits(n,m,q,U))
