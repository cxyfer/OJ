"""
P2341 [USACO03FALL / HAOI2006] 受欢迎的牛 G
https://www.luogu.com.cn/problem/P2341

只有三種情況：
1. 只有一個 SCC，則答案為該 SCC 的大小
2. 縮點後，只有一個 SCC 的出度為 0，則答案為該 SCC 的大小
3. 剩餘情況，答案為 0
"""
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
        # self.dfn[u] = self.low[u] = self.time
        # self.time += 1
        # self.stk.append(u)
        # self.in_stk[u] = True
        # for v in self.g[u]:
        #     if self.dfn[v] == -1:
        #         self.dfs(v)
        #         self.low[u] = min(self.low[u], self.low[v])
        #     elif self.in_stk[v]:
        #         self.low[u] = min(self.low[u], self.dfn[v])
        # if self.dfn[u] == self.low[u]:
        #     scc = []
        #     while True:
        #         v = self.stk.pop()
        #         self.in_stk[v] = False
        #         self.scc_id[v] = len(self.sccs)
        #         scc.append(v)
        #         if v == u:
        #             break
        #     self.sccs.append(scc)
        """迭代版本"""
        st = [(u, 0)]  # (u, i)
        while st:
            u, i = st.pop()
            if i == 0:
                self.dfn[u] = self.low[u] = self.time
                self.time += 1
                self.stk.append(u)
                self.in_stk[u] = True
            if i > 0:  # 處理 i - 1 的返回邏輯
                v = self.g[u][i-1]
                self.low[u] = min(self.low[u], self.low[v])
            for j in range(i, len(self.g[u])):
                v = self.g[u][j]
                if self.dfn[v] == -1:
                    st.append((u, j + 1))
                    st.append((v, 0))
                    break
                elif self.in_stk[v]:
                    self.low[u] = min(self.low[u], self.dfn[v])
            else:
                if self.dfn[u] == self.low[u]:
                    scc = []
                    while True:
                        v = self.stk.pop()
                        self.in_stk[v] = False
                        self.scc_id[v] = len(self.sccs)
                        scc.append(v)
                        if v == u:
                            break
                    self.sccs.append(scc)

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
    if len(g.sccs) == 1:
        print(n)
    else:
        k = len(g.sccs)
        out_deg = [0] * k
        for i, scc in enumerate(g.sccs):
            for u in scc:
                for v in g.g[u]:
                    if i != g.scc_id[v]:
                        out_deg[i] += 1

        if out_deg.count(0) == 1:
            idx = out_deg.index(0)
            print(len(g.sccs[idx]))
        else:
            print(0)

solve()