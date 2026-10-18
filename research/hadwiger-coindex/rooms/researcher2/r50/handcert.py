# hand-structured FB+ certificate for G*: K4 S={a,b}, T={c,d}; copy1 uses even-unicyclic W-partition (pattern SST)
from common import *
w=W(); V=list(w)
def parts(pattern,mode):
    out=[]
    for bits in itertools.product([0,1],repeat=10):
        S=[v for v,b in zip(V,bits) if b]; T=[v for v,b in zip(V,bits) if not b]
        if ''.join('S' if v in S else 'T' for v in 'xyz')!=pattern: continue
        if not nx.is_bipartite(w.subgraph(T)): continue
        H=w.subgraph(S)
        if mode=='forest' and not nx.is_forest(H): continue
        if mode=='uni' and bad_cores(w,S,'uni'): continue
        out.append(set(S))
    return out
for pat in ['SST','STS','TTS','STT','TSS','TST']:
    P=parts(pat,'forest' if pat!='SST' else 'uni')
    print(pat, len(P), [sorted(s) for s in sorted(P,key=lambda s:(len(s),sorted(s)))[:2]])
