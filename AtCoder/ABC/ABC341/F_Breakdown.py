from collections import deque
from functools import cache

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
W = list(map(int, input().split()))
A = list(map(int, input().split()))
g = [[] for _ in range(N)]

for u, v in edges:
    u, v = u-1, v-1
    g[u].append(v)
    g[v].append(u)

def get_subset(u):
    res = []
    nodes = [v for v in g[u] if W[v] < W[u]]
    if not nodes:
        return []
    adj = sorted(nodes, key=lambda v: W[v])
    l, r = 0, 0
    s = 0
    while r < len(adj):
        s += W[adj[r]]
        while l < r and s >= W[u]:
            s -= W[adj[l]]
            l += 1
        if s >= W[u]:
            break
        r += 1
        res.append(adj[l:r])
    return res
subsets = [get_subset(i) for i in range(N)]

@cache
def DFS(u):
    res = 0
    for subset in subsets[u]:
        tmp = 0
        for v in subset:
            tmp += DFS(v)
        res = max(res, tmp)
    return 1 + res

f = [DFS(i) for i in range(N)]

ans = 0
for i in range(N):
    ans += f[i] * A[i]
print(ans)