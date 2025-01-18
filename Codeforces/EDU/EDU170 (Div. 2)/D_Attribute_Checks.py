import sys
from bisect import *
from functools import cache

sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
R = list(map(int, input().split()))

checkpoints = [[] for _ in range(m + 1)] # current point -> queries
cur = 0
for r in R:
    if r == 0:
        cur += 1
    else:
        checkpoints[cur].append(r)

list_S = []
list_I = []
for queries in checkpoints:
    s, i = [], []
    for q in queries:
        if q > 0:
            s.append(q)
        else:
            i.append(-q)
    s.sort()
    i.sort()
    list_S.append(s)
    list_I.append(i)

@cache
def f(p, s): # p: current point, s: strength
    if p > m:
        return 0
    i = p - s # i: intelligence
    if i < 0 or i > m:
        return -float('inf')
    c = 0
    c += bisect_right(list_S[p], s) # Check Strength
    c += bisect_right(list_I[p], i) # Check Intelligence

    res1 = f(p + 1, s + 1) + c if s < m else -float('inf') # Allocate to Strength
    res2 = f(p + 1, s) + c if i < m else -float('inf') # Allocate to Intelligence
    return max(res1, res2)

print(f(0, 0))

# dp = [[-float('inf')] * (m + 1) for _ in range(m + 2)]
# dp[m + 1] = [0] * (m + 1)

# for p in range(m, -1, -1):
#     for s in range(m + 1):
#         i = p - s
#         if 0 <= i <= m:
#             c = bisect_right(list_S[p], s) + bisect_right(list_I[p], i)
#             res1 = dp[p + 1][s + 1] + c if s < m else -float('inf')
#             res2 = dp[p + 1][s] + c if i < m else -float('inf')
#             dp[p][s] = max(res1, res2)
# print(dp[0][0])