# R12 r1: inspect the (ga)-data of Moebius ladder M12 found by r12_examples.py
import itertools, networkx as nx
from r11_inverse import try_W, build_manual
from r12_examples import allW, mob
G=mob(6)
for W in allW(G,'full'):
    P=try_W(G,W,'full'); M,Mc,A=build_manual(P)
    print('W',W,'N',A.number_of_nodes(),'pieces',P, 'iso M',nx.is_isomorphic(M,G))
