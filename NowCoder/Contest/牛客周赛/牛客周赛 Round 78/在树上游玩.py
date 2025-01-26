from collections import *

class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.pa[py] = px
        self.sz[px] += self.sz[py]
        self.cnt -= 1
        return True

MOD = int(1e9 + 7)
n, k = map(int, input().split())
marks = set(map(lambda x: int(x) - 1, input().split()))
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

uf = UnionFind(n)

for u, v in edges:
    if u in marks and v in marks:
        uf.union(u, v)

reds = [[] for _ in range(n)]
for u in range(n):
    if u in marks:
        reds[uf.find(u)].append(u)
comps = []
for u in range(n):
    if len(reds[u]) > 0:
        comps.append(reds[u])
    
cnt = [0] * n
for u, v in edges:
    if u in marks and v not in marks:
        cnt[uf.find(u)] += 1
    elif v in marks and u not in marks:
        cnt[uf.find(v)] += 1

ans = 1
for u in range(n):
    if cnt[u] > 0:
        ans = ans * cnt[u] % MOD
print(len(comps), ans)