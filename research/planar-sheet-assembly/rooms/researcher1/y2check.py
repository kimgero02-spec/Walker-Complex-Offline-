# 반례꾼 Y2 (R02-researcher2-interim) 를 정리 N2 판정기로 독립 확인
from n2 import n2_test, cyc
C0=['u1','m1','w1','g1','u2','m2','w2','g2']; P0=cyc(C0)+[('u1','z'),('z','u2')]
CQ=['u1','m1','w1','p','w2','m2','u2','q']; PQ=cyc(CQ)+[('y','u1'),('y','w1')]
print(n2_test([(P0,C0),(PQ,CQ)],"Y2 (r2)"))
