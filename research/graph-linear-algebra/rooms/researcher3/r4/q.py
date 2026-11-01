from g import *
def ratio(a,b):
    pa=Pg(C(a)); pb=Pg(C(b)); r=sp.factor(sp.cancel(pb/pa)); return r
for a,b in [(3,9),(4,8),(3,6),(3,12),(5,15),(2+1,3)]:
    print(a,b, ratio(a,b))
