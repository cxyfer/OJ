#
# @lc app=leetcode id=3148 lang=python3
# @lcpr version=30204
#
# [3148] Maximum Difference Score in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i: int, j: int): # 以 (i, j) 為終點，其起點的最小值
            if i < 0 or j < 0:
                return float("inf")
            return min(dfs(i - 1, j), dfs(i, j - 1), grid[i][j])
        ans = -float("inf")
        for r in range(m):
            for c in range(n):
                ans = max(ans, grid[r][c] - min(dfs(r - 1, c), dfs(r, c - 1)))
        return ans
# @lc code=end

sol = Solution()
print(sol.maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]])) # 9
print(sol.maxScore([[4,3,2],[3,2,1]])) # -1



#
# @lcpr case=start
# [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,2],[3,2,1]]\n
# @lcpr case=end

#

