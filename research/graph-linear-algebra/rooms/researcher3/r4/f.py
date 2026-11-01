import sympy as sp
x=sp.symbols('x'); t=sp.symbols('t')
def counts(fpoly,p):
    c=[int(v)%p for v in sp.Poly(fpoly,t).all_coeffs()]  # descending
    deg=len(c)-1
    def chi1(v):
        v%=p
        if v==0: return 0
        return 1 if pow(v,(p-1)//2,p)==1 else -1
    N1=0
    for a in range(p):
        v=0
        for co in c: v=(v*a+co)%p
        N1+=1+chi1(v)
    if deg%2==1: N1+=1
    else: N1+=1+chi1(c[0])
    # F_p^2 = F_p[s]/(s^2-d)
    d=next(k for k in range(2,p) if chi1(k)==-1)
    def mul(u,v): return ((u[0]*v[0]+d*u[1]*v[1])%p,(u[0]*v[1]+u[1]*v[0])%p)
    def pw(u,e):
        r=(1,0)
        while e:
            if e&1: r=mul(r,u)
            u=mul(u,u); e>>=1
        return r
    N2=0
    for a in range(p):
        for b in range(p):
            v=(0,0); z=(a,b)
            for co in c: v=mul(v,z); v=((v[0]+co)%p,v[1])
            if v==(0,0): N2+=1
            else: N2+= 1+ (1 if pw(v,(p*p-1)//2)==(1,0) else -1)
    if deg%2==1: N2+=1
    else:
        lc=(c[0]%p,0); N2+=1+(1 if pw(lc,(p*p-1)//2)==(1,0) else -1)
    return N1,N2
def lpoly(fpoly,p):
    N1,N2=counts(fpoly,p); c1=N1-p-1; c2=(c1**2-(p*p+1-N2))//2
    return N1,N2,c1,c2
f=-(t+1)*(4*t**2+t-1); g=(2*t+1)*(4*t**2+2*t-1)
D=sp.expand(f*g)
print('f',sp.factor(f),'g',sp.factor(g),'D disc',sp.factorint(sp.discriminant(D,t)))
for p in [5,7,11,13,17]:
    a=p+1-counts(f,p)[0]; b=p+1-counts(g,p)[0]
    N1,N2,c1,c2=lpoly(D,p)
    h=sp.Poly(x**4+c1*x**3+c2*x**2+p*c1*x+p**2,x)
    print(p,'a_E_G',a,'a_E_H',b,'sum',a+b,' tr J(D)=',-c1,' charpoly',h.as_expr(),'irreducible over Q:',sp.Poly(h).is_irreducible if hasattr(sp.Poly(h),'is_irreducible') else None, sp.factor_list(h.as_expr())[1].__len__())
print('--- test')
for p in [7,11]:
    for h in [f,g]:
        N1,N2=counts(h,p); a=p+1-N1; print(p,N1,N2,'expected N2',p*p+1-(a*a-2*p))
