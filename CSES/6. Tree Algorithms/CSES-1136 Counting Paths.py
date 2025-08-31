"""
CSES-1136 Counting Paths
https://cses.fi/problemset/task/1136/

TLE
"""
from typing import List

class LCA:
    def __init__(self, g: List[List[int]]):
        n = len(g)
        self.m = m = n.bit_length()

        dep = [0] * n
        pa = [[-1] * m for _ in range(n)]  # pa[u][i] 表示 u 的第 2^i 個祖先
        def dfs(u: int, fa: int) -> None:
            """遞迴寫法"""
            # pa[u][0] = fa
            # for v in g[u]:
            #     if v == fa:
            #         continue
            #     dep[v] = dep[u] + 1
            #     dfs(v, u)
            """非遞迴寫法"""
            st = [(u, fa, 0)]  # (u, fa, i)
            while st:
                u, fa, i = st.pop()
                if i == 0:
                    pa[u][0] = fa
                for j in range(i, len(g[u])):
                    v = g[u][j]
                    if v == fa:
                        continue
                    dep[v] = dep[u] + 1
                    st.append((u, fa, j + 1))
                    st.append((v, u, 0))
                    break
        dfs(0, -1)

        # 用倍增法更新 pa
        for i in range(m - 1):
            for u in range(n):
                if pa[u][i] != -1:
                    pa[u][i + 1] = pa[pa[u][i]][i]

        self.dep = dep
        self.pa = pa

    # 返回 u 的第 k 個祖先
    def get_kth_ancestor(self, u: int, k: int) -> int:
        # for i in range(k.bit_length()):
        #     if k >> i & 1:
        #         u = self.pa[u][i]
        while k and u != -1:  # 當 u 被更新成 -1 後，可能會訪問到錯誤的位置，提前退出
            lb = k & -k
            u = self.pa[u][lb.bit_length() - 1]
            k &= k - 1
        return u

    # 返回 u 和 v 的 LCA
    def get_lca(self, u: int, v: int) -> int:
        if self.dep[u] > self.dep[v]:
            u, v = v, u
        # 使 v 和 u 在同一深度
        v = self.get_kth_ancestor(v, self.dep[v] - self.dep[u])
        if v == u:
            return u
        for i in range(self.m - 1, -1, -1):
            fu, fv = self.pa[u][i], self.pa[v][i]
            if fu != fv:  # 同時往上跳 2^i 步後還不會相遇
                u, v = fu, fv
        return self.pa[u][0]  # 再往上跳一步就是答案

    # 返回 u 到 v 的距離
    def get_dis(self, u: int, v: int) -> int:
        return self.dep[u] + self.dep[v] - self.dep[self.get_lca(u, v)] * 2

def solve():
    n, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
    lca = LCA(g)

    f = [0] * n
    for _ in range(q):
        u, v = map(lambda x: int(x) - 1, input().split())
        f[u] += 1
        f[v] += 1
        z = lca.get_lca(u, v)
        f[z] -= 1
        if z != 0:
            f[lca.pa[z][0]] -= 1

    def dfs(u: int, fa: int) -> None:
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     dfs(v, u)
        #     f[u] += f[v]
        st = [(u, fa, 0)]  # (u, fa, i)
        while st:
            u, fa, i = st.pop()
            if i > 0:
                v = g[u][i - 1]
                f[u] += f[v]
            for j in range(i, len(g[u])):
                v = g[u][j]
                if v == fa:
                    continue
                st.append((u, fa, j + 1))
                st.append((v, u, 0))
                break
    dfs(0, -1)
    print(*f)
    return

if __name__ == "__main__":
    solve()