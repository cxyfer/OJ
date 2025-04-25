"""
【虾皮】20250423_3_购物车最优子集（Optimal Subset）
https://niumacode.com/problem/P1595
"""
from heapq import *

"""
【虾皮】20250423_3_购物车最优子集（Optimal Subset）
精確求出總價 ≤ M 的最大子集和
https://niumacode.com/problem/P1595
"""

n, M = map(int, input().split())
arr = list(map(int, input().split()))

tot = sum(arr)
if tot <= M:
    exit(print(tot))

f = 1
mask = (1 << (M + 1)) - 1
for v in arr:
    f |= (f << v)
    f &= mask

print(f.bit_length() - 1)