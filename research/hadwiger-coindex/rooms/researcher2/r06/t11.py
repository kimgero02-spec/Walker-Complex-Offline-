import sys, time
sys.path.insert(0,'.')
from graphs import *
from homol import *
from pi1 import *
from t10 import complex_parts
for name,(n,adj) in [('C9^3', circulant(9,[1,2,3])), ('C8^3', circulant(8,[1,2,3])), ('C11^3', circulant(11,[1,2,3]))]:
    t=time.time()
    print(name, 'H~(N;F2)', betti_gf2(neighborhood_complex(n, adj)), 'time %.1f'%(time.time()-t), flush=True)
