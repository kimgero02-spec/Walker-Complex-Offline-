# R22 researcher3: one-vertex extensions of Moser spindle and C7^2 (omega<=3), H^3(Q;F2) and zig.
import sys, io, contextlib, itertools
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
    from r06_lib import make, zig
def omega(n,E):
    S=set(map(frozenset,E)); best=1
    for k in range(2,n+1):
        for c in itertools.combinations(range(n),k):
            if all(frozenset((a,b)) in S for a,b in itertools.combinations(c,2)): best=k
            else: pass
    return best
def chi_ge4(n,E):
    # is G 3-colorable?
    adj=[set() for _ in range(n)]
    for a,b in E: adj[a].add(b); adj[b].add(a)
    col=[-1]*n
    def bt(i):
        if i==n: return True
        for c in range(3):
            if all(col[j]!=c for j in adj[i] if j<i):
                col[i]=c
                if bt(i+1): return True
        col[i]=-1
        return False
    return not bt(0)
moser=[(0,1),(0,2),(1,2),(1,3),(2,3),(0,4),(0,5),(4,5),(4,6),(5,6),(3,6)]
c72=[(i,(i+1)%7) for i in range(7)]+[(i,(i+2)%7) for i in range(7)]
bases={"moser":(7,moser),"C7sq":(7,c72)}
out=[]
for name,(n,E) in bases.items():
    cnt=0
    for r in range(0,n+1):
        for N in itertools.combinations(range(n),r):
            E2=E+[(v,n) for v in N]
            if omega(n+1,E2)>3: continue
            if not chi_ge4(n+1,E2): continue
            cnt+=1
            q=quotient_betti(n+1,E2)
            if q.get(3,0)==0:
                out.append((name,N,q))
    print(name,"valid extensions (omega<=3, chi>=4):",cnt, flush=True)
print("H3(Q)=0 extensions:", len(out))
for name,N,q in out[:30]:
    print(name, N, q, flush=True)
