#
# @lc app=leetcode id=1975 lang=python3
# @lcpr version=30204
#
# [1975] Maximum Matrix Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 0
        cnt = 0
        mn = float("inf")
        for row in matrix:
            for val in row:
                if val < 0:
                    cnt += 1
                    val = -val
                s += val
                mn = min(mn, val)
        return s - mn * 2 if cnt & 1 else s
# @lc code=end



#
# @lcpr case=start
# [[1,-1],[-1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[-1,-2,-3],[1,2,3]]\n
# @lcpr case=end

#

