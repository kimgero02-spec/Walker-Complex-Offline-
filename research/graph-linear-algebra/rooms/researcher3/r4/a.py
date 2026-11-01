from g import *
for name,A in [('K3',K(3)),('K4',K(4)),('P4',P(4)),('C5',C(5)),('K2',K(2)),('K1',K(1)),
  ('K2box K2=C4',cart(K(2),K(2))),('prism K3box K2',cart(K(3),K(2))),('K3box K3',cart(K(3),K(3))),
  ('K3x K2',tens(K(3),K(2))),('P3box K2',cart(P(3),K(2))),('K2+K2',dsum(K(2),K(2)))]:
    print(name, Pg(A))
