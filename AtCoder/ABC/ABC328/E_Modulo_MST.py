from atcoder.dsu import *
from itertools import *

N, M, K = map(int, input().split())

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v, w))

ans = float('inf')
for pattern in combinations(range(M), N-1):
    dsu = DSU(N) # Disjoint Set Union
    tmp = 0
    for i in pattern:
        u, v, w = edges[i]
        dsu.merge(u, v)
        tmp += w 
        tmp %= K
    if len(dsu.groups()) == 1:
        ans = min(ans, tmp % K)
print(ans)
