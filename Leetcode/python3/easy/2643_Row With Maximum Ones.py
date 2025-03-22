#
# @lc app=leetcode id=2643 lang=python3
#
# [2643] Row With Maximum Ones
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        for i, row in enumerate(mat):
            s = sum(row)
            if s > ans[1]:
                ans = [i, s]
        return ans
# @lc code=end

