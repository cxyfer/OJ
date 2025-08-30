"""
776D - The Door Problem
https://codeforces.com/contest/776/problem/D

每個門有兩個開關，令 P 表示第一個開關為開啟狀態、Q 表示第二個開關為開啟狀態。
- 如果門本來是關閉的，則需要滿足 (¬P ∧ Q) ∨ (P ∧ ¬Q)
  - 換句話說，如果第一個開關為關閉狀態，則第二個開關必需為開啟狀態，反之同理
  - 得到 ¬P ⇔ Q 和 ¬Q ⇔ P 兩個蘊含關係
- 如果門本來是開啟的，則需要滿足 (P ∧ Q) ∨ (¬P ∧ ¬Q)
  - 得到 P ⇔ Q 和 ¬Q ⇔ ¬P 兩個蘊含關係
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
    R = list(map(int, input().split()))
    switchs = [[] for _ in range(n)]
    for i in range(m):
        X = list(map(int, input().split()))[1:]
        for x in X:
            switchs[x-1].append(i)

    T = SCC(2 * m)  # (i, i + m) 分別代表開關 i 的是關閉和開啟
    assert len(switchs) == n
    assert all(len(s) == 2 for s in switchs)
    for i, (u, v) in enumerate(switchs):
        if R[i] == 0:
            T.add_edge(u, v + m)
            T.add_edge(v + m, u)
            T.add_edge(v, u + m)
            T.add_edge(u + m, v)
        else:
            T.add_edge(u + m, v + m)
            T.add_edge(v + m, u + m)
            T.add_edge(v, u)
            T.add_edge(u, v)

    T.run()

    if any(T.scc_id[i] == T.scc_id[i + m] for i in range(m)):
        print("NO")
    else:
        print("YES")

solve()