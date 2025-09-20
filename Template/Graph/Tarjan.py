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