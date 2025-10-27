#
# @lc app=leetcode id=3727 lang=python3
#
# [3727] Maximum Alternating Sum of Squares
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i, x in enumerate(nums):
            nums[i] *= x
        nums.sort()
        return sum(nums[n//2:]) - sum(nums[:n//2])
# @lc code=end

