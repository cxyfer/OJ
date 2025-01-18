import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.cnt = n
        self.mx = 1

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
        self.mx = max(self.mx, self.sz[fx])
        return True

n, m = map(int, input().split())

uf = UnionFind(n)

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    uf.union(u, v)
    print(f"{uf.cnt} {uf.mx}")