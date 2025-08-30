"""
CF1000E We Need More Bosses
https://codeforces.com/problemset/problem/1000/E

如果 s, t 在同一個 BCC 中，則根據 BCC 的定義，s 到 t 至少有兩條完全不相交的路徑。
故同一個 BCC 中的兩點一定不可能對答案有貢獻。

考慮根據 BCC 縮點，得到一個樹，則最大的必經邊數量為這個樹的直徑。
"""
from collections import deque

class Tarjan:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]
        
        # --- Tarjan & BCC & v-BCC 相關 ---
        self.time = 0
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.bridges = set()
        self.bcc_id = [-1] * n
        self.bccs = []

    def add_edge(self, u: int, v: int):
        self.g[u].append(v)
        self.g[v].append(u)
    
    def dfs1(self, u: int, fa: int):
        """遞迴版本"""
        # self.dfn[u] = self.low[u] = self.time
        # self.time += 1
        # for v in self.g[u]:
        #     if v == fa:
        #         continue
        #     if self.dfn[v] != -1:
        #         self.low[u] = min(self.low[u], self.dfn[v])
        #     else:
        #         self.dfs1(v, u)
        #         self.low[u] = min(self.low[u], self.low[v])
        #         if self.low[v] > self.dfn[u]:  # bridge
        #             self.bridges.add((min(u, v), max(u, v)))
        """迭代版本"""
        st = [(u, fa, 0)]  # (u, fa, i)
        while st:
            u, fa, i = st.pop()
            if i == 0:
                self.dfn[u] = self.low[u] = self.time
                self.time += 1
            if i > 0:  # 處理 i - 1 的返回邏輯
                v = self.g[u][i-1]
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:  # bridge
                    self.bridges.add((min(u, v), max(u, v)))
            for j in range(i, len(self.g[u])):
                v = self.g[u][j]
                if v == fa:
                    continue
                if self.dfn[v] != -1:
                    self.low[u] = min(self.low[u], self.dfn[v])
                else:
                    st.append((u, fa, j + 1))
                    st.append((v, u, 0))
                    break
            else:
                pass

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
        for u in range(self.n):
            if self.bcc_id[u] == -1:
                self.bccs.append([])
                self.dfs2(u)

def solve():
    n, m = map(int, input().split())
    T = Tarjan(n)
    for _ in range(m):
        u, v = map(int, input().split())
        T.add_edge(u - 1, v - 1)
    
    T.run()

    k = len(T.bccs)
    g = [[] for _ in range(k)]
    for u, v in T.bridges:
        g[T.bcc_id[u]].append(T.bcc_id[v])
        g[T.bcc_id[v]].append(T.bcc_id[u])

    dist = [0] * k
    def bfs(u: int, fa: int):
        q = deque([(u, fa, 0)])
        while q:
            u, fa, d = q.popleft()
            dist[u] = d
            for v in g[u]:
                if v == fa:
                    continue
                q.append((v, u, d + 1))

    bfs(0, -1)
    u = dist.index(max(dist))
    bfs(u, -1)
    print(max(dist))

if __name__ == "__main__":
    solve()