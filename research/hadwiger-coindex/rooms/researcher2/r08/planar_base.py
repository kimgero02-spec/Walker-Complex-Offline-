import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_small import zig
from zig_dfs import zig_value
K23 = [(i, j) for i in range(2) for j in range(2, 5)]
print("zig(K_3) =", zig(3, [(0,1),(1,2),(0,2)]))
print("zig(K_4) =", zig(4, [(i,j) for i in range(4) for j in range(i+1,4)]))
print("zig(K_{2,3}) =", zig(5, K23))
print("zig(C_5) =", zig(5, [(i,(i+1)%5) for i in range(5)]))
print("zig(K_2) =", zig(2, [(0,1)]))
# outerplanar sample: fan F_4 = P_4 + K_1 (planar, outerplanar)
F = [(0,1),(1,2),(2,3),(3,4)] + [(4,i) for i in range(4)]
print("zig(fan on 5 vertices) =", zig(5, F))
