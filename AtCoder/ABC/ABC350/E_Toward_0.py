"""
    DP
    令 f(x) 表示當前數字為 x 時的最小花費
    1. 選擇直接除以A： f(N) = f(N / A) + X
    2. 選擇骰骰子：f(N) = (f(N) + f(N / 2) + f(N / 3) + f(N / 4) + f(N / 5) + f(N / 6)) / 6 + Y
       整理得：f(N) = (f(N / 2) + f(N / 3) + f(N / 4) + f(N / 5) + f(N / 6) + 6Y ) / 5
"""
from functools import cache

N, A, X, Y = map(int, input().split())

@cache
def f(x):
    if not x:
        return 0
    res1 = f(x // A) + X
    res2 = (sum(f(x // i) for i in range(2, 7)) + 6 * Y) / 5
    return min(res1, res2)

print(f(N))