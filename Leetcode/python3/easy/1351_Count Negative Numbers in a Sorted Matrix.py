#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # return sum(len(row) - bisect_right(row, 0, key = lambda x: -x) for row in grid)
        ans = 0
        for row in grid:
            idx = bisect_right(row, 0, key=lambda x: -x)
            ans += len(row) - idx
        return ans
# @lc code=end

