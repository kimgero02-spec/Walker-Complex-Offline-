import sys; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def union_faces(Fs):
    U={}
    for F in Fs:
        for k,v in F.items(): U.setdefault(k,set()).update(v)
    return {k:sorted(v) for k,v in U.items()}
def test(name,n,sheets):
    E=set(); 
    for S in sheets: E|=set(tuple(sorted(e)) for e in S)
    full=B0_empty(make(n,list(E)),n)
    parts=[B0_empty(make(n,S),n) for S in sheets]
    U=union_faces(parts)
    bf=reduced_betti(full); bu=reduced_betti(U)
    nf=sum(len(v) for v in full.values()); nu=sum(len(v) for v in U.values())
    print(name,"X(G) betti",{k:v for k,v in bf.items() if v},"| union of sheets betti",{k:v for k,v in bu.items() if v},
          "| faces",nf,nu,flush=True)
C5=cyc(5); C5b=[e for e in itertools.combinations(range(5),2) if e not in C5]
test("K5=C5+C5bar",5,[C5,C5b])
oct_=[e for e in itertools.combinations(range(6),2) if e not in [(0,3),(1,4),(2,5)]]
test("K6=oct+PM",6,[oct_,[(0,3),(1,4),(2,5)]])
