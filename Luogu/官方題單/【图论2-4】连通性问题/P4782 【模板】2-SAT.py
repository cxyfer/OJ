"""
P4782 【模板】2-SAT
https://www.luogu.com.cn/problem/P4782

將 (xi == x) or (xj == y) 轉換為：
1. NOT (xi == x) => (xj == y)
2. NOT (xj == y) => (xi == x)

在 c1: x_i 為假 (i) 和 c2: x_i 為真 (i + n) 中，優先選擇 scc_id 小，即拓撲序靠後的狀態。
假設存在一條由 SCC(i + n) 到 SCC(i) 的路徑，這意味著如果選擇 c2，那麼將選擇一系列狀態，最終必須選擇 c1，這顯然是矛盾的。
也就是說，在縮點後的樹上，如果存在一條由 c2 到 c1 的路徑，那麼在 c1 和 c2 中，我們只能選擇 c1，反之亦然。
而判定是否存在一條由 SCC(c2) 到 SCC(c1) 的路徑可以由拓樸序來判定，
拓樸排序後，SCC(c1) 的拓樸序一定比 SCC(c2) 還要靠後，因此若兩點間存在一條有向路徑，則拓樸序靠後的點必是終點。
在 Tarjan 中，由於添加到 SCCs 中的順序是逆拓樸序，因此 scc_id 越小，拓樸序越大。
故選擇 scc_id 小的狀態，即拓樸序靠後的狀態，可以保證不選擇到矛盾的狀態。

Python 應該過不了，但 C++ 可以過
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
        self.scc_cnt = 0

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
                    while True:
                        v = self.stk.pop()
                        self.in_stk[v] = False
                        self.scc_id[v] = self.scc_cnt
                        if v == u:
                            break
                    self.scc_cnt += 1

    def run(self):
        for u in range(self.n):
            if self.dfn[u] == -1:
                self.dfs(u)

def solve():
    n, m = map(int, input().split())
    T = SCC(2 * n)  # 2 * n 個節點，(i, i + n) 分別代表 x_i 為假和 x_i 為真
    for _ in range(m):
        i, x, j, y = map(int, input().split())
        i -= 1
        j -= 1
        # NOT (x_i = x) => (x_j = y)
        T.add_edge(i + n * (1 - x), j + n * y)
        # NOT (x_j = y) => (x_i = x)
        T.add_edge(j + n * (1 - y), i + n * x)

    T.run()

    for i in range(n):
        # 如果 x_i 為假和 x_i 為真在同一個 SCC 中，則無解
        if T.scc_id[i] == T.scc_id[i + n]:
            print("IMPOSSIBLE")
            return

    print("POSSIBLE")
    ans = [-1] * n
    for i in range(n):
        # 在 x_i 為假 (i) 和 x_i 為真 (i + n) 中，優先選擇 scc_id 小，即拓撲序靠後的狀態
        ans[i] = 0 if T.scc_id[i] < T.scc_id[i + n] else 1
    
    print(*ans)

if __name__ == "__main__":
    solve()

