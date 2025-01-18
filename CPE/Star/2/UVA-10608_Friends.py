class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n

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
        return True

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        uf.union(x, y)
    print(max(uf.sz))