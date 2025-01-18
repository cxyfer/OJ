#
# @lc app=leetcode id=2371 lang=python3
# @lcpr version=30204
#
# [2371] Minimize Maximum Value in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        rows = [1 for _ in range(n)] # rank
        cols = [1 for _ in range(m)] # rank

        nums = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                nums.append((x, i, j))

        nums.sort()
        for x, i, j in nums:
            val = max(rows[i], cols[j])
            grid[i][j] = val
            rows[i], cols[j] = val + 1, val + 1
        return grid
# @lc code=end



#
# @lcpr case=start
# [[3,1],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[10]]\n
# @lcpr case=end

#

