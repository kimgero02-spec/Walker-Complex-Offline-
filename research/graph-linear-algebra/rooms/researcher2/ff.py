import numpy as np, itertools, random
class Field:
    def __init__(s,q):
        s.q=q
        if q in (3,5,7,11,13):
            r=np.arange(q)
            s.ADD=((r[:,None]+r[None,:])%q).astype(np.int16)
            s.MUL=((r[:,None]*r[None,:])%q).astype(np.int16)
        elif q==9:  # F3[i], i^2=-1, element a+3b? use a+3*b encoding (a,b in 0..2)
            def dec(x): return (x%3,x//3)
            def enc(a,b): return (a%3)+3*(b%3)
            s.ADD=np.zeros((9,9),np.int16);s.MUL=np.zeros((9,9),np.int16)
            for x in range(9):
                for y in range(9):
                    a,b=dec(x);c,d=dec(y)
                    s.ADD[x,y]=enc(a+c,b+d); s.MUL[x,y]=enc(a*c-b*d,a*d+b*c)
        s.NEG=np.array([int(np.where(s.ADD[x]==0)[0][0]) for x in range(q)],np.int16)
        s.INV=np.array([0]+[int(np.where(s.MUL[x]==1)[0][0]) for x in range(1,q)],np.int16)
        s.char=3 if q==9 else q
        # integer embedding
        s.INT=[0]*(2*q)
        one=1
        for n in range(1,2*q): s.INT[n]=int(s.ADD[s.INT[n-1],one])
    def add(s,a,b): return s.ADD[a,b]
    def mul(s,a,b): return s.MUL[a,b]
    def neg(s,a): return s.NEG[a]
    def sub(s,a,b): return s.ADD[a,s.NEG[b]]
    def smul(s,n,a):  # integer n times array
        n=n%s.char
        return s.MUL[s.INT[n],a]
    def sq(s):
        return sorted(set(int(s.MUL[x,x]) for x in range(1,s.q)))
