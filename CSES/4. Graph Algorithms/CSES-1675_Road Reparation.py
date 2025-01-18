# import sys
# input = lambda: sys.stdin.readline().strip()
# print = lambda val: sys.stdout.write(str(val) + "\n")

# class UnionFind:
#     def __init__(self, n):
#         self.pa = list(range(n))
#         self.sz = [1] * n
#         self.cnt = n

#     def find(self, x):
#         if self.pa[x] != x:
#             self.pa[x] = self.find(self.pa[x])
#         return self.pa[x]

#     def union(self, x, y):
#         fx, fy = self.find(x), self.find(y)
#         if fx == fy:
#             return False
#         if self.sz[fx] < self.sz[fy]:
#             fx, fy = fy, fx
#         self.pa[fy] = fx
#         self.sz[fx] += self.sz[fy]
#         self.cnt -= 1
#         return True

# n, m = map(int, input().split())

# edges = []
# for _ in range(m):
#     u, v, w = map(int, input().split())
#     edges.append((u - 1, v - 1, w))

# edges.sort(key=lambda x: x[2])
# uf = UnionFind(n)
# ans = 0
# for u, v, w in edges:
#     if uf.union(u, v):
#         ans += w

# print(ans if uf.cnt == 1 else "IMPOSSIBLE")

import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")
from heapq import heappush, heappop

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))

ans = 0
cnt = 1
selected = [False] * n
hp = []
for v, w in g[0]:
    heappush(hp, (w, 0, v))
selected[0] = True

while hp and cnt < n:
    w, u, v = heappop(hp)
    if selected[v]:
        continue
    selected[v] = True
    cnt += 1
    ans += w
    for v, w in g[v]:
        if not selected[v]:
            heappush(hp, (w, v, v))

print(ans if cnt == n else "IMPOSSIBLE")