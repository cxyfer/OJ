#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#
from preImport import *
# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        @cache
        def dfs(t: int, j1: int, j2: int) -> int:
            if j1 < 0 or j2 < 0 or t < j1 or t < j2 or grid[t - j1][j1] < 0 or grid[t - j2][j2] < 0:
                return -float("inf")
            if t == 0:
                return grid[0][0]
            res = max(dfs(t - 1, j1, j2), dfs(t - 1, j1, j2 - 1), dfs(t - 1, j1 - 1, j2), dfs(t - 1, j1 - 1, j2 - 1))
            return res + grid[t - j1][j1] + (grid[t - j2][j2] if j2 != j1 else 0)
        return max(dfs(n * 2 - 2, n - 1, n - 1), 0)
# @lc code=end

