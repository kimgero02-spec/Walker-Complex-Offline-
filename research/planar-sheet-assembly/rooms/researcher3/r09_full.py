import sys, itertools; sys.path.insert(0,__import__('os').path.dirname(__file__))
from r09_check import manual
K2=({'u','v'},{('u','v')})
def all_morph(Mp,M):
    cand={x:[y for y in M['nodes'] if M['rho'](y)==M['rho'](x)] for x in Mp['nodes']}
    xs=Mp['nodes']; out=[]
    for ch in itertools.product(*[cand[x] for x in xs]):
        f=dict(zip(xs,ch)); ok=True
        for e in Mp['E']:
            a,b=tuple(e)
            if f[a]!=f[b] and frozenset([f[a],f[b]]) not in M['E']: ok=False;break
        if ok: out.append(f)
    return out
Mb=manual([K2,K2])
Ms=all_morph(Mb,Mb)
white_collapse=[f for f in Ms if all(f[x][0]=='w' for x in Mb['nodes'] if x[0]=='c')]
print('|End_Psi(M_b)|=',len(Ms),' copies->whites maps:',len(white_collapse))
for f in white_collapse: print({str(k):str(v) for k,v in f.items()})
