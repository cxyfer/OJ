from collections import defaultdict

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
    
n = int(input())
g = defaultdict(list)
deg = defaultdict(int)
uf = UnionFind(128) # ASCII
cnt = 0
for i in range(n):
    u, v = map(ord, input().strip()) # ASCII
    g[u].append((v, i))
    g[v].append((u, i))
    deg[u] += 1
    deg[v] += 1
    cnt += uf.union(u, v)

for u in g:
    g[u].sort()

odds = [u for u, val in deg.items() if val & 1]
if odds:
    st = min(odds)
else:
    st = min(g.keys())

path = []
used = [False] * n
def dfs(u):
    while g[u]:
        v, idx = g[u].pop(0) # 從 ASCII 小的先選
        if used[idx]:
            continue
        used[idx] = True
        dfs(v)
    path.append(u)

dfs(st)
root = uf.find(path[0]) if path else 0 # 避免 path 為空的情況
is_connected = all(uf.find(u) == root for u in g)
if len(odds) in [0, 2] and len(path) == n + 1 and is_connected:
    print(*map(chr, path[::-1]), sep='')
else:
    print("No Solution")