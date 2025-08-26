#
# @lc app=leetcode id=3000 lang=python3
#
# [3000] Maximum Area of Longest Diagonal Rectangle
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # return max((x * x + y * y, x * y) for x, y in dimensions)[1]
        max_d = ans = 0
        for x, y in dimensions:
            if x * x + y * y > max_d:
                max_d = x * x + y * y
                ans = x * y
            elif x * x + y * y == max_d:
                ans = max(ans, x * y)
        return ans
# @lc code=end

