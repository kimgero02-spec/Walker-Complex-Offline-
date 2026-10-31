import sys, time
sys.path.insert(0,'.')
import numpy as np
from fractions import Fraction as F
from graphs import *
from exactsep import *
Y = np.load('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/C5K3_d5.npy')
n, adj = lex_blowup(5, cycle(5)[1], 3)
pairs = maximal_pairs(n, adj)
for D in (10, 100, 1000):
    Yq = [tuple(int(round(float(x)*D)) for x in row) for row in Y]
    b = bad_pairs_d(n, adj, Yq, pairs)
    print('scale', D, 'bad pairs', len(b), flush=True)
