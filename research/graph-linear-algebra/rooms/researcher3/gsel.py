from descent import *
import sys
def S_units(S):
    gens=[-1]+list(S); out=[]
    for bits in itertools.product([0,1],repeat=len(gens)):
        r=1
        for b,g in zip(bits,gens):
            if b: r*=g
        out.append(r)
    return out
def selmer(th,verbose=False):
    S=primes_S(th); places=[0]+S
    imgs={v:kummer_image(th,v)[0] for v in places}
    U=S_units(S); res=[]; kerglob=[]
    for d1 in U:
        for d2 in U:
            d3=squarefree(d1*d2)
            delta=(d1,d2,d3)
            ker=all(isotropic_class(th,delta,v) for v in places)
            kerglob.append((delta,ker))
            if all(clsvec(delta,v) in imgs[v] for v in places): res.append(delta)
    return S,res,[d for d,k in kerglob if k]
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def issq(x):
    x=Fraction(x)
    if x<=0: return False
    return isqrt(x.numerator)**2==x.numerator and isqrt(x.denominator)**2==x.denominator
def solve_isometry(lam,R=12):
    """rational matrix with columns s_i, s_i^T A s_j = lam_i delta_ij (isometry D -> A)"""
    rng=range(-R,R+1)
    cand=[v for v in itertools.product(rng,repeat=3) if v!=(0,0,0) and qA(v)!=0 and issq(Fraction(qA(v))/lam[0])]
    cand.sort(key=lambda v:sum(abs(x) for x in v))
    for s1 in cand[:300]:
        w=matvec(A,s1)
        # basis of w-orthogonal lattice (rational): u1=cross(w,e_i), pick two independent
        us=[cross(w,e) for e in [(1,0,0),(0,1,0),(0,0,1)]]
        us=[u for u in us if any(u)]
        u1=us[0]; u2=next(u for u in us[1:] if any(cross(u1,u)))
        for x in range(-R,R+1):
            for y in range(-R,R+1):
                if (x,y)==(0,0): continue
                s2=tuple(x*u1[i]+y*u2[i] for i in range(3))
                q2=qA(s2)
                if q2!=0 and issq(Fraction(q2)/lam[1]):
                    s3=cross(w,matvec(A,s2))
                    q3=qA(s3)
                    if q3!=0 and issq(Fraction(q3)/lam[2]):
                        cols=[]
                        for s,q,l in [(s1,qA(s1),lam[0]),(s2,q2,lam[1]),(s3,q3,lam[2])]:
                            r=Fraction(q)/l
                            rn=Fraction(isqrt(r.numerator),isqrt(r.denominator))
                            cols.append([sp.Rational(c)/sp.Rational(rn.numerator,rn.denominator) for c in s])
                        return sp.Matrix(cols).T
    return None
def M_from_delta(th,delta,R=10):
    lam=[Fraction(-2*delta[i],fp(th,i)) for i in range(3)]
    S=solve_isometry(lam,R)
    if S is None: return None
    Th=sp.diag(*th)
    N=S*Th*S.inv()
    M=sp.Matrix(A)*N
    assert M==M.T
    return M
def delta_of_M(th,M):
    """d_i = -2 qA(v_i) f'(th_i) mod squares, v_i eigenvector of A^{-1}M"""
    out=[]
    Aq=sp.Matrix(A)
    for i in range(3):
        K=(th[i]*Aq-M).nullspace()
        assert len(K)==1
        v=K[0]; q=(v.T*Aq*v)[0]
        out.append(sqf_frac(Fraction(int(q.p),int(q.q))*(-2)*fp(th,i)))
    return tuple(out)
def quartic_int(M):
    c=quartic([[Fraction(int(M[i,j].p),int(M[i,j].q)) for j in range(3)] for i in range(3)])
    den=1
    for x in c: den=den*Fraction(x).denominator//gcd(den,Fraction(x).denominator)
    return [int(x*den*den) for x in c]
if __name__=="__main__":
    th=tuple(int(x) for x in sys.argv[1:4])
    S,sel,ker=selmer(th)
    print("theta",th,"S",S,"|Sel2|",len(sel),"|global ker|",len(ker))
    print("Sel2",sel)
    places=[0]+S
    import time
    for delta in ker:
        t0=time.time()
        M=M_from_delta(th,delta)
        if M is None: print(delta,"no M found (search limit)"); continue
        assert delta_of_M(th,M)==tuple(delta) , (delta_of_M(th,M),delta)
        c=quartic_int(M)
        sol=[solv_quartic(c,0 if v==0 else v) for v in places]
        print(delta,"in Sel:",delta in sel,"M-quartic solvable at",dict(zip(places,sol)),"M=",M.tolist(),"time %.1f"%(time.time()-t0),flush=True)
