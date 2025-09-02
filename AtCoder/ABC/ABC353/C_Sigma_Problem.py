"""
    注意數據範圍 Ai <= 10^8
    所以 f(Ai, Aj) = (Ai + Aj) % 10^8 其實只有兩種情況
    1. Ai + Aj < 10^8
    2. Ai + Aj >= 10^8 ，這時候 f(Ai, Aj) = Ai + Aj - 10^8
    先全部以第一種情況計算，再減去第二種情況的數量 * 10^8 即可

    暴力枚舉左端點會超時，要用Binary Search找到左端點
"""
from bisect import *
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = sum(A) * (N - 1) # 初始化答案
for r in range(1, N): # 枚舉右端點
    idx = bisect_left(A, 10**8 - A[r]) # 找到左端點
    if idx < r:
        ans -= (r - idx) * 10**8 # 減去第二種情況的數量
print(int(ans))