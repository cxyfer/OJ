class UnionFind:
    def __init__(self, n, nums):
        self.pa = list(range(n))
        self.sz = [1] * n
        self.tot = nums
 
    def find(self, x):
        # if self.pa[x] != x:
        #     self.pa[x] = self.find(self.pa[x])
        # return self.pa[x]
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x
     
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if fx < fy:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.tot[fx] += self.tot[fy]
 
    def get(self, x):
        return self.tot[self.find(x)] / self.sz[self.find(x)]
 
n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
 
uf = UnionFind(n + 1, A)

for _ in range(m):
    op, *args = map(int, input().split())
    if op == 1:
        l, r = args
        idx = uf.find(l)
        while idx < r:
            uf.union(idx, idx + 1)
            idx = uf.find(idx)
    else:
        i = args[0]
        print(f"{uf.get(i):.10f}")