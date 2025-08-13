import sys
sys.setrecursionlimit(int(1e5))
from functools import cache

N, M = map(int, input().split())
MOD = int(1e9 + 7)

@cache
def dfs(i, j, k):
    if i == 0:
        return 1 if j > 0 and j == k else 0
    if j == 0 or j < k:
        return 0
    res = 0
    if (k << 1) <= j:
        res += dfs(i - 1, j, k << 1)
    if k > 0:
        res += dfs(i, j - 1, k - 1)
    return res % MOD
print(dfs(N, M, 2))