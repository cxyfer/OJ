"""
P2860 [USACO06JAN] Redundant Paths G
https://www.luogu.com.cn/problem/P2860
Tarjan 求 BCC
"""
class Tarjan:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.time = 0
        self.bridges = set()
        self.comp_id = [-1] * n
        self.bccs = []

    def add_edge(self, u: int, v: int):
        self.g[u].append(v)
        self.g[v].append(u)
    
    def dfs1(self, u: int, fa: int):
        self.dfn[u] = self.low[u] = self.time
        self.time += 1
        cnt = 0
        for v in self.g[u]:
            if v == fa:
                continue
            if self.dfn[v] != -1:
                self.low[u] = min(self.low[u], self.dfn[v])
            else:
                cnt += 1
                self.dfs1(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:
                    self.bridges.add((min(u, v), max(u, v)))

    def dfs2(self, u: int):
        self.comp_id[u] = len(self.bccs) - 1
        self.bccs[-1].append(u)
        for v in self.g[u]:
            if self.comp_id[v] != -1 or (min(u, v), max(u, v)) in self.bridges:
                continue
            self.dfs2(v)

    def run(self):
        for u in range(self.n):
            if self.dfn[u] == -1:
                self.dfs1(u, -1)
        for u in range(self.n):
            if self.comp_id[u] == -1:
                self.bccs.append([])
                self.dfs2(u)

def solve():
    n, m = map(int, input().split())
    g = Tarjan(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)

    g.run()
    deg = [0] * len(g.bccs)
    for u, v in g.bridges:
        deg[g.comp_id[u]] += 1
        deg[g.comp_id[v]] += 1
    
    k = sum(d == 1 for d in deg)
    print((k + 1) // 2)

solve()