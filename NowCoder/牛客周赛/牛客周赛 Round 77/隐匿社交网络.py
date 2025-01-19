class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
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

t = int(input())

for _ in range(t):
    n = int(input())
    W = list(map(int, input().split()))

    M = max(W).bit_length()
    uf = UnionFind(n)
    mp = [[] for _ in range(M)]
    
    for i, w in enumerate(W):
        while w > 0:
            lb = w & -w
            mp[lb.bit_length() - 1].append(i)
            w ^= lb
    
    for b, accs in enumerate(mp):
        if len(accs) <= 1:
            continue
        u = accs[0]
        for v in accs:
            uf.union(u, v)

    ans = 0
    for i in range(n):
        ans = max(ans, uf.sz[uf.find(i)])
    print(ans)