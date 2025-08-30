"""
P4171 [JSOI2010] 满汉全席
https://www.luogu.com.cn/problem/P4171

每個材料的作法只能是 h 或 m，且每個評審只有兩個要求，因此為 2-SAT 問題。

P ∨ Q 邏輯上等價於 ¬P ⇒ Q，有以下兩個蘊含關係：
1. ¬P ⇒ Q
2. ¬Q ⇒ P
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
        c1, c2 = input().split()
        i, j = int(c1[1:]) - 1, int(c2[1:]) - 1
        x, y = int(c1[0] == 'h'), int(c2[0] == 'h')

        # ¬P ⇒ Q
        T.add_edge(i + n * (1 ^ x), j + n * y)
        # ¬Q ⇒ P
        T.add_edge(j + n * (1 ^ y), i + n * x)

    T.run()

    if any(T.scc_id[i] == T.scc_id[i + n] for i in range(n)):
        print("BAD")
    else:
        print("GOOD")

t = int(input())
for _ in range(t):
    solve()