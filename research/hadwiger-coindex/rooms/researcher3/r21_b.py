import sys, io, contextlib, itertools
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r21_scan import rep
C5=[(i,(i+1)%5) for i in range(5)]
rep("C5+Kbar2", 7, C5+[(i,5) for i in range(5)]+[(i,6) for i in range(5)])
moser=[(0,1),(0,2),(1,2),(1,3),(2,3),(0,4),(0,5),(4,5),(4,6),(5,6),(3,6)]
rep("Moser spindle", 7, moser)
rep("C7(1,3)", 7, [(i,(i+1)%7) for i in range(7)]+[(i,(i+3)%7) for i in range(7)])
