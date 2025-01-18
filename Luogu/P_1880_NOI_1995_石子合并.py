from itertools import accumulate
from functools import cache

n = int(input())
A = list(map(int, input().split()))

A = A + A

s = list(accumulate(A, initial=0))
@cache
def dfs(l, r):
    if l == r:
        return 0, 0
    mx, mn = float('-inf'), float('inf')
    for i in range(l, r):
        l_mx, l_mn = dfs(l, i)
        r_mx, r_mn = dfs(i + 1, r)
        mx = max(mx, l_mx + r_mx + s[r + 1] - s[l])
        mn = min(mn, l_mn + r_mn + s[r + 1] - s[l])
    return mx, mn

mx, mn = float('-inf'), float('inf')
for i in range(n):
    r_mx, r_mn = dfs(i, i + n - 1)
    mx = max(mx, r_mx)
    mn = min(mn, r_mn)
print(mn, mx, sep="\n")