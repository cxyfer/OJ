"""
E. 小L的空投
https://ac.nowcoder.com/acm/contest/120566/E

正難則反
按照順序處理每個連通分量中存活的城市很困難，但可以逆序處理，
將所有城市都視為消失，然後逐個加入城市，計算連通分量中存活的城市數量。
"""


class UnionFind:
    __slots__ = ["pa", "sz"]

    def __init__(self, n: int):
        self.pa = list(range(n))
        self.sz = [1] * n

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        return True


def solve():
    n, m, x, d = map(int, input().split())
    A = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append(v)
        g[v].append(u)
    H = [int(input()) for _ in range(x)]

    idxs = sorted(range(n), key=lambda i: A[i], reverse=True)

    uf = UnionFind(n)
    active = [False] * n
    cur = 0  # 大小 >= d 的連通分量數量

    def merge(u, v):
        nonlocal cur
        fu, fv = uf.find(u), uf.find(v)
        if fu == fv:
            return
        # 合併前先減去兩個連通分量對答案的貢獻
        cur -= uf.sz[fu] >= d
        cur -= uf.sz[fv] >= d
        # 合併
        uf.union(u, v)
        # 合併後，更新新的連通分量對答案的貢獻
        cur += uf.sz[uf.find(u)] >= d

    ans = []
    i = 0
    for h in reversed(H):  # 逆序處理
        # 處理在當前高度下，可以存活的城市
        while i < n and A[idxs[i]] > h:
            u = idxs[i]
            i += 1
            active[u] = True
            if d == 1:  # 特殊處理 d=1 的特殊情況
                cur += 1
            for v in g[u]:
                if active[v]:
                    merge(u, v)
        ans.append(cur)

    ans.reverse()
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
