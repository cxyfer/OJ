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

t = int(input())
for _ in range(t):
    n, m1, m2 = map(int, input().split())
    edges1 = []
    for _ in range(m1):
        u, v = map(lambda x: int(x) - 1, input().split())
        edges1.append((u, v))
    edges2 = []
    for _ in range(m2):
        u, v = map(lambda x: int(x) - 1, input().split())
        edges2.append((u, v))

    uf2 = UnionFind(n)
    for u, v in edges2:
        uf2.union(u, v)

    ans = 0
    uf1 = UnionFind(n)
    for (u, v) in edges1:
        if uf2.find(u) != uf2.find(v):  # 刪除這條邊
            ans += 1
        else:
            uf1.union(u, v)

    # 將 G 的連通分量分組
    comps = defaultdict(list)
    for u in range(n):
        comps[uf2.find(u)].append(u)

    for _, nodes in comps.items():
        # G 的這個連通分量，在 F 中被分成了 len(nodes) 個連通分量，需要將其連接起來
        roots = set()
        for u in nodes:
            roots.add(uf1.find(u))
        cost = len(roots)
        if cost > 1:
            ans += (cost - 1)

    print(ans)