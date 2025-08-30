"""
P5782 [POI 2001] 和平委员会
https://www.luogu.com.cn/problem/P5782

把至少選一個代表改成恰好選一個代表，則為 2-SAT 問題。

令 (a, b) 所屬的黨派分別為 i, j，且同黨派的另外一位代表分別為 (a', b')，
則 (a, b) 不能同時出現等同於 P: i 黨派選擇 a' 作為代表、或 Q: j 黨派選擇 b' 作為代表
P ∨ Q 邏輯上等價於 ¬P ⇒ Q，有以下兩個蘊含關係：
1. ¬P ⇒ Q
2. ¬Q ⇒ P

用位運算可以獲取：
- a 所屬的黨派： a >> 1
- a' ：(a ^ 1)
- a 是第一位或第二位代表：a & 1 == 0/1

如果要維持與其他 2-SAT 題目的同樣寫法，可以把題目給定的 (i, i + 1) 轉換為 (i >> 1, (i >> 1) + n)。
不過直接對給定的 a, b 建圖更加直觀。
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
        a, b = map(lambda x: x - 1, map(int, input().split()))
        # i, j = a >> 1, b >> 1
        # x, y = (a & 1) ^ 1, (b & 1) ^ 1
        # # ¬P ⇒ Q
        # T.add_edge(i + n * (1 ^ x), j + n * y)
        # # ¬Q ⇒ P
        # T.add_edge(j + n * (1 ^ y), i + n * x)

        # P: 選 a ^ 1 作為代表、¬P: 選 a 作為代表
        # Q: 選 b ^ 1 作為代表、¬Q: 選 b 作為代表
        # ¬P ⇒ Q
        T.add_edge(a, b ^ 1)
        # ¬Q ⇒ P
        T.add_edge(b, a ^ 1)

    T.run()

    # if any(T.scc_id[i] == T.scc_id[i + n] for i in range(n)):
    if any(T.scc_id[i << 1] == T.scc_id[(i << 1) | 1] for i in range(n)):
        print("NIE")
        return

    # ans = [(i << 1) + 1 if T.scc_id[i] < T.scc_id[i + n] else (i << 1 | 1) + 1 for i in range(n)]
    ans = [(i << 1) + 1 if T.scc_id[i << 1] < T.scc_id[(i << 1) | 1] else (i << 1 | 1) + 1 for i in range(n)]
    print(*ans, sep="\n")

solve()