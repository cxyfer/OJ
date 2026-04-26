#
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
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

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        uf = UnionFind(n * m)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i > 0 and x == grid[i - 1][j]:
                    # 若加上這條邊之前就已經連通，則有環
                    # 由於網格圖中的環至少為 4，因此不用判斷環的大小
                    if not uf.union(i * m + j, (i - 1) * m + j):
                        return True
                if j > 0 and x == grid[i][j - 1]:
                    if not uf.union(i * m + j, i * m + j - 1):
                        return True
        return False
# @lc code=end

sol = Solution()
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
print(sol.containsCycle(grid))  # true
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
print(sol.containsCycle(grid))  # true
grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
print(sol.containsCycle(grid))  # false
grid = [["b","a","c"],["c","a","c"],["d","d","c"],["b","c","c"]]
print(sol.containsCycle(grid))  # false