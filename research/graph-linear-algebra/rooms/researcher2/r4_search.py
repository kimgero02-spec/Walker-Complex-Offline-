import sys,random
from r4lib import *
random.seed(1)
def connected(A):
    n=len(A);seen={0};st=[0]
    while st:
        u=st.pop()
        for v in range(n):
            if A[u][v] and v not in seen: seen.add(v);st.append(v)
    return len(seen)==n
found=[]
seenkeys=set()
for n in (4,5,6):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    for mask in range(1<<len(edges)):
        es=[edges[k] for k in range(len(edges)) if mask>>k&1]
        if len(es)<n: continue   # need a cycle
        A=[[0]*n for _ in range(n)]
        for i,j in es: A[i][j]=A[j][i]=1
        if not connected(A): continue
        key=(n,tuple(sorted(sum(r) for r in A)),)
        P=PG(A)
        k2=(n,tuple(P.all_coeffs()))
        if k2 in seenkeys: continue
        seenkeys.add(k2)
        g=gab(P)
        if g==0: continue
        # try signatures (random few)
        for trial in range(6):
            sig={e:random.choice([1,-1]) for e in es}
            H,S=signed_cover(A,sig)
            # H connected?
            if not connected(H.tolist()): continue
            PH=PG(H.tolist())
            assert (PH.as_expr()/P.as_expr()).simplify().is_polynomial(t)
            gh=gab(PH)
            if gh<g:
                found.append((n,es,sig,g,gh)); print(n,es,sig,'gG',g,'gH',gh,flush=True); break
        if len(found)>=3: sys.exit()
print('done',len(seenkeys),len(found))
