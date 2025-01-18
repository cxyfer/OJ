N, M = map(int, input().split())
A = list(map(int, input().split()))

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
    
edges = []
for i, x in enumerate(A):
    for j in range(i + 1, N):
        y = A[j]
        w = (pow(x, y, M) + pow(y, x, M)) % M
        edges.append((w, i, j))
edges.sort(reverse=True)

ans = 0
uf = UnionFind(N)
for (w, u, v) in edges:
    if uf.union(u, v):
        ans += w
        if uf.cnt == 1:
            break
print(ans)