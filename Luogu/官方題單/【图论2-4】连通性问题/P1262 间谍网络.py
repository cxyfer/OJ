"""
P1262 间谍网络
https://www.luogu.com.cn/problem/P1262
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
    N = int(input())
    P = int(input())
    A = []
    W = [float('inf')] * N
    for i in range(P):
        a, w = map(int, input().split())
        A.append(a - 1)
        W[a - 1] = w

    M = int(input())
    g = SCC(N)
    for _ in range(M):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)

    for u in A:
        if g.dfn[u] == -1:
            g.dfs(u)
    
    # 檢查是否連通
    for u in range(N):
        if g.dfn[u] == -1:
            print("NO")
            print(u + 1)
            return

    # 縮點，找出每個 SCC 的最小收買價格
    k = len(g.sccs)
    in_deg = [0] * k
    values = [float('inf')] * k
    for scc in g.sccs:
        for u in scc:
            i = g.scc_id[u]
            values[i] = min(values[i], W[u])
            for v in g.g[u]:
                j = g.scc_id[v]
                if i != j:
                    in_deg[j] += 1
    ans = 0
    for i in range(k):
        if in_deg[i] == 0:
            ans += values[i]
    
    print("YES")
    print(ans)

solve()