"""
P3469 [POI 2008] BLO-Blockade
https://www.luogu.com.cn/problem/P3469

注意移除的是與該點相鄰的邊，因此該點仍然會對答案產生貢獻。
"""
class Tarjan:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]
        
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.time = 0

        self.ans = [0] * n
        self.sz = [0] * n

    def add_edge(self, u: int, v: int):
        self.g[u].append(v)
        self.g[v].append(u)
        
    def dfs(self, u: int, fa: int):
        """遞迴版本"""
        # self.dfn[u] = self.low[u] = self.time
        # self.time += 1
        # self.sz[u] = 1 # 初始化子樹大小為 1 (包含 u 自己)
        # s = 0  # 被分割的子樹總大小
        # for v in self.g[u]:
        #     if v == fa:
        #         continue
        #     if self.dfn[v] != -1:
        #         self.low[u] = min(self.low[u], self.dfn[v])
        #     else:
        #         self.dfs(v, u)
        #         self.sz[u] += self.sz[v]
        #         self.low[u] = min(self.low[u], self.low[v])
        #         # 判斷 u 是否是割點，但這裡可以忽略根節點需要的額外判斷
        #         if self.low[v] >= self.dfn[u]:
        #             # 被分割的子樹貢獻
        #             self.ans[u] += self.sz[v] * (self.n - self.sz[v])
        #             s += self.sz[v]
        # # 剩餘分量貢獻：剩餘分量 = 總數 - u - 所有被分割的子樹
        # r = self.n - 1 - s
        # self.ans[u] += r * (self.n - r)
        # # 自身分量貢獻：u 自己形成一個大小為 1 的分量
        # self.ans[u] += 1 * (self.n - 1)
        """迭代版本"""
        st = [(u, fa, 0, 0)]  # (u, fa, i, s)
        while st:
            u, fa, i, s = st.pop()
            if i == 0:
                self.dfn[u] = self.low[u] = self.time
                self.time += 1
                self.sz[u] = 1
            if i > 0:  # 處理 i - 1 的返回邏輯
                v = self.g[u][i-1]
                self.low[u] = min(self.low[u], self.low[v])
                self.sz[u] += self.sz[v]
                if self.low[v] >= self.dfn[u]:
                    self.ans[u] += self.sz[v] * (self.n - self.sz[v])
                    s += self.sz[v]

            for j in range(i, len(self.g[u])):
                v = self.g[u][j]
                if v == fa:
                    continue
                if self.dfn[v] != -1:
                    self.low[u] = min(self.low[u], self.dfn[v])
                else:
                    st.append((u, fa, j + 1, s))
                    st.append((v, u, 0, 0))
                    break
            else:
                r = self.n - 1 - s
                self.ans[u] += r * (self.n - r)
                self.ans[u] += 1 * (self.n - 1)

    def run(self):
        # 題目保證圖連通，從 0 開始即可
        self.dfs(0, -1)

def solve():
    n, m = map(int, input().split())
    g = Tarjan(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u - 1, v - 1)
    g.run()
    print(*g.ans, sep='\n')

solve()