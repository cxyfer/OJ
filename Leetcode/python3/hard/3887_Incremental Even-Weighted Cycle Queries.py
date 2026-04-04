#
# @lc app=leetcode id=3887 lang=python3
#
# [3887] Incremental Even-Weighted Cycle Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.sz = [1] * n
        # dis[x] = potential(x) ^ potential(fa[x])
        self.dis = [0] * n

    def find(self, x: int) -> int:
        fa = self.fa
        if fa[x] != x:
            rt = self.find(fa[x])
            self.dis[x] ^= self.dis[fa[x]]
            fa[x] = rt
        return fa[x]

    def union(self, x: int, y: int, w: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        dx, dy = self.dis[x], self.dis[y]
        if rx == ry:
            # x 和 y 在同一集合，不做合併
            return (dy ^ dx) == w

        if self.sz[rx] < self.sz[ry]:  # fa[rx] = ry
            # rx <------- ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y
            # => pot(rx) - pot(ry) = dy - w - dx
            self.fa[rx] = ry
            self.dis[rx] = (dy ^ w ^ dx) % 2
            self.sz[ry] += self.sz[rx]
        else:  # fa[ry] = rx
            # rx -------> ry
            # |           |
            # | dx        | dy
            # ↓     w     ↓
            # x --------> y
            # => pot(ry) - pot(rx) = w - dy + dx
            self.fa[ry] = rx
            self.dis[ry] = w ^ dy ^ dx
            self.sz[rx] += self.sz[ry]

        return True


class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        ans = 0
        for u, v, w in edges:
            if uf.union(u, v, w):
                ans += 1
        return ans
# @lc code=end
