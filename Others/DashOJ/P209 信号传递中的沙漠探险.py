import sys
sys.setrecursionlimit(1 << 25)
from functools import cache

n = int(input())
x = list(map(float, input().split()))
a = list(map(float, input().split()))

tgt = 5

@cache
def dfs(i, j):
    if i == n- 1:
        return 1.0 if j == tgt else -float('inf')
    if j == tgt:
        return -float('inf')
    res = -float('inf')
    for k in range(i + 1, n):
        den = x[k] - x[i]
        if den == 0:
            continue
        res = max(res, (a[i] + a[k]) / den * dfs(k, j + 1))
    return res
ans = dfs(0, 1) if dfs(0, 1) != -float('inf') else 0.0
print("{0:.10f}".format(ans))