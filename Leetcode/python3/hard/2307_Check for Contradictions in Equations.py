#
# @lc app=leetcode id=2307 lang=python3
#
# [2307] Check for Contradictions in Equations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class DSU:
    """
    帶權並查集
    維護條件：val(y) / val(x) = w

    支援：
    - union(x, y, w): 合併並加入約束 y - x = w
    - diff(x, y): 若同集合，回傳 y - x；否則回傳 None
    """

    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.sz = [1] * n
        # dis[x] = val(x) / val(fa[x])
        self.dis = [1] * n

    def find(self, x: int) -> int:
        """回傳 x 的根，同時做路徑壓縮並更新 dis[x] 為 x 到根的位勢差。"""
        fa = self.fa
        if fa[x] != x:
            rt = self.find(fa[x])
            self.dis[x] *= self.dis[fa[x]]
            fa[x] = rt
        return fa[x]

    def union(self, x: int, y: int, w: int) -> bool:
        """
        合併並加入約束：val(y) / val(x) = w
        回傳：
        - True：成功合併（或已同集合且不發生矛盾）
        - False：已同集合但發生矛盾
        """
        rx, ry = self.find(x), self.find(y)
        dx, dy = self.dis[x], self.dis[y]
        if rx == ry:
            # x 和 y 在同一集合，不做合併
            # return (dy / dx) == w
            return abs(dy - dx * w) <= 1e-5

        if self.sz[rx] < self.sz[ry]:  # fa[rx] = ry
            # rx <------- ry
            # |           |
            # | dx        | dy
            # ↓           ↓
            # x --------> y
            # => pot(rx) - pot(ry) = dy - w - dx
            self.fa[rx] = ry
            self.dis[rx] = dy / w / dx
            self.sz[ry] += self.sz[rx]
        else:  # fa[ry] = rx
            # rx -------> ry
            # |           |
            # | dx        | dy
            # ↓     w     ↓
            # x --------> y
            # => pot(ry) - pot(rx) = w - dy + dx
            self.fa[ry] = rx
            self.dis[ry] = w / dy * dx
            self.sz[rx] += self.sz[ry]

        return True

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        mp = dict()
        for equation in equations:
            for var in equation:
                if var not in mp:
                    mp[var] = len(mp)

        m = len(mp)
        uf = DSU(m)
        for (a, b), val in zip(equations, values):
            if not uf.union(mp[b], mp[a], val):
                return True
        return False
# @lc code=end

[["a","b"],["b","c"],["a","c"]]
[3,0.5,1.5]

sol = Solution()
print(sol.checkContradictions([["a","b"],["b","c"],["a","c"]], [3,0.5,1.5]))