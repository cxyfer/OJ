#
# @lc app=leetcode id=2373 lang=python3
# @lcpr version=30201
#
# [2373] Largest Local Values in a Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n - 2):
            for j in range(n - 2):
                grid[i][j] = max(max(row[j:j + 3]) for row in grid[i:i + 3])
            del grid[i][n-2:]
        del grid[n-2:]
        return grid
# @lc code=end



#
# @lcpr case=start
# [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]\n
# @lcpr case=end

#

