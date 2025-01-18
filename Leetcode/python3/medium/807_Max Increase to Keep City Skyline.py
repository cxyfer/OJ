#
# @lc app=leetcode id=807 lang=python3
# @lcpr version=30204
#
# [807] Max Increase to Keep City Skyline
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_mx = [max(row) for row in grid]
        col_mx = [max([grid[i][j] for i in range(n)]) for j in range(n)]
        ans = 0
        for i, row in enumerate(grid):
            for j, h in enumerate(row):
                ans += min(row_mx[i], col_mx[j]) - h
        return ans
# @lc code=end



#
# @lcpr case=start
# [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[0,0,0],[0,0,0]]\n
# @lcpr case=end

#

