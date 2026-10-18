import sys; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def zz(n,E): return zig(make(n,E),n)
C5=cyc(5); C5b=[e for e in itertools.combinations(range(5),2) if e not in C5]
print("C5 zig",zz(5,C5),"C5bar zig",zz(5,C5b),"K5 zig",zz(5,list(itertools.combinations(range(5),2))))
oct_=[e for e in itertools.combinations(range(6),2) if e not in [(0,3),(1,4),(2,5)]]
PM=[(0,3),(1,4),(2,5)]
print("PM zig",zz(6,PM),"oct zig",zz(6,oct_))
