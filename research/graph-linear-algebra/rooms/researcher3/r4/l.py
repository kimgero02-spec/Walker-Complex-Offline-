import sympy as sp
from c import IJ,jinv,t
fG=-(t+1)*(4*t**2+t-1)
E1=(1-t)*(16*t**2-9*t+1); E2=t*E1
for nm,f in [('E_G',fG),('E1',E1),('E2',E2)]:
    I,J=IJ(f); print(nm,I,J,jinv(f),sp.factorint(I) if I else 0, sp.factorint(J))
