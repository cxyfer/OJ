import sys
from itertools import pairwise
sys.setrecursionlimit(int(7e6))

class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True
    
    def copy(self):
        other = UnionFind(len(self.pa))
        other.pa = self.pa[:]
        other.sz = self.sz[:]
        other.cnt = self.cnt
        return other

n, m, s = map(int, input().strip().split())

tot = 0
deg = [0] * (n + 1)
uf0 = UnionFind(n + 1)
for _ in range(m):
    u, v = map(int, input().strip().split())
    deg[u] += 1
    deg[v] += 1
    tot += abs(u - v)
    uf0.union(u, v)

answer = []
for i in range(1, n + 1):
    uf = uf0.copy()
    ans = tot
    deg[s] += 1
    deg[i] += 1

    # 連接奇數度的頂點
    odds = [u for u in range(1, n + 1) if deg[u] & 1]
    for j in range(0, len(odds), 2):
        x, y = odds[j], odds[j + 1]
        # 連接 (x, y) 邊的 cost 等同連接 (x, x + 1), (x + 1, x + 2), ... , (y - 1, y) 的邊
        # 但後者可以使更多頂點連通
        for k in range(x, y):
            uf.union(k, k + 1)
        ans += y - x

    nodes = [u for u in range(1, n + 1) if deg[u]]
    edges = []
    for x, y in pairwise(nodes):
        if uf.find(x) != uf.find(y):
            edges.append((x, y))
    edges.sort(key=lambda x: x[1] - x[0])
    for x, y in edges:
        if uf.union(x, y):
            ans += (y - x) << 1

    # print(ans, end=' ')
    answer.append(ans)
    deg[s] -= 1
    deg[i] -= 1

print(*answer)