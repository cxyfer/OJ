import sys
sys.setrecursionlimit(int(2e4))

class SCC:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]
        
        # --- Tarjan & SCC 相關 ---
        self.time = 0
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.stk = []
        self.in_stk = [False] * n
        self.scc_id = [-1] * n
        self.sccs = []

    def add_edge(self, u: int, v: int):
        self.g[u].append(v)
    
    def dfs(self, u: int):
        """遞迴版本"""
        self.dfn[u] = self.low[u] = self.time
        self.time += 1
        self.stk.append(u)
        self.in_stk[u] = True
        for v in self.g[u]:
            if self.dfn[v] == -1:
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.in_stk[v]:
                self.low[u] = min(self.low[u], self.dfn[v])
        if self.dfn[u] == self.low[u]:
            scc = []
            while True:
                v = self.stk.pop()
                self.in_stk[v] = False
                scc.append(v)
                if v == u:
                    break
            self.sccs.append(scc)
        """迭代版本"""
        # st = [(u, 0)]  # (u, i)
        # while st:
        #     u, i = st.pop()
        #     if i == 0:
        #         self.dfn[u] = self.low[u] = self.time
        #         self.time += 1
        #         self.stk.append(u)
        #         self.in_stk[u] = True
        #     if i > 0:  # 處理 i - 1 的返回邏輯
        #         v = self.g[u][i-1]
        #         self.low[u] = min(self.low[u], self.low[v])
        #     for j in range(i, len(self.g[u])):
        #         v = self.g[u][j]
        #         if self.dfn[v] == -1:
        #             st.append((u, j + 1))
        #             st.append((v, 0))
        #             break
        #         elif self.in_stk[v]:
        #             self.low[u] = min(self.low[u], self.dfn[v])
        #     else:
        #         if self.dfn[u] == self.low[u]:
        #             scc = []
        #             while True:
        #                 v = self.stk.pop()
        #                 self.in_stk[v] = False
        #                 scc.append(v)
        #                 if v == u:
        #                     break
        #             self.sccs.append(scc)

    def run(self):
        for u in range(self.n):
            if self.dfn[u] == -1:
                self.dfs(u)

def solve():
    n, m = map(int, input().split())
    g = SCC(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)
    g.run()
    ans = 0
    for scc in g.sccs:
        ans += len(scc) > 1
    print(ans)

solve()