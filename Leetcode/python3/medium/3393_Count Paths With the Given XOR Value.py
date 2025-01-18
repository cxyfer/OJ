#
# @lc app=leetcode id=3393 lang=python3
# @lcpr version=30204
#
# [3393] Count Paths With the Given XOR Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = int(1e9 + 7)
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(x, y, val):
            if x == m - 1 and y == n - 1:
                return 1 if val == k else 0
            res = 0
            if x < m - 1:
                res += dfs(x + 1, y, val ^ grid[x + 1][y])
            if y < n - 1:
                res += dfs(x, y + 1, val ^ grid[x][y + 1])
            return res % MOD
        return dfs(0, 0, grid[0][0])
# @lc code=end



#
# @lcpr case=start
# [[2, 1, 5], [7, 10, 0], [12, 6, 4]]\n11\n
# @lcpr case=end

# @lcpr case=start
# [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]]\n10\n
# @lcpr case=end

#

