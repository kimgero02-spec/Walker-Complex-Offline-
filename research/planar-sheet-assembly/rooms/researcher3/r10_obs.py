# R10: universal construction of the white-point obstruction. G=K4, u=0.
# pieces: S=star(u), U={u} (K1), rest = edges avoiding u (K2 each)
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from r09_check import *
S=({0,1,2,3},{(0,1),(0,2),(0,3)}); U=({0},set())
rest=[({1,2},{(1,2)}),({1,3},{(1,3)}),({2,3},{(2,3)})]
D2=[S,U]+rest; D3=[S,U,U]+rest; D1=[S,U]+rest; D0=[S]+rest
tau=(0,1,3,4,5); sig=(0,0,1,2,3,4)        # D2->D3->D1
tau2=(0,0,1,2,3); sig2=(0,2,3,4)          # D2->D0->D1
pi=(0,0,2,3,4)
assert tuple(sig[t] for t in tau)==pi and tuple(sig2[t] for t in tau2)==pi
res={}
for name,(A,B,s) in dict(tau=(D2,D3,tau),sig=(D3,D1,sig),tau2=(D2,D0,tau2),sig2=(D0,D1,sig2),pi=(D2,D1,pi)).items():
    _,_,Ls=L(A,B,s); res[name]=Ls
    print(name,'|L|=',len(Ls),' images of w_0:',sorted({str(f.get(('w',0))) for f in Ls}))
cA={str(s[t[('w',0)]]) for t in res['tau'] for s in res['sig']}
cB={str(s[t[('w',0)]]) for t in res['tau2'] for s in res['sig2']}
print('via D3 forces',cA,'; via D0 forces',cB)
def eps(f): return {w[1]:(1 if f[w][0]=='w' else 0) for w in f if w[0]=='w'}
for (a,b) in [('tau','sig'),('tau2','sig2')]:
    for t in res[a]:
        for s in res[b]:
            comp={x:s[t[x]] for x in t}
            et,es,ec=eps(t),eps(s),eps(comp)
            assert {v:(et[v] and es.get(v,0)) for v in et}==ec
print('epsilon AND-rule holds on these pairs')
