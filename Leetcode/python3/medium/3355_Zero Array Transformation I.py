#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        for i in range(n):
            if diff[i] < nums[i]:
                return False
            diff[i + 1] += diff[i]
        return True
# @lc code=end

