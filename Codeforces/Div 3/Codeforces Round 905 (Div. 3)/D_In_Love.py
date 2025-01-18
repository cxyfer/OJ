"""
    MultiSet + 貪心 + Heap
    C++ 的 STL 有 multiset，可以直接過
"""
from collections import Counter
from heapq import *

Q = int(input())

L = Counter()
R = Counter()
hp_l = [] # max heap
hp_r = [] # min heap

ans = []
flag = False
for _ in range(Q):
    op, l, r = input().split()
    l, r = map(int, (l, r))

    if op == '+':
        L[l] += 1
        R[r] += 1
        if L[l] == 1:
            heappush(hp_l, -l) # max heap
        if R[r] == 1:
            heappush(hp_r, r) # min heap
    else:
        L[l] -= 1
        R[r] -= 1
    
    # 移除已經不存在的元素
    while hp_l and L[-hp_l[0]] == 0: 
        heappop(hp_l)
    while hp_r and R[hp_r[0]] == 0: 
        heappop(hp_r)
    
    if hp_l and hp_r and hp_r[0] < -hp_l[0]:
        print("YES")
    else:
        print("NO")