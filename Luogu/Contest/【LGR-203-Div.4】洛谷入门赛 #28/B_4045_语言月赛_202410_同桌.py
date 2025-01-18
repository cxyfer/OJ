class UnionFind:
    def __init__(self, n):
        self.pa = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True if self.sz[px] <= 2 else False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.pa[py] = px
        self.sz[px] += self.sz[py]
        if self.sz[px] > 2:
            return False
        return True
    
n = int(input())
P = list(map(int, input().split()))

uf = UnionFind(2 * n + 1)

flag = True
for i, p in enumerate(P, 1):
    if i == p or not uf.union(i, p):
        flag = False
        break

print("Yes" if flag else "No")
    



