#
# @lc app=leetcode id=3643 lang=python3
#
# [3643] Flip Square Submatrix Vertically
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        ans = [[x for x in row] for row in grid]
        for i in range(x, x + k):
            for j in range(y, y + k):
                ans[i][j] = grid[(x + k - 1) - (i - x)][j]
        return ans
# @lc code=end

