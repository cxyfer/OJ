#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> tuple[int, int]:
            x = grid[i][j]
            if i == m - 1 and j == n - 1:
                return (x, x)
            mx, mn = float("-inf"), float("inf")
            if i + 1 < m:
                res1 = dfs(i + 1, j)
                if x >= 0:
                    mx = max(mx, x * res1[0], x * res1[1])
                    mn = min(mn, x * res1[1], x * res1[0])
                else:
                    mx = max(mx, x * res1[1], x * res1[0])
                    mn = min(mn, x * res1[0], x * res1[1])
            if j + 1 < n:
                res2 = dfs(i, j + 1)
                if x >= 0:
                    mx = max(mx, x * res2[0])
                    mn = min(mn, x * res2[1])
                else:
                    mx = max(mx, x * res2[1])
                    mn = min(mn, x * res2[0])
            return (mx, mn)

        ans = dfs(0, 0)[0]
        dfs.cache_clear()
        return ans % MOD if ans >= 0 else -1
# @lc code=end

