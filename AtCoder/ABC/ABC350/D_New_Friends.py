"""
    Find size of each Connected Components
"""
class UnionFind:
    __slots__ = ['pa', 'size', 'count']

    def __init__(self, n: int):
        self.pa = list(range(n)) # 父節點
        self.size = [1] * n # 連通分量大小
        self.count = n # 連通分量數量

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.pa[py] = px
        self.size[px] += self.size[py]
        self.count -= 1
        return True
    
N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

ans = -M
visited = [False] * N
for i in range(N):
    pa = uf.find(i)
    if not visited[pa]:
        visited[pa] = True
        ans += uf.size[pa] * (uf.size[pa] - 1) // 2
print(ans)