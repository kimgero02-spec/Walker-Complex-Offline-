# W: which outer patterns (x,y,z) in {T,S}^3 admit T bipartite + S 2-choosable (uni / ert)
from common import *
w=W(); V=list(w)
for mode in ['forest','uni','ert']:
    pats={}
    for bits in itertools.product([0,1],repeat=len(V)):
        S=[v for v,b in zip(V,bits) if b]; T=[v for v,b in zip(V,bits) if not b]
        if not nx.is_bipartite(w.subgraph(T)): continue
        if mode=='forest':
            if not nx.is_forest(w.subgraph(S)) : continue
        elif bad_cores(w,S,mode): continue
        key=''.join('S' if v in S else 'T' for v in 'xyz')
        pats.setdefault(key,[]).append(sorted(S,key=str))
    print(mode,{k:len(v) for k,v in sorted(pats.items())})
    if mode!='forest' and 'SST' in pats: print('  example SST:',pats['SST'][:3])
