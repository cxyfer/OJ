"""
【华为】20240410_2_相似图片分类
https://niumacode.com/problem/P1549
"""

class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'wt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))
        self.sz = [1] * n
        self.wt = [0] * n

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int, w: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        self.wt[fx] += w
        if fx == fy:
            return
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.wt[fx] += self.wt[fy]
    
n = int(input())
uf = UnionFind(n)

for i in range(n):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if i == j: continue
        if v > 0:
            uf.union(i, j, v)

ans = []
vis = [False] * n
for u in range(n):
    fu = uf.find(u)
    if vis[fu]: continue
    vis[fu] = True
    assert uf.wt[fu] % 2 == 0
    ans.append(uf.wt[fu] // 2)

print(*sorted(ans, reverse=True))
