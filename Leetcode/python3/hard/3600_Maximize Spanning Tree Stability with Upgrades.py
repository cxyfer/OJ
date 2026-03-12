#
# @lc app=leetcode id=3600 lang=python3
#
# [3600] Maximize Spanning Tree Stability with Upgrades
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
最大化最小值 -> 二分
"""
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

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
        self.cnt -= 1
        return True

    def copy(self):
        uf = UnionFind(self.n)
        uf.pa = self.pa.copy()
        uf.sz = self.sz.copy()
        uf.cnt = self.cnt
        return uf

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf0 = UnionFind(n)

        for u, v, _, must in edges:
            if must and not uf0.union(u, v):
                return -1

        def check(mid: int) -> bool:
            uf = uf0.copy()
            for u, v, w, must in edges:
                if must and w < mid:
                    return False
                # 必須先使用不需代價的邊
                elif not must and w >= mid:
                    uf.union(u, v)
            cost = 0
            for u, v, w, must in edges:
                # 因為 k 可能為 0，所以這個檢查不能寫在 cost += 1 後面
                if cost == k or uf.cnt == 1:
                    break
                if not must and w < mid and 2 * w >= mid:
                    if uf.union(u, v):
                        cost += 1
            return uf.cnt == 1

        mn = min(w for _, _, w, _ in edges)
        mx = max(w for _, _, w, _ in edges)
        left, right = mn, mx * 2
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right if right >= mn else -1
# @lc code=end
sol = Solution()
print(sol.maxStability(3, [[0,1,2,1],[1,2,3,0]], 1))  # 2
print(sol.maxStability(3, [[0,1,4,0],[1,2,3,0],[0,2,1,0]], 2))  # 6

print(sol.maxStability(3, [[0,1,55839,0],[0,2,39867,0],[1,2,62840,0]], 1))  # 62840