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
        for i in range(k // 2):
            row1 = grid[x + i]
            row2 = grid[x + k - 1 - i]
            row1[y:y+k], row2[y:y+k] = row2[y:y+k], row1[y:y+k]
        return grid
# @lc code=end

