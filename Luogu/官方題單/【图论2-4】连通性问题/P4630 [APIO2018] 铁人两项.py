"""
P4630 [APIO2018] 铁人两项
https://www.luogu.com.cn/problem/P4630
Tarjan 求 v-BCC & Block-Cut Tree
在 Block-Cut Tree 上跑樹形 DP 計算貢獻

拚盡全力還是 TLE 了兩個點，96/100
"""
from collections import deque

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
        self.cut_vertices = [False] * n

        # --- 圓方樹 (Block-Cut Tree) 相關 ---
        self.bct_sz = n
        self.bct = [[] for _ in range(2 * n)]
        self.weights = [-1] * n + [0] * n

    def add_edge(self, u: int, v: int):
        self.g[u].append(v)
        self.g[v].append(u)

    def add_bct_edge(self, u: int, v: int):
        self.bct[u].append(v)
        self.bct[v].append(u)
    
    def dfs1(self, u: int, fa: int):
        """遞迴版本"""
        # self.dfn[u] = self.low[u] = self.time
        # self.time += 1
        # self.stk.append(u)
        # cnt = 0
        # for v in self.g[u]:
        #     if v == fa:
        #         continue
        #     if self.dfn[v] != -1:
        #         self.low[u] = min(self.low[u], self.dfn[v])
        #     else:
        #         cnt += 1
        #         self.dfs1(v, u)
        #         self.low[u] = min(self.low[u], self.low[v])
        #         if self.low[v] > self.dfn[u]:  # bridge
        #             self.bridges.add((min(u, v), max(u, v)))
        #         if fa != -1 and self.low[v] >= self.dfn[u]:  # cut vertex
        #             self.cut_vertices[u] = True
        #         if self.low[v] >= self.dfn[u]:  # v-BCC & Block-Cut Tree
        #             s = self.bct_sz
        #             self.bct_sz += 1
                    
        #             # 從棧中彈出節點，它們都屬於這個 v-BCC
        #             vbcc_sz = 1
        #             self.add_bct_edge(s, u)
        #             while True:
        #                 w = self.stk.pop()
        #                 self.add_bct_edge(s, w)
        #                 vbcc_sz += 1
        #                 if w == v:
        #                     break
                    
        #             # 方點的權重是 v-BCC 的大小
        #             self.weights[s] = vbcc_sz
        # if fa == -1 and cnt > 1:  # cut vertex of root
        #     self.cut_vertices[u] = True
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
                if fa != -1 and self.low[v] >= self.dfn[u]:  # cut vertex
                    self.cut_vertices[u] = True
                if self.low[v] >= self.dfn[u]:  # v-BCC & Block-Cut Tree
                    s = self.bct_sz
                    self.bct_sz += 1
                    # 從棧中彈出節點，它們都屬於這個 v-BCC
                    vbcc_sz = 1
                    self.add_bct_edge(s, u)
                    while True:
                        w = self.stk.pop()
                        self.add_bct_edge(s, w)
                        vbcc_sz += 1
                        if w == v:
                            break
                    # 方點的權重是 v-BCC 的大小
                    self.weights[s] = vbcc_sz
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
            else:
                if fa == -1 and cnt > 1:  # cut vertex of root
                    self.cut_vertices[u] = True

    def run(self):
        for u in range(self.n):
            if self.dfn[u] == -1:
                self.dfs1(u, -1)
                self.stk.clear()

def solve():
    n, m = map(int, input().split())

    if n < 3:
        print(0)
        return

    T = Tarjan(n)
    for _ in range(m):
        u, v = map(int, input().split())
        T.add_edge(u - 1, v - 1)
    T.run()

    ans = 0
    vis = [False] * n
    for u in range(n):
        if vis[u]:
            continue
        # 1. 標記原圖中的連通分量，並計算大小
        # 這是因為原圖可能是不連通的，對於每個連通分量，我們需要分別計算貢獻
        vis[u] = True
        q = deque([u])
        comp_sz = 0
        while q:
            u = q.popleft()
            comp_sz += 1
            for v in T.g[u]:
                if vis[v]:
                    continue
                vis[v] = True
                q.append(v)
        if comp_sz < 2:
            continue

        # 2. 在 Block-Cut Tree 上跑樹形 DP 計算貢獻，f[u] 表示以 u 為根的子樹中圓點的數量

        """2.a. 遞迴版本"""
        # def f(u: int, fa: int) -> int:
        #     nonlocal ans
        #     sz = 1 if u < n else 0  # Block-Cut Tree 中以 u 為根的子樹中圓點的數量
        #     # 遍歷 u 的子節點
        #     for v in T.bct[u]:
        #         if v == fa:
        #             continue
        #         sz_v = f(v, u)
        #         # 節點 u 的貢獻：來自 v 子樹的圓點 與 u 子樹中其他已處理部分的圓點 構成的路徑
        #         # 每條路徑 (s,f) 和 (f,s) 都會經過 u，所以貢獻要乘以 2
        #         ans += T.weights[u] * sz_v * sz * 2
        #         sz += sz_v
        
        #     # 節點 u 的貢獻：來自 u 的整個子樹的圓點 與 子樹外的圓點 構成的路徑
        #     ans += T.weights[u] * sz * (comp_sz - sz) * 2
        #     return sz
        # f(u, -1)
        """2.b. 迭代版本，使用拓樸排序的方式計算"""
        order = []
        sz = [0] * T.bct_sz
        pa = [-1] * T.bct_sz
        q = deque([u])
        while q:
            u = q.popleft()
            order.append(u)
            for v in T.bct[u]:
                if v == pa[u]:
                    continue
                pa[v] = u
                q.append(v)
        
        for u in reversed(order):
            sz_u = 1 if u < n else 0
            fa = pa[u]
            for v in T.bct[u]:
                if v == fa:
                    continue
                sz_v = sz[v]
                # 計算貢獻：v 子樹中的圓點與 u 子樹中其他已處理部分的圓點
                ans += T.weights[u] * sz_v * sz_u * 2
                sz_u += sz_v
            # 計算貢獻：u 的整個子樹中的圓點與子樹外的圓點
            ans += T.weights[u] * sz_u * (comp_sz - sz_u) * 2
            sz[u] = sz_u
    
    print(ans)

solve()