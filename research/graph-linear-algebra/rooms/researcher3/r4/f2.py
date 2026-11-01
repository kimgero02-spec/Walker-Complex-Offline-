exec(open('f.py').read().split("f=-(t+1)")[0])
f=-(t+1)*(4*t**2+t-1); g=(2*t+1)*(4*t**2+2*t-1); D=sp.expand(f*g)
print(sp.Poly(D,t).all_coeffs())
for p in [7,11,13]:
    N1,N2=counts(D,p); print(p,N1,N2, p+1-N1)
    # brute force F_p points
    c=[int(v)%p for v in sp.Poly(D,t).all_coeffs()]
    n=0
    for a in range(p):
        v=0
        for co in c: v=(v*a+co)%p
        n+= sum(1 for y in range(p) if (y*y-v)%p==0)
    print(' affine brute',n, 'inf',N1-n)
