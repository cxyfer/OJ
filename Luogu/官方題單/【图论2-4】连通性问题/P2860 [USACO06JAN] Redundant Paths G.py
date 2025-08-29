"""
P2860 [USACO06JAN] Redundant Paths G
https://www.luogu.com.cn/problem/P2860
Tarjan 求 BCC
"""
class Tarjan:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]
        
        # --- Tarjan & BCC & v-BCC 相關 ---
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.stk = []
        self.time = 0
        self.bridges = set()
        self.bcc_id = [-1] * n
        self.bccs = []

    def add_edge(self, u: int, v: int):
        self.g[u].append(v)
        self.g[v].append(u)
    
    def dfs1(self, u: int, fa: int):
        """遞迴版本"""
        # self.dfn[u] = self.low[u] = self.time
        # self.time += 1
        # for v in self.g[u]:
        #     if v == fa:
        #         continue
        #     if self.dfn[v] != -1:
        #         self.low[u] = min(self.low[u], self.dfn[v])
        #     else:
        #         self.dfs1(v, u)
        #         self.low[u] = min(self.low[u], self.low[v])
        #         if self.low[v] > self.dfn[u]:  # bridge
        #             self.bridges.add((min(u, v), max(u, v)))
        """迭代版本"""
        st = [(u, fa, 0, 0)]  # (u, fa, i, cnt)
        while st:
            u, fa, i, cnt = st.pop()
            if i == 0:
                self.dfn[u] = self.low[u] = self.time
                self.time += 1
                self.stk.append(u)
            if i > 0:  # 處理 i - 1 的返回邏輯
                v = self.g[u][i-1]
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:  # bridge
                    self.bridges.add((min(u, v), max(u, v)))
            for j in range(i, len(self.g[u])):
                v = self.g[u][j]
                if v == fa:
                    continue
                if self.dfn[v] != -1:
                    self.low[u] = min(self.low[u], self.dfn[v])
                else:
                    st.append((u, fa, j + 1, cnt + 1))
                    st.append((v, u, 0, 0))
                    break

    def dfs2(self, u: int):
        """遞迴版本"""
        # self.comp_id[u] = len(self.bccs) - 1
        # self.bccs[-1].append(u)
        # for v in self.g[u]:
        #     if self.comp_id[v] != -1 or (min(u, v), max(u, v)) in self.bridges:
        #         continue
        #     self.dfs2(v)
        """迭代版本"""
        st = [u]
        while st:
            u = st.pop()
            self.bcc_id[u] = len(self.bccs) - 1
            self.bccs[-1].append(u)
            for v in self.g[u]:
                if self.bcc_id[v] != -1 or (min(u, v), max(u, v)) in self.bridges:
                    continue
                st.append(v)

    def run(self):
        for u in range(self.n):
            if self.dfn[u] == -1:
                self.dfs1(u, -1)
                self.stk.clear()
        for u in range(self.n):
            if self.bcc_id[u] == -1:
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
        deg[g.bcc_id[u]] += 1
        deg[g.bcc_id[v]] += 1
    
    k = sum(d == 1 for d in deg)
    print((k + 1) // 2)

solve()