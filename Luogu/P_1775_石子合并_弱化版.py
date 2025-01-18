from itertools import accumulate
from functools import cache

n = int(input())
A = list(map(int, input().split()))

s = list(accumulate(A, initial=0))
@cache
def dfs(l, r):
    if l == r:
        return 0
    res = float('inf')
    for i in range(l, r):
        res = min(res, dfs(l, i) + dfs(i + 1, r) + s[r + 1] - s[l])
    return res

print(dfs(0, n - 1))
