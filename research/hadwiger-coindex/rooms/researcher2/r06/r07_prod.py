# R07 반례꾼: 곱 법칙 zig(G1∪G2) <= zig(G1) zig(G2) 의 원형 시험. K_n = C_n(S1) ∪ C_n(S2) 분할 (거리 집합 분할).
import sys, time
sys.path.insert(0,'.')
from graphs import *
from r07_check import kn
def cir(n, S): return circulant(n, S)
for n, S1, S2 in [(10, [1,2], [3,4,5]), (9, [1,2], [3,4]), (11, [1,2], [3,4,5])]:
    t=time.time()
    g1 = cir(n, S1); g2 = cir(n, S2)
    z1 = zig(*g1)[0]; z2 = zig(*g2)[0]
    print('n',n,'S1',S1,'zig',z1,'omega',clique_number(*g1),'| S2',S2,'zig',z2,'omega',clique_number(*g2),'| zig(K_n)=',n,'product',z1*z2, 'time %.1f'%(time.time()-t), flush=True)
