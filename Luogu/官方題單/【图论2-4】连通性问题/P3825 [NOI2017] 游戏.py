"""
P3825 [NOI2017] 游戏
https://www.luogu.com.cn/problem/P3825

P ⇒ Q 邏輯上等價於 ¬P ∨ Q，有以下兩個蘊含關係：
1. P ⇒ Q
2. ¬Q ⇒ ¬P

對於一個 x 地圖，與其枚舉「用哪輛車」，不如枚舉「禁用哪輛車」。
如果禁止使用賽車 A，那麼選擇就變成了 B 或 C，又回到了「二選一」的問題。
而考慮禁用 A 和 禁用 B 兩種情況，就能包含到所有的 3 種車，
因此枚舉 3 種車的哪種，不如枚舉禁用哪 2 種車。

其餘參考 P4782 【模板】2-SAT
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

    def reset(self):
        for u in range(self.n):
            self.g[u].clear()
        self.time = 0
        self.dfn = [-1] * self.n
        self.low = [-1] * self.n
        self.stk = []
        self.in_stk = [False] * self.n
        self.scc_id = [-1] * self.n
        self.scc_cnt = 0

def solve():
    n, d = map(int, input().split())
    s = input().strip()
    m = int(input())
    rules = []
    for _ in range(m):
        i, hi, j, hj = input().split()
        i, j = int(i) - 1, int(j) - 1
        rules.append((i, hi, j, hj))

    choices = [None] * n
    x_pos = []
    for i in range(n):
        if s[i] == 'a':
            choices[i] = ('B', 'C')
        elif s[i] == 'b':
            choices[i] = ('A', 'C')
        elif s[i] == 'c':
            choices[i] = ('A', 'B')
        else:
            x_pos.append(i)

    # (i, i + n) 分別代表在第 i 場比賽使用 choices[i][0] 和 choices[i][1]
    T = SCC(2 * n)
    for k in range(1 << d):
        for i, pos in enumerate(x_pos):
            if (k >> i) & 1:
                choices[pos] = ('A', 'B') # 禁用 C
            else:
                choices[pos] = ('B', 'C') # 禁用 A

        T.reset()
        for i, h_i, j, h_j in rules:
            ci, cj = choices[i], choices[j]

            # 如果規則要求的車 h_i 是第一種選項，那麼 P 對應節點 i， ¬P 對應節點 i + n
            if h_i == ci[0]:
                p, not_p = i, i + n
            elif h_i == ci[1]:
                p, not_p = i + n, i
            else:
                # P 不可能成立，因此 P ⇒ Q 一定成立
                continue

            if h_j == cj[0]:
                q, not_q = j, j + n
            elif h_j == cj[1]:
                q, not_q = j + n, j
            else:
                # Q 不可能成立，因此 P 需要不成立才能使 P ⇒ Q 成立
                # P 不成立可以用 P ⇒ ¬P 來限制，這意味著如果選了 P，那麼也要選 ¬P，這一定會導致矛盾
                T.add_edge(p, not_p)
                continue
            
            T.add_edge(p, q)
            T.add_edge(not_q, not_p)

        T.run()

        # 檢查是否有解
        if any(T.scc_id[i] == T.scc_id[i + n] for i in range(n)):
            continue

        # 在 選第一種車 (i) 和 選第二種車 (i + n) 中，優先選擇 scc_id 小，即拓撲序靠後的狀態
        ans = [c1 if T.scc_id[i] < T.scc_id[i + n] else c2 for i, (c1, c2) in enumerate(choices)]
        print("".join(ans))
        return

    print(-1)

if __name__ == "__main__":
    solve()
