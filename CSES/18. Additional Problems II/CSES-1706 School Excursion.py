class UnionFind:
    def __init__(self, n):
        self.pa = [i for i in range(n)]
        self.sz = [1] * n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.sz[fx] > self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fx] = fy
        self.sz[fy] += self.sz[fx]

n, m = map(int, input().split())

uf = UnionFind(n)
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    uf.union(u, v)

arr = []
vis = [False] * n
for x in range(n):
    fx = uf.find(x)
    if vis[fx]:
        continue
    vis[fx] = True
    arr.append(uf.sz[fx])

# f = [False] * (n + 1)
# f[0] = True
# for x in arr:
#     for i in range(n, x - 1, -1):
#         f[i] |= f[i - x]

f = 1
for x in arr:
    f |= f << x

for i in range(1, n + 1):
    print("1" if f >> i & 1 else "0", end="")
print()