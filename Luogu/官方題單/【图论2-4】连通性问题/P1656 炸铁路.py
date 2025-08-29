"""
P1656 炸铁路
https://www.luogu.com.cn/problem/P1656
Tarjan 求 bridge
"""

class Tarjan:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.time = 0
        self.bridges = set()

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

    def run(self):
        for u in range(self.n):
            if self.dfn[u] == -1:
                self.dfs1(u, -1)

def solve():
    n, m = map(int, input().split())
    g = Tarjan(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)
    g.run()
    bridges = sorted(list(g.bridges))
    for u, v in bridges:
        print(u + 1, v + 1)

solve()